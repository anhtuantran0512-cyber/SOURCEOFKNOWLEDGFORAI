---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-4-3-card-image-cover/"
title: "CSS Aspect Ratio 4 3 Card Image Cover"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "The card grid every blog, news site and docs hub ships — with every thumbnail cut to an identical 4:3 no matter what shape the CMS uploads."
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio 4 3 Card Image Cover
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-4-3-card-image-cover/

The card grid every blog, news site and docs hub ships — with every thumbnail cut to an identical 4:3 no matter what shape the CMS uploads. aspect-ratio: 4/3 sizes the box, object-fit: cover art-directs the crop, and the width/height attributes on each <img> keep the page CLS-clean while photos stream in. A magazine front page with one 16:9 lead story proves you can mix ratios in one system without a single fixed height.
## HTML
```html
<section class="car-04" aria-label="4:3 card image cover demo">
  <div class="car-04__stage" id="car04-top">
    <header class="car-04__mast">
      <p class="car-04__date">Weekend Edition · Front Page</p>
      <a class="car-04__logo" href="#car04-top">The Meridian</a>
      <nav class="car-04__nav" aria-label="Sections">
        <a href="#car04-lead">Technology</a>
        <a href="#car04-grid">Culture</a>
        <a href="#car04-grid">Climate</a>
        <a href="#car04-grid">Ideas</a>
      </nav>
    </header>
    <main class="car-04__main">
      <article class="car-04__lead" id="car04-lead">
        <a class="car-04__lead-media" href="#car04-top"><img src="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=1600&h=900&auto=format&fit=crop" width="1600" height="900" alt="City skyline at dusk" loading="eager"></a>
        <div class="car-04__lead-body">
          <p class="car-04__chip">The Lead · 16:9</p>
          <h1><a href="#car04-top">The city that rebuilt its grid around light</a></h1>
          <p class="car-04__standfirst">One slot on this page runs widescreen while every card below runs 4:3 — same two CSS properties, different numbers. The photos never know what shape they were uploaded in.</p>
          <p class="car-04__by"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt="">Daniel Reyes · 14 min read</p>
        </div>
      </article>
      <div class="car-04__grid" id="car04-grid">
        <article class="car-04__card"><a class="car-04__media" href="#car04-top"><img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?q=80&w=1200&h=900&auto=format&fit=crop" width="1200" height="900" loading="lazy" alt="Street crossing from above"><span>4:3</span></a><div><p class="car-04__chip">Culture</p><h2><a href="#car04-top">Crosswalks, drones and the choreography of a Tuesday</a></h2><p class="car-04__ex">The upload was a towering portrait shot. The card doesn't care — the box is 4:3 and cover crops the rest.</p><p class="car-04__by"><img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt="">Sofia Lindqvist · 6 min</p></div></article>
        <article class="car-04__card"><a class="car-04__media" href="#car04-top"><img src="https://images.unsplash.com/photo-1522199755839-a2bacb67c546?q=80&w=1200&h=900&auto=format&fit=crop" width="1200" height="900" loading="lazy" alt="Laptop and coffee on a desk"><span>4:3</span></a><div><p class="car-04__chip">Technology</p><h2><a href="#car04-top">Remote work's second decade starts at the kitchen table</a></h2><p class="car-04__ex">Landscape upload, portrait upload, screenshot — the grid stays perfectly rhythmic because no image chooses its own height.</p><p class="car-04__by"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt="">Marcus Bell · 9 min</p></div></article>
        <article class="car-04__card"><a class="car-04__media" href="#car04-top"><img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1200&h=900&auto=format&fit=crop" width="1200" height="900" loading="lazy" alt="Code on a laptop screen"><span>4:3</span></a><div><p class="car-04__chip">Ideas</p><h2><a href="#car04-top">Why every styleguide now starts with a ratio scale</a></h2><p class="car-04__ex">Design systems ship 1:1, 4:3 and 16:9 slots the way they ship type scales — one custom property per slot.</p><p class="car-04__by"><img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt="">Amara Chen · 7 min</p></div></article>
        <article class="car-04__card"><a class="car-04__media" href="#car04-top"><img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=1200&h=900&auto=format&fit=crop" width="1200" height="900" loading="lazy" alt="Pour-over coffee"><span>4:3</span></a><div><p class="car-04__chip">Culture</p><h2><a href="#car04-top">The slow return of the neighborhood café</a></h2><p class="car-04__ex">Object-position is the art-direction dial: this crop is biased toward the cup, not the counter.</p><p class="car-04__by"><img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt="">Owen Park · 5 min</p></div></article>
        <article class="car-04__card"><a class="car-04__media" href="#car04-top"><img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1200&h=900&auto=format&fit=crop" width="1200" height="900" loading="lazy" alt="Plated dinner"><span>4:3</span></a><div><p class="car-04__chip">Climate</p><h2><a href="#car04-top">What a dinner plate looks like at 1.5 degrees</a></h2><p class="car-04__ex">The width/height attributes on every img reserve space before pixels arrive — CSS then overrides the shape.</p><p class="car-04__by"><img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt="">June Okafor · 8 min</p></div></article>
        <article class="car-04__card"><a class="car-04__media" href="#car04-top"><img src="https://images.unsplash.com/photo-1444723121867-7a241cacace9?q=80&w=1200&h=900&auto=format&fit=crop" width="1200" height="900" loading="lazy" alt="City sunset panorama"><span>4:3</span></a><div><p class="car-04__chip">Ideas</p><h2><a href="#car04-top">Skylines are the new screensavers</a></h2><p class="car-04__ex">A panorama upload survives the square-ish crop because cover scales from the center out — no letterboxing, ever.</p><p class="car-04__by"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt="">Daniel Reyes · 4 min</p></div></article>
      </div>
    </main>
    <footer class="car-04__foot">Every thumbnail: <code>aspect-ratio:4/3</code> + <code>object-fit:cover</code> + width/height attributes for CLS. The lead swaps one number for <code>16/9</code>. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-04,
.car-04 *,
.car-04 *::before,
.car-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-04 {
  --bg: oklch(0.97 0.006 85);
  --ink: oklch(0.2 0.015 60);
  --mut: oklch(0.48 0.015 60);
  --line: oklch(0.88 0.012 80);
  --acc: oklch(0.5 0.16 25);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-04__stage {
  width: 100%;
  container: car04/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.car-04__mast {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 14px;
  padding: 16px clamp(16px,4cqi,44px);
  border-bottom: 3px double var(--ink);
}

.car-04__date {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--mut);
}

.car-04__logo {
  justify-self: center;
  font-size: clamp(22px,3.6cqi,32px);
  font-weight: 700;
  letter-spacing: -.01em;
  color: inherit;
  text-decoration: none;
}

.car-04__nav {
  justify-self: end;
  display: flex;
  gap: 2px;
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.car-04__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 11px;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  border-radius: 8px;
  transition: color .2s,background .2s;
}

.car-04__nav a:hover,
.car-04__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.92 0.01 85);
}

.car-04__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.car-04__main {
  max-width: 1140px;
  margin-inline: auto;
  padding: clamp(20px,4cqi,40px) clamp(16px,4cqi,44px);
}

.car-04__lead {
  display: grid;
  grid-template-columns: minmax(0,3fr) minmax(0,2fr);
  gap: clamp(18px,3.5cqi,36px);
  align-items: center;
  padding-bottom: clamp(22px,4cqi,40px);
  border-bottom: 1px solid var(--line);
}

.car-04__lead-media {
  display: block;
  overflow: hidden;
  border-radius: 6px;
}

.car-04__lead-media img {
  width: 100%;
  height: auto;
  aspect-ratio: 16/9;
  object-fit: cover;
  display: block;
  background: linear-gradient(130deg,oklch(0.75 0.06 60),oklch(0.6 0.08 30));
  transition: scale .6s cubic-bezier(.2,.7,.2,1);
}

.car-04__lead-media:hover img,
.car-04__lead-media:focus-visible img {
  scale: 1.04;
}

.car-04__lead-media:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.car-04__chip {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--acc);
}

.car-04__lead h1 {
  font-size: clamp(24px,3.8cqi,40px);
  line-height: 1.08;
  letter-spacing: -.015em;
  margin-top: 10px;
  text-wrap: balance;
}

.car-04__lead h1 a,
.car-04__card h2 a {
  color: inherit;
  text-decoration: none;
  transition: color .2s;
}

.car-04__lead h1 a:hover,
.car-04__lead h1 a:focus-visible,
.car-04__card h2 a:hover,
.car-04__card h2 a:focus-visible {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1.5px;
}

.car-04__lead h1 a:focus-visible,
.car-04__card h2 a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.car-04__standfirst {
  margin-top: 12px;
  font-size: 15px;
  line-height: 1.6;
  color: var(--mut);
}

.car-04__by {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 14px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12px;
  color: var(--mut);
}

.car-04__by img {
  width: 26px;
  height: auto;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
  background: oklch(0.85 0.02 60);
}

.car-04__grid {
  display: grid;
  gap: clamp(18px,3cqi,30px);
  grid-template-columns: repeat(auto-fill,minmax(min(280px,100%),1fr));
  padding-top: clamp(22px,4cqi,40px);
}

.car-04__card {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.car-04__media {
  position: relative;
  display: block;
  overflow: hidden;
  border-radius: 6px;
}

.car-04__media img {
  width: 100%;
  height: auto;
  aspect-ratio: 4/3;
  object-fit: cover;
  display: block;
  background: linear-gradient(130deg,oklch(0.8 0.04 80),oklch(0.68 0.05 40));
  transition: scale .55s cubic-bezier(.2,.7,.2,1);
}

.car-04__media:hover img,
.car-04__media:focus-visible img {
  scale: 1.05;
}

.car-04__media:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.car-04__media span {
  position: absolute;
  right: 10px;
  bottom: 8px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .05em;
  color: oklch(0.98 0 0);
  background: oklch(0.2 0.02 60/.65);
  padding: 3px 7px;
  border-radius: 6px;
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
}

.car-04__card > div {
  padding-top: 12px;
}

.car-04__card h2 {
  font-size: 19px;
  line-height: 1.22;
  letter-spacing: -.01em;
  margin-top: 8px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.car-04__ex {
  margin-top: 8px;
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--mut);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.car-04__foot {
  max-width: 1140px;
  margin-inline: auto;
  padding: 20px clamp(16px,4cqi,44px) 36px;
  border-top: 1px solid var(--line);
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
}

.car-04__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.91 0.012 85);
  padding: 1px 5px;
  border-radius: 5px;
  color: oklch(0.4 0.12 25);
}

@container car04 (width < 780px) {
  .car-04__lead {
    grid-template-columns: 1fr;
  }

  .car-04__mast {
    grid-template-columns: 1fr auto;
    grid-template-rows: auto auto;
  }

  .car-04__date {
    display: none;
  }

  .car-04__logo {
    justify-self: start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-04 * {
    transition-duration: .01ms !important;
  }
}
```
