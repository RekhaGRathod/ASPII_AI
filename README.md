🎯 Candidate Selection Process using Video & Transcript Sentiment Analysis
📌 Project Overview

The Candidate Selection Process is an AI-driven system designed to assist recruiters and evaluators by objectively analyzing interview responses.
The system supports both interview videos and text-based transcripts, converts them into structured question–answer pairs, and applies sentiment analysis using NLTK to evaluate candidate responses.

This project demonstrates the practical application of Natural Language Processing (NLP) and AI-assisted decision support systems in recruitment.

🚀 Key Features

🎥 Supports interview video upload

📄 Supports direct transcript file upload

🧾 Automatically extracts Question–Answer (Q&A) pairs

🧠 Applies NLTK (VADER) sentiment analysis

📊 Generates sentiment labels and scores

📁 Outputs results in CSV / table format

🌐 Frontend integration for easy interaction

🔐 Secure and clean project structure


🔄 Workflow Explanation
🎥 Case 1: Video Upload → Sentiment Analysis

User uploads an interview video

Audio is extracted from the video

Speech-to-text conversion generates a raw transcript

Transcript is structured into Question–Answer pairs

Each candidate answer is analyzed using NLTK VADER

Sentiment label and score are generated

Results are displayed and stored for further evaluation

📄 Case 2: Transcript Upload → Sentiment Analysis

User uploads a text transcript file

System reads the transcript directly

Transcript is converted into Q&A pairs

Sentiment analysis is applied to each answer

Sentiment scores and labels are generated instantly

Results are shown without any video processing

🧠 Sentiment Analysis Logic

The system uses NLTK’s VADER Sentiment Analyzer to classify candidate responses:

Positive → Confident, clear, and strong responses

Neutral → Informational or balanced responses

Negative → Uncertain, hesitant, or weak responses

Each answer is assigned:

A sentiment label (Positive / Neutral / Negative)

A numerical sentiment score

This enables objective and consistent evaluation of interview answers.

📊 Output Format

The final output includes:

Question

Candidate Answer

Sentiment Label

Sentiment Score

Outputs can be:

Viewed through the frontend

Exported as a CSV file


📄 Input Format (Transcript Example)
Q: Tell me about yourself
A: I am passionate about learning and solving real-world problems

Q: What are your strengths?
A: I adapt quickly and enjoy working in teams

🔐 Security & Best Practices

No API keys are hardcoded

Sensitive data is managed using environment variables

.env file is excluded using .gitignore

Large media files are not committed to GitHub

🎓 Academic & Industry Relevance

This project reflects real-world AI system design by:

Supporting multiple input formats

Separating core logic and frontend

Following modular and scalable architecture

Applying AI for practical HR decision-making

🔮 Future Enhancements

Automatic candidate scoring & ranking

Audio emotion and tone analysis

Interactive analytics dashboard

Cloud deployment

Integration with recruitment platforms

👩‍💻 Author

Rekha Rathod
Artificial Intelligence & Machine Learning

⭐ Final Note

This project demonstrates how AI and NLP can be used to enhance fairness, consistency, and efficiency in the interview evaluation process.
