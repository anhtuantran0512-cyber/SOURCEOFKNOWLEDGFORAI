---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/obsidian-editorial/"
title: "Dark Mode Editorial Quote Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The card developer-tool and tech-publication sites converge on: serif quote, restrained ink, and a hairline border that catches light like brushed metal."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Editorial Quote Card
Source: https://codefronts.com/components/css-testimonials-reviews/obsidian-editorial/

The card developer-tool and tech-publication sites converge on: serif quote, restrained ink, and a hairline border that catches light like brushed metal. It ships with a working theme toggle built on the light-dark() function and color-scheme — one property flips the entire card between modes with no duplicate CSS and no class swapping.
## HTML
```html
<section class="tr-11" aria-label="Dark mode editorial quote card demo">
  <div class="tr-11__stage">
    <div class="tr-11__switch">
      <input class="tr-11__sr" type="checkbox" id="tr-11-light">
      <label class="tr-11__lab" for="tr-11-light">
        <svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="4" fill="currentColor"/><g stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M10 1.6v2.2M10 16.2v2.2M1.6 10h2.2M16.2 10h2.2M4.1 4.1l1.6 1.6M14.3 14.3l1.6 1.6M15.9 4.1l-1.6 1.6M5.7 14.3l-1.6 1.6"/></g></svg>
        <span>Light</span>
      </label>
    </div>

    <figure class="tr-11__card">
      <p class="tr-11__kicker">Field notes</p>
      <blockquote class="tr-11__q">
        <p>The first build took nine seconds. I assumed it had failed silently and ran it again. It had not failed. That was the moment the migration stopped being a project and started being a formality.</p>
      </blockquote>
      <figcaption class="tr-11__cap">
        <img src="https://images.unsplash.com/photo-1463453091185-61582044d556?q=80&w=160&h=160&fit=crop&auto=format" alt="Portrait of Samuel Idris" width="52" height="52" loading="lazy" decoding="async">
        <span class="tr-11__id"><b>Samuel Idris</b>Principal Engineer · Ashcombe Labs</span>
        <span class="tr-11__badge">Open-source maintainer</span>
      </figcaption>
      <div class="tr-11__foot">
        <span class="tr-11__stat"><b>9s</b>cold build</span>
        <span class="tr-11__stat"><b>1.2M</b>lines migrated</span>
        <span class="tr-11__stat"><b>0</b>rollbacks</span>
      </div>
    </figure>
    <p class="tr-11__chip" aria-hidden="true">light-dark() · color-scheme · gradient border via mask-composite:exclude · :has() theme toggle</p>
  </div>
</section>
```
## CSS
```css
.tr-11,
.tr-11 *,
.tr-11 *::before,
.tr-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  color-scheme: dark;
  --tr-11-bg: light-dark(oklch(0.95 0.006 265),oklch(0.135 0.014 265));
  --tr-11-surf: light-dark(oklch(1 0 0),oklch(0.19 0.018 265));
  --tr-11-ink: light-dark(oklch(0.21 0.02 265),oklch(0.96 0.008 265));
  --tr-11-mut: light-dark(oklch(0.5 0.02 265),oklch(0.68 0.018 265));
  --tr-11-acc: light-dark(oklch(0.55 0.16 265),oklch(0.79 0.14 200));
  --tr-11-line: light-dark(oklch(0 0 0/.1),oklch(1 0 0/.11));
  background: var(--tr-11-bg);
  color: var(--tr-11-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
  transition: background .4s;
}

.tr-11:has(#tr-11-light:checked) {
  color-scheme: light;
}

.tr-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(20px,5vw,60px);
}

.tr-11__switch {
  display: flex;
  justify-content: center;
}

.tr-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.tr-11__lab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 99px;
  border: 1px solid var(--tr-11-line);
  background: var(--tr-11-surf);
  color: var(--tr-11-mut);
  font-size: 13px;
  font-weight: 580;
  cursor: pointer;
  transition: color .25s,border-color .25s,background .25s;
}

.tr-11__lab svg {
  width: 17px;
  height: 17px;
  transition: rotate .5s cubic-bezier(.16,1,.3,1);
}

.tr-11__lab:hover {
  color: var(--tr-11-ink);
  border-color: color-mix(in oklch,var(--tr-11-acc) 45%,transparent);
}

.tr-11__sr:checked+.tr-11__lab {
  color: var(--tr-11-acc);
}

.tr-11__sr:checked+.tr-11__lab svg {
  rotate: 180deg;
}

.tr-11__sr:focus-visible+.tr-11__lab {
  outline: 3px solid var(--tr-11-acc);
  outline-offset: 3px;
}

.tr-11__card {
  position: relative;
  width: min(100%,660px);
  display: grid;
  gap: 24px;
  padding: clamp(28px,4vw,44px);
  border-radius: 22px;
  background: linear-gradient(168deg,color-mix(in oklch,var(--tr-11-acc) 5%,var(--tr-11-surf)),var(--tr-11-surf) 55%);
  border: 1px solid var(--tr-11-line);
  box-shadow: 0 40px 80px -50px oklch(0 0 0/.9);
  animation: tr-11-in .8s cubic-bezier(.16,1,.3,1) both;
  transition: background .4s,border-color .4s;
}

@keyframes tr-11-in {
  from {
    opacity: 0;
    translate: 0 18px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-11__card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(180deg,color-mix(in oklch,var(--tr-11-ink) 26%,transparent),transparent 42%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.tr-11__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--tr-11-acc);
}

.tr-11__q p {
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  font-size: clamp(20px,2.9vw,28px);
  line-height: 1.52;
  letter-spacing: -.014em;
  text-wrap: pretty;
  color: color-mix(in oklch,var(--tr-11-ink) 95%,transparent);
}

.tr-11__q p::first-letter {
  font-size: 1.5em;
  line-height: 1;
  padding-inline-end: 2px;
  color: var(--tr-11-acc);
}

.tr-11__cap {
  display: flex;
  align-items: center;
  gap: 13px;
  flex-wrap: wrap;
  padding-top: 22px;
  border-top: 1px solid var(--tr-11-line);
}

.tr-11__cap img {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  box-shadow: 0 0 0 1px var(--tr-11-line);
}

.tr-11__id {
  display: grid;
  gap: 2px;
  font-size: 12.5px;
  color: var(--tr-11-mut);
}

.tr-11__id b {
  font-size: 15.5px;
  font-weight: 640;
  color: var(--tr-11-ink);
  letter-spacing: -.018em;
}

.tr-11__badge {
  margin-inline-start: auto;
  padding: 6px 12px;
  border-radius: 99px;
  border: 1px solid color-mix(in oklch,var(--tr-11-acc) 32%,transparent);
  background: color-mix(in oklch,var(--tr-11-acc) 12%,transparent);
  color: var(--tr-11-acc);
  font-size: 11.5px;
  font-weight: 620;
}

.tr-11__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 26px;
  padding-top: 20px;
  border-top: 1px solid var(--tr-11-line);
}

.tr-11__stat {
  display: grid;
  gap: 2px;
  font-size: 11.5px;
  color: var(--tr-11-mut);
  letter-spacing: .02em;
}

.tr-11__stat b {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.035em;
  color: var(--tr-11-ink);
  font-variant-numeric: tabular-nums;
}

.tr-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-11-mut);
  padding: 8px 15px;
  border: 1px solid var(--tr-11-line);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .tr-11__card {
    animation: none;
  }

  .tr-11__lab svg {
    transition: none;
  }
}
```
