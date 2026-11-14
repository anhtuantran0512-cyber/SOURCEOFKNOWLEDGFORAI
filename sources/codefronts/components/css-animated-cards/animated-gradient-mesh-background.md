---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/animated-gradient-mesh-background/"
title: "Animated Gradient Mesh Background"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "A fluid mesh gradient built from four blurred radial blobs drifting on independent orbits — the aurora backdrop every modern dark-mode card wants, with no…"
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient Mesh Background
Source: https://codefronts.com/components/css-animated-cards/animated-gradient-mesh-background/

A fluid mesh gradient built from four blurred radial blobs drifting on independent orbits — the aurora backdrop every modern dark-mode card wants, with no SVG filters, no canvas and no images. Animating transforms on small blurred layers keeps it cheap; animating background-position on a giant gradient (the usual recipe) does not.
## HTML
```html
<section class="ac-17" aria-label="Animated gradient mesh background card demo">
  <div class="ac-17__stage">
    <article class="ac-17__card">
      <div class="ac-17__mesh" aria-hidden="true">
        <span class="ac-17__blob ac-17__blob--a"></span>
        <span class="ac-17__blob ac-17__blob--b"></span>
        <span class="ac-17__blob ac-17__blob--c"></span>
        <span class="ac-17__blob ac-17__blob--d"></span>
        <span class="ac-17__grain"></span>
      </div>
      <div class="ac-17__inner">
        <p class="ac-17__eyebrow">Aurora release</p>
        <h2 class="ac-17__title">Ship motion that costs nothing at runtime</h2>
        <p class="ac-17__copy">Four blurred blobs, four coprime orbits, one grain overlay. No canvas, no SVG filter, no image — the whole backdrop is composited on the GPU.</p>
        <div class="ac-17__row">
          <button class="ac-17__cta" type="button">Read the write-up</button>
          <span class="ac-17__meta">4 layers · 0 requests</span>
        </div>
      </div>
    </article>
    <p class="ac-17__chip" aria-hidden="true">radial blobs + blur(42px) · mix-blend-mode:screen · 18/22/26/31 s orbits · SVG noise anti-banding · backdrop-filter panel</p>
  </div>
</section>
```
## CSS
```css
.ac-17,
.ac-17 *,
.ac-17 *::before,
.ac-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-17-bg: oklch(0.13 0.02 275);
  --ac-17-ink: oklch(0.98 0.004 280);
  --ac-17-mut: oklch(0.76 0.02 280);
  --ac-17-1: oklch(0.62 0.22 300);
  --ac-17-2: oklch(0.68 0.19 210);
  --ac-17-3: oklch(0.66 0.21 12);
  --ac-17-4: oklch(0.72 0.18 150);
  background: var(--ac-17-bg);
  color: var(--ac-17-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,52px);
}

.ac-17__card {
  position: relative;
  width: min(100%,660px);
  min-height: min(64vh,440px);
  display: grid;
  align-items: end;
  border-radius: 26px;
  overflow: hidden;
  isolation: isolate;
  border: 1px solid oklch(1 0 0/.12);
  box-shadow: 0 50px 90px -50px oklch(0 0 0/.9);
}

.ac-17__mesh {
  position: absolute;
  inset: 0;
  background: oklch(0.16 0.03 280);
  isolation: isolate;
}

.ac-17__blob {
  position: absolute;
  width: 62%;
  aspect-ratio: 1;
  border-radius: 50%;
  filter: blur(44px);
  mix-blend-mode: screen;
  will-change: transform;
}

.ac-17__blob--a {
  top: -14%;
  left: -8%;
  background: radial-gradient(closest-side,var(--ac-17-1),transparent 72%);
  animation: ac-17-a 18s ease-in-out infinite;
}

.ac-17__blob--b {
  top: 8%;
  right: -14%;
  background: radial-gradient(closest-side,var(--ac-17-2),transparent 72%);
  animation: ac-17-b 22s ease-in-out -4s infinite;
}

.ac-17__blob--c {
  bottom: -18%;
  left: 14%;
  background: radial-gradient(closest-side,var(--ac-17-3),transparent 72%);
  animation: ac-17-c 26s ease-in-out -9s infinite;
}

.ac-17__blob--d {
  bottom: -6%;
  right: 6%;
  width: 46%;
  background: radial-gradient(closest-side,var(--ac-17-4),transparent 72%);
  animation: ac-17-d 31s ease-in-out -14s infinite;
}

@keyframes ac-17-a {
  0%,
    100% {
    translate: -10% -6%;
    scale: 1;
  }

  33% {
    translate: 20% 14%;
    scale: 1.2;
  }

  66% {
    translate: -4% 22%;
    scale: .92;
  }
}

@keyframes ac-17-b {
  0%,
    100% {
    translate: 8% 4%;
    scale: 1.05;
  }

  33% {
    translate: -18% 20%;
    scale: .9;
  }

  66% {
    translate: 6% -12%;
    scale: 1.16;
  }
}

@keyframes ac-17-c {
  0%,
    100% {
    translate: 0 8%;
    scale: .95;
  }

  33% {
    translate: 24% -14%;
    scale: 1.14;
  }

  66% {
    translate: -16% 4%;
    scale: 1.02;
  }
}

@keyframes ac-17-d {
  0%,
    100% {
    translate: 4% 0;
    scale: 1.1;
  }

  33% {
    translate: -22% -18%;
    scale: .94;
  }

  66% {
    translate: 14% 12%;
    scale: 1.2;
  }
}

.ac-17__grain {
  position: absolute;
  inset: 0;
  opacity: .05;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23n)'/%3E%3C/svg%3E");
}

.ac-17__inner {
  position: relative;
  display: grid;
  gap: 13px;
  padding: clamp(22px,4vw,34px);
  margin: clamp(14px,3vw,20px);
  border-radius: 20px;
  background: oklch(0.13 0.02 275/.52);
  backdrop-filter: blur(14px) saturate(1.3);
  -webkit-backdrop-filter: blur(14px) saturate(1.3);
  border: 1px solid oklch(1 0 0/.10);
}

.ac-17__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: oklch(0.88 0.12 300);
}

.ac-17__title {
  font-size: clamp(24px,3.6vw,36px);
  font-weight: 660;
  line-height: 1.1;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.ac-17__copy {
  font-size: 14px;
  line-height: 1.6;
  color: var(--ac-17-mut);
  text-wrap: pretty;
  max-width: 52ch;
}

.ac-17__row {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-top: 6px;
}

.ac-17__cta {
  min-height: 46px;
  padding: 0 22px;
  border: 0;
  border-radius: 13px;
  background: oklch(0.97 0.01 280);
  color: oklch(0.16 0.02 275);
  font-size: 14px;
  font-weight: 650;
  font-family: inherit;
  cursor: pointer;
  transition: transform .22s,box-shadow .22s;
}

.ac-17__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 28px -14px oklch(0 0 0/.8);
}

.ac-17__cta:focus-visible {
  outline: 2px solid oklch(0.88 0.12 300);
  outline-offset: 3px;
}

.ac-17__meta {
  font-size: 11.5px;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--ac-17-mut);
  font-variant-numeric: tabular-nums;
}

.ac-17__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-17-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,760px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-17__blob {
    animation: none;
  }
}
```
