---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/responsive-css-masonry-photo-grid-variable-height/"
title: "Responsive CSS Masonry Photo Grid Variable Height"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "The masonry technique nobody blogs about and every feed needs: a normal CSS Grid with tiny 10px auto-rows, where each photo spans a quantized number of rows…"
has_js: "false"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive CSS Masonry Photo Grid Variable Height
Source: https://codefronts.com/layouts/css-masonry-layouts/responsive-css-masonry-photo-grid-variable-height/

The masonry technique nobody blogs about and every feed needs: a normal CSS Grid with tiny 10px auto-rows, where each photo spans a quantized number of rows by height class. Unlike multi-column, items flow LEFT-TO-RIGHT — newest first stays newest first for eyes, screen readers and Tab alike — and unlike JavaScript masonry, a resize costs zero script. Cover-cropping absorbs the fractional differences, so the wall stays gapless at every container width.
## HTML
```html
<section class="msn-03" aria-label="Responsive variable height masonry photo grid demo">
  <div class="msn-03__stage" tabindex="0">
    <header class="msn-03__head">
      <div><h2>Latest uploads</h2><p>Reading order preserved — newest first</p></div>
      <a class="msn-03__cta" href="#submit">Submit a photo</a>
    </header>
    <div class="msn-03__grid">
      <a class="msn-03__card msn-03__card--tall" href="#p1" style="--img:url('https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=800&auto=format&fit=crop');--a:oklch(0.75 0.1 130);--b:oklch(0.45 0.11 150)"><div class="msn-03__meta"><strong>Valley light</strong><span>Anya R. · 4.2k</span></div></a>
      <a class="msn-03__card msn-03__card--wide" href="#p2" style="--img:url('https://images.unsplash.com/photo-1501594907352-04cda38ebc29?q=80&w=800&auto=format&fit=crop');--a:oklch(0.7 0.1 40);--b:oklch(0.45 0.13 20)"><div class="msn-03__meta"><strong>Gate in fog</strong><span>Marc D. · 3.1k</span></div></a>
      <a class="msn-03__card msn-03__card--square" href="#p3" style="--img:url('https://images.unsplash.com/photo-1482938289607-e9573fc25ebb?q=80&w=800&auto=format&fit=crop');--a:oklch(0.72 0.09 230);--b:oklch(0.45 0.1 250)"><div class="msn-03__meta"><strong>Canyon bend</strong><span>Jules K. · 2.8k</span></div></a>
      <a class="msn-03__card msn-03__card--portrait" href="#p4" style="--img:url('https://images.unsplash.com/photo-1433086966358-54859d0ed716?q=80&w=800&auto=format&fit=crop');--a:oklch(0.78 0.08 160);--b:oklch(0.5 0.09 180)"><div class="msn-03__meta"><strong>Falls, long exposure</strong><span>Priya S. · 2.2k</span></div></a>
      <a class="msn-03__card msn-03__card--square" href="#p5" style="--img:url('https://images.unsplash.com/photo-1519125323398-675f0ddb6308?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.07 120);--b:oklch(0.55 0.09 100)"><div class="msn-03__meta"><strong>Park lines</strong><span>Tom H. · 1.9k</span></div></a>
      <a class="msn-03__card msn-03__card--portrait" href="#p6" style="--img:url('https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?q=80&w=800&auto=format&fit=crop');--a:oklch(0.7 0.1 140);--b:oklch(0.42 0.1 160)"><div class="msn-03__meta"><strong>Understory</strong><span>Anya R. · 1.7k</span></div></a>
      <a class="msn-03__card msn-03__card--wide" href="#p7" style="--img:url('https://images.unsplash.com/photo-1444723121867-7a241cacace9?q=80&w=800&auto=format&fit=crop');--a:oklch(0.55 0.1 260);--b:oklch(0.32 0.1 280)"><div class="msn-03__meta"><strong>Skyline, 9pm</strong><span>Ken W. · 1.5k</span></div></a>
      <a class="msn-03__card msn-03__card--tall" href="#p8" style="--img:url('https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?q=80&w=800&auto=format&fit=crop');--a:oklch(0.6 0.08 250);--b:oklch(0.35 0.09 270)"><div class="msn-03__meta"><strong>Midtown canyon</strong><span>Sofia L. · 1.4k</span></div></a>
      <a class="msn-03__card msn-03__card--square" href="#p9" style="--img:url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=800&auto=format&fit=crop');--a:oklch(0.74 0.09 220);--b:oklch(0.48 0.1 240)"><div class="msn-03__meta"><strong>Mirror lake</strong><span>Marc D. · 1.2k</span></div></a>
      <a class="msn-03__card msn-03__card--wide" href="#p10" style="--img:url('https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.09 90);--b:oklch(0.55 0.12 70)"><div class="msn-03__meta"><strong>First cut</strong><span>Jules K. · 1.1k</span></div></a>
      <a class="msn-03__card msn-03__card--portrait" href="#p11" style="--img:url('https://images.unsplash.com/photo-1470770841072-f978cf4d019e?q=80&w=800&auto=format&fit=crop');--a:oklch(0.68 0.08 240);--b:oklch(0.4 0.08 260)"><div class="msn-03__meta"><strong>Cabin, blue hour</strong><span>Priya S. · 980</span></div></a>
      <a class="msn-03__card msn-03__card--square" href="#p12" style="--img:url('https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=800&auto=format&fit=crop');--a:oklch(0.62 0.07 260);--b:oklch(0.38 0.08 280)"><div class="msn-03__meta"><strong>River city</strong><span>Ken W. · 940</span></div></a>
    </div>
  </div>
</section>
```
## CSS
```css
.msn-03,
.msn-03 *,
.msn-03 *::before,
.msn-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-03 {
  --bg: oklch(0.98 0.004 250);
  --ink: oklch(0.23 0.015 260);
  --mut: oklch(0.55 0.015 260);
  --line: oklch(0.9 0.008 250);
  --acc: oklch(0.55 0.18 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-03__stage {
  width: 100%;
  container: msn03/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-03__head {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 16px clamp(16px,3cqi,28px);
  background: color-mix(in oklch,var(--bg) 84%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.msn-03__head h2 {
  font-size: clamp(18px,2.6cqi,24px);
  letter-spacing: -.02em;
}

.msn-03__head p {
  font-size: 12px;
  color: var(--mut);
  margin-top: 2px;
}

.msn-03__cta {
  display: grid;
  place-items: center;
  min-height: 40px;
  padding: 0 16px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.99 0 0);
  background: var(--acc);
  transition: background .2s,translate .2s;
}

.msn-03__cta:hover,
.msn-03__cta:focus-visible {
  background: oklch(0.48 0.18 255);
  translate: 0 -1px;
}

.msn-03__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.msn-03__grid {
  display: grid;
  gap: 10px;
  grid-template-columns: repeat(auto-fill,minmax(min(210px,100%),1fr));
  grid-auto-rows: 10px;
  padding: clamp(16px,3cqi,28px);
}

.msn-03__card {
  position: relative;
  border-radius: 14px;
  overflow: clip;
  background: linear-gradient(150deg,var(--a),var(--b));
  text-decoration: none;
  color: oklch(0.99 0 0);
}

.msn-03__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--img,none);
  background-size: cover;
  background-position: center;
  transition: scale .45s cubic-bezier(.2,.7,.2,1);
}

.msn-03__card::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,transparent 52%,oklch(0.2 0.02 260/.66));
  transition: opacity .3s;
}

.msn-03__card:hover::before,
.msn-03__card:focus-visible::before {
  scale: 1.04;
}

.msn-03__card:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.msn-03__card--tall {
  grid-row: span 24;
}

.msn-03__card--portrait {
  grid-row: span 18;
}

.msn-03__card--square {
  grid-row: span 13;
}

.msn-03__card--wide {
  grid-row: span 10;
}

.msn-03__meta {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 10px;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.msn-03__meta strong {
  font-size: 13.5px;
  letter-spacing: -.01em;
  text-shadow: 0 1px 8px oklch(0.15 0.02 260/.55);
}

.msn-03__meta span {
  font-size: 11.5px;
  opacity: .85;
}

@container msn03 (width < 460px) {
  .msn-03__grid {
    grid-template-columns: repeat(2,1fr);
    gap: 8px;
  }

  .msn-03__card--tall {
    grid-row: span 20;
  }

  .msn-03__card--portrait {
    grid-row: span 15;
  }

  .msn-03__cta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-03 *,
    .msn-03 *::before {
    transition-duration: .01ms !important;
  }
}
```
