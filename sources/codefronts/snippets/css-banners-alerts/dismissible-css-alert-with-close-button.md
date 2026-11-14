---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/dismissible-css-alert-with-close-button/"
title: "Newsletter Signup Bar"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "Two lessons in one component."
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Newsletter Signup Bar
Source: https://codefronts.com/snippets/css-banners-alerts/dismissible-css-alert-with-close-button/

Two lessons in one component. First, a close button that needs zero JavaScript: a hidden checkbox plus :has(:checked) removes the bar and animates it out with allow-discrete. Second, validation that only speaks when it should — :user-invalid waits until the field has actually been used, so nobody gets shouted at for an empty input they have not filled in yet.
## HTML
```html
<div class="ba-06">
  <article class="ba-06__reading" aria-hidden="true">
    <p class="ba-06__kicker">Issue 41 · Craft</p>
    <h2>The typeface that survived three bankruptcies</h2>
    <p>Between 1974 and 1991 the foundry changed hands four times, and each new owner tried to modernise the same twelve weights. What is remarkable is not that the family survived, but which parts of it did.</p>
    <p>The italic was cut last, in a rented room above a print shop in Bilbao, by two people who had never met the original designer.</p>
  </article>

  <section class="ba-06__bar" role="region" aria-labelledby="ba-06-h">
    <input class="ba-06__vh" type="checkbox" id="ba-06-x">
    <div class="ba-06__inner" data-state="ask">
      <div class="ba-06__pitch">
        <p class="ba-06__eyebrow">The Slab · weekly</p>
        <h2 class="ba-06__h" id="ba-06-h">One long read about type and printing, every Thursday.</h2>
        <p class="ba-06__note">9,400 designers. No sponsors, no tracking pixels, one click to leave.</p>
      </div>

      <div class="ba-06__form">
        <div class="ba-06__field">
          <label class="ba-06__vh" for="ba-06-email">Email address</label>
          <input id="ba-06-email" type="email" inputmode="email" autocomplete="email" required
                 placeholder="[email protected]" aria-describedby="ba-06-hint ba-06-err" data-email>
          <svg class="ba-06__tick" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m5 10.5 3.2 3.2L15 6.8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <p class="ba-06__err" id="ba-06-err">Enter an address like [email protected]</p>
        </div>
        <button class="ba-06__go" type="button" data-go>
          Subscribe
          <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M4 10h11m-4.4-4.4L15 10l-4.4 4.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <p class="ba-06__hint" id="ba-06-hint">
          <label class="ba-06__consent"><input type="checkbox" data-consent><span aria-hidden="true"></span>Email me the weekly issue and nothing else.</label>
        </p>
      </div>
    </div>

    <div class="ba-06__done" data-done hidden>
      <span class="ba-06__doneMark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="m6 12.5 4 4 8.5-9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <p><strong data-doneline>Check your inbox.</strong> Confirm the double opt-in and issue 41 lands on Thursday.</p>
    </div>

    <label class="ba-06__x" for="ba-06-x" tabindex="0" role="button" aria-label="Dismiss newsletter bar">
      <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m6 6 8 8m0-8-8 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
    </label>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400;12..96,600;12..96,800&family=Instrument+Sans:wght@400;500;600&display=swap');

.ba-06 {
  --bar-align: space-between;
  --paper: #f7f4ec;
  --ink: #181510;
  --bar: #181510;
  --bar-ink: #f9f7f1;
  --muted: #8b8478;
  --line: #e4dece;
  --acc: #ff5c2b;
  --good: #1f9d55;
  --bad: #ff6b5e;
  --display: "Bricolage Grotesque",ui-sans-serif,system-ui,sans-serif;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,sans-serif;
  container-type: inline-size;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  overflow: clip;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-06 *,
.ba-06 *::before,
.ba-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-06 {
    --paper: oklch(96.5% .014 88);
    --ink: oklch(18% .014 65);
    --bar: oklch(18% .014 65);
    --muted: oklch(59% .014 70);
    --line: oklch(90% .016 85);
    --acc: oklch(66% .2 38);
    --good: oklch(60% .15 150);
    --bad: oklch(68% .19 25);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-06:not([data-theme="light"]) {
    --paper: #0e0d0b;
    --ink: #f5f2ea;
    --bar: #1b1815;
    --bar-ink: #f5f2ea;
    --muted: #9b938a;
    --line: #292420;
  }
}

.ba-06[data-theme="dark"] {
  --paper: #0e0d0b;
  --ink: #f5f2ea;
  --bar: #1b1815;
  --bar-ink: #f5f2ea;
  --muted: #9b938a;
  --line: #292420;
}

.ba-06__reading {
  max-width: 38rem;
  margin-inline: auto;
  padding: clamp(2rem,7vh,4.5rem) clamp(1.25rem,5vw,2rem) clamp(14rem,30vh,20rem);
  display: grid;
  gap: 1rem;
}

.ba-06__kicker {
  margin: 0;
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.ba-06__reading h2 {
  margin: 0;
  font-family: var(--display);
  font-size: clamp(1.75rem,6cqw,2.75rem);
  font-weight: 800;
  line-height: 1.02;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.ba-06__reading p:not(.ba-06__kicker) {
  margin: 0;
  font-size: 1.0625rem;
  line-height: 1.65;
  color: var(--muted);
  max-width: 64ch;
  text-wrap: pretty;
}

.ba-06__bar {
  position: fixed;
  z-index: 5;
  inset: auto 0 0 0;
  display: flex;
  align-items: center;
  justify-content: var(--bar-align);
  gap: clamp(1rem,4cqw,3rem);
  padding: clamp(1rem,2.5vw,1.4rem) clamp(1rem,4vw,2.25rem);
  background: var(--bar);
  color: var(--bar-ink);
  border-block-start: 3px solid var(--acc);
  box-shadow: 0 -1.5rem 3rem -2rem rgb(0 0 0 / .5);
  transition: opacity .35s ease, translate .4s cubic-bezier(.16,1,.3,1), display .4s allow-discrete;
}

.ba-06__bar::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: .5;
  background-image: radial-gradient(currentColor .5px, transparent .5px);
  background-size: 14px 14px;
  color: color-mix(in oklab,var(--bar-ink) 12%,transparent);
  mask-image: linear-gradient(100deg,black,transparent 62%);
}

.ba-06__bar:has(#ba-06-x:checked) {
  opacity: 0;
  translate: 0 1.5rem;
  display: none;
}

.ba-06__inner {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: clamp(1rem,4cqw,3rem);
  flex: 1;
  flex-wrap: wrap;
}

.ba-06__inner[hidden] {
  display: none;
}

.ba-06__pitch {
  min-width: 0;
  display: grid;
  gap: .3rem;
  max-width: 34rem;
}

.ba-06__eyebrow {
  margin: 0;
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.ba-06__h {
  margin: 0;
  font-family: var(--display);
  font-size: clamp(1.0625rem,2.4cqw,1.4375rem);
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ba-06__note {
  margin: 0;
  font-size: .75rem;
  color: color-mix(in oklab,var(--bar-ink) 62%,transparent);
}

.ba-06__form {
  display: grid;
  grid-template-columns: minmax(12rem,20rem) auto;
  gap: .5rem;
  align-items: start;
}

.ba-06__field {
  position: relative;
  --ring: color-mix(in oklab,var(--bar-ink) 24%,transparent);
}

.ba-06__field input {
  width: 100%;
  min-inline-size: 12rem;
  min-height: 2.9rem;
  padding: .75rem 2.4rem .75rem .9rem;
  font: inherit;
  font-size: .9375rem;
  color: var(--bar-ink);
  border-radius: .8rem;
  background: color-mix(in oklab,var(--bar-ink) 8%,transparent);
  border: 1.5px solid var(--ring);
  transition: border-color .2s ease, background .2s ease;
}

@supports (field-sizing: content) {
  .ba-06__field input {
    field-sizing: content;
    max-inline-size: 22rem;
  }
}

.ba-06__field input::placeholder {
  color: color-mix(in oklab,var(--bar-ink) 42%,transparent);
}

.ba-06__field input:focus {
  outline: 0;
  border-color: var(--acc);
  background: color-mix(in oklab,var(--bar-ink) 12%,transparent);
}

.ba-06__field:has(input:user-invalid) {
  --ring: var(--bad);
}

.ba-06__field:has(input:user-valid) {
  --ring: var(--good);
}

.ba-06__tick {
  position: absolute;
  inset-inline-end: .85rem;
  inset-block-start: .95rem;
  width: 1.1rem;
  height: 1.1rem;
  color: var(--good);
  scale: 0;
  transition: scale .3s cubic-bezier(.34,1.56,.64,1);
}

.ba-06__field:has(input:user-valid) .ba-06__tick {
  scale: 1;
}

.ba-06__err {
  display: none;
  margin: .4rem 0 0;
  font-size: .75rem;
  font-weight: 600;
  color: var(--bad);
}

.ba-06__field:has(input:user-invalid) .ba-06__err {
  display: block;
}

.ba-06__go {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.9rem;
  padding: .75rem 1.25rem;
  border: 0;
  border-radius: .8rem;
  cursor: pointer;
  font: inherit;
  font-size: .9375rem;
  font-weight: 600;
  font-family: var(--display);
  letter-spacing: -.02em;
  background: var(--acc);
  color: #fff;
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .2s ease, background .2s ease;
}

.ba-06__go svg {
  width: 1.0625rem;
  height: 1.0625rem;
  transition: translate .25s cubic-bezier(.16,1,.3,1);
}

.ba-06__go:hover {
  translate: 0 -1px;
  box-shadow: 0 .7rem 1.5rem -.7rem color-mix(in oklab,var(--acc) 75%,transparent);
}

.ba-06__go:hover svg {
  translate: .2rem 0;
}

.ba-06__hint {
  grid-column: 1 / -1;
  margin: .15rem 0 0;
}

.ba-06__consent {
  display: flex;
  align-items: center;
  gap: .45rem;
  min-height: 1.75rem;
  cursor: pointer;
  font-size: .6875rem;
  color: color-mix(in oklab,var(--bar-ink) 58%,transparent);
}

.ba-06__consent input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.ba-06__consent span {
  display: grid;
  place-items: center;
  width: 1rem;
  height: 1rem;
  flex: none;
  border-radius: .3rem;
  border: 1.5px solid color-mix(in oklab,var(--bar-ink) 30%,transparent);
  transition: background .2s ease, border-color .2s ease;
}

.ba-06__consent input:checked + span {
  background: var(--acc);
  border-color: var(--acc);
}

.ba-06__consent input:checked + span::after {
  content: "";
  width: .3rem;
  height: .55rem;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  rotate: 45deg;
  translate: 0 -1px;
}

.ba-06__consent input:focus-visible + span {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-06__done {
  display: flex;
  align-items: center;
  gap: .85rem;
  flex: 1;
  font-size: .9375rem;
  line-height: 1.5;
  color: color-mix(in oklab,var(--bar-ink) 78%,transparent);
  transition: opacity .3s ease, translate .3s ease;
}

.ba-06__done[hidden] {
  display: none;
}

@starting-style {
  .ba-06__done {
    opacity: 0;
    translate: 0 .5rem;
  }
}

.ba-06__done strong {
  color: var(--bar-ink);
  font-family: var(--display);
  font-weight: 600;
}

.ba-06__doneMark {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  flex: none;
  border-radius: 999px;
  color: var(--good);
  background: color-mix(in oklab,var(--good) 16%,transparent);
  border: 1px solid color-mix(in oklab,var(--good) 34%,transparent);
}

.ba-06__doneMark svg {
  width: 1.35rem;
  height: 1.35rem;
}

.ba-06__x {
  display: grid;
  place-items: center;
  width: 2.75rem;
  height: 2.75rem;
  flex: none;
  border-radius: .75rem;
  cursor: pointer;
  color: color-mix(in oklab,var(--bar-ink) 55%,transparent);
  border: 1px solid transparent;
  transition: color .2s ease, background .2s ease;
}

.ba-06__x:hover {
  color: var(--bar-ink);
  background: color-mix(in oklab,var(--bar-ink) 10%,transparent);
}

.ba-06__x svg {
  width: 1.125rem;
  height: 1.125rem;
}

.ba-06__x:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-06__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ba-06 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-06 a {
  color: var(--acc);
}

.ba-06 a:hover {
  color: color-mix(in oklab,var(--acc) 70%,var(--ink));
}

@container (max-width: 56rem) {
  .ba-06__inner {
    flex-direction: column;
    align-items: stretch;
  }

  .ba-06__form {
    grid-template-columns: 1fr auto;
  }
}

@container (max-width: 30rem) {
  .ba-06__form {
    grid-template-columns: 1fr;
  }

  .ba-06__go {
    justify-content: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-06 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-06__bar {
    border: 1px solid CanvasText;
  }

  .ba-06__go {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-06');
  if (!root) return;
  const ask = root.querySelector('.ba-06__inner');
  const done = root.querySelector('[data-done]');
  const email = root.querySelector('[data-email]');

  root.querySelector('[data-go]').addEventListener('click', () => {
    if (!email.checkValidity()) { email.focus(); email.reportValidity?.(); return; }
    root.querySelector('[data-doneline]').textContent = 'Check ' + email.value + '.';
    ask.hidden = true; done.hidden = false;
    done.setAttribute('tabindex', '-1'); done.focus();
  });
  // keyboard parity for the CSS-only close label
  root.querySelector('.ba-06__x').addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); root.querySelector('#ba-06-x').checked = true; }
  });
})();
```
