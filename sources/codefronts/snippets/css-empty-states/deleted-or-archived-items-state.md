---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/deleted-or-archived-items-state/"
title: "Deleted or Archived Items State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "An empty trash that answers the only question users have here: how long do I have?"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Deleted or Archived Items State
Source: https://codefronts.com/snippets/css-empty-states/deleted-or-archived-items-state/

An empty trash that answers the only question users have here: how long do I have? The retention policy is on screen in the sidebar and in the copy, and the interactive control is a retention picker that rewrites both at once &mdash; 7, 30 or 90 days. The bin itself is drawn in CSS, with a lid that lifts once every six seconds.
## HTML
```html
<div class="est-15">
  <div class="est-15__shell">
    <aside class="est-15__side">
      <span class="est-15__logo">Slate Drive</span>
      <nav class="est-15__nav">
        <a class="est-15__nl" href="#est-15">My files</a>
        <a class="est-15__nl" href="#est-15">Shared</a>
        <a class="est-15__nl" href="#est-15">Recent</a>
        <a class="est-15__nl est-15__nl--on" href="#est-15" aria-current="page">Trash</a>
      </nav>
      <div class="est-15__meter">
        <span class="est-15__mtrack"><span class="est-15__mfill"></span></span>
        <span class="est-15__mtext">Trash is emptied 30 days after deletion</span>
      </div>
    </aside>

    <main class="est-15__main">
      <header class="est-15__top">
        <div class="est-15__crumbs"><span>Slate Drive</span><span aria-hidden="true">/</span><span class="est-15__crumbon">Trash</span></div>
        <div class="est-15__tacts">
          <button class="est-15__ghost" type="button" id="est-15-toggle" aria-expanded="false" aria-controls="est-15-ret">Retention</button>
          <button class="est-15__danger" type="button" disabled>Empty trash</button>
        </div>
      </header>

      <div class="est-15__cols" aria-hidden="true">
        <span>Name</span><span>Deleted</span><span>Owner</span><span>Size</span>
      </div>

      <div class="est-15__body" aria-live="polite">
        <div class="est-15__empty" id="est-15-empty">
          <span class="est-15__bin" aria-hidden="true">
            <span class="est-15__binlid"></span>
            <span class="est-15__binbody"></span>
          </span>
          <h1 class="est-15__h1">Trash is empty</h1>
          <p class="est-15__p">Nothing has been deleted in the last 30 days. Anything you remove will wait here before it goes for good.</p>
          <div class="est-15__acts">
            <button class="est-15__pri" type="button">Back to my files</button>
            <button class="est-15__ghost est-15__ghost--sm" type="button" id="est-15-toggle2">Change retention</button>
          </div>

          <fieldset class="est-15__ret" id="est-15-ret" hidden>
            <legend>Keep deleted files for</legend>
            <div class="est-15__retrow">
              <label class="est-15__opt"><input type="radio" name="est-15-days" value="7"><span>7 days</span></label>
              <label class="est-15__opt"><input type="radio" name="est-15-days" value="30" checked><span>30 days</span></label>
              <label class="est-15__opt"><input type="radio" name="est-15-days" value="90"><span>90 days</span></label>
            </div>
          </fieldset>
        </div>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-15 {
  --bg: #f7f7f6;
  --surface: #ffffff;
  --sunk: #efefed;
  --line: #e5e5e2;
  --line-2: #d3d3cf;
  --ink: #16171a;
  --muted: #5c5e62;
  --faint: #8b8d92;
  --accent: #37514a;
  --bad: #9c3f32;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-15 *,
.est-15 *::before,
.est-15 *::after {
  box-sizing: border-box;
}

.est-15 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-15 {
    --bg: oklch(0.974 0.002 120);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.955 0.003 120);
    --line: oklch(0.918 0.004 120);
    --line-2: oklch(0.862 0.005 120);
    --ink: oklch(0.18 0.008 260);
    --muted: oklch(0.47 0.009 260);
    --faint: oklch(0.625 0.01 260);
    --accent: oklch(0.4 0.045 165);
    --bad: oklch(0.47 0.12 30);
  }
}

.est-15__shell {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-columns: min(14.5rem,23vw) minmax(0,1fr);
}

.est-15__side {
  display: grid;
  grid-template-rows: auto minmax(0,1fr) auto;
  gap: 1.25rem;
  padding: 1.15rem .85rem;
  border-inline-end: 1px solid var(--line);
  background: var(--surface);
}

.est-15__logo {
  padding-inline: .4rem;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.025em;
}

.est-15__nav {
  display: grid;
  gap: .1rem;
  align-content: start;
}

.est-15__nl {
  padding: .45rem .6rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: .86rem;
  color: var(--muted);
  transition: color .16s, background .16s;
}

.est-15__nl:hover {
  color: var(--ink);
  background: var(--sunk);
}

.est-15__nl--on {
  color: var(--ink);
  background: var(--sunk);
  box-shadow: inset 0 0 0 1px var(--line);
}

.est-15__meter {
  display: grid;
  gap: .45rem;
  padding: .7rem .75rem;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--sunk);
}

.est-15__mtrack {
  block-size: .3rem;
  border-radius: 99px;
  background: var(--line-2);
  overflow: hidden;
}

.est-15__mfill {
  display: block;
  block-size: 100%;
  inline-size: 8%;
  border-radius: 99px;
  background: var(--accent);
}

.est-15__mtext {
  font-size: .72rem;
  line-height: 1.4;
  color: var(--faint);
}

.est-15__main {
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto auto minmax(0,1fr);
  align-content: start;
}

.est-15__top {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.25rem;
  align-items: center;
  justify-content: space-between;
  padding: 1rem clamp(1rem,3vw,2rem);
}

.est-15__crumbs {
  display: flex;
  gap: .4rem;
  font-size: .88rem;
  color: var(--faint);
}

.est-15__crumbon {
  color: var(--ink);
  font-weight: 600;
}

.est-15__tacts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.est-15__ghost {
  min-block-size: 2.55rem;
  padding: .6rem .95rem;
  font: inherit;
  font-size: .85rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 9px;
  transition: background .16s;
}

.est-15__ghost:hover {
  background: var(--sunk);
}

.est-15__ghost--sm {
  min-block-size: 2.4rem;
  padding: .5rem .85rem;
  font-size: .82rem;
}

.est-15__danger {
  min-block-size: 2.55rem;
  padding: .6rem .95rem;
  font: inherit;
  font-size: .85rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--bad);
  background: var(--surface);
  border: 1px solid color-mix(in oklab, var(--bad) 30%, var(--line-2));
  border-radius: 9px;
  transition: background .16s, color .16s;
}

.est-15__danger:hover {
  color: #fff;
  background: var(--bad);
  border-color: var(--bad);
}

.est-15__danger:disabled {
  opacity: .45;
  cursor: not-allowed;
  color: var(--faint);
  background: var(--surface);
  border-color: var(--line);
}

.est-15__pri {
  min-block-size: 2.7rem;
  padding: .65rem 1.05rem;
  font: inherit;
  font-size: .87rem;
  font-weight: 500;
  cursor: pointer;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 10px;
  box-shadow: 0 8px 18px -14px color-mix(in oklab, var(--accent) 80%, transparent);
  transition: translate .16s, background .16s;
}

.est-15__pri:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 86%, #000);
}

.est-15__cols {
  display: grid;
  grid-template-columns: minmax(0,2.4fr) minmax(0,1fr) minmax(0,1fr) minmax(0,.7fr);
  gap: 1rem;
  padding: .6rem clamp(1rem,3vw,2rem);
  border-block: 1px solid var(--line);
  background: var(--surface);
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .66rem;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-15__body {
  min-block-size: 0;
  padding: clamp(1rem,3vw,2rem);
}

.est-15__empty {
  inline-size: min(32rem,100%);
  margin: clamp(1rem,6vh,3.5rem) auto;
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .55rem;
  animation: est-15-in .55s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-15-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-15__bin {
  position: relative;
  inline-size: 4.5rem;
  block-size: 4.75rem;
  display: block;
  margin-block-end: .65rem;
}

.est-15__binlid {
  position: absolute;
  inset-block-start: 0;
  inset-inline: .35rem;
  block-size: .55rem;
  border-radius: 3px;
  background: var(--surface);
  border: 1px solid var(--line-2);
  transform-origin: 0% 100%;
  animation: est-15-lid 6s ease-in-out infinite;
}

.est-15__binlid::after {
  content: '';
  position: absolute;
  inset-block-start: -.42rem;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: 1.5rem;
  block-size: .42rem;
  border: 1px solid var(--line-2);
  border-block-end: 0;
  border-start-start-radius: 4px;
  border-start-end-radius: 4px;
  background: var(--surface);
}

@keyframes est-15-lid {
  0%,
    80%,
    100% {
    rotate: 0deg;
  }

  88% {
    rotate: -14deg;
  }
}

.est-15__binbody {
  position: absolute;
  inset-block-end: 0;
  inset-inline: .6rem;
  block-size: 3.65rem;
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 3px 3px 8px 8px;
  clip-path: polygon(0 0, 100% 0, 92% 100%, 8% 100%);
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--line) 60%, transparent);
}

.est-15__binbody::before,
.est-15__binbody::after {
  content: '';
  position: absolute;
  inset-block: .6rem .7rem;
  inline-size: 1px;
  background: var(--line);
}

.est-15__binbody::before {
  inset-inline-start: 35%;
}

.est-15__binbody::after {
  inset-inline-start: 65%;
}

.est-15__h1 {
  margin: 0;
  font-size: clamp(1.25rem,2.8vw,1.6rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.est-15__p {
  margin: 0;
  max-inline-size: 46ch;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-15__acts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .9rem;
}

.est-15__ret {
  margin: 1.35rem 0 0;
  padding: 1rem 1.1rem;
  inline-size: min(28rem,100%);
  display: grid;
  gap: .7rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 14px;
  text-align: start;
  animation: est-15-in .35s cubic-bezier(.2,.7,.3,1) both;
}

.est-15__ret legend {
  padding: 0;
  font-size: .78rem;
  font-weight: 500;
  color: var(--faint);
}

.est-15__retrow {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}

.est-15__opt {
  position: relative;
  display: inline-flex;
}

.est-15__opt input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
}

.est-15__opt span {
  min-block-size: 2.5rem;
  display: inline-flex;
  align-items: center;
  padding: .55rem .9rem;
  cursor: pointer;
  font-size: .85rem;
  color: var(--muted);
  background: var(--sunk);
  border: 1px solid var(--line);
  border-radius: 9px;
  transition: color .16s, background .16s, border-color .16s;
}

.est-15__opt span:hover {
  color: var(--ink);
}

.est-15__opt input:checked + span {
  color: #fff;
  background: var(--accent);
  border-color: var(--accent);
}

.est-15__opt input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-15__rows {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .35rem;
}

.est-15__row {
  display: grid;
  grid-template-columns: minmax(0,2.4fr) minmax(0,1fr) minmax(0,1fr) minmax(0,.7fr);
  gap: 1rem;
  align-items: center;
  padding: .75rem 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 11px;
  font-size: .86rem;
  animation: est-15-in .4s cubic-bezier(.2,.7,.3,1) both;
}

.est-15__rname {
  display: flex;
  align-items: center;
  gap: .6rem;
  min-inline-size: 0;
}

.est-15__rname i {
  inline-size: 1.7rem;
  block-size: 1.7rem;
  flex: none;
  border-radius: 6px;
  background: color-mix(in oklab, var(--accent) 10%, var(--surface));
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--accent) 18%, transparent);
}

.est-15__rname span {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.est-15__rmeta {
  font-size: .8rem;
  color: var(--faint);
}

.est-15__ghost:focus-visible,
.est-15__pri:focus-visible,
.est-15__danger:focus-visible,
.est-15__nl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 860px) {
  .est-15__shell {
    grid-template-columns: 1fr;
  }

  .est-15__side {
    grid-template-rows: auto;
    grid-template-columns: auto minmax(0,1fr);
    align-items: center;
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }

  .est-15__nav {
    display: none;
  }

  .est-15__meter {
    display: none;
  }

  .est-15__cols {
    display: none;
  }

  .est-15__row {
    grid-template-columns: 1fr;
    gap: .35rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-15 *,
    .est-15 *::before,
    .est-15 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-15__row,
    .est-15__binbody,
    .est-15__pri {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-15'); if(!root) return;
  var ret = root.querySelector('#est-15-ret'), toggle = root.querySelector('#est-15-toggle'),
      toggle2 = root.querySelector('#est-15-toggle2'), note = root.querySelector('.est-15__mtext'),
      copy = root.querySelector('.est-15__p'), fill = root.querySelector('.est-15__mfill');
  function open(){
    var next = ret.hidden;
    ret.hidden = !next;
    toggle.setAttribute('aria-expanded', String(next));
    if(next) ret.querySelector('input:checked').focus();
  }
  toggle.addEventListener('click', open);
  toggle2.addEventListener('click', open);
  ret.addEventListener('change', function(e){
    var d = e.target.value;
    note.textContent = 'Trash is emptied ' + d + ' days after deletion';
    copy.textContent = 'Nothing has been deleted in the last ' + d + ' days. Anything you remove will wait here for ' + d + ' days before it goes for good.';
    fill.style.inlineSize = (d === '7' ? '4%' : d === '30' ? '8%' : '17%');
  });
})();
```
