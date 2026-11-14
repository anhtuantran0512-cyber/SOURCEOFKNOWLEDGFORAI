---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/rounded-block-footer/"
title: "Rounded Block Footer"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A site footer as one thick-bordered pastel block: four link columns, a newsletter row, social buttons in bordered squares and a bottom bar."
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rounded Block Footer
Source: https://codefronts.com/design-styles/css-brutalist/rounded-block-footer/

A site footer as one thick-bordered pastel block: four link columns, a newsletter row, social buttons in bordered squares and a bottom bar. Radii run 12-16px throughout, which is the clearest demonstration of how neubrutalism's softness separates it from the hard-cornered brutalist half of this collection.
## HTML
```html
<div class="brt-14">
  <input class="brt-14__sr" type="checkbox" id="brt-14-dark">
  <label class="brt-14__theme" for="brt-14-dark">
    <svg class="brt-14__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-14__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-14__vh">Dark theme</span>
  </label>

  <div class="brt-14__stage">
    <footer class="brt-14__block">
      <div class="brt-14__top">
        <div class="brt-14__brandcol">
          <p class="brt-14__brand"><span class="brt-14__mark" aria-hidden="true">P</span>Pagecraft</p>
          <p class="brt-14__pitch">Landing pages you can edit in the browser and hand to engineers as real CSS.</p>
          <ul class="brt-14__social">
            <li><a class="brt-14__icon" href="#brt-14-nl" aria-label="Pagecraft on GitHub"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9.3 20.5v-2.6c-3 .6-3.7-1.3-3.7-1.3-.5-1.2-1.2-1.6-1.2-1.6-1-.7 0-.7 0-.7 1.1.1 1.7 1.2 1.7 1.2 1 1.6 2.5 1.2 3.1.9.1-.7.4-1.2.7-1.5-2.4-.3-4.5-1.2-4.5-5 0-1.1.4-2 1-2.6-.1-.3-.4-1.4.1-2.8 0 0 1-.3 3.3 1a8.4 8.4 0 0 1 4.4 0c2.3-1.3 3.3-1 3.3-1 .5 1.4.2 2.5.1 2.8.6.6 1 1.5 1 2.6 0 3.8-2.1 4.7-4.5 5 .4.4.8 1.1.8 2.2v3.4" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/></svg></a></li>
            <li><a class="brt-14__icon" href="#brt-14-nl" aria-label="Pagecraft on Mastodon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 8.5c0-2.2 1.6-3.6 3.8-3.9a26 26 0 0 1 7.4 0c2.2.3 3.8 1.7 3.8 3.9v4c0 3.6-2.4 4.5-4.9 4.8-2 .2-3.9.1-5-.2" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M8.4 13.6V9.9c0-1.7 2.3-2 3.1-.5l.5 1 .5-1c.8-1.5 3.1-1.2 3.1.5v3.7M6.5 18.8c1.8 1 4.4 1.2 6.5.7" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></a></li>
            <li><a class="brt-14__icon" href="#brt-14-nl" aria-label="Pagecraft on YouTube"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="3" y="6" width="18" height="12" rx="3" stroke="currentColor" stroke-width="1.9"/><path d="M11 9.6l4 2.4-4 2.4z" fill="currentColor"/></svg></a></li>
            <li><a class="brt-14__icon" href="#brt-14-nl" aria-label="Pagecraft RSS feed"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="6.5" cy="17.5" r="1.8" fill="currentColor"/><path d="M5 5a14 14 0 0 1 14 14M5 10.5a8.5 8.5 0 0 1 8.5 8.5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></a></li>
          </ul>
        </div>

        <div class="brt-14__cols">
          <nav class="brt-14__col" aria-labelledby="brt-14-c1">
            <h2 class="brt-14__ch" id="brt-14-c1">Product</h2>
            <ul><li><a href="#brt-14-nl">Editor</a></li><li><a href="#brt-14-nl">Templates</a></li><li><a href="#brt-14-nl">Integrations</a></li><li><a href="#brt-14-nl">Changelog</a></li></ul>
          </nav>
          <nav class="brt-14__col" aria-labelledby="brt-14-c2">
            <h2 class="brt-14__ch" id="brt-14-c2">Developers</h2>
            <ul><li><a href="#brt-14-nl">Docs</a></li><li><a href="#brt-14-nl">CLI</a></li><li><a href="#brt-14-nl">API status</a></li><li><a href="#brt-14-nl">Self-host</a></li></ul>
          </nav>
          <nav class="brt-14__col" aria-labelledby="brt-14-c3">
            <h2 class="brt-14__ch" id="brt-14-c3">Company</h2>
            <ul><li><a href="#brt-14-nl">About</a></li><li><a href="#brt-14-nl">Careers</a></li><li><a href="#brt-14-nl">Field notes</a></li><li><a href="#brt-14-nl">Press kit</a></li></ul>
          </nav>
          <nav class="brt-14__col" aria-labelledby="brt-14-c4">
            <h2 class="brt-14__ch" id="brt-14-c4">Legal</h2>
            <ul><li><a href="#brt-14-nl">Terms</a></li><li><a href="#brt-14-nl">Privacy</a></li><li><a href="#brt-14-nl">DPA</a></li><li><a href="#brt-14-nl">Sub-processors</a></li></ul>
          </nav>
        </div>
      </div>

      <div class="brt-14__nl" id="brt-14-nl">
        <div>
          <h2 class="brt-14__nlh">One email a month</h2>
          <p class="brt-14__nlp">New templates, CSS notes, no growth hacks.</p>
        </div>
        <div class="brt-14__field">
          <label class="brt-14__vh" for="brt-14-email">Email address</label>
          <input class="brt-14__input" id="brt-14-email" type="email" inputmode="email" autocomplete="email" placeholder="[email protected]">
          <button class="brt-14__send" type="button">Subscribe</button>
        </div>
      </div>

      <div class="brt-14__bottom">
        <p>© 2026 Pagecraft Ltd · Bristol, UK</p>
        <ul class="brt-14__meta">
          <li><a href="#brt-14-nl">Status: all systems normal</a></li>
          <li><a href="#brt-14-nl">Cookie choices</a></li>
        </ul>
      </div>
    </footer>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-14 {
  --page: #f7f4ec;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 16px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Space Grotesk','Sora',ui-sans-serif,system-ui,sans-serif;
}

.brt-14 *,
.brt-14 *::before,
.brt-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-14 {
    --page: oklch(0.968 0.016 88);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-14__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-14__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-14__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-14__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-14__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-14__sr:focus-visible + .brt-14__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-14__sun {
  display: none;
}

.brt-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3rem);
}

.brt-14__block {
  inline-size: min(74rem,100%);
  padding: clamp(1.35rem,3vw,2.25rem);
  background: var(--lilac);
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 8px 8px 0 var(--sh);
}

.brt-14__top {
  display: grid;
  gap: clamp(1.5rem,3.5vw,2.5rem);
  grid-template-columns: minmax(0,1fr);
}

@media (min-width: 56rem) {
  .brt-14__top {
    grid-template-columns: 18rem minmax(0,1fr);
  }
}

.brt-14__brand {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -.02em;
}

.brt-14__mark {
  display: grid;
  place-items: center;
  inline-size: 2.1rem;
  block-size: 2.1rem;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: calc(var(--r) - var(--bw) - 3px);
  font-size: 1rem;
}

.brt-14__pitch {
  margin: .7rem 0 1.1rem;
  max-inline-size: 28ch;
  font-size: .92rem;
  line-height: 1.5;
  opacity: .8;
  text-wrap: pretty;
}

.brt-14__social {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: .6rem;
}

.brt-14__icon {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 11px;
  box-shadow: 3px 3px 0 var(--sh);
  transition: translate .13s ease, box-shadow .13s ease, background .13s ease;
}

.brt-14__icon svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
}

.brt-14__icon:hover {
  background: var(--butter);
  translate: -1px -1px;
  box-shadow: 5px 5px 0 var(--sh);
}

.brt-14__icon:active {
  translate: 2px 2px;
  box-shadow: 1px 1px 0 var(--sh);
}

.brt-14__icon:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-14__cols {
  display: grid;
  gap: 1.25rem 1.5rem;
  grid-template-columns: repeat(auto-fit,minmax(min(8.5rem,100%),1fr));
}

.brt-14__ch {
  margin: 0 0 .7rem;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  opacity: .75;
}

.brt-14__col ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .15rem;
}

.brt-14__col a {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.25rem;
  color: var(--on);
  font-size: .95rem;
  font-weight: 600;
  text-decoration: none;
}

.brt-14__col a:hover {
  text-decoration: 3px underline currentColor;
  text-underline-offset: 4px;
}

.brt-14__col a:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
  border-radius: 4px;
}

.brt-14__nl {
  display: flex;
  flex-wrap: wrap;
  gap: 1.1rem;
  align-items: center;
  justify-content: space-between;
  margin-block: clamp(1.5rem,3.5vw,2.25rem);
  padding: clamp(1.1rem,2.4vw,1.5rem);
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: calc(var(--r) - var(--bw));
  box-shadow: 5px 5px 0 var(--sh);
}

.brt-14__nlh {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: -.02em;
}

.brt-14__nlp {
  margin: .25rem 0 0;
  font-size: .9rem;
  color: var(--muted);
}

.brt-14__field {
  display: flex;
  flex: 1 1 min(18rem,100%);
  min-inline-size: 0;
  max-inline-size: 26rem;
}

.brt-14__input {
  flex: 1;
  min-inline-size: 0;
  min-block-size: 3rem;
  padding: .75rem .9rem;
  font: inherit;
  font-size: 1rem;
  color: var(--ink);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-inline-end: 0;
  border-start-start-radius: 11px;
  border-end-start-radius: 11px;
  border-start-end-radius: 0;
  border-end-end-radius: 0;
}

.brt-14__input::placeholder {
  color: var(--muted);
}

.brt-14__input:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: -3px;
}

.brt-14__send {
  min-block-size: 3rem;
  padding: .75rem 1.15rem;
  font: inherit;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  background: var(--ink);
  color: var(--panel);
  border: var(--bw) solid var(--edge);
  border-start-end-radius: 11px;
  border-end-end-radius: 11px;
  border-start-start-radius: 0;
  border-end-start-radius: 0;
  transition: translate .13s ease, box-shadow .13s ease;
}

.brt-14__send:active {
  translate: 2px 2px;
}

.brt-14__send:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-14__bottom {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem 1.5rem;
  align-items: center;
  justify-content: space-between;
  padding-block-start: 1.1rem;
  border-block-start: var(--bw) solid var(--edge);
  font-size: .86rem;
}

.brt-14__bottom p {
  margin: 0;
  opacity: .8;
}

.brt-14__meta {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .4rem 1.25rem;
}

.brt-14__meta a {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.25rem;
  color: var(--on);
  font-weight: 600;
  text-decoration: 3px underline transparent;
  text-underline-offset: 4px;
}

.brt-14__meta a:hover {
  text-decoration-color: currentColor;
}

.brt-14__meta a:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
  border-radius: 4px;
}

.brt-14:has(#brt-14-dark:checked) {
  --page: #131218;
  --panel: #221f2b;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-14:has(#brt-14-dark:checked) .brt-14__moon {
  display: none;
}

.brt-14:has(#brt-14-dark:checked) .brt-14__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-14:not(:has(#brt-14-dark:checked)) {
    --page: #131218;
    --panel: #221f2b;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-14:not(:has(#brt-14-dark:checked)) .brt-14__moon {
    display: none;
  }

  .brt-14:not(:has(#brt-14-dark:checked)) .brt-14__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-14 *,
    .brt-14 *::before,
    .brt-14 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-14__block,
    .brt-14__nl,
    .brt-14__icon,
    .brt-14__input,
    .brt-14__send,
    .brt-14__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-14__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
