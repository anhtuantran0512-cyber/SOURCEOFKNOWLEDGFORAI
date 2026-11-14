---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/phosphor-card/"
title: "Phosphor Glow Dark Mode Card"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A product-launch card with a genuinely emissive CTA: the glow is a wide, low-alpha box-shadow in the accent hue, layered under a tight inner highlight so the…"
has_js: "true"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Phosphor Glow Dark Mode Card
Source: https://codefronts.com/design-styles/css-dark-mode-ui/phosphor-card/

A product-launch card with a genuinely emissive CTA: the glow is a wide, low-alpha box-shadow in the accent hue, layered under a tight inner highlight so the button looks lit rather than blurred. A live countdown ticks in tabular figures (fifteen lines of vanilla JS, no theming logic), and the ambient pulse behind the card stops dead under prefers-reduced-motion.
## HTML
```html
<div class="dmu-20">
  <div class="dmu-20__stage">
    <article class="dmu-20__card">
      <span class="dmu-20__halo" aria-hidden="true"></span>

      <header class="dmu-20__head">
        <span class="dmu-20__pill">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 3.2 5.8 13.4h4.6L10 20.8l7.4-10.4h-4.6Z"/></svg>
          Launching in
        </span>
        <p class="dmu-20__version">v4.2 &middot; Phosphor</p>
      </header>

      <h1 class="dmu-20__h1">Command palette,<br>rebuilt for the dark</h1>
      <p class="dmu-20__lede">Fuzzy search over every surface, 60fps on a five-year-old laptop, and a theme layer that flips without a single line of script.</p>

      <div class="dmu-20__clock" role="timer" aria-live="off">
        <div class="dmu-20__unit"><b id="dmu-20-d">02</b><span>days</span></div>
        <div class="dmu-20__unit"><b id="dmu-20-h">14</b><span>hrs</span></div>
        <div class="dmu-20__unit"><b id="dmu-20-m">37</b><span>min</span></div>
        <div class="dmu-20__unit"><b id="dmu-20-s">05</b><span>sec</span></div>
      </div>

      <div class="dmu-20__row">
        <label class="dmu-20__sr" for="dmu-20-email">Email address</label>
        <input class="dmu-20__input" id="dmu-20-email" type="email" inputmode="email" placeholder="[email protected]" autocomplete="email">
        <button class="dmu-20__cta" type="button">
          Notify me
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 12h13"/><path d="M12 6.5 17.5 12 12 17.5"/></svg>
        </button>
      </div>

      <footer class="dmu-20__foot">
        <span class="dmu-20__facePile" aria-hidden="true"><i>AC</i><i>PS</i><i>JL</i></span>
        <p class="dmu-20__footText">2,481 developers on the list &middot; no spam, one email</p>
      </footer>
    </article>
  </div>
</div>
```
## CSS
```css
.dmu-20 {
  --bg: #08070d;
  --surface: #111019;
  --raised: #171626;
  --ink: #f2f0fa;
  --muted: #9b97b5;
  --line: #262338;
  --accent: #8b5cf6;
  --accent-hi: #a78bfa;
  --accent-ink: #ffffff;
  --glow: rgba(139,92,246,.42);
  --glow-far: rgba(139,92,246,.20);
  --glow-hover: rgba(167,139,250,.55);
  --focus: #c4b5fd;
  --shadow: rgba(0,0,0,.8);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(120% 80% at 50% -10%,#151228,var(--bg) 62%),var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-20,
.dmu-20 *,
.dmu-20 *::before,
.dmu-20 *::after {
  box-sizing: border-box;
}

.dmu-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-20__card {
  position: relative;
  isolation: isolate;
  width: min(38rem,100%);
  display: grid;
  gap: .85rem;
  padding: clamp(1.5rem,4vw,2.5rem);
  border-radius: 1.4rem;
  background: linear-gradient(180deg,var(--raised),var(--surface));
  border: 1px solid var(--line);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.05), 0 48px 90px -55px var(--shadow);
}

.dmu-20__halo {
  position: absolute;
  z-index: -1;
  left: 50%;
  bottom: -4rem;
  translate: -50% 0;
  width: 22rem;
  height: 14rem;
  border-radius: 50%;
  background: radial-gradient(circle,var(--glow) 0%,transparent 68%);
  filter: blur(28px);
  opacity: .7;
  animation: dmu-20-breathe 5.5s ease-in-out infinite;
}

@keyframes dmu-20-breathe {
  0%,
    100% {
    opacity: .55;
    scale: 1;
  }

  50% {
    opacity: .85;
    scale: 1.06;
  }
}

.dmu-20__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.dmu-20__pill {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  padding: .32rem .6rem;
  border-radius: 999px;
  font-size: .72rem;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: var(--accent-hi);
  background: color-mix(in oklab,var(--accent) 16%,transparent);
  border: 1px solid color-mix(in oklab,var(--accent) 38%,transparent);
}

.dmu-20__pill svg {
  width: .85rem;
  height: .85rem;
}

.dmu-20__version {
  margin: 0;
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--muted);
}

.dmu-20__h1 {
  margin: 0;
  font-size: clamp(1.75rem,4.6vw,2.6rem);
  font-weight: 650;
  line-height: 1.1;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.dmu-20__lede {
  margin: 0 0 .3rem;
  font-size: .95rem;
  line-height: 1.65;
  color: var(--muted);
  max-width: 44ch;
  text-wrap: pretty;
}

.dmu-20__clock {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .5rem;
}

.dmu-20__unit {
  display: grid;
  gap: .15rem;
  justify-items: center;
  padding: .7rem .4rem;
  border-radius: .75rem;
  background: color-mix(in oklab,var(--surface),white 4%);
  border: 1px solid var(--line);
}

.dmu-20__unit b {
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  font-size: 1.45rem;
  font-weight: 600;
  letter-spacing: -.04em;
}

.dmu-20__unit span {
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-20__row {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
  margin-top: .2rem;
}

.dmu-20__input {
  flex: 1 1 12rem;
  min-height: 3rem;
  padding: 0 .95rem;
  border-radius: .75rem;
  font: inherit;
  font-size: .9rem;
  background: #0c0b13;
  color: var(--ink);
  border: 1px solid var(--line);
  transition: border-color .18s ease;
}

.dmu-20__input::placeholder {
  color: var(--muted);
}

.dmu-20__input:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
  border-color: var(--accent);
}

.dmu-20__cta {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-height: 3rem;
  padding: 0 1.3rem;
  border: 0;
  border-radius: .75rem;
  cursor: pointer;
  font: inherit;
  font-size: .92rem;
  font-weight: 600;
  letter-spacing: -.01em;
  background: linear-gradient(180deg,var(--accent-hi),var(--accent));
  color: var(--accent-ink);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.28), 0 2px 8px rgba(0,0,0,.5), 0 0 40px var(--glow), 0 0 90px var(--glow-far);
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .25s ease;
}

.dmu-20__cta svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-20__cta:hover {
  translate: 0 -2px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.32), 0 4px 12px rgba(0,0,0,.55), 0 0 56px var(--glow-hover), 0 0 110px var(--glow-far);
}

.dmu-20__cta:active {
  translate: 0 0;
}

.dmu-20__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-20__foot {
  display: flex;
  align-items: center;
  gap: .7rem;
  flex-wrap: wrap;
  padding-top: .9rem;
  border-top: 1px solid var(--line);
}

.dmu-20__facePile {
  display: flex;
}

.dmu-20__facePile i {
  display: grid;
  place-items: center;
  width: 1.85rem;
  height: 1.85rem;
  border-radius: 50%;
  font-style: normal;
  font-size: .64rem;
  font-weight: 650;
  letter-spacing: .02em;
  background: var(--raised);
  color: var(--muted);
  border: 1px solid var(--line);
  margin-left: -.45rem;
}

.dmu-20__facePile i:first-child {
  margin-left: 0;
}

.dmu-20__footText {
  margin: 0;
  font-size: .78rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-20__halo {
    animation: none;
  }

  .dmu-20__cta,
    .dmu-20__input {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-20__card,
    .dmu-20__unit,
    .dmu-20__input {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-20__halo {
    display: none;
  }

  .dmu-20__cta {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }
}
```

## JavaScript
```js
const dmu20 = document.querySelector('.dmu-20');
if (dmu20) {
  const pad = (n) => String(n).padStart(2, '0');
  const target = Date.now() + 2 * 864e5 + 14 * 36e5 + 37 * 6e4;
  const out = {
    d: dmu20.querySelector('#dmu-20-d'), h: dmu20.querySelector('#dmu-20-h'),
    m: dmu20.querySelector('#dmu-20-m'), s: dmu20.querySelector('#dmu-20-s'),
  };
  const tick = () => {
    const left = Math.max(0, target - Date.now()) / 1000 | 0;
    out.d.textContent = pad(left / 86400 | 0);
    out.h.textContent = pad(left / 3600 % 24 | 0);
    out.m.textContent = pad(left / 60 % 60 | 0);
    out.s.textContent = pad(left % 60);
  };
  tick();
  setInterval(tick, 1000);
}
```
