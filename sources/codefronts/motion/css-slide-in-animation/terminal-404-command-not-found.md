---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/terminal-404-command-not-found/"
title: "Terminal 404 Command Not Found"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A macOS/Linux terminal window as a 404 error page where the failed URL is rendered as a bash command that returned 'command not found', followed by three…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal 404 Command Not Found
Source: https://codefronts.com/motion/css-slide-in-animation/terminal-404-command-not-found/

A macOS/Linux terminal window as a 404 error page where the failed URL is rendered as a bash command that returned 'command not found', followed by three fuzzy-match suggestions the user might have meant — the dev-culture 404 pattern used by GitHub, Vercel, Cloudflare, and every terminal-lover product page. Zero decorative fluff, zero apology.
## HTML
```html
<div class="sl-18">
  <div class="sl-18__window">
    <div class="sl-18__bar">
      <span class="sl-18__dot sl-18__dot--r"></span>
      <span class="sl-18__dot sl-18__dot--y"></span>
      <span class="sl-18__dot sl-18__dot--g"></span>
      <span class="sl-18__title">~/codefronts.com — bash — 80×24</span>
    </div>
    <div class="sl-18__screen">
      <div class="sl-18__scanline" aria-hidden="true"></div>
      <div class="sl-18__lines">
        <div class="sl-18__line">
          <span class="sl-18__prompt">visitor@codefronts</span><span class="sl-18__colon">:</span><span class="sl-18__path">~/</span><span class="sl-18__dollar">$</span>
          <span class="sl-18__cmd">cat /components/mystery-widget</span>
        </div>
        <div class="sl-18__error">
          <span class="sl-18__errcode">bash: /components/mystery-widget:</span>
          <span class="sl-18__errmsg">No such file or directory</span>
        </div>
        <div class="sl-18__hint">Did you mean one of these?</div>
        <a href="#" class="sl-18__sug">
          <span class="sl-18__arrow">›</span>
          <span class="sl-18__sugpath">/components/<mark>my</mark>-<mark>widget</mark>s/</span>
          <span class="sl-18__sugmeta">92% match · 43 demos</span>
        </a>
        <a href="#" class="sl-18__sug">
          <span class="sl-18__arrow">›</span>
          <span class="sl-18__sugpath">/motion/<mark>mystery</mark>-animations/</span>
          <span class="sl-18__sugmeta">78% match · 22 demos</span>
        </a>
        <a href="#" class="sl-18__sug">
          <span class="sl-18__arrow">›</span>
          <span class="sl-18__sugpath">/generators/<mark>widget</mark>-generator/</span>
          <span class="sl-18__sugmeta">64% match · CSS gen tool</span>
        </a>
        <div class="sl-18__foot">
          <span class="sl-18__prompt">visitor@codefronts</span><span class="sl-18__colon">:</span><span class="sl-18__path">~/</span><span class="sl-18__dollar">$</span>
          <span class="sl-18__cursor" aria-hidden="true"></span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-18 {
  --bg: #0f0f13;
  --window: #1a1a1e;
  --screen: #0a0a0a;
  --phosphor: #3eff7f;
  --phosphor-dim: #1f7f3f;
  --muted: #5a7a5a;
  --red: #ff5f57;
  --yellow: #febc2e;
  --green: #28c840;
  --gray: #8a8a94;
  --match: #00d4ff;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(80% 100% at 50% 0%, rgba(62,255,127,.06) 0%, transparent 60%), var(--bg);
  color: var(--phosphor);
}

.sl-18 *,
.sl-18 *::before,
.sl-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-18 ::selection {
  background: var(--phosphor);
  color: #0a0a0a;
}

.sl-18__window {
  width: min(680px,100%);
  border-radius: 10px;
  overflow: hidden;
  background: var(--window);
  box-shadow: 0 40px 80px -20px rgba(0,0,0,.7),0 0 0 1px rgba(255,255,255,.05),0 0 60px -20px rgba(62,255,127,.15);
  opacity: 0;
  transform: translateY(30px);
  animation: sl-18-window .6s cubic-bezier(.22,1,.36,1) .1s forwards;
}

.sl-18__bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 11px 14px;
  background: linear-gradient(180deg,#2a2a30,#1e1e24);
  border-bottom: 1px solid rgba(0,0,0,.4);
  position: relative;
}

.sl-18__dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
  flex-shrink: 0;
}

.sl-18__dot--r {
  background: var(--red);
}

.sl-18__dot--y {
  background: var(--yellow);
}

.sl-18__dot--g {
  background: var(--green);
}

.sl-18__title {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  font-family: 'SF Mono','JetBrains Mono',ui-monospace,monospace;
  font-size: .72rem;
  color: var(--gray);
  font-weight: 500;
  letter-spacing: .02em;
}

.sl-18__screen {
  position: relative;
  padding: 22px 24px 20px;
  background: var(--screen);
  min-height: 360px;
  font-family: 'SF Mono','JetBrains Mono',ui-monospace,'Courier New',monospace;
  font-size: .88rem;
  line-height: 1.65;
  overflow: hidden;
}

.sl-18__scanline {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg,rgba(62,255,127,.04) 0 2px,transparent 2px 4px);
  pointer-events: none;
  mix-blend-mode: screen;
}

.sl-18__lines {
  position: relative;
  z-index: 1;
}

.sl-18__line {
  color: var(--phosphor);
  margin-bottom: 6px;
}

.sl-18__prompt {
  color: var(--phosphor);
  font-weight: 500;
}

.sl-18__colon {
  color: var(--gray);
}

.sl-18__path {
  color: var(--match);
  font-weight: 500;
}

.sl-18__dollar {
  color: var(--gray);
  margin: 0 8px 0 2px;
}

.sl-18__cmd {
  color: #fff;
  font-weight: 400;
}

.sl-18__error {
  color: #ff5f57;
  font-weight: 400;
  margin-bottom: 16px;
  opacity: 0;
  transform: translateY(20px);
  animation: sl-18-slide .5s cubic-bezier(.22,1,.36,1) .4s forwards;
}

.sl-18__errcode {
  color: #ff5f57;
  font-weight: 500;
}

.sl-18__errmsg {
  color: #ff9099;
  margin-left: 6px;
}

.sl-18__hint {
  color: var(--gray);
  font-size: .82rem;
  margin-bottom: 10px;
  opacity: 0;
  animation: sl-18-fade .3s ease-out .55s forwards;
}

.sl-18__sug {
  display: flex;
  align-items: baseline;
  gap: 12px;
  padding: 6px 8px;
  border-radius: 5px;
  margin-bottom: 4px;
  color: var(--phosphor);
  text-decoration: none;
  cursor: pointer;
  opacity: 0;
  transform: translateY(15px);
  animation: sl-18-sug .45s cubic-bezier(.22,1,.36,1) forwards;
  transition: background .15s ease;
}

.sl-18__sug:hover,
.sl-18__sug:focus-visible {
  background: rgba(62,255,127,.08);
  outline: none;
}

.sl-18__sug:nth-of-type(1) {
  animation-delay: .7s;
}

.sl-18__sug:nth-of-type(2) {
  animation-delay: .9s;
}

.sl-18__sug:nth-of-type(3) {
  animation-delay: 1.1s;
}

.sl-18__arrow {
  color: var(--phosphor-dim);
  font-weight: 700;
  font-size: .95rem;
  flex-shrink: 0;
}

.sl-18__sugpath {
  color: var(--phosphor);
  flex: 1;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.sl-18__sugpath mark {
  background: transparent;
  color: var(--match);
  font-weight: 700;
  text-shadow: 0 0 8px rgba(0,212,255,.4);
}

.sl-18__sugmeta {
  color: var(--muted);
  font-size: .72rem;
  flex-shrink: 0;
}

.sl-18__foot {
  margin-top: 20px;
  color: var(--phosphor);
  opacity: 0;
  animation: sl-18-fade .3s ease-out 1.35s forwards;
}

.sl-18__cursor {
  display: inline-block;
  width: 8px;
  height: 16px;
  background: var(--phosphor);
  vertical-align: text-bottom;
  margin-left: 3px;
  animation: sl-18-blink 1s steps(1) infinite;
  box-shadow: 0 0 6px rgba(62,255,127,.7);
}

@keyframes sl-18-window {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes sl-18-slide {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes sl-18-sug {
  from {
    opacity: 0;
    transform: translateY(15px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes sl-18-fade {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes sl-18-blink {
  0%,
    50% {
    opacity: 1;
  }

  50.01%,
    100% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-18 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }

  .sl-18__cursor {
    animation: none!important;
    opacity: 1!important;
  }
}

@media (max-width: 600px) {
  .sl-18__screen {
    padding: 18px 16px;
    font-size: .78rem;
  }

  .sl-18__title {
    display: none;
  }

  .sl-18__sugmeta {
    display: none;
  }
}
```
