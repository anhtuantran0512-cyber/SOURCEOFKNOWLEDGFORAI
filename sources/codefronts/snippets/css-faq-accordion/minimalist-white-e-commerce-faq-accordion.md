---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/minimalist-white-e-commerce-faq-accordion/"
title: "Minimalist White E-Commerce FAQ Accordion"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The product-page FAQ that converts: shipping, returns and care answers in a bone-white, hairline-divided accordion sitting beside the product photo — the…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist White E-Commerce FAQ Accordion
Source: https://codefronts.com/snippets/css-faq-accordion/minimalist-white-e-commerce-faq-accordion/

The product-page FAQ that converts: shipping, returns and care answers in a bone-white, hairline-divided accordion sitting beside the product photo — the exact layout premium DTC brands (and every Shopify theme worth buying) use. No borders-on-borders, no color except one warm accent, generous whitespace, and an em-dash marker instead of a chevron. Minimalism here is a discipline demo: every rule that isn't structure or type has been deleted.
## HTML
```html
<section class="cfa-08" aria-label="Minimalist e-commerce FAQ accordion">
  <div class="cfa-08__stage">
    <div class="cfa-08__cols">
      <figure class="cfa-08__photo" style="--img:url('https://images.unsplash.com/photo-1523381210434-271e8be1f52b?q=80&w=1200&auto=format&fit=crop')">
        <figcaption>Heavyweight organic tee — $48</figcaption>
      </figure>
      <div class="cfa-08__faq">
        <h1>Details &amp; care</h1>
        <div class="cfa-08__list">
          <details class="cfa-08__item" open>
            <summary class="cfa-08__q">Shipping &amp; delivery<i aria-hidden="true"></i></summary>
            <div class="cfa-08__a"><p>Free carbon-neutral shipping over $75, dispatched within 24 hours. US 2–4 business days, UK &amp; EU 3–5, Australia 4–7. A tracked link lands in your inbox at dispatch.</p></div>
          </details>
          <details class="cfa-08__item">
            <summary class="cfa-08__q">Returns &amp; exchanges<i aria-hidden="true"></i></summary>
            <div class="cfa-08__a"><p>60 days, free, no questions. Start a return from your order email and drop the package at any carrier point — refunds land 3–5 days after scanning. Exchanges ship before your return even arrives.</p></div>
          </details>
          <details class="cfa-08__item">
            <summary class="cfa-08__q">Fabric &amp; fit<i aria-hidden="true"></i></summary>
            <div class="cfa-08__a"><p>230gsm organic cotton, garment-dyed and pre-shrunk. The fit is relaxed through the body with a ribbed collar that holds its shape — if you are between sizes, size down.</p></div>
          </details>
          <details class="cfa-08__item">
            <summary class="cfa-08__q">Care instructions<i aria-hidden="true"></i></summary>
            <div class="cfa-08__a"><p>Machine wash cold, inside out, with like colors. Hang dry — the dryer is where the garment-dye patina goes to die. Iron low, never on the print.</p></div>
          </details>
        </div>
        <p class="cfa-08__foot">One hairline per item, one accent color, zero boxes.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.cfa-08,
.cfa-08 *,
.cfa-08 *::before,
.cfa-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-08 {
  --bg: oklch(0.99 0.004 90);
  --ink: oklch(0.24 0.012 60);
  --mut: oklch(0.45 0.015 60);
  --line: oklch(0.9 0.008 80);
  --acc: oklch(0.55 0.12 40);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-08__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,64px);
  background: var(--bg);
  container: cfa08/inline-size;
}

.cfa-08__cols {
  display: grid;
  grid-template-columns: minmax(0,5fr) minmax(0,6fr);
  gap: clamp(28px,5cqi,72px);
  align-items: center;
  width: min(100%,980px);
}

.cfa-08__photo {
  aspect-ratio: 4/5;
  background-image: linear-gradient(oklch(0.9 0.01 80/.1),oklch(0.85 0.015 70/.2)),var(--img);
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: flex-end;
}

.cfa-08__photo figcaption {
  width: 100%;
  padding: 14px 16px;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.99 0.004 90);
  background: linear-gradient(transparent,oklch(0.2 0.01 60/.55));
}

.cfa-08__faq h1 {
  font-size: clamp(22px,3cqi,30px);
  font-weight: 600;
  letter-spacing: -.02em;
}

.cfa-08__list {
  margin-top: 18px;
  border-top: 1px solid var(--line);
  interpolate-size: allow-keywords;
}

.cfa-08__item {
  border-bottom: 1px solid var(--line);
}

.cfa-08__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 22px 2px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .02em;
  list-style: none;
  transition: color .2s;
}

.cfa-08__q::-webkit-details-marker {
  display: none;
}

.cfa-08__q:hover {
  color: var(--acc);
}

.cfa-08__q:focus-visible {
  outline: 1.5px solid var(--acc);
  outline-offset: 4px;
}

.cfa-08__q i {
  position: relative;
  flex: none;
  width: 14px;
  height: 14px;
}

.cfa-08__q i::before,
.cfa-08__q i::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  width: 14px;
  height: 1px;
  background: currentColor;
  transition: rotate .4s cubic-bezier(.4,0,.2,1);
}

.cfa-08__q i::after {
  rotate: 90deg;
}

.cfa-08__item[open] .cfa-08__q i::after {
  rotate: 0deg;
}

.cfa-08__a p {
  padding: 0 2px 22px;
  font-size: 13.5px;
  line-height: 1.8;
  color: var(--mut);
  max-width: 52ch;
  translate: 0 0;
  transition: translate .35s,opacity .35s;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-08__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .4s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .4s allow-discrete;
  }

  .cfa-08__item[open]::details-content {
    height: auto;
    opacity: 1;
  }

  .cfa-08__item:not([open]) .cfa-08__a p {
    translate: 0 4px;
  }
}

.cfa-08__foot {
  margin-top: 16px;
  font-size: 11.5px;
  letter-spacing: .04em;
  color: var(--mut);
}

@container cfa08 (width < 720px) {
  .cfa-08__cols {
    grid-template-columns: 1fr;
  }

  .cfa-08__photo {
    max-height: 340px;
    aspect-ratio: 16/10;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cfa-08 *,
    .cfa-08 .cfa-08__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
