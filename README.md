<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  
</head>
<body>

  <h1>⚖️ Legal Sentiment Analyzer</h1>

  <p>A Gemini-powered Streamlit app to analyze the <strong>sentiment of legal documents</strong>, generate <strong>AI-powered summaries</strong>, and export results in a clean PDF — all in a pastel-themed user-friendly UI.</p>


  <h2>✨ Features</h2>
  <ul>
    <li class="feature">📄 Paste any legal document and analyze its <strong>sentiment</strong> (Positive, Neutral, Negative)</li>
    <li class="feature">🧠 Get a <strong>concise AI summary</strong> powered by Gemini 1.5</li>
    <li class="feature">📊 Visual sentiment scores via Hugging Face transformers</li>
    <li class="feature">📥 Export everything into a beautiful <strong>PDF report</strong></li>
    <li class="feature">🎨 Pastel modern UI with clean typography and soft styling</li>
    <li class="feature">🔐 API key securely loaded via <code>.env</code> or <code>secrets.toml</code></li>
  </ul>

  <h2>🛠️ Tech Stack</h2>
  <ul>
    <li>Streamlit – UI framework</li>
    <li>Gemini API – by Google Generative AI</li>
    <li>Hugging Face Transformers – for sentiment analysis</li>
    <li>fpdf – for PDF creation</li>
    <li>python-dotenv – for securely loading API keys</li>
    <li>torch – for model inference</li>
  </ul>

  

  <h2>📂 How to Run Locally</h2>
  <div class="highlight">
    <pre><code>git clone https://github.com/yourusername/Legal-Sentiment-Analyzer.git
cd Legal-Sentiment-Analyzer
pip install -r requirements.txt</code></pre>
  </div>

  <p>Then, create a <code>.env</code> file in the root directory:</p>
  <div class="highlight"><code>GEMINI_API_KEY=your-api-key-here</code></div>

  <p>Or, for deployment with Streamlit Cloud, create:</p>
  <div class="highlight"><code>.streamlit/secrets.toml</code></div>
  <pre><code>[secrets]
GEMINI_API_KEY = "your-api-key-here"</code></pre>

  <p>Now, run the app:</p>
  <div class="highlight">
    <pre><code>streamlit run new.py</code></pre>
  </div>

  <h2>🙌 Credits</h2>
  <p>Made with ❤️ using Gemini, Hugging Face, and Streamlit.  
  <br>Fork it, star it, or build your own custom analyzer!</p>

  <h2>🔐 Security Tip</h2>
  <p>Ensure your <code>.env</code> is in <code>.gitignore</code> and is never committed to GitHub.</p>

</body>
</html>
