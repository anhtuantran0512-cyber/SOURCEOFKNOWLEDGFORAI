---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/floating-card/"
title: "Floating Card CSS Search Bar (Modal Style)"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Search-as-overlay: click the header field and a raised card floats above a dimmed, blurred page with a large input and recent result cards."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Card CSS Search Bar (Modal Style)
Source: https://codefronts.com/components/css-search-boxes/floating-card/

Search-as-overlay: click the header field and a raised card floats above a dimmed, blurred page with a large input and recent result cards. A native <dialog> handles focus trapping, Escape and the backdrop — the pattern behind Notion, Vercel and most editorial sites.
## HTML
```html
<div class="sb-35">
  <button class="sb-35__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-35__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-35__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-35__stage">
    <div class="sb-35__page">
      <header class="sb-35__header">
        <span class="sb-35__brand"><span class="sb-35__mark" aria-hidden="true"></span>Atlas</span>
        <button class="sb-35__trigger" id="sb-35-open" type="button" aria-haspopup="dialog" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.3" stroke="currentColor" stroke-width="1.8"/><path d="m15.9 15.9 4.3 4.3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <span>Search Atlas</span>
        </button>
      </header>
      <div class="sb-35__body" aria-hidden="true">
        <span class="sb-35__sk sb-35__sk--wide"></span>
        <span class="sb-35__sk"></span>
        <span class="sb-35__sk sb-35__sk--short"></span>
      </div>
    </div>

    <dialog class="sb-35__modal" id="sb-35-modal" aria-label="Search Atlas">
      <div class="sb-35__field" role="search">
        <svg class="sb-35__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <label class="sb-35__vh" for="sb-35-input">Search Atlas</label>
        <input class="sb-35__input" id="sb-35-input" type="search" placeholder="Search articles, guides and people&hellip;" autocomplete="off">
        <button class="sb-35__close" id="sb-35-close" type="button" aria-label="Close search">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </button>
      </div>
      <p class="sb-35__h">Recently viewed</p>
      <ul class="sb-35__grid">
        <li class="sb-35__card"><span class="sb-35__tag">Guide</span>Designing search that feels instant<span class="sb-35__meta">8 min read</span></li>
        <li class="sb-35__card"><span class="sb-35__tag">Doc</span>Q3 revenue forecast<span class="sb-35__meta">Updated 2h ago</span></li>
        <li class="sb-35__card"><span class="sb-35__tag">Person</span>Priya Sharma<span class="sb-35__meta">Product lead</span></li>
        <li class="sb-35__card"><span class="sb-35__tag">Guide</span>Onboarding checklist<span class="sb-35__meta">12 steps</span></li>
      </ul>
    </dialog>
  </div>
</div>
```
## CSS
```css
.sb-35 {
  --bg: #f2f3f7;
  --card: #ffffff;
  --ink: #131722;
  --muted: #6a7180;
  --line: #e4e7ee;
  --acc: #2c5cff;
  --wash: rgba(44,92,255,.10);
  --ring: #2c5cff;
  --shadow: rgba(19,23,34,.2);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-35 *,
.sb-35 *::before,
.sb-35 *::after {
  box-sizing: border-box;
}

.sb-35__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-35__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-35__page {
  inline-size: min(46rem,100%);
  padding: 1rem 1.1rem 2.4rem;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--card);
  box-shadow: 0 24px 50px -34px var(--shadow);
}

.sb-35__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.sb-35__brand {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  font: 700 1rem/1 inherit;
  letter-spacing: -.02em;
}

.sb-35__mark {
  inline-size: 20px;
  block-size: 20px;
  border-radius: 6px;
  background: conic-gradient(from 200deg,#2c5cff,#7c3aed 45%,#06b6d4 80%,#2c5cff);
}

.sb-35__trigger {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-block-size: 44px;
  padding-inline: .9rem;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: #fafbfd;
  color: var(--muted);
  cursor: pointer;
  font: 500 .9rem/1 inherit;
  transition: border-color .18s, color .18s, background .18s;
}

.sb-35__trigger:hover {
  border-color: var(--acc);
  color: var(--ink);
  background: var(--card);
}

.sb-35__trigger svg {
  inline-size: 17px;
  block-size: 17px;
}

.sb-35__body {
  display: grid;
  gap: .7rem;
  margin-block-start: 1.6rem;
}

.sb-35__sk {
  block-size: .85rem;
  border-radius: 6px;
  background: #eef0f5;
  inline-size: 78%;
}

.sb-35__sk--wide {
  inline-size: 100%;
  block-size: 1.6rem;
}

.sb-35__sk--short {
  inline-size: 52%;
}

.sb-35__modal {
  inline-size: min(42rem,92vw);
  max-block-size: min(34rem,84svh);
  margin-block-start: 10vh;
  padding: 0;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: var(--card);
  color: var(--ink);
  box-shadow: 0 2px 4px rgba(19,23,34,.08), 0 12px 24px -8px rgba(19,23,34,.14), 0 40px 80px -24px var(--shadow), inset 0 1px 0 rgba(255,255,255,.7);
  flex-direction: column;
}

.sb-35__modal[open] {
  display: flex;
}

.sb-35__modal::backdrop {
  background: rgba(10,12,20,.5);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

@supports (transition-behavior: allow-discrete) {
  .sb-35__modal {
    opacity: 0;
    translate: 0 12px;
    scale: .98;
    transition: opacity .24s cubic-bezier(.2,.9,.25,1), translate .24s cubic-bezier(.2,.9,.25,1), scale .24s, overlay .24s allow-discrete, display .24s allow-discrete;
  }

  .sb-35__modal[open] {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }

  @starting-style {
    .sb-35__modal[open] {
      opacity: 0;
      translate: 0 12px;
      scale: .98;
    }
  }
}

.sb-35__field {
  display: flex;
  align-items: center;
  gap: .8rem;
  padding: 1rem 1rem 1rem 1.25rem;
  border-block-end: 1px solid var(--line);
}

.sb-35__ico {
  inline-size: 21px;
  block-size: 21px;
  flex: none;
  color: var(--muted);
}

.sb-35__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 1.05rem/1.3 inherit;
}

.sb-35__input::placeholder {
  color: var(--muted);
}

.sb-35__input:focus {
  outline: none;
}

.sb-35__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-35__close {
  display: grid;
  place-items: center;
  inline-size: 36px;
  block-size: 36px;
  flex: none;
  border: 0;
  border-radius: 10px;
  background: #f2f4f8;
  color: var(--muted);
  cursor: pointer;
  transition: background .16s, color .16s;
}

.sb-35__close:hover {
  background: #e7eaf1;
  color: var(--ink);
}

.sb-35__close svg {
  inline-size: 15px;
  block-size: 15px;
}

.sb-35__h {
  margin: 1rem 1.25rem .5rem;
  color: var(--muted);
  font: 600 .68rem/1 inherit;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.sb-35__grid {
  list-style: none;
  margin: 0;
  padding: 0 1rem 1.1rem;
  display: grid;
  gap: .6rem;
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
  overflow: auto;
  overscroll-behavior: contain;
}

.sb-35__card {
  display: flex;
  flex-direction: column;
  gap: .3rem;
  padding: .85rem .9rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: #fbfcfe;
  cursor: pointer;
  font: 600 .92rem/1.3 inherit;
  text-wrap: pretty;
  transition: border-color .16s, translate .16s, background .16s;
}

.sb-35__card:hover {
  border-color: var(--acc);
  background: var(--card);
  translate: 0 -1px;
}

.sb-35__tag {
  align-self: start;
  padding: .16rem .4rem;
  border-radius: 5px;
  background: var(--wash);
  color: var(--acc);
  font: 600 .66rem/1 inherit;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.sb-35__meta {
  color: var(--muted);
  font: 400 .78rem/1 inherit;
}

.sb-35 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-35__input:focus-visible {
  outline: none;
}

.sb-35[data-theme="dark"] {
  --bg: #0a0c12;
  --card: #141821;
  --ink: #e9ecf4;
  --muted: #878e9e;
  --line: #232936;
  --acc: #7c9cff;
  --wash: rgba(124,156,255,.14);
  --ring: #7c9cff;
  --shadow: rgba(0,0,0,.8);
}

.sb-35[data-theme="dark"] .sb-35__trigger,
.sb-35[data-theme="dark"] .sb-35__card {
  background: #101520;
}

.sb-35[data-theme="dark"] .sb-35__sk {
  background: #1b2230;
}

.sb-35[data-theme="dark"] .sb-35__close {
  background: #1b2230;
}

.sb-35[data-theme="dark"] .sb-35__modal {
  box-shadow: 0 40px 80px -24px #000, inset 0 1px 0 rgba(255,255,255,.05);
}

@media (prefers-color-scheme: dark) {
  .sb-35:not([data-theme="light"]) {
    --bg: #0a0c12;
    --card: #141821;
    --ink: #e9ecf4;
    --muted: #878e9e;
    --line: #232936;
    --acc: #7c9cff;
    --wash: rgba(124,156,255,.14);
    --ring: #7c9cff;
    --shadow: rgba(0,0,0,.8);
  }

  .sb-35:not([data-theme="light"]) .sb-35__trigger,
    .sb-35:not([data-theme="light"]) .sb-35__card {
    background: #101520;
  }

  .sb-35:not([data-theme="light"]) .sb-35__sk {
    background: #1b2230;
  }

  .sb-35:not([data-theme="light"]) .sb-35__close {
    background: #1b2230;
  }

  .sb-35:not([data-theme="light"]) .sb-35__modal {
    box-shadow: 0 40px 80px -24px #000, inset 0 1px 0 rgba(255,255,255,.05);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-35 *,
    .sb-35 *::before,
    .sb-35 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-35__modal,
    .sb-35__page,
    .sb-35__trigger,
    .sb-35__card {
    border: 1px solid CanvasText;
  }
}

.sb-35__theme {
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

.sb-35[data-theme="dark"] .sb-35__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-35:not([data-theme="light"]) .sb-35__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-35__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-35[data-theme="dark"] .sb-35__theme:hover,
.sb-35:not([data-theme="light"]) .sb-35__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-35__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-35__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-35__sun {
  display: none;
}

.sb-35__theme[aria-pressed="true"] .sb-35__sun {
  display: block;
}

.sb-35__theme[aria-pressed="true"] .sb-35__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-35__theme {
    transition: none;
  }

  .sb-35__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-35');
  if (!root) return;
  const dlg = root.querySelector('#sb-35-modal');
  const trigger = root.querySelector('#sb-35-open');
  const input = root.querySelector('#sb-35-input');

  const open = () => { dlg.showModal(); trigger.setAttribute('aria-expanded', 'true'); input.focus(); };
  trigger.addEventListener('click', open);
  root.querySelector('#sb-35-close').addEventListener('click', () => dlg.close());
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });   /* backdrop click */
  dlg.addEventListener('close', () => { trigger.setAttribute('aria-expanded', 'false'); trigger.focus(); });
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); dlg.open ? dlg.close() : open(); }
  });
})();
(()=>{const r=document.querySelector('.sb-35');if(!r)return;const t=r.querySelector('.sb-35__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
