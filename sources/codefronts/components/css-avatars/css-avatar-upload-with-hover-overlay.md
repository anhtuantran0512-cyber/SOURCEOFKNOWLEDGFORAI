---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-upload-with-hover-overlay/"
title: "CSS Avatar Upload with Hover Overlay"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The affordance, not the flow: hovering (or focusing) the avatar reveals a camera-icon scrim that says the photo is changeable."
has_js: "true"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar Upload with Hover Overlay
Source: https://codefronts.com/components/css-avatars/css-avatar-upload-with-hover-overlay/

The affordance, not the flow: hovering (or focusing) the avatar reveals a camera-icon scrim that says the photo is changeable. The control is a real <input type="file"> wrapped in its <label> — so it is keyboard reachable, announced properly and needs no click handler — and a local preview swaps in immediately with a polite live-region confirmation. No progress bars, no drop zones; this demo is about making "you can change this" legible.
## HTML
```html
<div class="av-18">
  <button class="av-18__theme" type="button" aria-pressed="false">
    <svg class="av-18__i av-18__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-18__i av-18__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-18__vh">Toggle dark theme</span>
  </button>

  <div class="av-18__stage">
    <section class="av-18__wrap" aria-labelledby="av-18-h">
      <header class="av-18__head">
        <p class="av-18__eyebrow">Account · Profile photo</p>
        <h2 class="av-18__h" id="av-18-h">Change photo affordance</h2>
        <p class="av-18__sub">Hover or tab to the avatar. The control is a real file input in its label.</p>
      </header>

      <div class="av-18__panel">
        <label class="av-18__drop">
          <input class="av-18__file" type="file" accept="image/*" id="av-18-file">
          <span class="av-18__init" style="--h:96" aria-hidden="true">MO</span>
          <img class="av-18__img" id="av-18-img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=320&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="320" height="320" decoding="async">
          <span class="av-18__scrim" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 8.5A2.5 2.5 0 0 1 6.5 6h1.2l1-1.6h4.6L14.3 6h3.2A2.5 2.5 0 0 1 20 8.5v8A2.5 2.5 0 0 1 17.5 19h-11A2.5 2.5 0 0 1 4 16.5z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="12" cy="12.5" r="3.2" stroke="currentColor" stroke-width="1.7"/></svg>
            <span class="av-18__scrimtext">Change</span>
          </span>
          <span class="av-18__vh">Change your profile photo</span>
        </label>

        <div class="av-18__info">
          <p class="av-18__name">Maya Okonkwo</p>
          <p class="av-18__role">Design systems · Northwind</p>
          <p class="av-18__hint">Square JPG or PNG, at least 400×400. Shown at 40px in most places.</p>
          <div class="av-18__btns">
            <label class="av-18__btn">
              <input class="av-18__file" type="file" accept="image/*" id="av-18-file2">
              Upload new photo
            </label>
            <button class="av-18__btn av-18__btn--ghost" type="button" id="av-18-remove">Remove</button>
          </div>
          <p class="av-18__live" id="av-18-live" aria-live="polite">Using your current photo.</p>
        </div>
      </div>

      <ul class="av-18__sizes">
        <li class="av-18__size"><span class="av-18__mini"><img class="av-18__miniimg" id="av-18-m1" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async"></span>24px</li>
        <li class="av-18__size"><span class="av-18__mini av-18__mini--md"><img class="av-18__miniimg" id="av-18-m2" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async"></span>40px</li>
        <li class="av-18__size"><span class="av-18__mini av-18__mini--lg"><img class="av-18__miniimg" id="av-18-m3" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async"></span>64px</li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-18 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }

  .av-18__init {
    background: oklch(93% .055 var(--h));
    color: oklch(44% .13 var(--h));
  }
}

.av-18 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --size: clamp(6.5rem,20vw,9.5rem);
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

.av-18 *,
.av-18 *::before,
.av-18 *::after {
  box-sizing: border-box;
}

.av-18__vh {
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

.av-18__theme {
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

.av-18__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-18__theme:hover {
  translate: 0 -1px;
}

.av-18__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-18__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-18__i--sun {
  display: none;
}

.av-18[data-theme="dark"] .av-18__i--moon {
  display: none;
}

.av-18[data-theme="dark"] .av-18__i--sun {
  display: block;
}

.av-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-18__wrap {
  inline-size: min(54rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.6rem);
}

.av-18__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-18__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-18__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-18__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-18__panel {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: clamp(1.5rem,4vw,2.75rem);
  padding: clamp(1.5rem,4vw,2.25rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-18__drop {
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  flex: none;
  border-radius: 50%;
  overflow: hidden;
  cursor: pointer;
  background: var(--panel-2);
  box-shadow: 0 0 0 1px rgba(16,19,26,.08);
  transition: translate .22s cubic-bezier(.2,.7,.3,1), box-shadow .22s ease;
}

.av-18__drop:hover {
  translate: 0 -2px;
}

.av-18__drop:focus-within {
  box-shadow: 0 0 0 3px var(--panel), 0 0 0 5px var(--accent);
}

.av-18__file {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
  inset-block-start: 50%;
  inset-inline-start: 50%;
}

.av-18__init {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  background: hsl(var(--h) 72% 92%);
  color: hsl(var(--h) 55% 30%);
  font-size: calc(var(--size) * .3);
  font-weight: 700;
}

.av-18__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  object-position: center top;
  transition: opacity .25s ease;
}

.av-18__drop[data-empty="true"] .av-18__img {
  opacity: 0;
}

.av-18__scrim {
  position: absolute;
  inset: 0;
  z-index: 2;
  display: grid;
  place-items: center;
  align-content: center;
  gap: .2rem;
  background: linear-gradient(to top, rgba(8,10,14,.82), rgba(8,10,14,.42));
  color: #fff;
  opacity: 0;
  transition: opacity .22s ease;
}

@supports ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .av-18__scrim {
    -webkit-backdrop-filter: blur(1.5px);
    backdrop-filter: blur(1.5px);
  }
}

.av-18__scrim svg {
  inline-size: calc(var(--size) * .24);
  block-size: calc(var(--size) * .24);
}

.av-18__scrimtext {
  font-size: calc(var(--size) * .1);
  font-weight: 650;
  letter-spacing: .01em;
}

.av-18__drop:hover .av-18__scrim,
.av-18__drop:focus-within .av-18__scrim {
  opacity: 1;
}

.av-18__info {
  display: flex;
  flex-direction: column;
  gap: .35rem;
  min-inline-size: min(18rem,100%);
  flex: 1;
}

.av-18__name {
  margin: 0;
  font-size: clamp(1.15rem,3vw,1.5rem);
  font-weight: 650;
  letter-spacing: -.025em;
}

.av-18__role {
  margin: 0;
  font-size: .88rem;
  color: var(--muted);
}

.av-18__hint {
  margin: .35rem 0 .5rem;
  font-size: .82rem;
  color: var(--muted);
  text-wrap: pretty;
}

.av-18__btns {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.av-18__btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0 1rem;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--ink);
  color: var(--panel);
  font-size: .86rem;
  font-weight: 600;
  cursor: pointer;
  transition: translate .16s ease, opacity .16s ease;
}

.av-18__btn:hover {
  translate: 0 -1px;
  opacity: .93;
}

.av-18__btn--ghost {
  background: transparent;
  color: var(--muted);
}

.av-18__btn:focus-within,
.av-18__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-18__live {
  margin: .35rem 0 0;
  font-size: .8rem;
  color: var(--muted);
}

.av-18__sizes {
  list-style: none;
  margin: 0;
  padding: .9rem 1.15rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1.25rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  font-size: .78rem;
  color: var(--muted);
}

.av-18__size {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.av-18__mini {
  display: block;
  inline-size: 1.5rem;
  aspect-ratio: 1;
  border-radius: 50%;
  overflow: hidden;
  background: var(--panel-2);
  flex: none;
}

.av-18__mini--md {
  inline-size: 2.5rem;
}

.av-18__mini--lg {
  inline-size: 4rem;
}

.av-18__miniimg {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  object-position: center top;
}

.av-18[data-theme="dark"] {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-18[data-theme="dark"] .av-18__init {
  background: hsl(var(--h) 42% 22%);
  color: hsl(var(--h) 78% 82%);
}

@media (prefers-color-scheme: dark) {
  .av-18:not([data-theme="light"]) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-18:not([data-theme="light"]) .av-18__i--moon {
    display: none;
  }

  .av-18:not([data-theme="light"]) .av-18__i--sun {
    display: block;
  }

  .av-18:not([data-theme="light"]) .av-18__init {
    background: hsl(var(--h) 42% 22%);
    color: hsl(var(--h) 78% 82%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-18 *,
    .av-18 *::before,
    .av-18 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-18__scrim {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }

  .av-18__panel,
    .av-18__sizes,
    .av-18__btn,
    .av-18__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const av18 = document.querySelector('.av-18');
const av18img = av18.querySelector('#av-18-img');
const av18live = av18.querySelector('#av-18-live');
const av18minis = [...av18.querySelectorAll('.av-18__miniimg')];
const av18original = av18img.src;
let av18url = null;

const av18set = (src) => { av18img.src = src; av18minis.forEach((m) => (m.src = src)); };

av18.querySelectorAll('.av-18__file').forEach((input) => input.addEventListener('change', () => {
  const file = input.files && input.files[0];
  if (!file) return;
  if (av18url) URL.revokeObjectURL(av18url);
  av18url = URL.createObjectURL(file);
  av18.querySelector('.av-18__drop').dataset.empty = 'false';
  av18set(av18url);
  av18live.textContent = file.name + ' selected. Not saved yet.';
}));

av18.querySelector('#av-18-remove').addEventListener('click', () => {
  if (av18url) { URL.revokeObjectURL(av18url); av18url = null; }
  av18set(av18original);
  av18live.textContent = 'Photo removed. Initials will be shown.';
  av18.querySelector('.av-18__drop').dataset.empty = 'true';
});

av18.querySelector('.av-18__theme').addEventListener('click', (e) => {
  const on = av18.dataset.theme !== 'dark';
  av18.dataset.theme = on ? 'dark' : 'light';
  e.currentTarget.setAttribute('aria-pressed', String(on));
});
```
