---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-frosted-ice-cube-button/"
title: "CSS Frosted Ice Cube Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Real frosted glass over a photograph: backdrop-filter blurs and desaturates whatever is behind it, a bright inner rim catches the light on two edges only,…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Frosted Ice Cube Button
Source: https://codefronts.com/components/css-buttons/css-frosted-ice-cube-button/

Real frosted glass over a photograph: backdrop-filter blurs and desaturates whatever is behind it, a bright inner rim catches the light on two edges only, frost bloom collects in the corners, and pressing sends a hairline crack across the face.
## HTML
```html
<div class="cb-23">
  <div class="cb-23__stage">
    <img class="cb-23__bg" src="https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=1600&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="1600" height="1000" loading="lazy" decoding="async">
    <button class="cb-23__btn" type="button">
      <span class="cb-23__frost" aria-hidden="true"></span>
      <span class="cb-23__crack" aria-hidden="true"></span>
      <span class="cb-23__label">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><path d="M12 3v18M4 7.5l16 9M20 7.5l-16 9"/></svg>
        <span>Chill mode</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

.cb-23 {
  --fallback: #123044;
  --ink: #f2fbff;
  --rim: 255,255,255;
  --radius: 1.1rem;
  --sans: "Outfit",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fallback);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-23,
.cb-23 *,
.cb-23 *::before,
.cb-23 *::after {
  box-sizing: border-box;
}

.cb-23__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
  overflow: hidden;
}

.cb-23__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--fallback);
  filter: saturate(1.05) brightness(.92);
}

.cb-23__btn {
  position: relative;
  overflow: hidden;
  z-index: 1;
  cursor: pointer;
  min-height: 3.75rem;
  padding: 0 2.1rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.005em;
  color: var(--ink);
  background: linear-gradient(150deg, rgba(255,255,255,.30), rgba(255,255,255,.08));
  box-shadow: inset 1px 1px 0 rgba(var(--rim),.7), inset -1px -1px 0 rgba(var(--rim),.18), inset 0 0 24px rgba(var(--rim),.14), 0 20px 44px -20px rgba(4,16,26,.75);
  text-shadow: 0 1px 12px rgba(4,20,32,.65);
  -webkit-backdrop-filter: blur(16px) saturate(1.5) brightness(1.05);
  backdrop-filter: blur(16px) saturate(1.5) brightness(1.05);
  transition: translate .3s cubic-bezier(.16,1,.3,1), box-shadow .3s ease, scale .18s ease;
}

@supports not ((backdrop-filter: blur(4px)) or (-webkit-backdrop-filter: blur(4px))) {
  .cb-23__btn {
    background: linear-gradient(150deg, rgba(255,255,255,.55), rgba(210,235,250,.42));
    color: #0b2434;
    text-shadow: none;
  }
}

.cb-23__label {
  position: relative;
  z-index: 3;
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .55rem;
}

.cb-23__label svg {
  width: 1.15rem;
  height: 1.15rem;
}

.cb-23__frost {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  opacity: .85;
  background: radial-gradient(4rem 3rem at 8% 4%, rgba(255,255,255,.42), transparent 70%), radial-gradient(5rem 3.5rem at 96% 100%, rgba(255,255,255,.34), transparent 72%), radial-gradient(.06rem .06rem at 22% 62%, rgba(255,255,255,.9) 99%, transparent), radial-gradient(.05rem .05rem at 71% 28%, rgba(255,255,255,.8) 99%, transparent);
  background-size: 100% 100%, 100% 100%, 9px 9px, 14px 14px;
  transition: opacity .35s ease;
}

.cb-23__crack {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  opacity: 0;
  background: rgba(255,255,255,.95);
  clip-path: polygon(0 52%,18% 44%,26% 58%,44% 40%,58% 56%,72% 38%,86% 52%,100% 44%,100% 46%,86% 54%,72% 41%,58% 59%,44% 43%,26% 61%,18% 47%,0 54%);
}

.cb-23__btn:hover {
  translate: 0 -2px;
  box-shadow: inset 1px 1px 0 rgba(var(--rim),.85), inset -1px -1px 0 rgba(var(--rim),.22), inset 0 0 30px rgba(var(--rim),.2), 0 26px 50px -20px rgba(4,16,26,.8);
}

.cb-23__btn:hover .cb-23__frost {
  opacity: 1;
}

.cb-23__btn:focus-visible {
  outline: 2px solid rgba(var(--rim),.9);
  outline-offset: 4px;
}

.cb-23__btn:active {
  scale: .985;
}

.cb-23__btn:active .cb-23__crack {
  animation: cb-23-crack .5s ease-out;
}

@keyframes cb-23-crack {
  0% {
    opacity: 0;
    scale: .4 1;
  }

  30% {
    opacity: .9;
  }

  100% {
    opacity: 0;
    scale: 1 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-23__btn,
    .cb-23__frost {
    transition: none;
  }

  .cb-23__crack {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-23__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
    box-shadow: none;
    text-shadow: none;
  }

  .cb-23__frost,
    .cb-23__crack {
    display: none;
  }
}
```
