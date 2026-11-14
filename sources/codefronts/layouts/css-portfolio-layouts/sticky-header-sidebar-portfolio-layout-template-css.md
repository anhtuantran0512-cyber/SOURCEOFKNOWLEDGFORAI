---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/sticky-header-sidebar-portfolio-layout-template-css/"
title: "Sticky Header Sidebar Portfolio Layout Template CSS"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "The full app-shell template: a sticky header across the top, a sticky section rail down the left, and a long project list scrolling between them — the modern…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header Sidebar Portfolio Layout Template CSS
Source: https://codefronts.com/layouts/css-portfolio-layouts/sticky-header-sidebar-portfolio-layout-template-css/

The full app-shell template: a sticky header across the top, a sticky section rail down the left, and a long project list scrolling between them — the modern 'holy grail' with grid-template-areas naming the regions and two cooperating stickies doing what fixed positioning used to fake. The only trick worth memorizing is the offset handshake: the sidebar sticks at top: var(--headerH), so the two never fight.
## HTML
```html
<section class="cpl-16" aria-label="Sticky header and sidebar portfolio template demo">
  <div class="cpl-16__stage">
    <div class="cpl-16__shell">
      <header class="cpl-16__header">
        <span class="cpl-16__brand"><i aria-hidden="true"></i>Archive of Work</span>
        <a class="cpl-16__hire" href="#hire">Hire me</a>
      </header>
      <aside class="cpl-16__side">
        <nav aria-label="Sections">
          <a href="#cpl16-2026" aria-current="true">2026</a>
          <a href="#cpl16-2025">2025</a>
          <a href="#cpl16-2024">2024</a>
          <a href="#cpl16-experiments">Experiments</a>
        </nav>
        <p class="cpl-16__count">23 projects · 2019—2026</p>
      </aside>
      <main class="cpl-16__main">
        <h3 id="cpl16-2026">2026</h3>
        <a class="cpl-16__item" href="#halcyon" style="--img:url('https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.11 280);--b:oklch(0.5 0.15 305)"><figure></figure><div><h4>Halcyon Reader</h4><p>RSS client &amp; brand — calm software, calmer landing page.</p></div><span>Web</span></a>
        <a class="cpl-16__item" href="#matterhorn" style="--img:url('https://images.unsplash.com/photo-1551632811-561732d1e306?q=80&w=900&auto=format&fit=crop');--a:oklch(0.82 0.09 70);--b:oklch(0.55 0.14 45)"><figure></figure><div><h4>Matterhorn Gear Co.</h4><p>Storefront rebuild — 2.1s LCP to 0.8s on the same catalogue.</p></div><span>E-comm</span></a>
        <h3 id="cpl16-2025">2025</h3>
        <a class="cpl-16__item" href="#quill" style="--img:url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.1 160);--b:oklch(0.52 0.12 185)"><figure></figure><div><h4>Quill Grants</h4><p>Application portal for a state arts fund — WCAG 2.2 AA end to end.</p></div><span>Gov</span></a>
        <a class="cpl-16__item" href="#bellweather" style="--img:url('https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=900&auto=format&fit=crop');--a:oklch(0.76 0.12 20);--b:oklch(0.5 0.16 350)"><figure></figure><div><h4>Bellweather Radio</h4><p>Live player and 40-year episode archive, searchable in 90ms.</p></div><span>Media</span></a>
        <h3 id="cpl16-2024">2024</h3>
        <a class="cpl-16__item" href="#cartog" style="--img:url('https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=900&auto=format&fit=crop');--a:oklch(0.84 0.07 230);--b:oklch(0.56 0.11 260)"><figure></figure><div><h4>Cartog</h4><p>Map-annotation tool for field researchers; offline-first.</p></div><span>Tool</span></a>
        <h3 id="cpl16-experiments">Experiments</h3>
        <a class="cpl-16__item" href="#typetheremin" style="--img:url('https://images.unsplash.com/photo-1511512578047-dfb367046420?q=80&w=900&auto=format&fit=crop');--a:oklch(0.7 0.13 320);--b:oklch(0.45 0.14 345)"><figure></figure><div><h4>Type Theremin</h4><p>Variable-font weight played by cursor position. Useless, beloved.</p></div><span>Play</span></a>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-16,
.cpl-16 *,
.cpl-16 *::before,
.cpl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-16 {
  --headerH: 58px;
  --bg: oklch(0.975 0.005 100);
  --ink: oklch(0.24 0.02 280);
  --mut: oklch(0.54 0.015 280);
  --line: oklch(0.89 0.008 280);
  --acc: oklch(0.6 0.17 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-16__stage {
  width: 100%;
  container: cpl16/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cpl-16__shell {
  display: grid;
  min-height: 100%;
  grid-template-columns: 200px 1fr;
  grid-template-rows: var(--headerH) 1fr;
  grid-template-areas: "header header" "side main";
}

.cpl-16__header {
  grid-area: header;
  position: sticky;
  top: 0;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 22px;
  background: color-mix(in oklch,var(--bg) 82%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.cpl-16__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cpl-16__brand i {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: conic-gradient(from 120deg,var(--acc),oklch(0.75 0.12 200),var(--acc));
}

.cpl-16__hire {
  display: grid;
  place-items: center;
  min-height: 36px;
  padding: 0 15px;
  border-radius: 99px;
  font-size: 12.5px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.99 0 0);
  background: var(--ink);
  transition: background .2s,translate .2s;
}

.cpl-16__hire:hover,
.cpl-16__hire:focus-visible {
  background: var(--acc);
  translate: 0 -1px;
}

.cpl-16__hire:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-16__side {
  grid-area: side;
  position: sticky;
  top: var(--headerH);
  align-self: start;
  height: calc(100vh - var(--headerH));
  height: calc(100svh - var(--headerH));
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 22px 18px;
  border-right: 1px solid var(--line);
}

.cpl-16__side nav {
  display: grid;
  gap: 2px;
}

.cpl-16__side nav a {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  text-decoration: none;
  color: var(--mut);
  border-left: 2px solid transparent;
  transition: color .2s,background .2s,border-color .2s;
}

.cpl-16__side nav a:hover,
.cpl-16__side nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.93 0.01 100);
}

.cpl-16__side nav a[aria-current] {
  color: var(--ink);
  border-left-color: var(--acc);
  background: oklch(0.94 0.015 300);
}

.cpl-16__side nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cpl-16__count {
  margin-top: auto;
  font-size: 11.5px;
  color: var(--mut);
}

.cpl-16__main {
  grid-area: main;
  padding: 22px 24px 34px;
  display: grid;
  gap: 12px;
  align-content: start;
}

.cpl-16__main h3 {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--mut);
  margin-top: 14px;
  scroll-margin-top: calc(var(--headerH) + 12px);
}

.cpl-16__main h3:first-child {
  margin-top: 0;
}

.cpl-16__item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px;
  margin: 0 -12px;
  border-radius: 14px;
  text-decoration: none;
  color: inherit;
  transition: background .2s;
}

.cpl-16__item:hover,
.cpl-16__item:focus-visible {
  background: oklch(0.94 0.008 100);
}

.cpl-16__item:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cpl-16__item figure {
  flex: none;
  width: 92px;
  aspect-ratio: 4/3;
  border-radius: 10px;
  background-image: var(--img,none),linear-gradient(140deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
}

.cpl-16__item h4 {
  font-size: 14.5px;
  letter-spacing: -.01em;
}

.cpl-16__item p {
  margin-top: 3px;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--mut);
}

.cpl-16__item>span {
  margin-left: auto;
  flex: none;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .05em;
  padding: 4px 9px;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--mut);
}

@container cpl16 (width < 620px) {
  .cpl-16__shell {
    grid-template-columns: 1fr;
    grid-template-rows: var(--headerH) auto 1fr;
    grid-template-areas: "header" "side" "main";
  }

  .cpl-16__side {
    height: auto;
    flex-direction: row;
    align-items: center;
    padding: 10px 16px;
    border-right: none;
    border-bottom: 1px solid var(--line);
    background: color-mix(in oklch,var(--bg) 82%,transparent);
    backdrop-filter: blur(10px);
    z-index: 2;
  }

  .cpl-16__side nav {
    display: flex;
    gap: 4px;
    overflow-x: auto;
  }

  .cpl-16__side nav a {
    white-space: nowrap;
    border-left: none;
  }

  .cpl-16__count {
    display: none;
  }

  .cpl-16__item>span {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cpl-16 * {
    transition-duration: .01ms !important;
  }
}
```
