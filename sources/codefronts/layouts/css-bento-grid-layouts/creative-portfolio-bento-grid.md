---
source: "codefronts"
url: "https://codefronts.com/layouts/css-bento-grid-layouts/creative-portfolio-bento-grid/"
title: "Creative Portfolio Bento Grid"
section: "layouts"
category: "css-bento-grid-layouts"
category_name: "CSS Bento Grid Layouts"
description: "A bento grid portfolio template that acts as a one-screen resume for designers and frontend engineers in competitive job markets: a profile card with photo…"
has_js: "true"
---

Here's a working CSS Bento Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Creative Portfolio Bento Grid
Source: https://codefronts.com/layouts/css-bento-grid-layouts/creative-portfolio-bento-grid/

A bento grid portfolio template that acts as a one-screen resume for designers and frontend engineers in competitive job markets: a profile card with photo and bio, a wide case-studies block with slick hover states, a live clock + location widget, a social links square and a skills marquee strip. Variant B is a black-and-white neo-brutalist take with hard shadows and hover inversion.
## HTML
```html
<div class="bgl-04-group">
<section class="bgl-04a" aria-labelledby="bgl-04a-h">
  <div class="bgl-04a__grid">
    <article class="bgl-04a__card bgl-04a__profile">
      <img class="bgl-04a__pic" src="https://picsum.photos/seed/bglface/240/240" alt="Portrait of Jordan Vale" loading="lazy">
      <h2 class="bgl-04a__name" id="bgl-04a-h">Jordan Vale</h2>
      <p class="bgl-04a__bio">Product designer &amp; frontend engineer. I design systems, then ship them.</p>
    </article>
    <article class="bgl-04a__card bgl-04a__cases">
      <h3 class="bgl-04a__t">Selected work</h3>
      <ul class="bgl-04a__ul">
        <li><a href="#"><span class="bgl-04a__case">Atlas &mdash; design system for 40 teams</span><em>2025</em><b aria-hidden="true">&rarr;</b></a></li>
        <li><a href="#"><span class="bgl-04a__case">Pulse &mdash; realtime analytics app</span><em>2024</em><b aria-hidden="true">&rarr;</b></a></li>
        <li><a href="#"><span class="bgl-04a__case">Drift &mdash; onboarding that converts 2&times;</span><em>2024</em><b aria-hidden="true">&rarr;</b></a></li>
      </ul>
    </article>
    <article class="bgl-04a__card bgl-04a__clockcard">
      <p class="bgl-04a__clock" id="bgl-04a-clock">09:41:00</p>
      <p class="bgl-04a__loc">San Francisco, CA &mdash; open to remote</p>
    </article>
    <article class="bgl-04a__card bgl-04a__social">
      <h3 class="bgl-04a__t">Elsewhere</h3>
      <div class="bgl-04a__links">
        <a href="#" aria-label="GitHub profile">Gh</a><a href="#" aria-label="Dribbble profile">Dr</a><a href="#" aria-label="LinkedIn profile">In</a><a href="#" aria-label="Email me">@</a>
      </div>
    </article>
    <article class="bgl-04a__card bgl-04a__marquee" aria-label="Skills">
      <div class="bgl-04a__track"><span>Design systems &bull; React &bull; CSS architecture &bull; Prototyping &bull; Motion &bull; Accessibility &bull; Figma &bull; TypeScript &bull;&nbsp;</span><span aria-hidden="true">Design systems &bull; React &bull; CSS architecture &bull; Prototyping &bull; Motion &bull; Accessibility &bull; Figma &bull; TypeScript &bull;&nbsp;</span></div>
    </article>
  </div>
</section>
<section class="bgl-04b" aria-labelledby="bgl-04b-h">
  <div class="bgl-04b__grid">
    <article class="bgl-04b__card bgl-04b__intro">
      <p class="bgl-04b__idx">01</p>
      <h2 class="bgl-04b__name" id="bgl-04b-h">SAM&nbsp;OKAFOR</h2>
      <p class="bgl-04b__role">Creative developer. Berlin. Available Q4.</p>
    </article>
    <article class="bgl-04b__card"><p class="bgl-04b__idx">02</p><a class="bgl-04b__work" href="#">KINETIC TYPE ENGINE<b aria-hidden="true">&nearr;</b></a></article>
    <article class="bgl-04b__card"><p class="bgl-04b__idx">03</p><a class="bgl-04b__work" href="#">WEBGL STOREFRONT<b aria-hidden="true">&nearr;</b></a></article>
    <article class="bgl-04b__card"><p class="bgl-04b__idx">04</p><a class="bgl-04b__work" href="#">GENERATIVE ID SYSTEM<b aria-hidden="true">&nearr;</b></a></article>
    <article class="bgl-04b__card bgl-04b__contact"><p class="bgl-04b__idx">05</p><a class="bgl-04b__mail" href="mailto:[email protected]">[email protected]</a></article>
  </div>
</section>
</div>
```
## CSS
```css
.bgl-04-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.bgl-04-group > section {
  flex: 1 1 480px;
  min-width: 320px;
}

.bgl-04a,
.bgl-04a *,
.bgl-04a *::before,
.bgl-04a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-04a {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.68 0.18 35);
  --gap: 16px;
  --radius: 20px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 24px;
  background: #14110e;
  color: #f3ede6;
}

.bgl-04a__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(120px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-04a__card {
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  padding: 26px;
  border-radius: var(--radius);
  background: #1d1915;
  border: 1px solid rgba(243,237,230,.08);
  transition: transform .3s,border-color .3s;
}

.bgl-04a__card:hover {
  transform: translateY(-3px);
  border-color: color-mix(in oklab,var(--accent) 40%,transparent);
}

.bgl-04a__profile {
  grid-row: span 2;
  align-items: flex-start;
}

.bgl-04a__pic {
  width: 88px;
  height: 88px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid color-mix(in oklab,var(--accent) 60%,transparent);
}

.bgl-04a__name {
  font-size: clamp(24px,2.8cqw,32px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.bgl-04a__bio {
  font-size: 14.5px;
  line-height: 1.6;
  color: rgba(243,237,230,.6);
  text-wrap: pretty;
}

.bgl-04a__cases {
  grid-column: span 8;
  grid-row: span 2;
  justify-content: flex-start;
}

.bgl-04a__t {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(243,237,230,.45);
}

.bgl-04a__ul {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.bgl-04a__ul a {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 4px;
  color: inherit;
  text-decoration: none;
  border-bottom: 1px solid rgba(243,237,230,.08);
  font-size: 17px;
  font-weight: 600;
}

.bgl-04a__ul li:last-child a {
  border-bottom: none;
}

.bgl-04a__case {
  background: linear-gradient(var(--accent),var(--accent)) 0 100%/0 2px no-repeat;
  transition: background-size .35s;
}

.bgl-04a__ul a:hover .bgl-04a__case,
.bgl-04a__ul a:focus-visible .bgl-04a__case {
  background-size: 100% 2px;
}

.bgl-04a__ul em {
  margin-left: auto;
  font-style: normal;
  font-size: 13px;
  color: rgba(243,237,230,.4);
}

.bgl-04a__ul b {
  font-weight: 400;
  color: var(--accent);
  transform: translateX(-6px);
  opacity: 0;
  transition: transform .3s,opacity .3s;
}

.bgl-04a__ul a:hover b,
.bgl-04a__ul a:focus-visible b {
  transform: translateX(0);
  opacity: 1;
}

.bgl-04a__ul a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 6px;
}

.bgl-04a__clock {
  font-size: clamp(28px,3.2cqw,36px);
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  letter-spacing: .02em;
}

.bgl-04a__loc {
  font-size: 13px;
  color: rgba(243,237,230,.5);
}

.bgl-04a__links {
  display: flex;
  gap: 10px;
}

.bgl-04a__links a {
  display: grid;
  place-items: center;
  width: 48px;
  height: 48px;
  border-radius: 14px;
  font-size: 14px;
  font-weight: 800;
  color: #f3ede6;
  text-decoration: none;
  background: rgba(243,237,230,.07);
  border: 1px solid rgba(243,237,230,.1);
  transition: transform .25s,background .25s,color .25s;
}

.bgl-04a__links a:hover,
.bgl-04a__links a:focus-visible {
  transform: translateY(-3px);
  background: var(--accent);
  color: #14110e;
}

.bgl-04a__links a:focus-visible {
  outline: 3px solid #f3ede6;
  outline-offset: 2px;
}

.bgl-04a__marquee {
  grid-column: span 12;
  overflow: hidden;
  padding: 20px 0;
  justify-content: center;
}

.bgl-04a__track {
  display: flex;
  white-space: nowrap;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: rgba(243,237,230,.45);
  animation: bgl-04a-slide 18s linear infinite;
}

.bgl-04a__marquee:hover .bgl-04a__track {
  animation-play-state: paused;
}

@keyframes bgl-04a-slide {
  to {
    transform: translateX(-50%);
  }
}

@container (max-width: 880px) {
  .bgl-04a__cases {
    grid-column: span 12;
  }

  .bgl-04a__card {
    grid-column: span 6;
  }

  .bgl-04a__cases,
    .bgl-04a__marquee {
    grid-column: span 12;
  }
}

@container (max-width: 560px) {
  .bgl-04a__card,
    .bgl-04a__cases,
    .bgl-04a__marquee {
    grid-column: span 12;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-04a__card,
    .bgl-04a__links a {
    transition: none;
  }

  .bgl-04a__track {
    animation: none;
  }

  .bgl-04a__ul b {
    transition: none;
    opacity: 1;
    transform: none;
  }
}

.bgl-04b,
.bgl-04b *,
.bgl-04b *::before,
.bgl-04b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-04b {
  width: 100%;
  min-height: 100vh;
  --shift: 6px;
  --gap: 16px;
  --radius: 0px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 24px;
  background: #f2f0eb;
  color: #111;
}

.bgl-04b__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(150px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-04b__card {
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 16px;
  padding: 24px;
  border-radius: var(--radius);
  background: #fff;
  border: 3px solid #111;
  box-shadow: var(--shift) var(--shift) 0 #111;
  transition: transform .15s,box-shadow .15s;
}

.bgl-04b__card:hover {
  transform: translate(var(--shift),var(--shift));
  box-shadow: 0 0 0 #111;
}

.bgl-04b__intro {
  grid-column: span 8;
}

.bgl-04b__idx {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .1em;
}

.bgl-04b__name {
  font-size: clamp(36px,5.5cqw,64px);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: .95;
}

.bgl-04b__role {
  font-size: 15px;
  font-weight: 600;
}

.bgl-04b__work {
  display: flex;
  align-items: baseline;
  gap: 10px;
  font-size: clamp(17px,1.9cqw,21px);
  font-weight: 900;
  letter-spacing: -.01em;
  color: #111;
  text-decoration: none;
  line-height: 1.2;
}

.bgl-04b__work b {
  font-weight: 900;
  transition: transform .2s;
}

.bgl-04b__work:hover b,
.bgl-04b__work:focus-visible b {
  transform: translate(3px,-3px);
}

.bgl-04b__work:focus-visible,
.bgl-04b__mail:focus-visible {
  outline: 3px dashed #111;
  outline-offset: 4px;
}

.bgl-04b__contact {
  background: #111;
  color: #f2f0eb;
  box-shadow: var(--shift) var(--shift) 0 rgba(17,17,17,.35);
}

.bgl-04b__contact .bgl-04b__idx {
  color: #f2f0eb;
}

.bgl-04b__mail {
  font-size: clamp(17px,2cqw,22px);
  font-weight: 900;
  color: #f2f0eb;
  text-decoration: underline;
  text-decoration-thickness: 3px;
  text-underline-offset: 5px;
}

@container (max-width: 880px) {
  .bgl-04b__intro {
    grid-column: span 12;
  }

  .bgl-04b__card {
    grid-column: span 6;
  }

  .bgl-04b__intro {
    grid-column: span 12;
  }
}

@container (max-width: 560px) {
  .bgl-04b__card,
    .bgl-04b__intro {
    grid-column: span 12;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-04b__card,
    .bgl-04b__work b {
    transition: none;
  }

  .bgl-04b__card:hover {
    transform: none;
    box-shadow: var(--shift) var(--shift) 0 #111;
  }
}
```

## JavaScript
```js
(() => {
  const el = document.querySelector('#bgl-04a-clock'); if (!el) return;
  const tick = () => { el.textContent = new Date().toLocaleTimeString('en-US', { hour12: false, timeZone: 'America/Los_Angeles' }); };
  tick(); setInterval(tick, 1000);
})();

/* No JavaScript — hard 6px box-shadow offsets; on hover each card translates by exactly the shadow offset so it reads as physically pressed flat. */
```
