import random

AGENT_REPLIES = [
    "I am confused, can you explain again?",
    "Why is this urgent? I just used my account.",
    "I didn’t receive any OTP yet.",
    "Can you resend the message?",
    "Is there any other way to verify?"
]

def generate_reply():
    return random.choice(AGENT_REPLIES)
