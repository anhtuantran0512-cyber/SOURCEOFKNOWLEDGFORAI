---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/language-flashcard-with-pronunciation/"
title: "Language Flashcard with Pronunciation"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front shows a foreign-language word with phonetic transcription and an audio play button; back reveals definition, usage example, and a memory tip."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Language Flashcard with Pronunciation
Source: https://codefronts.com/components/css-flip-cards/language-flashcard-with-pronunciation/

Front shows a foreign-language word with phonetic transcription and an audio play button; back reveals definition, usage example, and a memory tip.
## HTML
```html
<div class="fc-06">
  <div class="fc-06__nav">
    <button class="fc-06__nav-btn">← Prev</button>
    <button class="fc-06__nav-btn">Next →</button>
  </div>
  <div class="fc-06__counter">Card 7 of 24 · Japanese N3</div>
  <div class="fc-06__scene">
    <div class="fc-06__card">
      <div class="fc-06__front">
        <div class="fc-06__lang-flag">🇯🇵</div>
        <div class="fc-06__lang-label">Japanese</div>
        <div class="fc-06__word">木漏れ日</div>
        <div class="fc-06__phonetic">/ ko·mo·re·bi /</div>
        <button class="fc-06__sound-btn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          Play audio
        </button>
        <div class="fc-06__front-hint">Hover to see definition →</div>
      </div>
      <div class="fc-06__back">
        <div class="fc-06__def-label">Definition</div>
        <div class="fc-06__pos">noun · untranslatable</div>
        <div class="fc-06__definition">Sunlight filtering through leaves; the interplay of light and shadow when sun shines through a canopy of trees.</div>
        <div class="fc-06__example-label">Example sentence</div>
        <div class="fc-06__example">「公園の木漏れ日の中で読書するのが好きです。」<br>"I love reading in the komorebi of the park."</div>
        <div class="fc-06__mnemonic"><strong>Memory tip:</strong> 木 (ki = tree) + 漏れ (more = leaking) + 日 (hi = sun) → "sun leaking through trees" — paint the picture.</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-06,
.fc-06 *,
.fc-06 *::before,
.fc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-06 ::selection {
  background: #a78bfa;
  color: #000;
}

.fc-06 {
  --bg: #080612;
  --purple: #a78bfa;
  --indigo: #6366f1;
  --mint: #34d399;
  --white: #f5f3ff;
  --card-w: 340px;
  --card-h: 400px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 40%,#120b2e,#080612 65%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 20px;
  color: var(--white);
}

.fc-06__nav {
  display: flex;
  gap: 12px;
}

.fc-06__nav-btn {
  padding: 8px 20px;
  border-radius: 20px;
  border: 1px solid rgba(163,139,250,.25);
  background: rgba(163,139,250,.08);
  color: rgba(245,243,255,.6);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: background .2s;
}

.fc-06__nav-btn:hover {
  background: rgba(163,139,250,.18);
  color: var(--purple);
}

.fc-06__counter {
  font-size: 12px;
  color: rgba(245,243,255,.35);
  letter-spacing: .08em;
}

.fc-06__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-06__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fc-06__scene:hover .fc-06__card {
  transform: rotateY(180deg);
}

.fc-06__front,
.fc-06__back {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-06__front {
  background: linear-gradient(145deg,#130d2e,#0e0a22);
  border: 1px solid rgba(163,139,250,.25);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 40px 32px;
}

.fc-06__front::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 30%,rgba(163,139,250,.1),transparent 60%);
}

.fc-06__lang-flag {
  font-size: 40px;
  position: relative;
  z-index: 1;
}

.fc-06__lang-label {
  font-size: 10px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(245,243,255,.4);
  font-weight: 600;
  position: relative;
  z-index: 1;
}

.fc-06__word {
  font-size: 52px;
  font-weight: 900;
  background: linear-gradient(135deg,var(--purple),var(--indigo));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-align: center;
  position: relative;
  z-index: 1;
}

.fc-06__phonetic {
  font-size: 16px;
  color: rgba(245,243,255,.5);
  font-style: italic;
  position: relative;
  z-index: 1;
  letter-spacing: .04em;
}

.fc-06__sound-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 20px;
  background: rgba(163,139,250,.1);
  border: 1px solid rgba(163,139,250,.2);
  color: var(--purple);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  position: relative;
  z-index: 1;
  transition: background .2s;
}

.fc-06__sound-btn:hover {
  background: rgba(163,139,250,.2);
}

.fc-06__front-hint {
  position: absolute;
  bottom: 18px;
  font-size: 10px;
  color: rgba(245,243,255,.2);
  letter-spacing: .08em;
}
/* BACK */

.fc-06__back {
  background: linear-gradient(145deg,#0a1a0e,#0d1f12);
  border: 1px solid rgba(52,211,153,.2);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 30px;
  gap: 14px;
}

.fc-06__def-label {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--mint);
  font-weight: 700;
}

.fc-06__definition {
  font-size: 16px;
  font-weight: 700;
  color: var(--white);
  line-height: 1.4;
}

.fc-06__pos {
  display: inline-block;
  font-size: 10px;
  padding: 2px 10px;
  border-radius: 20px;
  background: rgba(52,211,153,.1);
  border: 1px solid rgba(52,211,153,.2);
  color: var(--mint);
  font-style: italic;
  margin-bottom: 4px;
}

.fc-06__example-label {
  font-size: 10px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(245,243,255,.35);
  margin-top: 4px;
}

.fc-06__example {
  font-size: 13px;
  color: rgba(245,243,255,.65);
  line-height: 1.7;
  font-style: italic;
  border-left: 2px solid rgba(52,211,153,.3);
  padding-left: 12px;
}

.fc-06__mnemonic {
  margin-top: auto;
  padding: 12px;
  border-radius: 12px;
  background: rgba(163,139,250,.06);
  border: 1px solid rgba(163,139,250,.12);
  font-size: 12px;
  color: rgba(245,243,255,.5);
  line-height: 1.6;
}

.fc-06__mnemonic strong {
  color: var(--purple);
}

@media (prefers-reduced-motion: reduce) {
  .fc-06__card {
    transition: none;
  }
}
```
