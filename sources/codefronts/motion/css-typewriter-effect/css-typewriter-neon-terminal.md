---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-neon-terminal/"
title: "CSS Typewriter Neon Terminal"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "A glowing neon CRT-style terminal with scanlines, phosphor bloom, and a stepped-width typewriter revealing a command prompt sequence — all in pure CSS."
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Neon Terminal
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-neon-terminal/

A glowing neon CRT-style terminal with scanlines, phosphor bloom, and a stepped-width typewriter revealing a command prompt sequence — all in pure CSS.
## HTML
```html
<div class="tw-04">
  <div class="tw-04__crt">
    <div class="tw-04__scanlines"></div>
    <div class="tw-04__content">
      <div class="tw-04__header">AXIOM-OS v2.4 // SECURE SHELL</div>
      <div class="tw-04__divider">════════════════════════════════</div>
      <p class="tw-04__line tw-04__line--dim">Last login: Mon Jun  9 04:12:33 UTC 2025</p>
      <p class="tw-04__line tw-04__line--cmd" style="--len:24;--d:0.5s">root@axiom:~$ ls -la /vault</p>
      <p class="tw-04__line tw-04__line--out" style="--d:2.2s">drwxr-x--- 8 root root  4096 vault/</p>
      <p class="tw-04__line tw-04__line--cmd" style="--len:28;--d:3.6s">root@axiom:~$ cat manifest.enc</p>
      <p class="tw-04__line tw-04__line--active" style="--len:18;--d:5.8s">DECRYPTING... ██░░░░</p>
    </div>
  </div>
</div>
```
## CSS
```css
.tw-04,
.tw-04 *,
.tw-04 *::before,
.tw-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-04 ::selection {
  background: #00ff41;
  color: #000;
}

.tw-04 {
  --phosphor: #00ff41;
  --dim: #00882a;
  --bg: #030a03;
  font-family: 'Courier New', monospace;
  background: #000;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.tw-04__crt {
  position: relative;
  width: 100%;
  max-width: 540px;
  border: 2px solid #00441a;
  border-radius: 8px;
  padding: 28px 24px;
  box-shadow: 0 0 40px rgba(0,255,65,0.12), 0 0 80px rgba(0,255,65,0.06), inset 0 0 60px rgba(0,0,0,0.5);
  overflow: hidden;
}

.tw-04__scanlines {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      to bottom,
      transparent 0px,
      transparent 2px,
      rgba(0,0,0,0.25) 2px,
      rgba(0,0,0,0.25) 4px
    );
  pointer-events: none;
  z-index: 2;
  border-radius: 8px;
}

.tw-04__content {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.tw-04__header {
  font-size: 0.72rem;
  color: var(--dim);
  letter-spacing: 0.12em;
  margin-bottom: 4px;
  text-shadow: 0 0 6px var(--dim);
}

.tw-04__divider {
  color: #00441a;
  font-size: 0.75rem;
  letter-spacing: 0;
  margin-bottom: 8px;
}

.tw-04__line {
  font-size: 0.88rem;
  color: var(--phosphor);
  text-shadow: 0 0 8px rgba(0,255,65,0.8), 0 0 20px rgba(0,255,65,0.3);
  white-space: nowrap;
  overflow: hidden;
}

.tw-04__line--dim {
  color: var(--dim);
  text-shadow: 0 0 4px rgba(0,136,42,0.5);
}

.tw-04__line--cmd {
  width: 0;
  animation: tw-04-type steps(var(--len)) var(--d, 0s) forwards;
  animation-duration: calc(var(--len, 24) * 0.06s);
}

.tw-04__line--out {
  opacity: 0;
  animation: tw-04-appear 0.1s var(--d, 0s) forwards;
}

.tw-04__line--active {
  color: #7fff7f;
  width: 0;
  animation: tw-04-type steps(var(--len)) var(--d, 0s) forwards;
  animation-duration: calc(var(--len, 18) * 0.08s);
}

@keyframes tw-04-type {
  from {
    width: 0;
  }

  to {
    width: calc(var(--len) * 1ch);
  }
}

@keyframes tw-04-appear {
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-04__line--cmd,
    .tw-04__line--active {
    width: calc(var(--len, 24) * 1ch);
    animation: none;
  }

  .tw-04__line--out {
    opacity: 1;
    animation: none;
  }
}
```
