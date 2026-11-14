---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/e-commerce-header-with-cart-wishlist-account/"
title: "E-Commerce Header with Cart Wishlist Account"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A storefront header with the utility cluster shoppers reach for: account, a wishlist heart carrying its count, and a cart pill showing the running total."
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Header with Cart Wishlist Account
Source: https://codefronts.com/layouts/css-header-designs/e-commerce-header-with-cart-wishlist-account/

A storefront header with the utility cluster shoppers reach for: account, a wishlist heart carrying its count, and a cart pill showing the running total. Hovering Shop opens a category mega panel with three featured products; the count and total use tabular-nums so nothing shifts as the basket changes. Peach-to-lavender ground, condensed display type, accent-tinted shadow bloom.
## HTML
```html
<div class="hd-04">
  <a class="hd-04__skip" href="#hd-04-main">Skip to content</a>

  <header class="hd-04__bar">
    <a class="hd-04__brand" href="#hd-04-main">
      <svg class="hd-04__mark" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
        <path d="M4 9.5h20l-2.2 13a2 2 0 0 1-2 1.7H8.2a2 2 0 0 1-2-1.7L4 9.5Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
        <path d="M10 9.5V7.6a4 4 0 0 1 8 0v1.9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
      <span class="hd-04__word">Lumen &amp; Field</span>
    </a>

    <nav class="hd-04__nav" aria-label="Main">
      <ul class="hd-04__nav-list">
        <li class="hd-04__item">
          <a href="#hd-04-main" aria-haspopup="menu">Shop
            <svg class="hd-04__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 10.5 12 14.5l4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <div class="hd-04__mega" role="menu" aria-label="Shop categories">
            <div class="hd-04__cats">
              <p class="hd-04__mega-h">Categories</p>
              <a role="menuitem" href="#hd-04-main">New arrivals</a>
              <a role="menuitem" href="#hd-04-main">Footwear</a>
              <a role="menuitem" href="#hd-04-main">Outerwear</a>
              <a role="menuitem" href="#hd-04-main">Accessories</a>
              <a role="menuitem" href="#hd-04-main">Home objects</a>
              <a role="menuitem" href="#hd-04-main" class="hd-04__sale">Last chance</a>
            </div>
            <div class="hd-04__feat">
              <p class="hd-04__mega-h">Featured this week</p>
              <div class="hd-04__cards">
                <a class="hd-04__card" role="menuitem" href="#hd-04-main">
                  <span class="hd-04__shot"><img src="https://images.unsplash.com/photo-1560769629-975ec94e6a86?auto=format&amp;fit=crop&amp;w=420&amp;q=70" alt="Low-top canvas sneakers in bone white" loading="lazy" width="420" height="315"></span>
                  <span class="hd-04__card-t">Ridge low-top</span>
                  <span class="hd-04__card-p">$128.00</span>
                </a>
                <a class="hd-04__card" role="menuitem" href="#hd-04-main">
                  <span class="hd-04__shot"><img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&amp;fit=crop&amp;w=420&amp;q=70" alt="Analogue wristwatch with a woven strap" loading="lazy" width="420" height="315"></span>
                  <span class="hd-04__card-t">Field watch 38</span>
                  <span class="hd-04__card-p">$245.00</span>
                </a>
                <a class="hd-04__card" role="menuitem" href="#hd-04-main">
                  <span class="hd-04__shot"><img src="https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&amp;fit=crop&amp;w=420&amp;q=70" alt="Sunglasses with amber lenses on a pale surface" loading="lazy" width="420" height="315"></span>
                  <span class="hd-04__card-t">Meridian shades</span>
                  <span class="hd-04__card-p">$96.00</span>
                </a>
              </div>
            </div>
            <div class="hd-04__promo">
              <p class="hd-04__promo-k">Members</p>
              <p class="hd-04__promo-t">Free returns for 60 days</p>
              <p class="hd-04__promo-d">Plus early access to the autumn drop on 2 September.</p>
              <span class="hd-04__promo-cta" aria-hidden="true">Join free &#8594;</span>
            </div>
          </div>
        </li>
        <li class="hd-04__item"><a href="#hd-04-main">Collections</a></li>
        <li class="hd-04__item"><a href="#hd-04-main">Journal</a></li>
        <li class="hd-04__item"><a href="#hd-04-main">Stores</a></li>
      </ul>
    </nav>

    <label class="hd-04__search" for="hd-04-q">
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <input class="hd-04__q" id="hd-04-q" type="text" placeholder="Search boots, bags, gifts" aria-label="Search products">
    </label>

    <div class="hd-04__utility">
      <input class="hd-04__sr" type="checkbox" id="hd-04-dark">
      <label class="hd-04__theme" for="hd-04-dark">
        <svg class="hd-04__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-04__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-04__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-04__ic" href="#hd-04-main" aria-label="Your account">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="8.4" r="3.6" stroke="currentColor" stroke-width="1.8"/><path d="M5.4 19.6a6.8 6.8 0 0 1 13.2 0" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </a>
      <a class="hd-04__ic" href="#hd-04-main" aria-label="Wishlist, 4 saved items">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 20s-7.3-4.4-7.3-9.2A4.3 4.3 0 0 1 12 8.2a4.3 4.3 0 0 1 7.3 2.6C19.3 15.6 12 20 12 20Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-04__count">4</span>
      </a>
      <a class="hd-04__cart" href="#hd-04-main">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M3.5 5h2.2l2.1 9.6a1.8 1.8 0 0 0 1.8 1.4h7.7a1.8 1.8 0 0 0 1.7-1.3l1.6-5.7H7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><circle cx="10" cy="19.4" r="1.4" fill="currentColor"/><circle cx="17.4" cy="19.4" r="1.4" fill="currentColor"/></svg>
        <span class="hd-04__cart-total">$142.00</span>
        <span class="hd-04__cart-n">3</span>
      </a>
    </div>
  </header>

  <main class="hd-04__main" id="hd-04-main">
    <section class="hd-04__hero">
      <p class="hd-04__eyebrow">Autumn 2026</p>
      <h1>Made for the long walk home.</h1>
      <p class="hd-04__lead">Hover <strong>Shop</strong> in the header to open the category panel. The cart pill keeps its running total in tabular figures, so the bar never shifts when your basket changes.</p>
      <div class="hd-04__actions"><a class="hd-04__cta" href="#hd-04-main">Shop the edit</a><a class="hd-04__cta2" href="#hd-04-main">Find a store</a></div>
    </section>

    <ul class="hd-04__grid">
      <li><span class="hd-04__shot"><img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&amp;fit=crop&amp;w=520&amp;q=70" alt="Red high-top trainer on a plain background" loading="lazy" width="520" height="390"></span><p class="hd-04__g-t">Crimson runner</p><p class="hd-04__g-p">$118.00</p></li>
      <li><span class="hd-04__shot"><img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&amp;fit=crop&amp;w=520&amp;q=70" alt="Over-ear headphones in matte black" loading="lazy" width="520" height="390"></span><p class="hd-04__g-t">Quiet Field over-ear</p><p class="hd-04__g-p">$264.00</p></li>
      <li><span class="hd-04__shot"><img src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&amp;fit=crop&amp;w=520&amp;q=70" alt="Camera lens standing on a table" loading="lazy" width="520" height="390"></span><p class="hd-04__g-t">Prime 35mm</p><p class="hd-04__g-p">$399.00</p></li>
      <li><span class="hd-04__shot"><img src="https://images.unsplash.com/photo-1491553895911-0055eca6402d?auto=format&amp;fit=crop&amp;w=520&amp;q=70" alt="Pair of white trainers seen from above" loading="lazy" width="520" height="390"></span><p class="hd-04__g-t">Bone court</p><p class="hd-04__g-p">$134.00</p></li>
    </ul>
    <div class="hd-04__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-04 {
  --bg-a: #fff1e6;
  --bg-b: #efe6ff;
  --panel: #ffffff;
  --panel2: #fdf6f0;
  --ink: #241a20;
  --muted: #6f6169;
  --line: rgba(36,26,32,.12);
  --line2: rgba(36,26,32,.2);
  --accent: #e2553c;
  --accent-soft: rgba(226,85,60,.12);
  --accent-ink: #ffffff;
  --bloom: .22;
  --font-display: "Avenir Next Condensed","Arial Narrow",system-ui,sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: linear-gradient(170deg, var(--bg-a) 0%, var(--bg-b) 46%, var(--panel) 100%);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-04 {
    --bg-a: oklch(95% .04 60);
    --bg-b: oklch(93% .045 300);
    --ink: oklch(22% .02 350);
    --muted: oklch(52% .02 350);
    --accent: oklch(62% .16 32);
  }
}

.hd-04 * {
  box-sizing: border-box;
}

.hd-04 h1,
.hd-04 p,
.hd-04 ul {
  margin: 0;
  padding: 0;
}

.hd-04 ul {
  list-style: none;
}

.hd-04 [hidden] {
  display: none;
}

.hd-04 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .4rem;
}

.hd-04__skip {
  position: absolute;
  inset-inline-start: .75rem;
  top: -3rem;
  z-index: 60;
  padding: .55rem 1rem;
  border-radius: 999px;
  background: var(--ink);
  color: #fff;
  font-size: .82rem;
  font-weight: 640;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-04__skip:focus-visible {
  top: .75rem;
}
/* ── header: elevated with accent bloom ───────────────────────────── */

.hd-04__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.6rem,2vw,1.25rem);
  padding: .85rem clamp(.85rem,3vw,1.75rem);
  background: color-mix(in srgb, var(--panel) 88%, transparent);
  backdrop-filter: blur(12px) saturate(150%);
  box-shadow: 0 1px 0 var(--line), 0 1.1rem 2.4rem -1.2rem rgba(226,85,60,var(--bloom));
}

.hd-04__brand {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-04__mark {
  inline-size: 1.7rem;
  block-size: 1.7rem;
  color: var(--accent);
  flex: none;
}

.hd-04__word {
  font-family: var(--font-display);
  font-size: 1.14rem;
  font-weight: 700;
  letter-spacing: .01em;
  text-transform: uppercase;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-04__nav {
  min-inline-size: 0;
}

.hd-04__nav-list {
  display: flex;
  align-items: center;
  gap: .1rem;
}

.hd-04__item {
  position: relative;
}

.hd-04__nav-list a {
  display: inline-flex;
  align-items: center;
  gap: .25rem;
  padding: .5rem .7rem;
  border-radius: .5rem;
  color: var(--ink);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: .02em;
  text-transform: uppercase;
  white-space: nowrap;
  transition: color .15s ease, background-color .15s ease;
}

.hd-04__nav-list a:hover {
  color: var(--accent);
  background: var(--accent-soft);
}

.hd-04__chev {
  inline-size: .9rem;
  block-size: .9rem;
  transition: rotate .2s ease;
}

.hd-04__item:has(> a:hover) .hd-04__chev {
  rotate: 180deg;
}

.hd-04__mega {
  position: absolute;
  inset-inline-start: -1rem;
  top: calc(100% + .6rem);
  z-index: 35;
  inline-size: min(58rem,92vw);
  display: grid;
  grid-template-columns: 11rem minmax(0,1fr) 13rem;
  gap: 1.25rem;
  padding: 1.25rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel);
  box-shadow: 0 2rem 3.5rem -1.4rem rgba(36,26,32,.3), 0 0 0 1px rgba(226,85,60,.08);
  visibility: hidden;
  opacity: 0;
  translate: 0 -.4rem;
  transition: opacity .18s ease, translate .18s ease, visibility .18s allow-discrete;
}

.hd-04__item:has(> a:hover) > .hd-04__mega,
.hd-04__item:has(> a:focus-visible) > .hd-04__mega,
.hd-04__item:hover > .hd-04__mega,
.hd-04__item:focus-within > .hd-04__mega {
  visibility: visible;
  opacity: 1;
  translate: 0 0;
}

.hd-04__mega-h {
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: .5rem;
}

.hd-04__cats {
  display: grid;
  gap: .1rem;
  align-content: start;
  border-inline-end: 1px solid var(--line);
  padding-inline-end: 1rem;
}

.hd-04__cats a {
  font-family: var(--font-body);
  font-size: .88rem;
  font-weight: 520;
  text-transform: none;
  letter-spacing: 0;
  padding: .4rem .5rem;
  min-block-size: 2.2rem;
}

.hd-04__sale {
  color: var(--accent) !important;
  font-weight: 640 !important;
}

.hd-04__cards {
  display: grid;
  grid-template-columns: repeat(3,minmax(0,1fr));
  gap: .75rem;
}

.hd-04__card {
  display: grid !important;
  gap: .3rem;
  padding: .4rem !important;
  border-radius: .7rem !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: var(--font-body) !important;
  min-inline-size: 0;
}

.hd-04__card:hover {
  background: var(--panel2) !important;
}

.hd-04__shot {
  display: block;
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: .55rem;
  background: linear-gradient(135deg, var(--bg-a), var(--bg-b));
}

.hd-04__shot img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
  transition: scale .35s ease;
}

.hd-04__card:hover .hd-04__shot img {
  scale: 1.05;
}

.hd-04__card-t {
  font-size: .84rem;
  font-weight: 600;
}

.hd-04__card-p {
  font-size: .8rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.hd-04__promo {
  display: grid;
  align-content: start;
  gap: .3rem;
  padding: 1rem;
  border-radius: .8rem;
  background: linear-gradient(160deg, var(--accent-soft), transparent 70%), var(--panel2);
  border: 1px solid var(--line);
}

.hd-04__promo-k {
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-04__promo-t {
  font-family: var(--font-display);
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.15;
  text-wrap: balance;
}

.hd-04__promo-d {
  font-size: .8rem;
  color: var(--muted);
}

.hd-04__promo-cta {
  font-size: .82rem;
  font-weight: 640;
  color: var(--accent);
  margin-top: .2rem;
}

.hd-04__search {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex: 1;
  min-inline-size: 0;
  max-inline-size: 17rem;
  min-block-size: 2.5rem;
  padding: .4rem .8rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--panel2);
  cursor: text;
  transition: border-color .15s ease, box-shadow .15s ease;
}

.hd-04__search svg {
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--muted);
  flex: none;
}

.hd-04__q {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: .86rem;
  color: var(--ink);
}

.hd-04__q::placeholder {
  color: var(--muted);
}

.hd-04__q:focus {
  outline: none;
}

.hd-04__search:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-soft);
}

.hd-04__utility {
  display: flex;
  align-items: center;
  gap: .3rem;
  margin-inline-start: auto;
}

.hd-04__ic {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 999px;
  color: var(--ink);
  overflow: visible;
  transition: background-color .15s ease, color .15s ease;
}

.hd-04__ic svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.hd-04__ic:hover {
  background: var(--accent-soft);
  color: var(--accent);
}

.hd-04__count {
  position: absolute;
  top: .35rem;
  inset-inline-end: .3rem;
  min-inline-size: 1.1rem;
  block-size: 1.1rem;
  display: grid;
  place-items: center;
  padding: 0 .2rem;
  border-radius: 999px;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .66rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  box-shadow: 0 0 0 2px var(--panel);
}

.hd-04__cart {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  padding: .5rem .8rem .5rem .7rem;
  border-radius: 999px;
  background: var(--ink);
  color: #fff;
  text-decoration: none;
  font-size: .86rem;
  font-weight: 640;
  box-shadow: 0 .6rem 1.4rem -.6rem rgba(36,26,32,.55);
  transition: translate .15s ease, background-color .15s ease;
}

.hd-04__cart svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-04__cart:hover {
  translate: 0 -1px;
  background: var(--accent);
}

.hd-04__cart-total {
  font-variant-numeric: tabular-nums;
}

.hd-04__cart-n {
  display: grid;
  place-items: center;
  min-inline-size: 1.25rem;
  block-size: 1.25rem;
  border-radius: 999px;
  background: rgba(255,255,255,.2);
  font-size: .7rem;
  font-variant-numeric: tabular-nums;
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-04__main {
  max-inline-size: 76rem;
  margin-inline: auto;
  padding: clamp(2rem,6vw,4rem) clamp(1rem,3vw,1.75rem) 4rem;
}

.hd-04__eyebrow {
  font-family: var(--font-display);
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-04__hero h1 {
  font-family: var(--font-display);
  font-size: clamp(2.2rem,8vw,4.6rem);
  line-height: .98;
  letter-spacing: -.01em;
  text-transform: uppercase;
  font-weight: 700;
  margin-top: .6rem;
  max-inline-size: 22ch;
  text-wrap: balance;
}

.hd-04__lead {
  margin-top: 1rem;
  max-inline-size: 52ch;
  color: var(--muted);
  font-size: 1.02rem;
  text-wrap: pretty;
}

.hd-04__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  margin-top: 1.5rem;
}

.hd-04__cta,
.hd-04__cta2 {
  padding: .8rem 1.4rem;
  border-radius: 999px;
  text-decoration: none;
  font-size: .9rem;
  font-weight: 650;
  transition: translate .15s ease;
}

.hd-04__cta {
  background: var(--accent);
  color: var(--accent-ink);
  box-shadow: 0 .8rem 1.8rem -.7rem rgba(226,85,60,.75);
}

.hd-04__cta2 {
  border: 1px solid var(--line2);
  color: var(--ink);
}

.hd-04__cta:hover,
.hd-04__cta2:hover {
  translate: 0 -2px;
}

.hd-04__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
  margin-top: clamp(2rem,6vw,3.5rem);
}

.hd-04__grid li {
  min-inline-size: 0;
  padding: .6rem;
  border-radius: .9rem;
  background: var(--panel);
  border: 1px solid var(--line);
  box-shadow: 0 1rem 2rem -1.4rem rgba(226,85,60,.5);
}

.hd-04__g-t {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 660;
  text-transform: uppercase;
  letter-spacing: .02em;
  margin-top: .55rem;
}

.hd-04__g-p {
  font-size: .85rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.hd-04__filler {
  block-size: 45vh;
}

@media (max-width: 1080px) {
  .hd-04__mega {
    grid-template-columns: 10rem minmax(0,1fr);
    inline-size: min(44rem,92vw);
  }

  .hd-04__promo {
    display: none;
  }

  .hd-04__cards {
    grid-template-columns: repeat(2,minmax(0,1fr));
  }
}

@media (max-width: 860px) {
  .hd-04__search {
    display: none;
  }
}

@media (max-width: 760px) {
  .hd-04__bar {
    flex-wrap: wrap;
  }

  .hd-04__nav {
    order: 3;
    flex-basis: 100%;
    overflow: auto;
    scroll-snap-type: x proximity;
    scrollbar-width: none;
  }

  .hd-04__nav::-webkit-scrollbar {
    display: none;
  }

  .hd-04__nav-list a {
    scroll-snap-align: start;
  }

  .hd-04__mega {
    position: static;
    inline-size: 100%;
    grid-template-columns: minmax(0,1fr);
    visibility: visible;
    opacity: 1;
    translate: 0 0;
    display: none;
    box-shadow: none;
  }

  .hd-04__item:focus-within > .hd-04__mega {
    display: grid;
  }

  .hd-04__cats {
    border-inline-end: 0;
    padding-inline-end: 0;
  }
}

@media (max-width: 430px) {
  .hd-04__cart-total {
    display: none;
  }

  .hd-04__word {
    font-size: 1rem;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-04:has(#hd-04-dark:checked) {
  --bg-a: #2a1a20;
  --bg-b: #1a1726;
  --panel: #171319;
  --panel2: #211a22;
  --ink: #f7eeea;
  --muted: #b09ea6;
  --line: rgba(247,238,234,.12);
  --line2: rgba(247,238,234,.22);
  --accent: #ff8a6b;
  --accent-soft: rgba(255,138,107,.16);
  --accent-ink: #2a0f06;
  --bloom: .3;
}

.hd-04:has(#hd-04-dark:checked) .hd-04__cart {
  background: var(--accent);
  color: var(--accent-ink);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-04__sun {
  display: none;
}

.hd-04:has(#hd-04-dark:checked) .hd-04__moon {
  display: none;
}

.hd-04:has(#hd-04-dark:checked) .hd-04__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-04:not([data-theme="light"]):not(:has(#hd-04-dark:checked)) {
    --bg-a: #2a1a20;
    --bg-b: #1a1726;
    --panel: #171319;
    --panel2: #211a22;
    --ink: #f7eeea;
    --muted: #b09ea6;
    --line: rgba(247,238,234,.12);
    --line2: rgba(247,238,234,.22);
    --accent: #ff8a6b;
    --accent-soft: rgba(255,138,107,.16);
    --accent-ink: #2a0f06;
    --bloom: .3;
  }

  .hd-04:not([data-theme="light"]):not(:has(#hd-04-dark:checked)) .hd-04__cart {
    background: var(--accent);
    color: var(--accent-ink);
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-04:has(#hd-04-dark:checked) {
    --bg-a: #fff1e6;
    --bg-b: #efe6ff;
    --panel: #ffffff;
    --panel2: #fdf6f0;
    --ink: #241a20;
    --muted: #6f6169;
    --line: rgba(36,26,32,.12);
    --line2: rgba(36,26,32,.2);
    --accent: #e2553c;
    --accent-soft: rgba(226,85,60,.12);
    --accent-ink: #ffffff;
    --bloom: .22;
    --font-display: "Avenir Next Condensed","Arial Narrow",system-ui,sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }

  .hd-04:has(#hd-04-dark:checked) .hd-04__cart {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    min-block-size: 2.75rem;
    padding: .5rem .8rem .5rem .7rem;
    border-radius: 999px;
    background: var(--ink);
    color: #fff;
    text-decoration: none;
    font-size: .86rem;
    font-weight: 640;
    box-shadow: 0 .6rem 1.4rem -.6rem rgba(36,26,32,.55);
    transition: translate .15s ease, background-color .15s ease;
  }
  /* the icon always offers the scheme you are not in */

  .hd-04:not([data-theme="light"]):not(:has(#hd-04-dark:checked)) .hd-04__moon {
    display: none;
  }

  .hd-04:not([data-theme="light"]):not(:has(#hd-04-dark:checked)) .hd-04__sun {
    display: block;
  }

  .hd-04:has(#hd-04-dark:checked) .hd-04__sun {
    display: none;
  }

  .hd-04:has(#hd-04-dark:checked) .hd-04__moon {
    display: block;
  }
}

.hd-04[data-theme="dark"] {
  --bg-a: #2a1a20;
  --bg-b: #1a1726;
  --panel: #171319;
  --panel2: #211a22;
  --ink: #f7eeea;
  --muted: #b09ea6;
  --line: rgba(247,238,234,.12);
  --line2: rgba(247,238,234,.22);
  --accent: #ff8a6b;
  --accent-soft: rgba(255,138,107,.16);
  --accent-ink: #2a0f06;
}

@media (prefers-reduced-motion: reduce) {
  .hd-04 * {
    transition-duration: 1ms !important;
    animation-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-04__mega {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-04__sr,
.hd-04__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-04__theme {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: inherit;
  cursor: pointer;
  transition: background-color .18s ease;
}

.hd-04__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-04__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-04:has(#hd-04-dark:focus-visible) .hd-04__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
