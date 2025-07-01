import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from google.generativeai import configure, GenerativeModel
from fpdf import FPDF
import io

# --- Configure Gemini ---
configure(api_key="AIzaSyDA3pB8a9GqkfYUUPE3opPyEoKZrp-Hr-U")  # Replace with your API key

# --- Custom CSS ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f5f7fa;
        color: #1a1a1a;
    }
    .main {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        font-size: 1rem;
    }
    .stButton>button:hover {
        background-color: #2563eb;
    }
    .sentiment-chip {
        display: inline-block;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        color: white;
        font-weight: bold;
        margin-top: 0.5rem;
    }
    .positive { background-color: #10b981; }
    .neutral { background-color: #f59e0b; }
    .negative { background-color: #ef4444; }
    </style>
""", unsafe_allow_html=True)

# --- Sentiment Analysis ---
def analyze_sentiment(text):
    model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=1)[0]

    labels = ['negative', 'neutral', 'positive']
    results = {label: float(scores[i]) for i, label in enumerate(labels)}
    sentiment = max(results, key=results.get)
    return sentiment, results

# --- Gemini Summary ---
def summarize_text(text):
    try:
        model = GenerativeModel("gemini-1.5-flash")
        prompt = f"Summarize this legal document:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# --- PDF Generator ---
def create_pdf(sentiment, scores, summary, original):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    def safe_line(line):
        return line.encode("latin-1", "replace").decode("latin-1")

    content = f"""Legal Document Sentiment Analysis

Sentiment: {sentiment}
Scores:
- Positive: {scores['positive']:.2f}
- Neutral : {scores['neutral']:.2f}
- Negative: {scores['negative']:.2f}

--- Summary by AI ---

{summary}

--- Original Document ---

{original}
"""

    for line in content.split("\n"):
        pdf.multi_cell(0, 10, safe_line(line))

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

# --- Streamlit Layout ---
st.set_page_config(page_title="Legal Sentiment Analyzer", layout="centered")

st.title("⚖️ Legal Sentiment Analyzer")
st.markdown("Analyze the **sentiment** of legal documents and generate a **Gemini AI-powered summary** instantly.")

text = st.text_area("📄 Paste Legal Document Below:", height=250)

if st.button("🔍 Analyze"):
    if not text.strip():
        st.warning("Please paste some text.")
    else:
        with st.spinner("Analyzing sentiment..."):
            sentiment, scores = analyze_sentiment(text)

        st.subheader("📊 Sentiment Result")
        color_class = f"sentiment-chip {sentiment}"
        st.markdown(f'<div class="{color_class}">{sentiment.capitalize()}</div>', unsafe_allow_html=True)

        cols = st.columns(3)
        cols[0].metric("🟢 Positive", f"{scores['positive']:.2f}")
        cols[1].metric("🟡 Neutral", f"{scores['neutral']:.2f}")
        cols[2].metric("🔴 Negative", f"{scores['negative']:.2f}")

        with st.spinner("Generating Gemini Summary..."):
            summary = summarize_text(text)

        st.subheader("🧠 Gemini Summary")
        st.markdown(f"<div padding:1rem;border-radius:8px'>{summary}</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("🔗 Built with 🤖 Hugging Face + 🧠 Gemini + 🌐 Streamlit")
