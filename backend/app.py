# EverHart Labs – Nova Play Backend (FastAPI)
# Version: MVP Prototype
# Author: Blossom EverHart

from fastapi import FastAPI
from pydantic import BaseModel
from gtts import gTTS
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Nova Play – EverHart Labs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Dev-only (accepts requests from any source)
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        message = "Mode not recognized. Try assist, follow, or vibe."

    return {"status": "success", "message": message}
