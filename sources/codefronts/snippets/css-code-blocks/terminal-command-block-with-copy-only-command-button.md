---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/terminal-command-block-with-copy-only-command-button/"
title: "Terminal Command Block with Copy Only Command Button"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "The install block from every good docs site: a terminal shell with a muted $ prompt, npm / pnpm / yarn / bun tabs, and a copy button that copies only the…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal Command Block with Copy Only Command Button
Source: https://codefronts.com/snippets/css-code-blocks/terminal-command-block-with-copy-only-command-button/

The install block from every good docs site: a terminal shell with a muted $ prompt, npm / pnpm / yarn / bun tabs, and a copy button that copies only the command — never the prompt character. That one detail is the difference between a reader pasting pnpm add framer-motion and pasting $ pnpm add framer-motion straight into a syntax error.
## HTML
```html
<div class="cbk-05">
  <button class="cbk-05__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-05__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-05__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-05__stage">
    <input class="cbk-05__tbox" id="cbk-05-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-05__tbtn" for="cbk-05-tbox" title="Toggle light and dark theme">
      <svg class="cbk-05__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-05__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <div class="cbk-05__term" id="cbk-05-term">
      <div class="cbk-05__head">
        <span class="cbk-05__ico" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="3" y="4.5" width="18" height="15" rx="2.5" stroke="currentColor" stroke-width="1.6"/><path d="m7.5 10 2.4 2.4-2.4 2.4M12.5 14.8h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <span class="cbk-05__title">Terminal</span>
        <div class="cbk-05__tabs" role="tablist" aria-label="Package manager">
          <button class="cbk-05__tab" type="button" role="tab" id="cbk-05-t0" aria-controls="cbk-05-p0" aria-selected="true" tabindex="0">npm</button>
          <button class="cbk-05__tab" type="button" role="tab" id="cbk-05-t1" aria-controls="cbk-05-p1" aria-selected="false" tabindex="-1">pnpm</button>
          <button class="cbk-05__tab" type="button" role="tab" id="cbk-05-t2" aria-controls="cbk-05-p2" aria-selected="false" tabindex="-1">yarn</button>
          <button class="cbk-05__tab" type="button" role="tab" id="cbk-05-t3" aria-controls="cbk-05-p3" aria-selected="false" tabindex="-1">bun</button>
        </div>
      </div>

      <div class="cbk-05__body">
        <section class="cbk-05__panel" role="tabpanel" id="cbk-05-p0" aria-labelledby="cbk-05-t0">
<pre class="cbk-05__pre"><code class="language-shell"><span class="cbk-05__prompt" aria-hidden="true">$</span><span class="cbk-05__cmd">npm install @tanstack/react-query framer-motion</span></code></pre>
        </section>
        <section class="cbk-05__panel" role="tabpanel" id="cbk-05-p1" aria-labelledby="cbk-05-t1" hidden>
<pre class="cbk-05__pre"><code class="language-shell"><span class="cbk-05__prompt" aria-hidden="true">$</span><span class="cbk-05__cmd">pnpm add @tanstack/react-query framer-motion</span></code></pre>
        </section>
        <section class="cbk-05__panel" role="tabpanel" id="cbk-05-p2" aria-labelledby="cbk-05-t2" hidden>
<pre class="cbk-05__pre"><code class="language-shell"><span class="cbk-05__prompt" aria-hidden="true">$</span><span class="cbk-05__cmd">yarn add @tanstack/react-query framer-motion</span></code></pre>
        </section>
        <section class="cbk-05__panel" role="tabpanel" id="cbk-05-p3" aria-labelledby="cbk-05-t3" hidden>
<pre class="cbk-05__pre"><code class="language-shell"><span class="cbk-05__prompt" aria-hidden="true">$</span><span class="cbk-05__cmd">bun add @tanstack/react-query framer-motion</span></code></pre>
        </section>

        <button class="cbk-05__copy" type="button" id="cbk-05-copy" aria-label="Copy command to clipboard" data-state="">
          <svg class="cbk-05__c-ico cbk-05__c-ico--copy" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M15 6.5A2.5 2.5 0 0 0 12.5 4H6.5A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <svg class="cbk-05__c-ico cbk-05__c-ico--ok" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m5 12.5 4.4 4.4L19 7.3" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <svg class="cbk-05__c-ico cbk-05__c-ico--err" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 7.5v6m0 3h.01" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.6"/></svg>
        </button>
      </div>

      <p class="cbk-05__status" id="cbk-05-status" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cbk-05 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #06070b;
  --surface: #0d1016;
  --head: #111520;
  --line: #1f2431;
  --ink: #e8ebf2;
  --muted: #8d95a6;
  --acc: #4ade80;
  --err: #f87171;
  background: radial-gradient(58rem 32rem at 50% -8%, #121a20 0%, transparent 64%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-05 {
    --bg: oklch(11% .01 250);
    --surface: oklch(16% .013 250);
    --head: oklch(19% .015 250);
    --line: oklch(26% .017 250);
    --ink: oklch(93% .008 250);
    --muted: oklch(69% .02 250);
    --acc: oklch(84% .17 150);
    --err: oklch(72% .17 25);
  }
}

.cbk-05 *,
.cbk-05 *::before,
.cbk-05 *::after {
  box-sizing: border-box;
}

.cbk-05__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-05__term {
  inline-size: min(52rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.05), 0 24px 60px -30px rgba(0,0,0,.9);
  container-type: inline-size;
}

.cbk-05__head {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .55rem .75rem;
  background: var(--head);
  border-block-end: 1px solid var(--line);
}

.cbk-05__ico {
  display: grid;
  place-items: center;
  color: var(--acc);
}

.cbk-05__ico svg {
  inline-size: 17px;
  block-size: 17px;
}

.cbk-05__title {
  color: var(--muted);
  font-size: .78125rem;
  letter-spacing: .02em;
}

.cbk-05__tabs {
  display: flex;
  gap: .15rem;
  margin-inline-start: auto;
}

.cbk-05__tab {
  position: relative;
  min-block-size: 34px;
  padding: .35rem .6rem;
  border: 0;
  border-radius: 7px;
  background: none;
  color: var(--muted);
  font-family: var(--mono);
  font-size: .78125rem;
  cursor: pointer;
  transition: color .16s, background-color .16s;
}

.cbk-05__tab:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.cbk-05__tab[aria-selected="true"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--acc) 14%,transparent);
}

.cbk-05__tab[aria-selected="true"]::after {
  content: "";
  position: absolute;
  inset-inline: .55rem;
  inset-block-end: -.55rem;
  block-size: 2px;
  background: var(--acc);
  border-radius: 2px;
}

.cbk-05__body {
  position: relative;
  display: flex;
  align-items: center;
  gap: .75rem;
  padding-inline-end: 3.6rem;
}

.cbk-05__panel {
  flex: 1;
  min-inline-size: 0;
}

.cbk-05__panel[hidden] {
  display: none;
}

.cbk-05__pre {
  margin: 0;
  padding: 1.15rem 1.15rem 1.2rem;
  overflow-x: auto;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.5rem + .5cqi,1rem);
  line-height: 1.6;
  white-space: pre;
  font-variant-ligatures: none;
}

.cbk-05__prompt {
  color: var(--acc);
  opacity: .85;
  user-select: none;
  margin-inline-end: .75ch;
}

.cbk-05__cmd {
  color: var(--ink);
}

.cbk-05__copy {
  position: absolute;
  inset-inline-end: .6rem;
  inset-block-start: 50%;
  translate: 0 -50%;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: color-mix(in oklab,var(--ink) 5%,transparent);
  color: var(--muted);
  cursor: pointer;
  transition: color .18s, background-color .18s, border-color .18s, scale .12s;
}

.cbk-05__copy:hover {
  color: var(--ink);
  border-color: color-mix(in oklab,var(--ink) 26%,transparent);
}

.cbk-05__copy:active {
  scale: .94;
}

.cbk-05__c-ico {
  position: absolute;
  inline-size: 18px;
  block-size: 18px;
  opacity: 0;
  scale: .6;
  transition: opacity .18s, scale .18s cubic-bezier(.2,.9,.25,1);
}

.cbk-05__copy[data-state=""] .cbk-05__c-ico--copy,
.cbk-05__copy:not([data-state]) .cbk-05__c-ico--copy {
  opacity: 1;
  scale: 1;
}

.cbk-05__copy[data-state="copied"] {
  color: var(--acc);
  border-color: color-mix(in oklab,var(--acc) 45%,transparent);
  background: color-mix(in oklab,var(--acc) 14%,transparent);
}

.cbk-05__copy[data-state="copied"] .cbk-05__c-ico--ok {
  opacity: 1;
  scale: 1;
}

.cbk-05__copy[data-state="error"] {
  color: var(--err);
  border-color: color-mix(in oklab,var(--err) 45%,transparent);
}

.cbk-05__copy[data-state="error"] .cbk-05__c-ico--err {
  opacity: 1;
  scale: 1;
}

.cbk-05__status {
  margin: 0;
  padding: 0 1.15rem;
  max-block-size: 0;
  overflow: hidden;
  color: var(--acc);
  font-size: .75rem;
  transition: max-block-size .2s, padding-block .2s;
}

.cbk-05__status:not(:empty) {
  max-block-size: 2.2rem;
  padding-block: 0 .7rem;
}

.cbk-05 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cbk-05[data-theme="light"] {
  --bg: #f5f7f9;
  --surface: #ffffff;
  --head: #eff2f5;
  --line: #e0e5ea;
  --ink: #10141a;
  --muted: #5a6270;
  --acc: #0d8a4b;
  --err: #c0392b;
  background: radial-gradient(58rem 32rem at 50% -8%, #e6f4ec 0%, transparent 64%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-05:not([data-theme="dark"]) {
    --bg: #f5f7f9;
    --surface: #ffffff;
    --head: #eff2f5;
    --line: #e0e5ea;
    --ink: #10141a;
    --muted: #5a6270;
    --acc: #0d8a4b;
    --err: #c0392b;
    background: radial-gradient(58rem 32rem at 50% -8%, #e6f4ec 0%, transparent 64%), var(--bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-05 *,
    .cbk-05 *::before,
    .cbk-05 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cbk-05__term {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-05__tab[aria-selected="true"] {
    background: Highlight;
    color: HighlightText;
  }

  .cbk-05__copy {
    border: 1px solid CanvasText;
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-05__stage {
  position: relative;
}

.cbk-05__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-05__tbtn {
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
  .cbk-05__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-05__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-05__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-05__tbox:focus-visible + .cbk-05__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-05__tmoon {
  display: none;
}

.cbk-05:has(.cbk-05__tbox:checked) .cbk-05__tsun {
  display: none;
}

.cbk-05:has(.cbk-05__tbox:checked) .cbk-05__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-05__tbtn {
    transition: none;
  }

  .cbk-05__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-05__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-05:has(.cbk-05__tbox:checked) {
  --bg: #f5f7f9;
  --surface: #ffffff;
  --head: #eff2f5;
  --line: #e0e5ea;
  --ink: #10141a;
  --muted: #5a6270;
  --acc: #0d8a4b;
  --err: #c0392b;
  background: radial-gradient(58rem 32rem at 50% -8%, #e6f4ec 0%, transparent 64%), var(--bg);
}

.cbk-05__theme {
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

.cbk-05[data-theme="dark"] .cbk-05__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-05:not([data-theme="light"]) .cbk-05__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-05__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-05[data-theme="dark"] .cbk-05__theme:hover,
.cbk-05:not([data-theme="light"]) .cbk-05__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-05__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-05__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-05__sun {
  display: none;
}

.cbk-05__theme[aria-pressed="true"] .cbk-05__sun {
  display: block;
}

.cbk-05__theme[aria-pressed="true"] .cbk-05__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-05__theme {
    transition: none;
  }

  .cbk-05__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const term = document.getElementById('cbk-05-term');
  if (!term) return;
  const tabs = [...term.querySelectorAll('[role="tab"]')];
  const panels = tabs.map((t) => document.getElementById(t.getAttribute('aria-controls')));
  const btn = document.getElementById('cbk-05-copy');
  const status = document.getElementById('cbk-05-status');
  let live = 0;

  const select = (i, focus) => {
    tabs.forEach((t, n) => {
      t.setAttribute('aria-selected', String(n === i));
      t.tabIndex = n === i ? 0 : -1;
      panels[n].hidden = n !== i;
    });
    live = i;
    if (focus) tabs[i].focus();
  };
  tabs.forEach((t, i) => t.addEventListener('click', () => select(i, false)));
  term.querySelector('[role="tablist"]').addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    const map = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 };
    if (i < 0 || !(e.key in map)) return;
    e.preventDefault();
    select((map[e.key] + tabs.length) % tabs.length, true);
  });

  btn.addEventListener('click', async () => {
    const text = panels[live].querySelector('.cbk-05__cmd').textContent.trim();
    try {
      await navigator.clipboard.writeText(text);
      btn.dataset.state = 'copied';
      status.textContent = 'Copied: ' + text;
    } catch {
      btn.dataset.state = 'error';
      status.textContent = 'Clipboard blocked — select the command and press Ctrl+C.';
    }
    setTimeout(() => { btn.dataset.state = ''; status.textContent = ''; }, 2200);
  });
})();
(()=>{const r=document.querySelector('.cbk-05');if(!r)return;const t=r.querySelector('.cbk-05__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
