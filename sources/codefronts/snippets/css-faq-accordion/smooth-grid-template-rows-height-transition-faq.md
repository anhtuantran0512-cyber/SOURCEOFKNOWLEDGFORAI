---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/smooth-grid-template-rows-height-transition-faq/"
title: "Smooth grid-template-rows Height Transition FAQ"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The technique demo: how grid-template-rows: 0fr → 1fr finally solved CSS's oldest animation problem — transitioning to height:auto."
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Smooth grid-template-rows Height Transition FAQ
Source: https://codefronts.com/snippets/css-faq-accordion/smooth-grid-template-rows-height-transition-faq/

The technique demo: how grid-template-rows: 0fr → 1fr finally solved CSS's oldest animation problem — transitioning to height:auto. This FAQ dissects its own animation: each open panel shows a live annotation of the current track value, and the answers themselves teach why max-height hacks break, why fr units interpolate, and how the one mandatory overflow:hidden wrapper works. Copy the pattern from any demo in this collection; read this one to actually understand it.
## HTML
```html
<section class="cfa-10" aria-label="grid-template-rows height transition FAQ">
  <div class="cfa-10__wrap">
    <header class="cfa-10__head">
      <span class="cfa-10__chip">grid-template-rows: 0fr → 1fr</span>
      <h1>Animating to height: auto</h1>
      <p>The accordion that explains its own animation. Watch the track annotation as panels open.</p>
    </header>
    <div class="cfa-10__list">
      <div class="cfa-10__item">
        <input type="checkbox" id="cfa10-q1" class="cfa-10__cb" checked>
        <label class="cfa-10__q" for="cfa10-q1">Why doesn't height: auto animate?<i aria-hidden="true"></i></label>
        <div class="cfa-10__a"><div class="cfa-10__inner"><p>Because <code>auto</code> is a keyword, not a number — the engine has nothing to interpolate between 0px and “whatever it turns out to be”. Fraction units sidestep this: <code>0fr → 1fr</code> is a numeric share of the content's size, resolved to real pixels every frame.</p><span class="cfa-10__track" aria-hidden="true">grid-template-rows: <b>1fr</b> · height resolved per frame</span></div></div>
      </div>
      <div class="cfa-10__item">
        <input type="checkbox" id="cfa10-q2" class="cfa-10__cb">
        <label class="cfa-10__q" for="cfa10-q2">What's wrong with max-height: 500px?<i aria-hidden="true"></i></label>
        <div class="cfa-10__a"><div class="cfa-10__inner"><p>It animates to 500px, not to your content. Short answers finish early then “wait” invisibly; long answers get clipped. Every max-height accordion has a magic number that is wrong for someone's content, font size, or translation.</p><span class="cfa-10__track" aria-hidden="true">this panel needed no magic number</span></div></div>
      </div>
      <div class="cfa-10__item">
        <input type="checkbox" id="cfa10-q3" class="cfa-10__cb">
        <label class="cfa-10__q" for="cfa10-q3">Why the extra inner wrapper?<i aria-hidden="true"></i></label>
        <div class="cfa-10__a"><div class="cfa-10__inner"><p>Grid items refuse to shrink below <code>min-content</code> by default — a 0fr track with an unclippable child still renders tall. <code>overflow: hidden</code> (plus <code>min-height: 0</code>) on the direct child releases that constraint. Forget it and the accordion “never closes”.</p><span class="cfa-10__track" aria-hidden="true">.inner { overflow: hidden; min-height: 0 }</span></div></div>
      </div>
      <div class="cfa-10__item">
        <input type="checkbox" id="cfa10-q4" class="cfa-10__cb">
        <label class="cfa-10__q" for="cfa10-q4">Does this work with really long content?<i aria-hidden="true"></i></label>
        <div class="cfa-10__a"><div class="cfa-10__inner"><p>Yes — that is the whole point. This answer is deliberately longer to prove it: the track interpolates shares, not pixels, so a two-line answer and a twelve-line answer both animate over the same 500 milliseconds with the same easing, and the browser resolves the actual height continuously during the transition. Resize the pane mid-animation; it self-corrects. Add another paragraph tomorrow; nothing to update. That is what “no magic numbers” buys you in maintenance terms.</p><span class="cfa-10__track" aria-hidden="true">same .5s regardless of content length</span></div></div>
      </div>
    </div>
    <p class="cfa-10__foot">Same pattern rotated 90° = demo 15's horizontal accordion (<code>grid-template-columns</code>). CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-10,
.cfa-10 *,
.cfa-10 *::before,
.cfa-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-10 {
  --bg: oklch(0.16 0.015 220);
  --panel: oklch(0.21 0.02 220);
  --ink: oklch(0.95 0.008 210);
  --mut: oklch(0.67 0.02 215);
  --line: oklch(0.31 0.025 218);
  --acc: oklch(0.8 0.14 190);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: radial-gradient(1000px 500px at 100% 100%,oklch(0.22 0.05 190/.5),transparent 55%),var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-10__wrap {
  width: min(100%,680px);
}

.cfa-10__chip {
  display: inline-block;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  font-weight: 600;
  color: var(--acc);
  padding: 7px 13px;
  background: color-mix(in oklch,var(--acc) 12%,transparent);
  border-radius: 99px;
}

.cfa-10__head h1 {
  margin-top: 14px;
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-10__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-10__list {
  margin-top: 26px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.cfa-10__item {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--panel);
  overflow: hidden;
  transition: border-color .3s;
}

.cfa-10__item:has(.cfa-10__cb:checked) {
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
}

.cfa-10__cb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cfa-10__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 16px 18px;
  cursor: pointer;
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.01em;
  transition: color .2s;
}

.cfa-10__q:hover {
  color: var(--acc);
}

.cfa-10__cb:focus-visible + .cfa-10__q {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 14px;
}

.cfa-10__q i {
  position: relative;
  flex: none;
  width: 22px;
  height: 22px;
}

.cfa-10__q i::before,
.cfa-10__q i::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  width: 12px;
  height: 2px;
  border-radius: 2px;
  background: var(--acc);
  transition: rotate .5s cubic-bezier(.4,0,.2,1);
}

.cfa-10__q i::after {
  rotate: 90deg;
}

.cfa-10__cb:checked + .cfa-10__q i::after {
  rotate: 0deg;
}

.cfa-10__cb:checked + .cfa-10__q i::before {
  rotate: 180deg;
}

.cfa-10__a {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .5s cubic-bezier(.4,0,.2,1);
}

.cfa-10__inner {
  overflow: hidden;
  min-height: 0;
}

.cfa-10__inner p {
  padding: 0 18px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 62ch;
}

.cfa-10__inner p code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: oklch(0.28 0.025 218);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.cfa-10__track {
  display: block;
  margin: 12px 18px 16px;
  padding: 8px 12px;
  border-left: 3px solid var(--acc);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 7%,transparent);
  border-radius: 0 8px 8px 0;
}

.cfa-10__track b {
  font-weight: 700;
}

.cfa-10__cb:checked ~ .cfa-10__a {
  grid-template-rows: 1fr;
}

.cfa-10__foot {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--mut);
}

.cfa-10__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: oklch(0.28 0.025 218);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-10 * {
    transition-duration: .01ms !important;
  }
}
```
