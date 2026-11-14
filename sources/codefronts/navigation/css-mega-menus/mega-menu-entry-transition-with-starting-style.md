---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/mega-menu-entry-transition-with-starting-style/"
title: "Mega Menu Entry Transition with Starting Style"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "An element entering the DOM or coming out of display: none has no previous state to transition from, which is why panel entry animations historically needed…"
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mega Menu Entry Transition with Starting Style
Source: https://codefronts.com/navigation/css-mega-menus/mega-menu-entry-transition-with-starting-style/

An element entering the DOM or coming out of display: none has no previous state to transition from, which is why panel entry animations historically needed a keyframe or a forced reflow. @starting-style declares that before-state and transition-behavior: allow-discrete lets display flip at the end of the exit, so this coffee subscription panel genuinely leaves the layout and still fades out.
## HTML
```html
<section class="mm-13" aria-labelledby="mm-13-title">
  <h2 class="mm-13__sr" id="mm-13-title">Sable Coffee Roasters</h2>

  <div class="mm-13__theme">
    <input class="mm-13__theme-input" type="checkbox" id="mm-13-theme">
    <label class="mm-13__theme-label" for="mm-13-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-13__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-13__header">
    <div class="mm-13__bar">
      <a class="mm-13__brand" href="#mm-13-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 9h11v6a4 4 0 0 1-4 4H9a4 4 0 0 1-4-4Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M16 11h2.5a2.5 2.5 0 0 1 0 5H16" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8 3v3m4-3v3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        Sable
      </a>

      <nav class="mm-13__nav" aria-label="Primary">
        <ul class="mm-13__list">
          <li class="mm-13__item">
            <button class="mm-13__trigger" type="button" aria-expanded="false" aria-controls="mm-13-panel-coffee">Coffee</button>
            <div class="mm-13__panel" id="mm-13-panel-coffee" aria-label="Coffee">
              <div class="mm-13__half">
                <h3 class="mm-13__half-head">Single origin</h3>
                <ul class="mm-13__links">
                  <li><a href="#mm-13-title"><b>Yirgacheffe</b><span>Jasmine, bergamot</span></a></li>
                  <li><a href="#mm-13-title"><b>Huila</b><span>Red apple, cane sugar</span></a></li>
                  <li><a href="#mm-13-title"><b>Antigua</b><span>Cocoa, orange peel</span></a></li>
                  <li><a href="#mm-13-title"><b>Kirinyaga</b><span>Blackcurrant</span></a></li>
                </ul>
              </div>
              <div class="mm-13__half mm-13__half--alt">
                <h3 class="mm-13__half-head">Blends and gear</h3>
                <ul class="mm-13__links">
                  <li><a href="#mm-13-title"><b>Morning house</b><span>Everyday filter</span></a></li>
                  <li><a href="#mm-13-title"><b>Espresso No.4</b><span>For milk drinks</span></a></li>
                  <li><a href="#mm-13-title"><b>Decaf Vale</b><span>Sugarcane process</span></a></li>
                  <li><a href="#mm-13-title"><b>Brewers and grinders</b><span>Kit and spares</span></a></li>
                </ul>
              </div>
            </div>
          </li>

          <li class="mm-13__item">
            <button class="mm-13__trigger" type="button" aria-expanded="false" aria-controls="mm-13-panel-plans">Subscribe</button>
            <div class="mm-13__panel" id="mm-13-panel-plans" aria-label="Subscribe">
              <div class="mm-13__half">
                <h3 class="mm-13__half-head">Plans</h3>
                <ul class="mm-13__links">
                  <li><a href="#mm-13-title"><b>Weekly</b><span>250g, every Monday</span></a></li>
                  <li><a href="#mm-13-title"><b>Fortnightly</b><span>500g</span></a></li>
                  <li><a href="#mm-13-title"><b>Roaster's choice</b><span>We pick, you brew</span></a></li>
                </ul>
              </div>
              <div class="mm-13__half mm-13__half--alt">
                <h3 class="mm-13__half-head">Manage</h3>
                <ul class="mm-13__links">
                  <li><a href="#mm-13-title"><b>Pause or skip</b><span>Any time</span></a></li>
                  <li><a href="#mm-13-title"><b>Change grind</b><span>Before dispatch</span></a></li>
                  <li><a href="#mm-13-title"><b>Gift a subscription</b><span>3, 6 or 12 months</span></a></li>
                </ul>
              </div>
            </div>
          </li>

          <li class="mm-13__item"><a class="mm-13__plain" href="#mm-13-title">Wholesale</a></li>
          <li class="mm-13__item"><a class="mm-13__plain" href="#mm-13-title">Cafes</a></li>
        </ul>
      </nav>

      <div class="mm-13__utils">
        <a class="mm-13__util" href="#mm-13-title">Account</a>
        <a class="mm-13__cart" href="#mm-13-title">Cart / 2</a>
      </div>
    </div>
  </header>

  <main class="mm-13__page">
    <div class="mm-13__hero">
      <p class="mm-13__kicker">This week on the roaster</p>
      <h1 class="mm-13__h1">Kirinyaga AA<br>washed, 1,780m</h1>
      <p class="mm-13__sub">Roasted Tuesday, shipped Wednesday. 250g from &pound;14.</p>
      <a class="mm-13__cta" href="#mm-13-title">Start a subscription</a>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-13 {
  --mm-13-bg: #f4efe9;
  --mm-13-surf: #fffcf8;
  --mm-13-line: #2b211b;
  --mm-13-soft: #e6dbd0;
  --mm-13-ink: #2b211b;
  --mm-13-mut: #6d5c50;
  --mm-13-acc: #7c4a2d;
  --mm-13-acc: oklch(45% 0.1 50);
  --mm-13-on-acc: #ffffff;
  --mm-13-in: 200ms;
  --mm-13-out: 260ms;
  --mm-13-lift: 8px;
  --mm-13-offset: 6px;
  --mm-13-font-display: "Oswald", "Archivo Narrow", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-13-bg);
  color: var(--mm-13-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-13 *,
.mm-13 *::before,
.mm-13 *::after {
  box-sizing: border-box;
}

.mm-13 :focus-visible {
  outline: 2px solid var(--mm-13-acc);
  outline-offset: 3px;
}

.mm-13__sr {
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

.mm-13:has(.mm-13__theme-input:checked) {
  --mm-13-bg: #130f0c;
  --mm-13-surf: #1c1712;
  --mm-13-line: #efe6dc;
  --mm-13-soft: #2c241d;
  --mm-13-ink: #f4ece3;
  --mm-13-mut: #ab9a8c;
  --mm-13-acc: #e0a878;
  --mm-13-acc: oklch(78% 0.1 58);
  --mm-13-on-acc: #12100e;
}

@media (prefers-color-scheme: dark) {
  .mm-13 {
    --mm-13-bg: #130f0c;
    --mm-13-surf: #1c1712;
    --mm-13-line: #efe6dc;
    --mm-13-soft: #2c241d;
    --mm-13-ink: #f4ece3;
    --mm-13-mut: #ab9a8c;
    --mm-13-acc: #e0a878;
    --mm-13-acc: oklch(78% 0.1 58);
    --mm-13-on-acc: #12100e;
  }

  .mm-13:has(.mm-13__theme-input:checked) {
    --mm-13-bg: #f4efe9;
    --mm-13-surf: #fffcf8;
    --mm-13-line: #2b211b;
    --mm-13-soft: #e6dbd0;
    --mm-13-ink: #2b211b;
    --mm-13-mut: #6d5c50;
    --mm-13-acc: #7c4a2d;
    --mm-13-acc: oklch(45% 0.1 50);
    --mm-13-on-acc: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .mm-13:has(.mm-13__theme-input:checked) {
    --mm-13-bg: #130f0c;
    --mm-13-surf: #1c1712;
    --mm-13-line: #efe6dc;
    --mm-13-soft: #2c241d;
    --mm-13-ink: #f4ece3;
    --mm-13-mut: #ab9a8c;
    --mm-13-acc: #e0a878;
    --mm-13-acc: oklch(78% 0.1 58);
    --mm-13-on-acc: #12100e;
  }
}

.mm-13__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-13__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-13__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 2px solid var(--mm-13-line);
  background: var(--mm-13-surf);
  color: var(--mm-13-ink);
  cursor: pointer;
  box-shadow: 4px 4px 0 var(--mm-13-line);
}

.mm-13__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-13__theme-input:focus-visible + .mm-13__theme-label {
  outline: 2px solid var(--mm-13-acc);
  outline-offset: 3px;
}

.mm-13__header {
  position: relative;
  z-index: 10;
  inline-size: min(72rem, calc(100% - 2rem));
  margin: clamp(1rem, 3vw, 1.75rem) auto 0;
}

.mm-13__bar {
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 1.75rem);
  flex-wrap: wrap;
  min-block-size: 62px;
  padding-inline: 0.85rem 64px;
  background: var(--mm-13-surf);
  border: 2px solid var(--mm-13-line);
  box-shadow: var(--mm-13-offset) var(--mm-13-offset) 0 var(--mm-13-line);
}

.mm-13__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  color: var(--mm-13-ink);
  text-decoration: none;
  font: 600 1.15rem/1 var(--mm-13-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.mm-13__brand svg {
  inline-size: 22px;
  block-size: 22px;
  color: var(--mm-13-acc);
}

.mm-13__nav {
  min-inline-size: 0;
}

.mm-13__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-13__item {
  position: static;
}

.mm-13__trigger,
.mm-13__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.85rem;
  border: 0;
  background: transparent;
  color: var(--mm-13-ink);
  font: 500 0.9rem/1 var(--mm-13-font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
}

.mm-13__item--open > .mm-13__trigger,
.mm-13__item:hover > .mm-13__trigger,
.mm-13__item:focus-within > .mm-13__trigger {
  background: var(--mm-13-ink);
  color: var(--mm-13-surf);
}

.mm-13__plain:hover,
.mm-13__trigger:hover {
  color: var(--mm-13-acc);
}

.mm-13__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.mm-13__util {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.5rem;
  color: var(--mm-13-mut);
  text-decoration: none;
  font: 500 0.78rem/1 var(--mm-13-font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.mm-13__cart {
  display: inline-flex;
  align-items: center;
  min-block-size: 36px;
  padding-inline: 0.8rem;
  border: 2px solid var(--mm-13-line);
  color: var(--mm-13-ink);
  text-decoration: none;
  font: 600 0.76rem/1 var(--mm-13-font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.mm-13__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  border: 2px solid var(--mm-13-line);
  background: var(--mm-13-surf);
  box-shadow: var(--mm-13-offset) var(--mm-13-offset) 0 var(--mm-13-line);
  opacity: 0;
  visibility: hidden;
  translate: 0 calc(var(--mm-13-lift) * -1);
  transition: opacity var(--mm-13-out) ease, translate var(--mm-13-out) ease, visibility 0s linear var(--mm-13-out);
}

.mm-13__item--open > .mm-13__panel,
.mm-13__item:focus-within > .mm-13__panel {
  opacity: 1;
  visibility: visible;
  translate: 0 0;
  transition-duration: var(--mm-13-in);
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-13__item:hover > .mm-13__panel {
    opacity: 1;
    visibility: visible;
    translate: 0 0;
    transition-duration: var(--mm-13-in);
    transition-delay: 0s;
  }
}

@supports (transition-behavior: allow-discrete) {
  .mm-13__panel {
    display: none;
    visibility: visible;
    transition: opacity var(--mm-13-out) ease, translate var(--mm-13-out) ease, display var(--mm-13-out) allow-discrete;
  }

  .mm-13__item--open > .mm-13__panel,
    .mm-13__item:focus-within > .mm-13__panel {
    display: grid;
    opacity: 1;
    translate: 0 0;
    transition-duration: var(--mm-13-in);

    @starting-style {
      opacity: 0;
      translate: 0 calc(var(--mm-13-lift) * -1);
    }
  }

  @media (hover: hover) {
    .mm-13__item:hover > .mm-13__panel {
      display: grid;
      opacity: 1;
      translate: 0 0;
      transition-duration: var(--mm-13-in);

      @starting-style {
        opacity: 0;
        translate: 0 calc(var(--mm-13-lift) * -1);
      }
    }
  }
}

.mm-13__half {
  min-inline-size: 0;
  padding: clamp(0.9rem, 2.4vw, 1.35rem);
}

.mm-13__half--alt {
  background: var(--mm-13-soft);
}

.mm-13__half-head {
  margin: 0 0 0.5rem;
  font: 600 0.74rem/1 var(--mm-13-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-13-mut);
}

.mm-13__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-13__links a {
  display: grid;
  align-content: center;
  gap: 1px;
  min-block-size: 48px;
  color: var(--mm-13-ink);
  text-decoration: none;
  min-inline-size: 0;
}

.mm-13__links b {
  font: 600 0.94rem/1.2 system-ui, sans-serif;
}

.mm-13__links span {
  font-size: 0.78rem;
  color: var(--mm-13-mut);
}

.mm-13__links a:hover b {
  text-decoration: underline;
  text-underline-offset: 4px;
  text-decoration-thickness: 2px;
  color: var(--mm-13-acc);
}

.mm-13__page {
  inline-size: min(72rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(3rem, 10vw, 6rem);
}

.mm-13__hero {
  max-inline-size: 34rem;
  display: grid;
  gap: 0.6rem;
}

.mm-13__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--mm-13-font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--mm-13-acc);
}

.mm-13__h1 {
  margin: 0;
  font: 600 clamp(2.2rem, 7vw, 4rem)/1 var(--mm-13-font-display);
  letter-spacing: 0.01em;
  text-transform: uppercase;
}

.mm-13__sub {
  margin: 0;
  color: var(--mm-13-mut);
  font-size: clamp(0.95rem, 2.3vw, 1.05rem);
}

.mm-13__cta {
  justify-self: start;
  display: inline-flex;
  align-items: center;
  min-block-size: 48px;
  margin-block-start: 0.4rem;
  padding-inline: 1.3rem;
  border: 2px solid var(--mm-13-line);
  background: var(--mm-13-acc);
  color: var(--mm-13-on-acc);
  text-decoration: none;
  font: 600 0.85rem/1 var(--mm-13-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  box-shadow: var(--mm-13-offset) var(--mm-13-offset) 0 var(--mm-13-line);
}

@media (max-width: 52rem) {
  .mm-13__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-13__list {
    flex-direction: column;
  }

  .mm-13__utils {
    margin-inline-start: 0;
  }

  .mm-13__panel {
    position: static;
    grid-template-columns: minmax(0, 1fr);
    opacity: 1;
    visibility: visible;
    translate: none;
    display: none;
    margin-block-start: 0.6rem;
  }

  .mm-13__item--open > .mm-13__panel,
    .mm-13__item:focus-within > .mm-13__panel {
    display: grid;
  }

  @supports (transition-behavior: allow-discrete) {
    .mm-13__panel {
      grid-template-columns: minmax(0, 1fr);
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-13__panel {
    transition-duration: 1ms;
  }

  @supports (transition-behavior: allow-discrete) {
    .mm-13__panel {
      transition-duration: 1ms;
    }
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-13__trigger {
    position: relative;
  }

  .mm-13__item:hover > .mm-13__trigger::after,
    .mm-13__item:focus-within > .mm-13__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — hard-edged snap in discrete steps, no smoothing anywhere */

.mm-13__links li,
.mm-13__sub li {
  opacity: 0;
  translate: -10px 0;
  transition: opacity 1ms steps(1, end), translate 180ms steps(3, end);
}

.mm-13__item:hover > .mm-13__panel .mm-13__links li,
.mm-13__item:focus-within > .mm-13__panel .mm-13__links li,
.mm-13__item--open > .mm-13__panel .mm-13__links li {
  opacity: 1;
  translate: 0 0;
}

.mm-13__item:hover > .mm-13__panel .mm-13__sub li,
.mm-13__item:focus-within > .mm-13__panel .mm-13__sub li,
.mm-13__item--open > .mm-13__panel .mm-13__sub li {
  opacity: 1;
  translate: 0 0;
}

.mm-13__links li:nth-child(1) {
  transition-delay: 30ms;
}

.mm-13__links li:nth-child(2) {
  transition-delay: 85ms;
}

.mm-13__links li:nth-child(3) {
  transition-delay: 140ms;
}

.mm-13__links li:nth-child(4) {
  transition-delay: 195ms;
}

.mm-13__links li:nth-child(5) {
  transition-delay: 250ms;
}

.mm-13__links li:nth-child(6) {
  transition-delay: 305ms;
}

.mm-13__links li:nth-child(n+7) {
  transition-delay: 305ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-13__links li,
    .mm-13__sub li {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-13__links li,
    .mm-13__sub li {
    opacity: 1;
    translate: none;
  }
}
```
