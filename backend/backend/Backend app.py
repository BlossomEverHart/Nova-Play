from fastapi import FastAPI

from pydantic import BaseModel

from typing import Optional

import random



app = FastAPI(title="Nova Play Local API")



class Sense(BaseModel):

    mode: str = "assist"  # assist|follow|vibe

    context: Optional[str] = None



TIPS = {

    "assist": [

        "Rotate right to high ground.",

        "Heal now; you’re below 35%.",

        "Zone closes in 30s — move early."

    ],

    "follow": [

        "On your six — covering you.",

        "I’ll ping loot ahead.",

        "Sticking close — call the push."

    ],

    "vibe": [

        "You got this — breathe and flow.",

        "Victory playlist queued in my head 😉",

        "Let’s make this round cozy and smart."

    ]

}



@app.post("/plan")

def plan(s: Sense):

    mode = (s.mode or "assist").lower()

    tips = TIPS.get(mode, TIPS["assist"])


    return {"mode": mode, "suggestion": random.choice(tips)}

