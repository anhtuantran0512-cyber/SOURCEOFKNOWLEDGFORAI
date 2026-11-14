---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/full-screen-overlay-hamburger-header/"
title: "Full Screen Overlay Hamburger Header"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A header that opens into a full-screen navigation overlay with no JavaScript: a visually hidden checkbox, a label styled as the hamburger, and :has(:checked)…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full Screen Overlay Hamburger Header
Source: https://codefronts.com/layouts/css-header-designs/full-screen-overlay-hamburger-header/

A header that opens into a full-screen navigation overlay with no JavaScript: a visually hidden checkbox, a label styled as the hamburger, and :has(:checked) on the root. The bars morph into an X with a spring curve, menu items stagger in on animation-delay, and the closed overlay is hidden with visibility so its links never sit in the tab order.
## HTML
```html
<div class="hd-15">
  <a class="hd-15__skip" href="#hd-15-main">Skip to content</a>
    <input class="hd-15__sr" type="checkbox" id="hd-15-open" aria-label="Open navigation menu">

  <header class="hd-15__bar">
    <a class="hd-15__brand" href="#hd-15-main">
      <span class="hd-15__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 3.5 20.5 12 12 20.5 3.5 12 12 3.5Z" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="2.6" fill="currentColor"/></svg>
      </span>
      <span class="hd-15__word">Vantage</span>
    </a>

    <p class="hd-15__tag">Studio for interface engineering</p>

    <input class="hd-15__sr" type="checkbox" id="hd-15-light">
    <label class="hd-15__theme" for="hd-15-light">
      <svg class="hd-15__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
      <svg class="hd-15__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      <span class="hd-15__vh">Switch light or dark theme</span>
    </label>
    <label class="hd-15__burger" for="hd-15-open">
      <span class="hd-15__bars" aria-hidden="true">
        <span class="hd-15__b1"></span><span class="hd-15__b2"></span><span class="hd-15__b3"></span>
      </span>
      <span class="hd-15__burger-t" aria-hidden="true">Menu</span>
    </label>
  </header>

  <div class="hd-15__overlay">
    <label class="hd-15__close-all" for="hd-15-open" aria-label="Close navigation menu"></label>
    <div class="hd-15__overlay-in">
      <nav class="hd-15__menu" aria-label="Main">
        <ul>
          <li style="--i:1"><a class="hd-15__link" href="#hd-15-main"><span class="hd-15__num">01</span>Work</a></li>
          <li style="--i:2"><a class="hd-15__link" href="#hd-15-main"><span class="hd-15__num">02</span>Services</a></li>
          <li style="--i:3"><a class="hd-15__link" href="#hd-15-main"><span class="hd-15__num">03</span>Studio</a></li>
          <li style="--i:4"><a class="hd-15__link" href="#hd-15-main"><span class="hd-15__num">04</span>Writing</a></li>
          <li style="--i:5"><a class="hd-15__link" href="#hd-15-main"><span class="hd-15__num">05</span>Contact</a></li>
        </ul>
      </nav>
      <div class="hd-15__meta" style="--i:6">
        <p class="hd-15__meta-h">Studio</p>
        <p>Unit 4, Ropewalk<br>Bristol BS1 6QT</p>
        <p class="hd-15__meta-h">New work</p>
        <p>[email protected]<br>+44 117 496 0142</p>
      </div>
    </div>
    <label class="hd-15__close" for="hd-15-open">
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <span class="hd-15__vh">Close navigation menu</span>
    </label>
  </div>

  <main class="hd-15__main" id="hd-15-main">
    <p class="hd-15__eyebrow">Selected work &middot; 2026</p>
    <h1>Interfaces that survive the second release.</h1>
    <p class="hd-15__lead">Press the menu button &mdash; or tab to it and hit space. The bars morph, the overlay blurs the page and five links stagger in. Nothing here is JavaScript.</p>
    <ul class="hd-15__work">
      <li><span class="hd-15__w-n">01</span><span class="hd-15__w-t">Northwind &mdash; freight console</span><span class="hd-15__w-y">2026</span></li>
      <li><span class="hd-15__w-n">02</span><span class="hd-15__w-t">Halcyon &mdash; design system</span><span class="hd-15__w-y">2025</span></li>
      <li><span class="hd-15__w-n">03</span><span class="hd-15__w-t">Meridian &mdash; docs platform</span><span class="hd-15__w-y">2025</span></li>
      <li><span class="hd-15__w-n">04</span><span class="hd-15__w-t">Foundry &mdash; asset pipeline</span><span class="hd-15__w-y">2024</span></li>
    </ul>
    <div class="hd-15__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-15 {
  --bg: #000000;
  --surface: #0b0d0f;
  --ink: #f4f7f8;
  --muted: #8c9599;
  --line: rgba(244,247,248,.14);
  --accent: #22e0d0;
  --accent-ink: #00201d;
  --menu-size: clamp(2.1rem,9vw,4.6rem);
  --font-display: "Avenir Next Condensed","Arial Narrow",system-ui,sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-15 {
    --surface: oklch(14% .006 200);
    --ink: oklch(97% .006 200);
    --muted: oklch(68% .015 200);
    --accent: oklch(84% .14 185);
  }
}

.hd-15 * {
  box-sizing: border-box;
}

.hd-15 h1,
.hd-15 p,
.hd-15 ul {
  margin: 0;
  padding: 0;
}

.hd-15 ul {
  list-style: none;
}

.hd-15 [hidden] {
  display: none;
}

.hd-15 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.hd-15__sr,
.hd-15__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-15__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 80;
  padding: .55rem 1rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .8rem;
  font-weight: 700;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-15__skip:focus-visible {
  top: 1rem;
}
/* ── header: no chrome, type only ─────────────────────────────────── */

.hd-15__bar {
  position: sticky;
  top: 0;
  z-index: 60;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: clamp(1rem,3vw,1.5rem) clamp(1rem,4vw,2.5rem);
  background: color-mix(in srgb, var(--bg) 78%, transparent);
  backdrop-filter: blur(10px);
}

.hd-15__brand {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-15__mark {
  display: grid;
  place-items: center;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  color: var(--accent);
  flex: none;
}

.hd-15__mark svg {
  inline-size: 1.9rem;
  block-size: 1.9rem;
}

.hd-15__word {
  font-family: var(--font-display);
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-15__tag {
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-15__burger {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  margin-inline-start: auto;
  min-block-size: 2.75rem;
  padding: .5rem .75rem;
  border: 1px solid var(--line);
  cursor: pointer;
  transition: border-color .18s ease, background-color .18s ease;
}

.hd-15__burger:hover {
  border-color: var(--accent);
  background: rgba(34,224,208,.08);
}

.hd-15__bars {
  display: grid;
  gap: 4px;
  inline-size: 1.4rem;
}

.hd-15__bars span {
  display: block;
  block-size: 2px;
  background: var(--ink);
  border-radius: 2px;
  transition: translate .3s cubic-bezier(.5,-.35,.4,1.4), rotate .3s cubic-bezier(.5,-.35,.4,1.4), opacity .2s ease, scale .2s ease, background-color .2s ease;
}

.hd-15__burger-t {
  font-family: var(--font-display);
  font-size: .82rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-15:has(#hd-15-open:checked) .hd-15__b1 {
  translate: 0 6px;
  rotate: 45deg;
  background: var(--accent);
}

.hd-15:has(#hd-15-open:checked) .hd-15__b2 {
  opacity: 0;
  scale: .3 1;
}

.hd-15:has(#hd-15-open:checked) .hd-15__b3 {
  translate: 0 -6px;
  rotate: -45deg;
  background: var(--accent);
}

.hd-15:has(#hd-15-open:focus-visible) .hd-15__burger {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
/* ── full-screen overlay ──────────────────────────────────────────── */

.hd-15__overlay {
  position: fixed;
  inset: 0;
  z-index: 70;
  display: grid;
  align-items: center;
  background: rgba(0,0,0,.94);
  visibility: hidden;
  opacity: 0;
  pointer-events: none;
  transition: opacity .28s ease, visibility .28s allow-discrete;
}

@supports (backdrop-filter: blur(2px)) {
  .hd-15__overlay {
    background: rgba(0,0,0,.72);
    backdrop-filter: blur(22px) saturate(120%);
  }
}

.hd-15:has(#hd-15-open:checked) .hd-15__overlay {
  visibility: visible;
  opacity: 1;
  pointer-events: auto;
}

.hd-15__close-all {
  position: absolute;
  inset: 0;
  cursor: default;
}

.hd-15__overlay-in {
  position: relative;
  inline-size: 100%;
  max-inline-size: 72rem;
  margin-inline: auto;
  display: grid;
  grid-template-columns: minmax(0,1fr) 14rem;
  gap: clamp(1.5rem,5vw,4rem);
  align-items: end;
  padding: clamp(2rem,8vh,5rem) clamp(1.25rem,5vw,3rem);
}

.hd-15__menu ul {
  display: grid;
  gap: .1rem;
}

.hd-15__link {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  padding: .15rem 0;
  font-family: var(--font-display);
  font-size: var(--menu-size);
  line-height: 1.05;
  font-weight: 700;
  letter-spacing: -.01em;
  text-transform: uppercase;
  color: var(--ink);
  text-decoration: none;
  transition: color .18s ease, translate .18s ease;
}

.hd-15__link:hover {
  color: var(--accent);
  translate: .6rem 0;
}

.hd-15__num {
  font-family: var(--font-body);
  font-size: .8rem;
  font-weight: 600;
  letter-spacing: .14em;
  color: var(--muted);
  flex: none;
}

.hd-15__meta {
  display: grid;
  gap: .25rem;
  color: var(--muted);
  font-size: .85rem;
}

.hd-15__meta-h {
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
  margin-top: .75rem;
}

.hd-15__meta-h:first-child {
  margin-top: 0;
}

.hd-15__close {
  position: absolute;
  top: clamp(1rem,3vw,1.5rem);
  inset-inline-end: clamp(1rem,4vw,2.5rem);
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--line);
  color: var(--ink);
  cursor: pointer;
  transition: border-color .18s ease, color .18s ease;
}

.hd-15__close svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
}

.hd-15__close:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.hd-15:has(#hd-15-open:checked) .hd-15__link,
.hd-15:has(#hd-15-open:checked) .hd-15__meta {
  animation: hd-15-in .45s cubic-bezier(.2,.8,.2,1) backwards;
  animation-delay: calc(var(--i,1) * 55ms + 80ms);
}

@keyframes hd-15-in {
  from {
    opacity: 0;
    translate: 0 1.4rem;
  }
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-15__main {
  max-inline-size: 64rem;
  margin-inline: auto;
  padding: clamp(3rem,9vw,6rem) clamp(1.25rem,4vw,2.5rem) 5rem;
}

.hd-15__eyebrow {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-15__main h1 {
  font-family: var(--font-display);
  font-size: clamp(2.2rem,8vw,4.4rem);
  line-height: 1.02;
  font-weight: 700;
  letter-spacing: -.01em;
  text-transform: uppercase;
  margin-top: 1rem;
  max-inline-size: 22ch;
  text-wrap: balance;
}

.hd-15__lead {
  margin-top: 1.2rem;
  max-inline-size: 52ch;
  color: var(--muted);
  font-size: 1.02rem;
  text-wrap: pretty;
}

.hd-15__work {
  margin-top: clamp(2.5rem,7vw,4rem);
  border-top: 1px solid var(--line);
}

.hd-15__work li {
  display: grid;
  grid-template-columns: 3rem minmax(0,1fr) 4rem;
  align-items: center;
  gap: 1rem;
  padding: 1rem .25rem;
  border-bottom: 1px solid var(--line);
}

.hd-15__work li:hover {
  background: var(--surface);
}

.hd-15__w-n {
  font-size: .75rem;
  letter-spacing: .14em;
  color: var(--muted);
}

.hd-15__w-t {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .02em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-15__w-y {
  font-size: .8rem;
  color: var(--muted);
  text-align: end;
  font-variant-numeric: tabular-nums;
}

.hd-15__filler {
  block-size: 40vh;
}

@media (max-width: 720px) {
  .hd-15__tag {
    display: none;
  }

  .hd-15__overlay-in {
    grid-template-columns: minmax(0,1fr);
    align-items: start;
  }

  .hd-15__meta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hd-15 * {
    animation-duration: 1ms !important;
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-15__overlay {
    background: Canvas;
  }

  .hd-15__burger,
    .hd-15__close {
    border: 1px solid CanvasText;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-15:has(#hd-15-light:checked) {
  --bg: #f6f8f8;
  --surface: #ffffff;
  --ink: #0b0d0f;
  --muted: #5b6568;
  --line: rgba(11,13,15,.14);
  --accent: #0f8f85;
  --accent-ink: #ffffff;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-15__moon {
  display: none;
}

.hd-15:has(#hd-15-light:checked) .hd-15__sun {
  display: none;
}

.hd-15:has(#hd-15-light:checked) .hd-15__moon {
  display: block;
}

@media (prefers-color-scheme: light) {
  .hd-15:not([data-theme="dark"]):not(:has(#hd-15-light:checked)) {
    --bg: #f6f8f8;
    --surface: #ffffff;
    --ink: #0b0d0f;
    --muted: #5b6568;
    --line: rgba(11,13,15,.14);
    --accent: #0f8f85;
    --accent-ink: #ffffff;
  }
  /* FLIP-BACK — light OS + checked toggle returns to the dark surface */

  .hd-15:has(#hd-15-light:checked) {
    --bg: #000000;
    --surface: #0b0d0f;
    --ink: #f4f7f8;
    --muted: #8c9599;
    --line: rgba(244,247,248,.14);
    --accent: #22e0d0;
    --accent-ink: #00201d;
  }
  /* the icon always offers the scheme you are not in */

  .hd-15:not([data-theme="dark"]):not(:has(#hd-15-light:checked)) .hd-15__sun {
    display: none;
  }

  .hd-15:not([data-theme="dark"]):not(:has(#hd-15-light:checked)) .hd-15__moon {
    display: block;
  }

  .hd-15:has(#hd-15-light:checked) .hd-15__moon {
    display: none;
  }

  .hd-15:has(#hd-15-light:checked) .hd-15__sun {
    display: block;
  }
}

.hd-15[data-theme="light"] {
  --bg: #f6f8f8;
  --surface: #ffffff;
  --ink: #0b0d0f;
  --muted: #5b6568;
  --line: rgba(11,13,15,.14);
  --accent: #0f8f85;
  --accent-ink: #ffffff;
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-15__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-15__theme {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: inherit;
  cursor: pointer;
  transition: background-color .18s ease;
}

.hd-15__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-15__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-15:has(#hd-15-light:focus-visible) .hd-15__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
