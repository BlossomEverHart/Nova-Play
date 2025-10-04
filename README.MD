<div align="center">
  <img src="docs/cover.png" width="100%" alt="Nova Play — EverHart Labs banner" />

  # 🎮 Nova Play — EverHart Labs 
  **AI Co-Pilot for Gamers • Voice + Vision + Vibe**

  🌸 *By Blossom EverHart*

  [![Status](https://img.shields.io/badge/status-MVP--prototype-pink)](./)
  [![Made With](https://img.shields.io/badge/made_with-Electron_+_FastAPI-black)](./)
  [![License](https://img.shields.io/badge/license-MIT-black)](./)

  <br>
  <p><em>Your AI teammate — adaptive, empathic, and always cheering you on.</em></p>
</div>

---

## ✨ Features (MVP)
- Electron overlay (always-on-top toggle)
- Modes: **Assist / Follow / Vibe**
- 🔊 **Text-to-Speech** replies + 🎙️ **Push-to-Talk** (experimental)
- Local FastAPI endpoint `POST /plan` (returns a suggestion)

## ⚙️ Quickstart
### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 5055
cd app
npm install
npm start

Hotkeys: F9 toggles always-on-top









🧠 How it works





Overlay calls http://localhost:5055/plan with the current mode.
Backend returns a suggestion.
Overlay speaks the line via Web Speech API (TTS).
Optional Push-to-Talk listens (Chrome-based).










🛡️ Policy Guard





No game memory access
No input spoofing
Explicit mic consent








— Created by Blossom EverHart · EverHart Labs

