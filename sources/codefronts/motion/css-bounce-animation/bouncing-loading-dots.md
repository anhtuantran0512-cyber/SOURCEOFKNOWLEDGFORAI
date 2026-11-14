---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/bouncing-loading-dots/"
title: "Bouncing Loading Dots"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "The canonical chat-typing / loading indicator — 3 dots inside a rounded speech bubble bouncing sequentially, signaling \"loading\" or \"the other person is…"
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncing Loading Dots
Source: https://codefronts.com/motion/css-bounce-animation/bouncing-loading-dots/

The canonical chat-typing / loading indicator — 3 dots inside a rounded speech bubble bouncing sequentially, signaling "loading" or "the other person is typing." iMessage blue bubble (#007aff) on a soft-gray chat surface. The pattern users search for when building chat interfaces, AI streaming responses, or any loading state that needs to feel calm rather than urgent.
## HTML
```html
<div class="bn-05">
  <p class="bn-05__label">Alex is typing…</p>
  <div class="bn-05__bubble" aria-label="Loading indicator">
    <span class="bn-05__dot" aria-hidden="true"></span>
    <span class="bn-05__dot" aria-hidden="true"></span>
    <span class="bn-05__dot" aria-hidden="true"></span>
  </div>
</div>
```
## CSS
```css
.bn-05 {
  --page-bg: #f2f2f7;
  --bubble: #e5e5ea;
  --ink: #1c1c1e;
  --sub: #8e8e93;
  --dot: #8e8e93;
  font-family: -apple-system,BlinkMacSystemFont,'SF Pro Text','Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.bn-05 *,
.bn-05 *::before,
.bn-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-05 ::selection {
  background: #007aff;
  color: #fff;
}

.bn-05__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-05__bubble {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 22px 28px;
  border-radius: 26px;
  background: var(--bubble);
  border-bottom-left-radius: 10px;
  box-shadow: 0 4px 12px -4px rgba(28,28,30,.08);
}

.bn-05__dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--dot);
  animation: bn-05-dot 1.4s ease-in-out infinite;
}

.bn-05__dot:nth-child(2) {
  animation-delay: .16s;
}

.bn-05__dot:nth-child(3) {
  animation-delay: .32s;
}

@keyframes bn-05-dot {
  0%,
    60%,
    100% {
    transform: translateY(0);
    opacity: .4;
  }

  30% {
    transform: translateY(-8px);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bn-05__dot {
    animation: none!important;
    transform: none!important;
    opacity: .7!important;
  }
}
```
