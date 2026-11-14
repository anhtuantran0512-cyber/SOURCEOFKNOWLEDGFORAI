---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/streaming-response-progress-with-readablestream-reader/"
title: "Streaming Response Progress with ReadableStream Reader"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "Progress for a response that arrives in pieces: a bar advancing as chunks land from response.body.getReader(), a live token counter, a chunk counter, and a…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Streaming Response Progress with ReadableStream Reader
Source: https://codefronts.com/components/css-progress-bars/streaming-response-progress-with-readablestream-reader/

Progress for a response that arrives in pieces: a bar advancing as chunks land from response.body.getReader(), a live token counter, a chunk counter, and a pulsing status dot that becomes a checkmark when the stream closes. The AI-SDK pattern, built from the actual reader loop.
## HTML
```html
<div class="pb-04">
  <button class="pb-04__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-04__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-04__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-04__stage">
    <div class="pb-04__card" id="pb-04-card" data-state="idle">
      <header class="pb-04__head">
        <span class="pb-04__avatar" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><path d="M12 3.2l1.9 4.5 4.9.4-3.7 3.2 1.1 4.8L12 13.6l-4.2 2.5 1.1-4.8L5.2 8.1l4.9-.4z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
        </span>
        <span class="pb-04__headMeta">
          <span class="pb-04__who">Assistant</span>
          <span class="pb-04__mono">POST /v1/messages &middot; stream: true</span>
        </span>
        <span class="pb-04__model pb-04__mono">gpt-oss-120b</span>
      </header>

      <p class="pb-04__prompt"><span class="pb-04__promptTag">You</span>Summarise the migration notes for the new router API.</p>

      <div class="pb-04__body">
        <p class="pb-04__out" id="pb-04-out">The router API replaces nested layouts with a flat segment map, so every route</p>
        <span class="pb-04__caret" aria-hidden="true"></span>
      </div>

      <div class="pb-04__barRow">
        <span class="pb-04__dot" aria-hidden="true"></span>
        <svg class="pb-04__doneIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9.2" stroke="currentColor" stroke-width="1.7"/><path d="M7.8 12.4l3 3 5.4-6" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div class="pb-04__bar" id="pb-04-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-valuetext="0 tokens received" aria-label="Streaming response progress" style="--value:0">
          <span class="pb-04__fill"><span class="pb-04__sheen"></span></span>
        </div>
        <span class="pb-04__pct pb-04__mono" id="pb-04-pct">0%</span>
      </div>

      <div class="pb-04__stats">
        <p class="pb-04__stat"><span class="pb-04__k">Received</span><span class="pb-04__v pb-04__mono" id="pb-04-tokens">0 tokens</span></p>
        <p class="pb-04__stat"><span class="pb-04__k">Chunks</span><span class="pb-04__v pb-04__mono" id="pb-04-chunks">0</span></p>
        <p class="pb-04__stat"><span class="pb-04__k">Status</span><span class="pb-04__v" id="pb-04-status">Idle</span></p>
      </div>

      <div class="pb-04__controls">
        <button class="pb-04__btn pb-04__btn--primary" type="button" id="pb-04-run">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 5.5l10 6.5-10 6.5z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>Stream response
        </button>
        <span class="pb-04__hint pb-04__mono">while (!done) await reader.read()</span>
      </div>
      <p class="pb-04__live" id="pb-04-live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-04 {
  --bg: #08070f;
  --card: #0e0d1a;
  --card2: #141327;
  --ink: #f0edff;
  --muted: rgba(240,237,255,.6);
  --line: rgba(240,237,255,.12);
  --track: rgba(240,237,255,.08);
  --accent: #a78bfa;
  --accent-2: #c4b5fd;
  --ok: #34d399;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(76% .16 295)) {
  .pb-04 {
    --accent: oklch(76% .16 295);
    --accent-2: oklch(84% .1 295);
    --ok: oklch(78% .15 162);
  }
}

.pb-04 *,
.pb-04 *::before,
.pb-04 *::after {
  box-sizing: border-box;
}

.pb-04__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(90% 60% at 80% -5%,color-mix(in srgb,var(--accent) 22%,transparent),transparent 60%), radial-gradient(80% 60% at 5% 100%,color-mix(in srgb,var(--accent-2) 12%,transparent),transparent 60%);
}

.pb-04__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-04__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.11);
}

.pb-04__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-04__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-04__sun {
  display: none;
}

.pb-04__moon {
  display: block;
}

.pb-04[data-theme="light"] .pb-04__sun {
  display: block;
}

.pb-04[data-theme="light"] .pb-04__moon {
  display: none;
}

.pb-04__card {
  inline-size: min(42rem,100%);
  display: grid;
  gap: clamp(.9rem,2.1vw,1.3rem);
  padding: clamp(1.25rem,3.2vw,2rem);
  border-radius: 1.6rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 92%,transparent);
  -webkit-backdrop-filter: blur(16px);
  backdrop-filter: blur(16px);
  box-shadow: 0 1px 0 rgba(255,255,255,.06) inset,0 36px 90px -46px rgba(0,0,0,.95);
}

.pb-04__head {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .75rem;
  align-items: center;
}

.pb-04__avatar {
  inline-size: 2.4rem;
  block-size: 2.4rem;
  display: grid;
  place-items: center;
  border-radius: .75rem;
  color: var(--accent-2);
  border: 1px solid color-mix(in srgb,var(--accent) 34%,transparent);
  background: color-mix(in srgb,var(--accent) 16%,transparent);
}

.pb-04__avatar svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
}

.pb-04__headMeta {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
}

.pb-04__who {
  font-size: .92rem;
  font-weight: 600;
}

.pb-04__mono {
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-04__model {
  padding: .3rem .55rem;
  border-radius: .5rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
}

.pb-04__prompt {
  margin: 0;
  display: flex;
  gap: .6rem;
  align-items: baseline;
  font-size: .9rem;
  color: var(--muted);
  padding: .7rem .85rem;
  border-radius: .9rem;
  background: color-mix(in srgb,var(--ink) 5%,transparent);
  border: 1px solid var(--line);
}

.pb-04__promptTag {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent-2);
  flex: none;
}

.pb-04__body {
  position: relative;
  min-block-size: 5.5rem;
  padding: 1rem 1.05rem;
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  background: var(--card2);
}

.pb-04__out {
  margin: 0;
  font-size: clamp(.9rem,1.5vw,1rem);
  line-height: 1.65;
  color: var(--ink);
  text-wrap: pretty;
}

.pb-04__caret {
  display: inline-block;
  inline-size: .14rem;
  block-size: 1.05em;
  vertical-align: -.18em;
  margin-inline-start: .18rem;
  background: var(--accent-2);
  animation: pb-04-blink 1s steps(2,jump-none) infinite;
}

@keyframes pb-04-blink {
  50% {
    opacity: 0;
  }
}

.pb-04__card[data-state="done"] .pb-04__caret,
.pb-04__card[data-state="idle"] .pb-04__caret {
  display: none;
}

.pb-04__barRow {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .7rem;
  align-items: center;
}

.pb-04__dot {
  inline-size: .55rem;
  block-size: .55rem;
  border-radius: 99px;
  background: var(--accent-2);
  animation: pb-04-pulse 1.4s ease-in-out infinite;
}

@keyframes pb-04-pulse {
  0%,
    100% {
    transform: scale(.7);
    opacity: .55;
  }

  50% {
    transform: scale(1.15);
    opacity: 1;
  }
}

.pb-04__doneIcon {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  color: var(--ok);
  display: none;
}

.pb-04__card[data-state="done"] .pb-04__dot {
  display: none;
}

.pb-04__card[data-state="done"] .pb-04__doneIcon {
  display: block;
}

.pb-04__bar {
  position: relative;
  inline-size: 100%;
  block-size: .6rem;
  border-radius: 99px;
  background: var(--track);
  border: 1px solid var(--line);
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(0,0,0,.45) inset;
}

.pb-04__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  overflow: hidden;
  transition: inline-size .28s cubic-bezier(.4,0,.2,1);
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
}

.pb-04__sheen {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.55),transparent);
  transform: translateX(-100%);
  animation: pb-04-sheen 1.6s linear infinite;
}

.pb-04__card[data-state="done"] .pb-04__sheen {
  animation: none;
  opacity: 0;
}

.pb-04__card[data-state="done"] .pb-04__fill {
  background: linear-gradient(90deg,var(--accent),var(--ok));
}

@keyframes pb-04-sheen {
  0% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(260%);
  }
}

.pb-04__pct {
  font-size: .85rem;
  color: var(--ink);
  font-weight: 600;
  min-inline-size: 2.6rem;
  text-align: end;
}

.pb-04__stats {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(8rem,1fr));
  gap: .5rem;
}

.pb-04__stat {
  margin: 0;
  display: grid;
  gap: .2rem;
  padding: .65rem .8rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
}

.pb-04__k {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--muted);
}

.pb-04__v {
  font-size: .92rem;
  font-weight: 600;
  color: var(--ink);
}

.pb-04__controls {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem;
  align-items: center;
}

.pb-04__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  padding: .65rem 1.1rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
  font: inherit;
  font-size: .88rem;
  font-weight: 550;
  cursor: pointer;
  transition: transform .18s,background .18s;
}

.pb-04__btn svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.pb-04__btn:hover {
  transform: translateY(-1px);
}

.pb-04__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-04__btn--primary {
  background: var(--accent);
  border-color: transparent;
  color: #160c2a;
  box-shadow: 0 12px 28px -16px var(--accent);
}

.pb-04__btn--primary:hover {
  background: color-mix(in srgb,var(--accent) 88%,white);
}

.pb-04__hint {
  opacity: .8;
}

.pb-04__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .78rem;
  color: var(--ok);
}

.pb-04[data-theme="light"] {
  --bg: #f7f5ff;
  --card: #ffffff;
  --card2: #faf9ff;
  --ink: #160c2a;
  --muted: rgba(22,12,42,.62);
  --line: rgba(22,12,42,.1);
  --track: rgba(22,12,42,.07);
  --accent: #7c3aed;
  --accent-2: #8b5cf6;
  --ok: #059669;
}

.pb-04[data-theme="light"] .pb-04__theme {
  background: rgba(22,12,42,.05);
}

.pb-04[data-theme="light"] .pb-04__btn--primary {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .pb-04:not([data-theme="dark"]) {
    --bg: #f7f5ff;
    --card: #ffffff;
    --card2: #faf9ff;
    --ink: #160c2a;
    --muted: rgba(22,12,42,.62);
    --line: rgba(22,12,42,.1);
    --track: rgba(22,12,42,.07);
    --accent: #7c3aed;
    --accent-2: #8b5cf6;
    --ok: #059669;
  }

  .pb-04:not([data-theme="dark"]) .pb-04__theme {
    background: rgba(22,12,42,.05);
  }

  .pb-04:not([data-theme="dark"]) .pb-04__btn--primary {
    color: #fff;
  }

  .pb-04:not([data-theme="dark"]) .pb-04__sun {
    display: block;
  }

  .pb-04:not([data-theme="dark"]) .pb-04__moon {
    display: none;
  }

  .pb-04[data-theme="dark"] .pb-04__sun {
    display: none;
  }

  .pb-04[data-theme="dark"] .pb-04__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-04 *,
    .pb-04 *::before,
    .pb-04 *::after {
    animation: none !important;
    transition: none !important;
  }

  .pb-04__caret {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .pb-04__card,
    .pb-04__bar,
    .pb-04__btn,
    .pb-04__theme,
    .pb-04__body,
    .pb-04__stat {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-04__fill {
    background: Highlight;
  }
}
```

