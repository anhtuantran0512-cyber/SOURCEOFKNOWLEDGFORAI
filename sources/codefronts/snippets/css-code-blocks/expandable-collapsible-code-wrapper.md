---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/expandable-collapsible-code-wrapper/"
title: "Expandable Collapsible CSS Code Wrapper (Show More Button)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "Long snippets should not eat a whole screen."
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Collapsible CSS Code Wrapper (Show More Button)
Source: https://codefronts.com/snippets/css-code-blocks/expandable-collapsible-code-wrapper/

Long snippets should not eat a whole screen. This wrapper collapses to six lines with a mask-based fade, then expands to full height on click — no JavaScript, using a hidden checkbox and :checked. The label swaps between "Show more" and "Show less" with a rotating chevron, and the collapsed region is masked rather than covered, so the fade works on any surface.
## HTML
```html
<div class="cbk-20">
  <button class="cbk-20__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-20__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-20__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-20__stage">
    <input class="cbk-20__tbox" id="cbk-20-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-20__tbtn" for="cbk-20-tbox" title="Toggle light and dark theme">
      <svg class="cbk-20__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-20__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-20__block">
      <figcaption class="cbk-20__bar">
        <span class="cbk-20__file">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 3.5h7L18 8v12.5H6.5z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M13 3.5V8h5" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
          Button.stories.tsx
        </span>
        <span class="cbk-20__lines">24 lines</span>
      </figcaption>

      <input class="cbk-20__toggle" type="checkbox" id="cbk-20-more">
      <div class="cbk-20__clip">
<pre class="cbk-20__pre"><code class="language-tsx"><span class="tok-keyword">import type</span> <span class="tok-punct">{</span> <span class="tok-fn2">Meta</span><span class="tok-punct">,</span> <span class="tok-fn2">StoryObj</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'@storybook/react'</span><span class="tok-punct">;</span>
<span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-function">Button</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'./Button'</span><span class="tok-punct">;</span>

<span class="tok-keyword">const</span> <span class="tok-variable">meta</span> <span class="tok-op">=</span> <span class="tok-punct">{</span>
  <span class="tok-variable">title</span><span class="tok-punct">:</span> <span class="tok-string">'Primitives/Button'</span><span class="tok-punct">,</span>
  <span class="tok-variable">component</span><span class="tok-punct">:</span> <span class="tok-function">Button</span><span class="tok-punct">,</span>
  <span class="tok-variable">parameters</span><span class="tok-punct">: {</span> <span class="tok-variable">layout</span><span class="tok-punct">:</span> <span class="tok-string">'centered'</span> <span class="tok-punct">},</span>
  <span class="tok-variable">argTypes</span><span class="tok-punct">: {</span>
    <span class="tok-variable">tone</span><span class="tok-punct">: {</span> <span class="tok-variable">control</span><span class="tok-punct">:</span> <span class="tok-string">'inline-radio'</span><span class="tok-punct">,</span> <span class="tok-variable">options</span><span class="tok-punct">: [</span><span class="tok-string">'brand'</span><span class="tok-punct">,</span> <span class="tok-string">'ghost'</span><span class="tok-punct">,</span> <span class="tok-string">'critical'</span><span class="tok-punct">] },</span>
    <span class="tok-variable">size</span><span class="tok-punct">: {</span> <span class="tok-variable">control</span><span class="tok-punct">:</span> <span class="tok-string">'inline-radio'</span><span class="tok-punct">,</span> <span class="tok-variable">options</span><span class="tok-punct">: [</span><span class="tok-string">'sm'</span><span class="tok-punct">,</span> <span class="tok-string">'md'</span><span class="tok-punct">,</span> <span class="tok-string">'lg'</span><span class="tok-punct">] },</span>
  <span class="tok-punct">},</span>
<span class="tok-punct">} </span><span class="tok-keyword">satisfies</span> <span class="tok-fn2">Meta</span><span class="tok-op">&lt;</span><span class="tok-keyword">typeof</span> <span class="tok-function">Button</span><span class="tok-op">&gt;</span><span class="tok-punct">;</span>

<span class="tok-keyword">export default</span> <span class="tok-variable">meta</span><span class="tok-punct">;</span>
<span class="tok-keyword">type</span> <span class="tok-fn2">Story</span> <span class="tok-op">=</span> <span class="tok-fn2">StoryObj</span><span class="tok-op">&lt;</span><span class="tok-keyword">typeof</span> <span class="tok-variable">meta</span><span class="tok-op">&gt;</span><span class="tok-punct">;</span>

<span class="tok-keyword">export const</span> <span class="tok-function">Brand</span><span class="tok-punct">:</span> <span class="tok-fn2">Story</span> <span class="tok-op">=</span> <span class="tok-punct">{</span>
  <span class="tok-variable">args</span><span class="tok-punct">: {</span> <span class="tok-variable">tone</span><span class="tok-punct">:</span> <span class="tok-string">'brand'</span><span class="tok-punct">,</span> <span class="tok-variable">size</span><span class="tok-punct">:</span> <span class="tok-string">'md'</span><span class="tok-punct">,</span> <span class="tok-variable">children</span><span class="tok-punct">:</span> <span class="tok-string">'Deploy project'</span> <span class="tok-punct">},</span>
<span class="tok-punct">};</span>

<span class="tok-keyword">export const</span> <span class="tok-function">Critical</span><span class="tok-punct">:</span> <span class="tok-fn2">Story</span> <span class="tok-op">=</span> <span class="tok-punct">{</span>
  <span class="tok-variable">args</span><span class="tok-punct">: {</span> <span class="tok-variable">tone</span><span class="tok-punct">:</span> <span class="tok-string">'critical'</span><span class="tok-punct">,</span> <span class="tok-variable">children</span><span class="tok-punct">:</span> <span class="tok-string">'Delete workspace'</span> <span class="tok-punct">},</span>
  <span class="tok-variable">play</span><span class="tok-punct">: </span><span class="tok-keyword">async</span> <span class="tok-punct">({</span> <span class="tok-variable">canvasElement</span> <span class="tok-punct">}) =&gt; {</span>
    <span class="tok-keyword">const</span> <span class="tok-variable">btn</span> <span class="tok-op">=</span> <span class="tok-variable">canvasElement</span><span class="tok-punct">.</span><span class="tok-function">querySelector</span><span class="tok-punct">(</span><span class="tok-string">'button'</span><span class="tok-punct">);</span>
    <span class="tok-variable">btn</span><span class="tok-punct">?.</span><span class="tok-function">focus</span><span class="tok-punct">();</span>
  <span class="tok-punct">},</span>
<span class="tok-punct">};</span></code></pre>
      </div>

      <label class="cbk-20__btn" for="cbk-20-more">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 10 5 5 5-5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </label>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-20 {
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
  --acc: #5eead4;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-op: #ff9d6b;
  --tok-fn2: #5eead4;
  background: radial-gradient(60rem 34rem at 50% -10%, #0f2225 0%, transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-20 {
    --bg: oklch(12% .012 250);
    --surface: oklch(16.5% .014 250);
    --bar: oklch(20% .016 250);
    --line: oklch(27% .018 250);
    --ink: oklch(93% .008 250);
    --muted: oklch(69% .02 250);
    --acc: oklch(85% .13 175);
  }
}

.cbk-20 *,
.cbk-20 *::before,
.cbk-20 *::after {
  box-sizing: border-box;
}

.cbk-20__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-20__block {
  margin: 0;
  inline-size: min(54rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04), 0 22px 54px -30px rgba(0,0,0,.9);
}

.cbk-20__bar {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .65rem 1rem;
  border-block-end: 1px solid var(--line);
  background: var(--bar);
  font-size: .78125rem;
}

.cbk-20__file {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  color: var(--ink);
  font-family: var(--mono);
}

.cbk-20__file svg {
  inline-size: 14px;
  block-size: 14px;
  color: var(--muted);
}

.cbk-20__lines {
  margin-inline-start: auto;
  color: var(--muted);
  font-family: var(--mono);
  font-size: .71875rem;
}

.cbk-20__toggle {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  opacity: 0;
}

.cbk-20__clip {
  max-block-size: 19rem;
  overflow: hidden;
  -webkit-mask-image: linear-gradient(#000 58%, transparent 98%);
  mask-image: linear-gradient(#000 58%, transparent 98%);
  transition: max-block-size .42s cubic-bezier(.2,.9,.25,1);
}

@supports (max-block-size: 1lh) {
  .cbk-20__clip {
    max-block-size: calc(6lh + 2.5rem);
  }
}

.cbk-20__toggle:checked ~ .cbk-20__clip {
  max-block-size: 200lh;
  -webkit-mask-image: none;
  mask-image: none;
}

@supports not (max-block-size: 1lh) {
  .cbk-20__toggle:checked ~ .cbk-20__clip {
    max-block-size: 120rem;
  }
}

.cbk-20__pre {
  margin: 0;
  padding: 1.15rem 1.25rem 1.35rem;
  overflow-x: auto;
  scrollbar-width: thin;
  font-family: var(--mono);
  font-size: clamp(.78125rem,.45rem + .48cqi,.90625rem);
  line-height: 1.8;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-20__pre code {
  font: inherit;
}

.cbk-20__btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .45rem;
  min-block-size: 46px;
  padding: .7rem 1rem;
  border-block-start: 1px solid var(--line);
  background: color-mix(in oklab,var(--ink) 4%,transparent);
  color: var(--acc);
  cursor: pointer;
  font-family: var(--sans);
  font-size: .8125rem;
  font-weight: 600;
  letter-spacing: .01em;
  user-select: none;
  transition: background-color .18s, color .18s;
}

.cbk-20__btn::after {
  content: "Show more";
}

.cbk-20__btn:hover {
  background: color-mix(in oklab,var(--acc) 12%,transparent);
}

.cbk-20__btn svg {
  inline-size: 16px;
  block-size: 16px;
  transition: rotate .3s cubic-bezier(.2,.9,.25,1);
}

.cbk-20__toggle:checked ~ .cbk-20__btn::after {
  content: "Show less";
}

.cbk-20__toggle:checked ~ .cbk-20__btn svg {
  rotate: 180deg;
}

.cbk-20__toggle:focus-visible ~ .cbk-20__btn {
  outline: 2px solid var(--acc);
  outline-offset: -3px;
}

.cbk-20 .tok-keyword {
  color: var(--tok-key);
}

.cbk-20 .tok-string {
  color: var(--tok-str);
}

.cbk-20 .tok-function {
  color: var(--tok-fn);
}

.cbk-20 .tok-variable {
  color: var(--tok-var);
}

.cbk-20 .tok-number {
  color: var(--tok-num);
}

.cbk-20 .tok-punct {
  color: var(--tok-punct);
}

.cbk-20 .tok-op {
  color: var(--tok-op);
}

.cbk-20 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-20[data-theme="light"] {
  --bg: #f5f9f8;
  --surface: #ffffff;
  --bar: #eff5f4;
  --line: #e0e8e6;
  --ink: #11131a;
  --muted: #59636e;
  --acc: #0f766e;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  background: radial-gradient(60rem 34rem at 50% -10%, #e2f2f0 0%, transparent 62%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-20:not([data-theme="dark"]) {
    --bg: #f5f9f8;
    --surface: #ffffff;
    --bar: #eff5f4;
    --line: #e0e8e6;
    --ink: #11131a;
    --muted: #59636e;
    --acc: #0f766e;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-op: #a2410a;
    --tok-fn2: #0f766e;
    background: radial-gradient(60rem 34rem at 50% -10%, #e2f2f0 0%, transparent 62%), var(--bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-20 *,
    .cbk-20 *::before,
    .cbk-20 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cbk-20__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-20__clip {
    -webkit-mask-image: none;
    mask-image: none;
  }

  .cbk-20__btn {
    border-block-start: 1px solid CanvasText;
    color: LinkText;
  }

  .cbk-20 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-20__stage {
  position: relative;
}

.cbk-20__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-20__tbtn {
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
  .cbk-20__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-20__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-20__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-20__tbox:focus-visible + .cbk-20__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-20__tmoon {
  display: none;
}

.cbk-20:has(.cbk-20__tbox:checked) .cbk-20__tsun {
  display: none;
}

.cbk-20:has(.cbk-20__tbox:checked) .cbk-20__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-20__tbtn {
    transition: none;
  }

  .cbk-20__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-20__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-20:has(.cbk-20__tbox:checked) {
  --bg: #f5f9f8;
  --surface: #ffffff;
  --bar: #eff5f4;
  --line: #e0e8e6;
  --ink: #11131a;
  --muted: #59636e;
  --acc: #0f766e;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  background: radial-gradient(60rem 34rem at 50% -10%, #e2f2f0 0%, transparent 62%), var(--bg);
}

.cbk-20__theme {
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

.cbk-20[data-theme="dark"] .cbk-20__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-20:not([data-theme="light"]) .cbk-20__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-20__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-20[data-theme="dark"] .cbk-20__theme:hover,
.cbk-20:not([data-theme="light"]) .cbk-20__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-20__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-20__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-20__sun {
  display: none;
}

.cbk-20__theme[aria-pressed="true"] .cbk-20__sun {
  display: block;
}

.cbk-20__theme[aria-pressed="true"] .cbk-20__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-20__theme {
    transition: none;
  }

  .cbk-20__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-20');if(!r)return;const t=r.querySelector('.cbk-20__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
