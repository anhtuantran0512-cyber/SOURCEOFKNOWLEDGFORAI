---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-responsive-map-box/"
title: "CSS Aspect Ratio Responsive Map Box"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "The contact-page map, minus the height:450px it shipped with since 2009: the wrapper owns aspect-ratio:16/9, the map iframe fills it 100%/100%, and a…"
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Responsive Map Box
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-responsive-map-box/

The contact-page map, minus the height:450px it shipped with since 2009: the wrapper owns aspect-ratio:16/9, the map iframe fills it 100%/100%, and a container query re-shapes the box to 1:1 when the section gets narrow — because a widescreen sliver of map is useless under a thumb. An address card overlaps the map from a shared grid cell, the wrapper paints a gradient placeholder while (or if) the tiles load, and a live badge reports which ratio is currently in charge.
## HTML
```html
<section class="car-12" aria-label="Responsive map box demo">
  <div class="car-12__stage" id="car12-top">
    <header class="car-12__bar">
      <a class="car-12__brand" href="#car12-top"><i aria-hidden="true"></i>Fjord&nbsp;Studio</a>
      <nav class="car-12__nav" aria-label="Primary"><a href="#car12-top">Work</a><a href="#car12-top">Studio</a><a href="#car12-visit" aria-current="page">Visit</a></nav>
    </header>
    <main class="car-12__main" id="car12-visit">
      <div class="car-12__intro">
        <p class="car-12__kicker">Visit us</p>
        <h1>Coffee's on. Bring sketches.</h1>
        <p class="car-12__lede">The map beside this text is an iframe with no height attribute anywhere — its wrapper declares <code>aspect-ratio:16/9</code>, and a container query squares it to <code>1:1</code> when this section drops under 640px. Resize the pane and watch the badge.</p>
        <ul class="car-12__facts">
          <li><b>Address</b><span>Skippergata 22, 0154 Oslo, Norway</span></li>
          <li><b>Hours</b><span>Mon–Fri 09–17 · Fika at 14:00 sharp</span></li>
          <li><b>Email</b><span><a href="mailto:[email protected]">[email protected]</a></span></li>
          <li><b>Phone</b><span><a href="tel:+4722334455">+47 22 33 44 55</a></span></li>
        </ul>
        <a class="car-12__cta" href="https://www.openstreetmap.org/?mlat=59.9115&mlon=10.7454#map=16/59.9115/10.7454" target="_blank" rel="noopener">Get directions ↗</a>
      </div>
      <div class="car-12__mapzone">
        <div class="car-12__map">
          <span class="car-12__fallback" aria-hidden="true"><svg viewBox="0 0 24 24" width="34" height="34"><path d="M12 2a7 7 0 0 1 7 7c0 5-7 13-7 13S5 14 5 9a7 7 0 0 1 7-7zm0 9.5A2.5 2.5 0 1 0 12 6.5a2.5 2.5 0 0 0 0 5z" fill="currentColor"/></svg></span>
          <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=10.7254%2C59.9035%2C10.7654%2C59.9195&layer=mapnik&marker=59.9115%2C10.7454" title="Map showing Fjord Studio, Skippergata 22, Oslo" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          <p class="car-12__badge" aria-hidden="true"><span class="car-12__badge--wide">aspect-ratio: 16/9</span><span class="car-12__badge--narrow">aspect-ratio: 1/1</span></p>
          <address class="car-12__card">
            <b>Fjord Studio</b>
            <span>Skippergata 22, Oslo</span>
            <em>2 min from Jernbanetorget</em>
          </address>
        </div>
      </div>
    </main>
    <footer class="car-12__foot">Ratio on the wrapper, <code>width:100%; height:100%</code> on the iframe — one source of truth, zero fixed heights. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-12,
.car-12 *,
.car-12 *::before,
.car-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-12 {
  --bg: oklch(0.975 0.005 230);
  --ink: oklch(0.24 0.02 240);
  --mut: oklch(0.5 0.015 240);
  --line: oklch(0.89 0.01 235);
  --acc: oklch(0.55 0.14 240);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-12__stage {
  width: 100%;
  container: car12/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  background: var(--bg);
}

.car-12__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 16px clamp(16px,4cqi,44px);
  border-bottom: 1px solid var(--line);
}

.car-12__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.car-12__brand i {
  width: 13px;
  height: 13px;
  border-radius: 50%;
  background: conic-gradient(from 120deg,var(--acc),oklch(0.7 0.12 190),var(--acc));
}

.car-12__nav {
  display: flex;
  gap: 2px;
}

.car-12__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.car-12__nav a:hover,
.car-12__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.93 0.008 235);
}

.car-12__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.car-12__nav a[aria-current] {
  color: var(--acc);
}

.car-12__main {
  flex: 1;
  display: grid;
  grid-template-columns: minmax(280px,2fr) minmax(0,3fr);
  gap: clamp(22px,4cqi,52px);
  align-items: center;
  max-width: 1180px;
  width: 100%;
  margin-inline: auto;
  padding: clamp(20px,4cqi,44px) clamp(16px,4cqi,44px);
}

.car-12__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.car-12__intro h1 {
  font-size: clamp(26px,4cqi,42px);
  letter-spacing: -.025em;
  font-weight: 800;
  margin-top: 8px;
  text-wrap: balance;
}

.car-12__lede {
  margin-top: 12px;
  font-size: 14px;
  line-height: 1.65;
  color: var(--mut);
}

.car-12__lede code,
.car-12__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: oklch(0.92 0.01 235);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.car-12__facts {
  list-style: none;
  margin-top: 18px;
  border-top: 1px solid var(--line);
}

.car-12__facts li {
  display: flex;
  gap: 14px;
  padding: 10px 0;
  border-bottom: 1px solid var(--line);
  font-size: 13.5px;
}

.car-12__facts b {
  flex: none;
  width: 74px;
  color: var(--mut);
  font-weight: 600;
}

.car-12__facts a {
  color: var(--acc);
  text-decoration: none;
  font-weight: 600;
}

.car-12__facts a:hover,
.car-12__facts a:focus-visible {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.car-12__facts a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 2px;
}

.car-12__cta {
  display: inline-grid;
  place-items: center;
  min-height: 48px;
  margin-top: 18px;
  padding: 0 22px;
  border-radius: 12px;
  background: var(--acc);
  color: oklch(0.99 0 0);
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  transition: background .2s,translate .2s;
}

.car-12__cta:hover,
.car-12__cta:focus-visible {
  background: color-mix(in oklch,var(--acc) 85%,black);
  translate: 0 -2px;
}

.car-12__cta:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.car-12__mapzone {
  container: car12zone/inline-size;
  min-width: 0;
}

.car-12__map {
  position: relative;
  display: grid;
  aspect-ratio: 16/9;
  border-radius: 18px;
  overflow: hidden;
  border: 1px solid var(--line);
  box-shadow: 0 18px 50px oklch(0.3 0.04 240/.14);
  background: linear-gradient(135deg,oklch(0.9 0.02 230),oklch(0.82 0.04 250)),repeating-linear-gradient(0deg,transparent 0 34px,oklch(0.75 0.03 240/.35) 34px 35px),repeating-linear-gradient(90deg,transparent 0 34px,oklch(0.75 0.03 240/.35) 34px 35px);
}

.car-12__map > * {
  grid-area: 1/1;
}

.car-12__fallback {
  place-self: center;
  color: oklch(0.55 0.1 240/.7);
}

.car-12__map iframe {
  width: 100%;
  height: 100%;
  border: 0;
  position: relative;
}

.car-12__badge {
  place-self: start end;
  margin: 12px;
  z-index: 2;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  font-weight: 600;
  color: oklch(0.98 0 0);
  background: oklch(0.25 0.03 240/.78);
  padding: 6px 10px;
  border-radius: 99px;
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  pointer-events: none;
}

.car-12__badge--narrow {
  display: none;
}

.car-12__card {
  place-self: end start;
  margin: 14px;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 2px;
  font-style: normal;
  padding: 13px 16px;
  border-radius: 13px;
  background: oklch(0.99 0.002 230/.92);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border: 1px solid oklch(0.9 0.01 235/.8);
  box-shadow: 0 8px 26px oklch(0.3 0.04 240/.2);
  max-width: min(72%,300px);
}

.car-12__card b {
  font-size: 13.5px;
  font-weight: 800;
}

.car-12__card span {
  font-size: 12px;
  color: var(--mut);
}

.car-12__card em {
  font-style: normal;
  font-size: 11px;
  font-weight: 700;
  color: var(--acc);
  margin-top: 3px;
}

.car-12__foot {
  padding: 14px clamp(16px,4cqi,44px) 28px;
  border-top: 1px solid var(--line);
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
}

@container car12zone (width < 640px) {
  .car-12__map {
    aspect-ratio: 1/1;
  }

  .car-12__badge--wide {
    display: none;
  }

  .car-12__badge--narrow {
    display: inline;
  }
}

@container car12 (width < 760px) {
  .car-12__main {
    grid-template-columns: 1fr;
    align-content: start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-12 * {
    transition-duration: .01ms !important;
  }
}
```
