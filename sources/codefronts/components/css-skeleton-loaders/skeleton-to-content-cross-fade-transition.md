---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/skeleton-to-content-cross-fade-transition/"
title: "Skeleton to Content Cross-Fade Transition"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "The swap is the part users actually feel."
has_js: "true"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeleton to Content Cross-Fade Transition
Source: https://codefronts.com/components/css-skeleton-loaders/skeleton-to-content-cross-fade-transition/

The swap is the part users actually feel. Stack the skeleton and the real content in the same grid cell, cross-fade them over 200ms, and the resolved content arrives instead of snapping in — with @starting-style and transition-behavior: allow-discrete so the entry animates even though the element starts at display: none.
## HTML
```html
<div class="sk-07">
  <div class="sk-07__stage">
    <section class="sk-07__wrap" aria-labelledby="sk-07-h">
      <header class="sk-07__head">
        <p class="sk-07__eyebrow">200ms · cross-fade</p>
        <h2 class="sk-07__h" id="sk-07-h">Resolve into the content, don't snap to it</h2>
        <p class="sk-07__sub">Skeleton and content share one grid cell. On resolve, one fades out while the other fades in and rises 4px — no reflow, no pop.</p>
        <div class="sk-07__controls">
          <button class="sk-07__btn" id="sk-07-btn" type="button">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 12a8 8 0 1 0-2.6 5.9" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M20 6.5V12h-5.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Replay the swap
          </button>
          <p class="sk-07__phase" id="sk-07-phase">phase: pending</p>
        </div>
      </header>

      <div class="sk-07__swap" id="sk-07-swap">
        <div class="sk-07__skel" role="status" aria-live="polite" id="sk-07-live">
          <span class="sk-07__vh">Loading release notes…</span>
          <div class="sk-07__row" aria-hidden="true">
            <span class="sk-07__bar sk-07__avatar"></span>
            <div class="sk-07__ident"><span class="sk-07__bar" style="inline-size:9rem"></span><span class="sk-07__bar sk-07__bar--sm" style="inline-size:6rem"></span></div>
            <span class="sk-07__bar sk-07__bar--pill"></span>
          </div>
          <span class="sk-07__bar sk-07__bar--title"></span>
          <div class="sk-07__lines" aria-hidden="true">
            <span class="sk-07__bar sk-07__bar--sm"></span>
            <span class="sk-07__bar sk-07__bar--sm"></span>
            <span class="sk-07__bar sk-07__bar--sm" style="inline-size:64%"></span>
          </div>
          <div class="sk-07__foot" aria-hidden="true">
            <span class="sk-07__bar sk-07__bar--chip"></span>
            <span class="sk-07__bar sk-07__bar--chip"></span>
            <span class="sk-07__bar sk-07__bar--chip"></span>
          </div>
        </div>

        <article class="sk-07__real">
          <div class="sk-07__row">
            <img class="sk-07__pic" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&amp;fit=crop&amp;w=96&amp;h=96&amp;q=70" width="96" height="96" alt="Jordan Lee" loading="lazy" decoding="async">
            <div class="sk-07__ident">
              <p class="sk-07__name">Jordan Lee</p>
              <p class="sk-07__meta">Platform · pushed 12 minutes ago</p>
            </div>
            <p class="sk-07__tagpill">v4.2.0</p>
          </div>
          <h3 class="sk-07__title">Route-level skeletons everywhere</h3>
          <p class="sk-07__copy">Every dashboard segment now ships a matching loading shell, so navigation paints instantly and the resolved page lands in the same boxes. p75 CLS across the app dropped from 0.14 to 0.00.</p>
          <ul class="sk-07__chips">
            <li>performance</li>
            <li>app-router</li>
            <li>a11y</li>
          </ul>
        </article>
      </div>

      <aside class="sk-07__spec" aria-label="Recipe">
        <p class="sk-07__srow"><span class="sk-07__skey">overlap</span><span class="sk-07__sval">display: grid; both children on grid-area: 1 / 1</span></p>
        <p class="sk-07__srow"><span class="sk-07__skey">fade</span><span class="sk-07__sval">opacity .2s ease + translate .2s cubic-bezier(.2,.7,.3,1)</span></p>
        <p class="sk-07__srow"><span class="sk-07__skey">insert</span><span class="sk-07__sval">@starting-style + transition-behavior: allow-discrete (Chrome 117+)</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-07 {
  --bg: #06070d;
  --bg2: #0c0f1c;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #f3f5fc;
  --muted: rgba(243,245,252,.62);
  --faint: rgba(243,245,252,.42);
  --accent: #7aa2ff;
  --sk: rgba(243,245,252,.1);
  --sheen: rgba(243,245,252,.16);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(65% 45% at 20% -6%, rgba(122,162,255,.16) 0%, transparent 62%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-07 *,
.sk-07 *::before,
.sk-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 260)) {
  .sk-07 {
    --ink: oklch(0.97 0.008 265);
    --muted: oklch(0.97 0.008 265 / .62);
    --faint: oklch(0.97 0.008 265 / .42);
    --accent: oklch(0.76 0.13 262);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-07 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 16%, transparent);
  }
}

.sk-07__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-07__wrap {
  inline-size: min(58rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-07__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 44rem;
}

.sk-07__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-07__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-07__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-07__controls {
  display: flex;
  align-items: center;
  gap: .9rem;
  flex-wrap: wrap;
  margin-block-start: .35rem;
}

.sk-07__btn {
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding: .6rem 1.05rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  color: #0a1024;
  background: var(--accent);
  border: 1px solid transparent;
  transition: translate .18s ease;
}

.sk-07__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sk-07__btn:hover {
  translate: 0 -1px;
}

.sk-07__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.sk-07__phase {
  margin: 0;
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--muted);
}

.sk-07__swap {
  display: grid;
  padding: clamp(1.1rem,2.2vw,1.6rem);
  border: 1px solid var(--line);
  border-radius: 1.15rem;
  background: var(--surface);
  box-shadow: 0 30px 72px -44px rgba(0,0,0,.9);
  min-block-size: 17rem;
}

.sk-07__swap > * {
  grid-area: 1 / 1;
}

.sk-07__skel {
  display: grid;
  gap: .85rem;
  align-content: start;
  opacity: 1;
  transition: opacity .2s ease;
}

.sk-07__real {
  display: grid;
  gap: .85rem;
  align-content: start;
  opacity: 0;
  translate: 0 4px;
  pointer-events: none;
  transition: opacity .2s ease, translate .2s cubic-bezier(.2,.7,.3,1);
}

.sk-07__swap.is-ready .sk-07__skel {
  opacity: 0;
  pointer-events: none;
}

.sk-07__swap.is-ready .sk-07__real {
  opacity: 1;
  translate: 0 0;
  pointer-events: auto;
}

@supports (transition-behavior: allow-discrete) {
  .sk-07__real {
    transition: opacity .2s ease, translate .2s cubic-bezier(.2,.7,.3,1), display .2s allow-discrete;
  }
}

.sk-07__row {
  display: flex;
  align-items: center;
  gap: .85rem;
}

.sk-07__ident {
  display: grid;
  gap: .4rem;
  flex: 1;
  min-inline-size: 0;
}

.sk-07__pic {
  inline-size: 2.9rem;
  aspect-ratio: 1;
  border-radius: 999px;
  object-fit: cover;
  background: var(--sk);
  flex: none;
}

.sk-07__name {
  margin: 0;
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: -.01em;
}

.sk-07__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.sk-07__tagpill {
  margin: 0;
  padding: .35rem .7rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(122,162,255,.14);
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--accent);
  flex: none;
}

.sk-07__title {
  margin: .15rem 0 0;
  font-size: clamp(1.15rem,2.2vw,1.45rem);
  font-weight: 600;
  letter-spacing: -.022em;
}

.sk-07__copy {
  margin: 0;
  font-size: .95rem;
  line-height: 1.62;
  color: var(--muted);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.sk-07__chips {
  list-style: none;
  margin: .15rem 0 0;
  padding: 0;
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
}

.sk-07__chips li {
  padding: .35rem .75rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.04);
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.sk-07__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .85rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-07__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-07-sheen 1.4s linear infinite;
}

@keyframes sk-07-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-07__bar--sm {
  block-size: .7rem;
}

.sk-07__bar--title {
  block-size: 1.5rem;
  inline-size: clamp(50%,32ch,80%);
  border-radius: 8px;
  margin-block-start: .15rem;
}

.sk-07__bar--pill {
  inline-size: 4.2rem;
  block-size: 1.6rem;
  border-radius: 999px;
  flex: none;
}

.sk-07__bar--chip {
  inline-size: 5.2rem;
  block-size: 1.7rem;
  border-radius: 999px;
}

.sk-07__avatar {
  inline-size: 2.9rem;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}

.sk-07__lines {
  display: grid;
  gap: .6rem;
}

.sk-07__foot {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
  margin-block-start: .15rem;
}

.sk-07__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-07__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-07__skey {
  min-inline-size: 4rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-07__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-07[data-theme="light"] {
  --bg: #f7f8fd;
  --bg2: #fff;
  --surface: rgba(8,10,26,.026);
  --line: rgba(8,10,26,.11);
  --ink: #080a1a;
  --muted: rgba(8,10,26,.62);
  --faint: rgba(8,10,26,.44);
  --accent: #2c4bd8;
  background: linear-gradient(178deg,#fff 0%,#eceefb 100%);
}

.sk-07[data-theme="light"] .sk-07__btn {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .sk-07:not([data-theme="dark"]) {
    --bg: #f7f8fd;
    --bg2: #fff;
    --surface: rgba(8,10,26,.026);
    --line: rgba(8,10,26,.11);
    --ink: #080a1a;
    --muted: rgba(8,10,26,.62);
    --faint: rgba(8,10,26,.44);
    --accent: #2c4bd8;
    background: linear-gradient(178deg,#fff 0%,#eceefb 100%);
  }

  .sk-07:not([data-theme="dark"]) .sk-07__btn {
    color: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-07__bar::after {
    animation: none;
    background: none;
  }

  .sk-07__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }

  .sk-07__skel,
    .sk-07__real {
    transition-duration: .01ms;
    translate: none;
  }

  .sk-07__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .sk-07__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-07__bar::after {
    animation: none;
    background: none;
  }

  .sk-07__swap,
    .sk-07__spec,
    .sk-07__btn,
    .sk-07__chips li,
    .sk-07__tagpill {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const swap = document.getElementById('sk-07-swap');
const btn = document.getElementById('sk-07-btn');
const phase = document.getElementById('sk-07-phase');
const live = document.getElementById('sk-07-live');

const resolve = () => {
  swap.classList.add('is-ready');
  phase.textContent = 'phase: resolved · cross-faded in 200ms';
  live.querySelector('.sk-07__vh').textContent = 'Release notes loaded.';
  btn.disabled = false;
};

btn.addEventListener('click', () => {
  btn.disabled = true;
  swap.classList.remove('is-ready');
  phase.textContent = 'phase: pending · skeleton visible';
  live.querySelector('.sk-07__vh').textContent = 'Loading release notes…';
  setTimeout(resolve, 1500);
});

setTimeout(resolve, 1800);
```
