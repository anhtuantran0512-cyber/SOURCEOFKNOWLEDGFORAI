---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/faq-drawer/"
title: "CSS Accordion FAQ Footer Section"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "An FAQ block in the footer that answers the four questions your support inbox is full of — and does it in markup that can earn a rich result."
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Accordion FAQ Footer Section
Source: https://codefronts.com/layouts/css-footer-designs/faq-drawer/

An FAQ block in the footer that answers the four questions your support inbox is full of — and does it in markup that can earn a rich result. Native <details> disclosure, smooth panel animation, deep-linkable answers, and the JSON-LD you need for FAQPage.
## HTML
```html
<section class="ft-22" aria-label="Accordion FAQ footer demo">
  <main class="ft-22__main">
    <p class="ft-22__eyebrow">&lt;details&gt; · FAQPage JSON-LD</p>
    <h1 class="ft-22__title">The four questions before checkout</h1>
    <p class="ft-22__sub">Native disclosure means Ctrl+F finds text inside closed answers and opens them — something no hand-rolled accordion does for free.</p>
  </main>
  <footer class="ft-22__foot">
    <section class="ft-22__faq" aria-labelledby="ft-22-h">
      <div class="ft-22__intro">
        <h2 class="ft-22__h" id="ft-22-h">Frequently asked</h2>
        <p class="ft-22__isub">Still stuck? <a class="ft-22__inline" href="#ft-22-a">Talk to a human</a> — median reply 41 minutes.</p>
      </div>
      <div class="ft-22__items">
        <details class="ft-22__d" id="ft-22-shipping" name="ft-22-faq" open>
          <summary class="ft-22__sum"><span>How long does delivery take, and what does it cost?</span><span class="ft-22__plus" aria-hidden="true"></span></summary>
          <div class="ft-22__panel"><div class="ft-22__panelin"><p class="ft-22__a">Orders placed before 18:00 ship the same working day. UK next-day is free over £40 and £3.95 below it; EU is 2–4 days from our Rotterdam warehouse with duties included. Every parcel gets a tracking link within an hour of dispatch.</p></div></div>
        </details>
        <details class="ft-22__d" id="ft-22-returns" name="ft-22-faq">
          <summary class="ft-22__sum"><span>What if it doesn't fit or I change my mind?</span><span class="ft-22__plus" aria-hidden="true"></span></summary>
          <div class="ft-22__panel"><div class="ft-22__panelin"><p class="ft-22__a">You have 30 days from delivery, and a prepaid returns label is in the box. Refunds are issued to the original payment method within five working days of the parcel reaching us. Worn items are fine — we only ask that they are clean.</p></div></div>
        </details>
        <details class="ft-22__d" id="ft-22-sizing" name="ft-22-faq">
          <summary class="ft-22__sum"><span>How do I choose between two sizes?</span><span class="ft-22__plus" aria-hidden="true"></span></summary>
          <div class="ft-22__panel"><div class="ft-22__panelin"><p class="ft-22__a">Our sizes run true to European measurements. If you are between two, size down for the shell layers and up for the insulated ones — every product page lists the model's height and the size worn. The <a class="ft-22__inline" href="#ft-22-a">size guide</a> has the full measurement table.</p></div></div>
        </details>
        <details class="ft-22__d" id="ft-22-warranty" name="ft-22-faq">
          <summary class="ft-22__sum"><span>Is the warranty transferable if I sell the item?</span><span class="ft-22__plus" aria-hidden="true"></span></summary>
          <div class="ft-22__panel"><div class="ft-22__panelin"><p class="ft-22__a">Yes. The guarantee follows the product, not the buyer — the new owner registers it with the serial number on the care label. We also stock spare parts for fifteen years, so a repair is almost always cheaper than a replacement.</p></div></div>
        </details>
      </div>
      <a class="ft-22__all" href="#ft-22-a">All 46 answers in the help centre<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
    </section>
    <div class="ft-22__bar">
      <div class="ft-22__brand"><span class="ft-22__mark" aria-hidden="true"></span>Fellside</div>
      <nav class="ft-22__nav" aria-label="Footer"><a class="ft-22__link" href="#ft-22-a">Shop</a><a class="ft-22__link" href="#ft-22-a">Help centre</a><a class="ft-22__link" href="#ft-22-a">Returns</a><a class="ft-22__link" href="#ft-22-a">Privacy</a></nav>
      <p class="ft-22__copy">© <time datetime="2026">2026</time> Fellside Outdoor Ltd</p>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-22-bg);
  --ft-22-bg: oklch(0.97 0.01 200);
  --ft-22-foot: oklch(1 0 0);
  --ft-22-ink: oklch(0.21 0.03 220);
  --ft-22-mut: oklch(0.52 0.02 220);
  --ft-22-acc: oklch(0.5 0.14 215);
  --ft-22-line: oklch(0.21 0.03 220/.12);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-22-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-22 *,
.ft-22 *::before,
.ft-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-22__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(36px,7vh,80px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1060px)/2));
}

.ft-22__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-22-acc);
}

.ft-22__title {
  font-size: clamp(29px,5.2vw,56px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-22__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-22-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-22__foot {
  background: var(--ft-22-foot);
  border-top: 1px solid var(--ft-22-line);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1060px)/2));
}

.ft-22__faq {
  display: grid;
  gap: 16px;
  padding-block: clamp(28px,4vw,48px);
}

.ft-22__intro {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 8px 20px;
}

.ft-22__h {
  font-size: clamp(19px,2.3vw,25px);
  font-weight: 690;
  letter-spacing: -.025em;
}

.ft-22__isub {
  margin-inline-start: auto;
  font-size: 13.6px;
  color: var(--ft-22-mut);
}

.ft-22__inline {
  color: var(--ft-22-acc);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: .22em;
}

.ft-22__items {
  display: grid;
  border-top: 1px solid var(--ft-22-line);
}

.ft-22__d {
  border-bottom: 1px solid var(--ft-22-line);
}

.ft-22__d[open] {
  background: color-mix(in oklch,var(--ft-22-acc) 4%,transparent);
}

.ft-22__sum {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 60px;
  padding: 12px 14px;
  font-size: clamp(15px,1.7vw,17px);
  font-weight: 640;
  letter-spacing: -.015em;
  line-height: 1.35;
  cursor: pointer;
  list-style: none;
  text-wrap: balance;
  -webkit-tap-highlight-color: transparent;
  transition: color .2s ease;
}

.ft-22__sum::-webkit-details-marker {
  display: none;
}

.ft-22__sum:hover {
  color: var(--ft-22-acc);
}

.ft-22__sum:focus-visible {
  outline: 2px solid var(--ft-22-acc);
  outline-offset: -2px;
  border-radius: 8px;
}

.ft-22__plus {
  position: relative;
  width: 20px;
  height: 20px;
  flex: none;
  border-radius: 50%;
  border: 1.5px solid var(--ft-22-line);
  transition: background .25s ease,border-color .25s ease,rotate .3s cubic-bezier(.2,.8,.2,1);
}

.ft-22__plus::before,
.ft-22__plus::after {
  content: '';
  position: absolute;
  left: 50%;
  top: 50%;
  background: currentColor;
  border-radius: 2px;
}

.ft-22__plus::before {
  width: 9px;
  height: 1.6px;
  translate: -50% -50%;
}

.ft-22__plus::after {
  width: 1.6px;
  height: 9px;
  translate: -50% -50%;
  transition: opacity .25s ease;
}

.ft-22__d[open] .ft-22__plus {
  rotate: 180deg;
  border-color: var(--ft-22-acc);
  background: color-mix(in oklch,var(--ft-22-acc) 14%,transparent);
  color: var(--ft-22-acc);
}

.ft-22__d[open] .ft-22__plus::after {
  opacity: 0;
}

.ft-22__panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .38s cubic-bezier(.2,.8,.2,1);
}

.ft-22__d[open] .ft-22__panel {
  grid-template-rows: 1fr;
}

.ft-22__panelin {
  overflow: hidden;
  min-height: 0;
}

.ft-22__a {
  padding: 0 14px 18px;
  font-size: 14.8px;
  line-height: 1.65;
  color: var(--ft-22-mut);
  max-width: 68ch;
  text-wrap: pretty;
}

.ft-22__all {
  display: inline-flex;
  align-items: center;
  justify-self: start;
  gap: 8px;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 11px;
  border: 1px solid var(--ft-22-line);
  font-size: 14px;
  font-weight: 650;
  color: var(--ft-22-ink);
  text-decoration: none;
  transition: border-color .2s ease,color .2s ease,background .2s ease;
}

.ft-22__all:hover {
  color: var(--ft-22-acc);
  border-color: var(--ft-22-acc);
  background: color-mix(in oklch,var(--ft-22-acc) 8%,transparent);
}

.ft-22__all:hover svg {
  translate: 3px 0;
}

.ft-22__all svg {
  transition: translate .2s ease;
}

.ft-22__all:focus-visible,
.ft-22__inline:focus-visible,
.ft-22__link:focus-visible {
  outline: 2px solid var(--ft-22-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.ft-22__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px 24px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-22-line);
}

.ft-22__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ft-22__mark {
  width: 21px;
  height: 21px;
  border-radius: 7px;
  background: linear-gradient(140deg,var(--ft-22-acc),oklch(0.68 0.13 175));
}

.ft-22__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  margin-inline-start: auto;
}

.ft-22__link {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 11px;
  border-radius: 9px;
  font-size: 13.5px;
  color: var(--ft-22-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-22__link:hover {
  color: var(--ft-22-ink);
  background: oklch(0.21 0.03 220/.05);
}

.ft-22__copy {
  font-size: 12.8px;
  color: var(--ft-22-mut);
}

@media (max-width: 700px) {
  .ft-22__isub,
    .ft-22__nav {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-22 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-22');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const open = (hash) => {
    if (!hash) return;
    const el = root.querySelector(hash.startsWith('#') ? hash : '#' + hash);
    if (el && el.tagName === 'DETAILS') { el.open = true; el.querySelector('summary').focus({ preventScroll: true }); }
  };
  open(location.hash);
  window.addEventListener('hashchange', () => open(location.hash));
  root.querySelectorAll('.ft-22__d').forEach((d) => d.addEventListener('toggle', () => {
    if (d.open && history.replaceState) history.replaceState(null, '', '#' + d.id);
  }));
})();
```
