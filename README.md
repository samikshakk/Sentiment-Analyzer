<h2 align="center" style="color:#4CAF50">🔍 Analyze Legal Documents</h2>


<p align="center">
  <a href="https://streamlit.io/">
    <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-Live%20App-ff4b4b?logo=streamlit&logoColor=white&style=for-the-badge">
  </a>
  <a href="https://huggingface.co/google/flan-t5-base">
    <img alt="Hugging Face Model" src="https://img.shields.io/badge/Made%20with-FLAN--T5-blue?logo=google&style=for-the-badge">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  </a>
</p>


An AI-powered tool that automates sentiment analysis on legal documents using large language models like FLAN-T5 or Mistral. Built with Streamlit for a smooth, interactive experience.

<b> Description</b>

This project analyzes legal documents to determine sentiment—positive, negative, or neutral. It helps law firms or compliance teams quickly evaluate the tone and implication of large case summaries or client feedback.

 <b>🎯Features</b>

⚖️ Clean and preprocess legal language

🤖 Analyze sentiment using FLAN-T5

🧼 Summarized and labeled output

🌐 Streamlit-based web interface

📂 File upload support for .txt

🧠 Hugging Face Transformers-based NLP

🪄 Prompt-style zero-shot inference

🚀 <b> Getting Started </b>

1. Install Dependencies

pip install -r requirements.txt

2. Run the App

streamlit run streamlit_app.py

 <b>🛠️ File Structure </b>

GenAI/
├── main.py               # CLI version
├── preprocess.py         # Text cleaning
├── analyze.py            # Model-based analysis
├── streamlit_app.py      # Web UI with file upload
├── legal_doc.txt         # Sample input file
├── requirements.txt      # Dependencies
└── README.md             # Project description

 <b>🤖 Models Used </b>

google/flan-t5-base (via Hugging Face Transformers)

Compatible with: Mistral, BERT, GPT-2 (if extended)

📚 Tech Stack

Python 3.9+

Streamlit

Hugging Face Transformers

PyTorch

Regex for cleaning text

 <b>🌐 Use Cases </b>

📑 Sentiment tagging of legal case summaries

🧾 Reviewing client feedback

⚖️ Pre-litigation document triage

🕵️‍♀️ Legal research and compliance automation

 <b>🔐 Security and Ethics </b>

This tool is designed for internal use and educational/demo purposes. Users are encouraged to anonymize legal documents and ensure data privacy when testing.

