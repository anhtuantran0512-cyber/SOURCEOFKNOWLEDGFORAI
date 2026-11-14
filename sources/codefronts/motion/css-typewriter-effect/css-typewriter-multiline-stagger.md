---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-multiline-stagger/"
title: "CSS Typewriter Multiline Stagger"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "Multiple lines reveal sequentially using staggered animation-delay on each row, creating a cascading terminal-output feel entirely in CSS."
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Multiline Stagger
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-multiline-stagger/

Multiple lines reveal sequentially using staggered animation-delay on each row, creating a cascading terminal-output feel entirely in CSS.
## HTML
```html
<div class="tw-02">
  <div class="tw-02__terminal">
    <div class="tw-02__bar">
      <span class="tw-02__dot"></span><span class="tw-02__dot"></span><span class="tw-02__dot"></span>
      <span class="tw-02__title">terminal — bash</span>
    </div>
    <div class="tw-02__body">
      <p class="tw-02__line" style="--len:32;--delay:0.3s">$ initialising project scaffold...</p>
      <p class="tw-02__line" style="--len:28;--delay:2s">✓ Dependencies resolved (1.2s)</p>
      <p class="tw-02__line" style="--len:34;--delay:3.4s">✓ TypeScript config generated</p>
      <p class="tw-02__line" style="--len:30;--delay:4.8s">✓ Tailwind CSS v4 installed</p>
      <p class="tw-02__line tw-02__line--active" style="--len:26;--delay:6.2s">$ npm run dev █</p>
    </div>
  </div>
</div>
```
## CSS
```css
.tw-02,
.tw-02 *,
.tw-02 *::before,
.tw-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-02 ::selection {
  background: #22d3ee;
  color: #001a1f;
}

.tw-02 {
  --green: #4ade80;
  --cyan: #22d3ee;
  --bg: #0a0f0a;
  --surface: #111811;
  --border: #1e2d1e;
  font-family: 'Courier New', monospace;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}

.tw-02__terminal {
  width: 100%;
  max-width: 520px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 24px 60px rgba(0,0,0,0.6), 0 0 0 1px rgba(74,222,128,0.05);
  overflow: hidden;
}

.tw-02__bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background: #0d150d;
  border-bottom: 1px solid var(--border);
}

.tw-02__dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #3a3a3a;
}

.tw-02__dot:nth-child(1) {
  background: #ff5f57;
}

.tw-02__dot:nth-child(2) {
  background: #febc2e;
}

.tw-02__dot:nth-child(3) {
  background: #28c840;
}

.tw-02__title {
  margin-left: auto;
  font-size: 0.72rem;
  color: #3a5a3a;
  letter-spacing: 0.05em;
}

.tw-02__body {
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.tw-02__line {
  font-size: 0.9rem;
  color: var(--green);
  overflow: hidden;
  white-space: nowrap;
  width: 0;
  animation: tw-02-type steps(var(--len)) var(--delay) forwards;
  animation-duration: calc(var(--len) * 0.055s);
}

.tw-02__line:nth-child(2) {
  color: #86efac;
}

.tw-02__line:nth-child(3) {
  color: #86efac;
}

.tw-02__line:nth-child(4) {
  color: #86efac;
}

.tw-02__line--active {
  color: var(--cyan);
}

@keyframes tw-02-type {
  from {
    width: 0;
  }

  to {
    width: calc(var(--len) * 1ch);
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-02__line {
    width: calc(var(--len) * 1ch);
    animation: none;
  }
}
```
