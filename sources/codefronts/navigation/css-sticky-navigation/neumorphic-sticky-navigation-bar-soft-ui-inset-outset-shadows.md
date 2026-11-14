---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/neumorphic-sticky-navigation-bar-soft-ui-inset-outset-shadows/"
title: "Neumorphic Sticky Navigation Bar (Soft-UI Inset/Outset Shadows)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "Soft-UI applied to a sticky bar, with the physics done properly: every raised surface casts one light and one dark shadow from a single consistent light…"
has_js: "false"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Sticky Navigation Bar (Soft-UI Inset/Outset Shadows)
Source: https://codefronts.com/navigation/css-sticky-navigation/neumorphic-sticky-navigation-bar-soft-ui-inset-outset-shadows/

Soft-UI applied to a sticky bar, with the physics done properly: every raised surface casts one light and one dark shadow from a single consistent light source, and active items invert to inset so they read as genuinely pressed into the panel. Includes the guardrails that keep the style usable — because the classic failure of this aesthetic is unreadable, un-focusable controls.
## HTML
```html
<section class="sn-15" aria-label="Neumorphic sticky navigation bar demo">
    <header class="sn-15__bar">
      <a class="sn-15__brand" href="#sn-15-s1"><span class="sn-15__logo" aria-hidden="true"></span>Pebble</a>
      <nav class="sn-15__nav" aria-label="Primary">
        <a class="sn-15__link" href="#sn-15-s1" aria-current="page">Home</a>
        <a class="sn-15__link" href="#sn-15-s2">Library</a>
        <a class="sn-15__link" href="#sn-15-s3">Devices</a>
      </nav>
      <button class="sn-15__icon" type="button" aria-label="Notifications, 3 unread">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M18 15.5V11a6 6 0 1 0-12 0v4.5L4.5 18h15L18 15.5zM10 20.5a2 2 0 0 0 4 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="sn-15__badge" aria-hidden="true">3</span>
      </button>
    </header>
  <div class="sn-15__intro">
    <div class="sn-15__introin">
    <p class="sn-15__intro-eyebrow">one light source · paired shadows</p>
    <h2 class="sn-15__intro-title">Soft UI with guardrails</h2>
    </div>
  </div>
    <main>
      <section class="sn-15__sec" id="sn-15-s1">
        <h3 class="sn-15__h">Two shadows, one source</h3>
        <p class="sn-15__p">A light highlight at the top-left and a matching dark shadow at the bottom-right. Equal offsets, opposite colours — anything else looks tilted rather than raised.</p>
        <div class="sn-15__row">
          <span class="sn-15__tile">raised</span>
          <span class="sn-15__tile sn-15__tile--in">inset</span>
          <span class="sn-15__tile sn-15__tile--flat">flat</span>
        </div>
      </section>
      <section class="sn-15__sec" id="sn-15-s2">
        <h3 class="sn-15__h">Pressed means inset</h3>
        <p class="sn-15__p">The active nav item inverts both shadows so it sits inside the panel — and changes colour and weight too, because depth alone is invisible to plenty of users.</p>
      </section>
      <section class="sn-15__sec" id="sn-15-s3">
        <h3 class="sn-15__h">Focus needs a real outline</h3>
        <p class="sn-15__p">Soft shadows vanish in forced-colours mode. Every control here draws a genuine outline on <code>:focus-visible</code>, and <code>prefers-contrast: more</code> swaps the shadows for solid borders.</p>
      </section>
    </main>
  <footer class="sn-15__pagefoot">
    <p class="sn-15__pagefootin">Sticky navigation pattern 15 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-15-bg);
  --sn-15-bg: oklch(0.925 0.008 265);
  --sn-15-lit: oklch(1 0 0);
  --sn-15-dim: oklch(0.78 0.016 265);
  --sn-15-ink: oklch(0.3 0.024 265);
  --sn-15-mut: oklch(0.48 0.02 265);
  --sn-15-acc: oklch(0.52 0.16 285);
  --sn-15-h: 74px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-15-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-15 *,
.sn-15 *::before,
.sn-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-15__eyebrow,
.sn-15__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-15-acc);
}

.sn-15__title,
.sn-15__intro-title {
  font-size: clamp(23px,3.5vw,36px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-15__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,20px);
  min-height: var(--sn-15-h);
  padding: 0 clamp(14px,2.6vw,22px);
  background: var(--sn-15-bg);
  box-shadow: 0 8px 18px -12px var(--sn-15-dim);
}

.sn-15__brand {
  display: flex;
  align-items: center;
  gap: 11px;
  font-size: 15.5px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sn-15__logo {
  width: 34px;
  height: 34px;
  border-radius: 12px;
  background: var(--sn-15-bg);
  box-shadow: -4px -4px 8px var(--sn-15-lit),4px 4px 10px var(--sn-15-dim);
}

.sn-15__nav {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-inline-start: auto;
}

.sn-15__link {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 14px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-15-mut);
  text-decoration: none;
  background: var(--sn-15-bg);
  box-shadow: -4px -4px 9px var(--sn-15-lit),4px 4px 10px var(--sn-15-dim);
  transition: box-shadow .22s ease,color .18s ease;
}

.sn-15__link:hover {
  color: var(--sn-15-ink);
  box-shadow: -2px -2px 6px var(--sn-15-lit),2px 2px 7px var(--sn-15-dim);
}

.sn-15__link[aria-current="page"] {
  color: var(--sn-15-acc);
  font-weight: 700;
  box-shadow: inset -3px -3px 7px var(--sn-15-lit),inset 3px 3px 7px var(--sn-15-dim);
}

.sn-15__icon {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 0;
  border-radius: 14px;
  background: var(--sn-15-bg);
  color: var(--sn-15-mut);
  cursor: pointer;
  box-shadow: -4px -4px 9px var(--sn-15-lit),4px 4px 10px var(--sn-15-dim);
  transition: box-shadow .22s ease,color .18s ease;
}

.sn-15__icon:hover {
  color: var(--sn-15-ink);
}

.sn-15__icon:active {
  box-shadow: inset -3px -3px 7px var(--sn-15-lit),inset 3px 3px 7px var(--sn-15-dim);
}

.sn-15__icon svg {
  inline-size: 19px;
  block-size: 19px;
}

.sn-15__badge {
  position: absolute;
  inset-block-start: 6px;
  inset-inline-end: 6px;
  display: grid;
  place-items: center;
  min-inline-size: 16px;
  block-size: 16px;
  padding-inline: 4px;
  border-radius: 99px;
  background: var(--sn-15-acc);
  color: oklch(1 0 0);
  font-size: 10px;
  font-weight: 700;
}

.sn-15__link:focus-visible,
.sn-15__icon:focus-visible,
.sn-15__brand:focus-visible {
  outline: 2.5px solid var(--sn-15-acc);
  outline-offset: 3px;
}

.sn-15__sec {
  scroll-margin-top: var(--sn-15-h);
  display: grid;
  gap: 12px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(26px,4.4vw,50px);
}

.sn-15__h {
  font-size: clamp(19px,2.6vw,25px);
  line-height: 1.18;
  letter-spacing: -.025em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-15__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.68;
  color: var(--sn-15-mut);
  text-wrap: pretty;
}

.sn-15__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  padding: 2px 7px;
  border-radius: 6px;
  background: var(--sn-15-bg);
  box-shadow: inset -2px -2px 4px var(--sn-15-lit),inset 2px 2px 4px var(--sn-15-dim);
}

.sn-15__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-block-start: 4px;
}

.sn-15__tile {
  display: grid;
  place-items: center;
  min-inline-size: 92px;
  min-block-size: 44px;
  padding-inline: 14px;
  border-radius: 14px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sn-15-mut);
  background: var(--sn-15-bg);
  box-shadow: -4px -4px 9px var(--sn-15-lit),4px 4px 10px var(--sn-15-dim);
}

.sn-15__tile--in {
  box-shadow: inset -3px -3px 7px var(--sn-15-lit),inset 3px 3px 7px var(--sn-15-dim);
}

.sn-15__tile--flat {
  box-shadow: none;
  border: 1px solid oklch(0.3 0.024 265/.14);
}

@media (prefers-contrast: more) {
  .sn-15__link,
    .sn-15__icon,
    .sn-15__logo,
    .sn-15__tile {
    box-shadow: none;
    border: 2px solid var(--sn-15-ink);
  }

  .sn-15__link[aria-current="page"] {
    background: var(--sn-15-acc);
    color: oklch(1 0 0);
  }
}

@media (max-width: 560px) {
  .sn-15__nav {
    gap: 5px;
  }

  .sn-15__link {
    padding: 0 12px;
    font-size: 12.8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-15 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-15) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-15-h) + 10px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-15) {
    scroll-behavior: auto;
  }
}

.sn-15__bar,
.sn-15__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-15__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-15__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
}

.sn-15__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-15__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-15__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-15__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-15__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-15-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-15-mut);
  animation: sn-15-cue 2.6s ease-in-out infinite;
}

@keyframes sn-15-cue {
  0%,
    100% {
    transform: translateY(0);
    opacity: .75;
  }

  50% {
    transform: translateY(5px);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-15__intro::after {
    animation: none;
  }
}

.sn-15__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-15-line);
}

.sn-15__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-15-mut);
  text-align: center;
}

.sn-15__intro-title,
.sn-15__intro-sub {
  text-wrap: balance;
}
```
