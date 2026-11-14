---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-like-heart-button/"
title: "CSS Like Heart Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A like button with a springy heart pop, eight radial sparks and a count that rolls over — and not one line of JavaScript."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Like Heart Button
Source: https://codefronts.com/components/css-buttons/css-like-heart-button/

A like button with a springy heart pop, eight radial sparks and a count that rolls over — and not one line of JavaScript. State lives in a checkbox, the sparks are generated from a shared keyframe with per-child custom properties, and the count slides between two spans so the digits animate like an odometer.
## HTML
```html
<div class="cb-11">
  <div class="cb-11__stage">
    <label class="cb-11__btn">
      <input type="checkbox" aria-label="Like this post">
      <span class="cb-11__ico" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20.2s-7.4-4.3-7.4-9.4A4.3 4.3 0 0 1 12 8.1a4.3 4.3 0 0 1 7.4 2.7c0 5.1-7.4 9.4-7.4 9.4z"/></svg>
        <span class="cb-11__sparks">
          <span class="cb-11__spark"></span><span class="cb-11__spark"></span><span class="cb-11__spark"></span><span class="cb-11__spark"></span>
          <span class="cb-11__spark"></span><span class="cb-11__spark"></span><span class="cb-11__spark"></span><span class="cb-11__spark"></span>
        </span>
      </span>
      <span class="cb-11__count" aria-hidden="true"><span class="cb-11__roll"><span>2,417</span><span>2,418</span></span></span>
    </label>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&display=swap');

.cb-11 {
  --bg: #fbf7f7;
  --surface: #ffffff;
  --line: #eadfe0;
  --text: #241a1c;
  --muted: #8a7a7d;
  --like: #e11d48;
  --radius: 999px;
  --spring: linear(0,.45 7%,.85 15%,1.12 23%,1.18 28%,1.1 36%,1 50%,1);
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-11 {
    --bg: oklch(97.6% .006 15);
    --like: oklch(56% .22 12);
    --line: oklch(91% .014 15);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-11:not([data-theme="light"]) {
    --bg: #0e0a0b;
    --surface: #181112;
    --line: #2c2022;
    --text: #f6eef0;
    --muted: #a5949a;
    --like: #fb7185;
  }
}

.cb-11[data-theme="dark"] {
  --bg: #0e0a0b;
  --surface: #181112;
  --line: #2c2022;
  --text: #f6eef0;
  --muted: #a5949a;
  --like: #fb7185;
}

.cb-11,
.cb-11 *,
.cb-11 *::before,
.cb-11 *::after {
  box-sizing: border-box;
}

.cb-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-11__btn {
  position: relative;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-height: 2.9rem;
  padding: 0 1.1rem 0 .9rem;
  border-radius: var(--radius);
  background: var(--surface);
  border: 1px solid var(--line);
  font-size: .9375rem;
  font-weight: 700;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  box-shadow: 0 8px 20px -16px color-mix(in oklab,var(--text) 60%,transparent);
  transition: border-color .25s ease, color .25s ease, scale .2s cubic-bezier(.16,1,.3,1);
  -webkit-tap-highlight-color: transparent;
}

.cb-11__btn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-11__ico {
  position: relative;
  display: grid;
  place-items: center;
  width: 1.6rem;
  height: 1.6rem;
  color: var(--muted);
}

.cb-11__ico svg {
  width: 1.45rem;
  height: 1.45rem;
  transition: scale .35s cubic-bezier(.16,1,.3,1), color .25s ease, fill .25s ease;
}

.cb-11__btn:hover {
  border-color: color-mix(in oklab,var(--like) 45%,var(--line));
  color: var(--text);
  scale: 1.02;
}

.cb-11__btn:hover .cb-11__ico {
  color: var(--like);
}

.cb-11__btn:active {
  scale: .97;
}

.cb-11__btn:has(input:focus-visible) {
  outline: 2px solid var(--like);
  outline-offset: 3px;
}

.cb-11__btn:has(input:checked) {
  color: var(--like);
  border-color: color-mix(in oklab,var(--like) 55%,var(--line));
  background: color-mix(in oklab,var(--like) 7%,var(--surface));
}

.cb-11__btn:has(input:checked) .cb-11__ico {
  color: var(--like);
}

.cb-11__btn:has(input:checked) .cb-11__ico svg {
  fill: var(--like);
  animation: cb-11-pop .6s var(--spring);
}

@keyframes cb-11-pop {
  0% {
    scale: 1;
  }

  22% {
    scale: .75;
  }

  55% {
    scale: 1.28;
  }

  100% {
    scale: 1;
  }
}

.cb-11__sparks {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.cb-11__spark {
  position: absolute;
  top: 50%;
  left: 50%;
  width: .28rem;
  height: .28rem;
  margin: -.14rem 0 0 -.14rem;
  border-radius: 999px;
  background: var(--like);
  opacity: 0;
}

.cb-11__spark:nth-child(1) {
  rotate: 0deg;
}

.cb-11__spark:nth-child(2) {
  rotate: 45deg;
  background: color-mix(in oklab,var(--like) 60%,#f59e0b);
}

.cb-11__spark:nth-child(3) {
  rotate: 90deg;
}

.cb-11__spark:nth-child(4) {
  rotate: 135deg;
  background: color-mix(in oklab,var(--like) 60%,#f59e0b);
}

.cb-11__spark:nth-child(5) {
  rotate: 180deg;
}

.cb-11__spark:nth-child(6) {
  rotate: 225deg;
  background: color-mix(in oklab,var(--like) 55%,#a855f7);
}

.cb-11__spark:nth-child(7) {
  rotate: 270deg;
}

.cb-11__spark:nth-child(8) {
  rotate: 315deg;
  background: color-mix(in oklab,var(--like) 55%,#a855f7);
}

.cb-11__btn:has(input:checked) .cb-11__spark {
  animation: cb-11-spark .62s cubic-bezier(.16,1,.3,1) forwards;
}

@keyframes cb-11-spark {
  0% {
    opacity: 0;
    scale: .3;
    translate: 0 0;
  }

  25% {
    opacity: 1;
    scale: 1.1;
  }

  100% {
    opacity: 0;
    scale: .5;
    translate: 0 -1.55rem;
  }
}

.cb-11__count {
  display: block;
  height: 1.25rem;
  overflow: hidden;
}

.cb-11__roll {
  display: grid;
  transition: translate .45s cubic-bezier(.16,1,.3,1);
}

.cb-11__roll span {
  display: block;
  height: 1.25rem;
  line-height: 1.25rem;
}

.cb-11__btn:has(input:checked) .cb-11__roll {
  translate: 0 -1.25rem;
}

@supports (transition-timing-function: linear(0,1)) {
  .cb-11__roll {
    transition: translate .55s var(--spring);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-11__btn,
    .cb-11__ico svg,
    .cb-11__roll {
    transition: none;
  }

  .cb-11__btn:has(input:checked) .cb-11__ico svg {
    animation: none;
  }

  .cb-11__spark {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-11__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }

  .cb-11__btn:has(input:checked) {
    background: Highlight;
    color: HighlightText;
  }

  .cb-11__spark {
    display: none;
  }
}
```
