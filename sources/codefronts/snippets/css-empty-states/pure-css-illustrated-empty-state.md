---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/pure-css-illustrated-empty-state/"
title: "Pure CSS Illustrated Empty State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "An illustrated empty state with no image files and no SVG: a copper pot, its broth, two handles, a plate shadow, three curls of steam and a herb sprig, all…"
has_js: "false"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Illustrated Empty State
Source: https://codefronts.com/snippets/css-empty-states/pure-css-illustrated-empty-state/

An illustrated empty state with no image files and no SVG: a copper pot, its broth, two handles, a plate shadow, three curls of steam and a herb sprig, all built from elements, gradients, border-radius and clip-path. It sits in a real cookbook app &mdash; header, collections rail, saved tab .
## HTML
```html
<div class="est-18">
  <header class="est-18__top">
    <span class="est-18__brand">Copperpot</span>
    <nav class="est-18__nav" aria-label="Cookbook">
      <a href="#est-18">Discover</a>
      <a href="#est-18">Weeknight</a>
      <a href="#est-18">Baking</a>
      <a class="est-18__navon" href="#est-18" aria-current="page">Saved</a>
    </nav>
    <span class="est-18__ava" aria-hidden="true">RS</span>
  </header>

  <main class="est-18__main">
    <aside class="est-18__side">
      <p class="est-18__slabel">Collections</p>
      <ul class="est-18__slist">
        <li><a href="#est-18">Sunday roasts</a></li>
        <li><a href="#est-18">Twenty minutes</a></li>
        <li><a href="#est-18">Bread and doughs</a></li>
        <li><a href="#est-18">Preserving</a></li>
      </ul>
      <p class="est-18__slabel">Shopping</p>
      <ul class="est-18__slist">
        <li><a href="#est-18">This week</a></li>
        <li><a href="#est-18">Pantry staples</a></li>
      </ul>
    </aside>

    <section class="est-18__stage">
      <div class="est-18__art" aria-hidden="true">
        <span class="est-18__steam" data-s="1"></span>
        <span class="est-18__steam" data-s="2"></span>
        <span class="est-18__steam" data-s="3"></span>
        <span class="est-18__pot">
          <span class="est-18__handle" data-h="l"></span>
          <span class="est-18__handle" data-h="r"></span>
          <span class="est-18__broth"></span>
        </span>
        <span class="est-18__plate"></span>
        <span class="est-18__sprig"><i></i><i></i><i></i></span>
      </div>

      <h1 class="est-18__h1">Nothing saved to your cookbook</h1>
      <p class="est-18__p">Save a recipe and it lands here with its ingredients scaled to your household, ready for the week&rsquo;s shopping list.</p>
      <div class="est-18__acts">
        <a class="est-18__pri" href="#est-18">Browse this week&rsquo;s picks</a>
        <a class="est-18__sec" href="#est-18">Import from a link</a>
      </div>
    </section>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap');

.est-18 {
  --paper: #f7f2e9;
  --card: #fffdf8;
  --sunk: #efe7d9;
  --line: #e3d9c7;
  --line-2: #cec1a9;
  --ink: #221d16;
  --muted: #665d4f;
  --faint: #918675;
  --clay: #b05f2f;
  --olive: #5e6a3f;
  --cream: #f3e4c9;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  box-sizing: border-box;
  background: var(--paper);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-18 *,
.est-18 *::before,
.est-18 *::after {
  box-sizing: border-box;
}

.est-18 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-18 {
    --paper: oklch(0.962 0.015 85);
    --card: oklch(0.991 0.007 85);
    --sunk: oklch(0.925 0.022 82);
    --line: oklch(0.885 0.026 82);
    --line-2: oklch(0.805 0.036 80);
    --ink: oklch(0.225 0.018 55);
    --muted: oklch(0.465 0.022 62);
    --faint: oklch(0.615 0.024 65);
    --clay: oklch(0.56 0.125 47);
    --olive: oklch(0.5 0.06 118);
    --cream: oklch(0.915 0.045 85);
  }
}

.est-18__top {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.5rem;
  align-items: center;
  padding: 1.1rem clamp(1rem,4vw,3rem);
  border-block-end: 1px solid var(--line);
}

.est-18__brand {
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: 1.4rem;
  letter-spacing: -.01em;
}

.est-18__nav {
  flex: 1 1 auto;
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.est-18__nav a {
  font-size: .86rem;
  color: var(--muted);
  text-decoration: none;
  padding-block: .2rem;
  border-block-end: 1.5px solid transparent;
  transition: color .16s, border-color .16s;
}

.est-18__nav a:hover {
  color: var(--ink);
  border-color: var(--clay);
}

.est-18__navon {
  color: var(--ink);
  border-color: var(--ink);
}

.est-18__ava {
  margin-inline-start: auto;
  inline-size: 2rem;
  block-size: 2rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: .7rem;
  font-weight: 600;
  color: var(--card);
  background: var(--olive);
}

.est-18__main {
  min-inline-size: 0;
  inline-size: min(74rem,100%);
  justify-self: center;
  display: grid;
  grid-template-columns: minmax(0,13rem) minmax(0,1fr);
  gap: clamp(1.25rem,3vw,2.5rem);
  padding: clamp(1.5rem,4vw,3rem) clamp(1rem,4vw,3rem);
  align-items: start;
}

.est-18__side {
  display: grid;
  gap: .5rem;
  align-content: start;
}

.est-18__slabel {
  margin: .75rem 0 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-style: italic;
  font-size: 1rem;
  color: var(--faint);
}

.est-18__slabel:first-child {
  margin-block-start: 0;
}

.est-18__slist {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .1rem;
}

.est-18__slist a {
  display: block;
  padding: .4rem .55rem;
  border-radius: 8px;
  font-size: .86rem;
  color: var(--muted);
  text-decoration: none;
  transition: color .16s, background .16s;
}

.est-18__slist a:hover {
  color: var(--ink);
  background: var(--sunk);
}

.est-18__stage {
  min-inline-size: 0;
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .6rem;
  padding: clamp(2rem,5vw,3.5rem) clamp(1.25rem,3vw,2.5rem);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: 0 1px 0 var(--line), 0 40px 70px -60px rgba(34,29,22,.55);
  background-image: radial-gradient(color-mix(in oklab, var(--line-2) 35%, transparent) .6px, transparent .6px);
  background-size: 15px 15px;
}

.est-18__art {
  position: relative;
  inline-size: min(17rem,80%);
  aspect-ratio: 1.35;
  margin-block-end: .75rem;
}

.est-18__plate {
  position: absolute;
  inset-block-end: 4%;
  inset-inline: 6%;
  block-size: 14%;
  border-radius: 50%;
  background: linear-gradient(180deg, var(--sunk), color-mix(in oklab, var(--line-2) 60%, var(--sunk)));
  box-shadow: 0 6px 14px -8px rgba(34,29,22,.45);
}

.est-18__pot {
  position: absolute;
  inset-block-end: 12%;
  inset-inline: 26%;
  block-size: 40%;
  border-radius: 8% 8% 42% 42% / 6% 6% 46% 46%;
  background: linear-gradient(100deg, var(--clay) 0 42%, color-mix(in oklab, var(--clay) 78%, #000) 42% 100%);
  box-shadow: inset 0 -1rem 1.6rem -.9rem rgba(0,0,0,.4);
}

.est-18__pot::after {
  content: '';
  position: absolute;
  inset-block-start: -.42rem;
  inset-inline: -8%;
  block-size: .75rem;
  border-radius: 50%;
  background: color-mix(in oklab, var(--clay) 82%, #fff);
  box-shadow: 0 .2rem .4rem -.2rem rgba(0,0,0,.3);
}

.est-18__broth {
  position: absolute;
  inset-block-start: -.05rem;
  inset-inline: 4%;
  block-size: 16%;
  z-index: 1;
  border-radius: 50%;
  background: radial-gradient(120% 180% at 50% 20%, color-mix(in oklab, var(--cream) 92%, #fff), color-mix(in oklab, var(--cream) 62%, var(--clay)));
  animation: est-18-swell 7s ease-in-out infinite;
}

@keyframes est-18-swell {
  0%,
    100% {
    scale: 1 1;
  }

  50% {
    scale: 1.02 1.12;
  }
}

.est-18__handle {
  position: absolute;
  inset-block-start: 12%;
  inline-size: 26%;
  block-size: 34%;
  border: .34rem solid color-mix(in oklab, var(--clay) 88%, #000);
  border-radius: 50%;
  background: transparent;
}

.est-18__handle[data-h="l"] {
  inset-inline-start: -22%;
  clip-path: inset(0 52% 0 0);
}

.est-18__handle[data-h="r"] {
  inset-inline-end: -22%;
  clip-path: inset(0 0 0 52%);
}

.est-18__steam {
  position: absolute;
  inset-block-start: 8%;
  inline-size: .55rem;
  block-size: 26%;
  z-index: 2;
  border-inline-start: 2px solid color-mix(in oklab, var(--faint) 55%, transparent);
  border-radius: 60% 0 60% 0;
  opacity: 0;
  animation: est-18-rise 5.5s ease-in-out infinite;
}

.est-18__steam[data-s="1"] {
  inset-inline-start: 38%;
  animation-delay: 0s;
}

.est-18__steam[data-s="2"] {
  inset-inline-start: 48%;
  block-size: 32%;
  animation-delay: 1.6s;
}

.est-18__steam[data-s="3"] {
  inset-inline-start: 58%;
  block-size: 22%;
  animation-delay: 3.1s;
}

@keyframes est-18-rise {
  0% {
    opacity: 0;
    translate: 0 20%;
    scale: .9;
  }

  35% {
    opacity: .75;
  }

  100% {
    opacity: 0;
    translate: 0 -55%;
    scale: 1.08;
  }
}

.est-18__sprig {
  position: absolute;
  inset-block-end: 16%;
  inset-inline-end: 11%;
  inline-size: 16%;
  block-size: 26%;
}

.est-18__sprig i {
  position: absolute;
  inset-block-end: 0;
  inline-size: 42%;
  block-size: 70%;
  border-radius: 70% 0 70% 0;
  background: linear-gradient(150deg, color-mix(in oklab, var(--olive) 85%, #fff), var(--olive));
  transform-origin: 50% 100%;
}

.est-18__sprig i:nth-child(1) {
  rotate: -24deg;
}

.est-18__sprig i:nth-child(2) {
  rotate: 2deg;
  block-size: 88%;
}

.est-18__sprig i:nth-child(3) {
  rotate: 26deg;
}

.est-18__h1 {
  margin: 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: clamp(1.7rem,4vw,2.6rem);
  font-weight: 400;
  line-height: 1.05;
  letter-spacing: -.02em;
  text-wrap: balance;
  max-inline-size: 24ch;
}

.est-18__p {
  margin: 0;
  max-inline-size: 46ch;
  font-size: .95rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.est-18__acts {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  justify-content: center;
  margin-block-start: .9rem;
}

.est-18__pri {
  min-block-size: 2.85rem;
  display: inline-flex;
  align-items: center;
  padding: .7rem 1.25rem;
  font-size: .88rem;
  font-weight: 500;
  color: var(--card);
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 2px;
  text-decoration: none;
  transition: background .18s, border-color .18s, translate .16s;
}

.est-18__pri:hover {
  background: var(--clay);
  border-color: var(--clay);
  translate: 0 -1px;
}

.est-18__sec {
  min-block-size: 2.85rem;
  display: inline-flex;
  align-items: center;
  padding: .7rem 1.1rem;
  font-size: .88rem;
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--line-2);
  border-radius: 2px;
  text-decoration: none;
  transition: background .18s;
}

.est-18__sec:hover {
  background: var(--sunk);
}

.est-18__pri:focus-visible,
.est-18__sec:focus-visible,
.est-18__nav a:focus-visible,
.est-18__slist a:focus-visible {
  outline: 2px solid var(--clay);
  outline-offset: 3px;
}

@media (max-width: 760px) {
  .est-18__main {
    grid-template-columns: 1fr;
  }

  .est-18__side {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-18 *,
    .est-18 *::before,
    .est-18 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-18__stage,
    .est-18__pri {
    border-color: CanvasText;
  }

  .est-18__art {
    display: none;
  }
}
```
