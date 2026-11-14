---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/responsive-portfolio-grid-with-hover-overlay-css/"
title: "Responsive Portfolio Grid with Hover Overlay CSS"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "Project thumbnails that keep quiet until you ask: hover (or Tab onto) a card and a gradient scrim fades up, the title and tags rise in a stagger, and a 'View…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Portfolio Grid with Hover Overlay CSS
Source: https://codefronts.com/layouts/css-portfolio-layouts/responsive-portfolio-grid-with-hover-overlay-css/

Project thumbnails that keep quiet until you ask: hover (or Tab onto) a card and a gradient scrim fades up, the title and tags rise in a stagger, and a 'View case' pill arrives last — all transform/opacity, all CSS. The part most tutorials skip is here too: the overlay fires on :focus-visible as well as :hover, so keyboard users get the identical reveal, and touch users see a permanent compact caption via a hover-capability media query.
## HTML
```html
<section class="cpl-05" aria-label="Portfolio grid with hover overlay demo">
  <div class="cpl-05__stage">
    <header class="cpl-05__head">
      <h2>Case Studies</h2>
      <p>Hover, tap or Tab — every card answers</p>
    </header>
    <div class="cpl-05__grid">
      <a class="cpl-05__card" href="#helio" style="--img:url('https://images.unsplash.com/photo-1504608524841-42fe6f032b4b?q=80&w=900&auto=format&fit=crop');--a:oklch(0.75 0.13 290);--b:oklch(0.45 0.16 260)">
        <figure></figure>
        <span class="cpl-05__ov">
          <span class="cpl-05__tags" style="--i:0"><i>iOS</i><i>Design system</i></span>
          <strong style="--i:1">Helio Weather</strong>
          <em style="--i:2">View case <b aria-hidden="true">→</b></em>
        </span>
        <span class="cpl-05__cap"><strong>Helio Weather</strong><i>iOS</i></span>
      </a>
      <a class="cpl-05__card" href="#forma" style="--img:url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=900&auto=format&fit=crop');--a:oklch(0.82 0.1 70);--b:oklch(0.55 0.15 45)">
        <figure></figure>
        <span class="cpl-05__ov">
          <span class="cpl-05__tags" style="--i:0"><i>Brand</i><i>Web</i></span>
          <strong style="--i:1">Forma Architecture</strong>
          <em style="--i:2">View case <b aria-hidden="true">→</b></em>
        </span>
        <span class="cpl-05__cap"><strong>Forma Architecture</strong><i>Brand</i></span>
      </a>
      <a class="cpl-05__card" href="#loop" style="--img:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.11 170);--b:oklch(0.48 0.12 200)">
        <figure></figure>
        <span class="cpl-05__ov">
          <span class="cpl-05__tags" style="--i:0"><i>SaaS</i><i>Dashboard</i></span>
          <strong style="--i:1">Loop Analytics</strong>
          <em style="--i:2">View case <b aria-hidden="true">→</b></em>
        </span>
        <span class="cpl-05__cap"><strong>Loop Analytics</strong><i>SaaS</i></span>
      </a>
      <a class="cpl-05__card" href="#ember" style="--img:url('https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.12 20);--b:oklch(0.5 0.17 350)">
        <figure></figure>
        <span class="cpl-05__ov">
          <span class="cpl-05__tags" style="--i:0"><i>E-comm</i><i>Art direction</i></span>
          <strong style="--i:1">Ember Ceramics</strong>
          <em style="--i:2">View case <b aria-hidden="true">→</b></em>
        </span>
        <span class="cpl-05__cap"><strong>Ember Ceramics</strong><i>E-comm</i></span>
      </a>
      <a class="cpl-05__card" href="#north" style="--img:url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=900&auto=format&fit=crop');--a:oklch(0.84 0.07 240);--b:oklch(0.58 0.11 270)">
        <figure></figure>
        <span class="cpl-05__ov">
          <span class="cpl-05__tags" style="--i:0"><i>Web</i><i>3D</i></span>
          <strong style="--i:1">North Peak Gear</strong>
          <em style="--i:2">View case <b aria-hidden="true">→</b></em>
        </span>
        <span class="cpl-05__cap"><strong>North Peak Gear</strong><i>Web</i></span>
      </a>
      <a class="cpl-05__card" href="#veda" style="--img:url('https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=900&auto=format&fit=crop');--a:oklch(0.82 0.09 130);--b:oklch(0.54 0.12 160)">
        <figure></figure>
        <span class="cpl-05__ov">
          <span class="cpl-05__tags" style="--i:0"><i>Health</i><i>Mobile</i></span>
          <strong style="--i:1">Veda Wellness</strong>
          <em style="--i:2">View case <b aria-hidden="true">→</b></em>
        </span>
        <span class="cpl-05__cap"><strong>Veda Wellness</strong><i>Health</i></span>
      </a>
      <a class="cpl-05__card" href="#cinder" style="--img:url('https://images.unsplash.com/photo-1447933601403-0c6688de566e?q=80&w=900&auto=format&fit=crop');--a:oklch(0.76 0.1 60);--b:oklch(0.5 0.13 40)">
        <figure></figure>
        <span class="cpl-05__ov">
          <span class="cpl-05__tags" style="--i:0"><i>Brand</i><i>Packaging</i></span>
          <strong style="--i:1">Cinder Coffee</strong>
          <em style="--i:2">View case <b aria-hidden="true">→</b></em>
        </span>
        <span class="cpl-05__cap"><strong>Cinder Coffee</strong><i>Brand</i></span>
      </a>
      <a class="cpl-05__card" href="#wander" style="--img:url('https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.09 210);--b:oklch(0.52 0.11 240)">
        <figure></figure>
        <span class="cpl-05__ov">
          <span class="cpl-05__tags" style="--i:0"><i>Travel</i><i>Web</i></span>
          <strong style="--i:1">Wander Atlas</strong>
          <em style="--i:2">View case <b aria-hidden="true">→</b></em>
        </span>
        <span class="cpl-05__cap"><strong>Wander Atlas</strong><i>Travel</i></span>
      </a>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-05,
.cpl-05 *,
.cpl-05 *::before,
.cpl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-05 {
  --bg: oklch(0.97 0.005 270);
  --ink: oklch(0.23 0.02 270);
  --mut: oklch(0.55 0.015 270);
  --line: oklch(0.89 0.008 270);
  --acc: oklch(0.62 0.18 290);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-05__stage {
  width: 100%;
  background: var(--bg);
  padding: clamp(18px,4cqi,30px);
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-05__head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 14px;
  margin-bottom: 20px;
}

.cpl-05__head h2 {
  font-size: 24px;
  letter-spacing: -.02em;
}

.cpl-05__head p {
  font-size: 12.5px;
  color: var(--mut);
}

.cpl-05__grid {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fill,minmax(min(220px,100%),1fr));
}

.cpl-05__card {
  position: relative;
  display: block;
  border-radius: 16px;
  overflow: hidden;
  text-decoration: none;
  color: oklch(0.98 0.005 90);
}

.cpl-05__card figure {
  aspect-ratio: 4/3;
  background-image: var(--img,none),linear-gradient(140deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  transition: scale .6s cubic-bezier(.2,.7,.2,1);
}

.cpl-05__card:hover figure,
.cpl-05__card:focus-visible figure {
  scale: 1.06;
}

.cpl-05__card:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-05__ov {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 7px;
  padding: 16px;
  opacity: 0;
  background: linear-gradient(to top,oklch(0.18 0.03 280/.92),oklch(0.18 0.03 280/.35) 55%,transparent 80%);
  transition: opacity .35s;
}

.cpl-05__ov>* {
  opacity: 0;
  translate: 0 14px;
  transition: opacity .3s,translate .4s cubic-bezier(.2,.7,.2,1);
}

.cpl-05__card:hover .cpl-05__ov,
.cpl-05__card:focus-visible .cpl-05__ov {
  opacity: 1;
}

.cpl-05__card:hover .cpl-05__ov>*,
.cpl-05__card:focus-visible .cpl-05__ov>* {
  opacity: 1;
  translate: 0 0;
  transition-delay: calc(var(--i)*70ms);
}

.cpl-05__tags {
  display: flex;
  gap: 6px;
}

.cpl-05__tags i {
  font-style: normal;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .04em;
  padding: 4px 9px;
  border-radius: 99px;
  background: oklch(1 0 0/.16);
  backdrop-filter: blur(4px);
}

.cpl-05__ov strong {
  font-size: 18px;
  letter-spacing: -.015em;
}

.cpl-05__ov em {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  align-self: start;
  font-style: normal;
  font-size: 12.5px;
  font-weight: 700;
  min-height: 34px;
  padding: 0 13px;
  border-radius: 99px;
  background: oklch(0.98 0.005 90);
  color: oklch(0.2 0.03 280);
}

.cpl-05__cap {
  display: none;
}

@media (hover: none) {
  .cpl-05__ov {
    display: none;
  }

  .cpl-05__cap {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 10px;
    padding: 12px 4px 4px;
    color: var(--ink);
  }

  .cpl-05__cap strong {
    font-size: 14px;
  }

  .cpl-05__cap i {
    font-style: normal;
    font-size: 11.5px;
    color: var(--mut);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cpl-05 * {
    transition-duration: .01ms !important;
    transition-delay: 0s !important;
  }
}
```
