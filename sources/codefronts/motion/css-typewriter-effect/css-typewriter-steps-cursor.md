---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-steps-cursor/"
title: "CSS Typewriter steps() Cursor"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "The canonical CSS-only typewriter: width animates from 0 to a fixed ch value using steps() timing, paired with a blinking border-right cursor — no JS at all."
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter steps() Cursor
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-steps-cursor/

The canonical CSS-only typewriter: width animates from 0 to a fixed ch value using steps() timing, paired with a blinking border-right cursor — no JS at all.
## HTML
```html
<div class="tw-01">
  <div class="tw-01__stage">
    <p class="tw-01__label">Frontend Developer</p>
    <h1 class="tw-01__text">Hello, World.</h1>
    <p class="tw-01__sub">Building beautiful interfaces with code.</p>
  </div>
</div>
```
## CSS
```css
.tw-01,
.tw-01 *,
.tw-01 *::before,
.tw-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-01 ::selection {
  background: #a78bfa;
  color: #0f0a1e;
}

.tw-01 {
  --bg: #0f0a1e;
  --surface: #1a1033;
  --accent: #a78bfa;
  --text: #e2d9f3;
  --muted: #6b5fa0;
  font-family: 'Courier New', Courier, monospace;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tw-01__stage {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.tw-01__label {
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
  opacity: 0;
  animation: tw-01-fadein 0.4s 0.2s forwards;
}

.tw-01__text {
  font-size: clamp(1.8rem, 5vw, 3rem);
  font-weight: 700;
  color: var(--text);
  overflow: hidden;
  white-space: nowrap;
  width: 0;
  border-right: 3px solid var(--accent);
  animation: tw-01-type 1.1s steps(13) 0.8s forwards, tw-01-blink 0.75s steps(2) 0.8s infinite;
}

.tw-01__sub {
  font-size: 0.95rem;
  color: var(--muted);
  overflow: hidden;
  white-space: nowrap;
  width: 0;
  animation: tw-01-sub 1.5s steps(38) 2.2s forwards;
}

@keyframes tw-01-type {
  from {
    width: 0;
  }

  to {
    width: 13ch;
  }
}

@keyframes tw-01-sub {
  from {
    width: 0;
  }

  to {
    width: 38ch;
  }
}

@keyframes tw-01-blink {
  0%,
    100% {
    border-color: var(--accent);
  }

  50% {
    border-color: transparent;
  }
}

@keyframes tw-01-fadein {
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-01__text {
    width: 13ch;
    animation: none;
    border-right-color: var(--accent);
  }

  .tw-01__sub {
    width: 38ch;
    animation: none;
  }

  .tw-01__label {
    opacity: 1;
    animation: none;
  }
}
```
