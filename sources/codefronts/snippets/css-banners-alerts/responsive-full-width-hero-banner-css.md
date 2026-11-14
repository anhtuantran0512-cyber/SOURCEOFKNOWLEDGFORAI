---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/responsive-full-width-hero-banner-css/"
title: "Full Width Hero Banner"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "A hero that holds up on a 320px phone and a 5K display from the same markup: <picture> art direction so the crop changes rather than shrinks, a two-stop…"
has_js: "false"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full Width Hero Banner
Source: https://codefronts.com/snippets/css-banners-alerts/responsive-full-width-hero-banner-css/

A hero that holds up on a 320px phone and a 5K display from the same markup: <picture> art direction so the crop changes rather than shrinks, a two-stop scrim tuned for text contrast instead of decoration, fluid type on cqi units, and a scroll-driven parallax that is declared, not scripted.
## HTML
```html
<div class="ba-18">
  <section class="ba-18__hero" aria-labelledby="ba-18-h">
    <picture class="ba-18__media" aria-hidden="true">
      <source media="(max-width: 40rem)" srcset="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=900&amp;h=1200&amp;q=70&amp;auto=format&amp;fit=crop">
      <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=2000&amp;q=72&amp;auto=format&amp;fit=crop" alt="" width="2000" height="1125" loading="eager" decoding="async" fetchpriority="high">
    </picture>
    <span class="ba-18__scrim" aria-hidden="true"></span>

    <div class="ba-18__inner">
      <p class="ba-18__eyebrow">Season 04 · Coastal range</p>
      <h1 class="ba-18__h" id="ba-18-h">Built for the last hour of light</h1>
      <p class="ba-18__lede">Shell, mid-layer and pack, tested for eleven months on the west coast path. One system, three temperatures, no compromises you can feel at hour nine.</p>

      <div class="ba-18__cta">
        <a class="ba-18__primary" href="#ba-18-h">Shop the range<svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M4 10h11m-4.4-4.4L15 10l-4.4 4.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a class="ba-18__secondary" href="#ba-18-h">Watch the field test <span>2:14</span></a>
      </div>

      <ul class="ba-18__stats">
        <li><b>11</b><span>months of field testing</span></li>
        <li><b>340g</b><span>shell weight, size M</span></li>
        <li><b>92%</b><span>recycled face fabric</span></li>
      </ul>
    </div>

  </section>


</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=Newsreader:opsz,[email protected],300;6..72,400&display=swap');

.ba-18 {
  --hero-h: 100svh;
  --scrim-strength: 88%;
  --ink: #08100c;
  --paper: #f6f8f5;
  --muted: #b9c4bd;
  --acc: #7ce8a4;
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--ink);
  color: var(--paper);
  font-family: var(--sans);
}

.ba-18 *,
.ba-18 *::before,
.ba-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-18 {
    --ink: oklch(16% .022 155);
    --paper: oklch(97% .008 150);
    --muted: oklch(80% .018 155);
    --acc: oklch(86% .15 155);
  }
}

.ba-18__hero {
  container-type: inline-size;
  position: relative;
  min-height: var(--hero-h);
  display: grid;
  align-items: end;
  overflow: clip;
  isolation: isolate;
}

.ba-18__media {
  position: absolute;
  inset: 0;
  z-index: 0;
  display: block;
  overflow: hidden;
}

.ba-18__media img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 40%;
  background: color-mix(in oklab,var(--ink) 70%,black);
}

.ba-18__scrim {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  background: linear-gradient(to top,
        color-mix(in oklab, var(--ink) var(--scrim-strength), transparent) 0 26%,
        color-mix(in oklab, var(--ink) 42%, transparent) 60%,
        color-mix(in oklab, var(--ink) 12%, transparent) 100%), linear-gradient(to right, color-mix(in oklab, var(--ink) 40%, transparent), transparent 62%);
}

@supports (animation-timeline: view()) {
  .ba-18__media img {
    animation: ba-18-parallax linear both;
    animation-timeline: view();
    animation-range: entry 0% exit 100%;
  }

  @keyframes ba-18-parallax {
    from {
      translate: 0 -3%;
      scale: 1.06;
    }

    to {
      translate: 0 3%;
      scale: 1.12;
    }
  }
}

.ba-18__inner {
  position: relative;
  z-index: 2;
  display: grid;
  gap: clamp(.85rem,2cqi,1.35rem);
  align-content: end;
  max-width: min(72rem,100%);
  margin-inline: auto;
  width: 100%;
  padding: clamp(3rem,12cqi,7rem) clamp(1.25rem,5cqi,4rem) clamp(3.5rem,9cqi,5rem);
}

.ba-18__eyebrow {
  margin: 0;
  font-size: clamp(.6875rem,1.1cqi,.8125rem);
  font-weight: 600;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--acc);
}

.ba-18__h {
  margin: 0;
  font-size: clamp(2.25rem,9cqi,6rem);
  font-weight: 600;
  line-height: .94;
  letter-spacing: -.05em;
  text-wrap: balance;
  max-width: 22ch;
  text-shadow: 0 .15rem 2.5rem color-mix(in oklab,var(--ink) 55%,transparent);
}

.ba-18__lede {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(1rem,2cqi,1.375rem);
  font-weight: 300;
  line-height: 1.55;
  color: var(--paper);
  opacity: .88;
  max-width: 52ch;
  text-wrap: pretty;
}

.ba-18__cta {
  display: flex;
  flex-wrap: wrap;
  gap: .7rem;
  align-items: center;
  margin-block-start: .35rem;
}

.ba-18__primary {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-height: 3.25rem;
  padding: .95rem 1.6rem;
  border-radius: 999px;
  text-decoration: none;
  background: var(--paper);
  color: var(--ink);
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.015em;
  transition: translate .22s cubic-bezier(.16,1,.3,1), box-shadow .25s ease, background .2s ease;
}

.ba-18__primary svg {
  width: 1.1rem;
  height: 1.1rem;
  transition: translate .25s cubic-bezier(.16,1,.3,1);
}

.ba-18__primary:hover {
  translate: 0 -2px;
  background: var(--acc);
  box-shadow: 0 1.25rem 2.5rem -1.25rem color-mix(in oklab,var(--acc) 65%,transparent);
}

.ba-18__primary:hover svg {
  translate: .25rem 0;
}

.ba-18__secondary {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-height: 3.25rem;
  padding: .95rem 1.35rem;
  border-radius: 999px;
  text-decoration: none;
  color: var(--paper);
  border: 1px solid color-mix(in oklab,var(--paper) 38%,transparent);
  font-size: .9375rem;
  font-weight: 500;
  transition: background .2s ease, border-color .2s ease;
}

.ba-18__secondary span {
  font-variant-numeric: tabular-nums;
  opacity: .65;
  font-size: .8125rem;
}

.ba-18__secondary:hover {
  background: color-mix(in oklab,var(--paper) 14%,transparent);
  border-color: var(--paper);
}

.ba-18__stats {
  margin: clamp(.75rem,2cqi,1.5rem) 0 0;
  padding: clamp(.85rem,2cqi,1.25rem) 0 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,9rem),1fr));
  gap: 1rem;
  border-block-start: 1px solid color-mix(in oklab,var(--paper) 22%,transparent);
}

.ba-18__stats b {
  display: block;
  font-size: clamp(1.25rem,3cqi,1.875rem);
  font-weight: 600;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
}

.ba-18__stats span {
  font-size: .75rem;
  color: var(--muted);
  line-height: 1.4;
}

.ba-18 a {
  color: var(--acc);
}

.ba-18 a:hover {
  color: color-mix(in oklab,var(--acc) 75%,var(--paper));
}

.ba-18 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ba-18 * {
    animation: none !important;
    transition: none !important;
  }

  .ba-18__media img {
    translate: 0 0;
    scale: 1;
  }
}

@media (forced-colors: active) {
  .ba-18__scrim {
    display: none;
  }

  .ba-18__primary {
    background: Highlight;
    color: HighlightText;
  }
}
```
