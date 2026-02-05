import regex as re

PHONE = r"\b\d{10}\b"
URL = r"https?://\S+"
MONEY = r"(₹\s?\d+|\$\s?\d+)"

def extract_intelligence(text: str):
    return {
        "phone_numbers": re.findall(PHONE, text),
        "urls": re.findall(URL, text),
        "money_mentions": re.findall(MONEY, text)
    }
