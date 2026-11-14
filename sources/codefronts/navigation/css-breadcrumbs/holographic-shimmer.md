---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/holographic-shimmer/"
title: "NFT/Web3 Holographic Shimmer Breadcrumb Component"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A dark deep-space breadcrumb bar with a Pokemon-holo-card iridescent shimmer that sweeps a conic rainbow across the frosted glass surface on hover, giving…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: NFT/Web3 Holographic Shimmer Breadcrumb Component
Source: https://codefronts.com/navigation/css-breadcrumbs/holographic-shimmer/

A dark deep-space breadcrumb bar with a Pokemon-holo-card iridescent shimmer that sweeps a conic rainbow across the frosted glass surface on hover, giving NFT marketplaces an angle-dependent signature that fits collection to token drill-down paths.
## HTML
```html
<section class="bc-18" aria-label="Web3 NFT breadcrumb navigation demo">
      <nav aria-label="Breadcrumb">
        <ol class="bc-18__list">
          <li class="bc-18__item">
            <a class="bc-18__link" href="#">
              <svg class="bc-18__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 11.5 12 4l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
              <span>Home</span>
            </a>
          </li>
          <li class="bc-18__item"><a class="bc-18__link" href="#">Collections</a></li>
          <li class="bc-18__item"><a class="bc-18__link" href="#">CryptoPunks</a></li>
          <li class="bc-18__item"><a class="bc-18__link" aria-current="page" href="#">Punk #7804</a></li>
        </ol>
      </nav>
    </section>
```
## CSS
```css
@property --bc-18-holo-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.bc-18 {
  --bc-18-bg-1: oklch(0.16 0.06 275);
  --bc-18-bg-2: oklch(0.11 0.05 295);
  --bc-18-bg-3: oklch(0.09 0.04 250);
  --bc-18-card: oklch(0.22 0.03 275 / 0.55);
  --bc-18-stroke: oklch(0.78 0.05 280 / 0.22);
  --bc-18-ink: oklch(0.94 0.02 280);
  --bc-18-muted: oklch(0.72 0.04 280);
  --bc-18-focus: oklch(0.82 0.18 300);
  --bc-18-holo-1: oklch(0.82 0.19 25);
  --bc-18-holo-2: oklch(0.86 0.19 90);
  --bc-18-holo-3: oklch(0.84 0.18 160);
  --bc-18-holo-4: oklch(0.80 0.20 240);
  --bc-18-holo-5: oklch(0.78 0.22 315);
  --bc-18-holo-opacity: 0.35;
  --bc-18-font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --bc-18-size: 0.9375rem;
  --bc-18-weight: 500;
  --bc-18-collapse: 36rem;
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem, 5vw, 4rem);
  font-family: var(--bc-18-font);
  color: var(--bc-18-ink);
  background: radial-gradient(1200px 700px at 15% 10%, oklch(0.30 0.10 285 / 0.55), transparent 60%), radial-gradient(900px 600px at 85% 90%, oklch(0.28 0.12 320 / 0.45), transparent 65%), linear-gradient(160deg, var(--bc-18-bg-1), var(--bc-18-bg-2) 55%, var(--bc-18-bg-3));
  overflow: hidden;
}

.bc-18 *,
.bc-18 *::before,
.bc-18 *::after {
  box-sizing: border-box;
}

.bc-18 nav {
  width: min(100%, 720px);
}

.bc-18__list {
  position: relative;
  isolation: isolate;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.25rem 0.5rem;
  margin: 0;
  padding: 0.5rem 1rem;
  list-style: none;
  border-radius: 999px;
  background: var(--bc-18-card);
  border: 1px solid var(--bc-18-stroke);
  backdrop-filter: blur(18px) saturate(140%);
  -webkit-backdrop-filter: blur(18px) saturate(140%);
  box-shadow: 0 1px 0 oklch(1 0 0 / 0.08) inset, 0 20px 50px -20px oklch(0 0 0 / 0.55);
  overflow: hidden;
}

.bc-18__list::before,
.bc-18__list::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  opacity: 0;
  transition: opacity 260ms ease;
  z-index: 0;
}

.bc-18__list::before {
  background: conic-gradient(
          from var(--bc-18-holo-angle),
          var(--bc-18-holo-1),
          var(--bc-18-holo-2),
          var(--bc-18-holo-3),
          var(--bc-18-holo-4),
          var(--bc-18-holo-5),
          var(--bc-18-holo-1)
        );
  mix-blend-mode: color-dodge;
  filter: blur(6px) saturate(160%);
}

.bc-18__list::after {
  background: repeating-linear-gradient(
          115deg,
          oklch(1 0 0 / 0.10) 0 2px,
          transparent 2px 7px
        );
  mix-blend-mode: overlay;
  mask-image: linear-gradient(115deg, transparent 20%, black 45%, black 60%, transparent 85%);
  -webkit-mask-image: linear-gradient(115deg, transparent 20%, black 45%, black 60%, transparent 85%);
}

.bc-18__list:hover::before,
.bc-18__list:focus-within::before {
  opacity: var(--bc-18-holo-opacity);
  animation: bc-18-spin 6s linear infinite;
}

.bc-18__list:hover::after,
.bc-18__list:focus-within::after {
  opacity: 0.55;
  animation: bc-18-sweep 3.6s ease-in-out infinite;
}

@keyframes bc-18-spin {
  to {
    --bc-18-holo-angle: 360deg;
  }
}

@keyframes bc-18-sweep {
  0%,
    100% {
    transform: translateX(-8%);
  }

  50% {
    transform: translateX(8%);
  }
}

.bc-18__item {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  min-height: 44px;
}

.bc-18__item + .bc-18__item::before {
  content: "";
  display: inline-block;
  width: 8px;
  height: 8px;
  margin: 0 0.35rem 0 0.1rem;
  border-right: 1.5px solid var(--bc-18-muted);
  border-top: 1.5px solid var(--bc-18-muted);
  transform: rotate(45deg);
  opacity: 0.7;
}

.bc-18__link {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  min-height: 44px;
  padding: 0.45rem 0.7rem;
  border-radius: 8px;
  font-size: var(--bc-18-size);
  font-weight: var(--bc-18-weight);
  letter-spacing: 0.01em;
  color: var(--bc-18-muted);
  text-decoration: none;
  transition: color 180ms ease, background-color 180ms ease, transform 180ms ease;
}

.bc-18__link:hover {
  color: var(--bc-18-ink);
  background: color-mix(in oklch, var(--bc-18-ink) 8%, transparent);
}

.bc-18__link:focus-visible {
  outline: 2px solid var(--bc-18-focus);
  outline-offset: 3px;
  color: var(--bc-18-ink);
}

.bc-18__link[aria-current="page"] {
  color: var(--bc-18-ink);
  background: color-mix(in oklch, var(--bc-18-ink) 6%, transparent);
  border-bottom: 2px solid transparent;
  border-image: linear-gradient(
          90deg,
          color-mix(in oklch, var(--bc-18-holo-1) 70%, transparent),
          color-mix(in oklch, var(--bc-18-holo-3) 70%, transparent),
          color-mix(in oklch, var(--bc-18-holo-5) 70%, transparent)
        ) 1;
  border-radius: 8px 8px 0 0;
}

.bc-18__icon {
  width: 16px;
  height: 16px;
  color: currentColor;
  flex: none;
}

.bc-18__list:has(.bc-18__link:hover) .bc-18__link:not(:hover):not([aria-current="page"]) {
  color: color-mix(in oklch, var(--bc-18-muted) 80%, transparent);
}

@container (max-width: 24rem) {
  .bc-18__item:nth-child(2),
    .bc-18__item:nth-child(3) {
    display: none;
  }

  .bc-18__list::after {
    content: "";
  }
}

@media (max-width: 30rem) {
  .bc-18__link {
    padding: 0.4rem 0.5rem;
  }

  .bc-18__item + .bc-18__item::before {
    margin: 0 0.15rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bc-18__list:hover::before,
    .bc-18__list:focus-within::before,
    .bc-18__list:hover::after,
    .bc-18__list:focus-within::after {
    animation: none;
  }

  .bc-18__link {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — @property makes --bc-18-holo-angle animatable, so the conic-gradient shimmer rotates via @keyframes. */
```