## JavaScript
```js
const pb04 = document.querySelector('.pb-04');
if (pb04) {
  const q = (s) => pb04.querySelector(s);
  const [card, bar, pct, tokens, chunks, status, out, live] =
    ['#pb-04-card','#pb-04-bar','#pb-04-pct','#pb-04-tokens','#pb-04-chunks','#pb-04-status','#pb-04-out','#pb-04-live'].map(q);
  const TEXT = ['The router API replaces nested layouts',' with a flat segment map,',' so every route resolves',' in a single pass.',' Loaders now run in parallel',' and stream their results',' to the shell as they settle.',' Migration is mechanical:',' move each layout file',' into the segment it owned,',' then delete the bridge adapter.'];
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  async function* mockStream(parts) { for (const p of parts) { await sleep(80 + Math.random() * 120); yield p; } }
  const stream = async () => {
    card.dataset.state = 'streaming'; status.textContent = 'Streaming'; live.textContent = 'Response streaming.';
    let tok = 0, n = 0, text = '';
    for await (const part of mockStream(TEXT)) {           // real: for await (const {value} of reader)
      n += 1; tok += Math.round(part.length / 3.6); text += part;
      const p = Math.round((n / TEXT.length) * 100);
      bar.style.setProperty('--value', p); bar.setAttribute('aria-valuenow', p);
      bar.setAttribute('aria-valuetext', tok + ' tokens received');
      pct.textContent = p + '%'; tokens.textContent = tok + ' tokens'; chunks.textContent = n; out.textContent = text;
    }
    card.dataset.state = 'done'; status.textContent = 'Complete';
    live.textContent = 'Response complete, ' + tok + ' tokens in ' + TEXT.length + ' chunks.';
  };
  q('#pb-04-run').addEventListener('click', stream);
  q('.pb-04__theme').addEventListener('click', (e) => {
    const light = pb04.dataset.theme !== 'light';
    pb04.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  stream();
}
```
