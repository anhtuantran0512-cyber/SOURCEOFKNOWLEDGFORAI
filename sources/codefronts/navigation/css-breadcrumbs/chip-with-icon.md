---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/chip-with-icon/"
title: "Airbnb-Style Filter Chip Breadcrumb Navigation with Icons"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "Airbnb-style breadcrumb that pairs the category path with a row of removable filter chips — each chip carries an icon, a label, and a hoverable X — the exact…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Airbnb-Style Filter Chip Breadcrumb Navigation with Icons
Source: https://codefronts.com/navigation/css-breadcrumbs/chip-with-icon/

Airbnb-style breadcrumb that pairs the category path with a row of removable filter chips — each chip carries an icon, a label, and a hoverable X — the exact pattern travel and marketplace sites use to show active filters above listings.
## HTML
```html
<section class="bc-20" aria-label="Airbnb-style filter chip breadcrumb demo">
      <nav class="bc-20__nav" aria-label="Breadcrumb and active filters">
        <ol class="bc-20__crumbs">
          <li><a href="#">Stays</a></li>
          <li><a href="#">Paris</a></li>
          <li><a aria-current="page" href="#">Le Marais</a></li>
        </ol>
        <ul class="bc-20__filters" aria-label="Active filters">
          <li>
            <button type="button" class="bc-20__chip" aria-label="Remove Dec 15-22 filter">
              <svg class="bc-20__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
              <span>Dec 15-22</span>
              <svg class="bc-20__x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>
            </button>
          </li>
          <li>
            <button type="button" class="bc-20__chip" aria-label="Remove 2 guests filter">
              <svg class="bc-20__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              <span>2 guests</span>
              <svg class="bc-20__x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>
            </button>
          </li>
          <li>
            <button type="button" class="bc-20__chip" aria-label="Remove under $200 per night filter">
              <svg class="bc-20__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
              <span>Under $200/night</span>
              <svg class="bc-20__x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>
            </button>
          </li>
          <li>
            <button type="button" class="bc-20__chip" aria-label="Remove Pool amenity filter">
              <svg class="bc-20__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 20c1.5 0 1.5-1 3-1s1.5 1 3 1 1.5-1 3-1 1.5 1 3 1 1.5-1 3-1 1.5 1 3 1"/><path d="M2 16c1.5 0 1.5-1 3-1s1.5 1 3 1 1.5-1 3-1 1.5 1 3 1 1.5-1 3-1 1.5 1 3 1"/><path d="M7 14V5a2 2 0 0 1 2-2h1M17 14V5a2 2 0 0 0-2-2h-1"/></svg>
              <span>Pool</span>
              <svg class="bc-20__x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>
            </button>
          </li>
        </ul>
      </nav>
    </section>
```
## CSS
```css
.bc-20 {
  --bc-20-bg: oklch(98.6% 0.008 60);
  --bc-20-surface: oklch(100% 0 0);
  --bc-20-ink: oklch(24% 0.02 60);
  --bc-20-muted: oklch(52% 0.015 60);
  --bc-20-border: oklch(90% 0.012 60);
  --bc-20-accent: oklch(63% 0.19 25);
  --bc-20-focus: oklch(55% 0.15 250);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  display: grid;
  place-items: start center;
  padding: clamp(1.5rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem);
  background: radial-gradient(1200px 500px at 12% -10%, oklch(96% 0.03 30 / .55), transparent 60%), radial-gradient(900px 400px at 100% 0%, oklch(96% 0.025 220 / .35), transparent 60%), var(--bc-20-bg);
  color: var(--bc-20-ink);
  font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  place-items: center;
}

@media (prefers-color-scheme: dark) {
  .bc-20 {
    --bc-20-bg: oklch(18% 0.015 260);
    --bc-20-surface: oklch(22% 0.018 260);
    --bc-20-ink: oklch(96% 0.01 60);
    --bc-20-muted: oklch(72% 0.015 60);
    --bc-20-border: oklch(30% 0.015 260);
    --bc-20-accent: oklch(72% 0.17 25);
    --bc-20-focus: oklch(78% 0.13 220);
  }
}

.bc-20 .bc-20__nav {
  container-type: inline-size;
  container-name: bc34bar;
  width: min(100%, 1080px);
  background: var(--bc-20-surface);
  border: 1px solid var(--bc-20-border);
  border-radius: 999px;
  padding: .55rem .8rem .55rem 1.25rem;
  box-shadow: 0 1px 0 oklch(100% 0 0 / .6) inset, 0 10px 30px -18px oklch(20% 0.05 60 / .25), 0 2px 6px -3px oklch(20% 0.05 60 / .12);
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.bc-20 .bc-20__crumbs {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: .1rem .35rem;
  font-size: .95rem;
  font-weight: 500;
  min-height: 44px;
}

.bc-20 .bc-20__crumbs li {
  display: inline-flex;
  align-items: center;
  color: var(--bc-20-muted);
}

.bc-20 .bc-20__crumbs li + li::before {
  content: "";
  width: 6px;
  height: 6px;
  margin: 0 .55rem 0 .2rem;
  border-top: 1.5px solid currentColor;
  border-right: 1.5px solid currentColor;
  transform: rotate(45deg);
  opacity: .55;
}

.bc-20 .bc-20__crumbs a {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 .25rem;
  color: var(--bc-20-muted);
  text-decoration: none;
  border-radius: 8px;
  transition: color .18s ease;
}

.bc-20 .bc-20__crumbs a:hover {
  color: var(--bc-20-ink);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1.5px;
}

.bc-20 .bc-20__crumbs a[aria-current="page"] {
  color: var(--bc-20-ink);
  font-weight: 600;
}

.bc-20 .bc-20__crumbs a:focus-visible {
  outline: 2px solid var(--bc-20-focus);
  outline-offset: 3px;
}

.bc-20 .bc-20__filters {
  list-style: none;
  margin: 0 0 0 auto;
  padding: 0;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: .4rem;
}

.bc-20 .bc-20__chip {
  appearance: none;
  -webkit-appearance: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-height: 44px;
  padding: .45rem .75rem .45rem .7rem;
  border-radius: 999px;
  border: 1px solid var(--bc-20-border);
  background: var(--bc-20-surface);
  color: var(--bc-20-ink);
  font: inherit;
  font-size: .875rem;
  font-weight: 500;
  line-height: 1;
  white-space: nowrap;
  transition: transform .2s ease, border-color .2s ease, box-shadow .2s ease, background .2s ease;
}

.bc-20 .bc-20__chip .bc-20__icon {
  width: 16px;
  height: 16px;
  color: var(--bc-20-muted);
  flex: none;
  transition: color .2s ease;
}

.bc-20 .bc-20__chip .bc-20__x {
  width: 14px;
  height: 14px;
  margin-left: .15rem;
  color: color-mix(in oklch, var(--bc-20-muted) 65%, transparent);
  flex: none;
  transition: color .2s ease, transform .2s ease;
}

.bc-20 .bc-20__chip:hover {
  border-color: color-mix(in oklch, var(--bc-20-accent) 40%, var(--bc-20-border));
  background: color-mix(in oklch, var(--bc-20-accent) 6%, var(--bc-20-surface));
  transform: translateY(-1px);
  box-shadow: 0 6px 14px -8px color-mix(in oklch, var(--bc-20-accent) 55%, transparent);
}

.bc-20 .bc-20__chip:hover .bc-20__icon {
  color: var(--bc-20-ink);
}

.bc-20 .bc-20__chip:hover .bc-20__x {
  color: var(--bc-20-accent);
  transform: scale(1.1);
}

.bc-20 .bc-20__chip:active {
  transform: translateY(0);
}

.bc-20 .bc-20__chip:focus-visible {
  outline: 2px solid var(--bc-20-focus);
  outline-offset: 3px;
}

@container bc34bar (max-width: 600px) {
  .bc-20 .bc-20__nav {
    border-radius: 22px;
    padding: .85rem 1rem;
    flex-direction: column;
    align-items: stretch;
    gap: .75rem;
  }

  .bc-20 .bc-20__filters {
    margin-left: 0;
    justify-content: flex-start;
  }

  .bc-20 .bc-20__crumbs {
    justify-content: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bc-20 .bc-20__chip,
    .bc-20 .bc-20__chip .bc-20__icon,
    .bc-20 .bc-20__chip .bc-20__x,
    .bc-20 .bc-20__crumbs a {
    transition: none;
  }

  .bc-20 .bc-20__chip:hover {
    transform: none;
  }

  .bc-20 .bc-20__chip:hover .bc-20__x {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript for the visual — chip removal is wired to your filter state in production (React setState, URL params, etc). */
```
