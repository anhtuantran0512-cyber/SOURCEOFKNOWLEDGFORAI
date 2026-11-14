---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/aria-live-region-loading-announcement/"
title: "ARIA Live Region Loading Announcement"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "A skeleton is a purely visual promise — a screen reader user gets silence."
has_js: "true"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: ARIA Live Region Loading Announcement
Source: https://codefronts.com/components/css-skeleton-loaders/aria-live-region-loading-announcement/

A skeleton is a purely visual promise — a screen reader user gets silence. This demo pairs the skeleton with a visually hidden aria-live="polite" region that says "Loading" on mount and "Content loaded" on resolve, shows the role="status" alternative side by side, and prints an announcement transcript so you can see exactly what assistive tech will read.
## HTML
```html
<div class="sk-08">
  <div class="sk-08__stage">
    <section class="sk-08__wrap" aria-labelledby="sk-08-h">
      <header class="sk-08__head">
        <p class="sk-08__eyebrow">WCAG 2.2 · SC 4.1.3</p>
        <h2 class="sk-08__h" id="sk-08-h">Say out loud what the skeleton only shows</h2>
        <p class="sk-08__sub">The bars are <code>aria-hidden</code>. A hidden polite region carries the words — once when loading starts, once when it ends.</p>
        <button class="sk-08__btn" id="sk-08-btn" type="button">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v6.2l4.4 2.6" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="12" r="8.4" stroke="currentColor" stroke-width="1.9"/></svg>
          Run the load cycle
        </button>
      </header>

      <div class="sk-08__cols">
        <section class="sk-08__panel" aria-labelledby="sk-08-a">
          <p class="sk-08__label" id="sk-08-a">aria-live="polite" · explicit</p>
          <div class="sk-08__feed" id="sk-08-feed" aria-busy="true">
            <p class="sk-08__vh" id="sk-08-live" aria-live="polite" aria-atomic="true"></p>
            <ul class="sk-08__list" id="sk-08-skel">
              <li class="sk-08__item" aria-hidden="true"><span class="sk-08__bar sk-08__avatar"></span><div class="sk-08__ident"><span class="sk-08__bar" style="inline-size:8rem"></span><span class="sk-08__bar sk-08__bar--sm" style="inline-size:11rem"></span></div></li>
              <li class="sk-08__item" aria-hidden="true"><span class="sk-08__bar sk-08__avatar"></span><div class="sk-08__ident"><span class="sk-08__bar" style="inline-size:6.5rem"></span><span class="sk-08__bar sk-08__bar--sm" style="inline-size:13rem"></span></div></li>
              <li class="sk-08__item" aria-hidden="true"><span class="sk-08__bar sk-08__avatar"></span><div class="sk-08__ident"><span class="sk-08__bar" style="inline-size:9rem"></span><span class="sk-08__bar sk-08__bar--sm" style="inline-size:9.5rem"></span></div></li>
            </ul>
            <ul class="sk-08__list sk-08__list--real" id="sk-08-real" hidden>
              <li class="sk-08__item"><span class="sk-08__dot" aria-hidden="true">AC</span><div class="sk-08__ident"><p class="sk-08__name">Alex Chen</p><p class="sk-08__note">merged “skeleton tokens” into main</p></div></li>
              <li class="sk-08__item"><span class="sk-08__dot" aria-hidden="true">PS</span><div class="sk-08__ident"><p class="sk-08__name">Priya Sharma</p><p class="sk-08__note">commented on Loading UI audit</p></div></li>
              <li class="sk-08__item"><span class="sk-08__dot" aria-hidden="true">SR</span><div class="sk-08__ident"><p class="sk-08__name">Sam Rivera</p><p class="sk-08__note">closed CLS regression on /reports</p></div></li>
            </ul>
          </div>
        </section>

        <section class="sk-08__panel" aria-labelledby="sk-08-b">
          <p class="sk-08__label">role="status" · implicit polite</p>
          <p class="sk-08__labelsub" id="sk-08-b">Same behaviour, broader legacy AT support</p>
          <pre class="sk-08__code"><code>&lt;section aria-busy="true"&gt;
  &lt;p class="vh" role="status"&gt;
    Loading activity feed…
  &lt;/p&gt;
  &lt;span class="bar" aria-hidden="true"&gt;&lt;/span&gt;
&lt;/section&gt;</code></pre>
          <div class="sk-08__sr" aria-hidden="true">
            <p class="sk-08__srhead">
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 9.5h3.2L13 5v14l-5.8-4.5H4v-5Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M16.6 9a4.5 4.5 0 0 1 0 6M19 6.4a8 8 0 0 1 0 11.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
              Screen reader transcript
            </p>
            <ol class="sk-08__log" id="sk-08-log"></ol>
          </div>
        </section>
      </div>

      <aside class="sk-08__spec" aria-label="Recipe">
        <p class="sk-08__srow"><span class="sk-08__skey">region</span><span class="sk-08__sval">render it empty on mount, then write text — never insert both at once</span></p>
        <p class="sk-08__srow"><span class="sk-08__skey">bars</span><span class="sk-08__sval">aria-hidden="true" on every decorative bar + aria-busy on the container</span></p>
        <p class="sk-08__srow"><span class="sk-08__skey">never</span><span class="sk-08__sval">aria-live="assertive" for loading · display:none on the region</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-08 {
  --bg: #050a08;
  --bg2: #0a1512;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #eef7f2;
  --muted: rgba(238,247,242,.62);
  --faint: rgba(238,247,242,.42);
  --accent: #4ade9a;
  --sk: rgba(238,247,242,.1);
  --sheen: rgba(238,247,242,.16);
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
  background: radial-gradient(62% 44% at 84% -6%, rgba(74,222,154,.14) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-08 *,
.sk-08 *::before,
.sk-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 160)) {
  .sk-08 {
    --ink: oklch(0.97 0.01 165);
    --muted: oklch(0.97 0.01 165 / .62);
    --faint: oklch(0.97 0.01 165 / .42);
    --accent: oklch(0.83 0.14 158);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-08 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 16%, transparent);
  }
}

.sk-08__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-08__wrap {
  inline-size: min(74rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-08__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
  justify-items: start;
}

.sk-08__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-08__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-08__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-08__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-08__btn {
  margin-block-start: .35rem;
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
  color: #04140d;
  background: var(--accent);
  border: 1px solid transparent;
  transition: translate .18s ease, opacity .18s ease;
}

.sk-08__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sk-08__btn:hover {
  translate: 0 -1px;
}

.sk-08__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.sk-08__btn[disabled] {
  opacity: .5;
  translate: none;
  cursor: progress;
}

.sk-08__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(18rem,1fr));
  align-items: start;
}

.sk-08__panel {
  display: grid;
  gap: .75rem;
  padding: clamp(1.05rem,2vw,1.45rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
  min-block-size: 17rem;
  align-content: start;
}

.sk-08__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--accent);
}

.sk-08__labelsub {
  margin: -.35rem 0 0;
  font-size: .85rem;
  color: var(--muted);
}

.sk-08__feed {
  display: grid;
  gap: .2rem;
}

.sk-08__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .85rem;
}

.sk-08__item {
  display: flex;
  align-items: center;
  gap: .85rem;
  min-block-size: 2.6rem;
}

.sk-08__ident {
  display: grid;
  gap: .4rem;
  min-inline-size: 0;
}

.sk-08__dot {
  inline-size: 2.4rem;
  block-size: 2.4rem;
  flex: none;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: rgba(74,222,154,.16);
  border: 1px solid rgba(74,222,154,.3);
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--accent);
}

.sk-08__name {
  margin: 0;
  font-size: .95rem;
  font-weight: 500;
}

.sk-08__note {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.sk-08__code {
  margin: 0;
  padding: .9rem 1rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: rgba(0,0,0,.28);
  font-family: var(--mono);
  font-size: .72rem;
  line-height: 1.65;
  color: var(--muted);
  overflow-x: auto;
}

.sk-08__sr {
  padding: .85rem 1rem;
  border-radius: .7rem;
  border: 1px dashed var(--line);
  display: grid;
  gap: .5rem;
}

.sk-08__srhead {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-08__srhead svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.sk-08__log {
  margin: 0;
  padding-inline-start: 1.2rem;
  display: grid;
  gap: .3rem;
  font-family: var(--mono);
  font-size: .73rem;
  line-height: 1.5;
  color: var(--ink);
}

.sk-08__log li::marker {
  color: var(--accent);
}

.sk-08__log li:empty {
  display: none;
}

.sk-08__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-08__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-08-sheen 1.4s linear infinite;
}

@keyframes sk-08-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-08__bar--sm {
  block-size: .68rem;
}

.sk-08__avatar {
  inline-size: 2.4rem;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}

.sk-08__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-08__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-08__skey {
  min-inline-size: 4rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-08__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-08[data-theme="light"] {
  --bg: #f6fbf8;
  --bg2: #fff;
  --surface: rgba(4,20,13,.026);
  --line: rgba(4,20,13,.11);
  --ink: #04140d;
  --muted: rgba(4,20,13,.62);
  --faint: rgba(4,20,13,.44);
  --accent: #0d7a4a;
  background: linear-gradient(178deg,#fff 0%,#e9f6ef 100%);
}

.sk-08[data-theme="light"] .sk-08__btn {
  color: #fff;
}

.sk-08[data-theme="light"] .sk-08__code {
  background: rgba(4,20,13,.04);
}

@media (prefers-color-scheme: light) {
  .sk-08:not([data-theme="dark"]) {
    --bg: #f6fbf8;
    --bg2: #fff;
    --surface: rgba(4,20,13,.026);
    --line: rgba(4,20,13,.11);
    --ink: #04140d;
    --muted: rgba(4,20,13,.62);
    --faint: rgba(4,20,13,.44);
    --accent: #0d7a4a;
    background: linear-gradient(178deg,#fff 0%,#e9f6ef 100%);
  }

  .sk-08:not([data-theme="dark"]) .sk-08__btn {
    color: #fff;
  }

  .sk-08:not([data-theme="dark"]) .sk-08__code {
    background: rgba(4,20,13,.04);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-08__bar::after {
    animation: none;
    background: none;
  }

  .sk-08__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }

  .sk-08__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .sk-08__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-08__bar::after {
    animation: none;
    background: none;
  }

  .sk-08__panel,
    .sk-08__spec,
    .sk-08__btn,
    .sk-08__code,
    .sk-08__sr,
    .sk-08__dot {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const feed = document.getElementById('sk-08-feed');
const live = document.getElementById('sk-08-live');
const log = document.getElementById('sk-08-log');
const skel = document.getElementById('sk-08-skel');
const real = document.getElementById('sk-08-real');
const btn = document.getElementById('sk-08-btn');

const say = (text) => {
  live.textContent = text;                        // region already exists → announced
  const li = document.createElement('li');
  li.textContent = text;
  log.append(li);
};

const cycle = () => {
  btn.disabled = true;
  log.replaceChildren();
  skel.hidden = false; real.hidden = true;
  feed.setAttribute('aria-busy', 'true');
  say('Loading activity feed…');
  setTimeout(() => {
    skel.hidden = true; real.hidden = false;
    feed.removeAttribute('aria-busy');
    say('Activity feed loaded. 3 new items.');
    btn.disabled = false;
  }, 1900);
};

btn.addEventListener('click', cycle);
cycle();
```
