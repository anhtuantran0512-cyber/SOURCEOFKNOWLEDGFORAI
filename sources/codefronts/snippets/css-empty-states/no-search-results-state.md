---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/no-search-results-state/"
title: "No Search Results State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "A search that returns nothing inside a real issue tracker: filter chips above the results, the query echoed back in monospace, and one primary recovery that…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: No Search Results State
Source: https://codefronts.com/snippets/css-empty-states/no-search-results-state/

A search that returns nothing inside a real issue tracker: filter chips above the results, the query echoed back in monospace, and one primary recovery that removes the filter most likely to be the problem. Dropping a chip swaps the empty state for real rows, so the demo shows both halves of the state machine rather than a poster of the sad half.
## HTML
```html
<div class="est-01">
  <div class="est-01__shell">
    <nav class="est-01__rail" aria-label="Workspace">
      <span class="est-01__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M5 17.5 12 4l7 13.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M8.4 17.5h7.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </span>
      <button class="est-01__ri est-01__ri--on" type="button" aria-label="Issues" aria-current="page">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.5" stroke="currentColor" stroke-width="1.7"/><path d="M12 8.4v4.2M12 15.5h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
      <button class="est-01__ri" type="button" aria-label="Pull requests">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="7" cy="6.5" r="2.3" stroke="currentColor" stroke-width="1.7"/><circle cx="7" cy="17.5" r="2.3" stroke="currentColor" stroke-width="1.7"/><circle cx="17" cy="17.5" r="2.3" stroke="currentColor" stroke-width="1.7"/><path d="M7 8.8v6.4M9.3 6.5h5.2a2.5 2.5 0 0 1 2.5 2.5v6.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </button>
      <button class="est-01__ri" type="button" aria-label="Deployments">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 15.5 12 4l8 11.5" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M4.5 19.5h15" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </button>
      <button class="est-01__ri" type="button" aria-label="Insights">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 19V6M20 19H4M8 15.5V11M12.5 15.5V8M17 15.5v-3" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </button>
      <span class="est-01__grow"></span>
      <span class="est-01__me" aria-hidden="true">AR</span>
    </nav>

    <div class="est-01__main">
      <header class="est-01__top">
        <div class="est-01__field">
          <svg class="est-01__mag" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="1.8"/><path d="m15.8 15.8 3.7 3.7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <span class="est-01__q" id="est-01-query">is:open label:regression owner:platform</span>
          <button class="est-01__x" type="button" data-act="reset" aria-label="Clear search">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          </button>
        </div>
        <div class="est-01__tabs" role="tablist" aria-label="Search scope">
          <button class="est-01__tab est-01__tab--on" type="button" role="tab" aria-selected="true">Issues</button>
          <button class="est-01__tab" type="button" role="tab" aria-selected="false">Pull requests</button>
          <button class="est-01__tab" type="button" role="tab" aria-selected="false">Discussions</button>
        </div>
      </header>

      <div class="est-01__chips" id="est-01-chips">
        <button class="est-01__chip" type="button" data-drop="label:regression">label:regression<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
        <button class="est-01__chip" type="button" data-drop="owner:platform">owner:platform<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
        <button class="est-01__chip" type="button" data-drop="is:open">is:open<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
      </div>

      <section class="est-01__body" aria-live="polite" aria-atomic="true">
        <div class="est-01__empty" id="est-01-empty">
          <span class="est-01__glyph" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="10.5" cy="10.5" r="6.4" stroke="currentColor" stroke-width="1.6"/><path d="m15.4 15.4 4.1 4.1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M8 10.5h5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
          </span>
          <h1 class="est-01__h">No issues match all three filters</h1>
          <p class="est-01__p">Platform has nothing open with that label.</p>
          <div class="est-01__acts">
            <button class="est-01__act est-01__act--pri" type="button" data-drop="label:regression">Drop label:regression</button>
            <button class="est-01__act" type="button" data-act="reset">Search every repository</button>
          </div>
        </div>

        <ol class="est-01__list" id="est-01-list" hidden>
          <li class="est-01__row">
            <span class="est-01__dot est-01__dot--open" aria-hidden="true"></span>
            <span class="est-01__rmain"><span class="est-01__rt">Retry storm when the queue drains mid-deploy</span><span class="est-01__rm">platform/edge-router &middot; #4821 &middot; opened by dcheng</span></span>
            <span class="est-01__pill">needs triage</span>
          </li>
          <li class="est-01__row">
            <span class="est-01__dot est-01__dot--open" aria-hidden="true"></span>
            <span class="est-01__rmain"><span class="est-01__rt">Token refresh drops the websocket session</span><span class="est-01__rm">platform/auth &middot; #4804 &middot; opened by mira.k</span></span>
            <span class="est-01__pill est-01__pill--alt">in review</span>
          </li>
          <li class="est-01__row">
            <span class="est-01__dot" aria-hidden="true"></span>
            <span class="est-01__rmain"><span class="est-01__rt">Cold start regression on the image pipeline</span><span class="est-01__rm">platform/media &middot; #4790 &middot; opened by t.oyelaran</span></span>
            <span class="est-01__pill est-01__pill--done">closed</span>
          </li>
        </ol>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-01 {
  --bg: #0b0c0f;
  --panel: #12141a;
  --panel-2: #171a21;
  --line: #22262f;
  --line-2: #2c313c;
  --text: #eef0f5;
  --muted: #9aa1b1;
  --faint: #6b7383;
  --accent: #7aa2ff;
  --open: #4ade80;
  --warn: #f5b661;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--text);
  color-scheme: dark;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-01 *,
.est-01 *::before,
.est-01 *::after {
  box-sizing: border-box;
}

.est-01 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-01 {
    --bg: oklch(0.16 0.011 265);
    --panel: oklch(0.203 0.013 265);
    --panel-2: oklch(0.235 0.015 265);
    --line: oklch(0.29 0.014 265);
    --line-2: oklch(0.345 0.016 265);
    --text: oklch(0.965 0.004 265);
    --muted: oklch(0.735 0.021 265);
    --faint: oklch(0.585 0.021 265);
    --accent: oklch(0.775 0.115 262);
    --open: oklch(0.82 0.17 152);
    --warn: oklch(0.82 0.11 72);
  }
}

.est-01__shell {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-columns: 4.25rem minmax(0,1fr);
}

.est-01__rail {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .35rem;
  padding: 1rem .75rem 1.25rem;
  border-inline-end: 1px solid var(--line);
  background: linear-gradient(180deg,var(--panel),var(--bg));
}

.est-01__mark {
  inline-size: 2.25rem;
  block-size: 2.25rem;
  display: grid;
  place-items: center;
  margin-block-end: .75rem;
  border-radius: 11px;
  color: var(--bg);
  background: var(--text);
}

.est-01__mark svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.est-01__ri {
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 11px;
  color: var(--faint);
  transition: color .18s, background .18s, border-color .18s;
}

.est-01__ri svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.est-01__ri:hover {
  color: var(--text);
  background: var(--panel-2);
}

.est-01__ri--on {
  color: var(--text);
  background: var(--panel-2);
  border-color: var(--line-2);
}

.est-01__ri:focus-visible,
.est-01__x:focus-visible,
.est-01__chip:focus-visible,
.est-01__act:focus-visible,
.est-01__tab:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-01__grow {
  flex: 1 1 auto;
}

.est-01__me {
  inline-size: 2rem;
  block-size: 2rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .68rem;
  letter-spacing: .04em;
  color: var(--text);
  background: var(--panel-2);
  border: 1px solid var(--line-2);
}

.est-01__main {
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto auto minmax(0,1fr);
  align-content: start;
}

.est-01__top {
  display: flex;
  flex-wrap: wrap;
  gap: .9rem 1.5rem;
  align-items: center;
  justify-content: space-between;
  padding: 1rem clamp(1rem,3vw,2rem);
  border-block-end: 1px solid var(--line);
  background: color-mix(in oklab, var(--panel) 70%, transparent);
  backdrop-filter: blur(8px);
}

.est-01__field {
  flex: 1 1 22rem;
  min-inline-size: 0;
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .6rem .7rem .6rem .8rem;
  background: var(--panel-2);
  border: 1px solid var(--line-2);
  border-radius: 12px;
  box-shadow: inset 0 1px 0 color-mix(in oklab, #fff 5%, transparent);
}

.est-01__mag {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  flex: none;
  color: var(--faint);
}

.est-01__q {
  flex: 1 1 auto;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .82rem;
  letter-spacing: -.01em;
  color: var(--text);
}

.est-01__x {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  flex: none;
  display: grid;
  place-items: center;
  cursor: pointer;
  color: var(--faint);
  background: transparent;
  border: 0;
  border-radius: 7px;
  transition: color .16s, background .16s;
}

.est-01__x svg {
  inline-size: .85rem;
  block-size: .85rem;
}

.est-01__x:hover {
  color: var(--text);
  background: var(--line-2);
}

.est-01__tabs {
  display: flex;
  gap: .15rem;
  padding: .2rem;
  background: var(--panel-2);
  border: 1px solid var(--line);
  border-radius: 11px;
}

.est-01__tab {
  padding: .42rem .7rem;
  font: inherit;
  font-size: .8rem;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
  color: var(--muted);
  background: transparent;
  border: 0;
  border-radius: 8px;
  transition: color .16s, background .16s;
}

.est-01__tab:hover {
  color: var(--text);
}

.est-01__tab--on {
  color: var(--text);
  background: var(--line-2);
  box-shadow: 0 1px 2px rgba(0,0,0,.35);
}

.est-01__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  padding: .75rem clamp(1rem,3vw,2rem);
  border-block-end: 1px solid var(--line);
}

.est-01__chip {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .34rem .5rem .34rem .6rem;
  cursor: pointer;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .72rem;
  letter-spacing: -.01em;
  color: var(--muted);
  background: var(--panel);
  border: 1px solid var(--line-2);
  border-radius: 8px;
  transition: color .16s, border-color .16s, background .16s, opacity .2s, scale .2s;
}

.est-01__chip svg {
  inline-size: .6rem;
  block-size: .6rem;
  opacity: .65;
}

.est-01__chip:hover {
  color: var(--text);
  background: var(--panel-2);
  border-color: var(--accent);
}

.est-01__chip[data-gone] {
  opacity: 0;
  scale: .9;
  pointer-events: none;
}

.est-01__body {
  min-block-size: 0;
  padding: clamp(1rem,3vw,2rem);
  display: grid;
  align-content: start;
}

.est-01__empty {
  justify-self: center;
  align-self: start;
  margin-block: clamp(1.5rem,7vh,5rem);
  inline-size: min(30rem,100%);
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .55rem;
  animation: est-01-in .5s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-01-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-01__glyph {
  position: relative;
  inline-size: 5.5rem;
  block-size: 5.5rem;
  display: grid;
  place-items: center;
  margin-block-end: .6rem;
  border: 1px solid var(--line-2);
  border-radius: 18px;
  color: var(--muted);
  overflow: hidden;
  background: radial-gradient(circle at 50% 45%, color-mix(in oklab, var(--accent) 12%, transparent), transparent 62%), var(--panel-2);
}

.est-01__glyph::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);
  background-size: 11px 11px;
  opacity: .55;
  mask-image: radial-gradient(circle at 50% 50%, #000 45%, transparent 78%);
}

.est-01__glyph::after {
  content: '';
  position: absolute;
  inset-block: 0;
  inline-size: 38%;
  background: linear-gradient(90deg,transparent,color-mix(in oklab, var(--accent) 18%, transparent),transparent);
  animation: est-01-sweep 5.5s ease-in-out infinite;
}

@keyframes est-01-sweep {
  0%,
    100% {
    translate: -140% 0;
  }

  50% {
    translate: 280% 0;
  }
}

.est-01__glyph svg {
  position: relative;
  inline-size: 1.85rem;
  block-size: 1.85rem;
}

.est-01__h {
  margin: 0;
  font-size: clamp(1.1rem,2.4vw,1.35rem);
  font-weight: 600;
  letter-spacing: -.025em;
  line-height: 1.25;
  text-wrap: balance;
}

.est-01__p {
  margin: 0;
  font-size: .9rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.est-01__acts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .85rem;
}

.est-01__act {
  min-block-size: 2.75rem;
  padding: .6rem 1rem;
  font: inherit;
  font-size: .85rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--text);
  background: var(--panel-2);
  border: 1px solid var(--line-2);
  border-radius: 11px;
  transition: translate .16s, background .16s, border-color .16s;
}

.est-01__act:hover {
  translate: 0 -1px;
  background: var(--line-2);
}

.est-01__act--pri {
  color: #0a0e1a;
  background: var(--accent);
  border-color: transparent;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .8rem;
  letter-spacing: -.01em;
}

.est-01__act--pri:hover {
  background: color-mix(in oklab, var(--accent) 88%, #fff);
}

.est-01__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .5rem;
  inline-size: min(52rem,100%);
  justify-self: center;
}

.est-01__row {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .25rem .75rem;
  align-items: center;
  padding: .85rem 1rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  animation: est-01-in .45s cubic-bezier(.2,.7,.3,1) both;
}

.est-01__row:nth-child(2) {
  animation-delay: .06s;
}

.est-01__row:nth-child(3) {
  animation-delay: .12s;
}

.est-01__row:hover {
  border-color: var(--line-2);
  background: var(--panel-2);
}

.est-01__dot {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 50%;
  background: var(--faint);
}

.est-01__dot--open {
  background: var(--open);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--open) 18%, transparent);
}

.est-01__rmain {
  min-inline-size: 0;
  display: grid;
  gap: .2rem;
}

.est-01__rt {
  font-size: .9rem;
  font-weight: 500;
  letter-spacing: -.012em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.est-01__rm {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .7rem;
  color: var(--faint);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.est-01__pill {
  padding: .24rem .5rem;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .66rem;
  letter-spacing: .02em;
  white-space: nowrap;
  color: var(--warn);
  background: color-mix(in oklab, var(--warn) 12%, transparent);
  border: 1px solid color-mix(in oklab, var(--warn) 30%, transparent);
  border-radius: 6px;
}

.est-01__pill--alt {
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 12%, transparent);
  border-color: color-mix(in oklab, var(--accent) 30%, transparent);
}

.est-01__pill--done {
  color: var(--faint);
  background: var(--panel-2);
  border-color: var(--line-2);
}

@media (max-width: 640px) {
  .est-01__shell {
    grid-template-columns: 1fr;
  }

  .est-01__rail {
    flex-direction: row;
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }

  .est-01__mark {
    margin: 0 .5rem 0 0;
  }

  .est-01__pill {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-01 *,
    .est-01 *::before,
    .est-01 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-01__glyph,
    .est-01__row,
    .est-01__field,
    .est-01__act {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-01'); if(!root) return;
  var chips = root.querySelector('#est-01-chips'), empty = root.querySelector('#est-01-empty'),
      list = root.querySelector('#est-01-list'), query = root.querySelector('#est-01-query');
  var base = ['is:open','label:regression','owner:platform'];
  function paint(){
    var live = base.filter(function(t){ var c = chips.querySelector('[data-drop="' + t + '"]'); return c && !c.hasAttribute('data-gone'); });
    query.textContent = live.length ? live.join(' ') : 'search all repositories';
    var found = live.length < 3;
    empty.hidden = found; list.hidden = !found;
  }
  root.addEventListener('click', function(e){
    var drop = e.target.closest('[data-drop]'), act = e.target.closest('[data-act="reset"]');
    if(drop){
      var chip = chips.querySelector('[data-drop="' + drop.dataset.drop + '"]');
      if(chip) chip.setAttribute('data-gone','');
      paint(); return;
    }
    if(act){
      chips.querySelectorAll('[data-drop]').forEach(function(c){ c.setAttribute('data-gone',''); });
      paint();
    }
  });
})();
```
