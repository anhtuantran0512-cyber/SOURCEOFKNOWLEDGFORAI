---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/notched-corner-badge-for-blog-cards/"
title: "Notched Corner Badge for Blog Cards"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "Most freshness badges are stickers laid on top of the artwork."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Notched Corner Badge for Blog Cards
Source: https://codefronts.com/snippets/css-ribbons/notched-corner-badge-for-blog-cards/

Most freshness badges are stickers laid on top of the artwork. This one is a hole. The thumbnail's corner is chamfered away with clip-path, and the label sits in the negative space as a separate tab with a real gap around it, so the badge reads as slotted through the card rather than printed on it. One registered @property length drives the notch and the tab together, which makes a clip-path chamfer animatable — hover a card and the corner opens. Underneath, freshness is a quantity, not a sticker: a hairline meter whose length and colour both interpolate from one number.
## HTML
```html
<section class="rib-05" aria-label="New and updated corner badge on blog thumbnails demo">
  <div class="rib-05__stage">
    <header class="rib-05__head">
      <p class="rib-05__eyebrow">The Frontend Digest</p>
      <h2 class="rib-05__title">Fresh this fortnight</h2>
      <p class="rib-05__sub">The corner is cut away, not covered up — and the rule under each headline shows how fresh the piece actually is.</p>
    </header>
    <div class="rib-05__grid">
      <article class="rib-05__card" data-flag="new">
        <a class="rib-05__thumb" href="#rib-05-a" tabindex="-1" aria-hidden="true">
          <img class="rib-05__img" alt="" loading="lazy" decoding="async" width="560" height="380"
            src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=700&auto=format&fit=crop">
        </a>
        <span class="rib-05__tab" aria-hidden="true">NEW</span>
        <div class="rib-05__body">
          <p class="rib-05__kicker">CSS</p>
          <h3 class="rib-05__name"><a class="rib-05__link" id="rib-05-a" href="#rib-05-a">Anchor positioning is finally usable</a></h3>
          <p class="rib-05__age">
            <span class="rib-05__meter" style="--rib-05-fresh:.92" aria-hidden="true"></span>
            <span class="rib-05__meta">Published <time datetime="2026-08-04">4 Aug 2026</time></span>
          </p>
        </div>
      </article>
      <article class="rib-05__card" data-flag="updated">
        <a class="rib-05__thumb" href="#rib-05-b" tabindex="-1" aria-hidden="true">
          <img class="rib-05__img" alt="" loading="lazy" decoding="async" width="560" height="380"
            src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?q=80&w=700&auto=format&fit=crop">
        </a>
        <span class="rib-05__tab" aria-hidden="true">UPDATED</span>
        <div class="rib-05__body">
          <p class="rib-05__kicker">Design systems</p>
          <h3 class="rib-05__name"><a class="rib-05__link" id="rib-05-b" href="#rib-05-b">Token naming that survives a rebrand</a></h3>
          <p class="rib-05__age">
            <span class="rib-05__meter" style="--rib-05-fresh:.78" aria-hidden="true"></span>
            <span class="rib-05__meta">Updated <time datetime="2026-08-07">7 Aug 2026</time></span>
          </p>
        </div>
      </article>
      <article class="rib-05__card">
        <a class="rib-05__thumb" href="#rib-05-c" tabindex="-1" aria-hidden="true">
          <img class="rib-05__img" alt="" loading="lazy" decoding="async" width="560" height="380"
            src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=700&auto=format&fit=crop">
        </a>
        <div class="rib-05__body">
          <p class="rib-05__kicker">Performance</p>
          <h3 class="rib-05__name"><a class="rib-05__link" id="rib-05-c" href="#rib-05-c">Budgeting INP before it budgets you</a></h3>
          <p class="rib-05__age">
            <span class="rib-05__meter" style="--rib-05-fresh:.12" aria-hidden="true"></span>
            <span class="rib-05__meta">Published <time datetime="2026-06-19">19 Jun 2026</time></span>
          </p>
        </div>
      </article>
    </div>
    <p class="rib-05__chip" aria-hidden="true">@property &lt;length&gt; · animated clip-path chamfer · tab in the negative space · color-mix freshness meter</p>
  </div>
</section>
```
## CSS
```css
.rib-05,
.rib-05 *,
.rib-05 *::before,
.rib-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --rib-05-cut {
  syntax: '<length>';
  inherits: true;
  initial-value: 0px;
}

.rib-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-05-paper: #efe9dd;
  --rib-05-paper: oklch(0.93 0.015 85);
  --rib-05-card: #fbf8f3;
  --rib-05-card: oklch(0.985 0.006 90);
  --rib-05-ink: #1b1917;
  --rib-05-ink: oklch(0.22 0.008 75);
  --rib-05-mut: #7a736a;
  --rib-05-mut: oklch(0.57 0.014 78);
  --rib-05-rule: rgba(27,25,23,.14);
  --rib-05-rule: oklch(0.22 0.008 75/.14);
  --rib-05-new: #0d7a4a;
  --rib-05-new: oklch(0.53 0.13 158);
  --rib-05-upd: #9a4a15;
  --rib-05-upd: oklch(0.53 0.14 55);
  --rib-05-tab: 26px;
  --rib-05-gap: 5px;
  background: var(--rib-05-paper);
  color: var(--rib-05-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3.4vw,34px);
  padding: clamp(20px,5vw,58px);
}

.rib-05__head {
  display: grid;
  gap: 10px;
  justify-items: center;
  text-align: center;
  max-width: 34ch;
}

.rib-05__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--rib-05-mut);
}

.rib-05__title {
  font-family: 'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif;
  font-size: clamp(28px,5vw,44px);
  font-weight: 500;
  letter-spacing: -.02em;
  line-height: 1.06;
}

.rib-05__sub {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--rib-05-mut);
  text-wrap: pretty;
}

.rib-05__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
  gap: clamp(16px,2.6vw,26px);
  width: min(100%,1020px);
}

.rib-05__card {
  container-type: inline-size;
  container-name: rib-05-card;
  position: relative;
  display: grid;
  gap: 0;
  overflow: hidden;
  background: var(--rib-05-card);
  border: 1px solid var(--rib-05-rule);
  border-radius: 4px;
  padding: 10px 10px 0;
  transition: --rib-05-cut .5s cubic-bezier(.16,1,.3,1),border-color .4s,translate .5s cubic-bezier(.16,1,.3,1);
}

.rib-05__card[data-flag] {
  --rib-05-cut: 92px;
}

.rib-05__card[data-flag]:hover,
.rib-05__card[data-flag]:focus-within {
  --rib-05-cut: 116px;
  border-color: color-mix(in oklch,var(--rib-05-acc) 40%,var(--rib-05-rule));
}

.rib-05__card[data-flag="new"] {
  --rib-05-acc: var(--rib-05-new);
}

.rib-05__card[data-flag="updated"] {
  --rib-05-acc: var(--rib-05-upd);
}

.rib-05__thumb {
  transition: --rib-05-cut .5s cubic-bezier(.16,1,.3,1);
  position: relative;
  display: block;
  aspect-ratio: 16/10;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.88 0.02 250),oklch(0.83 0.03 200));
  clip-path: polygon(0 0,calc(100% - var(--rib-05-cut)) 0,100% var(--rib-05-cut),100% 100%,0 100%);
}

.rib-05__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: scale .7s cubic-bezier(.16,1,.3,1);
}

.rib-05__card:hover .rib-05__img {
  scale: 1.04;
}

.rib-05__tab {
  transition: --rib-05-cut .5s cubic-bezier(.16,1,.3,1);
  --rib-05-reach: calc(var(--rib-05-cut) - (var(--rib-05-gap) + var(--rib-05-tab) / 2) * 1.415);
  --rib-05-len: calc(var(--rib-05-reach) * 1.415 + var(--rib-05-tab) * 2);
  position: absolute;
  z-index: 2;
  inset-block-start: calc(var(--rib-05-reach) / 2 - var(--rib-05-tab) / 2 + 10px);
  inset-inline-end: calc((var(--rib-05-len) - var(--rib-05-reach)) / -2 + 10px);
  inline-size: var(--rib-05-len);
  min-block-size: var(--rib-05-tab);
  display: grid;
  place-items: center;
  rotate: 45deg;
  pointer-events: none;
  background: var(--rib-05-acc);
  color: oklch(0.99 0.01 90);
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: .14em;
  line-height: 1;
  box-shadow: inset 0 1px 0 oklch(1 0 0/.28),inset 0 -1px 0 oklch(0 0 0/.2);
}

.rib-05__body {
  display: grid;
  gap: 9px;
  padding: 15px 6px 16px;
}

.rib-05__kicker {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--rib-05-acc,var(--rib-05-mut));
}

.rib-05__name {
  font-family: 'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif;
  font-size: 19px;
  font-weight: 500;
  line-height: 1.28;
  letter-spacing: -.012em;
  text-wrap: balance;
}

.rib-05__link {
  color: inherit;
  text-decoration: none;
  background-image: linear-gradient(currentColor,currentColor);
  background-size: 0% 1px;
  background-repeat: no-repeat;
  background-position: 0 100%;
  transition: background-size .35s cubic-bezier(.16,1,.3,1);
}

.rib-05__link:hover {
  background-size: 100% 1px;
}

.rib-05__link:focus-visible {
  outline: 3px solid var(--rib-05-acc,var(--rib-05-ink));
  outline-offset: 3px;
  border-radius: 2px;
}

.rib-05__age {
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  gap: 10px;
  margin-top: 2px;
  padding-top: 9px;
  border-top: 1px solid var(--rib-05-rule);
}

.rib-05__meter {
  block-size: 3px;
  border-radius: 99px;
  background: oklch(0.22 0.008 75/.09);
  overflow: hidden;
}

.rib-05__meter::after {
  content: '';
  display: block;
  block-size: 100%;
  inline-size: calc(var(--rib-05-fresh,0) * 100%);
  background: color-mix(in oklch,var(--rib-05-acc,var(--rib-05-mut)) calc(var(--rib-05-fresh,0) * 100%),var(--rib-05-mut));
}

.rib-05__meta {
  font-size: 11.5px;
  color: var(--rib-05-mut);
  font-variant-numeric: tabular-nums;
  letter-spacing: .01em;
  white-space: nowrap;
}

@container rib-05-card (inline-size > 330px) {
  .rib-05__card[data-flag] .rib-05__thumb,
    .rib-05__card[data-flag] .rib-05__tab {
    --rib-05-cut: 118px;
  }

  .rib-05__card[data-flag]:hover .rib-05__thumb,
    .rib-05__card[data-flag]:hover .rib-05__tab,
    .rib-05__card[data-flag]:focus-within .rib-05__thumb,
    .rib-05__card[data-flag]:focus-within .rib-05__tab {
    --rib-05-cut: 146px;
  }

  .rib-05__tab {
    --rib-05-tab: 30px;
    font-size: 11px;
  }

  .rib-05__name {
    font-size: 21px;
  }
}

.rib-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-05-mut);
  padding: 8px 15px;
  border: 1px solid var(--rib-05-rule);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-05 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
