from fastapi import FastAPI, Depends
from auth import verify_api_key
from models import ScamRequest, ScamResponse
from safety import sanitize
from detector import detect_scam
from extractor import extract_intelligence
from agent import generate_reply
from memory import update_session
from nlp import analyze_text
from callback import send_callback
from config import APP_NAME, VERSION

app = FastAPI(title=APP_NAME, version=VERSION)

@app.post("/analyze", response_model=ScamResponse)
def analyze(data: ScamRequest, auth=Depends(verify_api_key)):

    message = sanitize(data.message)

    detection = detect_scam(message)
    intelligence = extract_intelligence(message)
    nlp_data = analyze_text(message)

    reply = generate_reply() if detection["is_scam"] else "Thank you for the information."

    if data.session_id:
        update_session(data.session_id, message)

    response = {
        "is_scam": detection["is_scam"],
        "confidence_score": detection["confidence"],
        "category": detection["category"],
        "extracted_intelligence": intelligence,
        "nlp_entities": nlp_data,
        "agent_reply": reply
    }

    send_callback(response)

    return response
