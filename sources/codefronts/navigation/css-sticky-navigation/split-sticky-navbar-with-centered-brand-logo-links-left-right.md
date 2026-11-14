---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/split-sticky-navbar-with-centered-brand-logo-links-left-right/"
title: "Split Sticky Navbar with Centered Brand Logo (Links Left + Right)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The symmetrical header favoured by fashion, hospitality and editorial brands: navigation split into two wings with the wordmark holding the centre."
has_js: "false"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split Sticky Navbar with Centered Brand Logo (Links Left + Right)
Source: https://codefronts.com/navigation/css-sticky-navigation/split-sticky-navbar-with-centered-brand-logo-links-left-right/

The symmetrical header favoured by fashion, hospitality and editorial brands: navigation split into two wings with the wordmark holding the centre. The layout must keep the logo optically centred even when one wing has three links and the other has two — which is exactly what 1fr auto 1fr guarantees and flexbox does not.
## HTML
```html
<section class="sn-14" aria-label="Split sticky navbar with centered logo demo">
    <header class="sn-14__bar">
      <nav class="sn-14__wing sn-14__wing--start" aria-label="Primary">
        <a class="sn-14__link" href="#sn-14-s1" aria-current="page">New in</a>
        <a class="sn-14__link" href="#sn-14-s2">Atelier</a>
        <a class="sn-14__link" href="#sn-14-s3">Journal</a>
      </nav>
      <a class="sn-14__brand" href="#sn-14-s1">MAISON<span class="sn-14__mark" aria-hidden="true">·</span>NEUF</a>
      <nav class="sn-14__wing sn-14__wing--end" aria-label="Account">
        <a class="sn-14__link" href="#sn-14-s2">Stores</a>
        <a class="sn-14__link" href="#sn-14-s3">Account</a>
        <a class="sn-14__link sn-14__link--bag" href="#sn-14-s3">Bag <span class="sn-14__count">2</span></a>
      </nav>
    </header>
    <main>
      <section class="sn-14__hero">
        <img class="sn-14__img" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=1200&auto=format&fit=crop" alt="A minimalist wristwatch photographed on a plain surface" width="1200" height="800" loading="lazy" decoding="async">
        <div class="sn-14__herotext">
          <p class="sn-14__kicker">Autumn edit</p>
          <h2 class="sn-14__title">Balanced by construction</h2>
        </div>
      </section>
      <section class="sn-14__sec" id="sn-14-s1">
        <h3 class="sn-14__h">1fr · auto · 1fr</h3>
        <p class="sn-14__p">Two equal tracks flank an auto track sized to the wordmark. The centre is geometric, not coincidental, so uneven wings cannot pull it off-axis.</p>
      </section>
      <section class="sn-14__sec" id="sn-14-s2">
        <h3 class="sn-14__h">Wings that shrink politely</h3>
        <p class="sn-14__p">Each wing carries <code>min-width: 0</code>, so a long label truncates instead of shouldering the logo out of the middle.</p>
      </section>
      <section class="sn-14__sec" id="sn-14-s3">
        <h3 class="sn-14__h">Two rows, not a hamburger</h3>
        <p class="sn-14__p">Below 720px the header stacks wordmark over a centred nav row, keeping the brand-first hierarchy the layout exists for.</p>
      </section>
    </main>
  <footer class="sn-14__pagefoot">
    <p class="sn-14__pagefootin">Sticky navigation pattern 14 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-14-bg);
  --sn-14-bg: oklch(0.955 0.006 90);
  --sn-14-surface: oklch(0.992 0.003 90);
  --sn-14-ink: oklch(0.2 0.012 60);
  --sn-14-mut: oklch(0.5 0.012 60);
  --sn-14-acc: oklch(0.44 0.09 40);
  --sn-14-line: oklch(0.2 0.012 60/.14);
  --sn-14-h: 70px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-14-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-14 *,
.sn-14 *::before,
.sn-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-14__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 16px;
  min-height: var(--sn-14-h);
  padding: 0 clamp(16px,3vw,30px);
  background: color-mix(in oklch,var(--sn-14-surface) 88%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-14-line);
}

.sn-14__wing {
  display: flex;
  align-items: center;
  gap: clamp(6px,1.6vw,18px);
  min-width: 0;
}

.sn-14__wing--start {
  justify-self: start;
}

.sn-14__wing--end {
  justify-self: end;
}

.sn-14__brand {
  justify-self: center;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: clamp(14px,2.2vw,17px);
  font-weight: 600;
  letter-spacing: .22em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-14__mark {
  color: var(--sn-14-acc);
}

.sn-14__link {
  display: flex;
  align-items: center;
  gap: 6px;
  min-height: 40px;
  padding: 0 4px;
  font-size: 12.4px;
  font-weight: 560;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--sn-14-mut);
  text-decoration: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: color .18s ease;
}

.sn-14__link:hover {
  color: var(--sn-14-ink);
}

.sn-14__link[aria-current="page"] {
  color: var(--sn-14-ink);
  text-decoration: underline;
  text-underline-offset: 6px;
  text-decoration-thickness: 1px;
}

.sn-14__link:focus-visible,
.sn-14__brand:focus-visible {
  outline: 1.5px solid var(--sn-14-acc);
  outline-offset: 4px;
}

.sn-14__count {
  display: grid;
  place-items: center;
  min-inline-size: 18px;
  block-size: 18px;
  padding-inline: 5px;
  border-radius: 99px;
  background: var(--sn-14-acc);
  color: oklch(1 0 0);
  font-size: 10.5px;
  letter-spacing: 0;
  font-weight: 660;
}

.sn-14__hero {
  position: relative;
  height: min(50svh,400px);
  display: grid;
}

.sn-14__img {
  grid-area: 1/1;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: linear-gradient(150deg,oklch(0.78 0.04 60),oklch(0.62 0.05 40));
}

.sn-14__herotext {
  grid-area: 1/1;
  align-self: end;
  display: grid;
  gap: 8px;
  padding: clamp(20px,4vw,42px);
  color: oklch(1 0 0);
  background: linear-gradient(to top,oklch(0.2 0.012 60/.75),transparent 70%);
}

.sn-14__kicker {
  font-size: 11px;
  letter-spacing: .22em;
  text-transform: uppercase;
  opacity: .92;
}

.sn-14__title {
  font-size: clamp(24px,4.4vw,40px);
  line-height: 1.06;
  letter-spacing: -.02em;
  font-weight: 600;
  text-wrap: balance;
}

.sn-14__sec {
  scroll-margin-top: var(--sn-14-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(26px,4.6vw,52px);
  border-bottom: 1px solid var(--sn-14-line);
}

.sn-14__h {
  font-size: clamp(18px,2.4vw,24px);
  line-height: 1.18;
  letter-spacing: -.015em;
  font-weight: 640;
  text-wrap: balance;
}

.sn-14__p {
  max-width: 52ch;
  font-size: 15px;
  line-height: 1.7;
  color: var(--sn-14-mut);
  text-wrap: pretty;
}

.sn-14__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.2 0.012 60/.07);
  padding: 2px 6px;
  border-radius: 4px;
}

@media (max-width: 720px) {
  .sn-14 {
    --sn-14-h: auto;
  }

  .sn-14__bar {
    grid-template-columns: 1fr;
    justify-items: center;
    gap: 6px;
    padding-block: 12px;
  }

  .sn-14__wing--start,
    .sn-14__wing--end {
    justify-self: center;
  }

  .sn-14__brand {
    order: -1;
  }

  .sn-14__wing--end {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-14 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-14) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-14-h) + 8px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-14) {
    scroll-behavior: auto;
  }
}

.sn-14__bar,
.sn-14__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-14__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-14__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-14-line);
}

.sn-14__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-14-mut);
  text-align: center;
}

.sn-14__intro-title,
.sn-14__intro-sub {
  text-wrap: balance;
}
```
