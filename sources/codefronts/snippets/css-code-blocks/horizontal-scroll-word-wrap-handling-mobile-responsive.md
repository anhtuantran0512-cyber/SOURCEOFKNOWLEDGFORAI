---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/horizontal-scroll-word-wrap-handling-mobile-responsive/"
title: "Responsive CSS Code Block (Mobile Horizontal Scroll and Word Wrap)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "Long lines are the hardest part of shipping code on phones."
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive CSS Code Block (Mobile Horizontal Scroll and Word Wrap)
Source: https://codefronts.com/snippets/css-code-blocks/horizontal-scroll-word-wrap-handling-mobile-responsive/

Long lines are the hardest part of shipping code on phones. This block does both correct things: it scrolls horizontally with a fade that appears only while there is more to see, and it offers a word-wrap toggle with hanging indents so wrapped continuations stay readable. Container queries drive the layout, and the fade is powered by a scroll-driven animation with a static fallback.
## HTML
```html
<div class="cbk-13" id="cbk-13-root" data-wrap="off">
  <button class="cbk-13__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-13__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-13__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-13__stage">
    <input class="cbk-13__tbox" id="cbk-13-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-13__tbtn" for="cbk-13-tbox" title="Toggle light and dark theme">
      <svg class="cbk-13__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-13__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-13__block">
      <figcaption class="cbk-13__bar">
        <span class="cbk-13__file">next.config.mjs</span>
        <button class="cbk-13__toggle" type="button" id="cbk-13-toggle" aria-pressed="false">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 6.5h16M4 12h11.5a3.2 3.2 0 1 1 0 6.4H12" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="m13.6 16.2-1.8 2.2 1.8 2.1" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span class="cbk-13__toggle-t">Wrap lines</span>
        </button>
      </figcaption>

      <div class="cbk-13__wrapper">
        <div class="cbk-13__scroll" tabindex="0" role="region" aria-label="Code, scroll horizontally to see long lines">
<pre class="cbk-13__pre"><code class="language-js"><span class="tok-comment">/** @type {import('next').NextConfig} */</span>
<span class="tok-keyword">const</span> <span class="tok-variable">nextConfig</span> <span class="tok-op">=</span> <span class="tok-punct">{</span>
  <span class="tok-variable">images</span><span class="tok-punct">: {</span> <span class="tok-variable">remotePatterns</span><span class="tok-punct">: [{</span> <span class="tok-variable">protocol</span><span class="tok-punct">:</span> <span class="tok-string">'https'</span><span class="tok-punct">,</span> <span class="tok-variable">hostname</span><span class="tok-punct">:</span> <span class="tok-string">'picsum.photos'</span> <span class="tok-punct">}] },</span>
  <span class="tok-variable">experimental</span><span class="tok-punct">: {</span> <span class="tok-variable">optimizePackageImports</span><span class="tok-punct">: [</span><span class="tok-string">'@tanstack/react-query'</span><span class="tok-punct">,</span> <span class="tok-string">'framer-motion'</span><span class="tok-punct">,</span> <span class="tok-string">'date-fns'</span><span class="tok-punct">] },</span>
  <span class="tok-keyword">async</span> <span class="tok-function">headers</span><span class="tok-punct">() {</span>
    <span class="tok-keyword">return</span> <span class="tok-punct">[{</span> <span class="tok-variable">source</span><span class="tok-punct">:</span> <span class="tok-string">'/(.*)'</span><span class="tok-punct">,</span> <span class="tok-variable">headers</span><span class="tok-punct">: [{</span> <span class="tok-variable">key</span><span class="tok-punct">:</span> <span class="tok-string">'Strict-Transport-Security'</span><span class="tok-punct">,</span> <span class="tok-variable">value</span><span class="tok-punct">:</span> <span class="tok-string">'max-age=63072000; includeSubDomains; preload'</span> <span class="tok-punct">}] }];</span>
  <span class="tok-punct">},</span>
<span class="tok-punct">};</span>

<span class="tok-keyword">export default</span> <span class="tok-variable">nextConfig</span><span class="tok-punct">;</span></code></pre>
        </div>
        <span class="cbk-13__fade" aria-hidden="true"></span>
      </div>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-13 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #07080c;
  --surface: #0e1117;
  --bar: #12161f;
  --line: #212634;
  --ink: #e7eaf3;
  --muted: #8e96a7;
  --acc: #f472b6;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-op: #ff9d6b;
  --tok-com: #8e96a7;
  background: radial-gradient(58rem 32rem at 50% -8%, #211423 0%, transparent 64%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-13 {
    --bg: oklch(12% .012 300);
    --surface: oklch(16.5% .014 300);
    --bar: oklch(20% .016 300);
    --line: oklch(27% .018 300);
    --ink: oklch(93% .008 300);
    --muted: oklch(69% .02 300);
    --acc: oklch(78% .15 350);
    --tok-com: oklch(69% .02 300);
  }
}

.cbk-13 *,
.cbk-13 *::before,
.cbk-13 *::after {
  box-sizing: border-box;
}

.cbk-13__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-13__block {
  margin: 0;
  inline-size: min(50rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04), 0 22px 54px -30px rgba(0,0,0,.9);
}

.cbk-13__bar {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .5rem .5rem .5rem .95rem;
  border-block-end: 1px solid var(--line);
  background: var(--bar);
}

.cbk-13__file {
  color: var(--muted);
  font-family: var(--mono);
  font-size: .78125rem;
}

.cbk-13__toggle {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  margin-inline-start: auto;
  min-block-size: 36px;
  padding: .4rem .65rem;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: color-mix(in oklab,var(--ink) 5%,transparent);
  color: var(--muted);
  cursor: pointer;
  font-family: var(--sans);
  font-size: .75rem;
  font-weight: 500;
  transition: color .16s, border-color .16s, background-color .16s;
}

.cbk-13__toggle svg {
  inline-size: 15px;
  block-size: 15px;
}

.cbk-13__toggle:hover {
  color: var(--ink);
  border-color: color-mix(in oklab,var(--ink) 26%,transparent);
}

.cbk-13__toggle[aria-pressed="true"] {
  color: var(--acc);
  border-color: color-mix(in oklab,var(--acc) 45%,transparent);
  background: color-mix(in oklab,var(--acc) 13%,transparent);
}

.cbk-13__wrapper {
  position: relative;
}

.cbk-13__scroll {
  overflow-x: auto;
  overscroll-behavior-inline: contain;
  scrollbar-gutter: stable;
  scrollbar-width: thin;
  scrollbar-color: var(--line) transparent;
}

.cbk-13__scroll::-webkit-scrollbar {
  block-size: 9px;
}

.cbk-13__scroll::-webkit-scrollbar-thumb {
  background: var(--line);
  border-radius: 999px;
}

.cbk-13__pre {
  margin: 0;
  padding: 1.15rem 1.25rem 1.3rem;
  font-family: var(--mono);
  font-size: clamp(.78125rem,.42rem + .5cqi,.90625rem);
  line-height: 1.8;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-13__pre code {
  font: inherit;
}

.cbk-13[data-wrap="on"] .cbk-13__pre {
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  text-indent: -2ch;
  padding-inline-start: calc(1.25rem + 2ch);
}

.cbk-13[data-wrap="on"] .cbk-13__fade {
  display: none;
}

.cbk-13__fade {
  position: absolute;
  inset-block: 0;
  inset-inline-end: 0;
  inline-size: 4.5rem;
  pointer-events: none;
  background: linear-gradient(to right, transparent, var(--surface) 78%);
}

@supports (animation-timeline: scroll()) {
  .cbk-13__fade {
    animation: cbk-13-fade linear both;
    animation-timeline: scroll(nearest inline);
  }
}

@keyframes cbk-13-fade {
  0%,
    78% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

.cbk-13 .tok-keyword {
  color: var(--tok-key);
}

.cbk-13 .tok-string {
  color: var(--tok-str);
}

.cbk-13 .tok-function {
  color: var(--tok-fn);
}

.cbk-13 .tok-variable {
  color: var(--tok-var);
}

.cbk-13 .tok-number {
  color: var(--tok-num);
}

.cbk-13 .tok-punct {
  color: var(--tok-punct);
}

.cbk-13 .tok-op {
  color: var(--tok-op);
}

.cbk-13 .tok-comment {
  color: var(--tok-com);
  font-style: italic;
}

.cbk-13 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@container (max-width: 30rem) {
  .cbk-13__toggle-t {
    position: absolute;
    inline-size: 1px;
    block-size: 1px;
    overflow: hidden;
    clip-path: inset(50%);
  }

  .cbk-13__toggle {
    padding-inline: .5rem;
  }
}

.cbk-13[data-theme="light"] {
  --bg: #faf7f9;
  --surface: #ffffff;
  --bar: #f6f2f5;
  --line: #eae4e9;
  --ink: #141118;
  --muted: #5f5a68;
  --acc: #be185d;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-com: #5f5a68;
  background: radial-gradient(58rem 32rem at 50% -8%, #fce9f2 0%, transparent 64%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-13:not([data-theme="dark"]) {
    --bg: #faf7f9;
    --surface: #ffffff;
    --bar: #f6f2f5;
    --line: #eae4e9;
    --ink: #141118;
    --muted: #5f5a68;
    --acc: #be185d;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-op: #a2410a;
    --tok-com: #5f5a68;
    background: radial-gradient(58rem 32rem at 50% -8%, #fce9f2 0%, transparent 64%), var(--bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-13 *,
    .cbk-13 *::before,
    .cbk-13 *::after {
    transition: none !important;
  }

  .cbk-13__scroll {
    scroll-behavior: auto;
  }
}

@media (forced-colors: active) {
  .cbk-13__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-13__fade {
    display: none;
  }

  .cbk-13__toggle {
    border: 1px solid CanvasText;
    color: CanvasText;
  }

  .cbk-13 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-13__stage {
  position: relative;
}

.cbk-13__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-13__tbtn {
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
  .cbk-13__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-13__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-13__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-13__tbox:focus-visible + .cbk-13__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-13__tmoon {
  display: none;
}

.cbk-13:has(.cbk-13__tbox:checked) .cbk-13__tsun {
  display: none;
}

.cbk-13:has(.cbk-13__tbox:checked) .cbk-13__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-13__tbtn {
    transition: none;
  }

  .cbk-13__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-13__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-13:has(.cbk-13__tbox:checked) {
  --bg: #faf7f9;
  --surface: #ffffff;
  --bar: #f6f2f5;
  --line: #eae4e9;
  --ink: #141118;
  --muted: #5f5a68;
  --acc: #be185d;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-com: #5f5a68;
  background: radial-gradient(58rem 32rem at 50% -8%, #fce9f2 0%, transparent 64%), var(--bg);
}

.cbk-13__theme {
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

.cbk-13[data-theme="dark"] .cbk-13__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-13:not([data-theme="light"]) .cbk-13__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-13__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-13[data-theme="dark"] .cbk-13__theme:hover,
.cbk-13:not([data-theme="light"]) .cbk-13__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-13__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-13__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-13__sun {
  display: none;
}

.cbk-13__theme[aria-pressed="true"] .cbk-13__sun {
  display: block;
}

.cbk-13__theme[aria-pressed="true"] .cbk-13__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-13__theme {
    transition: none;
  }

  .cbk-13__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('cbk-13-root');
  const btn = document.getElementById('cbk-13-toggle');
  if (!root || !btn) return;

  btn.addEventListener('click', () => {
    const on = btn.getAttribute('aria-pressed') === 'true';
    btn.setAttribute('aria-pressed', String(!on));
    root.dataset.wrap = on ? 'off' : 'on';
  });
})();
(()=>{const r=document.querySelector('.cbk-13');if(!r)return;const t=r.querySelector('.cbk-13__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
