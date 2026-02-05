from pydantic import BaseModel
from typing import List, Optional, Dict

class ScamRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ScamResponse(BaseModel):
    is_scam: bool
    confidence_score: float
    category: str
    extracted_intelligence: Dict
    nlp_entities: Dict
    agent_reply: str
