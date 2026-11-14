---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/css-expand-collapse-card-pure-css-height-auto/"
title: "CSS Expand Collapse Card (Pure CSS Height Auto)"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Animating to height: auto — the oldest impossible thing in CSS — solved twice over."
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Expand Collapse Card (Pure CSS Height Auto)
Source: https://codefronts.com/components/css-animated-cards/css-expand-collapse-card-pure-css-height-auto/

Animating to height: auto — the oldest impossible thing in CSS — solved twice over. The modern route is one line, interpolate-size: allow-keywords, which makes intrinsic keywords animatable. The universal route is the grid-template-rows: 0fr → 1fr trick. Both are wired to real <details> elements, so keyboard, screen reader and find-in-page all work with zero JavaScript.
## HTML
```html
<section class="ac-09" aria-label="CSS expand collapse card demo">
  <div class="ac-09__stage">
    <header class="ac-09__head">
      <p class="ac-09__eyebrow">Disclosure</p>
      <h2 class="ac-09__title">Animating to height: auto, without JavaScript</h2>
      <p class="ac-09__sub">Real <code>&lt;details&gt;</code> elements. Keyboard, find-in-page and screen readers all work.</p>
    </header>
    <div class="ac-09__list">
      <details class="ac-09__card" name="ac-09" open>
        <summary class="ac-09__sum">
          <span class="ac-09__ico" aria-hidden="true">01</span>
          <span class="ac-09__q">What exactly does interpolate-size do?</span>
          <svg class="ac-09__chev" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
        </summary>
        <div class="ac-09__panel"><div class="ac-09__inner">
          <p>It opts an element and its descendants into animating intrinsic size keywords — <code>auto</code>, <code>min-content</code>, <code>max-content</code>, <code>fit-content</code>. Before it, a transition to <code>height: auto</code> was a discrete jump; with it, the engine resolves the keyword each frame and interpolates properly.</p>
        </div></div>
      </details>
      <details class="ac-09__card" name="ac-09">
        <summary class="ac-09__sum">
          <span class="ac-09__ico" aria-hidden="true">02</span>
          <span class="ac-09__q">Why does the grid 0fr → 1fr trick still matter?</span>
          <svg class="ac-09__chev" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
        </summary>
        <div class="ac-09__panel"><div class="ac-09__inner">
          <p>Because it works everywhere, today. A grid track sized in <code>fr</code> is an animatable length under the hood, so transitioning <code>grid-template-rows</code> from <code>0fr</code> to <code>1fr</code> grows the row from nothing to exactly its content height — as long as the child clips with <code>overflow: hidden</code>.</p>
        </div></div>
      </details>
      <details class="ac-09__card" name="ac-09">
        <summary class="ac-09__sum">
          <span class="ac-09__ico" aria-hidden="true">03</span>
          <span class="ac-09__q">Can one panel close when another opens?</span>
          <svg class="ac-09__chev" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
        </summary>
        <div class="ac-09__panel"><div class="ac-09__inner">
          <p>Yes — give every <code>&lt;details&gt;</code> in the group the same <code>name</code> attribute, exactly like radio buttons. The browser enforces one-open-at-a-time natively. These three cards use <code>name="ac-09"</code>; try opening a second one.</p>
        </div></div>
      </details>
      <details class="ac-09__card" name="ac-09">
        <summary class="ac-09__sum">
          <span class="ac-09__ico" aria-hidden="true">04</span>
          <span class="ac-09__q">What breaks if I animate height with JavaScript instead?</span>
          <svg class="ac-09__chev" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
        </summary>
        <div class="ac-09__panel"><div class="ac-09__inner">
          <p>Measuring <code>scrollHeight</code> forces a synchronous layout on every open, goes stale when fonts load or the viewport resizes mid-animation, and needs a resize observer to stay correct. The CSS routes have none of those failure modes.</p>
        </div></div>
      </details>
    </div>
    <p class="ac-09__chip" aria-hidden="true">interpolate-size:allow-keywords · grid-template-rows 0fr→1fr fallback · ::details-content · name= exclusive accordion</p>
  </div>
</section>
```
## CSS
```css
.ac-09,
.ac-09 *,
.ac-09 *::before,
.ac-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-09 {
  interpolate-size: allow-keywords;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-09-bg: oklch(0.97 0.008 250);
  --ac-09-card: oklch(1 0 0);
  --ac-09-ink: oklch(0.22 0.02 260);
  --ac-09-mut: oklch(0.53 0.02 260);
  --ac-09-acc: oklch(0.52 0.16 250);
  --ac-09-line: oklch(0.22 0.02 260/.11);
  background: var(--ac-09-bg);
  color: var(--ac-09-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.6vw,26px);
  padding: clamp(20px,5vw,58px);
}

.ac-09__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
  max-width: 56ch;
}

.ac-09__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-09-acc);
}

.ac-09__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-09__sub {
  font-size: 14px;
  color: var(--ac-09-mut);
  text-wrap: pretty;
}

.ac-09__sub code,
.ac-09__inner code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  background: oklch(0.22 0.02 260/.07);
  padding: 2px 6px;
  border-radius: 6px;
}

.ac-09__list {
  display: grid;
  gap: 10px;
  width: min(100%,660px);
}

.ac-09__card {
  border: 1px solid var(--ac-09-line);
  border-radius: 16px;
  background: var(--ac-09-card);
  overflow: hidden;
  transition: box-shadow .3s,border-color .3s;
}

.ac-09__card[open] {
  border-color: color-mix(in oklch,var(--ac-09-acc) 38%,transparent);
  box-shadow: 0 16px 34px -24px oklch(0.22 0.02 260/.7);
}

.ac-09__sum {
  display: flex;
  align-items: center;
  gap: 13px;
  min-height: 60px;
  padding: 12px 16px;
  cursor: pointer;
  list-style: none;
  transition: background .2s;
}

.ac-09__sum::-webkit-details-marker {
  display: none;
}

.ac-09__sum:hover {
  background: oklch(0.22 0.02 260/.035);
}

.ac-09__sum:focus-visible {
  outline: 2px solid var(--ac-09-acc);
  outline-offset: -2px;
  border-radius: 16px;
}

.ac-09__ico {
  flex: none;
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  border-radius: 9px;
  background: color-mix(in oklch,var(--ac-09-acc) 13%,transparent);
  color: var(--ac-09-acc);
  font-size: 11.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.ac-09__q {
  flex: 1;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: -.015em;
  line-height: 1.35;
  text-wrap: pretty;
}

.ac-09__chev {
  flex: none;
  color: var(--ac-09-mut);
  transition: rotate .38s cubic-bezier(.16,1,.3,1),color .2s;
}

.ac-09__card[open] .ac-09__chev {
  rotate: 180deg;
  color: var(--ac-09-acc);
}

.ac-09__panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .42s cubic-bezier(.16,1,.3,1);
}

.ac-09__card[open] .ac-09__panel {
  grid-template-rows: 1fr;
}

.ac-09__inner {
  overflow: hidden;
  opacity: 0;
  transition: opacity .3s ease .04s;
}

.ac-09__card[open] .ac-09__inner {
  opacity: 1;
}

.ac-09__inner p {
  padding: 0 16px 18px 59px;
  font-size: 14px;
  line-height: 1.62;
  color: var(--ac-09-mut);
  text-wrap: pretty;
}

@supports (height: calc-size(auto,size)) {
  .ac-09__panel {
    display: block;
    height: 0;
    overflow: hidden;
    grid-template-rows: none;
    transition: height .42s cubic-bezier(.16,1,.3,1);
  }

  .ac-09__card[open] .ac-09__panel {
    height: auto;
  }
}

.ac-09__card::details-content {
  transition: content-visibility .42s allow-discrete,block-size .42s cubic-bezier(.16,1,.3,1);
}

.ac-09__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-09-mut);
  padding: 8px 15px;
  border: 1px dashed var(--ac-09-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,700px);
}

@media (max-width: 520px) {
  .ac-09__inner p {
    padding-left: 16px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ac-09 * {
    transition-duration: .01ms !important;
  }
}
```
