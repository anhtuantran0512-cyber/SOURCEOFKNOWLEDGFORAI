---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/amber-and-green-phosphor-monitor/"
title: "Amber and Green Phosphor Monitor"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "Two monochrome tubes side by side with the phosphor named on each: P1 green and P3 amber."
has_js: "true"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Amber and Green Phosphor Monitor
Source: https://codefronts.com/design-styles/css-retro-designs/amber-and-green-phosphor-monitor/

Two monochrome tubes side by side with the phosphor named on each: P1 green and P3 amber. Persistence is a real trailing fade on newly written lines rather than a static glow, bloom scales with glyph brightness, and a slow retrace line crawls the field. It also states the accessibility limit that a one-hue display forces on you, and what it uses instead.
## HTML
```html
<section class="rt-08" aria-labelledby="rt-08-title">
  <h2 class="rt-08__sr" id="rt-08-title">Monochrome phosphor monitors, P1 green and P3 amber</h2>

  <div class="rt-08__theme">
    <input class="rt-08__theme-input" type="checkbox" id="rt-08-theme">
    <label class="rt-08__theme-label" for="rt-08-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-08__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-08__stage">
    <header class="rt-08__head">
      <p class="rt-08__kicker">Monochrome CRT &middot; phosphor persistence and bloom</p>
      <h3 class="rt-08__h">Two phosphors, one code path</h3>
    </header>

    <div class="rt-08__pair">
      <article class="rt-08__tube rt-08__tube--p1" aria-labelledby="rt-08-l1">
        <div class="rt-08__screen">
          <div class="rt-08__feed" data-rt-08-feed="p1" role="log" aria-live="off" aria-relevant="additions"></div>
          <div class="rt-08__retrace" aria-hidden="true"></div>
        </div>
        <div class="rt-08__plate">
          <h4 class="rt-08__plate-h" id="rt-08-l1">P1 &middot; zinc silicate green</h4>
          <dl class="rt-08__spec">
            <div><dt>Decay</dt><dd>long &mdash; 1.4 s visible</dd></div>
            <div><dt>Peak</dt><dd>525 nm</dd></div>
          </dl>
        </div>
      </article>

      <article class="rt-08__tube rt-08__tube--p3" aria-labelledby="rt-08-l2">
        <div class="rt-08__screen">
          <div class="rt-08__feed" data-rt-08-feed="p3" role="log" aria-live="off" aria-relevant="additions"></div>
          <div class="rt-08__retrace" aria-hidden="true"></div>
        </div>
        <div class="rt-08__plate">
          <h4 class="rt-08__plate-h" id="rt-08-l2">P3 &middot; zinc beryllium amber</h4>
          <dl class="rt-08__spec">
            <div><dt>Decay</dt><dd>medium &mdash; 0.6 s visible</dd></div>
            <div><dt>Peak</dt><dd>602 nm</dd></div>
          </dl>
        </div>
      </article>
    </div>

    <aside class="rt-08__note">
      <h4 class="rt-08__note-h">State without colour</h4>
      <p>One hue means no colour coding. Every line below marks its state with a bracket glyph in a fixed column and a written word, so the distinction survives on a display that has exactly one colour to give.</p>
      <ul class="rt-08__key">
        <li><span class="rt-08__key-g">[ ]</span> routine</li>
        <li><span class="rt-08__key-g">[!]</span> warning</li>
        <li><span class="rt-08__key-g">[x]</span> fault</li>
        <li><span class="rt-08__key-g">[&gt;]</span> awaiting input</li>
      </ul>
    </aside>
  </div>
</section>
```
## CSS
```css
.rt-08 {
  --rt-08-mono: ui-monospace, SFMono-Regular, "Cascadia Mono", Menlo, Consolas, monospace;
  --rt-08-bloom: 3px;
  --rt-08-retrace-dur: 7s;
  --rt-08-bg: #1a1c1e;
  --rt-08-bg: oklch(23% 0.004 220);
  --rt-08-surface: #262a2d;
  --rt-08-surface: oklch(30% 0.006 220);
  --rt-08-ink: #eef1f2;
  --rt-08-ink: oklch(96% 0.003 220);
  --rt-08-ink-2: #aab2b6;
  --rt-08-ink-2: oklch(76% 0.008 220);
  --rt-08-line: #3e4548;
  --rt-08-line: oklch(37% 0.008 220);
  --rt-08-acc: #86d7c4;
  --rt-08-acc: oklch(84% 0.09 172);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-08-bg);
  color: var(--rt-08-ink);
  font-family: var(--rt-08-mono);
  -webkit-text-size-adjust: 100%;
}

.rt-08 *,
.rt-08 *::before,
.rt-08 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .rt-08 {
    --rt-08-bg: #dfe2e3;
    --rt-08-bg: oklch(90% 0.004 220);
    --rt-08-surface: #f4f6f6;
    --rt-08-surface: oklch(97% 0.002 220);
    --rt-08-ink: #16191b;
    --rt-08-ink: oklch(20% 0.005 220);
    --rt-08-ink-2: #4a5255;
    --rt-08-ink-2: oklch(43% 0.009 220);
    --rt-08-line: #aab1b4;
    --rt-08-line: oklch(75% 0.007 220);
    --rt-08-acc: #0d6d5b;
    --rt-08-acc: oklch(48% 0.1 172);
  }
}

.rt-08[data-theme="dark"] {
  --rt-08-bg: #1a1c1e;
  --rt-08-bg: oklch(23% 0.004 220);
  --rt-08-surface: #262a2d;
  --rt-08-surface: oklch(30% 0.006 220);
  --rt-08-ink: #eef1f2;
  --rt-08-ink: oklch(96% 0.003 220);
  --rt-08-ink-2: #aab2b6;
  --rt-08-ink-2: oklch(76% 0.008 220);
  --rt-08-line: #3e4548;
  --rt-08-line: oklch(37% 0.008 220);
  --rt-08-acc: #86d7c4;
  --rt-08-acc: oklch(84% 0.09 172);
}

@media (prefers-color-scheme: light) {
  .rt-08:has(.rt-08__theme-input:checked) {
    --rt-08-bg: #1a1c1e;
    --rt-08-bg: oklch(23% 0.004 220);
    --rt-08-surface: #262a2d;
    --rt-08-surface: oklch(30% 0.006 220);
    --rt-08-ink: #eef1f2;
    --rt-08-ink: oklch(96% 0.003 220);
    --rt-08-ink-2: #aab2b6;
    --rt-08-ink-2: oklch(76% 0.008 220);
    --rt-08-line: #3e4548;
    --rt-08-line: oklch(37% 0.008 220);
    --rt-08-acc: #86d7c4;
    --rt-08-acc: oklch(84% 0.09 172);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-08:has(.rt-08__theme-input:checked) {
    --rt-08-bg: #dfe2e3;
    --rt-08-bg: oklch(90% 0.004 220);
    --rt-08-surface: #f4f6f6;
    --rt-08-surface: oklch(97% 0.002 220);
    --rt-08-ink: #16191b;
    --rt-08-ink: oklch(20% 0.005 220);
    --rt-08-ink-2: #4a5255;
    --rt-08-ink-2: oklch(43% 0.009 220);
    --rt-08-line: #aab1b4;
    --rt-08-line: oklch(75% 0.007 220);
    --rt-08-acc: #0d6d5b;
    --rt-08-acc: oklch(48% 0.1 172);
  }
}

.rt-08__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-08__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-08__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-08__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-08-line);
  border-radius: 50%;
  background: var(--rt-08-surface);
  color: var(--rt-08-ink-2);
  cursor: pointer;
}

.rt-08__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-08__theme-input:focus-visible + .rt-08__theme-label {
  outline: 2px solid var(--rt-08-acc);
  outline-offset: 2px;
}

.rt-08__stage {
  max-inline-size: 74rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.85rem, 0.5rem + 2vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
}

.rt-08__head {
  display: grid;
  gap: 0.35rem;
  min-inline-size: 0;
}

.rt-08__kicker {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--rt-08-ink-2);
}

.rt-08__h {
  margin: 0;
  font-size: clamp(1.3rem, 1rem + 1.9vw, 2.05rem);
  line-height: 1.1;
  letter-spacing: -0.02em;
  font-weight: 600;
  min-inline-size: 0;
  text-wrap: balance;
}

.rt-08__pair {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.1rem;
}

.rt-08__tube {
  --rt-08-p: #33ff66;
  --rt-08-p-dim: #1c7a3a;
  --rt-08-decay: 1400ms;
  min-inline-size: 0;
  background: #3c3f3a;
  border-radius: 10px;
  padding: clamp(0.6rem, 0.4rem + 1vw, 1rem);
  box-shadow: inset 0 2px 0 rgba(255,255,255,0.22), inset 0 -3px 0 rgba(0,0,0,0.45), 0 16px 34px -18px rgba(0,0,0,0.7);
  display: grid;
  gap: 0.65rem;
}

.rt-08__tube--p3 {
  --rt-08-p: #ffb000;
  --rt-08-p-dim: #8a5f00;
  --rt-08-decay: 600ms;
  background: #423d34;
}

.rt-08__screen {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  border-radius: 14px;
  background: radial-gradient(120% 100% at 50% 40%, #0b0d0b 0%, #050605 78%);
  box-shadow: inset 0 0 0 2px #000000, inset 0 0 26px 8px rgba(0,0,0,0.8);
  min-block-size: clamp(200px, 34vw, 300px);
  padding: clamp(0.7rem, 0.5rem + 1vw, 1.1rem);
}

.rt-08__feed {
  min-inline-size: 0;
  display: grid;
  align-content: start;
  gap: 0.18em;
  font-size: clamp(0.62rem, 0.5rem + 0.7vw, 0.85rem);
  line-height: 1.5;
  color: var(--rt-08-p-dim);
}

.rt-08__ln {
  margin: 0;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  min-inline-size: 0;
  color: var(--rt-08-p-dim);
  transition: color var(--rt-08-decay) ease-out, text-shadow var(--rt-08-decay) ease-out;
}

.rt-08__ln--fresh {
  color: var(--rt-08-p);
  text-shadow: 0 0 var(--rt-08-bloom) var(--rt-08-p), 0 0 calc(var(--rt-08-bloom) * 3) var(--rt-08-p);
}

.rt-08__mark {
  display: inline-block;
  inline-size: 3ch;
}

.rt-08__retrace {
  position: absolute;
  inset-inline: 0;
  block-size: 22%;
  z-index: 3;
  pointer-events: none;
  background: linear-gradient(to bottom, rgba(255,255,255,0) 0%, rgba(255,255,255,0.045) 50%, rgba(255,255,255,0) 100%);
  animation: rt-08-retrace var(--rt-08-retrace-dur) linear infinite;
}

@keyframes rt-08-retrace {
  from {
    transform: translateY(-120%);
  }

  to {
    transform: translateY(560%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .rt-08__retrace {
    animation: none;
    opacity: 0;
  }

  .rt-08__ln {
    transition: none;
  }
}

.rt-08__plate {
  display: grid;
  gap: 0.4rem;
  min-inline-size: 0;
}

.rt-08__plate-h {
  margin: 0;
  font-size: 0.78rem;
  letter-spacing: 0.06em;
  color: #e8e6dd;
  min-inline-size: 0;
}

.rt-08__spec {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem 1.2rem;
  font-size: 0.7rem;
  color: #c3c0b5;
}

.rt-08__spec > div {
  display: flex;
  gap: 0.4rem;
  min-inline-size: 0;
}

.rt-08__spec dt {
  margin: 0;
  color: #9c998f;
}

.rt-08__spec dd {
  margin: 0;
}

.rt-08__note {
  min-inline-size: 0;
  background: var(--rt-08-surface);
  border: 1px solid var(--rt-08-line);
  padding: clamp(0.85rem, 0.6rem + 1vw, 1.2rem);
  display: grid;
  gap: 0.6rem;
}

.rt-08__note-h {
  margin: 0;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rt-08-ink-2);
}

.rt-08__note p {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.6;
  color: var(--rt-08-ink-2);
  max-inline-size: 68ch;
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-08__key {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 1.2rem;
  font-size: 0.8rem;
}

.rt-08__key li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-inline-size: 0;
}

.rt-08__key-g {
  color: var(--rt-08-acc);
}

@media (min-width: 52rem) {
  .rt-08__pair {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```

