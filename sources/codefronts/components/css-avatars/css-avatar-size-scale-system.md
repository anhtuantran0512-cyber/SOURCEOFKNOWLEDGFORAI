---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-size-scale-system/"
title: "CSS Avatar Size Scale System"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The design-system demo: five named sizes — xs, sm, md, lg, xl — all derived from a single --size token, with the ring, the status dot, the count badge and…"
has_js: "true"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar Size Scale System
Source: https://codefronts.com/components/css-avatars/css-avatar-size-scale-system/

The design-system demo: five named sizes — xs, sm, md, lg, xl — all derived from a single --size token, with the ring, the status dot, the count badge and the initials type all scaling proportionally because every one of them is expressed relative to that token. A slider retunes the base at runtime so you can watch the whole system stay in proportion instead of drifting.
## HTML
```html
<div class="av-21">
  <button class="av-21__theme" type="button" aria-pressed="false">
    <svg class="av-21__i av-21__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-21__i av-21__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-21__vh">Toggle dark theme</span>
  </button>

  <div class="av-21__stage">
    <section class="av-21__wrap" aria-labelledby="av-21-h">
      <header class="av-21__head">
        <p class="av-21__eyebrow">Design system · Avatar</p>
        <h2 class="av-21__h" id="av-21-h">One token, five steps</h2>
        <p class="av-21__sub">Ring, status dot, badge and monogram are all fractions of <code>--size</code>. Move the base and watch them hold proportion.</p>
      </header>

      <div class="av-21__panel">
        <ul class="av-21__scale">
          <li class="av-21__step">
            <span class="av-21__av av-21__av--xs">
              <img class="av-21__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-21__dot" aria-hidden="true"></span>
            </span>
            <span class="av-21__name">xs</span><span class="av-21__mult">0.5×</span>
          </li>
          <li class="av-21__step">
            <span class="av-21__av av-21__av--sm">
              <img class="av-21__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-21__dot" aria-hidden="true"></span>
            </span>
            <span class="av-21__name">sm</span><span class="av-21__mult">0.7×</span>
          </li>
          <li class="av-21__step">
            <span class="av-21__av av-21__av--md">
              <img class="av-21__img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-21__dot" aria-hidden="true"></span>
              <span class="av-21__badge" aria-hidden="true">4</span>
            </span>
            <span class="av-21__name">md</span><span class="av-21__mult">1×</span>
          </li>
          <li class="av-21__step">
            <span class="av-21__av av-21__av--lg">
              <img class="av-21__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=320&auto=format&fit=facearea&facepad=2.5" alt="Jordan Lee" width="320" height="320" loading="lazy" decoding="async">
              <span class="av-21__dot" aria-hidden="true"></span>
              <span class="av-21__badge" aria-hidden="true">12</span>
            </span>
            <span class="av-21__name">lg</span><span class="av-21__mult">1.45×</span>
          </li>
          <li class="av-21__step">
            <span class="av-21__av av-21__av--xl av-21__av--mono" style="--h:264">
              <span class="av-21__mono" aria-hidden="true">EV</span>
              <span class="av-21__vh">Elena Vasquez</span>
              <span class="av-21__dot" aria-hidden="true"></span>
              <span class="av-21__badge" aria-hidden="true">99+</span>
            </span>
            <span class="av-21__name">xl</span><span class="av-21__mult">2.2×</span>
          </li>
        </ul>

        <div class="av-21__ctl">
          <label class="av-21__ctllabel" for="av-21-range">Base size <output class="av-21__out" id="av-21-out">44px</output></label>
          <input class="av-21__range" type="range" id="av-21-range" min="28" max="64" step="2" value="44">
          <p class="av-21__note">md = base · every decoration is a fraction of it</p>
        </div>
      </div>

      <ul class="av-21__spec">
        <li><span class="av-21__k">Ring</span><code>max(1.5px, size × .06)</code></li>
        <li><span class="av-21__k">Status dot</span><code>max(.5rem, size × .3)</code></li>
        <li><span class="av-21__k">Count badge</span><code>max(1rem, size × .38)</code></li>
        <li><span class="av-21__k">Monogram</span><code>size × .36</code></li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-21 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
    --online: oklch(64% .17 150);
    --badge: oklch(55% .22 22);
  }

  .av-21__av--mono {
    background: oklch(93% .055 var(--h));
    color: oklch(44% .13 var(--h));
  }
}

.av-21 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --online: #16a34a;
  --badge: #dc2626;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --base: 44px;
  width: 100%;
  inline-size: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.av-21 *,
.av-21 *::before,
.av-21 *::after {
  box-sizing: border-box;
}

.av-21__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.av-21__theme {
  position: absolute;
  inset-block-start: clamp(.85rem,2.2vw,1.5rem);
  inset-inline-end: clamp(.85rem,2.2vw,1.5rem);
  z-index: 20;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--glass);
  color: var(--ink);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.av-21__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-21__theme:hover {
  translate: 0 -1px;
}

.av-21__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-21__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-21__i--sun {
  display: none;
}

.av-21[data-theme="dark"] .av-21__i--moon {
  display: none;
}

.av-21[data-theme="dark"] .av-21__i--sun {
  display: block;
}

.av-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-21__wrap {
  inline-size: min(56rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.6rem);
}

.av-21__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-21__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-21__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-21__sub {
  margin: 0;
  max-inline-size: 38rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-21__sub code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .85rem;
  padding: .05rem .3rem;
  border-radius: 5px;
  background: var(--panel-2);
}

.av-21__panel {
  display: flex;
  flex-direction: column;
  gap: clamp(1.5rem,4vw,2.25rem);
  padding: clamp(1.75rem,4.5vw,2.75rem) clamp(1.25rem,3.5vw,2.25rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-21__scale {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: center;
  gap: clamp(1.25rem,4vw,2.5rem);
}

.av-21__step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .4rem;
}

.av-21__av {
  --size: var(--base);
  --ring: max(1.5px, calc(var(--size) * .06));
  --dot: max(.5rem, calc(var(--size) * .3));
  --bdg: max(1rem, calc(var(--size) * .38));
  position: relative;
  display: grid;
  place-items: center;
  inline-size: var(--size);
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--panel-2);
  box-shadow: 0 0 0 var(--ring) var(--accent), 0 0 0 calc(var(--ring) + 1px) var(--panel);
  font-size: calc(var(--size) * .36);
  font-weight: 700;
  transition: inline-size .2s ease;
}

.av-21__av--xs {
  --size: calc(var(--base) * .5);
}

.av-21__av--sm {
  --size: calc(var(--base) * .7);
}

.av-21__av--md {
  --size: var(--base);
}

.av-21__av--lg {
  --size: calc(var(--base) * 1.45);
}

.av-21__av--xl {
  --size: calc(var(--base) * 2.2);
}

.av-21__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
}

.av-21__av--mono {
  background: hsl(var(--h) 72% 92%);
  color: hsl(var(--h) 55% 30%);
}

.av-21__mono {
  letter-spacing: .02em;
}

.av-21__dot {
  position: absolute;
  inset-block-end: 0;
  inset-inline-end: 0;
  z-index: 2;
  inline-size: var(--dot);
  block-size: var(--dot);
  border-radius: 50%;
  background: var(--online);
  box-shadow: 0 0 0 max(1.5px, calc(var(--size) * .045)) var(--panel);
}

.av-21__badge {
  position: absolute;
  inset-block-start: -4%;
  inset-inline-end: -8%;
  z-index: 2;
  display: grid;
  place-items: center;
  min-inline-size: var(--bdg);
  block-size: var(--bdg);
  padding-inline: calc(var(--bdg) * .2);
  border-radius: 999px;
  background: var(--badge);
  color: #fff;
  font-size: calc(var(--bdg) * .52);
  font-weight: 700;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  box-shadow: 0 0 0 max(1.5px, calc(var(--size) * .045)) var(--panel);
}

.av-21__name {
  font-size: .85rem;
  font-weight: 700;
  letter-spacing: .02em;
}

.av-21__mult {
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.av-21__ctl {
  display: flex;
  flex-direction: column;
  gap: .5rem;
  max-inline-size: 24rem;
  inline-size: 100%;
  margin-inline: auto;
}

.av-21__ctllabel {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  font-size: .82rem;
  font-weight: 600;
  color: var(--muted);
}

.av-21__out {
  font-size: .95rem;
  font-weight: 700;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.av-21__range {
  appearance: none;
  inline-size: 100%;
  block-size: 2.75rem;
  margin: 0;
  background: transparent;
  cursor: pointer;
}

.av-21__range::-webkit-slider-runnable-track {
  block-size: .4rem;
  border-radius: 999px;
  background: var(--panel-2);
}

.av-21__range::-moz-range-track {
  block-size: .4rem;
  border-radius: 999px;
  background: var(--panel-2);
}

.av-21__range::-webkit-slider-thumb {
  appearance: none;
  inline-size: 1.5rem;
  block-size: 1.5rem;
  margin-block-start: -.55rem;
  border-radius: 50%;
  background: var(--ink);
  border: 3px solid var(--panel);
  box-shadow: 0 1px 4px rgba(16,19,26,.3);
}

.av-21__range::-moz-range-thumb {
  inline-size: 1.5rem;
  block-size: 1.5rem;
  border-radius: 50%;
  background: var(--ink);
  border: 3px solid var(--panel);
}

.av-21__range:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
  border-radius: 8px;
}

.av-21__note {
  margin: 0;
  font-size: .78rem;
  color: var(--muted);
  text-align: center;
}

.av-21__spec {
  list-style: none;
  margin: 0;
  padding: 1rem 1.15rem;
  display: grid;
  gap: .4rem;
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-21__spec li {
  display: flex;
  align-items: baseline;
  gap: .6rem;
  font-size: .8rem;
}

.av-21__k {
  min-inline-size: 6rem;
  font-weight: 650;
  color: var(--ink);
}

.av-21__spec code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .75rem;
  color: var(--muted);
  padding: .1rem .35rem;
  border-radius: 5px;
  background: var(--panel-2);
}

.av-21[data-theme="dark"] {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --online: #4ade80;
  --badge: #ef4444;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-21[data-theme="dark"] .av-21__av--mono {
  background: hsl(var(--h) 42% 22%);
  color: hsl(var(--h) 78% 82%);
}

@media (prefers-color-scheme: dark) {
  .av-21:not([data-theme="light"]) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --online: #4ade80;
    --badge: #ef4444;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-21:not([data-theme="light"]) .av-21__i--moon {
    display: none;
  }

  .av-21:not([data-theme="light"]) .av-21__i--sun {
    display: block;
  }

  .av-21:not([data-theme="light"]) .av-21__av--mono {
    background: hsl(var(--h) 42% 22%);
    color: hsl(var(--h) 78% 82%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-21 *,
    .av-21 *::before,
    .av-21 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-21__av {
    box-shadow: none;
    outline: 2px solid CanvasText;
  }

  .av-21__dot,
    .av-21__badge {
    background: CanvasText;
    color: Canvas;
  }

  .av-21__panel,
    .av-21__spec,
    .av-21__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const av21 = document.querySelector('.av-21');
const av21range = av21.querySelector('#av-21-range');
const av21out = av21.querySelector('#av-21-out');

const av21sync = () => {
  av21.style.setProperty('--base', av21range.value + 'px');
  av21out.textContent = av21range.value + 'px';
};

av21range.addEventListener('input', av21sync);

av21.querySelector('.av-21__theme').addEventListener('click', (e) => {
  const on = av21.dataset.theme !== 'dark';
  av21.dataset.theme = on ? 'dark' : 'light';
  e.currentTarget.setAttribute('aria-pressed', String(on));
});
av21sync();
```
