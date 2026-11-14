---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/floating-glass-pill-sticky-navbar-rounded-backdrop-blur-elevation/"
title: "Floating Glass Pill Sticky Navbar (Rounded, Backdrop Blur, Elevation)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The detached pill header used across modern product and portfolio sites: lifted away from the viewport edge, rounded to a full radius, and frosted so the…"
has_js: "false"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Glass Pill Sticky Navbar (Rounded, Backdrop Blur, Elevation)
Source: https://codefronts.com/navigation/css-sticky-navigation/floating-glass-pill-sticky-navbar-rounded-backdrop-blur-elevation/

The detached pill header used across modern product and portfolio sites: lifted away from the viewport edge, rounded to a full radius, and frosted so the page reads through it as it scrolls past. The demo covers the two things that make or break the effect — a genuinely layered rim light instead of a flat border, and a solid fallback where backdrop blur is unavailable.
## HTML
```html
<section class="sn-05" aria-label="Floating glass pill sticky navbar demo">
    <header class="sn-05__pill">
      <a class="sn-05__brand" href="#sn-05-s1"><span class="sn-05__logo" aria-hidden="true"></span>Lumen</a>
      <nav class="sn-05__nav" aria-label="Primary">
        <a class="sn-05__link" href="#sn-05-s1" aria-current="page">Work</a>
        <a class="sn-05__link" href="#sn-05-s2">Studio</a>
        <a class="sn-05__link" href="#sn-05-s3">Journal</a>
      </nav>
      <a class="sn-05__cta" href="#sn-05-s3">Contact</a>
    </header>
    <div class="sn-05__hero">
      <img class="sn-05__img" src="https://images.unsplash.com/photo-1620121692029-d088224ddc74?q=80&w=1400&auto=format&fit=crop" alt="Abstract flowing colour gradient" width="1400" height="900" loading="lazy" decoding="async">
      <div class="sn-05__herotext">
        <p class="sn-05__kicker">Glassmorphism</p>
        <h2 class="sn-05__title">Chrome that floats</h2>
        <p class="sn-05__sub">Scroll — the artwork passes underneath and the pill stays legible the whole way.</p>
      </div>
    </div>
    <main class="sn-05__main">
      <section class="sn-05__sec" id="sn-05-s1">
        <h3 class="sn-05__h">Blur plus saturation</h3>
        <p class="sn-05__p">Blur alone greys out whatever is behind it. <code>saturate(1.8)</code> restores the colour bleeding through, and that is the half of the recipe most tutorials leave out.</p>
      </section>
      <section class="sn-05__sec" id="sn-05-s2">
        <h3 class="sn-05__h">Rim light, not a border</h3>
        <p class="sn-05__p">A bright <code>inset 0 1px 0</code> on the top edge and a darker one below make the pill read as a solid piece of glass catching light.</p>
      </section>
      <section class="sn-05__sec" id="sn-05-s3">
        <h3 class="sn-05__h">Legible in every engine</h3>
        <p class="sn-05__p">An <code>@supports not (backdrop-filter: blur(1px))</code> block swaps in an opaque surface, so the labels never fall below contrast where blur is unavailable.</p>
      </section>
    </main>
  <footer class="sn-05__pagefoot">
    <p class="sn-05__pagefootin">Sticky navigation pattern 05 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-05-bg);
  --sn-05-bg: oklch(0.17 0.03 285);
  --sn-05-glass: oklch(0.28 0.04 285);
  --sn-05-ink: oklch(0.98 0.005 285);
  --sn-05-mut: oklch(0.8 0.02 285);
  --sn-05-acc: oklch(0.8 0.15 330);
  --sn-05-line: oklch(1 0 0/.16);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-05-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-05 *,
.sn-05 *::before,
.sn-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-05__pill {
  position: sticky;
  top: 14px;
  z-index: 20;
  inline-size: min(100% - 28px,720px);
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(6px,1.6vw,18px);
  min-height: 56px;
  padding: 0 8px 0 18px;
  border-radius: 999px;
  border: 1px solid var(--sn-05-line);
  background: color-mix(in oklch,var(--sn-05-glass) 58%,transparent);
  backdrop-filter: blur(20px) saturate(1.8);
  -webkit-backdrop-filter: blur(20px) saturate(1.8);
  box-shadow: 0 18px 40px -18px oklch(0 0 0/.6),inset 0 1px 0 oklch(1 0 0/.22),inset 0 -1px 0 oklch(0 0 0/.28);
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .sn-05__pill {
    background: oklch(0.28 0.04 285);
  }
}

.sn-05__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-05__logo {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: conic-gradient(from 210deg,var(--sn-05-acc),oklch(0.85 0.14 200),var(--sn-05-acc));
  box-shadow: 0 0 14px -2px var(--sn-05-acc);
}

.sn-05__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-05__link {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 13px;
  border-radius: 99px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-05-mut);
  text-decoration: none;
  transition: color .2s ease,background .2s ease;
}

.sn-05__link:hover {
  color: var(--sn-05-ink);
  background: oklch(1 0 0/.1);
}

.sn-05__link[aria-current="page"] {
  color: var(--sn-05-ink);
  background: oklch(1 0 0/.14);
}

.sn-05__cta {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 18px;
  border-radius: 99px;
  font-size: 13.4px;
  font-weight: 670;
  color: oklch(0.17 0.03 285);
  background: var(--sn-05-ink);
  text-decoration: none;
  white-space: nowrap;
  transition: transform .2s ease,background .2s ease;
}

.sn-05__cta:hover {
  transform: translateY(-1px);
  background: var(--sn-05-acc);
}

.sn-05__link:focus-visible,
.sn-05__cta:focus-visible,
.sn-05__brand:focus-visible {
  outline: 2px solid var(--sn-05-acc);
  outline-offset: 2px;
}

.sn-05__hero {
  position: relative;
  margin-block-start: -70px;
  height: min(52svh,420px);
  display: grid;
}

.sn-05__img {
  grid-area: 1/1;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: linear-gradient(140deg,oklch(0.45 0.18 320),oklch(0.35 0.14 260));
}

.sn-05__herotext {
  grid-area: 1/1;
  align-self: end;
  display: grid;
  gap: 8px;
  padding: clamp(20px,4vw,40px);
  background: linear-gradient(to top,oklch(0.17 0.03 285/.92),transparent);
}

.sn-05__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sn-05-acc);
}

.sn-05__title {
  font-size: clamp(26px,5vw,44px);
  line-height: 1.02;
  letter-spacing: -.035em;
  font-weight: 720;
  text-wrap: balance;
}

.sn-05__sub {
  max-width: 46ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--sn-05-mut);
  text-wrap: pretty;
}

.sn-05__main {
  display: grid;
}

.sn-05__sec {
  scroll-margin-top: 82px;
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,46px);
  border-top: 1px solid oklch(1 0 0/.07);
}

.sn-05__sec:nth-child(even) {
  background: oklch(1 0 0/.03);
}

.sn-05__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-05__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-05-mut);
  text-wrap: pretty;
}

.sn-05__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.1);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 560px) {
  .sn-05__pill {
    padding-inline: 14px 6px;
  }

  .sn-05__link {
    padding: 0 10px;
    font-size: 12.8px;
  }

  .sn-05__cta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-05 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-05) {
  scroll-behavior: smooth;
  scroll-padding-top: 82px;
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-05) {
    scroll-behavior: auto;
  }
}

.sn-05__bar,
.sn-05__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-05__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-05__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-05-line);
}

.sn-05__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-05-mut);
  text-align: center;
}

.sn-05__intro-title,
.sn-05__intro-sub {
  text-wrap: balance;
}
```
