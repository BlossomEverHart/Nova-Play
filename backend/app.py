# ──────────────────────────────────────────────
# EverHart Labs – Nova Play Backend (FastAPI)
# Version: MVP Prototype
# Author: Blossom EverHart
# ──────────────────────────────────────────────

from fastapi import FastAPI
from pydantic import BaseModel
from gtts import gTTS
import os

app = FastAPI(title="Nova Play – EverHart Labs")

class ModeRequest(BaseModel):
    mode: str

@app.post("/plan")
def plan_mode(request: ModeRequest):
    mode = request.mode.lower()
    if mode == "assist":
        message = "I’m here to help you win this round, Blossom!"
    elif mode == "follow":
        message = "I’m analyzing your moves and syncing strategies."
    elif mode == "vibe":
        message = "Let’s relax, focus, and enjoy the game together."
    else:
        message = "Mode not recognized, but I’m still with you!"

    tts = gTTS(text=message, lang='en')
    tts.save("response.mp3")

    return {"status": "success", "message": message}

