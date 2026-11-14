---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/hacker-terminal-glitch/"
title: "Hacker Terminal Glitch"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Realistic macOS terminal window with authentic dot buttons and multiple output lines, where one critical error line fires a three-frame RGB-split…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hacker Terminal Glitch
Source: https://codefronts.com/motion/css-glitch-text-effect/hacker-terminal-glitch/

Realistic macOS terminal window with authentic dot buttons and multiple output lines, where one critical error line fires a three-frame RGB-split displacement burst every 3 seconds -- clinical, developer-focused aesthetic.
## HTML
```html
<div class="gt-12">
  <div class="gt-12__window">
    <div class="gt-12__titlebar">
      <div class="gt-12__dot"></div>
      <div class="gt-12__dot"></div>
      <div class="gt-12__dot"></div>
      <span class="gt-12__title-text">zsh — 80×24</span>
    </div>
    <div class="gt-12__body">
      <div class="gt-12__line gt-12__line--prompt">▸ npm run deploy --env=production</div>
      <div class="gt-12__line gt-12__line--output">  ✓ Building optimized bundle...</div>
      <div class="gt-12__line gt-12__line--output">  ✓ Compressing assets (847 files)</div>
      <div class="gt-12__line gt-12__line--warning">  ⚠ Integrity hash mismatch on layer 3</div>
      <div class="gt-12__line gt-12__line--glitch" data-text="  ✗ KERNEL_INJECT :: 0xDEAD_BEEF">  ✗ KERNEL_INJECT :: 0xDEAD_BEEF</div>
      <div class="gt-12__line gt-12__line--error">  ✗ Deploy failed — see logs above</div>
      <div class="gt-12__line gt-12__line--prompt">▸ <span class="gt-12__cursor"></span></div>
    </div>
  </div>
</div>
```
## CSS
```css
.gt-12,
.gt-12 *,
.gt-12 *::before,
.gt-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-12 ::selection {
  background: #22d3ee;
  color: #000;
}

.gt-12 {
  --cyan: #22d3ee;
  --dim-cyan: #164e63;
  --bg: #060d10;
  --term-bg: #040b0d;
  --text: #cffafe;
  --muted: rgba(207,250,254,0.4);
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 20px;
  font-family: 'Fira Code', 'Source Code Pro', 'Courier New', monospace;
}

.gt-12__window {
  width: 100%;
  max-width: 520px;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6), 0 0 0 1px rgba(34,211,238,0.12);
}
/* macOS-style titlebar */

.gt-12__titlebar {
  background: #111c1f;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1px solid rgba(34,211,238,0.08);
}

.gt-12__dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.gt-12__dot:nth-child(1) {
  background: #ff5f57;
}

.gt-12__dot:nth-child(2) {
  background: #febc2e;
}

.gt-12__dot:nth-child(3) {
  background: #28c840;
}

.gt-12__title-text {
  flex: 1;
  text-align: center;
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 1px;
}
/* Terminal body */

.gt-12__body {
  background: var(--term-bg);
  padding: 20px 22px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.gt-12__line {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.8;
  letter-spacing: 0.5px;
}

.gt-12__line--prompt {
  color: var(--cyan);
}

.gt-12__line--output {
  color: rgba(207,250,254,0.7);
}

.gt-12__line--warning {
  color: #fbbf24;
}

.gt-12__line--error {
  color: #f87171;
}
/* The glitchy highlight line */

.gt-12__line--glitch {
  position: relative;
  color: var(--text);
  text-shadow: 0 0 6px rgba(34,211,238,0.5);
  animation: gt-12-line-shift 3s steps(1) infinite;
}

.gt-12__line--glitch::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: #f0f;
  animation: gt-12-ghost-before 3s steps(1) infinite;
}

.gt-12__line--glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: #0ff;
  animation: gt-12-ghost-after 3s steps(1) infinite;
}

@keyframes gt-12-line-shift {
  0%,
    85%,
    100% {
    transform: translateX(0);
  }

  87% {
    transform: translateX(-4px);
  }

  89% {
    transform: translateX(3px);
  }

  91% {
    transform: translateX(-1px);
  }

  93% {
    transform: translateX(0);
  }
}

@keyframes gt-12-ghost-before {
  0%,
    85%,
    93%,
    100% {
    opacity: 0;
    transform: translateX(0);
  }

  87% {
    opacity: 0.8;
    transform: translateX(-5px);
  }

  89% {
    opacity: 0.5;
    transform: translateX(3px);
  }

  91% {
    opacity: 0.3;
  }
}

@keyframes gt-12-ghost-after {
  0%,
    85%,
    93%,
    100% {
    opacity: 0;
    transform: translateX(0);
  }

  87% {
    opacity: 0.6;
    transform: translateX(5px);
  }

  89% {
    opacity: 0.4;
    transform: translateX(-3px);
  }

  91% {
    opacity: 0.2;
  }
}
/* blinking cursor */

.gt-12__cursor {
  display: inline-block;
  width: 8px;
  height: 13px;
  background: var(--cyan);
  margin-left: 2px;
  vertical-align: middle;
  animation: gt-12-cur 1s steps(1) infinite;
}

@keyframes gt-12-cur {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-12__line--glitch,
    .gt-12__cursor {
    animation: none;
  }

  .gt-12__line--glitch::before,
    .gt-12__line--glitch::after {
    display: none;
  }
}
```
