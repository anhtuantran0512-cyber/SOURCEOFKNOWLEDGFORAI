---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/code-block-with-copy-to-clipboard-button/"
title: "CSS Code Block with Copy to Clipboard Button"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "A deep dive on the copy interaction itself: a hover tooltip that explains the button before you press it, an icon that morphs to a checkmark, a floating…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Code Block with Copy to Clipboard Button
Source: https://codefronts.com/snippets/css-code-blocks/code-block-with-copy-to-clipboard-button/

A deep dive on the copy interaction itself: a hover tooltip that explains the button before you press it, an icon that morphs to a checkmark, a floating "Copied!" toast that rises and fades, a polite live-region announcement, and an honest error state when the clipboard is unavailable. Twenty-six lines of vanilla JavaScript, zero dependencies.
## HTML
```html
<div class="cbk-11">
  <button class="cbk-11__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-11__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-11__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-11__stage">
    <input class="cbk-11__tbox" id="cbk-11-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-11__tbtn" for="cbk-11-tbox" title="Toggle light and dark theme">
      <svg class="cbk-11__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-11__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-11__block" id="cbk-11-block">
      <figcaption class="cbk-11__bar">
        <span class="cbk-11__file">tailwind.config.ts</span>
        <span class="cbk-11__wrap">
          <button class="cbk-11__copy" type="button" id="cbk-11-copy" aria-label="Copy code to clipboard" data-state="">
            <svg class="cbk-11__ci cbk-11__ci--copy" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M15 6.5A2.5 2.5 0 0 0 12.5 4H6.5A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
            <svg class="cbk-11__ci cbk-11__ci--ok" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m5 12.5 4.4 4.4L19 7.3" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <svg class="cbk-11__ci cbk-11__ci--err" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.6"/><path d="M12 7.6v6m0 2.9h.01" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>
            <span class="cbk-11__tip" aria-hidden="true">Copy</span>
          </button>
          <span class="cbk-11__toast" aria-hidden="true">Copied!</span>
        </span>
      </figcaption>

      <div class="cbk-11__scroll">
<pre class="cbk-11__pre"><code class="language-ts"><span class="tok-keyword">import type</span> <span class="tok-punct">{</span> <span class="tok-fn2">Config</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'tailwindcss'</span><span class="tok-punct">;</span>

<span class="tok-keyword">export default</span> <span class="tok-punct">{</span>
  <span class="tok-variable">content</span><span class="tok-punct">: [</span><span class="tok-string">'./app/**/*.{ts,tsx,mdx}'</span><span class="tok-punct">],</span>
  <span class="tok-variable">theme</span><span class="tok-punct">: {</span>
    <span class="tok-variable">extend</span><span class="tok-punct">: {</span>
      <span class="tok-variable">fontFamily</span><span class="tok-punct">: {</span> <span class="tok-variable">mono</span><span class="tok-punct">: [</span><span class="tok-string">'JetBrains Mono'</span><span class="tok-punct">,</span> <span class="tok-string">'ui-monospace'</span><span class="tok-punct">] },</span>
      <span class="tok-variable">colors</span><span class="tok-punct">: {</span> <span class="tok-variable">brand</span><span class="tok-punct">:</span> <span class="tok-string">'oklch(72% 0.16 292)'</span> <span class="tok-punct">},</span>
      <span class="tok-variable">borderRadius</span><span class="tok-punct">: {</span> <span class="tok-variable">xl</span><span class="tok-punct">:</span> <span class="tok-string">'14px'</span> <span class="tok-punct">},</span>
    <span class="tok-punct">},</span>
  <span class="tok-punct">},</span>
<span class="tok-punct">} </span><span class="tok-keyword">satisfies</span> <span class="tok-fn2">Config</span><span class="tok-punct">;</span></code></pre>
      </div>
      <p class="cbk-11__status" role="status" aria-live="polite" id="cbk-11-status"></p>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-11 {
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
  --acc: #38bdf8;
  --ok: #4ade80;
  --err: #f87171;
  --tip: #1c2230;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-fn2: #5eead4;
  background: radial-gradient(58rem 32rem at 50% -8%, #101a26 0%, transparent 64%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-11 {
    --bg: oklch(12% .012 260);
    --surface: oklch(16.5% .014 260);
    --bar: oklch(20% .016 260);
    --line: oklch(27% .018 260);
    --ink: oklch(93% .008 260);
    --muted: oklch(69% .02 260);
    --acc: oklch(80% .13 225);
    --ok: oklch(84% .17 150);
    --err: oklch(72% .17 25);
    --tip: oklch(24% .02 260);
  }
}

.cbk-11 *,
.cbk-11 *::before,
.cbk-11 *::after {
  box-sizing: border-box;
}

.cbk-11__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-11__block {
  margin: 0;
  inline-size: min(52rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  container-type: inline-size;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04), 0 22px 54px -30px rgba(0,0,0,.9);
}

.cbk-11__bar {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .5rem .5rem .5rem .95rem;
  border-block-end: 1px solid var(--line);
  background: var(--bar);
  border-radius: 14px 14px 0 0;
}

.cbk-11__file {
  color: var(--muted);
  font-family: var(--mono);
  font-size: .78125rem;
}

.cbk-11__wrap {
  position: relative;
  margin-inline-start: auto;
  display: flex;
}

.cbk-11__copy {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: color-mix(in oklab,var(--ink) 5%,transparent);
  color: var(--muted);
  cursor: pointer;
  transition: color .18s, border-color .18s, background-color .18s, scale .12s;
}

.cbk-11__copy:hover {
  color: var(--ink);
  border-color: color-mix(in oklab,var(--ink) 28%,transparent);
}

.cbk-11__copy:active {
  scale: .94;
}

.cbk-11__ci {
  position: absolute;
  inline-size: 18px;
  block-size: 18px;
  opacity: 0;
  scale: .55;
  transition: opacity .18s, scale .18s cubic-bezier(.2,.9,.25,1);
}

.cbk-11__copy[data-state=""] .cbk-11__ci--copy {
  opacity: 1;
  scale: 1;
}

.cbk-11__copy[data-state="copied"] {
  color: var(--ok);
  border-color: color-mix(in oklab,var(--ok) 45%,transparent);
  background: color-mix(in oklab,var(--ok) 13%,transparent);
}

.cbk-11__copy[data-state="copied"] .cbk-11__ci--ok {
  opacity: 1;
  scale: 1;
}

.cbk-11__copy[data-state="error"] {
  color: var(--err);
  border-color: color-mix(in oklab,var(--err) 45%,transparent);
}

.cbk-11__copy[data-state="error"] .cbk-11__ci--err {
  opacity: 1;
  scale: 1;
}

.cbk-11__tip {
  position: absolute;
  inset-block-end: calc(100% + 8px);
  inset-inline-end: 0;
  padding: .3rem .5rem;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: var(--tip);
  color: var(--ink);
  font-size: .71875rem;
  white-space: nowrap;
  opacity: 0;
  translate: 0 4px;
  pointer-events: none;
  transition: opacity .16s, translate .16s;
}

.cbk-11__copy:hover .cbk-11__tip,
.cbk-11__copy:focus-visible .cbk-11__tip {
  opacity: 1;
  translate: 0 0;
}

.cbk-11__copy[data-state="copied"] .cbk-11__tip,
.cbk-11__copy[data-state="error"] .cbk-11__tip {
  opacity: 0;
}

.cbk-11__toast {
  position: absolute;
  inset-block-end: calc(100% + 10px);
  inset-inline-end: 0;
  padding: .32rem .6rem;
  border-radius: 8px;
  background: var(--ok);
  color: #052e16;
  font-size: .71875rem;
  font-weight: 600;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
}

.cbk-11__copy[data-state="copied"] ~ .cbk-11__toast {
  animation: cbk-11-toast 2s cubic-bezier(.2,.9,.25,1) forwards;
}

@keyframes cbk-11-toast {
  0% {
    opacity: 0;
    translate: 0 6px;
    scale: .94;
  }

  14% {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }

  70% {
    opacity: 1;
    translate: 0 0;
  }

  100% {
    opacity: 0;
    translate: 0 -6px;
  }
}

.cbk-11__scroll {
  overflow: auto;
  scrollbar-gutter: stable;
  border-radius: 0 0 14px 14px;
}

.cbk-11__pre {
  margin: 0;
  padding: 1.15rem 1.25rem 1.35rem;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.45rem + .5cqi,.9375rem);
  line-height: 1.75;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-11__pre code {
  font: inherit;
}

.cbk-11__status {
  margin: 0;
  padding: 0 1.25rem;
  max-block-size: 0;
  overflow: hidden;
  color: var(--ok);
  font-size: .75rem;
  transition: max-block-size .2s, padding-block .2s;
}

.cbk-11__status:not(:empty) {
  max-block-size: 2.4rem;
  padding-block: 0 .8rem;
}

.cbk-11 .tok-keyword {
  color: var(--tok-key);
}

.cbk-11 .tok-string {
  color: var(--tok-str);
}

.cbk-11 .tok-function {
  color: var(--tok-fn);
}

.cbk-11 .tok-variable {
  color: var(--tok-var);
}

.cbk-11 .tok-number {
  color: var(--tok-num);
}

.cbk-11 .tok-punct {
  color: var(--tok-punct);
}

.cbk-11 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-11 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cbk-11[data-theme="light"] {
  --bg: #f6f8fb;
  --surface: #ffffff;
  --bar: #f1f4f9;
  --line: #e2e6f0;
  --ink: #11131a;
  --muted: #5b6373;
  --acc: #0284c7;
  --ok: #0f8a4d;
  --err: #c0392b;
  --tip: #111827;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-fn2: #0f766e;
  background: radial-gradient(58rem 32rem at 50% -8%, #e6eefc 0%, transparent 64%), var(--bg);
}

.cbk-11[data-theme="light"] .cbk-11__tip {
  color: #fff;
}

.cbk-11[data-theme="light"] .cbk-11__toast {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .cbk-11:not([data-theme="dark"]) {
    --bg: #f6f8fb;
    --surface: #ffffff;
    --bar: #f1f4f9;
    --line: #e2e6f0;
    --ink: #11131a;
    --muted: #5b6373;
    --acc: #0284c7;
    --ok: #0f8a4d;
    --err: #c0392b;
    --tip: #111827;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-fn2: #0f766e;
    background: radial-gradient(58rem 32rem at 50% -8%, #e6eefc 0%, transparent 64%), var(--bg);
  }

  .cbk-11:not([data-theme="dark"]) .cbk-11__tip,
    .cbk-11:not([data-theme="dark"]) .cbk-11__toast {
    color: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-11 *,
    .cbk-11 *::before,
    .cbk-11 *::after {
    animation-duration: .01ms !important;
    transition: none !important;
  }

  .cbk-11__copy[data-state="copied"] ~ .cbk-11__toast {
    animation: none;
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .cbk-11__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-11__copy {
    border: 1px solid CanvasText;
    color: CanvasText;
  }

  .cbk-11 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-11__stage {
  position: relative;
}

.cbk-11__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-11__tbtn {
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
  .cbk-11__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-11__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-11__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-11__tbox:focus-visible + .cbk-11__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-11__tmoon {
  display: none;
}

.cbk-11:has(.cbk-11__tbox:checked) .cbk-11__tsun {
  display: none;
}

.cbk-11:has(.cbk-11__tbox:checked) .cbk-11__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-11__tbtn {
    transition: none;
  }

  .cbk-11__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-11__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-11:has(.cbk-11__tbox:checked) {
  --bg: #f6f8fb;
  --surface: #ffffff;
  --bar: #f1f4f9;
  --line: #e2e6f0;
  --ink: #11131a;
  --muted: #5b6373;
  --acc: #0284c7;
  --ok: #0f8a4d;
  --err: #c0392b;
  --tip: #111827;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-fn2: #0f766e;
  background: radial-gradient(58rem 32rem at 50% -8%, #e6eefc 0%, transparent 64%), var(--bg);
}

.cbk-11:has(.cbk-11__tbox:checked) .cbk-11__tip {
  color: #fff;
}

.cbk-11:has(.cbk-11__tbox:checked) .cbk-11__toast {
  color: #fff;
}

.cbk-11__theme {
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

.cbk-11[data-theme="dark"] .cbk-11__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-11:not([data-theme="light"]) .cbk-11__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-11__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-11[data-theme="dark"] .cbk-11__theme:hover,
.cbk-11:not([data-theme="light"]) .cbk-11__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-11__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-11__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-11__sun {
  display: none;
}

.cbk-11__theme[aria-pressed="true"] .cbk-11__sun {
  display: block;
}

.cbk-11__theme[aria-pressed="true"] .cbk-11__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-11__theme {
    transition: none;
  }

  .cbk-11__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('cbk-11-copy');
  const status = document.getElementById('cbk-11-status');
  const code = document.querySelector('#cbk-11-block code');
  if (!btn || !code) return;
  let timer;
  const done = (state) => {
    btn.dataset.state = state;
    status.textContent = state === 'copied' ? 'Code copied to clipboard' : 'Copy blocked — select the code and press Ctrl+C.';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = ''; status.textContent = ''; }, 2000);
  };
  btn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(code.textContent);
      done('copied');
    } catch {
      const ta = Object.assign(document.createElement('textarea'), { value: code.textContent });
      ta.style.cssText = 'position:fixed;top:0;opacity:0';
      document.body.append(ta);
      ta.select();
      done(document.execCommand && document.execCommand('copy') ? 'copied' : 'error');
      ta.remove();
    }
  });
})();
(()=>{const r=document.querySelector('.cbk-11');if(!r)return;const t=r.querySelector('.cbk-11__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
