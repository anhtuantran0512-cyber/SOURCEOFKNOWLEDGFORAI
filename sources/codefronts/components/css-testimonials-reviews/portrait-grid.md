---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/portrait-grid/"
title: "Staggered Portrait Testimonial Grid"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Faces first."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Staggered Portrait Testimonial Grid
Source: https://codefronts.com/components/css-testimonials-reviews/portrait-grid/

Faces first. When the endorsement is the person — founders, influencers, practitioners — this staggered portrait grid outperforms any card layout. Alternate columns are offset vertically with an nth-child rule, each portrait carries its quote in an overlay that lifts on hover, and the whole grid reveals in a diagonal cascade.
## HTML
```html
<section class="tr-25" aria-label="Staggered portrait testimonial grid demo">
  <div class="tr-25__stage">
    <header class="tr-25__head">
      <p class="tr-25__eyebrow">The people, not the logos</p>
      <h2 class="tr-25__title">Eight founders. One sentence each.</h2>
    </header>

    <div class="tr-25__grid">
      <figure class="tr-25__item" style="--tr-25-i:0" tabindex="0">
        <img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=600&auto=format&fit=crop" alt="Portrait of Alessandra Rossi" width="440" height="586" loading="lazy" decoding="async">
        <figcaption class="tr-25__cap"><blockquote>“Nineteen years of records moved in a weekend.”</blockquote><span><b>Alessandra Rossi</b>Vaultline Financial</span></figcaption>
      </figure>
      <figure class="tr-25__item" style="--tr-25-i:1" tabindex="0">
        <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=600&auto=format&fit=crop" alt="Portrait of Marcus Yeung" width="440" height="586" loading="lazy" decoding="async">
        <figcaption class="tr-25__cap"><blockquote>“Compliance stopped filing tickets and started filing praise.”</blockquote><span><b>Marcus Yeung</b>Halden Group</span></figcaption>
      </figure>
      <figure class="tr-25__item" style="--tr-25-i:2" tabindex="0">
        <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=600&auto=format&fit=crop" alt="Portrait of Grace Whitlock" width="440" height="586" loading="lazy" decoding="async">
        <figcaption class="tr-25__cap"><blockquote>“94% of merged PRs now reference a token.”</blockquote><span><b>Grace Whitlock</b>Auryn</span></figcaption>
      </figure>
      <figure class="tr-25__item" style="--tr-25-i:3" tabindex="0">
        <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=600&auto=format&fit=crop" alt="Portrait of Dan Reyes" width="440" height="586" loading="lazy" decoding="async">
        <figcaption class="tr-25__cap"><blockquote>“Two data centres, four time zones, zero rollbacks.”</blockquote><span><b>Dan Reyes</b>Portside</span></figcaption>
      </figure>
      <figure class="tr-25__item" style="--tr-25-i:4" tabindex="0">
        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=600&auto=format&fit=crop" alt="Portrait of Hana Sørensen" width="440" height="586" loading="lazy" decoding="async">
        <figcaption class="tr-25__cap"><blockquote>“Asked on Friday. Shipped Tuesday. With docs.”</blockquote><span><b>Hana Sørensen</b>Blomst</span></figcaption>
      </figure>
      <figure class="tr-25__item" style="--tr-25-i:5" tabindex="0">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=600&auto=format&fit=crop" alt="Portrait of Nia Osei" width="440" height="586" loading="lazy" decoding="async">
        <figcaption class="tr-25__cap"><blockquote>“Onboarding took an afternoon, not a quarter.”</blockquote><span><b>Nia Osei</b>Fieldwork</span></figcaption>
      </figure>
      <figure class="tr-25__item" style="--tr-25-i:6" tabindex="0">
        <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=600&auto=format&fit=crop" alt="Portrait of Erin McAllister" width="440" height="586" loading="lazy" decoding="async">
        <figcaption class="tr-25__cap"><blockquote>“Renewal was a fifteen-minute conversation.”</blockquote><span><b>Erin McAllister</b>Larkfield Health</span></figcaption>
      </figure>
      <figure class="tr-25__item" style="--tr-25-i:7" tabindex="0">
        <img src="https://images.unsplash.com/photo-1463453091185-61582044d556?q=80&w=600&auto=format&fit=crop" alt="Portrait of Samuel Idris" width="440" height="586" loading="lazy" decoding="async">
        <figcaption class="tr-25__cap"><blockquote>“The first build took nine seconds. I ran it twice.”</blockquote><span><b>Samuel Idris</b>Ashcombe Labs</span></figcaption>
      </figure>
    </div>
    <p class="tr-25__chip" aria-hidden="true">nth-child vertical offsets · aspect-ratio 3/4 portraits · scrim overlay · diagonal --i cascade</p>
  </div>
</section>
```
## CSS
```css
.tr-25,
.tr-25 *,
.tr-25 *::before,
.tr-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-25-bg: oklch(0.955 0.008 60);
  --tr-25-ink: oklch(0.2 0.014 55);
  --tr-25-mut: oklch(0.52 0.014 55);
  --tr-25-acc: oklch(0.6 0.16 35);
  background: var(--tr-25-bg);
  color: var(--tr-25-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-25__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(22px,3.4vw,36px);
  padding: clamp(20px,4vw,58px);
}

.tr-25__head {
  text-align: center;
  display: grid;
  gap: 9px;
}

.tr-25__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--tr-25-acc);
}

.tr-25__title {
  font-size: clamp(24px,4vw,42px);
  font-weight: 670;
  letter-spacing: -.04em;
  line-height: 1.08;
  text-wrap: balance;
}

.tr-25__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: clamp(10px,1.5vw,18px);
  width: min(100%,1160px);
  padding-block-end: 52px;
}

.tr-25__item {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  background: linear-gradient(150deg,oklch(0.85 0.03 50),oklch(0.72 0.05 30));
  animation: tr-25-in .8s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--tr-25-i,0)*70ms);
  cursor: pointer;
}

.tr-25__item:nth-child(even) {
  margin-block-start: 46px;
}

.tr-25__item:nth-child(4n+3) {
  margin-block-start: 24px;
}

@keyframes tr-25-in {
  from {
    opacity: 0;
    translate: 0 22px;
    scale: .97;
  }

  to {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }
}

.tr-25__item img {
  width: 100%;
  height: auto;
  aspect-ratio: 3/4;
  object-fit: cover;
  display: block;
  transition: scale .7s cubic-bezier(.16,1,.3,1),filter .5s;
}

.tr-25__item:hover img,
.tr-25__item:focus-visible img {
  scale: 1.06;
}

.tr-25__item:focus-visible {
  outline: 3px solid var(--tr-25-acc);
  outline-offset: 3px;
}

.tr-25__cap {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  display: grid;
  gap: 9px;
  padding: clamp(14px,1.6vw,20px);
  color: oklch(0.99 0 0);
  background: linear-gradient(transparent,oklch(0.14 0.02 40/.5) 34%,oklch(0.12 0.02 40/.92));
  translate: 0 12px;
  opacity: .86;
  transition: translate .45s cubic-bezier(.16,1,.3,1),opacity .45s;
}

.tr-25__item:hover .tr-25__cap,
.tr-25__item:focus-within .tr-25__cap {
  translate: 0 0;
  opacity: 1;
}

.tr-25__cap blockquote {
  font-size: clamp(13px,1.15vw,15px);
  line-height: 1.42;
  letter-spacing: -.014em;
  font-weight: 550;
  text-wrap: pretty;
}

.tr-25__cap span {
  display: grid;
  font-size: 10.5px;
  line-height: 1.3;
  color: oklch(0.86 0.01 50);
  padding-top: 9px;
  border-top: 1px solid oklch(1 0 0/.22);
}

.tr-25__cap b {
  font-size: 12.5px;
  font-weight: 660;
  color: oklch(0.99 0 0);
  letter-spacing: -.01em;
}

.tr-25__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-25-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.5);
}

@media (max-width: 960px) {
  .tr-25__grid {
    grid-template-columns: repeat(3,1fr);
  }

  .tr-25__item:nth-child(4n+3) {
    margin-block-start: 0;
  }

  .tr-25__item:nth-child(even) {
    margin-block-start: 34px;
  }
}

@media (max-width: 620px) {
  .tr-25__grid {
    grid-template-columns: repeat(2,1fr);
    padding-block-end: 0;
  }

  .tr-25__item:nth-child(even),
    .tr-25__item:nth-child(4n+3) {
    margin-block-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tr-25__item {
    animation: none;
  }

  .tr-25__item img,
    .tr-25__cap {
    transition: none;
  }
}
```
