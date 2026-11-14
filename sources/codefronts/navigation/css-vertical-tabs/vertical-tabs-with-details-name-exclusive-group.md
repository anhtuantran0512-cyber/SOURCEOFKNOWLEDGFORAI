---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-details-name-exclusive-group/"
title: "Vertical Tabs with <details name=\"\"> Exclusive Group"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "The feature that finally deleted the accordion script: give a group of <details> elements the same name and the browser enforces one-open-at-a-time, exactly…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tabs with <details name=""> Exclusive Group
Source: https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-details-name-exclusive-group/

The feature that finally deleted the accordion script: give a group of <details> elements the same name and the browser enforces one-open-at-a-time, exactly like radio buttons. Paired with ::details-content, interpolate-size and @starting-style, you get a fully animated exclusive tab stack in pure HTML and CSS.
## HTML
```html
<section class="vt-15" aria-label="Exclusive details group vertical tabs demo">
  <div class="vt-15__stage">
    <div class="vt-15__head">
      <p class="vt-15__eyebrow">&lt;details name&gt; · ::details-content · @starting-style</p>
      <h2 class="vt-15__title">Exclusive tabs in four attributes</h2>
    </div>
    <div class="vt-15__set">
      <details class="vt-15__item" name="vt-15" open>
        <summary class="vt-15__sum"><span class="vt-15__idx">01</span><span class="vt-15__lbl">The name attribute</span><i class="vt-15__mark" aria-hidden="true"></i></summary>
        <div class="vt-15__body"><p class="vt-15__p">Matching <code>name</code> values make the group exclusive — opening one closes the rest. Unlike radios, clicking the open item closes it, so “none open” is a valid state.</p></div>
      </details>
      <details class="vt-15__item" name="vt-15">
        <summary class="vt-15__sum"><span class="vt-15__idx">02</span><span class="vt-15__lbl">Animating the impossible</span><i class="vt-15__mark" aria-hidden="true"></i></summary>
        <div class="vt-15__body"><p class="vt-15__p"><code>::details-content</code> targets the wrapper the browser generates around everything after the summary — the box that never existed for CSS before.</p></div>
      </details>
      <details class="vt-15__item" name="vt-15">
        <summary class="vt-15__sum"><span class="vt-15__idx">03</span><span class="vt-15__lbl">height: auto, transitioned</span><i class="vt-15__mark" aria-hidden="true"></i></summary>
        <div class="vt-15__body"><p class="vt-15__p"><code>interpolate-size:allow-keywords</code> opts the page into interpolating intrinsic sizes, which finally makes <code>block-size:auto</code> a legal transition endpoint.</p></div>
      </details>
      <details class="vt-15__item" name="vt-15">
        <summary class="vt-15__sum"><span class="vt-15__idx">04</span><span class="vt-15__lbl">allow-discrete</span><i class="vt-15__mark" aria-hidden="true"></i></summary>
        <div class="vt-15__body"><p class="vt-15__p">Without <code>transition-behavior:allow-discrete</code>, <code>content-visibility</code> flips instantly and the content vanishes before the height has finished collapsing.</p></div>
      </details>
      <details class="vt-15__item" name="vt-15">
        <summary class="vt-15__sum"><span class="vt-15__idx">05</span><span class="vt-15__lbl">Nothing to hydrate</span><i class="vt-15__mark" aria-hidden="true"></i></summary>
        <div class="vt-15__body"><p class="vt-15__p">Strip every enhancement and four HTML attributes still give you a working, keyboard-operable, screen-reader-correct exclusive accordion.</p></div>
      </details>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-15-bg);
  --vt-15-bg: oklch(0.97 0.008 30);
  --vt-15-card: oklch(1 0 0);
  --vt-15-ink: oklch(0.22 0.03 25);
  --vt-15-mut: oklch(0.54 0.028 25);
  --vt-15-acc: oklch(0.55 0.2 22);
  --vt-15-line: oklch(0.22 0.03 25/.12);
  interpolate-size: allow-keywords;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-15-ink);
}

.vt-15 *,
.vt-15 *::before,
.vt-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-15__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(18px,3vw,30px);
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(75% 55% at 50% 0%,oklch(0.95 0.04 30/.8),transparent);
}

.vt-15__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
  max-width: 54ch;
}

.vt-15__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--vt-15-acc);
}

.vt-15__title {
  font-size: clamp(24px,3.6vw,40px);
  line-height: 1.06;
  letter-spacing: -.032em;
  font-weight: 720;
  text-wrap: balance;
}

.vt-15__set {
  width: min(94vw,720px);
  background: var(--vt-15-card);
  border: 1px solid var(--vt-15-line);
  border-radius: 18px;
  box-shadow: 0 24px 64px -32px oklch(0.22 0.03 25/.4);
  overflow: hidden;
}

.vt-15__item+.vt-15__item {
  border-top: 1px solid var(--vt-15-line);
}

.vt-15__sum {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 60px;
  padding: 0 20px;
  font-size: 15.4px;
  font-weight: 640;
  color: var(--vt-15-mut);
  cursor: pointer;
  list-style: none;
  transition: color .2s ease,background .2s ease;
}

.vt-15__sum::-webkit-details-marker {
  display: none;
}

.vt-15__idx {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .05em;
  opacity: .5;
}

.vt-15__lbl {
  flex: 1 1 auto;
  min-inline-size: 0;
}

.vt-15__mark {
  position: relative;
  inline-size: 18px;
  block-size: 18px;
  flex: none;
  opacity: .6;
}

.vt-15__mark::before,
.vt-15__mark::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  background: currentColor;
  border-radius: 2px;
  translate: -50% -50%;
  transition: rotate .34s cubic-bezier(.32,.72,.3,1),opacity .28s ease;
}

.vt-15__mark::before {
  inline-size: 13px;
  block-size: 2px;
}

.vt-15__mark::after {
  inline-size: 2px;
  block-size: 13px;
}

.vt-15__sum:hover {
  color: var(--vt-15-ink);
  background: oklch(0.22 0.03 25/.035);
}

.vt-15__sum:focus-visible {
  outline: 2px solid var(--vt-15-acc);
  outline-offset: -3px;
}

.vt-15__item[open]>.vt-15__sum {
  color: var(--vt-15-acc);
  box-shadow: inset 3px 0 0 var(--vt-15-acc);
}

.vt-15__item[open]>.vt-15__sum .vt-15__mark {
  opacity: 1;
}

.vt-15__item[open]>.vt-15__sum .vt-15__mark::after {
  rotate: 90deg;
  opacity: 0;
}

.vt-15__item[open]>.vt-15__sum .vt-15__mark::before {
  rotate: 180deg;
}

.vt-15__body {
  padding: 0 20px 20px 52px;
}

.vt-15__p {
  max-width: 58ch;
  font-size: 14.8px;
  line-height: 1.68;
  color: var(--vt-15-mut);
  text-wrap: pretty;
}

.vt-15__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: color-mix(in oklch,var(--vt-15-acc) 10%,transparent);
  color: var(--vt-15-acc);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-15__item::details-content {
  block-size: 0;
  overflow: hidden;
  opacity: 0;
  transition: block-size .35s cubic-bezier(.32,.72,.3,1),opacity .3s ease,content-visibility .35s allow-discrete;
}

.vt-15__item[open]::details-content {
  block-size: auto;
  opacity: 1;
}

@starting-style {
  .vt-15__item[open]::details-content {
    block-size: 0;
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-15 * {
    transition-duration: .01ms !important;
  }
}
```
