---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-gradient-cta-button/"
title: "CSS Gradient CTA Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A conversion-grade CTA with a conic gradient ring that rotates continuously, a soft bloom underneath, and a mesh gradient body that shifts on hover."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient CTA Button
Source: https://codefronts.com/components/css-buttons/css-gradient-cta-button/

A conversion-grade CTA with a conic gradient ring that rotates continuously, a soft bloom underneath, and a mesh gradient body that shifts on hover. The rotation is possible at all because @property registers the angle as an <angle> type — plain custom properties cannot be animated.
## HTML
```html
<div class="cb-05">
  <div class="cb-05__stage">
    <button class="cb-05__btn" type="button">
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M13 3 4.5 13.5H11l-1 7.5 8.5-10.5H12l1-7.5z"/></svg>
      <span>Upgrade to Pro</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap');

@property --cb-05-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 135deg;
}

.cb-05 {
  --bg: #08070d;
  --c1: #6d28d9;
  --c2: #2dd4bf;
  --c3: #f472b6;
  --ink: #ffffff;
  --body: #141024;
  --bloom: .55;
  --radius: 1rem;
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(60rem 40rem at 50% 120%, color-mix(in oklab,var(--c1) 22%,transparent), transparent 70%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-05 {
    --c1: oklch(52% .24 293);
    --c2: oklch(80% .14 182);
    --c3: oklch(74% .17 349);
    --body: oklch(20% .04 290);
  }
}

@media (prefers-color-scheme: light) {
  .cb-05:not([data-theme="dark"]) {
    --bg: #f5f4fb;
    --body: #1a1530;
    --bloom: .4;
  }
}

.cb-05[data-theme="light"] {
  --bg: #f5f4fb;
  --body: #1a1530;
  --bloom: .4;
}

.cb-05,
.cb-05 *,
.cb-05 *::before,
.cb-05 *::after {
  box-sizing: border-box;
}

.cb-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-05__btn {
  position: relative;
  isolation: isolate;
  cursor: pointer;
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .55rem;
  min-height: 3.5rem;
  padding: 0 1.9rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.005em;
  color: var(--ink);
  background: radial-gradient(120% 140% at 15% 0%, color-mix(in oklab,var(--c1) 55%,transparent), transparent 60%), radial-gradient(120% 140% at 90% 100%, color-mix(in oklab,var(--c2) 35%,transparent), transparent 60%), var(--body);
  background-size: 150% 150%,150% 150%,100% 100%;
  background-position: 0% 0%,100% 100%,0 0;
  transition: translate .3s cubic-bezier(.16,1,.3,1), background-position .6s cubic-bezier(.16,1,.3,1), scale .18s ease;
}

.cb-05__btn svg {
  width: 1.1rem;
  height: 1.1rem;
  color: var(--c2);
}

.cb-05__btn::before,
.cb-05__btn::after {
  content: '';
  position: absolute;
  inset: -2px;
  z-index: -1;
  border-radius: inherit;
  background: conic-gradient(from var(--cb-05-a),var(--c1),var(--c2),var(--c3),var(--c1));
  animation: cb-05-spin 4.5s linear infinite;
}

.cb-05__btn::after {
  inset: 2px;
  filter: blur(20px);
  opacity: var(--bloom);
  transition: opacity .35s ease;
}

@keyframes cb-05-spin {
  to {
    --cb-05-a: 495deg;
  }
}

.cb-05__btn:hover {
  translate: 0 -2px;
  background-position: 30% 20%,70% 80%,0 0;
}

.cb-05__btn:hover::after {
  opacity: calc(var(--bloom) + .35);
}

.cb-05__btn:active {
  scale: .98;
  translate: 0 0;
}

.cb-05__btn:focus-visible {
  outline: 2px solid var(--c2);
  outline-offset: 5px;
}

.cb-05__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.85);
  opacity: .55;
}

.cb-05__btn:disabled::before,
.cb-05__btn:disabled::after {
  animation-play-state: paused;
}

@media (prefers-reduced-motion: reduce) {
  .cb-05__btn::before,
    .cb-05__btn::after {
    animation: none;
  }

  .cb-05__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-05__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .cb-05__btn::before,
    .cb-05__btn::after {
    display: none;
  }
}
```
