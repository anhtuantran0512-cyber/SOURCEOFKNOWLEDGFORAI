---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/animated-link-hover-effects-header/"
title: "Animated Link Hover Effects Header"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "Five nav-link hover treatments in one header, side by side, so you can compare them in context rather than in isolation: a scaleX underline, a clip-up fill,…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Link Hover Effects Header
Source: https://codefronts.com/layouts/css-header-designs/animated-link-hover-effects-header/

Five nav-link hover treatments in one header, side by side, so you can compare them in context rather than in isolation: a scaleX underline, a clip-up fill, a gradient sweep, a dual-layer label swap and a bracket reveal. Every one runs on transform and opacity only, and every one is wired to :focus-visible as well as :hover.
## HTML
```html
<div class="hd-19">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap">
  <a class="hd-19__skip" href="#hd-19-main">Skip to content</a>

  <header class="hd-19__bar">
    <a class="hd-19__brand" href="#hd-19-main">
      <span class="hd-19__prompt" aria-hidden="true">&#9655;</span>
      <span class="hd-19__word">phosphor<span>.sh</span></span>
    </a>

    <nav class="hd-19__nav" aria-label="Main">
      <ul>
        <li><a class="hd-19__a1" href="#hd-19-main">Overview</a></li>
        <li><a class="hd-19__a2" href="#hd-19-main"><span data-label="Runtime">Runtime</span></a></li>
        <li><a class="hd-19__a3" href="#hd-19-main">Pipelines</a></li>
        <li><a class="hd-19__a4" href="#hd-19-main"><span class="hd-19__l1">Registry</span><span class="hd-19__l2">Registry</span></a></li>
        <li><a class="hd-19__a5" href="#hd-19-main">Docs</a></li>
      </ul>
    </nav>

    <div class="hd-19__right">
      <input class="hd-19__sr" type="checkbox" id="hd-19-light">
      <label class="hd-19__theme" for="hd-19-light">
        <svg class="hd-19__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <svg class="hd-19__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <span class="hd-19__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-19__ghost" href="#hd-19-main">Log in</a>
      <a class="hd-19__cta" href="#hd-19-main">$ install</a>
    </div>
  </header>

  <main class="hd-19__main" id="hd-19-main">
    <p class="hd-19__eyebrow">// five hover treatments, one bar</p>
    <h1>Hover the nav. Then tab it &mdash; the effects fire on focus too.</h1>
    <p class="hd-19__lead">Each link uses a different mechanism, and all five stay on the compositor: transform, opacity and clip-path only. No width, no height, no margin.</p>

    <ol class="hd-19__legend">
      <li><span class="hd-19__k">01</span><span class="hd-19__n">Overview</span><span class="hd-19__d">scaleX underline &mdash; pseudo-element scaled from a set transform-origin</span></li>
      <li><span class="hd-19__k">02</span><span class="hd-19__n">Runtime</span><span class="hd-19__d">clip-up fill &mdash; clip-path inset animated from 100% to 0</span></li>
      <li><span class="hd-19__k">03</span><span class="hd-19__n">Pipelines</span><span class="hd-19__d">gradient sweep &mdash; background-size over background-clip: text</span></li>
      <li><span class="hd-19__k">04</span><span class="hd-19__n">Registry</span><span class="hd-19__d">dual-layer swap &mdash; two labels in one grid cell, translated opposite ways</span></li>
      <li><span class="hd-19__k">05</span><span class="hd-19__n">Docs</span><span class="hd-19__d">bracket reveal &mdash; ::before and ::after glyphs sliding into place</span></li>
    </ol>
    <div class="hd-19__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-19 {
  --bg: #05080a;
  --panel: #0b1013;
  --ink: #d7e6dc;
  --muted: #6d857a;
  --line: rgba(93,255,168,.18);
  --accent: #5dffa8;
  --accent-dim: #2fbf7a;
  --accent-ink: #04160d;
  --glow: 1;
  --sweep: 520ms;
  --font-display: "JetBrains Mono",ui-monospace,"IBM Plex Mono",monospace;
  --font-body: "JetBrains Mono",ui-monospace,"IBM Plex Mono",monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: repeating-linear-gradient(to bottom, rgba(93,255,168,.035) 0 1px, transparent 1px 3px), var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-19 {
    --bg: oklch(12% .02 160);
    --panel: oklch(16% .02 160);
    --ink: oklch(90% .04 160);
    --muted: oklch(62% .04 160);
    --accent: oklch(88% .18 155);
  }
}

.hd-19 * {
  box-sizing: border-box;
}

.hd-19 h1,
.hd-19 p,
.hd-19 ul,
.hd-19 ol {
  margin: 0;
  padding: 0;
}

.hd-19 ul,
.hd-19 ol {
  list-style: none;
}

.hd-19 [hidden] {
  display: none;
}

.hd-19 :focus-visible {
  outline: 1px solid var(--accent);
  outline-offset: 3px;
}

.hd-19__skip {
  position: absolute;
  inset-inline-start: .75rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .78rem;
  font-weight: 700;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-19__skip:focus-visible {
  top: .75rem;
}
/* ── header: ultra-compact, phosphor glow ─────────────────────────── */

.hd-19__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.6rem,2.5vw,1.75rem);
  padding: .45rem clamp(.7rem,3vw,1.5rem);
  background: color-mix(in srgb, var(--bg) 88%, transparent);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(8px);
}

.hd-19__brand {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-19__prompt {
  color: var(--accent);
  font-size: .85rem;
  text-shadow: 0 0 calc(.6rem * var(--glow)) var(--accent);
}

.hd-19__word {
  font-family: var(--font-display);
  font-size: .9rem;
  font-weight: 700;
  letter-spacing: -.03em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-19__word span {
  color: var(--muted);
  font-weight: 400;
}

.hd-19__nav {
  min-inline-size: 0;
}

.hd-19__nav ul {
  display: flex;
  align-items: center;
  gap: clamp(.35rem,1.6vw,1rem);
}

.hd-19__nav a {
  position: relative;
  display: block;
  padding: .4rem .3rem;
  color: var(--ink);
  text-decoration: none;
  font-size: .82rem;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
}
/* 01 — scaleX underline */

.hd-19__a1::after {
  content: "";
  position: absolute;
  inset-inline: .3rem;
  bottom: .15rem;
  block-size: 2px;
  background: var(--accent);
  box-shadow: 0 0 calc(.5rem * var(--glow)) var(--accent);
  scale: 0 1;
  transform-origin: left center;
  transition: scale .28s cubic-bezier(.2,.8,.2,1);
}

.hd-19__a1:hover::after,
.hd-19__a1:focus-visible::after {
  scale: 1 1;
}

.hd-19__a1:hover,
.hd-19__a1:focus-visible {
  color: var(--accent);
}
/* 02 — clip-up fill */

.hd-19__a2 span {
  position: relative;
  display: inline-block;
}

.hd-19__a2 span::after {
  content: attr(data-label);
  position: absolute;
  inset: 0;
  color: var(--accent-ink);
  background: var(--accent);
  padding-inline: .2rem;
  margin-inline: -.2rem;
  clip-path: inset(100% 0 0 0);
  transition: clip-path .3s cubic-bezier(.2,.8,.2,1);
}

.hd-19__a2:hover span::after,
.hd-19__a2:focus-visible span::after {
  clip-path: inset(0 0 0 0);
}
/* 03 — gradient sweep on the text itself */

.hd-19__a3 {
  background-image: linear-gradient(100deg, var(--accent) 0%, var(--accent-dim) 45%, var(--ink) 46%);
  background-size: 300% 100%;
  background-position: 100% 0;
  background-repeat: no-repeat;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  transition: background-position var(--sweep) cubic-bezier(.3,.8,.3,1);
}

.hd-19__a3:hover,
.hd-19__a3:focus-visible {
  background-position: 0 0;
}
/* 04 — dual-layer label swap */

.hd-19__a4 {
  display: grid;
  overflow: hidden;
}

.hd-19__a4 > span {
  grid-area: 1/1;
  transition: translate .28s cubic-bezier(.2,.8,.2,1), opacity .2s ease;
}

.hd-19__l2 {
  color: var(--accent);
  translate: 0 1.2em;
  opacity: 0;
  text-shadow: 0 0 calc(.55rem * var(--glow)) var(--accent);
}

.hd-19__a4:hover .hd-19__l1,
.hd-19__a4:focus-visible .hd-19__l1 {
  translate: 0 -1.2em;
  opacity: 0;
}

.hd-19__a4:hover .hd-19__l2,
.hd-19__a4:focus-visible .hd-19__l2 {
  translate: 0 0;
  opacity: 1;
}
/* 05 — bracket reveal */

.hd-19__a5 {
  padding-inline: .75rem;
}

.hd-19__a5::before,
.hd-19__a5::after {
  position: absolute;
  top: .4rem;
  color: var(--accent);
  opacity: 0;
  transition: translate .24s ease, opacity .24s ease;
}

.hd-19__a5::before {
  content: "[";
  inset-inline-start: .1rem;
  translate: .4rem 0;
}

.hd-19__a5::after {
  content: "]";
  inset-inline-end: .1rem;
  translate: -.4rem 0;
}

.hd-19__a5:hover::before,
.hd-19__a5:focus-visible::before,
.hd-19__a5:hover::after,
.hd-19__a5:focus-visible::after {
  opacity: 1;
  translate: 0 0;
}

.hd-19__a5:hover,
.hd-19__a5:focus-visible {
  color: var(--accent);
}

.hd-19__right {
  display: flex;
  align-items: center;
  gap: .5rem;
  margin-inline-start: auto;
}

.hd-19__ghost {
  color: var(--muted);
  text-decoration: none;
  font-size: .8rem;
  white-space: nowrap;
  transition: color .15s ease;
}

.hd-19__ghost:hover {
  color: var(--ink);
}

.hd-19__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.1rem;
  padding: .45rem .8rem;
  border: 1px solid var(--accent);
  color: var(--accent);
  text-decoration: none;
  font-size: .8rem;
  font-weight: 700;
  white-space: nowrap;
  transition: background-color .16s ease, color .16s ease, box-shadow .16s ease;
}

.hd-19__cta:hover,
.hd-19__cta:focus-visible {
  background: var(--accent);
  color: var(--accent-ink);
  box-shadow: 0 0 calc(1.2rem * var(--glow)) rgba(93,255,168,.5);
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-19__main {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(2rem,6vw,3.5rem) clamp(.85rem,3vw,1.5rem) 4rem;
}

.hd-19__eyebrow {
  font-size: .78rem;
  color: var(--muted);
}

.hd-19__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.6rem,5vw,2.6rem);
  line-height: 1.15;
  font-weight: 700;
  letter-spacing: -.045em;
  margin-top: .9rem;
  max-inline-size: 28ch;
  text-wrap: balance;
  text-shadow: 0 0 calc(1.6rem * var(--glow)) rgba(93,255,168,.16);
}

.hd-19__lead {
  margin-top: 1rem;
  max-inline-size: 60ch;
  color: var(--muted);
  font-size: .94rem;
  text-wrap: pretty;
}

.hd-19__legend {
  margin-top: 2rem;
  border-top: 1px solid var(--line);
}

.hd-19__legend li {
  display: grid;
  grid-template-columns: 2.5rem 7rem minmax(0,1fr);
  gap: 1rem;
  align-items: baseline;
  padding: .75rem .2rem;
  border-bottom: 1px solid var(--line);
  font-size: .84rem;
}

.hd-19__legend li:hover {
  background: var(--panel);
}

.hd-19__k {
  color: var(--accent-dim);
}

.hd-19__n {
  color: var(--ink);
  font-weight: 700;
}

.hd-19__d {
  color: var(--muted);
  min-inline-size: 0;
  text-wrap: pretty;
}

.hd-19__filler {
  block-size: 45vh;
}

@media (max-width: 900px) {
  .hd-19__bar {
    flex-wrap: wrap;
    gap: .5rem;
  }

  .hd-19__nav {
    order: 3;
    flex-basis: 100%;
    overflow-x: auto;
    scrollbar-width: none;
  }

  .hd-19__nav::-webkit-scrollbar {
    display: none;
  }
}

@media (max-width: 560px) {
  .hd-19__ghost {
    display: none;
  }

  .hd-19__legend li {
    grid-template-columns: 2.5rem minmax(0,1fr);
  }

  .hd-19__d {
    grid-column: 2;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-19:has(#hd-19-light:checked) {
  --bg: #f4f7f5;
  --panel: #eaf0ec;
  --ink: #0d1a13;
  --muted: #4e6157;
  --line: rgba(13,26,19,.14);
  --accent: #0d8f55;
  --accent-dim: #116b43;
  --accent-ink: #ffffff;
  --glow: 0;
}

.hd-19:has(#hd-19-light:checked) {
  background-image: none;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-19__moon {
  display: none;
}

.hd-19:has(#hd-19-light:checked) .hd-19__sun {
  display: none;
}

.hd-19:has(#hd-19-light:checked) .hd-19__moon {
  display: block;
}

@media (prefers-color-scheme: light) {
  .hd-19:not([data-theme="dark"]):not(:has(#hd-19-light:checked)):not(:has(#hd-19-light:checked)) {
    --bg: #f4f7f5;
    --panel: #eaf0ec;
    --ink: #0d1a13;
    --muted: #4e6157;
    --line: rgba(13,26,19,.14);
    --accent: #0d8f55;
    --accent-dim: #116b43;
    --accent-ink: #ffffff;
    --glow: 0;
  }

  .hd-19:not([data-theme="dark"]) {
    background-image: none;
  }
  /* FLIP-BACK — light OS + checked toggle returns to the other scheme */

  .hd-19:has(#hd-19-light:checked) {
    --bg: #05080a;
    --panel: #0b1013;
    --ink: #d7e6dc;
    --muted: #6d857a;
    --line: rgba(93,255,168,.18);
    --accent: #5dffa8;
    --accent-dim: #2fbf7a;
    --accent-ink: #04160d;
    --glow: 1;
    --sweep: 520ms;
    --font-display: "JetBrains Mono",ui-monospace,"IBM Plex Mono",monospace;
    --font-body: "JetBrains Mono",ui-monospace,"IBM Plex Mono",monospace;
  }
  /* the icon always offers the scheme you are not in */

  .hd-19:not([data-theme="dark"]):not(:has(#hd-19-light:checked)) .hd-19__sun {
    display: none;
  }

  .hd-19:not([data-theme="dark"]):not(:has(#hd-19-light:checked)) .hd-19__moon {
    display: block;
  }

  .hd-19:has(#hd-19-light:checked) .hd-19__moon {
    display: none;
  }

  .hd-19:has(#hd-19-light:checked) .hd-19__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hd-19 * {
    transition-duration: 1ms !important;
    animation-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-19__cta {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-19__sr,
.hd-19__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-19__theme {
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

.hd-19__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-19__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-19:has(#hd-19-light:focus-visible) .hd-19__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
