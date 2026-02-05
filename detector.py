SCAM_KEYWORDS = [
    "otp", "verify", "urgent", "account", "bank",
    "blocked", "refund", "lottery", "prize", "click"
]

def detect_scam(text: str):
    score = sum(1 for k in SCAM_KEYWORDS if k in text.lower())
    confidence = min(score * 0.15, 1.0)

    return {
        "is_scam": confidence >= 0.4,
        "confidence": confidence,
        "category": "financial_fraud" if confidence >= 0.4 else "unknown"
    }
