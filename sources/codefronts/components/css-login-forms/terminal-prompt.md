---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/terminal-prompt/"
title: "Terminal Prompt"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "An authentic CLI login for dev-tools, dev-ops panels and security apps: monospaced type, a traffic-light window bar, a blinking block cursor, and raw…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal Prompt
Source: https://codefronts.com/components/css-login-forms/terminal-prompt/

An authentic CLI login for dev-tools, dev-ops panels and security apps: monospaced type, a traffic-light window bar, a blinking block cursor, and raw prompt-style inputs with no chrome.
## HTML
```html
<section class="lf-12">
  <form class="lf-12__win" novalidate>
    <div class="lf-12__bar" aria-hidden="true"><span></span><span></span><span></span><em>auth — ssh login</em></div>
    <div class="lf-12__body">
      <p class="lf-12__line">$ ./login --secure</p>
      <label class="lf-12__field"><span class="lf-12__prompt">user@host:~$</span>
        <input type="text" autocomplete="username" placeholder="username" required></label>
      <label class="lf-12__field"><span class="lf-12__prompt">password:</span>
        <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
      <button class="lf-12__run" type="submit">▸ authenticate<span class="lf-12__cursor" aria-hidden="true"></span></button>
    </div>
  </form>
</section>
```
## CSS
```css
.lf-12,
.lf-12 *,
.lf-12 *::before,
.lf-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-12 {
  --bg: #0c0f14;
  --green: oklch(0.82 0.16 150);
  --amber: oklch(0.82 0.15 80);
  --radius: 8px;
  font-family: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;
  width: 100%;
  min-height: 100vh;
  background: #05070a;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-12__win {
  width: min(440px,100%);
  background: var(--bg);
  border: 1px solid #1c2230;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 30px 70px -44px #000;
}

.lf-12__bar {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 11px 14px;
  background: #11151d;
  border-bottom: 1px solid #1c2230;
}

.lf-12__bar span {
  width: 11px;
  height: 11px;
  border-radius: 50%;
}

.lf-12__bar span:nth-child(1) {
  background: #ff5f56;
}

.lf-12__bar span:nth-child(2) {
  background: #ffbd2e;
}

.lf-12__bar span:nth-child(3) {
  background: #27c93f;
}

.lf-12__bar em {
  margin-left: 8px;
  font-style: normal;
  font-size: 12px;
  color: #5c6678;
}

.lf-12__body {
  padding: 22px 20px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.lf-12__line {
  font-size: 13px;
  color: #5c6678;
}

.lf-12__field {
  display: flex;
  align-items: center;
  gap: 10px;
  border-bottom: 1px solid #232b3a;
  padding-bottom: 6px;
}

.lf-12__prompt {
  font-size: 13px;
  color: var(--green);
  flex: none;
}

.lf-12__field input {
  flex: 1;
  border: 0;
  background: transparent;
  font-family: inherit;
  font-size: 14px;
  color: #e6edf3;
  padding: 4px 0;
}

.lf-12__field input::placeholder {
  color: #4a5364;
}

.lf-12__field:focus-within {
  border-bottom-color: var(--amber);
}

.lf-12__field input:focus-visible {
  outline: none;
}

.lf-12__run {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  align-self: flex-start;
  margin-top: 6px;
  padding: 9px 16px;
  border: 1px solid var(--green);
  border-radius: var(--radius);
  cursor: pointer;
  background: transparent;
  color: var(--green);
  font-family: inherit;
  font-size: 13.5px;
  font-weight: 600;
  transition: background .16s;
}

.lf-12__run:hover {
  background: oklch(0.82 0.16 150/.12);
}

.lf-12__run:focus-visible {
  outline: 3px solid oklch(0.82 0.16 150/.5);
  outline-offset: 2px;
}

.lf-12__cursor {
  display: inline-block;
  width: 8px;
  height: 15px;
  margin-left: 4px;
  background: var(--green);
  animation: lf-12-blink 1s steps(1) infinite;
}

@keyframes lf-12-blink {
  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-12__cursor {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the block cursor blinks via a CSS steps() keyframe, not a timer. */
```
