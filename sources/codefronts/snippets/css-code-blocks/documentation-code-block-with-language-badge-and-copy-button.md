---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/documentation-code-block-with-language-badge-and-copy-button/"
title: "Documentation Code Block with Language Badge and Copy Button"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "The workhorse of every documentation site — language badge left, filename centre, copy button right — rebuilt with the polish Docusaurus, Mintlify, Nextra…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Documentation Code Block with Language Badge and Copy Button
Source: https://codefronts.com/snippets/css-code-blocks/documentation-code-block-with-language-badge-and-copy-button/

The workhorse of every documentation site — language badge left, filename centre, copy button right — rebuilt with the polish Docusaurus, Mintlify, Nextra and VitePress all converge on. The badge is colour-coded per language from a single data-lang attribute, and it is real text, so screen readers and search crawlers both know this block is TSX.
## HTML
```html
<div class="cbk-06">
  <button class="cbk-06__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-06__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-06__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-06__stage">
    <input class="cbk-06__tbox" id="cbk-06-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-06__tbtn" for="cbk-06-tbox" title="Toggle light and dark theme">
      <svg class="cbk-06__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-06__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-06__block" data-lang="tsx" id="cbk-06-block">
      <figcaption class="cbk-06__bar">
        <span class="cbk-06__badge">TSX</span>
        <span class="cbk-06__file">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 3.5h7L18 8v12.5H6.5z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M13 3.5V8h5" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
          app/providers.tsx
        </span>
        <button class="cbk-06__copy" type="button" id="cbk-06-copy" aria-label="Copy code to clipboard" data-state="">
          <svg class="cbk-06__ci cbk-06__ci--copy" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M15 6.5A2.5 2.5 0 0 0 12.5 4H6.5A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <svg class="cbk-06__ci cbk-06__ci--ok" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m5 12.5 4.4 4.4L19 7.3" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span class="cbk-06__copy-txt" aria-hidden="true">Copy</span>
        </button>
      </figcaption>

      <div class="cbk-06__scroll">
<pre class="cbk-06__pre"><code class="language-tsx"><span class="tok-keyword">'use client'</span><span class="tok-punct">;</span>

<span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">QueryClient</span><span class="tok-punct">,</span> <span class="tok-variable">QueryClientProvider</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'@tanstack/react-query'</span><span class="tok-punct">;</span>
<span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">useState</span><span class="tok-punct">,</span> <span class="tok-keyword">type</span> <span class="tok-fn2">ReactNode</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'react'</span><span class="tok-punct">;</span>

<span class="tok-keyword">export function</span> <span class="tok-function">Providers</span><span class="tok-punct">({</span> <span class="tok-variable">children</span> <span class="tok-punct">}: {</span> <span class="tok-variable">children</span><span class="tok-punct">:</span> <span class="tok-fn2">ReactNode</span> <span class="tok-punct">}) {</span>
  <span class="tok-keyword">const</span> <span class="tok-punct">[</span><span class="tok-variable">client</span><span class="tok-punct">] =</span> <span class="tok-function">useState</span><span class="tok-punct">(</span>
    <span class="tok-punct">() =&gt;</span> <span class="tok-keyword">new</span> <span class="tok-function">QueryClient</span><span class="tok-punct">({</span>
      <span class="tok-variable">defaultOptions</span><span class="tok-punct">: {</span> <span class="tok-variable">queries</span><span class="tok-punct">: {</span> <span class="tok-variable">staleTime</span><span class="tok-punct">:</span> <span class="tok-number">30_000</span><span class="tok-punct">,</span> <span class="tok-variable">retry</span><span class="tok-punct">:</span> <span class="tok-number">1</span> <span class="tok-punct">} },</span>
    <span class="tok-punct">}),</span>
  <span class="tok-punct">);</span>

  <span class="tok-keyword">return</span> <span class="tok-punct">&lt;</span><span class="tok-function">QueryClientProvider</span> <span class="tok-variable">client</span><span class="tok-punct">={</span><span class="tok-variable">client</span><span class="tok-punct">}&gt;{</span><span class="tok-variable">children</span><span class="tok-punct">}&lt;/</span><span class="tok-function">QueryClientProvider</span><span class="tok-punct">&gt;;</span>
<span class="tok-punct">}</span></code></pre>
      </div>
      <p class="cbk-06__status" role="status" aria-live="polite" id="cbk-06-status"></p>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-06 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #07080d;
  --surface: #0e1118;
  --bar: #12161f;
  --line: #212634;
  --ink: #e7eaf3;
  --muted: #8f97a8;
  --hue: 245;
  --badge: #79c0ff;
  --badge-bg: rgba(121,192,255,.14);
  --ring: #79c0ff;
  --ok: #4ade80;
  --err: #f87171;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-fn2: #5eead4;
  background: radial-gradient(62rem 34rem at 50% -10%, #141827 0%, transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-06 {
    --bg: oklch(12% .012 265);
    --surface: oklch(16.5% .014 265);
    --bar: oklch(20% .016 265);
    --line: oklch(27% .018 265);
    --ink: oklch(93% .008 265);
    --muted: oklch(69% .02 265);
    --badge: oklch(80% .13 var(--hue));
    --badge-bg: oklch(80% .13 var(--hue) / .15);
    --ring: oklch(80% .13 var(--hue));
  }
}

.cbk-06 *,
.cbk-06 *::before,
.cbk-06 *::after {
  box-sizing: border-box;
}

.cbk-06__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-06__block {
  margin: 0;
  inline-size: min(58rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
  box-shadow: 0 1px 0 rgba(255,255,255,.04) inset, 0 20px 50px -28px rgba(0,0,0,.85);
  transition: box-shadow .22s, border-color .22s;
}

.cbk-06__block[data-lang="tsx"],
.cbk-06__block[data-lang="ts"],
.cbk-06__block[data-lang="js"] {
  --hue: 245;
}

.cbk-06__block[data-lang="css"] {
  --hue: 150;
}

.cbk-06__block[data-lang="shell"] {
  --hue: 265;
}

.cbk-06__block[data-lang="json"] {
  --hue: 85;
}

.cbk-06__block:has(:focus-visible) {
  border-color: color-mix(in oklab,var(--ring) 45%,var(--line));
}

.cbk-06__bar {
  display: flex;
  align-items: center;
  gap: .7rem;
  padding: .6rem .7rem .6rem .9rem;
  border-block-end: 1px solid var(--line);
  background: var(--bar);
}

.cbk-06__badge {
  padding: .22rem .5rem;
  border: 1px solid color-mix(in oklab,var(--badge) 34%,transparent);
  border-radius: 6px;
  background: var(--badge-bg);
  color: var(--badge);
  font-family: var(--mono);
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .07em;
}

.cbk-06__file {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  color: var(--muted);
  font-family: var(--mono);
  font-size: .78125rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.cbk-06__file svg {
  inline-size: 14px;
  block-size: 14px;
  flex: none;
}

.cbk-06__copy {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  margin-inline-start: auto;
  min-block-size: 36px;
  padding: .4rem .6rem;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: color-mix(in oklab,var(--ink) 5%,transparent);
  color: var(--muted);
  cursor: pointer;
  font-family: var(--sans);
  font-size: .78125rem;
  transition: color .18s, border-color .18s, background-color .18s;
}

.cbk-06__copy:hover {
  color: var(--ink);
  border-color: color-mix(in oklab,var(--ink) 26%,transparent);
}

.cbk-06__ci {
  inline-size: 16px;
  block-size: 16px;
  transition: opacity .16s, scale .16s;
}

.cbk-06__ci--ok {
  position: absolute;
  inset-inline-start: .6rem;
  opacity: 0;
  scale: .6;
  color: var(--ok);
}

.cbk-06__copy[data-state="copied"] {
  color: var(--ok);
  border-color: color-mix(in oklab,var(--ok) 40%,transparent);
}

.cbk-06__copy[data-state="copied"] .cbk-06__ci--copy {
  opacity: 0;
  scale: .6;
}

.cbk-06__copy[data-state="copied"] .cbk-06__ci--ok {
  opacity: 1;
  scale: 1;
}

.cbk-06__copy[data-state="copied"] .cbk-06__copy-txt::after {
  content: "ied";
}

.cbk-06__copy[data-state="error"] {
  color: var(--err);
  border-color: color-mix(in oklab,var(--err) 40%,transparent);
}

.cbk-06__copy-txt {
  display: none;
}

@container (min-width: 32rem) {
  .cbk-06__copy-txt {
    display: inline;
  }
}

.cbk-06__scroll {
  overflow: auto;
  scrollbar-gutter: stable;
}

.cbk-06__pre {
  margin: 0;
  padding: 1.15rem 1.25rem 1.35rem;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.45rem + .5cqi,.9375rem);
  line-height: 1.75;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-06__pre code {
  font: inherit;
}

.cbk-06__status {
  margin: 0;
  padding: 0 1.25rem;
  max-block-size: 0;
  overflow: hidden;
  color: var(--ok);
  font-size: .75rem;
  transition: max-block-size .2s, padding-block .2s;
}

.cbk-06__status:not(:empty) {
  max-block-size: 2.4rem;
  padding-block: 0 .75rem;
}

.cbk-06 .tok-keyword {
  color: var(--tok-key);
}

.cbk-06 .tok-string {
  color: var(--tok-str);
}

.cbk-06 .tok-function {
  color: var(--tok-fn);
}

.cbk-06 .tok-variable {
  color: var(--tok-var);
}

.cbk-06 .tok-number {
  color: var(--tok-num);
}

.cbk-06 .tok-punct {
  color: var(--tok-punct);
}

.cbk-06 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-06 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.cbk-06[data-theme="light"] {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --bar: #f2f4fa;
  --line: #e2e6f0;
  --ink: #11131a;
  --muted: #5b6373;
  --badge: #0550ae;
  --badge-bg: rgba(5,80,174,.10);
  --ring: #0550ae;
  --ok: #1a7f37;
  --err: #c0392b;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-fn2: #0f766e;
  background: radial-gradient(62rem 34rem at 50% -10%, #e9edff 0%, transparent 62%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-06:not([data-theme="dark"]) {
    --bg: #f6f7fb;
    --surface: #ffffff;
    --bar: #f2f4fa;
    --line: #e2e6f0;
    --ink: #11131a;
    --muted: #5b6373;
    --badge: #0550ae;
    --badge-bg: rgba(5,80,174,.10);
    --ring: #0550ae;
    --ok: #1a7f37;
    --err: #c0392b;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-fn2: #0f766e;
    background: radial-gradient(62rem 34rem at 50% -10%, #e9edff 0%, transparent 62%), var(--bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-06 *,
    .cbk-06 *::before,
    .cbk-06 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cbk-06__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-06__badge,
    .cbk-06__copy {
    border: 1px solid CanvasText;
    color: CanvasText;
    background: Canvas;
  }

  .cbk-06 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-06__stage {
  position: relative;
}

.cbk-06__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-06__tbtn {
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
  .cbk-06__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-06__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-06__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-06__tbox:focus-visible + .cbk-06__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-06__tmoon {
  display: none;
}

.cbk-06:has(.cbk-06__tbox:checked) .cbk-06__tsun {
  display: none;
}

.cbk-06:has(.cbk-06__tbox:checked) .cbk-06__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-06__tbtn {
    transition: none;
  }

  .cbk-06__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-06__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-06:has(.cbk-06__tbox:checked) {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --bar: #f2f4fa;
  --line: #e2e6f0;
  --ink: #11131a;
  --muted: #5b6373;
  --badge: #0550ae;
  --badge-bg: rgba(5,80,174,.10);
  --ring: #0550ae;
  --ok: #1a7f37;
  --err: #c0392b;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-fn2: #0f766e;
  background: radial-gradient(62rem 34rem at 50% -10%, #e9edff 0%, transparent 62%), var(--bg);
}

.cbk-06__theme {
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

.cbk-06[data-theme="dark"] .cbk-06__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-06:not([data-theme="light"]) .cbk-06__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-06__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-06[data-theme="dark"] .cbk-06__theme:hover,
.cbk-06:not([data-theme="light"]) .cbk-06__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-06__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-06__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-06__sun {
  display: none;
}

.cbk-06__theme[aria-pressed="true"] .cbk-06__sun {
  display: block;
}

.cbk-06__theme[aria-pressed="true"] .cbk-06__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-06__theme {
    transition: none;
  }

  .cbk-06__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const block = document.getElementById('cbk-06-block');
  if (!block) return;
  const btn = document.getElementById('cbk-06-copy');
  const status = document.getElementById('cbk-06-status');
  const code = block.querySelector('code');

  btn.addEventListener('click', async () => {
    const text = code.textContent;
    try {
      await navigator.clipboard.writeText(text);
      btn.dataset.state = 'copied';
      status.textContent = 'Code copied to clipboard';
    } catch {
      const ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed';
      ta.style.opacity = '0'; block.append(ta); ta.select();
      const ok = document.execCommand && document.execCommand('copy');
      ta.remove();
      btn.dataset.state = ok ? 'copied' : 'error';
      status.textContent = ok ? 'Code copied to clipboard' : 'Copy blocked — select the code and press Ctrl+C.';
    }
    setTimeout(() => { btn.dataset.state = ''; status.textContent = ''; }, 2200);
  });
})();
(()=>{const r=document.querySelector('.cbk-06');if(!r)return;const t=r.querySelector('.cbk-06__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
