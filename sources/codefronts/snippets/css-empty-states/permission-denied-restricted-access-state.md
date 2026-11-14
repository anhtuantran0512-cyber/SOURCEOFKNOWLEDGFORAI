---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/permission-denied-restricted-access-state/"
title: "Permission Denied / Restricted Access State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "A 403 that shows the door it is refusing: the document renders behind a blur and a radial scrim, so the user can see the file exists without reading a word…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Permission Denied / Restricted Access State
Source: https://codefronts.com/snippets/css-empty-states/permission-denied-restricted-access-state/

A 403 that shows the door it is refusing: the document renders behind a blur and a radial scrim, so the user can see the file exists without reading a word of it, and the gate on top names the owners who can approve access. Requesting access swaps the buttons for a confirmation and rewrites the explanation &mdash; the screen resolves rather than repeating itself.
## HTML
```html
<div class="est-13">
  <div class="est-13__doc" aria-hidden="true">
    <div class="est-13__dtop">
      <span class="est-13__dbrand">Vellum</span>
      <span class="est-13__dpath">Legal / Vendor agreements / Northline MSA</span>
      <span class="est-13__dava"></span>
    </div>
    <div class="est-13__dpage">
      <span class="est-13__dh"></span>
      <span class="est-13__dl" data-w="92"></span>
      <span class="est-13__dl" data-w="84"></span>
      <span class="est-13__dl" data-w="96"></span>
      <span class="est-13__dl" data-w="61"></span>
      <span class="est-13__dh est-13__dh--sm"></span>
      <span class="est-13__dl" data-w="88"></span>
      <span class="est-13__dl" data-w="79"></span>
      <span class="est-13__dl" data-w="93"></span>
      <span class="est-13__dl" data-w="48"></span>
    </div>
  </div>

  <div class="est-13__scrim"></div>

  <section class="est-13__gate" role="region" aria-labelledby="est-13-h">
    <span class="est-13__lock" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="5" y="10.5" width="14" height="9.5" rx="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="15.2" r="1.15" fill="currentColor"/></svg>
    </span>
    <p class="est-13__code">403</p>
    <h1 class="est-13__h1" id="est-13-h">This document is restricted</h1>
    <p class="est-13__p" id="est-13-p">Northline MSA is limited to the legal group. Your account can see the file exists, but not its contents.</p>

    <div class="est-13__acts" id="est-13-acts">
      <button class="est-13__pri" type="button" id="est-13-req">Request access</button>
      <button class="est-13__ghost" type="button">Ask in the legal channel</button>
    </div>

    <div class="est-13__pending" id="est-13-pending" hidden>
      <span class="est-13__ptick" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="m6 12.5 4 4 8-9" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <span class="est-13__ptext">Request sent to the two document owners</span>
    </div>

    <dl class="est-13__owners">
      <div><dt>Owner</dt><dd>Priya Raman</dd></div>
      <div><dt>Owner</dt><dd>Marc Delacroix</dd></div>
      <div><dt>Group</dt><dd>legal-core</dd></div>
    </dl>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-13 {
  --bg: #eff0f2;
  --surface: #ffffff;
  --sunk: #e7e8ec;
  --line: #dfe1e5;
  --line-2: #cbced4;
  --ink: #15161a;
  --muted: #585c65;
  --faint: #888c95;
  --accent: #2f3a56;
  --ok: #2d6b4e;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  box-sizing: border-box;
  overflow: hidden;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-13 *,
.est-13 *::before,
.est-13 *::after {
  box-sizing: border-box;
}

.est-13 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-13 {
    --bg: oklch(0.945 0.004 265);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.925 0.005 265);
    --line: oklch(0.902 0.006 265);
    --line-2: oklch(0.845 0.008 265);
    --ink: oklch(0.175 0.009 265);
    --muted: oklch(0.465 0.012 265);
    --faint: oklch(0.62 0.012 265);
    --accent: oklch(0.33 0.055 265);
    --ok: oklch(0.48 0.085 158);
  }
}

.est-13__doc {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  filter: blur(6px) saturate(.85);
  transform: scale(1.02);
  pointer-events: none;
}

.est-13__dtop {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 1rem clamp(1rem,4vw,3rem);
  background: var(--surface);
  border-block-end: 1px solid var(--line);
}

.est-13__dbrand {
  font-size: .95rem;
  font-weight: 600;
}

.est-13__dpath {
  font-size: .82rem;
  color: var(--faint);
}

.est-13__dava {
  margin-inline-start: auto;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  border-radius: 50%;
  background: var(--sunk);
}

.est-13__dpage {
  inline-size: min(46rem,90%);
  justify-self: center;
  margin-block: clamp(1.5rem,5vh,3rem);
  display: grid;
  gap: .85rem;
  align-content: start;
  padding: clamp(1.75rem,4vw,3rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 6px;
  box-shadow: 0 30px 60px -50px rgba(20,22,26,.6);
}

.est-13__dh {
  block-size: 1.5rem;
  inline-size: 52%;
  border-radius: 4px;
  background: var(--sunk);
}

.est-13__dh--sm {
  block-size: 1.1rem;
  inline-size: 34%;
  margin-block-start: .75rem;
}

.est-13__dl {
  block-size: .7rem;
  inline-size: calc(var(--w, 90) * 1%);
  border-radius: 4px;
  background: color-mix(in oklab, var(--sunk) 75%, transparent);
}

.est-13__dl[data-w="92"] {
  --w: 92;
}

.est-13__dl[data-w="84"] {
  --w: 84;
}

.est-13__dl[data-w="96"] {
  --w: 96;
}

.est-13__dl[data-w="61"] {
  --w: 61;
}

.est-13__dl[data-w="88"] {
  --w: 88;
}

.est-13__dl[data-w="79"] {
  --w: 79;
}

.est-13__dl[data-w="93"] {
  --w: 93;
}

.est-13__dl[data-w="48"] {
  --w: 48;
}

.est-13__scrim {
  position: absolute;
  inset: 0;
  background: radial-gradient(70% 60% at 50% 45%, color-mix(in oklab, var(--bg) 55%, transparent), color-mix(in oklab, var(--bg) 88%, transparent));
}

.est-13__gate {
  position: relative;
  z-index: 1;
  inline-size: min(31rem,calc(100% - 2rem));
  margin: clamp(1rem,4vw,2rem);
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .5rem;
  padding: clamp(1.75rem,4vw,2.5rem);
  background: color-mix(in oklab, var(--surface) 96%, transparent);
  border: 1px solid var(--line);
  border-radius: 22px;
  box-shadow: 0 1px 2px rgba(20,22,26,.05), 0 50px 90px -60px rgba(20,22,26,.6);
  animation: est-13-in .55s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-13-in {
  from {
    opacity: 0;
    translate: 0 12px;
    scale: .99;
  }

  to {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }
}

.est-13__lock {
  position: relative;
  inline-size: 3.5rem;
  block-size: 3.5rem;
  display: grid;
  place-items: center;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 7%, var(--surface));
  border-radius: 16px;
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--accent) 15%, transparent);
}

.est-13__lock svg {
  inline-size: 1.55rem;
  block-size: 1.55rem;
}

.est-13__code {
  margin: .75rem 0 0;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .72rem;
  letter-spacing: .22em;
  color: var(--faint);
}

.est-13__h1 {
  margin: 0;
  font-size: clamp(1.3rem,3vw,1.75rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.15;
  text-wrap: balance;
}

.est-13__p {
  margin: 0;
  max-inline-size: 42ch;
  font-size: .92rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-13__acts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .95rem;
}

.est-13__pri {
  min-block-size: 2.8rem;
  padding: .68rem 1.1rem;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  cursor: pointer;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 11px;
  box-shadow: 0 10px 22px -16px color-mix(in oklab, var(--accent) 80%, transparent);
  transition: translate .16s, background .16s;
}

.est-13__pri:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 86%, #000);
}

.est-13__ghost {
  min-block-size: 2.8rem;
  padding: .68rem 1.05rem;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 11px;
  transition: background .16s;
}

.est-13__ghost:hover {
  background: var(--sunk);
}

.est-13__pending {
  display: flex;
  align-items: center;
  gap: .6rem;
  margin-block-start: .95rem;
  padding: .65rem .85rem;
  font-size: .85rem;
  color: var(--ok);
  background: color-mix(in oklab, var(--ok) 8%, var(--surface));
  border: 1px solid color-mix(in oklab, var(--ok) 24%, transparent);
  border-radius: 11px;
  animation: est-13-in .4s cubic-bezier(.2,.7,.3,1) both;
}

.est-13__ptick {
  inline-size: 1.3rem;
  block-size: 1.3rem;
  display: grid;
  place-items: center;
  flex: none;
  border-radius: 50%;
  color: #fff;
  background: var(--ok);
}

.est-13__ptick svg {
  inline-size: .8rem;
  block-size: .8rem;
}

.est-13__owners {
  margin: 1.4rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  justify-content: center;
  padding-block-start: 1rem;
  border-block-start: 1px solid var(--line);
  inline-size: 100%;
}

.est-13__owners div {
  display: grid;
  gap: .2rem;
}

.est-13__owners dt {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .62rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-13__owners dd {
  margin: 0;
  font-size: .84rem;
  color: var(--muted);
}

.est-13__pri:focus-visible,
.est-13__ghost:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .est-13 *,
    .est-13 *::before,
    .est-13 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-13__gate,
    .est-13__lock,
    .est-13__pri {
    border-color: CanvasText;
  }

  .est-13__doc {
    display: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-13'); if(!root) return;
  var req = root.querySelector('#est-13-req'), acts = root.querySelector('#est-13-acts'),
      pending = root.querySelector('#est-13-pending'), p = root.querySelector('#est-13-p');
  req.addEventListener('click', function(){
    acts.hidden = true; pending.hidden = false;
    p.textContent = 'Priya or Marc can approve it. You will get a notification the moment one of them does.';
  });
})();
```
