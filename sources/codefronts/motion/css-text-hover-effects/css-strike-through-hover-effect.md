---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/css-strike-through-hover-effect/"
title: "CSS Strike-Through Hover Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "text-decoration:line-through cannot animate — so every animated strike you've admired is a scaleX'd pseudo-element, and this demo ships the three that…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Strike-Through Hover Effect
Source: https://codefronts.com/motion/css-text-hover-effects/css-strike-through-hover-effect/

text-decoration:line-through cannot animate — so every animated strike you've admired is a scaleX'd pseudo-element, and this demo ships the three that matter: an e-commerce compare-at price whose old number gets crossed out as you hover the buy row, a task list where :has(:checked) draws a persistent strike the moment the checkbox ticks, and a sold-out nav link whose line enters left and exits right. The line is currentColor-independent, em-scaled, and slightly rotated so it reads as a pencil stroke, not a border.
## HTML
```html
<section class="cth-04" aria-label="Animated strike-through demo">
  <div class="cth-04__stage">
    <div class="cth-04__scene">
      <article class="cth-04__card">
        <header class="cth-04__cardhead">
          <h2>Studio membership</h2><span class="cth-04__badge">Spring pricing</span>
        </header>
        <a class="cth-04__buy" href="#cth04-top" id="cth04-top">
          <span class="cth-04__prices"><s class="cth-04__old"><span class="cth-04__strike">$79</span></s><b class="cth-04__new">$49<small>/mo</small></b></span>
          <span class="cth-04__cta">Lock it in &rarr;</span>
        </a>
        <p class="cth-04__note">Hover the row: the compare-at price is crossed out while you aim at the button.</p>
      </article>
      <div class="cth-04__split">
        <ul class="cth-04__todos" aria-label="Launch checklist">
          <li><label><input type="checkbox" checked><i aria-hidden="true"></i><span class="cth-04__strike">Freeze the type scale</span></label></li>
          <li><label><input type="checkbox"><i aria-hidden="true"></i><span class="cth-04__strike">Ship dark mode tokens</span></label></li>
          <li><label><input type="checkbox"><i aria-hidden="true"></i><span class="cth-04__strike">Audit hover states</span></label></li>
        </ul>
        <nav class="cth-04__nav" aria-label="Editions">
          <a href="#cth04-top">Spring drop</a>
          <a class="cth-04__gone" href="#cth04-top" aria-label="Winter drop, sold out">Winter drop<em aria-hidden="true">sold out</em></a>
        </nav>
      </div>
      <p class="cth-04__hint">Tick the boxes &mdash; <code>li:has(:checked)</code> draws the strike with zero JS. The sold-out link's line enters left, exits right.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-04,
.cth-04 *,
.cth-04 *::before,
.cth-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-04 {
  --bg: oklch(0.972 0.008 85);
  --ink: oklch(0.26 0.02 55);
  --mut: oklch(0.53 0.02 60);
  --pen: oklch(0.55 0.21 27);
  --line: oklch(0.88 0.014 80);
  --card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-04__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth04/inline-size;
}

.cth-04__scene {
  width: min(100%,720px);
  display: flex;
  flex-direction: column;
  gap: clamp(16px,3cqi,24px);
}

.cth-04__strike {
  position: relative;
  display: inline-block;
}

.cth-04__strike::after {
  content: '';
  position: absolute;
  left: -3%;
  right: -3%;
  top: calc(50% - .045em);
  height: .09em;
  border-radius: .05em;
  background: var(--pen);
  rotate: -1.5deg;
  transform: scaleX(0);
  transform-origin: 0 50%;
  transition: transform .35s cubic-bezier(.65,.05,.36,1);
}

.cth-04__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: clamp(18px,3.4cqi,28px);
  box-shadow: 0 14px 40px oklch(0.4 0.04 60/.08);
}

.cth-04__cardhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.cth-04__cardhead h2 {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cth-04__badge {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--pen);
  border: 1px solid color-mix(in oklch,var(--pen) 40%,transparent);
  border-radius: 99px;
  padding: 4px 10px;
}

.cth-04__buy {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-top: 16px;
  padding: 14px 18px;
  min-height: 64px;
  border: 1.5px solid var(--line);
  border-radius: 13px;
  text-decoration: none;
  color: inherit;
  transition: border-color .3s,background .3s;
}

.cth-04__buy:hover,
.cth-04__buy:focus-visible {
  border-color: var(--ink);
  background: oklch(0.985 0.005 85);
}

.cth-04__buy:focus-visible {
  outline: 2px solid var(--pen);
  outline-offset: 3px;
}

.cth-04__prices {
  display: flex;
  align-items: baseline;
  gap: 14px;
}

.cth-04__old {
  text-decoration: none;
  font-size: clamp(19px,3cqi,24px);
  font-weight: 650;
  color: var(--mut);
  transition: color .35s;
}

.cth-04__new {
  font-size: clamp(26px,4.4cqi,36px);
  font-weight: 850;
  letter-spacing: -.02em;
}

.cth-04__new small {
  font-size: .5em;
  font-weight: 650;
  color: var(--mut);
}

.cth-04__buy:hover .cth-04__strike::after,
.cth-04__buy:focus-visible .cth-04__strike::after {
  transform: scaleX(1);
}

.cth-04__buy:hover .cth-04__old,
.cth-04__buy:focus-visible .cth-04__old {
  color: color-mix(in oklch,var(--mut) 55%,transparent);
}

.cth-04__cta {
  font-size: 14.5px;
  font-weight: 750;
  color: var(--pen);
  white-space: nowrap;
}

.cth-04__note {
  margin-top: 12px;
  font-size: 12.5px;
  color: var(--mut);
}

.cth-04__split {
  display: grid;
  grid-template-columns: 1.25fr 1fr;
  gap: clamp(14px,2.6cqi,22px);
  align-items: start;
}

.cth-04__todos {
  list-style: none;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 8px;
  display: flex;
  flex-direction: column;
}

.cth-04__todos label {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 48px;
  padding: 0 12px;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: background .25s,color .4s;
}

.cth-04__todos label:hover {
  background: oklch(0.965 0.008 85);
}

.cth-04__todos input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cth-04__todos i {
  width: 19px;
  height: 19px;
  flex: none;
  border: 1.7px solid var(--mut);
  border-radius: 6px;
  display: grid;
  place-items: center;
  transition: border-color .25s,background .25s;
}

.cth-04__todos i::before {
  content: '';
  width: 9px;
  height: 5px;
  border-left: 2px solid var(--card);
  border-bottom: 2px solid var(--card);
  rotate: -45deg;
  translate: 0 -1px;
  opacity: 0;
  transition: opacity .2s;
}

.cth-04__todos li:has(:checked) i {
  background: var(--pen);
  border-color: var(--pen);
}

.cth-04__todos li:has(:checked) i::before {
  opacity: 1;
}

.cth-04__todos li:has(:checked) label {
  color: color-mix(in oklch,var(--mut) 70%,transparent);
}

.cth-04__todos li:has(:checked) .cth-04__strike::after {
  transform: scaleX(1);
}

.cth-04__todos label:has(:focus-visible) {
  outline: 2px solid var(--pen);
  outline-offset: -2px;
}

.cth-04__nav {
  display: flex;
  flex-direction: column;
  gap: 6px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 14px;
}

.cth-04__nav a {
  position: relative;
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  padding: 0 10px;
  font-size: 16px;
  font-weight: 750;
  letter-spacing: -.01em;
  color: inherit;
  text-decoration: none;
  border-radius: 9px;
}

.cth-04__nav a:hover,
.cth-04__nav a:focus-visible {
  background: oklch(0.965 0.008 85);
}

.cth-04__nav a:focus-visible {
  outline: 2px solid var(--pen);
  outline-offset: -2px;
}

.cth-04__gone {
  color: var(--mut);
}

.cth-04__gone em {
  font-style: normal;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--pen);
}

.cth-04__gone::after {
  content: '';
  position: absolute;
  left: 6px;
  width: calc(100% - 90px);
  top: calc(50% - .5px);
  height: 2px;
  border-radius: 2px;
  background: var(--pen);
  transform: scaleX(0);
  transform-origin: 0 50%;
  transition: transform .4s cubic-bezier(.65,.05,.36,1);
}

.cth-04__gone:hover::after,
.cth-04__gone:focus-visible::after {
  transform: scaleX(1);
}

.cth-04__gone:not(:hover):not(:focus-visible)::after {
  transform-origin: 100% 50%;
}

.cth-04__hint {
  font-size: 12.5px;
  color: var(--mut);
}

.cth-04__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.93 0.012 85);
  padding: 1px 6px;
  border-radius: 4px;
}

@container cth04 (width < 600px) {
  .cth-04__split {
    grid-template-columns: 1fr;
  }

  .cth-04__buy {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cth-04 *,
    .cth-04 *::after {
    transition-duration: .01ms !important;
  }
}
```
