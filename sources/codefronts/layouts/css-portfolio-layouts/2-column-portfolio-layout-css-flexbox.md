---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/2-column-portfolio-layout-css-flexbox/"
title: "2 Column Portfolio Layout CSS Flexbox"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "The freelancer classic: a fixed-width identity column on the left that stays put while the project list scrolls on the right — built with two flex children…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 2 Column Portfolio Layout CSS Flexbox
Source: https://codefronts.com/layouts/css-portfolio-layouts/2-column-portfolio-layout-css-flexbox/

The freelancer classic: a fixed-width identity column on the left that stays put while the project list scrolls on the right — built with two flex children and one position:sticky, no JS scroll math. The sidebar carries name, bio, section nav and socials; the content column is a stack of project rows with thumb, summary and tag chips. Under 560px of container width it degrades to a natural single-column stack.
## HTML
```html
<section class="cpl-04" aria-label="Two column flexbox portfolio layout demo">
  <div class="cpl-04__stage">
    <div class="cpl-04__layout">
      <aside class="cpl-04__side">
        <span class="cpl-04__mark" aria-hidden="true">MK</span>
        <h2>Mara Kessler</h2>
        <p class="cpl-04__role">Brand &amp; web designer<br>Portland, OR</p>
        <nav class="cpl-04__nav" aria-label="Sections">
          <a href="#cpl04-work" aria-current="true">Work</a>
          <a href="#cpl04-about">About</a>
          <a href="#cpl04-contact">Contact</a>
        </nav>
        <div class="cpl-04__soc">
          <a href="#dribbble">Dribbble</a><a href="#linkedin">LinkedIn</a><a href="#email">Email</a>
        </div>
      </aside>
      <main class="cpl-04__main">
        <h3 id="cpl04-work" class="cpl-04__sec">Selected work</h3>
        <a class="cpl-04__row" href="#lumen" style="--img:url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.1 280);--b:oklch(0.52 0.15 300)">
          <figure></figure>
          <div><h4>Lumen Health</h4><p>Patient portal redesign — 40% fewer support calls after relaunch.</p><span class="cpl-04__tags"><i>UX</i><i>Web</i><i>2026</i></span></div>
        </a>
        <a class="cpl-04__row" href="#copper" style="--img:url('https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=900&auto=format&fit=crop');--a:oklch(0.82 0.1 60);--b:oklch(0.55 0.15 40)">
          <figure></figure>
          <div><h4>Copper &amp; Pine</h4><p>Identity and packaging for a small-batch roastery in the Pacific NW.</p><span class="cpl-04__tags"><i>Brand</i><i>Print</i><i>2025</i></span></div>
        </a>
        <a class="cpl-04__row" href="#tidal" style="--img:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.09 200);--b:oklch(0.5 0.12 230)">
          <figure></figure>
          <div><h4>Tidal Analytics</h4><p>Marketing site and design tokens for a maritime data startup.</p><span class="cpl-04__tags"><i>Web</i><i>System</i><i>2025</i></span></div>
        </a>
        <a class="cpl-04__row" href="#fable" style="--img:url('https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=900&auto=format&fit=crop');--a:oklch(0.84 0.08 140);--b:oklch(0.56 0.11 160)">
          <figure></figure>
          <div><h4>Fable Press</h4><p>Editorial site for an independent publisher — variable fonts, zero images over 60KB.</p><span class="cpl-04__tags"><i>Web</i><i>Editorial</i><i>2024</i></span></div>
        </a>
        <h3 id="cpl04-about" class="cpl-04__sec">About</h3>
        <p class="cpl-04__body">Ten years making brands legible on screens. I work directly with founders — no account managers, no handoffs. Currently booking identity + site packages for Q1.</p>
        <h3 id="cpl04-contact" class="cpl-04__sec">Contact</h3>
        <p class="cpl-04__body">[email protected] — replies within two working days.</p>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-04,
.cpl-04 *,
.cpl-04 *::before,
.cpl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-04 {
  --bg: oklch(0.98 0.005 100);
  --ink: oklch(0.24 0.02 280);
  --mut: oklch(0.55 0.015 280);
  --line: oklch(0.9 0.008 280);
  --acc: oklch(0.6 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-04__stage {
  width: 100%;
  container: cpl04/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-behavior: smooth;
}

.cpl-04__layout {
  display: flex;
  gap: 32px;
  align-items: flex-start;
  padding: clamp(18px,4cqi,30px);
}

.cpl-04__side {
  flex: 0 0 210px;
  position: sticky;
  top: 24px;
  display: grid;
  gap: 14px;
}

.cpl-04__mark {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: .02em;
  color: oklch(0.98 0 0);
  background: linear-gradient(135deg,var(--acc),oklch(0.5 0.19 350));
}

.cpl-04__side h2 {
  font-size: 20px;
  letter-spacing: -.02em;
}

.cpl-04__role {
  font-size: 13px;
  line-height: 1.5;
  color: var(--mut);
}

.cpl-04__nav {
  display: grid;
  gap: 2px;
  margin-top: 6px;
}

.cpl-04__nav a {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  margin: 0 -12px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  text-decoration: none;
  color: var(--mut);
  transition: color .2s,background .2s;
}

.cpl-04__nav a[aria-current],
.cpl-04__nav a:hover,
.cpl-04__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.93 0.01 100);
}

.cpl-04__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cpl-04__soc {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  padding-top: 10px;
  border-top: 1px solid var(--line);
}

.cpl-04__soc a {
  font-size: 12px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  text-underline-offset: 3px;
  padding: 6px 0;
}

.cpl-04__soc a:hover,
.cpl-04__soc a:focus-visible {
  color: var(--acc);
  text-decoration: underline;
}

.cpl-04__main {
  flex: 1;
  min-width: 0;
  display: grid;
  gap: 14px;
}

.cpl-04__sec {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mut);
  margin-top: 10px;
  scroll-margin-top: 24px;
}

.cpl-04__sec:first-child {
  margin-top: 0;
}

.cpl-04__row {
  display: flex;
  gap: 16px;
  padding: 14px;
  margin: -4px;
  border-radius: 16px;
  text-decoration: none;
  color: inherit;
  transition: background .2s;
}

.cpl-04__row:hover,
.cpl-04__row:focus-visible {
  background: oklch(0.945 0.008 100);
}

.cpl-04__row:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cpl-04__row figure {
  flex: 0 0 118px;
  aspect-ratio: 4/3;
  border-radius: 11px;
  background-image: var(--img,none),linear-gradient(140deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
}

.cpl-04__row h4 {
  font-size: 15.5px;
  letter-spacing: -.01em;
  margin-bottom: 4px;
}

.cpl-04__row p {
  font-size: 13px;
  line-height: 1.5;
  color: var(--mut);
}

.cpl-04__tags {
  display: flex;
  gap: 6px;
  margin-top: 9px;
}

.cpl-04__tags i {
  font-style: normal;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .04em;
  padding: 3px 8px;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--mut);
}

.cpl-04__body {
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 52ch;
}

@container cpl04 (width < 560px) {
  .cpl-04__layout {
    flex-direction: column;
    gap: 22px;
  }

  .cpl-04__side {
    position: static;
    flex: none;
    width: 100%;
  }

  .cpl-04__row {
    flex-direction: column;
  }

  .cpl-04__row figure {
    flex: none;
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cpl-04__stage {
    scroll-behavior: auto;
  }

  .cpl-04 * {
    transition-duration: .01ms !important;
  }
}
```
