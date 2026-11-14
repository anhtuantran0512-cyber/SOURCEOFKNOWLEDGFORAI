---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/split-screen-portfolio-layout-html-css/"
title: "Split Screen Portfolio Layout HTML CSS"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "A true 50/50 split: the left half is a pinned identity panel — name, thesis, index of cases — while the right half scrolls through case studies."
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split Screen Portfolio Layout HTML CSS
Source: https://codefronts.com/layouts/css-portfolio-layouts/split-screen-portfolio-layout-html-css/

A true 50/50 split: the left half is a pinned identity panel — name, thesis, index of cases — while the right half scrolls through case studies. The 2026 twist is one selector: the stage uses :has() to watch which case you're hovering and repaints the left panel's accent to that project's hue, so the two halves feel wired together without a byte of JavaScript.
## HTML
```html
<section class="cpl-07" aria-label="Split screen portfolio layout demo">
  <div class="cpl-07__stage">
    <div class="cpl-07__split">
      <div class="cpl-07__left">
        <p class="cpl-07__kicker">Case files</p>
        <h2>Noor Haddad<br><em>UX writing &amp; content design</em></h2>
        <p class="cpl-07__bio">Interfaces fail in words before they fail in pixels. I write the words. Three recent cases on the right — hover them.</p>
        <nav class="cpl-07__index" aria-label="Case index">
          <a href="#cpl07-rose"><i>01</i>Meridian onboarding</a>
          <a href="#cpl07-gold"><i>02</i>Sift error language</a>
          <a href="#cpl07-jade"><i>03</i>Fieldnote voice &amp; tone</a>
        </nav>
        <span class="cpl-07__rule" aria-hidden="true"></span>
        <a class="cpl-07__mail" href="#email">[email protected]</a>
      </div>
      <div class="cpl-07__right">
        <article class="cpl-07__case cpl-07__case--rose" id="cpl07-rose">
          <figure style="--img:url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.12 20);--b:oklch(0.5 0.16 350)"></figure>
          <h3>Meridian onboarding</h3>
          <p>Cut sign-up abandonment 31% by rewriting a 9-screen flow down to 4 — every field earns its ask.</p>
          <a href="#case-meridian">Read the case</a>
        </article>
        <article class="cpl-07__case cpl-07__case--gold" id="cpl07-gold">
          <figure style="--img:url('https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=900&auto=format&fit=crop');--a:oklch(0.84 0.1 85);--b:oklch(0.6 0.14 60)"></figure>
          <h3>Sift error language</h3>
          <p>A 212-message audit that replaced blame ("Invalid input") with routes forward. Support tickets fell by a fifth.</p>
          <a href="#case-sift">Read the case</a>
        </article>
        <article class="cpl-07__case cpl-07__case--jade" id="cpl07-jade">
          <figure style="--img:url('https://images.unsplash.com/photo-1455390582262-044cdead277a?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.11 165);--b:oklch(0.52 0.13 190)"></figure>
          <h3>Fieldnote voice &amp; tone</h3>
          <p>A working voice guide with 40 before/afters — adopted by three product squads in its first month.</p>
          <a href="#case-fieldnote">Read the case</a>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-07,
.cpl-07 *,
.cpl-07 *::before,
.cpl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-07 {
  --bg: oklch(0.97 0.006 85);
  --panel: oklch(0.24 0.02 280);
  --ink: oklch(0.24 0.02 280);
  --mut: oklch(0.55 0.015 280);
  --line: oklch(0.89 0.01 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-07__stage {
  width: 100%;
  container: cpl07/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cpl-07__split {
  --acc: oklch(0.72 0.15 75);
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: start;
  min-height: 100%;
}

.cpl-07__split:has(.cpl-07__case--rose:hover) {
  --acc: oklch(0.68 0.18 15);
}

.cpl-07__split:has(.cpl-07__case--gold:hover) {
  --acc: oklch(0.78 0.14 85);
}

.cpl-07__split:has(.cpl-07__case--jade:hover) {
  --acc: oklch(0.72 0.14 165);
}

.cpl-07__left {
  position: sticky;
  top: 0;
  height: 100vh;
  height: 100svh;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding: 34px 30px;
  background: var(--panel);
  color: oklch(0.95 0.008 85);
}

.cpl-07__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
  transition: color .4s;
}

.cpl-07__left h2 {
  font-size: clamp(21px,3cqi,27px);
  line-height: 1.15;
  letter-spacing: -.02em;
}

.cpl-07__left h2 em {
  font-style: normal;
  font-weight: 400;
  color: oklch(0.68 0.02 85);
  font-size: .72em;
}

.cpl-07__bio {
  font-size: 13.5px;
  line-height: 1.6;
  color: oklch(0.78 0.015 85);
  max-width: 34ch;
}

.cpl-07__index {
  display: grid;
  gap: 2px;
  margin-top: auto;
}

.cpl-07__index a {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 40px;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  color: oklch(0.9 0.01 85);
  transition: color .25s,translate .25s;
}

.cpl-07__index a i {
  font-style: normal;
  font-size: 11px;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
  transition: color .4s;
}

.cpl-07__index a:hover,
.cpl-07__index a:focus-visible {
  color: var(--acc);
  translate: 4px 0;
}

.cpl-07__index a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.cpl-07__rule {
  height: 2px;
  width: 44px;
  background: var(--acc);
  border-radius: 2px;
  transition: background .4s,width .4s;
}

.cpl-07__split:has(.cpl-07__case:hover) .cpl-07__rule {
  width: 80px;
}

.cpl-07__mail {
  font-size: 12.5px;
  color: oklch(0.72 0.015 85);
  text-decoration: none;
  padding: 4px 0;
}

.cpl-07__mail:hover,
.cpl-07__mail:focus-visible {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cpl-07__right {
  display: grid;
  gap: 26px;
  padding: 34px 30px;
}

.cpl-07__case {
  display: grid;
  gap: 9px;
  scroll-margin: 24px;
}

.cpl-07__case figure {
  aspect-ratio: 16/10;
  border-radius: 14px;
  background-image: var(--img,none),linear-gradient(140deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  transition: scale .4s cubic-bezier(.2,.7,.2,1);
}

.cpl-07__case:hover figure {
  scale: 1.02;
}

.cpl-07__case h3 {
  font-size: 17px;
  letter-spacing: -.015em;
}

.cpl-07__case p {
  font-size: 13px;
  line-height: 1.55;
  color: var(--mut);
}

.cpl-07__case a {
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: underline;
  text-underline-offset: 4px;
  text-decoration-thickness: 1.5px;
  padding: 4px 0;
  justify-self: start;
}

.cpl-07__case a:hover,
.cpl-07__case a:focus-visible {
  color: oklch(0.5 0.15 280);
}

.cpl-07__case a:focus-visible {
  outline: 2px solid oklch(0.5 0.15 280);
  outline-offset: 3px;
  border-radius: 4px;
}

@container cpl07 (width < 620px) {
  .cpl-07__split {
    grid-template-columns: 1fr;
  }

  .cpl-07__left {
    position: static;
    height: auto;
  }

  .cpl-07__index {
    margin-top: 4px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cpl-07 * {
    transition-duration: .01ms !important;
  }
}
```
