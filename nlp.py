try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    SPACY = True
except:
    SPACY = False

def analyze_text(text: str):
    if not SPACY:
        return {"entities": []}

    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": entities}
