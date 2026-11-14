---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/retro-clothing-store-web-ui-design/"
title: "Vintage Storefront Layout"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A mail-order catalogue page: ruled columns, small caps, halftone product plates and a printed price block with the order code set in monospace."
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vintage Storefront Layout
Source: https://codefronts.com/design-styles/css-retro-designs/retro-clothing-store-web-ui-design/

A mail-order catalogue page: ruled columns, small caps, halftone product plates and a printed price block with the order code set in monospace. The typographic decisions are the demo &mdash; catalogue type was small, tightly leaded and set in serif with heavy tracking on the labels, and only one of those choices survives contact with an accessibility audit unchanged.
## HTML
```html
<section class="rt-19" aria-labelledby="rt-19-title">
  <h2 class="rt-19__sr" id="rt-19-title">Vintage mail-order catalogue storefront</h2>

  <div class="rt-19__theme">
    <input class="rt-19__theme-input" type="checkbox" id="rt-19-theme">
    <label class="rt-19__theme-label" for="rt-19-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-19__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-19__stage">
    <header class="rt-19__mast">
      <p class="rt-19__est">Established 1932 &middot; Northgate &amp; Co.</p>
      <h3 class="rt-19__h">Autumn Catalogue</h3>
      <p class="rt-19__sub">Outerwear, knitwear and workshirts &mdash; pages 44 to 47</p>
      <nav class="rt-19__nav" aria-label="Catalogue sections">
        <ul>
          <li><button class="rt-19__navbtn rt-19__navbtn--on" type="button">Outerwear</button></li>
          <li><button class="rt-19__navbtn" type="button">Knitwear</button></li>
          <li><button class="rt-19__navbtn" type="button">Shirting</button></li>
          <li><button class="rt-19__navbtn" type="button">Order form</button></li>
        </ul>
      </nav>
    </header>

    <ul class="rt-19__grid">
      <li class="rt-19__item">
        <span class="rt-19__plate rt-19__plate--a" role="img" aria-label="Catalogue plate: waxed cotton field coat, halftone illustration"></span>
        <h4 class="rt-19__name">Waxed Field Coat</h4>
        <p class="rt-19__desc">Four-pocket waxed cotton with corduroy collar and storm cuffs. Made in Yorkshire on a twelve-week lead.</p>
        <p class="rt-19__spec">Olive, Navy, Sand &middot; sizes 36&ndash;46</p>
        <p class="rt-19__price"><span class="rt-19__cur">&pound;</span>148<span class="rt-19__pence">00</span></p>
        <p class="rt-19__code">Order no. NG&ndash;4412</p>
      </li>
      <li class="rt-19__item">
        <span class="rt-19__plate rt-19__plate--b" role="img" aria-label="Catalogue plate: lambswool crew neck jumper, halftone illustration"></span>
        <h4 class="rt-19__name">Lambswool Crew</h4>
        <p class="rt-19__desc">Seven-gauge lambswool, fully fashioned shoulders, ribbed hem. Sixteen colours held in stock year round.</p>
        <p class="rt-19__spec">Sixteen colours &middot; sizes S&ndash;XXL</p>
        <p class="rt-19__price"><span class="rt-19__cur">&pound;</span>62<span class="rt-19__pence">50</span></p>
        <p class="rt-19__code">Order no. NG&ndash;2207</p>
      </li>
      <li class="rt-19__item">
        <span class="rt-19__plate rt-19__plate--c" role="img" aria-label="Catalogue plate: brushed cotton workshirt, halftone illustration"></span>
        <h4 class="rt-19__name">Brushed Workshirt</h4>
        <p class="rt-19__desc">Heavyweight brushed cotton, double-needle seams, two flap pockets. Cut generous through the body.</p>
        <p class="rt-19__spec">Check or plain &middot; sizes 14&frac12;&ndash;18</p>
        <p class="rt-19__price"><span class="rt-19__cur">&pound;</span>44<span class="rt-19__pence">00</span></p>
        <p class="rt-19__code">Order no. NG&ndash;1180</p>
      </li>
      <li class="rt-19__item">
        <span class="rt-19__plate rt-19__plate--d" role="img" aria-label="Catalogue plate: moleskin trousers, halftone illustration"></span>
        <h4 class="rt-19__name">Moleskin Trousers</h4>
        <p class="rt-19__desc">Peached moleskin with a straight leg and side adjusters. Softens considerably after the first wash.</p>
        <p class="rt-19__spec">Tobacco, Slate &middot; waist 30&ndash;42</p>
        <p class="rt-19__price"><span class="rt-19__cur">&pound;</span>78<span class="rt-19__pence">00</span></p>
        <p class="rt-19__code">Order no. NG&ndash;3095</p>
      </li>
    </ul>

    <footer class="rt-19__foot">
      <p>Post free on orders over &pound;120. Telephone orders taken 9 to 5, Monday to Saturday. Type here keeps the catalogue's proportions &mdash; small caps, tracked labels, ruled columns &mdash; and raises the body size and ink weight to a pairing that actually reads.</p>
    </footer>
  </div>
</section>
```
## CSS
```css
.rt-19 {
  --rt-19-dot: 6px;
  --rt-19-track: 0.16em;
  --rt-19-paper: #f3ecdd;
  --rt-19-paper: oklch(94% 0.022 88);
  --rt-19-paper-2: #e9e0cd;
  --rt-19-paper-2: oklch(90% 0.026 88);
  --rt-19-ink: #211c14;
  --rt-19-ink: oklch(23% 0.017 70);
  --rt-19-ink-2: #57503f;
  --rt-19-ink-2: oklch(45% 0.02 82);
  --rt-19-rule: #a89a7e;
  --rt-19-rule: oklch(70% 0.03 84);
  --rt-19-acc: #8c2b18;
  --rt-19-acc: oklch(41% 0.14 34);
  --rt-19-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif;
  --rt-19-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-19-paper);
  color: var(--rt-19-ink);
  font-family: var(--rt-19-serif);
  -webkit-text-size-adjust: 100%;
}

.rt-19 *,
.rt-19 *::before,
.rt-19 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-19 {
    --rt-19-paper: #1a1710;
    --rt-19-paper: oklch(21% 0.014 82);
    --rt-19-paper-2: #241f16;
    --rt-19-paper-2: oklch(26% 0.016 82);
    --rt-19-ink: #f1e9d8;
    --rt-19-ink: oklch(94% 0.016 88);
    --rt-19-ink-2: #b3a98f;
    --rt-19-ink-2: oklch(74% 0.022 88);
    --rt-19-rule: #4b4334;
    --rt-19-rule: oklch(38% 0.02 84);
    --rt-19-acc: #ff9a7a;
    --rt-19-acc: oklch(78% 0.13 34);
  }
}

.rt-19[data-theme="dark"],
.rt-19:has(.rt-19__theme-input:checked) {
  --rt-19-paper: #1a1710;
  --rt-19-paper: oklch(21% 0.014 82);
  --rt-19-paper-2: #241f16;
  --rt-19-paper-2: oklch(26% 0.016 82);
  --rt-19-ink: #f1e9d8;
  --rt-19-ink: oklch(94% 0.016 88);
  --rt-19-ink-2: #b3a98f;
  --rt-19-ink-2: oklch(74% 0.022 88);
  --rt-19-rule: #4b4334;
  --rt-19-rule: oklch(38% 0.02 84);
  --rt-19-acc: #ff9a7a;
  --rt-19-acc: oklch(78% 0.13 34);
}

@media (prefers-color-scheme: light) {
  .rt-19:has(.rt-19__theme-input:checked) {
    --rt-19-paper: #1a1710;
    --rt-19-paper: oklch(21% 0.014 82);
    --rt-19-paper-2: #241f16;
    --rt-19-paper-2: oklch(26% 0.016 82);
    --rt-19-ink: #f1e9d8;
    --rt-19-ink: oklch(94% 0.016 88);
    --rt-19-ink-2: #b3a98f;
    --rt-19-ink-2: oklch(74% 0.022 88);
    --rt-19-rule: #4b4334;
    --rt-19-rule: oklch(38% 0.02 84);
    --rt-19-acc: #ff9a7a;
    --rt-19-acc: oklch(78% 0.13 34);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-19:has(.rt-19__theme-input:checked) {
    --rt-19-paper: #f3ecdd;
    --rt-19-paper: oklch(94% 0.022 88);
    --rt-19-paper-2: #e9e0cd;
    --rt-19-paper-2: oklch(90% 0.026 88);
    --rt-19-ink: #211c14;
    --rt-19-ink: oklch(23% 0.017 70);
    --rt-19-ink-2: #57503f;
    --rt-19-ink-2: oklch(45% 0.02 82);
    --rt-19-rule: #a89a7e;
    --rt-19-rule: oklch(70% 0.03 84);
    --rt-19-acc: #8c2b18;
    --rt-19-acc: oklch(41% 0.14 34);
  }
}

.rt-19__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-19__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-19__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-19__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-19-rule);
  background: var(--rt-19-paper-2);
  color: var(--rt-19-ink-2);
  cursor: pointer;
}

.rt-19__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-19__theme-input:focus-visible + .rt-19__theme-label {
  outline: 2px solid var(--rt-19-acc);
  outline-offset: 2px;
}

.rt-19__stage {
  max-inline-size: 66rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.9rem, 0.6rem + 2vw, 2.5rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: clamp(1.25rem, 1rem + 1.5vw, 2rem);
}

.rt-19__mast {
  min-inline-size: 0;
  text-align: center;
  display: grid;
  gap: 0.5rem;
  justify-items: center;
  padding-block-end: 1.1rem;
  border-block-end: 3px double var(--rt-19-rule);
}

.rt-19__est {
  margin: 0;
  font-family: var(--rt-19-mono);
  font-size: 0.68rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--rt-19-ink-2);
}

.rt-19__h {
  margin: 0;
  font-size: clamp(1.9rem, 1.1rem + 4.5vw, 3.4rem);
  line-height: 1.02;
  letter-spacing: -0.015em;
  font-weight: 600;
  min-inline-size: 0;
  text-wrap: balance;
}

.rt-19__sub {
  margin: 0;
  font-size: 0.95rem;
  font-style: italic;
  color: var(--rt-19-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-19__nav {
  min-inline-size: 0;
}

.rt-19__nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.35rem;
}

.rt-19__navbtn {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 0.5rem 0.9rem;
  border: 1px solid var(--rt-19-rule);
  background: transparent;
  cursor: pointer;
  font: inherit;
  font-size: 0.78rem;
  letter-spacing: var(--rt-19-track);
  text-transform: uppercase;
  color: var(--rt-19-ink);
}

.rt-19__navbtn--on {
  background: var(--rt-19-ink);
  color: var(--rt-19-paper);
  border-color: var(--rt-19-ink);
}

.rt-19__navbtn:focus-visible {
  outline: 2px solid var(--rt-19-acc);
  outline-offset: 2px;
}

.rt-19__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: clamp(1.1rem, 0.8rem + 1.5vw, 1.8rem);
}

.rt-19__item {
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  align-content: start;
  padding-block-end: 1rem;
  border-block-end: 1px solid var(--rt-19-rule);
}

.rt-19__plate {
  display: block;
  inline-size: 100%;
  aspect-ratio: 1 / 1;
  min-inline-size: 0;
  border: 1px solid var(--rt-19-rule);
  background-color: var(--rt-19-paper-2);
  background-image: repeating-radial-gradient(circle at 0 0, var(--rt-19-ink) 0 1.4px, rgba(0,0,0,0) 1.5px var(--rt-19-dot)), linear-gradient(160deg, rgba(0,0,0,0.06), rgba(0,0,0,0));
  background-size: var(--rt-19-dot) var(--rt-19-dot), auto;
}

.rt-19__plate--b {
  --rt-19-dot: 5px;
}

.rt-19__plate--c {
  --rt-19-dot: 7px;
}

.rt-19__plate--d {
  --rt-19-dot: 4px;
}

.rt-19__name {
  margin: 0.35rem 0 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: var(--rt-19-track);
  text-transform: uppercase;
  min-inline-size: 0;
  overflow-wrap: break-word;
}

@supports (font-variant-caps: all-small-caps) {
  .rt-19__name {
    text-transform: none;
    font-variant-caps: all-small-caps;
    font-size: 1.2rem;
    letter-spacing: 0.09em;
  }
}

.rt-19__desc {
  margin: 0;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--rt-19-ink);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-19__spec {
  margin: 0;
  font-size: 0.82rem;
  font-style: italic;
  color: var(--rt-19-ink-2);
  min-inline-size: 0;
}

.rt-19__price {
  margin: 0.15rem 0 0;
  font-size: clamp(1.6rem, 1.1rem + 2vw, 2.2rem);
  line-height: 1;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
  color: var(--rt-19-acc);
  display: flex;
  align-items: flex-start;
  gap: 0.04em;
}

.rt-19__cur {
  font-size: 0.5em;
  padding-block-start: 0.18em;
}

.rt-19__pence {
  font-size: 0.5em;
  padding-block-start: 0.18em;
  padding-inline-start: 0.08em;
}

.rt-19__code {
  margin: 0;
  font-family: var(--rt-19-mono);
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  color: var(--rt-19-ink-2);
  font-variant-numeric: tabular-nums;
}

.rt-19__foot {
  min-inline-size: 0;
  padding-block-start: 1rem;
  border-block-start: 3px double var(--rt-19-rule);
}

.rt-19__foot p {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.65;
  color: var(--rt-19-ink-2);
  max-inline-size: 66ch;
  min-inline-size: 0;
  text-wrap: pretty;
}

@media (min-width: 40rem) {
  .rt-19__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 64rem) {
  .rt-19__grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}
```
