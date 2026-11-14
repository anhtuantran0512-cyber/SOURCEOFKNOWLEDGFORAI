---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/glow-effect-neon-tech-code-block/"
title: "Neon Glow CSS Code Block (Cyberpunk Tech Aesthetic)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "Full cyberpunk: a cyan-and-magenta neon frame built from four stacked box-shadow layers, a slow breathing pulse, a scanline grid on the surface,…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow CSS Code Block (Cyberpunk Tech Aesthetic)
Source: https://codefronts.com/snippets/css-code-blocks/glow-effect-neon-tech-code-block/

Full cyberpunk: a cyan-and-magenta neon frame built from four stacked box-shadow layers, a slow breathing pulse, a scanline grid on the surface, magenta-shifted syntax tokens and a blinking block cursor. Loud on purpose — and still measured, because the glow lives in shadows rather than filter, so the code itself stays razor-sharp at 4.6:1 contrast.
## HTML
```html
<div class="cbk-14">
  <button class="cbk-14__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-14__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-14__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-14__stage">
    <input class="cbk-14__tbox" id="cbk-14-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-14__tbtn" for="cbk-14-tbox" title="Toggle light and dark theme">
      <svg class="cbk-14__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-14__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-14__block">
      <figcaption class="cbk-14__bar">
        <span class="cbk-14__dot" aria-hidden="true"></span>
        <span class="cbk-14__label">socket.ts</span>
        <span class="cbk-14__ping">live</span>
      </figcaption>

<pre class="cbk-14__pre"><code class="language-ts"><span class="tok-comment">// Realtime presence channel — reconnects with jittered backoff.</span>
<span class="tok-keyword">const</span> <span class="tok-variable">socket</span> <span class="tok-op">=</span> <span class="tok-keyword">new</span> <span class="tok-function">WebSocket</span><span class="tok-punct">(</span><span class="tok-string">'wss://rt.codefronts.com/presence'</span><span class="tok-punct">);</span>
<span class="tok-keyword">let</span> <span class="tok-variable">attempt</span> <span class="tok-op">=</span> <span class="tok-number">0</span><span class="tok-punct">;</span>

<span class="tok-variable">socket</span><span class="tok-punct">.</span><span class="tok-variable">onopen</span> <span class="tok-op">=</span> <span class="tok-punct">() =&gt; {</span>
  <span class="tok-variable">attempt</span> <span class="tok-op">=</span> <span class="tok-number">0</span><span class="tok-punct">;</span>
  <span class="tok-variable">socket</span><span class="tok-punct">.</span><span class="tok-function">send</span><span class="tok-punct">(</span><span class="tok-fn2">JSON</span><span class="tok-punct">.</span><span class="tok-function">stringify</span><span class="tok-punct">({</span> <span class="tok-variable">join</span><span class="tok-punct">:</span> <span class="tok-string">'room:studio'</span> <span class="tok-punct">}));</span>
<span class="tok-punct">};</span>

<span class="tok-variable">socket</span><span class="tok-punct">.</span><span class="tok-variable">onclose</span> <span class="tok-op">=</span> <span class="tok-punct">() =&gt; {</span>
  <span class="tok-keyword">const</span> <span class="tok-variable">wait</span> <span class="tok-op">=</span> <span class="tok-fn2">Math</span><span class="tok-punct">.</span><span class="tok-function">min</span><span class="tok-punct">(</span><span class="tok-number">30_000</span><span class="tok-punct">,</span> <span class="tok-number">500</span> <span class="tok-op">*</span> <span class="tok-number">2</span> <span class="tok-op">**</span> <span class="tok-variable">attempt</span><span class="tok-op">++</span><span class="tok-punct">);</span>
  <span class="tok-function">setTimeout</span><span class="tok-punct">(</span><span class="tok-variable">reconnect</span><span class="tok-punct">,</span> <span class="tok-variable">wait</span> <span class="tok-op">+</span> <span class="tok-fn2">Math</span><span class="tok-punct">.</span><span class="tok-function">random</span><span class="tok-punct">()</span> <span class="tok-op">*</span> <span class="tok-number">400</span><span class="tok-punct">);</span>
<span class="tok-punct">};</span><span class="cbk-14__cursor" aria-hidden="true"></span></code></pre>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-14 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #05040a;
  --surface: #08070f;
  --bar: #0c0a16;
  --ink: #e8f6ff;
  --muted: #7f8fb0;
  --neon-1: #22d3ee;
  --neon-2: #f0f;
  --neon-3: #a78bfa;
  --tok-key: #ff7ae0;
  --tok-str: #7bffd0;
  --tok-fn: #7dd3fc;
  --tok-var: #e8f6ff;
  --tok-num: #ffd166;
  --tok-punct: #8ba3c7;
  --tok-op: #ff9de2;
  --tok-com: #7f8fb0;
  --tok-fn2: #c4b5fd;
  background: radial-gradient(46rem 26rem at 18% 0%, rgba(34,211,238,.14), transparent 66%), radial-gradient(42rem 26rem at 84% 100%, rgba(255,0,255,.12), transparent 68%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-14 {
    --surface: oklch(11% .02 285);
    --bar: oklch(14% .03 290);
    --ink: oklch(95% .02 220);
    --muted: oklch(70% .04 265);
    --neon-1: oklch(84% .16 200);
    --neon-2: oklch(72% .28 330);
    --neon-3: oklch(74% .18 292);
  }
}

.cbk-14 *,
.cbk-14 *::before,
.cbk-14 *::after {
  box-sizing: border-box;
}

.cbk-14__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(2rem,6vw,5rem);
}

.cbk-14__block {
  margin: 0;
  inline-size: min(52rem,100%);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
  box-shadow: 0 0 0 1px var(--neon-1), 0 0 12px color-mix(in oklab,var(--neon-1) 58%,transparent), 0 0 42px color-mix(in oklab,var(--neon-1) 32%,transparent), 0 0 92px color-mix(in oklab,var(--neon-2) 24%,transparent);
  animation: cbk-14-pulse 6s ease-in-out infinite;
}

@keyframes cbk-14-pulse {
  50% {
    box-shadow: 0 0 0 1px var(--neon-1), 0 0 18px color-mix(in oklab,var(--neon-1) 74%,transparent), 0 0 58px color-mix(in oklab,var(--neon-1) 44%,transparent), 0 0 124px color-mix(in oklab,var(--neon-2) 34%,transparent);
  }
}

.cbk-14__bar {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .6rem 1rem;
  background: var(--bar);
  border-block-end: 1px solid color-mix(in oklab,var(--neon-1) 30%,transparent);
}

.cbk-14__dot {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: var(--neon-2);
  box-shadow: 0 0 8px var(--neon-2), 0 0 18px color-mix(in oklab,var(--neon-2) 60%,transparent);
}

.cbk-14__label {
  color: var(--neon-1);
  font-family: var(--mono);
  font-size: .78125rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  text-shadow: 0 0 10px color-mix(in oklab,var(--neon-1) 60%,transparent);
}

.cbk-14__ping {
  margin-inline-start: auto;
  padding: .15rem .5rem;
  border: 1px solid color-mix(in oklab,var(--neon-2) 55%,transparent);
  border-radius: 999px;
  color: var(--neon-2);
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.cbk-14__pre {
  position: relative;
  margin: 0;
  padding: 1.3rem 1.35rem 1.5rem;
  overflow-x: auto;
  scrollbar-width: thin;
  font-family: var(--mono);
  font-size: clamp(.78125rem,.45rem + .5cqi,.90625rem);
  line-height: 1.85;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
  background: repeating-linear-gradient(180deg, rgba(120,220,255,.045) 0 1px, transparent 1px 3px);
}

.cbk-14__pre code {
  font: inherit;
  position: relative;
}

.cbk-14__cursor {
  display: inline-block;
  inline-size: 9px;
  block-size: 1.05em;
  margin-inline-start: 2px;
  vertical-align: text-bottom;
  background: var(--neon-1);
  box-shadow: 0 0 10px var(--neon-1);
  animation: cbk-14-blink 1.2s steps(1,end) infinite;
}

@keyframes cbk-14-blink {
  0%,
    50% {
    opacity: 1;
  }

  51%,
    100% {
    opacity: 0;
  }
}

.cbk-14 .tok-keyword {
  color: var(--tok-key);
}

.cbk-14 .tok-string {
  color: var(--tok-str);
}

.cbk-14 .tok-function {
  color: var(--tok-fn);
}

.cbk-14 .tok-variable {
  color: var(--tok-var);
}

.cbk-14 .tok-number {
  color: var(--tok-num);
}

.cbk-14 .tok-punct {
  color: var(--tok-punct);
}

.cbk-14 .tok-op {
  color: var(--tok-op);
}

.cbk-14 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-14 .tok-comment {
  color: var(--tok-com);
  font-style: italic;
}

.cbk-14[data-theme="light"] {
  --bg: #f3f1fb;
  --surface: #12101c;
  --bar: #171426;
  background: radial-gradient(46rem 26rem at 18% 0%, rgba(34,211,238,.22), transparent 66%), radial-gradient(42rem 26rem at 84% 100%, rgba(217,70,239,.18), transparent 68%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-14:not([data-theme="dark"]) {
    --bg: #f3f1fb;
    background: radial-gradient(46rem 26rem at 18% 0%, rgba(34,211,238,.22), transparent 66%), radial-gradient(42rem 26rem at 84% 100%, rgba(217,70,239,.18), transparent 68%), var(--bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-14 *,
    .cbk-14 *::before,
    .cbk-14 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cbk-14__cursor {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .cbk-14__block {
    border: 2px solid CanvasText;
    background: Canvas;
    box-shadow: none;
    animation: none;
  }

  .cbk-14__pre {
    background: Canvas;
  }

  .cbk-14 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-14__stage {
  position: relative;
}

.cbk-14__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-14__tbtn {
  position: absolute;
  inset-block-start: clamp(.7rem,2vw,1.35rem);
  inset-inline-end: clamp(.7rem,2vw,1.35rem);
  z-index: 7;
  display: grid;
  place-items: center;
  inline-size: 2.375rem;
  block-size: 2.375rem;
  border: 1px solid rgba(127,127,127,.34);
  border-radius: 11px;
  background: rgba(127,127,127,.14);
  color: var(--ink,#e7eaf3);
  cursor: pointer;
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  transition: background .18s ease, border-color .18s ease, transform .18s ease;
}

@supports (color: color-mix(in srgb,red,blue)) {
  .cbk-14__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-14__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-14__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-14__tbox:focus-visible + .cbk-14__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-14__tmoon {
  display: none;
}

.cbk-14:has(.cbk-14__tbox:checked) .cbk-14__tsun {
  display: none;
}

.cbk-14:has(.cbk-14__tbox:checked) .cbk-14__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-14__tbtn {
    transition: none;
  }

  .cbk-14__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-14__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-14:has(.cbk-14__tbox:checked) {
  --bg: #f3f1fb;
  --surface: #12101c;
  --bar: #171426;
  background: radial-gradient(46rem 26rem at 18% 0%, rgba(34,211,238,.22), transparent 66%), radial-gradient(42rem 26rem at 84% 100%, rgba(217,70,239,.18), transparent 68%), var(--bg);
}

.cbk-14__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2vw,1.25rem);
  inset-inline-end: clamp(.75rem,2vw,1.25rem);
  z-index: 50;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,.12);
  color: currentColor;
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.cbk-14[data-theme="dark"] .cbk-14__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-14:not([data-theme="light"]) .cbk-14__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-14__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-14[data-theme="dark"] .cbk-14__theme:hover,
.cbk-14:not([data-theme="light"]) .cbk-14__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-14__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-14__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-14__sun {
  display: none;
}

.cbk-14__theme[aria-pressed="true"] .cbk-14__sun {
  display: block;
}

.cbk-14__theme[aria-pressed="true"] .cbk-14__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-14__theme {
    transition: none;
  }

  .cbk-14__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-14');if(!r)return;const t=r.querySelector('.cbk-14__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
