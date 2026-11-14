---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-typing-dots-loader/"
title: "CSS Typing Dots Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Four conversational CSS loaders — a chat-bubble typing indicator, an inline AI-thinking status, a cursor blink, and a bouncing dot trio — matching the…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typing Dots Loader
Source: https://codefronts.com/motion/css-loader-designs/css-typing-dots-loader/

Four conversational CSS loaders — a chat-bubble typing indicator, an inline AI-thinking status, a cursor blink, and a bouncing dot trio — matching the patterns used in messaging and AI product UIs.
## HTML
```html
<div class="ld-16">
  <div class="ld-16__stage">
    <div>
      <div class="ld-16__label-row">Chat bubble</div>
      <div class="ld-16__bubble"><span></span><span></span><span></span></div>
    </div>
```
## CSS
```css
.ld-16,
.ld-16 *,
.ld-16 *::before,
.ld-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-16 {
  --bg: #1c1c2e;
  --c1: #e2e8f0;
  --c2: #94a3b8;
  --c3: #38bdf8;
  --c4: #a78bfa;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-16__stage {
  display: flex;
  gap: 28px;
  flex-direction: column;
  align-items: flex-start;
  padding: 40px;
  max-width: 400px;
  width: 100%;
}

.ld-16__label-row {
  color: rgba(255,255,255,.3);
  font-size: 10px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-bottom: 4px;
}
/* Chat bubble with typing dots */

.ld-16__bubble {
  background: #2d2d44;
  border-radius: 18px 18px 18px 4px;
  padding: 14px 18px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  max-width: 180px;
}

.ld-16__bubble span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--c2);
  animation: ld-16-typing 1.2s ease-in-out infinite;
}

.ld-16__bubble span:nth-child(1) {
  animation-delay: 0s;
}

.ld-16__bubble span:nth-child(2) {
  animation-delay: .2s;
}

.ld-16__bubble span:nth-child(3) {
  animation-delay: .4s;
}

@keyframes ld-16-typing {
  0%,
    60%,
    100% {
    transform: translateY(0);
    opacity: .4;
  }

  30% {
    transform: translateY(-6px);
    opacity: 1;
  }
}
/* Inline text dots */

.ld-16__inline {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--c2);
  font-size: 14px;
}

.ld-16__inline-dots {
  display: flex;
  gap: 3px;
}

.ld-16__inline-dots span {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--c3);
  animation: ld-16-typing 1s ease-in-out infinite;
}

.ld-16__inline-dots span:nth-child(1) {
  animation-delay: 0s;
}

.ld-16__inline-dots span:nth-child(2) {
  animation-delay: .15s;
}

.ld-16__inline-dots span:nth-child(3) {
  animation-delay: .3s;
}
/* Cursor blink */

.ld-16__cursor-wrap {
  color: var(--c1);
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 2px;
}

.ld-16__cursor {
  width: 2px;
  height: 20px;
  background: var(--c4);
  animation: ld-16-blink 1s step-end infinite;
}

@keyframes ld-16-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}
/* Processing dots large */

.ld-16__processing {
  display: flex;
  gap: 10px;
  align-items: center;
}

.ld-16__processing span {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--c4);
  animation: ld-16-proc 1.4s ease-in-out infinite;
}

.ld-16__processing span:nth-child(1) {
  animation-delay: 0s;
}

.ld-16__processing span:nth-child(2) {
  animation-delay: .2s;
  background: var(--c3);
}

.ld-16__processing span:nth-child(3) {
  animation-delay: .4s;
  background: var(--c4);
}

@keyframes ld-16-proc {
  0%,
    80%,
    100% {
    transform: scale(.6) translateY(0);
    opacity: .4;
  }

  40% {
    transform: scale(1) translateY(-10px);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-16__bubble span,
    .ld-16__inline-dots span,
    .ld-16__cursor,
    .ld-16__processing span {
    animation: none;
  }
}
```
