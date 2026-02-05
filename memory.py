session_store = {}

def get_session(session_id: str):
    return session_store.get(session_id, [])

def update_session(session_id: str, message: str):
    if session_id not in session_store:
        session_store[session_id] = []
    session_store[session_id].append(message)
