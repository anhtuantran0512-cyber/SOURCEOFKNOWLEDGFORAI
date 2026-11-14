---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/noir-editorial/"
title: "Editorial Mega Menu with Featured Image"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Publication navigation: section columns beside a featured article card with an image, an eyebrow and a headline."
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Mega Menu with Featured Image
Source: https://codefronts.com/navigation/css-mega-menus/noir-editorial/

Publication navigation: section columns beside a featured article card with an image, an eyebrow and a headline. The image column is the real layout challenge &mdash; an unconstrained image dictates the panel's height, so the card is given a fixed aspect ratio and the link columns are allowed to set the height instead. Rebuilt from the ground up for v2.
## HTML
```html
<section class="mm-15" aria-labelledby="mm-15-title">
  <h2 class="mm-15__sr" id="mm-15-title">The Meridian Review</h2>

  <div class="mm-15__theme">
    <input class="mm-15__theme-input" type="checkbox" id="mm-15-theme">
    <label class="mm-15__theme-label" for="mm-15-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-15__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-15__masthead">
    <p class="mm-15__dateline">Friday, 28 August 2026 &middot; Late edition</p>
    <p class="mm-15__logo">The Meridian Review</p>
    <p class="mm-15__strap">Reporting from 24 bureaux</p>
  </header>

  <header class="mm-15__header">
    <nav class="mm-15__nav" aria-label="Primary">
      <ul class="mm-15__list">
        <li class="mm-15__item">
          <button class="mm-15__trigger" type="button" id="mm-15-trigger-sections" aria-expanded="false" aria-controls="mm-15-panel-sections">Sections</button>
          <div class="mm-15__panel" id="mm-15-panel-sections" aria-labelledby="mm-15-trigger-sections">
            <div class="mm-15__panel-inner">
              <section class="mm-15__col" aria-labelledby="mm-15-h-news">
                <h3 class="mm-15__col-head" id="mm-15-h-news">News</h3>
                <ul class="mm-15__links"><li><a href="#mm-15-title">Politics</a></li><li><a href="#mm-15-title">Economy</a></li><li><a href="#mm-15-title">Cities</a></li><li><a href="#mm-15-title">Climate</a></li><li><a href="#mm-15-title">Investigations</a></li></ul>
              </section>
              <section class="mm-15__col" aria-labelledby="mm-15-h-culture">
                <h3 class="mm-15__col-head" id="mm-15-h-culture">Culture</h3>
                <ul class="mm-15__links"><li><a href="#mm-15-title">Books</a></li><li><a href="#mm-15-title">Film</a></li><li><a href="#mm-15-title">Architecture</a></li><li><a href="#mm-15-title">Food</a></li></ul>
              </section>
              <section class="mm-15__col" aria-labelledby="mm-15-h-opinion">
                <h3 class="mm-15__col-head" id="mm-15-h-opinion">Opinion</h3>
                <ul class="mm-15__links"><li><a href="#mm-15-title">Columnists</a></li><li><a href="#mm-15-title">Letters</a></li><li><a href="#mm-15-title">The long read</a></li></ul>
              </section>

              <article class="mm-15__feature">
                <a class="mm-15__feature-link" href="#mm-15-title">
                  <img class="mm-15__feature-img" src="https://picsum.photos/seed/meridian-harbour/640/400" alt="Cranes above a container terminal at dusk" width="640" height="400" loading="lazy" decoding="async">
                  <p class="mm-15__eyebrow">The long read</p>
                  <h3 class="mm-15__headline">The port that rebuilt itself twice in a decade</h3>
                  <p class="mm-15__byline">Priya Sharma &middot; 18 min read</p>
                </a>
              </article>
            </div>
          </div>
        </li>

        <li class="mm-15__item">
          <button class="mm-15__trigger" type="button" id="mm-15-trigger-more" aria-expanded="false" aria-controls="mm-15-panel-more">More</button>
          <div class="mm-15__panel" id="mm-15-panel-more" aria-labelledby="mm-15-trigger-more">
            <div class="mm-15__panel-inner">
              <section class="mm-15__col" aria-labelledby="mm-15-h-audio">
                <h3 class="mm-15__col-head" id="mm-15-h-audio">Audio</h3>
                <ul class="mm-15__links"><li><a href="#mm-15-title">Daily briefing</a></li><li><a href="#mm-15-title">The interview</a></li><li><a href="#mm-15-title">Archive tapes</a></li></ul>
              </section>
              <section class="mm-15__col" aria-labelledby="mm-15-h-news2">
                <h3 class="mm-15__col-head" id="mm-15-h-news2">Newsletters</h3>
                <ul class="mm-15__links"><li><a href="#mm-15-title">Morning edition</a></li><li><a href="#mm-15-title">Markets</a></li><li><a href="#mm-15-title">Weekend</a></li></ul>
              </section>
              <section class="mm-15__col" aria-labelledby="mm-15-h-paper">
                <h3 class="mm-15__col-head" id="mm-15-h-paper">The paper</h3>
                <ul class="mm-15__links"><li><a href="#mm-15-title">Today's front page</a></li><li><a href="#mm-15-title">Archive</a></li></ul>
              </section>
              <article class="mm-15__feature">
                <a class="mm-15__feature-link" href="#mm-15-title">
                  <img class="mm-15__feature-img" src="https://picsum.photos/seed/meridian-studio/640/400" alt="A recording studio desk lit by a single lamp" width="640" height="400" loading="lazy" decoding="async">
                  <p class="mm-15__eyebrow">New series</p>
                  <h3 class="mm-15__headline">Six weeks inside the coastal defence review</h3>
                  <p class="mm-15__byline">Jordan Lee &middot; 6 episodes</p>
                </a>
              </article>
            </div>
          </div>
        </li>

        <li class="mm-15__item"><a class="mm-15__plain" href="#mm-15-title">Newsletters</a></li>
        <li class="mm-15__item"><a class="mm-15__plain" href="#mm-15-title">Podcasts</a></li>
        <li class="mm-15__item"><a class="mm-15__plain mm-15__plain--sub" href="#mm-15-title">Subscribe</a></li>
      </ul>
    </nav>
  </header>

  <main class="mm-15__page">
    <article class="mm-15__story">
      <p class="mm-15__kicker">Economy</p>
      <h1 class="mm-15__h1">Freight volumes recover to pre-strike levels, but only on two corridors</h1>
      <p class="mm-15__standfirst">Operators report a fourteen per cent rebound since June, concentrated almost entirely on the eastern routes.</p>
      <p class="mm-15__by">By Alex Chen &middot; 06:00</p>
    </article>
  </main>
</section>
```
## CSS
```css
.mm-15 {
  --mm-15-bg: #f7f4ee;
  --mm-15-surf: #fffdf9;
  --mm-15-line: #ddd6c8;
  --mm-15-ink: #14110d;
  --mm-15-mut: #6b6357;
  --mm-15-acc: #8c1c13;
  --mm-15-acc: oklch(41% 0.16 30);
  --mm-15-rule: 1px;
  --mm-15-font-display: "Iowan Old Style", "Palatino Linotype", Palatino, ui-serif, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-15-bg);
  color: var(--mm-15-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-15 *,
.mm-15 *::before,
.mm-15 *::after {
  box-sizing: border-box;
}

.mm-15 :focus-visible {
  outline: 2px solid var(--mm-15-acc);
  outline-offset: 3px;
}

.mm-15__sr {
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

.mm-15:has(.mm-15__theme-input:checked) {
  --mm-15-bg: #0e0d0b;
  --mm-15-surf: #17150f;
  --mm-15-line: #2e2a22;
  --mm-15-ink: #f4f0e6;
  --mm-15-mut: #a79e8d;
  --mm-15-acc: #e8836f;
  --mm-15-acc: oklch(74% 0.13 32);
}

@media (prefers-color-scheme: dark) {
  .mm-15 {
    --mm-15-bg: #0e0d0b;
    --mm-15-surf: #17150f;
    --mm-15-line: #2e2a22;
    --mm-15-ink: #f4f0e6;
    --mm-15-mut: #a79e8d;
    --mm-15-acc: #e8836f;
    --mm-15-acc: oklch(74% 0.13 32);
  }

  .mm-15:has(.mm-15__theme-input:checked) {
    --mm-15-bg: #f7f4ee;
    --mm-15-surf: #fffdf9;
    --mm-15-line: #ddd6c8;
    --mm-15-ink: #14110d;
    --mm-15-mut: #6b6357;
    --mm-15-acc: #8c1c13;
    --mm-15-acc: oklch(41% 0.16 30);
  }
}

@media (prefers-color-scheme: light) {
  .mm-15:has(.mm-15__theme-input:checked) {
    --mm-15-bg: #0e0d0b;
    --mm-15-surf: #17150f;
    --mm-15-line: #2e2a22;
    --mm-15-ink: #f4f0e6;
    --mm-15-mut: #a79e8d;
    --mm-15-acc: #e8836f;
    --mm-15-acc: oklch(74% 0.13 32);
  }
}

.mm-15__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.25rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-15__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-15__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: var(--mm-15-rule) solid var(--mm-15-line);
  border-radius: 999px;
  background: var(--mm-15-surf);
  color: var(--mm-15-ink);
  cursor: pointer;
}

.mm-15__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-15__theme-input:focus-visible + .mm-15__theme-label {
  outline: 2px solid var(--mm-15-acc);
  outline-offset: 3px;
}

.mm-15__masthead {
  inline-size: min(74rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  justify-items: center;
  gap: 0.3rem;
  padding-block: clamp(2rem, 6vw, 3rem) clamp(0.9rem, 2.5vw, 1.4rem);
  text-align: center;
}

.mm-15__dateline {
  margin: 0;
  font: 500 0.68rem/1 system-ui, sans-serif;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--mm-15-mut);
}

.mm-15__logo {
  margin: 0;
  font: 400 clamp(1.9rem, 7vw, 3.6rem)/1 var(--mm-15-font-display);
  letter-spacing: -0.015em;
}

.mm-15__strap {
  margin: 0;
  font: 400 0.78rem/1 system-ui, sans-serif;
  font-style: italic;
  color: var(--mm-15-mut);
}

.mm-15__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  border-block: var(--mm-15-rule) solid var(--mm-15-ink);
  background: var(--mm-15-surf);
}

.mm-15__nav {
  inline-size: min(74rem, calc(100% - 2rem));
  margin-inline: auto;
}

.mm-15__list {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: clamp(0.25rem, 2vw, 1.5rem);
  list-style: none;
  margin: 0;
  padding: 0;
  min-block-size: 54px;
}

.mm-15__item {
  position: static;
}

.mm-15__trigger,
.mm-15__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.6rem;
  border: 0;
  background: transparent;
  color: var(--mm-15-ink);
  font: 500 0.8rem/1 system-ui, sans-serif;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
}

.mm-15__plain--sub {
  color: var(--mm-15-acc);
  font-weight: 700;
}

.mm-15__item--open > .mm-15__trigger,
.mm-15__item:hover > .mm-15__trigger,
.mm-15__item:focus-within > .mm-15__trigger {
  color: var(--mm-15-acc);
  box-shadow: inset 0 -2px 0 var(--mm-15-acc);
}

.mm-15__plain:hover,
.mm-15__trigger:hover {
  color: var(--mm-15-acc);
}

.mm-15__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-15-surf);
  border-block-end: var(--mm-15-rule) solid var(--mm-15-ink);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 170ms ease, visibility 0s linear 170ms;
}

.mm-15__item--open > .mm-15__panel,
.mm-15__item:focus-within > .mm-15__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-15__item:hover > .mm-15__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-15__panel-inner {
  inline-size: min(74rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 10rem), 1fr));
  gap: clamp(1rem, 3vw, 2.5rem);
  padding-block: clamp(1.1rem, 3vw, 2rem);
}

@media (min-width: 64rem) {
  .mm-15__panel-inner {
    grid-template-columns: repeat(3, minmax(0, 1fr)) 20rem;
  }
}

.mm-15__col {
  min-inline-size: 0;
}

.mm-15__col-head {
  margin: 0 0 0.5rem;
  padding-block-end: 0.4rem;
  border-block-end: var(--mm-15-rule) solid var(--mm-15-line);
  font: 400 1.15rem/1.2 var(--mm-15-font-display);
}

.mm-15__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
}

.mm-15__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-15-ink);
  text-decoration: none;
  font-size: 0.92rem;
  border-block-end: var(--mm-15-rule) dotted var(--mm-15-line);
  min-inline-size: 0;
}

.mm-15__links a:hover {
  color: var(--mm-15-acc);
}

.mm-15__feature {
  align-self: start;
  min-inline-size: 0;
}

.mm-15__feature-link {
  display: grid;
  gap: 0.4rem;
  text-decoration: none;
  color: inherit;
}

.mm-15__feature-img {
  inline-size: 100%;
  block-size: auto;
  aspect-ratio: 16 / 10;
  object-fit: cover;
  background: var(--mm-15-line);
  filter: grayscale(1) contrast(1.05);
}

.mm-15__feature-link:hover .mm-15__feature-img {
  filter: none;
}

.mm-15__eyebrow {
  margin: 0.3rem 0 0;
  font: 700 0.66rem/1 system-ui, sans-serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--mm-15-acc);
}

.mm-15__headline {
  margin: 0;
  font: 400 clamp(1.15rem, 3vw, 1.45rem)/1.15 var(--mm-15-font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.mm-15__feature-link:hover .mm-15__headline {
  text-decoration: underline;
  text-underline-offset: 4px;
}

.mm-15__byline {
  margin: 0;
  font: 400 0.78rem/1 system-ui, sans-serif;
  color: var(--mm-15-mut);
}

.mm-15__page {
  inline-size: min(74rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 8vw, 4.5rem);
}

.mm-15__story {
  max-inline-size: 44rem;
  display: grid;
  gap: 0.5rem;
}

.mm-15__kicker {
  margin: 0;
  font: 700 0.68rem/1 system-ui, sans-serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--mm-15-acc);
}

.mm-15__h1 {
  margin: 0;
  font: 400 clamp(1.8rem, 5.5vw, 3rem)/1.08 var(--mm-15-font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.mm-15__standfirst {
  margin: 0;
  font: 400 clamp(1rem, 2.4vw, 1.2rem)/1.5 var(--mm-15-font-display);
  color: var(--mm-15-mut);
  text-wrap: pretty;
}

.mm-15__by {
  margin: 0.3rem 0 0;
  font: 500 0.76rem/1 system-ui, sans-serif;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mm-15-mut);
}

@media (max-width: 48rem) {
  .mm-15__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    display: none;
  }

  .mm-15__item--open > .mm-15__panel,
    .mm-15__item:focus-within > .mm-15__panel {
    display: block;
  }

  .mm-15__list {
    justify-content: flex-start;
  }

  .mm-15__panel-inner {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-15__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-15__trigger {
    position: relative;
  }

  .mm-15__item:hover > .mm-15__trigger::after,
    .mm-15__item:focus-within > .mm-15__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — headlines rise from behind their own baseline, feature image settles out of an overscale */

.mm-15__feature-link {
  overflow: clip;
}

.mm-15__links li {
  clip-path: inset(115% 0 -8px 0);
  transition: clip-path 460ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-15__item:hover > .mm-15__panel .mm-15__links li,
.mm-15__item:focus-within > .mm-15__panel .mm-15__links li,
.mm-15__item--open > .mm-15__panel .mm-15__links li {
  clip-path: inset(-8px);
}

.mm-15__links li:nth-child(1) {
  transition-delay: 30ms;
}

.mm-15__links li:nth-child(2) {
  transition-delay: 75ms;
}

.mm-15__links li:nth-child(3) {
  transition-delay: 120ms;
}

.mm-15__links li:nth-child(4) {
  transition-delay: 165ms;
}

.mm-15__links li:nth-child(5) {
  transition-delay: 210ms;
}

.mm-15__links li:nth-child(6) {
  transition-delay: 255ms;
}

.mm-15__links li:nth-child(n+7) {
  transition-delay: 255ms;
}

.mm-15__feature-img {
  scale: 1.07;
  transition: scale 760ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-15__item:hover > .mm-15__panel .mm-15__feature-img,
.mm-15__item:focus-within > .mm-15__panel .mm-15__feature-img,
.mm-15__item--open > .mm-15__panel .mm-15__feature-img {
  scale: 1;
}

@media (prefers-reduced-motion: reduce) {
  .mm-15__links li,
    .mm-15__feature-img {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-15__links li {
    clip-path: none;
  }

  .mm-15__feature-img {
    scale: 1;
  }
}
```
