---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/neon-typing-loading-terminal/"
title: "Neon Typing / Loading Terminal"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A glowing monospace terminal that types a line out character-by-character behind a blinking neon caret — the boot-screen / loading-state look for dashboards…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Typing / Loading Terminal
Source: https://codefronts.com/motion/css-neon-text-effect/neon-typing-loading-terminal/

A glowing monospace terminal that types a line out character-by-character behind a blinking neon caret — the boot-screen / loading-state look for dashboards and dev tools, done with a steps() type-on and a caret border, no JS.
## HTML
```html
<div class="cnt-20">
  <div class="cnt-20__term">
    <div class="cnt-20__bar" aria-hidden="true"><i></i><i></i><i></i><span>boot.sh</span></div>
    <div class="cnt-20__body">
      <p class="cnt-20__ln"><span class="cnt-20__prompt">&gt;</span> <span class="cnt-20__type">initializing neon subsystem</span></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cnt-20,
.cnt-20 *,
.cnt-20 *::before,
.cnt-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-20 ::selection {
  background: oklch(0.86 0.2 150);
  color: #03140b;
}

.cnt-20 {
  --accent: oklch(0.86 0.2 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(120% 120% at 50% 30%,#07100c,#040706);
}

.cnt-20__term {
  width: min(620px,94vw);
  border-radius: 12px;
  overflow: hidden;
  background: #050807;
  border: 1px solid #14201a;
  box-shadow: 0 40px 80px -44px #000,0 0 60px -20px color-mix(in oklch,var(--accent) 30%,transparent);
}

.cnt-20__bar {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 12px 16px;
  background: #0a0f0c;
  border-bottom: 1px solid #14201a;
}

.cnt-20__bar i {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #233029;
}

.cnt-20__bar i:first-child {
  background: oklch(0.7 0.2 25);
}

.cnt-20__bar i:nth-child(2) {
  background: oklch(0.82 0.16 90);
}

.cnt-20__bar i:nth-child(3) {
  background: var(--accent);
}

.cnt-20__bar span {
  margin-left: 8px;
  font: 11px ui-monospace,Menlo,monospace;
  color: #4d635a;
  letter-spacing: .1em;
}

.cnt-20__body {
  padding: 26px 22px;
  min-height: 96px;
  background: repeating-linear-gradient(0deg,transparent 0 3px,rgba(0,0,0,.25) 3px 4px);
}

.cnt-20__ln {
  display: flex;
  align-items: center;
  gap: 10px;
  font: clamp(15px,3.4vw,22px)/1.4 ui-monospace,Menlo,monospace;
}

.cnt-20__prompt {
  color: color-mix(in oklch,var(--accent) 55%,#3a5245);
}

.cnt-20__type {
  color: var(--accent);
  white-space: nowrap;
  overflow: hidden;
  border-right: .6em solid var(--accent);
  width: 26ch;
  max-width: 100%;
  text-shadow: 0 0 5px #fff,0 0 12px var(--accent),0 0 30px var(--accent);
  animation: cnt-20-type 3.4s steps(26,end) infinite,cnt-20-caret .8s steps(1,end) infinite;
}

@keyframes cnt-20-type {
  0% {
    width: 0;
  }

  55%,
    100% {
    width: 26ch;
  }
}

@keyframes cnt-20-caret {
  0%,
    100% {
    border-color: var(--accent);
  }

  50% {
    border-color: transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-20__type {
    animation: none;
    width: 26ch;
    border-right-color: transparent;
  }
}
```

## JavaScript
```js
/* No JavaScript — steps() width reveal types the line; a border-right caret blinks. */
```
