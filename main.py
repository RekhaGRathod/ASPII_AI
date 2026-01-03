from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import os
import shutil
import uuid
import nltk
import pandas as pd
import assemblyai as aai
from nltk.sentiment import SentimentIntensityAnalyzer

# --------------------------------------------
# 🔧 Setup
# --------------------------------------------
nltk.download("vader_lexicon")
aai.settings.api_key = "c57f746912f54963b8c2d865aab671b7"  # Replace with your valid key
sia = SentimentIntensityAnalyzer()
app = FastAPI()

# Create temp folder if not exists
os.makedirs("temp", exist_ok=True)

# --------------------------------------------
# 📥 Upload + Analyze Video Endpoint
# --------------------------------------------
@app.post("/analyze/")
async def analyze_video(file: UploadFile = File(...)):
    temp_id = str(uuid.uuid4())
    video_path = f"temp/{temp_id}_{file.filename}"

    # Save file to temp folder
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Transcribe with speaker labels
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
        video_path,
        config=aai.TranscriptionConfig(speaker_labels=True)
    )

    # Map speakers
    speaker_map = {}
    speaker_roles = ["Interviewer", "Candidate"]
    role_index = 0

    for utt in transcript.utterances:
        spk = utt.speaker
        if spk not in speaker_map:
            speaker_map[spk] = speaker_roles[role_index] if role_index < len(speaker_roles) else f"Speaker {role_index+1}"
            role_index += 1

    # Extract Q&A pairs based on speaker transitions
    qa_pairs = []
    i = 0
    utts = transcript.utterances

    while i < len(utts) - 1:
        curr = utts[i]
        nxt = utts[i + 1]

        if speaker_map[curr.speaker] == "Interviewer" and speaker_map[nxt.speaker] == "Candidate":
            question = curr.text
            answer = nxt.text
            sentiment = sia.polarity_scores(answer)
            score = sentiment["compound"]
            sentiment_label = (
                "Positive" if score >= 0.05 else
                "Negative" if score <= -0.05 else
                "Neutral"
            )

            qa_pairs.append({
                "question": question,
                "answer": answer,
                "sentiment": sentiment_label,
                "score": score
            })
            i += 2  # Skip next since we just used it as answer
        else:
            i += 1

    # Save as CSV
    df = pd.DataFrame(qa_pairs)
    output_file = f"temp/{temp_id}_sentiment.csv"
    df.to_csv(output_file, index=False)

    return {
        "status": "done",
        "csv_file": output_file,
        "summary": {
            "total_pairs": len(df),
            "positive": int(df['sentiment'].value_counts().get("Positive", 0)),
            "neutral": int(df['sentiment'].value_counts().get("Neutral", 0)),
            "negative": int(df['sentiment'].value_counts().get("Negative", 0))
        }
    }

# --------------------------------------------
# 📊 (Optional) View Result as HTML Table
# --------------------------------------------
@app.get("/view-results/{file_name}", response_class=HTMLResponse)
def view_csv(file_name: str):
    path = f"temp/{file_name}"
    if not os.path.exists(path):
        return f"<h3>❌ File {file_name} not found!</h3>"
    
    df = pd.read_csv(path)
    return df.to_html(classes="table table-bordered", index=False)
