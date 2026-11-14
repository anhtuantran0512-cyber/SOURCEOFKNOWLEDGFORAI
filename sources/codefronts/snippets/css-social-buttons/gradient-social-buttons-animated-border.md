---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/gradient-social-buttons-animated-border/"
title: "Gradient Social Buttons Animated Border"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "A conic gradient rotates around each button's edge while the face stays flat and readable."
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Social Buttons Animated Border
Source: https://codefronts.com/snippets/css-social-buttons/gradient-social-buttons-animated-border/

A conic gradient rotates around each button's edge while the face stays flat and readable. The rotation works because the angle is a custom property registered with @property — an unregistered property is just a string, cannot be interpolated, and is the single most common reason this effect silently does nothing.
## HTML
```html
<div class="soc-19">
  <div class="soc-19__stage">
    <div class="soc-19__card">
      <p class="soc-19__eyebrow">Featured</p>
      <h2 class="soc-19__title">Two controls worth the extra paint</h2>
      <div class="soc-19__row">
        <a class="soc-19__btn" href="https://example.com/@alexchen" target="_blank" rel="noopener">
          <span class="soc-19__face">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="2.6" y="5.2" width="18.8" height="13.6" rx="4.4"/><path d="m10.4 9.4 5 2.6-5 2.6Z" fill="currentColor"/></svg>
            <span>Subscribe on YouTube</span>
          </span>
        </a>
        <a class="soc-19__btn soc-19__btn--alt" href="https://example.com/discord" target="_blank" rel="noopener">
          <span class="soc-19__face">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5.5 17.5 4 8.2a14 14 0 0 1 16 0l-1.5 9.3a11 11 0 0 1-13 0Z"/><circle cx="9.4" cy="12.4" r="1.1" fill="currentColor" stroke="none"/><circle cx="14.6" cy="12.4" r="1.1" fill="currentColor" stroke="none"/></svg>
            <span>Join the Discord</span>
          </span>
        </a>
      </div>
      <p class="soc-19__note">The angle is a registered custom property — that is the whole trick.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

@property --soc-19-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.soc-19 {
  --bg: #0b0b10;
  --surface: #15151c;
  --fg: #f4f4f8;
  --muted: #9a9aa8;
  --line: #2a2a34;
  --ring: #8ab4ff;
  --g1: #ff5f6d;
  --g2: #ffc371;
  --g3: #5f8bff;
  --g4: #c86dff;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: light) {
  .soc-19:not([data-theme="dark"]) {
    --bg: #f4f4f6;
    --surface: #ffffff;
    --fg: #0e0e12;
    --muted: #6a6a76;
    --line: #e5e5ea;
    --ring: #3d63ff;
  }
}

.soc-19[data-theme="light"] {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
}

.soc-19,
.soc-19 *,
.soc-19 *::before,
.soc-19 *::after {
  box-sizing: border-box;
}

.soc-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-19__card {
  inline-size: min(32rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.35rem;
  padding: clamp(1.5rem,4vw,2.25rem);
}

.soc-19__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-19__title {
  margin: 0 0 1.7rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.35rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.soc-19__row {
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
}

.soc-19__btn {
  position: relative;
  isolation: isolate;
  display: inline-block;
  min-inline-size: 0;
  border-radius: .95rem;
  text-decoration: none;
  color: var(--fg);
  background: linear-gradient(120deg,var(--g1),var(--g2),var(--g3),var(--g4));
  padding: 2px;
  transition: translate .2s cubic-bezier(.16,1,.3,1);
}

.soc-19__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background: linear-gradient(120deg,var(--g1),var(--g2),var(--g3),var(--g4));
  filter: blur(12px);
  opacity: .35;
  transition: opacity .25s ease;
}

@supports (background: conic-gradient(from 1deg, red, blue)) {
  .soc-19__btn {
    background: conic-gradient(from var(--soc-19-angle),var(--g1),var(--g2),var(--g3),var(--g4),var(--g1));
    animation: soc-19-spin 6s linear infinite;
  }

  .soc-19__btn::before {
    background: conic-gradient(from var(--soc-19-angle),var(--g1),var(--g2),var(--g3),var(--g4),var(--g1));
  }
}

@keyframes soc-19-spin {
  to {
    --soc-19-angle: 360deg;
  }
}

.soc-19__btn--alt {
  animation-duration: 9s;
  animation-direction: reverse;
}

.soc-19__face {
  display: flex;
  align-items: center;
  gap: .6rem;
  min-block-size: 2.75rem;
  padding: 0 1.15rem;
  border-radius: .8rem;
  background: var(--surface);
  color: var(--fg);
  font-size: .92rem;
  font-weight: 600;
  letter-spacing: -.01em;
  min-inline-size: 0;
}

.soc-19__face svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
  flex: none;
}

.soc-19__face span {
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.soc-19__btn:hover {
  translate: 0 -2px;
  animation-duration: 2.4s;
}

.soc-19__btn:hover::before {
  opacity: .6;
}

.soc-19__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 4px;
}

.soc-19__note {
  margin: 1.6rem 0 0;
  font-size: .8rem;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .soc-19__btn {
    animation: none;
    transition-duration: 1ms;
  }

  .soc-19__btn:hover {
    translate: none;
    animation: none;
  }
}

@media (forced-colors: active) {
  .soc-19__btn {
    background: ButtonFace;
    border: 1px solid ButtonText;
    animation: none;
  }

  .soc-19__btn::before {
    display: none;
  }

  .soc-19__face {
    background: ButtonFace;
    color: ButtonText;
  }
}
```
