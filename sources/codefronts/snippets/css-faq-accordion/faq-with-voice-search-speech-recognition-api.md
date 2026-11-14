---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/faq-with-voice-search-speech-recognition-api/"
title: "FAQ with Voice Search Speech-Recognition API"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "Speak your question, watch the FAQ filter: a microphone button feeds the Web Speech API's SpeechRecognition into the same live filter as demo 18, with…"
has_js: "true"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FAQ with Voice Search Speech-Recognition API
Source: https://codefronts.com/snippets/css-faq-accordion/faq-with-voice-search-speech-recognition-api/

Speak your question, watch the FAQ filter: a microphone button feeds the Web Speech API's SpeechRecognition into the same live filter as demo 18, with interim results streaming into the input as you talk, a pulsing listening indicator, and — the part most voice demos skip — a complete progressive-enhancement story: the mic button only renders where the API exists, the keyboard filter is the baseline everyone gets, and every state change is announced for screen readers. Voice as a bonus layer, never a requirement.
## HTML
```html
<section class="cfa-25" aria-label="FAQ with voice search">
  <div class="cfa-25__wrap">
    <header class="cfa-25__head">
      <h1>Ask out loud</h1>
      <p>Tap the mic and say “warranty” or “battery” — or just type. Voice is a layer on the same filter, not a requirement.</p>
    </header>
    <div class="cfa-25__bar">
      <input type="search" id="cfa25-input" class="cfa-25__input" placeholder="Type or speak to filter…" aria-label="Search frequently asked questions by typing or voice">
      <button type="button" class="cfa-25__mic" id="cfa25-mic" aria-pressed="false" aria-label="Search by voice">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 3a3 3 0 013 3v5a3 3 0 01-6 0V6a3 3 0 013-3z" fill="currentColor"/><path d="M6 11a6 6 0 0012 0M12 17v3.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </div>
    <p class="cfa-25__status" id="cfa25-status" aria-live="polite"></p>
    <div class="cfa-25__list" id="cfa25-list">
      <details class="cfa-25__item">
        <summary class="cfa-25__q">How long does the battery last?<i aria-hidden="true"></i></summary>
        <div class="cfa-25__a"><p>Up to 14 days in watch mode, 30 hours with continuous GPS. Battery care mode (on by default) caps daily charging to double the cell's lifespan.</p></div>
      </details>
      <details class="cfa-25__item">
        <summary class="cfa-25__q">What does the warranty cover?<i aria-hidden="true"></i></summary>
        <div class="cfa-25__a"><p>Two years on manufacturing defects and battery health below 80%. Accidental damage falls under the optional care plan with flat-rate repairs.</p></div>
      </details>
      <details class="cfa-25__item">
        <summary class="cfa-25__q">Can I swim with it?<i aria-hidden="true"></i></summary>
        <div class="cfa-25__a"><p>Yes — 5ATM rated for pool and open water, with a dedicated swim-tracking mode. Rinse with fresh water after the sea; salt is the enemy of every seal.</p></div>
      </details>
      <details class="cfa-25__item">
        <summary class="cfa-25__q">Does voice control work offline?<i aria-hidden="true"></i></summary>
        <div class="cfa-25__a"><p>Basic commands (timers, workouts, music controls) run on-device. Free-form questions need a connection — the same trade this very page makes with browser speech recognition.</p></div>
      </details>
      <details class="cfa-25__item">
        <summary class="cfa-25__q">How do I update the firmware?<i aria-hidden="true"></i></summary>
        <div class="cfa-25__a"><p>Updates install automatically overnight while charging, when on Wi-Fi. You can trigger one manually from the app under Device → Software.</p></div>
      </details>
    </div>
    <div class="cfa-25__empty" id="cfa25-empty" hidden><b>No matches.</b><p>Try different words, or clear the search.</p></div>
    <p class="cfa-25__foot">Voice audio is processed by your browser vendor's speech service. No mic in this browser? The typed filter is the baseline. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-25,
.cfa-25 *,
.cfa-25 *::before,
.cfa-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-25 {
  --bg: oklch(0.15 0.025 310);
  --panel: oklch(0.2 0.028 310);
  --ink: oklch(0.96 0.006 305);
  --mut: oklch(0.68 0.02 308);
  --line: oklch(0.31 0.03 309);
  --acc: oklch(0.75 0.17 350);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: radial-gradient(950px 550px at 20% -10%,oklch(0.24 0.06 350/.5),transparent 60%),var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-25__wrap {
  width: min(100%,640px);
}

.cfa-25__head h1 {
  font-size: clamp(28px,4.5cqi,40px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-25__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-25__bar {
  display: flex;
  align-items: stretch;
  gap: 10px;
  margin-top: 22px;
}

.cfa-25__input {
  flex: 1;
  min-width: 0;
  min-height: 52px;
  padding: 0 18px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  font: inherit;
  font-size: 15px;
  color: var(--ink);
  outline: 0;
  transition: border-color .25s,box-shadow .25s;
}

.cfa-25__input::placeholder {
  color: var(--mut);
}

.cfa-25__input:focus-visible {
  border-color: var(--acc);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--acc) 25%,transparent);
}

.cfa-25__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
}

.cfa-25__mic {
  position: relative;
  flex: none;
  width: 52px;
  min-height: 52px;
  display: grid;
  place-items: center;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--panel);
  color: var(--mut);
  cursor: pointer;
  transition: color .25s,border-color .25s,background .25s;
}

.cfa-25__mic:hover {
  color: var(--acc);
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
}

.cfa-25__mic:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cfa-25__mic[aria-pressed="true"] {
  color: oklch(0.98 0.005 350);
  background: var(--acc);
  border-color: var(--acc);
}

.cfa-25__mic[aria-pressed="true"]::before {
  content: "";
  position: absolute;
  inset: -4px;
  border-radius: 18px;
  border: 2px solid var(--acc);
  animation: cfa25pulse 1.3s ease-out infinite;
}

@keyframes cfa25pulse {
  0% {
    opacity: .8;
    scale: 1;
  }

  100% {
    opacity: 0;
    scale: 1.25;
  }
}

.cfa-25__status {
  min-height: 20px;
  margin-top: 10px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: var(--acc);
}

.cfa-25__list {
  margin-top: 8px;
  display: flex;
  flex-direction: column;
  gap: 9px;
  interpolate-size: allow-keywords;
}

.cfa-25__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  transition: border-color .3s;
}

.cfa-25__item[open] {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-25__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 15px 17px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 650;
  list-style: none;
  transition: color .2s;
}

.cfa-25__q::-webkit-details-marker {
  display: none;
}

.cfa-25__q:hover {
  color: var(--acc);
}

.cfa-25__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-25__q i {
  flex: none;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-25__item[open] .cfa-25__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-25__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-25__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .35s allow-discrete;
  }

  .cfa-25__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-25__empty {
  margin-top: 14px;
  padding: 24px 20px;
  text-align: center;
  border: 1px dashed var(--line);
  border-radius: 14px;
  color: var(--mut);
}

.cfa-25__empty b {
  color: var(--ink);
}

.cfa-25__empty p {
  margin-top: 5px;
  font-size: 13px;
}

.cfa-25__foot {
  margin-top: 20px;
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-25 *,
    .cfa-25 .cfa-25__item::details-content {
    transition-duration: .01ms !important;
    animation-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cfa-25');if(!root||root.dataset.cfa25)return;root.dataset.cfa25='1';
  var input=root.querySelector('#cfa25-input'),status=root.querySelector('#cfa25-status'),
      empty=root.querySelector('#cfa25-empty'),mic=root.querySelector('#cfa25-mic'),
      items=[].slice.call(root.querySelectorAll('.cfa-25__item'));
  function filter(){
    var q=input.value.trim().toLowerCase(),hits=0;
    items.forEach(function(d){
      var hit=!q||d.textContent.toLowerCase().indexOf(q)>-1;
      d.hidden=!hit;if(q&&hit)d.open=true;if(!q)d.open=false;if(hit)hits++;
    });
    empty.hidden=hits>0;
  }
  input.addEventListener('input',filter);
  var SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR){mic.remove();return;}
  var rec=new SR(),listening=false;
  rec.lang='en-US';rec.interimResults=true;rec.continuous=false;
  function setListening(on){
    listening=on;
    mic.setAttribute('aria-pressed',String(on));
    status.textContent=on?'Listening… speak now':'';
  }
  mic.addEventListener('click',function(){
    if(listening){rec.stop();return;}
    try{rec.start();setListening(true);}catch(e){setListening(false);}
  });
  rec.onresult=function(e){
    var t='';for(var i=0;i<e.results.length;i++)t+=e.results[i][0].transcript;
    input.value=t;filter();
  };
  rec.onerror=function(e){
    setListening(false);
    status.textContent=e.error==='not-allowed'?'Microphone permission denied — the typed filter still works.':'';
  };
  rec.onend=function(){setListening(false);};
})();
```
