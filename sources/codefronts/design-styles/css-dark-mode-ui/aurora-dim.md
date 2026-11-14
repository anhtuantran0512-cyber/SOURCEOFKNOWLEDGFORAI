---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/aurora-dim/"
title: "Aurora Dim Dark Mode Landing Panel"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A launch hero with a real atmosphere: three offset radial gradients — green, violet, cyan — masked into the top of the panel so the aurora fades before it…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Dim Dark Mode Landing Panel
Source: https://codefronts.com/design-styles/css-dark-mode-ui/aurora-dim/

A launch hero with a real atmosphere: three offset radial gradients — green, violet, cyan — masked into the top of the panel so the aurora fades before it reaches the text. Headline, subhead, dual CTAs and a trust bar, sized to fill a viewport at any aspect ratio. The whole effect is background layers and one masked pseudo-element; nothing animates unless the visitor allows motion.
## HTML
```html
<div class="dmu-21">
  <div class="dmu-21__stage">
    <section class="dmu-21__panel">
      <span class="dmu-21__aurora" aria-hidden="true"></span>

      <nav class="dmu-21__nav" aria-label="Product">
        <span class="dmu-21__brand">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18 12 5l8 13Z"/></svg>
          Northlight
        </span>
        <span class="dmu-21__navLinks">
          <a href="#dmu-21">Platform</a>
          <a href="#dmu-21">Docs</a>
          <a href="#dmu-21">Pricing</a>
        </span>
        <span class="dmu-21__navTag">v4.2 out now</span>
      </nav>

      <div class="dmu-21__hero">
        <p class="dmu-21__eyebrow">
          <span class="dmu-21__dot" aria-hidden="true"></span>
          Edge runtime &middot; 34 regions live
        </p>
        <h1 class="dmu-21__h1">Ship the dark theme<br>you actually designed</h1>
        <p class="dmu-21__sub">Token-level theming, per-scheme contrast audits and a preview that renders both palettes side by side. No inversion filters, no second stylesheet to maintain.</p>

        <div class="dmu-21__ctas">
          <a class="dmu-21__btn dmu-21__btn--primary" href="#dmu-21">
            Start building
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 12h13"/><path d="M12 6.5 17.5 12 12 17.5"/></svg>
          </a>
          <a class="dmu-21__btn" href="#dmu-21">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 8.2 15.8 12l-6.3 3.8Z"/><circle cx="12" cy="12" r="8.4"/></svg>
            Watch the 3-min tour
          </a>
        </div>

        <div class="dmu-21__trust">
          <p class="dmu-21__trustLabel">Powering theming at</p>
          <div class="dmu-21__logos">
            <span>MERIDIAN</span><span>Northwind</span><span>Cadence</span><span>ATLAS</span><span>Foxglove</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
.dmu-21 {
  --bg: #06070c;
  --panel: #080a11;
  --raised: #101425;
  --ink: #eef1f8;
  --muted: #98a0b8;
  --line: rgba(238,241,248,.12);
  --grid: rgba(238,241,248,.035);
  --a-green: rgba(52,211,153,.30);
  --a-violet: rgba(139,92,246,.34);
  --a-cyan: rgba(56,189,248,.28);
  --accent: #c7d2fe;
  --accent-ink: #0a0f22;
  --focus: #a5b4fc;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-21,
.dmu-21 *,
.dmu-21 *::before,
.dmu-21 *::after {
  box-sizing: border-box;
}

.dmu-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(.75rem,3vw,2.5rem);
}

.dmu-21__panel {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  width: min(74rem,100%);
  min-height: min(44rem,88vh);
  display: grid;
  grid-template-rows: auto 1fr;
  gap: clamp(1.5rem,4vw,3rem);
  padding: clamp(1.1rem,3vw,2rem);
  border-radius: 1.5rem;
  background: var(--panel);
  border: 1px solid var(--line);
  background-image: repeating-linear-gradient(90deg,var(--grid) 0 1px,transparent 1px 4.5rem), repeating-linear-gradient(0deg,var(--grid) 0 1px,transparent 1px 4.5rem);
}

.dmu-21__aurora {
  position: absolute;
  z-index: -1;
  inset: -20% -10% auto -10%;
  height: 70%;
  background: radial-gradient(38rem 24rem at 18% 18%,var(--a-green),transparent 70%), radial-gradient(34rem 22rem at 60% 4%,var(--a-violet),transparent 68%), radial-gradient(30rem 20rem at 92% 22%,var(--a-cyan),transparent 66%);
  filter: blur(18px) saturate(1.05);
  -webkit-mask-image: linear-gradient(180deg,#000 0%,rgba(0,0,0,.55) 45%,transparent 80%);
  mask-image: linear-gradient(180deg,#000 0%,rgba(0,0,0,.55) 45%,transparent 80%);
  animation: dmu-21-drift 18s ease-in-out infinite alternate;
}

@keyframes dmu-21-drift {
  0% {
    translate: -2% 0;
    opacity: .85;
  }

  100% {
    translate: 3% -2%;
    opacity: 1;
  }
}

.dmu-21__nav {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.dmu-21__brand {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.dmu-21__brand svg {
  width: 1.15rem;
  height: 1.15rem;
  color: var(--a-cyan);
}

.dmu-21__navLinks {
  display: flex;
  gap: .35rem;
  margin-left: .75rem;
}

.dmu-21__navLinks a {
  padding: .45rem .7rem;
  border-radius: .5rem;
  font-size: .83rem;
  color: var(--muted);
  text-decoration: none;
  transition: background-color .18s ease, color .18s ease;
}

.dmu-21__navLinks a:hover {
  color: var(--ink);
  background: rgba(255,255,255,.05);
}

.dmu-21__navLinks a:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-21__navTag {
  margin-left: auto;
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .35rem .6rem;
  border-radius: 999px;
  border: 1px solid var(--line);
}

.dmu-21__hero {
  display: grid;
  gap: .9rem;
  align-content: center;
  justify-items: start;
  max-width: 44rem;
  padding-bottom: 1rem;
}

.dmu-21__eyebrow {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  font-size: .76rem;
  letter-spacing: .02em;
  color: var(--muted);
  padding: .35rem .7rem;
  border-radius: 999px;
  background: rgba(255,255,255,.04);
  border: 1px solid var(--line);
}

.dmu-21__dot {
  width: .45rem;
  height: .45rem;
  border-radius: 50%;
  background: #34d399;
  box-shadow: 0 0 0 3px rgba(52,211,153,.22);
}

.dmu-21__h1 {
  margin: 0;
  font-size: clamp(2.1rem,6.4vw,4rem);
  font-weight: 640;
  line-height: 1.04;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.dmu-21__sub {
  margin: 0 0 .4rem;
  font-size: clamp(.95rem,1.6vw,1.08rem);
  line-height: 1.65;
  color: var(--muted);
  max-width: 46ch;
  text-wrap: pretty;
}

.dmu-21__ctas {
  display: flex;
  gap: .6rem;
  flex-wrap: wrap;
}

.dmu-21__btn {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-height: 3.1rem;
  padding: 0 1.35rem;
  border-radius: .8rem;
  font-size: .92rem;
  font-weight: 560;
  text-decoration: none;
  color: var(--ink);
  background: rgba(255,255,255,.05);
  border: 1px solid var(--line);
  transition: translate .2s cubic-bezier(.16,1,.3,1), background-color .2s ease;
}

.dmu-21__btn svg {
  width: 1.1rem;
  height: 1.1rem;
}

.dmu-21__btn:hover {
  translate: 0 -2px;
  background: rgba(255,255,255,.09);
}

.dmu-21__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-21__btn--primary {
  background: var(--accent);
  color: var(--accent-ink);
  border-color: transparent;
  font-weight: 620;
  box-shadow: 0 0 32px rgba(199,210,254,.22);
}

.dmu-21__btn--primary:hover {
  background: #ffffff;
}

.dmu-21__trust {
  display: grid;
  gap: .55rem;
  margin-top: .85rem;
  padding-top: 1.1rem;
  border-top: 1px solid var(--line);
  width: 100%;
}

.dmu-21__trustLabel {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-21__logos {
  display: flex;
  gap: 1.4rem;
  flex-wrap: wrap;
  align-items: center;
}

.dmu-21__logos span {
  font-size: .88rem;
  font-weight: 560;
  letter-spacing: -.01em;
  color: var(--muted);
  opacity: .9;
}

.dmu-21__logos span:nth-child(1),
.dmu-21__logos span:nth-child(4) {
  font-family: var(--mono);
  font-size: .8rem;
  letter-spacing: .08em;
}

@media (prefers-reduced-motion: reduce) {
  .dmu-21__aurora {
    animation: none;
  }

  .dmu-21__btn,
    .dmu-21__navLinks a {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-21__panel {
    background: Canvas;
    border-color: CanvasText;
    background-image: none;
  }

  .dmu-21__aurora {
    display: none;
  }

  .dmu-21__btn--primary {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }
}
```
