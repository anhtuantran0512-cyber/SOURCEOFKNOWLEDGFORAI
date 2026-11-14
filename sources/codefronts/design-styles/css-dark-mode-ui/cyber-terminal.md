---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/cyber-terminal/"
title: "Cyber Terminal Dark UI Panel"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A terminal panel with prompt history, streamed output and a live input line — phosphor green on black, a 2&percnt; scanline overlay and a blinking block caret."
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyber Terminal Dark UI Panel
Source: https://codefronts.com/design-styles/css-dark-mode-ui/cyber-terminal/

A terminal panel with prompt history, streamed output and a live input line — phosphor green on black, a 2&percnt; scanline overlay and a blinking block caret. The retro reference is deliberate, the contrast is not: the green is tuned to 11:1 against the substrate, dim output still clears 4.5:1, and the whole CRT layer disappears under prefers-reduced-motion.
## HTML
```html
<div class="dmu-14">
  <div class="dmu-14__stage">
    <section class="dmu-14__panel" aria-label="Terminal">
      <span class="dmu-14__crt" aria-hidden="true"></span>
      <header class="dmu-14__bar">
        <span class="dmu-14__dots" aria-hidden="true"><i></i><i></i><i></i></span>
        <p class="dmu-14__path">alex@meridian &mdash; ~/apps/web</p>
        <span class="dmu-14__status">
          <span class="dmu-14__led" aria-hidden="true"></span>
          connected
        </span>
      </header>

      <div class="dmu-14__scroll">
        <p class="dmu-14__line dmu-14__line--cmd">pnpm build --filter web</p>
        <p class="dmu-14__line dmu-14__line--out">Resolving 412 packages &hellip; done in 1.8s</p>
        <p class="dmu-14__line dmu-14__line--out">Compiled 96 routes with the edge runtime</p>
        <p class="dmu-14__line dmu-14__line--warn">theme.css: 3 selectors exceed specificity budget</p>
        <p class="dmu-14__line dmu-14__line--out">Bundle 184 kB gzip (&minus;12 kB from main)</p>
        <p class="dmu-14__line dmu-14__line--ok">Build succeeded in 14.2s</p>
        <p class="dmu-14__line dmu-14__line--cmd">node scripts/audit-contrast.mjs</p>
        <p class="dmu-14__line dmu-14__line--out">Checked 148 token pairs against WCAG AA</p>
        <p class="dmu-14__line dmu-14__line--ok">All pairs pass &mdash; lowest ratio 4.71:1</p>
      </div>

      <form class="dmu-14__prompt" onsubmit="return false">
        <label class="dmu-14__sr" for="dmu-14-input">Terminal command</label>
        <span class="dmu-14__sigil" aria-hidden="true">&#36;</span>
        <input class="dmu-14__input" id="dmu-14-input" type="text" autocomplete="off" spellcheck="false" placeholder="git switch -c theme/tokens">
        <span class="dmu-14__caret" aria-hidden="true"></span>
      </form>
    </section>
  </div>
</div>
```
## CSS
```css
.dmu-14 {
  --void: #04060a;
  --panel: #080c10;
  --bar: #0b1116;
  --hair: rgba(126,255,168,.16);
  --phosphor: #7effa8;
  --dim: #8fb7a0;
  --amber: #ffc866;
  --ok: #7effa8;
  --ink: #d8ffe6;
  --glow: rgba(126,255,168,.10);
  --rows: min(24rem,52vh);
  --mono: "JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(100% 70% at 50% 0%,#071016,var(--void) 70%),var(--void);
  color: var(--ink);
  font-family: var(--mono);
  -webkit-font-smoothing: antialiased;
}

.dmu-14,
.dmu-14 *,
.dmu-14 *::before,
.dmu-14 *::after {
  box-sizing: border-box;
}

.dmu-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-14__panel {
  position: relative;
  width: min(60rem,100%);
  overflow: hidden;
  border-radius: .9rem;
  background: var(--panel);
  border: 1px solid var(--hair);
  box-shadow: inset 0 0 60px var(--glow), 0 40px 80px -50px #000;
}

.dmu-14__crt {
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
  background: repeating-linear-gradient(180deg,rgba(255,255,255,.022) 0 1px,transparent 1px 3px), radial-gradient(120% 90% at 50% 50%,transparent 55%,rgba(0,0,0,.5));
}

.dmu-14__bar {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .6rem .85rem;
  background: var(--bar);
  border-bottom: 1px solid var(--hair);
}

.dmu-14__dots {
  display: flex;
  gap: .35rem;
}

.dmu-14__dots i {
  width: .6rem;
  height: .6rem;
  border-radius: 50%;
  background: rgba(126,255,168,.25);
}

.dmu-14__dots i:first-child {
  background: var(--phosphor);
}

.dmu-14__path {
  margin: 0;
  font-size: .74rem;
  color: var(--dim);
  letter-spacing: .02em;
}

.dmu-14__status {
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  font-size: .7rem;
  color: var(--dim);
}

.dmu-14__led {
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--ok);
  box-shadow: 0 0 8px var(--ok);
  animation: dmu-14-pulse 2.6s ease-in-out infinite;
}

@keyframes dmu-14-pulse {
  0%,
    100% {
    opacity: .55;
  }

  50% {
    opacity: 1;
  }
}

.dmu-14__scroll {
  display: grid;
  gap: .28rem;
  padding: 1rem 1.1rem;
  height: var(--rows);
  overflow: auto;
  align-content: start;
}

.dmu-14__line {
  margin: 0;
  display: grid;
  grid-template-columns: 1.1rem 1fr;
  gap: .5rem;
  font-size: .8rem;
  line-height: 1.55;
}

.dmu-14__line::before {
  color: var(--dim);
}

.dmu-14__line--cmd {
  color: var(--ink);
}

.dmu-14__line--cmd::before {
  content: '$';
  color: var(--phosphor);
}

.dmu-14__line--out {
  color: var(--dim);
}

.dmu-14__line--out::before {
  content: '\2192';
}

.dmu-14__line--warn {
  color: var(--amber);
}

.dmu-14__line--warn::before {
  content: '!';
  color: var(--amber);
}

.dmu-14__line--ok {
  color: var(--ok);
}

.dmu-14__line--ok::before {
  content: '\2713';
  color: var(--ok);
}

.dmu-14__prompt {
  position: relative;
  display: grid;
  grid-template-columns: 1.1rem 1fr;
  gap: .5rem;
  align-items: center;
  padding: .75rem 1.1rem;
  border-top: 1px solid var(--hair);
  background: var(--bar);
}

.dmu-14__sigil {
  color: var(--phosphor);
  font-size: .85rem;
}

.dmu-14__input {
  min-height: 2.1rem;
  border: 0;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: .82rem;
  letter-spacing: .01em;
  caret-color: var(--phosphor);
}

.dmu-14__input::placeholder {
  color: color-mix(in oklab,var(--dim) 75%,transparent);
}

.dmu-14__input:focus {
  outline: none;
}

.dmu-14__prompt:focus-within {
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--phosphor) 55%,transparent);
}

.dmu-14__caret {
  position: absolute;
  right: 1.1rem;
  width: .55rem;
  height: 1.05rem;
  background: var(--phosphor);
  animation: dmu-14-blink 1.05s steps(1,end) infinite;
}

.dmu-14__prompt:focus-within .dmu-14__caret {
  opacity: 0;
}

@keyframes dmu-14-blink {
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
  .dmu-14__caret,
    .dmu-14__led {
    animation: none;
  }

  .dmu-14__crt {
    background: radial-gradient(120% 90% at 50% 50%,transparent 60%,rgba(0,0,0,.4));
  }
}

@media (forced-colors: active) {
  .dmu-14__panel {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-14__crt {
    display: none;
  }

  .dmu-14__line,
    .dmu-14__line::before {
    color: CanvasText;
  }

  .dmu-14__caret {
    background: CanvasText;
  }
}
```