## JavaScript
```js
const root = document.currentScript.closest('.rt-08') || document.querySelector('.rt-08');
const feeds = [...root.querySelectorAll('[data-rt-08-feed]')];
const lines = [
  ['[ ]', 'MEM CHECK 640K OK'], ['[ ]', 'SEEK TRK 00 SEC 01'],
  ['[!]', 'PARITY RETRY 1 OF 3'], ['[ ]', 'BUFFER FLUSHED 4096B'],
  ['[x]', 'DEVICE 2 NOT READY'], ['[ ]', 'LINK 1200 BAUD 8N1'],
  ['[>]', 'AWAITING OPERATOR'], ['[ ]', 'SPOOL QUEUE EMPTY']
];
let i = 0;
const write = () => {
  for (const feed of feeds) {
    const p = document.createElement('p');
    p.className = 'rt-08__ln rt-08__ln--fresh';
    const m = document.createElement('span');
    m.className = 'rt-08__mark';
    m.textContent = lines[i % lines.length][0];
    p.append(m, lines[i % lines.length][1]);
    feed.append(p);
    requestAnimationFrame(() => requestAnimationFrame(() => p.classList.remove('rt-08__ln--fresh')));
    while (feed.childElementCount > 9) feed.firstElementChild.remove();
  }
  i += 1;
};
write();
const timer = setInterval(write, 1500);
root.__rtCleanup = () => { clearInterval(timer); feeds.forEach((f) => { f.textContent = ''; }); };
```
