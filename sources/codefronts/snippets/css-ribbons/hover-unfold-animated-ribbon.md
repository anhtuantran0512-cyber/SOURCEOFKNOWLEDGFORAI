---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/hover-unfold-animated-ribbon/"
title: "Hover Unfold Animated Ribbon"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "A compact corner tab that unfurls into a full ribbon when the card is hovered or focused — and it genuinely animates the shape, not just an opacity fade."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hover Unfold Animated Ribbon
Source: https://codefronts.com/snippets/css-ribbons/hover-unfold-animated-ribbon/

A compact corner tab that unfurls into a full ribbon when the card is hovered or focused — and it genuinely animates the shape, not just an opacity fade. A registered @property percentage lives inside the clip-path, which is the only way to transition a polygon smoothly. Keyboard users get the same reveal through :focus-within.
## HTML
```html
<section class="rib-17" aria-label="Hover unfold animated ribbon demo">
  <div class="rib-17__stage">
    <p class="rib-17__hint">Hover a card — or press <kbd>Tab</kbd> to reach the buttons</p>
    <div class="rib-17__grid">
      <article class="rib-17__card">
        <div class="rib-17__media">
          <img class="rib-17__img" alt="Analogue wristwatch with a brown leather strap" loading="lazy" decoding="async" width="560" height="500"
            src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=720&auto=format&fit=crop">
          <span class="rib-17__ribbon" aria-hidden="true"><span class="rib-17__rlabel">Members save 30%</span></span>
          <span class="rib-17__sr">Members save 30 percent on this item</span>
        </div>
        <div class="rib-17__body">
          <h3 class="rib-17__name">Halden Field Watch</h3>
          <p class="rib-17__price">$210<s>$300</s></p>
          <button class="rib-17__cta" type="button">Add to bag</button>
        </div>
      </article>
      <article class="rib-17__card">
        <div class="rib-17__media">
          <img class="rib-17__img" alt="Minimal desk lamp casting warm light on a wall" loading="lazy" decoding="async" width="560" height="500"
            src="https://images.unsplash.com/photo-1507473885765-e6ed057f782c?q=80&w=720&auto=format&fit=crop">
          <span class="rib-17__ribbon" aria-hidden="true"><span class="rib-17__rlabel">Members save 30%</span></span>
          <span class="rib-17__sr">Members save 30 percent on this item</span>
        </div>
        <div class="rib-17__body">
          <h3 class="rib-17__name">Orbit Task Lamp</h3>
          <p class="rib-17__price">$126<s>$180</s></p>
          <button class="rib-17__cta" type="button">Add to bag</button>
        </div>
      </article>
    </div>
    <p class="rib-17__chip" aria-hidden="true">@property &lt;percentage&gt; in clip-path · transition on a custom property · :focus-within</p>
  </div>
</section>
```
## CSS
```css
@property --rib-17-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.rib-17,
.rib-17 *,
.rib-17 *::before,
.rib-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-17-bg: #111318;
  --rib-17-bg: oklch(0.2 0.01 265);
  --rib-17-card: #1a1d24;
  --rib-17-card: oklch(0.25 0.012 265);
  --rib-17-ink: #eef0f5;
  --rib-17-ink: oklch(0.95 0.006 265);
  --rib-17-mut: #8b91a0;
  --rib-17-mut: oklch(0.65 0.016 265);
  --rib-17-acc: #ff5f7e;
  --rib-17-acc: oklch(0.68 0.19 5);
  --rib-17-h: 44px;
  background: var(--rib-17-bg);
  color: var(--rib-17-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(14px,2.6vw,22px);
  padding: clamp(20px,5vw,56px);
}

.rib-17__hint {
  font-size: 12.5px;
  color: var(--rib-17-mut);
  letter-spacing: .02em;
}

.rib-17__hint kbd {
  padding: 2px 6px;
  border-radius: 5px;
  background: oklch(1 0 0/.1);
  border: 1px solid oklch(1 0 0/.14);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
}

.rib-17__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(240px,1fr));
  gap: clamp(14px,2.6vw,22px);
  width: min(100%,760px);
}

.rib-17__card {
  border-radius: 20px;
  overflow: hidden;
  background: var(--rib-17-card);
  border: 1px solid oklch(1 0 0/.08);
  box-shadow: 0 22px 50px -28px oklch(0 0 0/.85);
  transition: border-color .35s,translate .4s cubic-bezier(.16,1,.3,1);
}

.rib-17__card:hover,
.rib-17__card:focus-within {
  translate: 0 -4px;
  border-color: color-mix(in oklch,var(--rib-17-acc) 40%,transparent);
}

.rib-17__media {
  position: relative;
  aspect-ratio: 7/6;
  overflow: hidden;
  background: linear-gradient(150deg,oklch(0.38 0.03 265),oklch(0.28 0.02 265));
}

.rib-17__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: scale .7s cubic-bezier(.16,1,.3,1);
}

.rib-17__card:hover .rib-17__img,
.rib-17__card:focus-within .rib-17__img {
  scale: 1.05;
}

.rib-17__ribbon {
  position: absolute;
  inset-block-end: 18px;
  inset-inline-start: 0;
  display: grid;
  align-items: center;
  min-block-size: var(--rib-17-h);
  padding-inline: 16px 20px;
  background: #ff5f7e;
  background: linear-gradient(100deg,color-mix(in oklch,var(--rib-17-acc) 100%,white 12%),var(--rib-17-acc));
  clip-path: inset(0 calc(100% - var(--rib-17-p)) 0 0);
  box-shadow: 0 10px 22px -10px color-mix(in oklch,var(--rib-17-acc) 70%,transparent);
  transition: --rib-17-p .55s cubic-bezier(.16,1,.3,1);
}

.rib-17__card:hover .rib-17__ribbon,
.rib-17__card:focus-within .rib-17__ribbon {
  --rib-17-p: 100%;
}

.rib-17__rlabel {
  color: oklch(0.16 0.04 5);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .04em;
  white-space: nowrap;
  translate: -14px 0;
  opacity: 0;
  transition: translate .5s cubic-bezier(.16,1,.3,1) .1s,opacity .35s ease .12s;
}

.rib-17__card:hover .rib-17__rlabel,
.rib-17__card:focus-within .rib-17__rlabel {
  translate: 0 0;
  opacity: 1;
}

.rib-17__ribbon::after {
  content: '';
  position: absolute;
  inset-block-start: 100%;
  inset-inline-start: 0;
  inline-size: 14px;
  block-size: 12px;
  background: color-mix(in oklch,var(--rib-17-acc) 52%,black);
  clip-path: polygon(0 0,100% 0,100% 100%);
  scale: 0 1;
  transform-origin: left center;
  transition: scale .35s cubic-bezier(.16,1,.3,1) .14s;
}

.rib-17__card:hover .rib-17__ribbon::after,
.rib-17__card:focus-within .rib-17__ribbon::after {
  scale: 1 1;
}

.rib-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.rib-17__body {
  display: grid;
  gap: 8px;
  padding: 18px 19px 20px;
}

.rib-17__name {
  font-size: 18px;
  font-weight: 640;
  letter-spacing: -.022em;
}

.rib-17__price {
  display: flex;
  align-items: baseline;
  gap: 9px;
  font-size: 20px;
  font-weight: 750;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.rib-17__price s {
  font-size: 13.5px;
  font-weight: 400;
  color: var(--rib-17-mut);
}

.rib-17__cta {
  margin-block-start: 6px;
  min-height: 46px;
  border: 1.5px solid oklch(1 0 0/.16);
  border-radius: 12px;
  background: transparent;
  color: var(--rib-17-ink);
  font: inherit;
  font-size: 14.5px;
  font-weight: 640;
  cursor: pointer;
  transition: background .25s,border-color .25s;
}

.rib-17__cta:hover {
  background: oklch(1 0 0/.07);
  border-color: var(--rib-17-acc);
}

.rib-17__cta:focus-visible {
  outline: 3px solid var(--rib-17-acc);
  outline-offset: 3px;
}

.rib-17__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-17-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (hover: none) {
  .rib-17__ribbon {
    --rib-17-p: 100%;
  }

  .rib-17__rlabel {
    translate: 0 0;
    opacity: 1;
  }

  .rib-17__ribbon::after {
    scale: 1 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rib-17 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
