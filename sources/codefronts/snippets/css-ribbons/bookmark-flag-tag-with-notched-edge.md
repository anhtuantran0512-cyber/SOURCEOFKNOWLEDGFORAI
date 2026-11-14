---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/bookmark-flag-tag-with-notched-edge/"
title: "Bookmark Flag Tag with Notched Edge"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "The vertical bookmark: a flag that hangs from a rail with a V notched out of its bottom edge."
has_js: "true"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bookmark Flag Tag with Notched Edge
Source: https://codefronts.com/snippets/css-ribbons/bookmark-flag-tag-with-notched-edge/

The vertical bookmark: a flag that hangs from a rail with a V notched out of its bottom edge. Five points of clip-path make the shape, one --rib-10-notch variable controls the bite, and a companion price tag shows the other half of the technique — a punched hole made by subtracting a circle with mask-composite. Selecting a flag is pure CSS: hidden checkboxes and :has().
## HTML
```html
<section class="rib-10" aria-label="Bookmark flag tag with notched bottom edge demo">
  <div class="rib-10__stage">
    <div class="rib-10__panel">
      <div class="rib-10__rail" aria-hidden="true"></div>
      <div class="rib-10__flags" role="group" aria-label="Filter by collection">
        <label class="rib-10__flag" style="--rib-10-h:22"><input class="rib-10__box" type="checkbox" checked><span class="rib-10__ftxt">Sale</span></label>
        <label class="rib-10__flag" style="--rib-10-h:150"><input class="rib-10__box" type="checkbox"><span class="rib-10__ftxt">New in</span></label>
        <label class="rib-10__flag" style="--rib-10-h:262"><input class="rib-10__box" type="checkbox" checked><span class="rib-10__ftxt">Limited</span></label>
        <label class="rib-10__flag" style="--rib-10-h:82"><input class="rib-10__box" type="checkbox"><span class="rib-10__ftxt">Archive</span></label>
        <label class="rib-10__flag" style="--rib-10-h:310"><input class="rib-10__box" type="checkbox"><span class="rib-10__ftxt">Refurb</span></label>
      </div>
      <div class="rib-10__result">
        <p class="rib-10__count" role="status">2 collections selected</p>
        <div class="rib-10__pricetag">
          <span class="rib-10__pt-label">From</span>
          <span class="rib-10__pt-price">$42</span>
        </div>
      </div>
    </div>
    <p class="rib-10__chip" aria-hidden="true">5-point clip-path notch · calc apex · mask-composite: subtract hole · :has(:checked)</p>
  </div>
</section>
```
## CSS
```css
.rib-10,
.rib-10 *,
.rib-10 *::before,
.rib-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-10-bg: #eef0ee;
  --rib-10-bg: oklch(0.95 0.008 150);
  --rib-10-panel: #fff;
  --rib-10-panel: oklch(1 0 0);
  --rib-10-ink: #1e2320;
  --rib-10-ink: oklch(0.25 0.012 155);
  --rib-10-mut: #6c736e;
  --rib-10-mut: oklch(0.57 0.012 155);
  --rib-10-notch: 20px;
  background: var(--rib-10-bg);
  color: var(--rib-10-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,3vw,26px);
  padding: clamp(20px,5vw,56px);
}

.rib-10__panel {
  position: relative;
  width: min(100%,640px);
  padding: clamp(22px,4vw,34px);
  border-radius: 24px;
  background: var(--rib-10-panel);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 24px 56px -28px oklch(0.3 0.03 155/.5);
}

.rib-10__rail {
  height: 6px;
  border-radius: 99px;
  background: linear-gradient(90deg,oklch(0 0 0/.1),oklch(0 0 0/.16),oklch(0 0 0/.1));
  box-shadow: inset 0 1px 0 oklch(1 0 0/.5);
}

.rib-10__flags {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(8px,2vw,14px);
  margin-block-start: -3px;
  padding-block-start: 0;
}

.rib-10__flag {
  position: relative;
  flex: 1 1 92px;
  min-inline-size: 88px;
  display: grid;
  justify-items: center;
  padding-block: 16px calc(var(--rib-10-notch) + 12px);
  padding-inline: 10px;
  cursor: pointer;
  color: oklch(0.99 0 0);
  background: oklch(0.62 0.02 var(--rib-10-h,150));
  clip-path: polygon(0 0,100% 0,100% 100%,50% calc(100% - var(--rib-10-notch)),0 100%);
  filter: saturate(.35) brightness(1.02);
  transition: filter .35s cubic-bezier(.16,1,.3,1),translate .35s cubic-bezier(.16,1,.3,1),background .35s;
}

.rib-10__flag:hover {
  translate: 0 3px;
}

.rib-10__flag:has(:checked) {
  background: oklch(0.58 0.17 var(--rib-10-h,150));
  filter: saturate(1) brightness(1);
  translate: 0 8px;
}

.rib-10__flag:has(:focus-visible) {
  outline: 3px solid var(--rib-10-ink);
  outline-offset: -3px;
}

.rib-10__box {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.rib-10__ftxt {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .06em;
  text-shadow: 0 1px 2px oklch(0 0 0/.3);
  text-align: center;
}

.rib-10__flag::after {
  content: '';
  position: absolute;
  inset-block-start: 14px;
  inset-inline: 0;
  margin-inline: auto;
  inline-size: 10px;
  block-size: 10px;
  border-radius: 50%;
  background: oklch(1 0 0/.28);
  box-shadow: inset 0 1px 2px oklch(0 0 0/.4);
  opacity: 0;
  transition: opacity .3s;
}

.rib-10__flag:has(:checked)::after {
  opacity: 1;
}

.rib-10__flag:has(:checked) .rib-10__ftxt {
  padding-block-start: 16px;
}

.rib-10__result {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-block-start: clamp(30px,6vw,44px);
  padding-block-start: 20px;
  border-block-start: 1px solid oklch(0 0 0/.08);
}

.rib-10__count {
  font-size: 14px;
  color: var(--rib-10-mut);
  font-variant-numeric: tabular-nums;
}

.rib-10__pricetag {
  position: relative;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 20px 14px 46px;
  color: oklch(0.99 0 0);
  background: linear-gradient(105deg,oklch(0.42 0.11 155),oklch(0.52 0.14 150));
  clip-path: polygon(0 50%,22px 0,100% 0,100% 100%,22px 100%);
  -webkit-mask-image: linear-gradient(#000,#000),radial-gradient(circle 7px at 30px 50%,#000 98%,transparent);
  -webkit-mask-composite: source-out;
  mask-image: linear-gradient(#000,#000),radial-gradient(circle 7px at 30px 50%,#000 98%,transparent);
  mask-composite: subtract;
  filter: drop-shadow(0 8px 16px oklch(0.4 0.08 155/.35));
}

.rib-10__pt-label {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  opacity: .8;
}

.rib-10__pt-price {
  font-size: 21px;
  font-weight: 750;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.rib-10__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-10-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-10 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.rib-10__panel').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const boxes = [...panel.querySelectorAll('.rib-10__box')];
    const count = panel.querySelector('.rib-10__count');
    const price = panel.querySelector('.rib-10__pt-price');
    const update = () => {
      const n = boxes.filter((b) => b.checked).length;
      count.textContent = n === 0 ? 'No collections selected' : n + (n === 1 ? ' collection selected' : ' collections selected');
      price.textContent = '$' + (n ? 42 - n * 4 : 68);
    };
    boxes.forEach((b) => b.addEventListener('change', update));
    update();
  });
})();
```
