// ------- TTS helper -------
function speak(text) {
  if (!text) return;
  if (!('speechSynthesis' in window)) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  // pick a reasonable voice if available
  const vs = speechSynthesis.getVoices();
  const pick = vs.find(v => /en-US/i.test(v.lang)) || vs[0];
  if (pick) u.voice = pick;
  u.volume = 1; u.rate = 1; u.pitch = 1;
  speechSynthesis.speak(u);
}

// ------- Backend call -------
async function fetchSuggestion(mode) {
  const res = await fetch('http://127.0.0.1:5055/plan', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mode })
  });
  const data = await res.json();
  const out = document.getElementById('output');
  out.textContent = data.message || 'No message';
  return data.message;
}

// ------- Buttons your HTML calls -------
async function ask() {
  const sel = document.getElementById('modeSelect');
  const mode = (sel?.value || 'assist').toLowerCase();
  const msg = await fetchSuggestion(mode);
  return msg;
}

async function speakOut() {
  const out = document.getElementById('output');
  const text = out?.textContent?.trim();
  if (text) {
    speak(text);
  } else {
    const msg = await ask();
    speak(msg);
  }
}

let PTT_ON = false;
function pttToggle() {
  PTT_ON = !PTT_ON;
  const badge = document.getElementById('pttStatus');
  if (badge) badge.textContent = PTT_ON ? 'PTT: on' : 'PTT: off';
  console.log('Push-to-Talk:', PTT_ON ? 'on' : 'off');
}

// expose for inline onclick (since file:// scope can be strict)
window.ask = ask;
window.speakOut = speakOut;
window.pttToggle = pttToggle;
