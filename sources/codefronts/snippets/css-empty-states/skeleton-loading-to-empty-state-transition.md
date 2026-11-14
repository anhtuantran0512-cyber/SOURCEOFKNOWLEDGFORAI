---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/skeleton-loading-to-empty-state-transition/"
title: "Skeleton Loading to Empty State Transition"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "The transition nobody tests: skeleton out, empty state in, without the page jumping."
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeleton Loading to Empty State Transition
Source: https://codefronts.com/snippets/css-empty-states/skeleton-loading-to-empty-state-transition/

The transition nobody tests: skeleton out, empty state in, without the page jumping. The skeleton reserves the exact block size the empty state will occupy &mdash; one min-block-size on the slot &mdash; so the swap costs zero layout shift, and the shimmer is a single moving background-position rather than an animated box.
## HTML
```html
<div class="est-16">
  <div class="est-16__wrap">
    <header class="est-16__head">
      <div class="est-16__idr">
        <span class="est-16__dot" id="est-16-dot" aria-hidden="true"></span>
        <span class="est-16__proj">payments-core</span>
        <span class="est-16__branch">main</span>
      </div>
      <button class="est-16__reload" type="button" id="est-16-reload">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M19 12a7 7 0 1 1-2.6-5.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M19 5v4h-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Refetch
      </button>
    </header>

    <section class="est-16__card">
      <div class="est-16__ctop">
        <span class="est-16__ctitle">Review queue</span>
        <span class="est-16__cstate" id="est-16-state">loading</span>
      </div>

      <div class="est-16__slot" id="est-16-slot">
        <div class="est-16__skel" id="est-16-skel">
          <div class="est-16__srow"><span class="est-16__sav"></span><span class="est-16__slines"><i data-w="62"></i><i data-w="38"></i></span><span class="est-16__spill"></span></div>
          <div class="est-16__srow"><span class="est-16__sav"></span><span class="est-16__slines"><i data-w="74"></i><i data-w="44"></i></span><span class="est-16__spill"></span></div>
          <div class="est-16__srow"><span class="est-16__sav"></span><span class="est-16__slines"><i data-w="56"></i><i data-w="33"></i></span><span class="est-16__spill"></span></div>
        </div>

        <div class="est-16__empty" id="est-16-empty" hidden>
          <span class="est-16__glyph" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="9" cy="7.5" r="2.6" stroke="currentColor" stroke-width="1.6"/><path d="M4 18c0-2.7 2.2-4.6 5-4.6 1.2 0 2.3.3 3.2 1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="m14.5 15.5 2.2 2.2 4-4.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <p class="est-16__eh">No reviews assigned to you</p>
          <p class="est-16__ep">Two teammates are on rotation this week. You will be paged here when something needs a second pair of eyes.</p>
          <div class="est-16__eacts">
            <button class="est-16__pri" type="button">Open the rotation</button>
            <button class="est-16__ghost" type="button">Watch this repository</button>
          </div>
        </div>
      </div>
    </section>

    <section class="est-16__card est-16__card--flat">
      <div class="est-16__ctop"><span class="est-16__ctitle">Checks</span><span class="est-16__cstate est-16__cstate--ok">passing</span></div>
      <ul class="est-16__checks">
        <li><span class="est-16__ctick" aria-hidden="true"></span>unit &mdash; 1m 42s</li>
        <li><span class="est-16__ctick" aria-hidden="true"></span>contract &mdash; 3m 07s</li>
        <li><span class="est-16__ctick" aria-hidden="true"></span>lint &mdash; 21s</li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-16 {
  --bg: #fafafb;
  --surface: #ffffff;
  --sunk: #f2f3f5;
  --line: #e5e7ea;
  --line-2: #d4d7dc;
  --ink: #14161a;
  --muted: #5a5f68;
  --faint: #8a8f98;
  --accent: #4b3fa8;
  --ok: #2c6b4f;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-16 *,
.est-16 *::before,
.est-16 *::after {
  box-sizing: border-box;
}

.est-16 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-16 {
    --bg: oklch(0.982 0.002 285);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.96 0.004 285);
    --line: oklch(0.918 0.005 285);
    --line-2: oklch(0.865 0.007 285);
    --ink: oklch(0.175 0.009 275);
    --muted: oklch(0.465 0.012 275);
    --faint: oklch(0.625 0.012 275);
    --accent: oklch(0.44 0.14 285);
    --ok: oklch(0.48 0.085 158);
  }
}

.est-16__wrap {
  inline-size: min(46rem,100%);
  justify-self: center;
  padding: clamp(1.5rem,5vw,3.5rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: 1rem;
  align-content: start;
}

.est-16__head {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.25rem;
  align-items: center;
  justify-content: space-between;
}

.est-16__idr {
  display: flex;
  align-items: center;
  gap: .55rem;
}

.est-16__dot {
  inline-size: .55rem;
  block-size: .55rem;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--accent) 16%, transparent);
  animation: est-16-blink 1.6s ease-in-out infinite;
}

.est-16__dot[data-idle] {
  background: var(--ok);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--ok) 16%, transparent);
  animation: none;
}

@keyframes est-16-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .35;
  }
}

.est-16__proj {
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.est-16__branch {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .7rem;
  color: var(--faint);
  padding: .15rem .4rem;
  border: 1px solid var(--line);
  border-radius: 5px;
}

.est-16__reload {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.5rem;
  padding: .55rem .9rem;
  font: inherit;
  font-size: .84rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 9px;
  transition: background .16s;
}

.est-16__reload svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.est-16__reload:hover {
  background: var(--sunk);
}

.est-16__reload[data-busy] svg {
  animation: est-16-spin .9s linear infinite;
}

@keyframes est-16-spin {
  to {
    rotate: 360deg;
  }
}

.est-16__card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(20,22,26,.04);
}

.est-16__ctop {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  padding: .8rem 1rem;
  border-block-end: 1px solid var(--line);
  background: var(--sunk);
}

.est-16__ctitle {
  font-size: .87rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.est-16__cstate {
  padding: .18rem .45rem;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .66rem;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 9%, var(--surface));
  border: 1px solid color-mix(in oklab, var(--accent) 24%, transparent);
  border-radius: 5px;
}

.est-16__cstate--ok {
  color: var(--ok);
  background: color-mix(in oklab, var(--ok) 9%, var(--surface));
  border-color: color-mix(in oklab, var(--ok) 24%, transparent);
}

.est-16__slot {
  min-block-size: 17.5rem;
  display: grid;
  align-content: center;
}

.est-16__skel {
  display: grid;
  gap: .15rem;
  padding: .75rem;
}

.est-16__srow {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .85rem;
  align-items: center;
  padding: .85rem .75rem;
}

.est-16__sav {
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 50%;
  background: var(--sunk);
  position: relative;
  overflow: hidden;
}

.est-16__slines {
  display: grid;
  gap: .45rem;
  min-inline-size: 0;
}

.est-16__slines i {
  block-size: .65rem;
  border-radius: 4px;
  background: var(--sunk);
  inline-size: calc(var(--w,60) * 1%);
}

.est-16__slines i[data-w="62"] {
  --w: 62;
}

.est-16__slines i[data-w="38"] {
  --w: 38;
}

.est-16__slines i[data-w="74"] {
  --w: 74;
}

.est-16__slines i[data-w="44"] {
  --w: 44;
}

.est-16__slines i[data-w="56"] {
  --w: 56;
}

.est-16__slines i[data-w="33"] {
  --w: 33;
}

.est-16__spill {
  inline-size: 4rem;
  block-size: 1.5rem;
  border-radius: 6px;
  background: var(--sunk);
}

.est-16__sav,
.est-16__slines i,
.est-16__spill {
  background-image: linear-gradient(90deg, transparent, color-mix(in oklab, var(--line-2) 55%, transparent), transparent);
  background-size: 220% 100%;
  background-repeat: no-repeat;
  animation: est-16-shim 1.5s linear infinite;
}

@keyframes est-16-shim {
  0% {
    background-position: -120% 0;
  }

  100% {
    background-position: 220% 0;
  }
}

.est-16__empty {
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .45rem;
  padding: clamp(1.75rem,5vh,2.75rem) 1.5rem;
  animation: est-16-in .45s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-16-in {
  from {
    opacity: 0;
    translate: 0 6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-16__glyph {
  inline-size: 3.4rem;
  block-size: 3.4rem;
  display: grid;
  place-items: center;
  margin-block-end: .5rem;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 8%, var(--surface));
  border-radius: 14px;
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--accent) 18%, transparent);
}

.est-16__glyph svg {
  inline-size: 1.45rem;
  block-size: 1.45rem;
}

.est-16__eh {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -.022em;
}

.est-16__ep {
  margin: 0;
  max-inline-size: 44ch;
  font-size: .88rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.est-16__eacts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .85rem;
}

.est-16__pri {
  min-block-size: 2.7rem;
  padding: .65rem 1.05rem;
  font: inherit;
  font-size: .86rem;
  font-weight: 500;
  cursor: pointer;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 10px;
  box-shadow: 0 8px 18px -14px color-mix(in oklab, var(--accent) 80%, transparent);
  transition: translate .16s, background .16s;
}

.est-16__pri:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 88%, #000);
}

.est-16__ghost {
  min-block-size: 2.7rem;
  padding: .65rem 1rem;
  font: inherit;
  font-size: .86rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 10px;
  transition: background .16s;
}

.est-16__ghost:hover {
  background: var(--sunk);
}

.est-16__card--flat {
  box-shadow: none;
}

.est-16__checks {
  margin: 0;
  padding: .6rem .75rem .85rem;
  list-style: none;
  display: grid;
  gap: .1rem;
}

.est-16__checks li {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .5rem .6rem;
  border-radius: 8px;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .78rem;
  color: var(--muted);
}

.est-16__checks li:hover {
  background: var(--sunk);
}

.est-16__ctick {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  flex: none;
  border-radius: 50%;
  background: color-mix(in oklab, var(--ok) 15%, var(--surface));
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--ok) 40%, transparent);
  position: relative;
}

.est-16__ctick::after {
  content: '';
  position: absolute;
  inset-block-start: .3rem;
  inset-inline-start: .26rem;
  inline-size: .34rem;
  block-size: .16rem;
  border-inline-start: 1.5px solid var(--ok);
  border-block-end: 1.5px solid var(--ok);
  rotate: -45deg;
}

.est-16__pri:focus-visible,
.est-16__ghost:focus-visible,
.est-16__reload:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .est-16 *,
    .est-16 *::before,
    .est-16 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-16__card,
    .est-16__glyph,
    .est-16__pri {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-16'); if(!root) return;
  var skel = root.querySelector('#est-16-skel'), empty = root.querySelector('#est-16-empty'),
      state = root.querySelector('#est-16-state'), dot = root.querySelector('#est-16-dot'),
      reload = root.querySelector('#est-16-reload');
  function settle(){
    skel.hidden = true; empty.hidden = false;
    state.textContent = 'no items'; state.className = 'est-16__cstate est-16__cstate--ok';
    dot.setAttribute('data-idle',''); reload.removeAttribute('data-busy');
  }
  function fetchAgain(){
    skel.hidden = false; empty.hidden = true;
    state.textContent = 'loading'; state.className = 'est-16__cstate';
    dot.removeAttribute('data-idle'); reload.setAttribute('data-busy','');
    setTimeout(settle, 1500);
  }
  reload.addEventListener('click', fetchAgain);
  setTimeout(settle, 1700);
})();
```
