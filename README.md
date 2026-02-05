🛡️ Agentic Honey-Pot for Scam Detection & Intelligence Extraction

An AI-powered Agentic Honey-Pot API that detects scam messages, autonomously engages scammers in multi-turn conversations, extracts actionable intelligence, and reports results in a structured format.
Built as part of a hackathon / evaluation-ready solution.

📌 Features

Scam intent detection using NLP & keyword analysis

Autonomous AI agent with human-like conversation behavior

Multi-turn conversation handling with session memory

Extraction of scam intelligence (UPI IDs, phone numbers, links, keywords)

Secure REST API with API key authentication

Evaluation-ready JSON responses

Optional callback support for final intelligence reporting

🧱 Project Structure
├── main.py
├── config.py
├── auth.py
├── memory.py
├── detector.py
├── agent.py
├── extractor.py
├── callback.py
├── safety.py
├── nlp.py
├── models.py
└── requirements.txt

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/your-username/agentic-honeypot.git
cd agentic-honeypot

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


(Optional NLP support)

python -m spacy download en_core_web_sm

4️⃣ Set API Key
export API_KEY=GUVI_EVAL_KEY_123     # Linux/macOS
set API_KEY=GUVI_EVAL_KEY_123        # Windows

5️⃣ Run the Server
uvicorn main:app --host 0.0.0.0 --port 8000

🔍 API Usage
Endpoint
POST /analyze

Headers
{
  "Content-Type": "application/json",
  "x-api-key": "GUVI_EVAL_KEY_123"
}

Sample Request
{
  "message": "Your bank account will be blocked today. Verify immediately.",
  "session_id": "session-123"
}

Sample Response
{
  "is_scam": true,
  "confidence_score": 0.6,
  "category": "financial_fraud",
  "extracted_intelligence": {
    "phone_numbers": [],
    "urls": [],
    "money_mentions": []
  },
  "nlp_entities": {
    "entities": []
  },
  "agent_reply": "Why is this urgent? I just used my account."
}

📊 Evaluation Readiness

Stable public API endpoint

Low-latency responses

Strict JSON schema compliance

API key–secured authentication

Supports automated evaluation systems

🧠 Technologies Used

FastAPI – REST API framework

Python – Core backend logic

spaCy – NLP entity extraction

Regex – Intelligence extraction

Uvicorn – ASGI server

⚠️ Ethics & Safety

No impersonation of real individuals

No illegal instructions

No harassment or abuse

Responsible handling of extracted data
