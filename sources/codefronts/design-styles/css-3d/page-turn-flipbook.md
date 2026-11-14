---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/page-turn-flipbook/"
title: "Page Turn Flipbook with Hinged Rotation"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "A four-spread journal that turns on a spine hinge: transform-origin at the gutter turns rotateY into a page turn, each leaf carries a front and a back, and…"
has_js: "true"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Page Turn Flipbook with Hinged Rotation
Source: https://codefronts.com/design-styles/css-3d/page-turn-flipbook/

A four-spread journal that turns on a spine hinge: transform-origin at the gutter turns rotateY into a page turn, each leaf carries a front and a back, and the script's real job is the stacking order &mdash; z-index recomputed on every turn so turned leaves fall behind the ones still to come. Prev and next buttons, click-a-half, and arrow keys all drive the same single index.
## HTML
```html
<section class="d3-15" aria-label="Page-turn flipbook demo">

  <div class="d3-15__theme">
    <input class="d3-15__theme-input" type="checkbox" id="d3-15-theme">
    <label class="d3-15__theme-label" for="d3-15-theme" aria-label="Toggle light and dark theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg>
    </label>
  </div>

  <div class="card">
    <div class="book-scene">
      <div class="book" data-d3-15-book>
        <div class="book-shadow" aria-hidden="true"></div>

        <div class="left-cover" data-d3-15-cover>
          <div class="cover-art">
            <div class="cover-eyebrow">FORMA STUDIO</div>
            <div class="cover-rule"></div>
            <div class="cover-title">FORMA<span class="cover-vol">Vol. VI</span></div>
            <div class="cover-rule"></div>
            <div class="cover-sub">Design · Architecture · Thought</div>
          </div>
        </div>

        <div class="page" data-page="0">
          <div class="page-front paper-warm">
            <div class="pg pg-warm">
              <div class="spread-label">Chapter One</div>
              <div class="spread-title sm">The Weight<br />of Silence</div>
              <div class="spread-rule"></div>
              <p class="spread-body">There is a moment before speech when the world holds its breath. Architecture inhabits this pause — not the buildings themselves, but the spaces they carve from air.</p>
              <p class="spread-body mt">The corridor narrows, draws the eye forward. Light slants from an unseen source. To walk through is to be composed by the building.</p>
              <span class="pg-num right">1</span>
              <span class="spread-big-num">I</span>
            </div>
          </div>
          <div class="page-back paper-cool">
            <div class="pg pg-cool">
              <div class="spread-label">Essay II</div>
              <div class="spread-title xs">Form<br />Without<br />Apology</div>
              <div class="spread-rule alt"></div>
              <p class="spread-body alt">To design is to make a claim about the world as it should be — not as it is. The blueprint precedes the building, and in that gap lives everything called imagination.</p>
              <span class="pg-num left">2</span>
            </div>
          </div>
        </div>

        <div class="page" data-page="1">
          <div class="page-front paper-sage">
            <div class="pg pg-sage">
              <div class="spread-label">Visual Field</div>
              <div class="spread-img sage-img">
                <div class="circle-outer">
                  <div class="circle-inner"></div>
                </div>
              </div>
              <div class="spread-pullquote sage">"Growth is not linear. It is fractal — repeating at every scale."</div>
              <p class="spread-body sage-body">The forest does not plan its canopy. Each tree simply grows toward light.</p>
              <span class="pg-num right sage">3</span>
            </div>
          </div>
          <div class="page-back paper-rose">
            <div class="pg pg-rose">
              <div class="spread-label">Interlude</div>
              <div class="spread-title sm rose">Red<br />Notation</div>
              <div class="spread-rule rose"></div>
              <p class="spread-body rose-body">Color arrives before language. Red is felt in the chest before named by the tongue. The ancient painters knew this — their ochre hands pressed flat on cave walls were not decoration. They were declaration.</p>
              <span class="pg-num left rose">4</span>
            </div>
          </div>
        </div>

        <div class="page" data-page="2">
          <div class="page-front paper-warm">
            <div class="pg pg-warm">
              <div class="spread-label">Final Study</div>
              <div class="spread-title sm">Endings<br />as Form</div>
              <div class="spread-rule"></div>
              <p class="spread-body">Every designed thing must eventually end — the page turn, the last note, the exit from the building. The best designs make their endings feel inevitable, not arbitrary.</p>
              <div class="spread-pullquote warm">"The final line is the first thing written."</div>
              <span class="pg-num right">5</span>
            </div>
          </div>
          <div class="page-back paper-ink">
            <div class="pg pg-ink">
              <div class="colophon-label">COLOPHON</div>
              <div class="colophon-title">FORMA</div>
              <div class="colophon-sub">A Journal of Design Thought</div>
              <p class="colophon-body">Issue VI · Printed on FSC-certified stock · Typography set in Playfair Display and EB Garamond · All rights reserved ©</p>
              <span class="pg-num left ink">6</span>
            </div>
          </div>
        </div>

      </div>

      <div class="nav">
        <button class="nav-btn" type="button" data-d3-15-prev disabled>← Prev</button>
        <span class="page-counter" data-d3-15-counter>Spread 1 of 4</span>
        <button class="nav-btn" type="button" data-d3-15-next>Next →</button>
      </div>

    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=EB+Garamond:ital,wght@0,400;0,500;1,400;1,500&display=swap');

.d3-15 {
  --d3-15-desk: #1c1410;
  --d3-15-desk-wash: rgba(180,120,40,0.06);
  --d3-15-spine-deep: rgba(0,0,0,0.40);
  --d3-15-spine-soft: rgba(0,0,0,0.10);
  --d3-15-page-shade: rgba(0,0,0,0.14);
  --d3-15-cover-shade: rgba(0,0,0,0.20);
  --d3-15-book-shadow: rgba(0,0,0,0.50);
  --d3-15-paper-warm: #f5ece0;
  --d3-15-paper-cool: #ede8f0;
  --d3-15-paper-rose: #f5e8e8;
  --d3-15-paper-sage: #e8f0e8;
  --d3-15-paper-ink: #1a1510;
  --d3-15-ink-warm: #2a1f14;
  --d3-15-ink-cool: #2a2432;
  --d3-15-ink-rose: #2a1418;
  --d3-15-ink-sage: #1a2a1e;
  --d3-15-ink-page: #e8d8c0;
  --d3-15-folio-warm: #8a6a4a;
  --d3-15-folio-cool: #7a6898;
  --d3-15-folio-rose: #8a4050;
  --d3-15-folio-sage: #4a7a50;
  --d3-15-folio-ink: rgba(200,180,140,0.40);
  --d3-15-rule-cool: #4a3868;
  --d3-15-rule-rose: #8a3040;
  --d3-15-quote-warm-line: #8a6a4a;
  --d3-15-quote-warm-ink: #4a3424;
  --d3-15-quote-sage-line: #3a6a40;
  --d3-15-quote-sage-ink: #2a4a2e;
  --d3-15-title-rose: #5a1828;
  --d3-15-body-cool: #3a2a50;
  --d3-15-body-rose: #3a1820;
  --d3-15-body-sage: #2a3a26;
  --d3-15-sage-img-1: #2a4a2e;
  --d3-15-sage-img-2: #1a3020;
  --d3-15-circle-line: rgba(120,200,120,0.40);
  --d3-15-circle-fill: rgba(120,200,120,0.20);
  --d3-15-cover-1: #1a0f08;
  --d3-15-cover-2: #0e0a06;
  --d3-15-cover-wash: rgba(180,120,40,0.12);
  --d3-15-gold-dim: rgba(200,160,80,0.55);
  --d3-15-gold-rule: rgba(200,160,80,0.35);
  --d3-15-cover-ink: #f0e4cc;
  --d3-15-nav-ink: rgba(228,203,163,0.96);
  --d3-15-nav-ink-hot: rgba(220,190,140,1);
  --d3-15-nav-hover: rgba(200,170,120,0.08);
  --d3-15-counter: rgba(214,186,142,0.9);
  --d3-15-ui-face: rgba(255,255,255,0.05);
  --d3-15-ui-line: rgba(200,170,120,0.28);
  --d3-15-ui-ink: rgba(220,190,140,0.92);
  width: 100%;
  min-height: max(100vh, 600px);
  display: block;
  position: relative;
  background: var(--d3-15-desk);
  font-family: 'EB Garamond', Georgia, serif;
  overflow: hidden;
  perspective: 2400px;
  box-sizing: border-box;
}

.d3-15 *,
.d3-15 *::before,
.d3-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.d3-15:has(.d3-15__theme-input:checked) {
  --d3-15-desk: #ded0bb;
  --d3-15-desk-wash: rgba(120,80,20,0.10);
  --d3-15-spine-deep: rgba(58,38,16,0.34);
  --d3-15-spine-soft: rgba(58,38,16,0.08);
  --d3-15-page-shade: rgba(78,54,24,0.13);
  --d3-15-cover-shade: rgba(70,46,20,0.18);
  --d3-15-book-shadow: rgba(72,50,22,0.30);
  --d3-15-paper-warm: #fdf7ec;
  --d3-15-paper-cool: #f4f0fa;
  --d3-15-paper-rose: #fdefef;
  --d3-15-paper-sage: #eef8ef;
  --d3-15-paper-ink: #241b13;
  --d3-15-ink-warm: #241a10;
  --d3-15-ink-cool: #241d2e;
  --d3-15-ink-rose: #2a1014;
  --d3-15-ink-sage: #14261a;
  --d3-15-ink-page: #f2e5ce;
  --d3-15-folio-warm: #6d4f2f;
  --d3-15-folio-cool: #5d4a80;
  --d3-15-folio-rose: #77303f;
  --d3-15-folio-sage: #35603f;
  --d3-15-folio-ink: rgba(216,198,160,0.55);
  --d3-15-rule-cool: #3d2b5c;
  --d3-15-rule-rose: #77242f;
  --d3-15-quote-warm-line: #7a5836;
  --d3-15-quote-warm-ink: #3b2a17;
  --d3-15-quote-sage-line: #2b5733;
  --d3-15-quote-sage-ink: #1e3d22;
  --d3-15-title-rose: #58101f;
  --d3-15-body-cool: #2f2044;
  --d3-15-body-rose: #34121a;
  --d3-15-body-sage: #22321d;
  --d3-15-sage-img-1: #23482a;
  --d3-15-sage-img-2: #12301b;
  --d3-15-circle-line: rgba(184,255,196,0.45);
  --d3-15-circle-fill: rgba(184,255,196,0.22);
  --d3-15-cover-1: #241408;
  --d3-15-cover-2: #150c05;
  --d3-15-cover-wash: rgba(220,160,60,0.16);
  --d3-15-gold-dim: rgba(228,188,106,0.72);
  --d3-15-gold-rule: rgba(228,188,106,0.45);
  --d3-15-cover-ink: #f8eed8;
  --d3-15-nav-ink: rgba(228,203,163,0.96);
  --d3-15-nav-ink-hot: #2a1e08;
  --d3-15-nav-hover: rgba(90,62,20,0.10);
  --d3-15-counter: rgba(214,186,142,0.9);
  --d3-15-ui-face: rgba(255,255,255,0.60);
  --d3-15-ui-line: rgba(70,48,22,0.22);
  --d3-15-ui-ink: #3a2a12;
}

@media (prefers-color-scheme: light) {
  .d3-15:has(.d3-15__theme-input:checked) {
    --d3-15-desk: #ded0bb;
    --d3-15-desk-wash: rgba(120,80,20,0.10);
    --d3-15-spine-deep: rgba(58,38,16,0.34);
    --d3-15-spine-soft: rgba(58,38,16,0.08);
    --d3-15-page-shade: rgba(78,54,24,0.13);
    --d3-15-cover-shade: rgba(70,46,20,0.18);
    --d3-15-book-shadow: rgba(72,50,22,0.30);
    --d3-15-paper-warm: #fdf7ec;
    --d3-15-paper-cool: #f4f0fa;
    --d3-15-paper-rose: #fdefef;
    --d3-15-paper-sage: #eef8ef;
    --d3-15-paper-ink: #241b13;
    --d3-15-ink-warm: #241a10;
    --d3-15-ink-cool: #241d2e;
    --d3-15-ink-rose: #2a1014;
    --d3-15-ink-sage: #14261a;
    --d3-15-ink-page: #f2e5ce;
    --d3-15-folio-warm: #6d4f2f;
    --d3-15-folio-cool: #5d4a80;
    --d3-15-folio-rose: #77303f;
    --d3-15-folio-sage: #35603f;
    --d3-15-folio-ink: rgba(216,198,160,0.55);
    --d3-15-rule-cool: #3d2b5c;
    --d3-15-rule-rose: #77242f;
    --d3-15-quote-warm-line: #7a5836;
    --d3-15-quote-warm-ink: #3b2a17;
    --d3-15-quote-sage-line: #2b5733;
    --d3-15-quote-sage-ink: #1e3d22;
    --d3-15-title-rose: #58101f;
    --d3-15-body-cool: #2f2044;
    --d3-15-body-rose: #34121a;
    --d3-15-body-sage: #22321d;
    --d3-15-sage-img-1: #23482a;
    --d3-15-sage-img-2: #12301b;
    --d3-15-circle-line: rgba(184,255,196,0.45);
    --d3-15-circle-fill: rgba(184,255,196,0.22);
    --d3-15-cover-1: #241408;
    --d3-15-cover-2: #150c05;
    --d3-15-cover-wash: rgba(220,160,60,0.16);
    --d3-15-gold-dim: rgba(228,188,106,0.72);
    --d3-15-gold-rule: rgba(228,188,106,0.45);
    --d3-15-cover-ink: #f8eed8;
    --d3-15-nav-ink: rgba(228,203,163,0.96);
    --d3-15-nav-ink-hot: #2a1e08;
    --d3-15-nav-hover: rgba(90,62,20,0.10);
    --d3-15-counter: rgba(214,186,142,0.9);
    --d3-15-ui-face: rgba(255,255,255,0.60);
    --d3-15-ui-line: rgba(70,48,22,0.22);
    --d3-15-ui-ink: #3a2a12;
  }
}

@media (prefers-color-scheme: dark) {
  .d3-15:has(.d3-15__theme-input:checked) {
    --d3-15-desk: #ded0bb;
    --d3-15-desk-wash: rgba(120,80,20,0.10);
    --d3-15-spine-deep: rgba(58,38,16,0.34);
    --d3-15-spine-soft: rgba(58,38,16,0.08);
    --d3-15-page-shade: rgba(78,54,24,0.13);
    --d3-15-cover-shade: rgba(70,46,20,0.18);
    --d3-15-book-shadow: rgba(72,50,22,0.30);
    --d3-15-paper-warm: #fdf7ec;
    --d3-15-paper-cool: #f4f0fa;
    --d3-15-paper-rose: #fdefef;
    --d3-15-paper-sage: #eef8ef;
    --d3-15-paper-ink: #241b13;
    --d3-15-ink-warm: #241a10;
    --d3-15-ink-cool: #241d2e;
    --d3-15-ink-rose: #2a1014;
    --d3-15-ink-sage: #14261a;
    --d3-15-ink-page: #f2e5ce;
    --d3-15-folio-warm: #6d4f2f;
    --d3-15-folio-cool: #5d4a80;
    --d3-15-folio-rose: #77303f;
    --d3-15-folio-sage: #35603f;
    --d3-15-folio-ink: rgba(216,198,160,0.55);
    --d3-15-rule-cool: #3d2b5c;
    --d3-15-rule-rose: #77242f;
    --d3-15-quote-warm-line: #7a5836;
    --d3-15-quote-warm-ink: #3b2a17;
    --d3-15-quote-sage-line: #2b5733;
    --d3-15-quote-sage-ink: #1e3d22;
    --d3-15-title-rose: #58101f;
    --d3-15-body-cool: #2f2044;
    --d3-15-body-rose: #34121a;
    --d3-15-body-sage: #22321d;
    --d3-15-sage-img-1: #23482a;
    --d3-15-sage-img-2: #12301b;
    --d3-15-circle-line: rgba(184,255,196,0.45);
    --d3-15-circle-fill: rgba(184,255,196,0.22);
    --d3-15-cover-1: #241408;
    --d3-15-cover-2: #150c05;
    --d3-15-cover-wash: rgba(220,160,60,0.16);
    --d3-15-gold-dim: rgba(228,188,106,0.72);
    --d3-15-gold-rule: rgba(228,188,106,0.45);
    --d3-15-cover-ink: #f8eed8;
    --d3-15-nav-ink: rgba(228,203,163,0.96);
    --d3-15-nav-ink-hot: #2a1e08;
    --d3-15-nav-hover: rgba(90,62,20,0.10);
    --d3-15-counter: rgba(214,186,142,0.9);
    --d3-15-ui-face: rgba(255,255,255,0.60);
    --d3-15-ui-line: rgba(70,48,22,0.22);
    --d3-15-ui-ink: #3a2a12;
  }
}

.d3-15 .d3-15__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 30;
}

.d3-15 .d3-15__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 1;
}

.d3-15 .d3-15__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-15-ui-line);
  border-radius: 12px;
  background: var(--d3-15-ui-face);
  color: var(--d3-15-ui-ink);
  pointer-events: none;
}

.d3-15 .d3-15__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-15 .d3-15__theme-input:focus-visible + .d3-15__theme-label {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.d3-15 .card {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 28px 16px;
}

.d3-15 .card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 60% 50% at 50% 40%, var(--d3-15-desk-wash) 0%, transparent 70%);
  pointer-events: none;
}

.d3-15 .book-scene {
  transform-style: preserve-3d;
  transform: rotateX(5deg) rotateY(-4deg);
  transition: transform 0.6s ease;
  position: relative;
  z-index: 1;
}

.d3-15 .book-scene:hover {
  transform: rotateX(4deg) rotateY(-2deg);
}

.d3-15 .book {
  width: 560px;
  height: 360px;
  position: relative;
  transform-style: preserve-3d;
}

.d3-15 .book::before {
  content: '';
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 12px;
  transform: translateX(-50%) translateZ(1px);
  background: linear-gradient(to right, var(--d3-15-spine-deep) 0%, var(--d3-15-spine-soft) 30%, var(--d3-15-spine-soft) 70%, var(--d3-15-spine-deep) 100%);
  z-index: 20;
  pointer-events: none;
}

.d3-15 .page {
  position: absolute;
  width: 280px;
  height: 360px;
  top: 0;
  left: 280px;
  transform-origin: left center;
  transform-style: preserve-3d;
  transition: transform 1.1s cubic-bezier(0.645, 0.045, 0.355, 1);
}

.d3-15 .page.flipped {
  transform: rotateY(-180deg);
}

.d3-15 .page-front,
.d3-15 .page-back {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  overflow: hidden;
}

.d3-15 .page-back {
  transform: rotateY(180deg);
}

.d3-15 .left-cover {
  position: absolute;
  left: 0;
  top: 0;
  width: 280px;
  height: 360px;
  z-index: 0;
  border-radius: 4px 0 0 4px;
  overflow: hidden;
}

.d3-15 .pg {
  width: 100%;
  height: 100%;
  padding: 30px 26px;
  display: flex;
  flex-direction: column;
  position: relative;
}

.d3-15 .pg-warm {
  color: var(--d3-15-ink-warm);
}

.d3-15 .pg-cool {
  color: var(--d3-15-ink-cool);
}

.d3-15 .pg-rose {
  color: var(--d3-15-ink-rose);
}

.d3-15 .pg-sage {
  color: var(--d3-15-ink-sage);
}

.d3-15 .pg-ink {
  color: var(--d3-15-ink-page);
}

.d3-15 .pg-num {
  font-family: 'EB Garamond', serif;
  font-size: 10px;
  letter-spacing: 2px;
  position: absolute;
  bottom: 16px;
}

.d3-15 .pg-num.right {
  right: 22px;
  color: var(--d3-15-folio-warm);
}

.d3-15 .pg-num.left {
  left: 22px;
  color: var(--d3-15-folio-cool);
}

.d3-15 .pg-num.rose {
  color: var(--d3-15-folio-rose);
}

.d3-15 .pg-num.sage {
  color: var(--d3-15-folio-sage);
}

.d3-15 .pg-num.ink {
  color: var(--d3-15-folio-ink);
}

.d3-15 .page-front::after,
.d3-15 .page-back::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 40px;
  pointer-events: none;
}

.d3-15 .page-front::after {
  right: 0;
  background: linear-gradient(to right, transparent, var(--d3-15-page-shade));
}

.d3-15 .page-back::after {
  left: 0;
  background: linear-gradient(to left, transparent, var(--d3-15-page-shade));
}

.d3-15 .left-cover::after {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 30px;
  background: linear-gradient(to right, transparent, var(--d3-15-cover-shade));
}

.d3-15 .paper-warm {
  background: var(--d3-15-paper-warm);
}

.d3-15 .paper-cool {
  background: var(--d3-15-paper-cool);
}

.d3-15 .paper-rose {
  background: var(--d3-15-paper-rose);
}

.d3-15 .paper-sage {
  background: var(--d3-15-paper-sage);
}

.d3-15 .paper-ink {
  background: var(--d3-15-paper-ink);
}

.d3-15 .spread-label {
  font-family: 'EB Garamond', serif;
  font-size: 9px;
  letter-spacing: 4px;
  text-transform: uppercase;
  opacity: 0.72;
  margin-bottom: 16px;
}

.d3-15 .spread-title {
  font-family: 'Playfair Display', serif;
  font-weight: 900;
  line-height: 1.1;
  margin-bottom: 14px;
}

.d3-15 .spread-title.sm {
  font-size: 26px;
}

.d3-15 .spread-title.xs {
  font-size: 22px;
}

.d3-15 .spread-title.rose {
  color: var(--d3-15-title-rose);
}

.d3-15 .spread-body {
  font-family: 'EB Garamond', serif;
  font-size: 13px;
  line-height: 1.78;
  opacity: 0.78;
}

.d3-15 .spread-body.mt {
  margin-top: 10px;
}

.d3-15 .spread-body.alt {
  color: var(--d3-15-body-cool);
}

.d3-15 .spread-body.rose-body {
  color: var(--d3-15-body-rose);
}

.d3-15 .spread-body.sage-body {
  color: var(--d3-15-body-sage);
}

.d3-15 .spread-pullquote {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 16px;
  line-height: 1.5;
  border-left: 2px solid currentColor;
  padding-left: 14px;
  margin: 16px 0;
  opacity: 0.85;
}

.d3-15 .spread-pullquote.warm {
  border-color: var(--d3-15-quote-warm-line);
  color: var(--d3-15-quote-warm-ink);
}

.d3-15 .spread-pullquote.sage {
  border-color: var(--d3-15-quote-sage-line);
  color: var(--d3-15-quote-sage-ink);
}

.d3-15 .spread-rule {
  width: 40px;
  height: 1px;
  background: currentColor;
  opacity: 0.3;
  margin: 14px 0;
}

.d3-15 .spread-rule.alt {
  background: var(--d3-15-rule-cool);
}

.d3-15 .spread-rule.rose {
  background: var(--d3-15-rule-rose);
}

.d3-15 .spread-img {
  width: 100%;
  height: 100px;
  border-radius: 4px;
  margin: 14px 0;
  overflow: hidden;
  flex-shrink: 0;
}

.d3-15 .sage-img {
  height: 72px;
  background: linear-gradient(135deg, var(--d3-15-sage-img-1), var(--d3-15-sage-img-2));
  display: flex;
  align-items: center;
  justify-content: center;
}

.d3-15 .circle-outer {
  width: 52px;
  height: 52px;
  border: 2px solid var(--d3-15-circle-line);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.d3-15 .circle-inner {
  width: 32px;
  height: 32px;
  background: var(--d3-15-circle-fill);
  border-radius: 50%;
}

.d3-15 .spread-big-num {
  font-family: 'Playfair Display', serif;
  font-size: 80px;
  font-weight: 900;
  line-height: 0.9;
  opacity: 0.07;
  position: absolute;
  right: 16px;
  bottom: 30px;
}

.d3-15 .cover-art {
  width: 100%;
  height: 100%;
  background: linear-gradient(148deg, var(--d3-15-cover-1), var(--d3-15-cover-2));
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 26px;
  border-radius: 4px 0 0 4px;
  position: relative;
  overflow: hidden;
}

.d3-15 .cover-art::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 70% 60% at 50% 40%, var(--d3-15-cover-wash) 0%, transparent 70%);
}

.d3-15 .cover-eyebrow {
  font-family: 'EB Garamond', serif;
  font-size: 9px;
  letter-spacing: 5px;
  color: var(--d3-15-gold-dim);
  margin-bottom: 26px;
  z-index: 1;
}

.d3-15 .cover-rule {
  width: 56px;
  height: 1px;
  background: var(--d3-15-gold-rule);
  margin: 0 0 26px;
  z-index: 1;
}

.d3-15 .cover-title {
  font-family: 'Playfair Display', serif;
  font-size: 34px;
  font-weight: 900;
  color: var(--d3-15-cover-ink);
  text-align: center;
  line-height: 1.1;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.d3-15 .cover-vol {
  font-style: italic;
  font-weight: 400;
  font-size: 20px;
  opacity: 0.7;
  margin-top: 6px;
}

.d3-15 .cover-rule:nth-of-type(2),
.d3-15 .cover-title + .cover-rule {
  margin: 26px 0;
}

.d3-15 .cover-sub {
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: 11px;
  color: var(--d3-15-gold-dim);
  letter-spacing: 1px;
  z-index: 1;
}

.d3-15 .colophon-label {
  font-family: 'EB Garamond', serif;
  font-size: 9px;
  letter-spacing: 4px;
  opacity: 0.45;
  margin-bottom: 18px;
}

.d3-15 .colophon-title {
  font-family: 'Playfair Display', serif;
  font-size: 18px;
  font-weight: 700;
  opacity: 0.9;
  margin-bottom: 8px;
}

.d3-15 .colophon-sub {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 12px;
  opacity: 0.6;
  margin-bottom: 22px;
}

.d3-15 .colophon-body {
  font-family: 'EB Garamond', serif;
  font-size: 11px;
  line-height: 1.8;
  opacity: 0.58;
}

.d3-15 .nav {
  display: flex;
  align-items: center;
  gap: 18px;
  margin-top: 26px;
  position: relative;
  z-index: 100;
}

.d3-15 .nav-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'EB Garamond', serif;
  font-size: 12px;
  letter-spacing: 2px;
  color: var(--d3-15-nav-ink);
  background: none;
  border: none;
  cursor: pointer;
  padding: 9px 18px;
  border-radius: 4px;
  transition: color 0.2s, background 0.2s;
}

.d3-15 .nav-btn:hover {
  color: var(--d3-15-nav-ink-hot);
  background: var(--d3-15-nav-hover);
}

.d3-15 .nav-btn:disabled {
  opacity: 0.35;
  cursor: default;
}

.d3-15 .page-counter {
  font-family: 'EB Garamond', serif;
  font-size: 12px;
  color: var(--d3-15-counter);
  letter-spacing: 2px;
  min-width: 80px;
  text-align: center;
}

.d3-15 .book-shadow {
  position: absolute;
  bottom: -18px;
  left: 10%;
  right: 10%;
  height: 28px;
  background: radial-gradient(ellipse at center, var(--d3-15-book-shadow) 0%, transparent 70%);
  filter: blur(12px);
  z-index: -1;
}

@media (max-width: 720px) {
  .d3-15 .book {
    width: 360px;
    height: 280px;
  }

  .d3-15 .page,
    .d3-15 .left-cover {
    width: 180px;
    height: 280px;
  }

  .d3-15 .page {
    left: 180px;
  }

  .d3-15 .pg {
    padding: 22px 18px;
  }

  .d3-15 .spread-title.sm {
    font-size: 20px;
  }

  .d3-15 .spread-title.xs {
    font-size: 18px;
  }

  .d3-15 .cover-title {
    font-size: 26px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .d3-15 .book-scene,
    .d3-15 .page {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.d3-15');
  if (!root) return;
  const book = root.querySelector('[data-d3-15-book]');
  const prevBtn = root.querySelector('[data-d3-15-prev]');
  const nextBtn = root.querySelector('[data-d3-15-next]');
  const counter = root.querySelector('[data-d3-15-counter]');
  if (!book || !prevBtn || !nextBtn || !counter) return;

  const pages = Array.from(root.querySelectorAll('.page[data-page]'));
  const TOTAL_SPREADS = pages.length + 1;
  let currentSpread = 0;

  function update() {
    pages.forEach((page, i) => {
      page.classList.toggle('flipped', i < currentSpread);
      page.style.zIndex = i < currentSpread ? i + 1 : pages.length - i + 4;
    });
    counter.textContent = 'Spread ' + (currentSpread + 1) + ' of ' + TOTAL_SPREADS;
    prevBtn.disabled = currentSpread === 0;
    nextBtn.disabled = currentSpread === TOTAL_SPREADS - 1;
  }

  prevBtn.addEventListener('click', () => { if (currentSpread > 0) { currentSpread--; update(); } });
  nextBtn.addEventListener('click', () => { if (currentSpread < TOTAL_SPREADS - 1) { currentSpread++; update(); } });

  book.addEventListener('click', e => {
    if (e.target.closest('.nav-btn')) return;
    const rect = book.getBoundingClientRect();
    if (e.clientX > rect.left + rect.width / 2) {
      if (currentSpread < TOTAL_SPREADS - 1) { currentSpread++; update(); }
    } else {
      if (currentSpread > 0) { currentSpread--; update(); }
    }
  });

  let pointerInside = false;
  root.addEventListener('mouseenter', () => { pointerInside = true; });
  root.addEventListener('mouseleave', () => { pointerInside = false; });
  document.addEventListener('keydown', e => {
    if (!pointerInside) return;
    if (e.key === 'ArrowRight') { nextBtn.click(); e.preventDefault(); }
    if (e.key === 'ArrowLeft')  { prevBtn.click(); e.preventDefault(); }
  });

  update();
})();
```
