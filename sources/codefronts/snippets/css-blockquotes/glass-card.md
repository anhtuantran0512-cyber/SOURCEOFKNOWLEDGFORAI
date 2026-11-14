---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/glass-card/"
title: "Glassmorphism CSS Blockquote Card"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "A frosted-glass quote card floating over a colorful gradient scene — the full glassmorphism recipe, not just blur(): backdrop-filter combines blur(18px) with…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism CSS Blockquote Card
Source: https://codefronts.com/snippets/css-blockquotes/glass-card/

A frosted-glass quote card floating over a colorful gradient scene — the full glassmorphism recipe, not just blur(): backdrop-filter combines blur(18px) with saturate(160%) so the colors behind the glass intensify the way real frosted acrylic does, a 1px white-alpha border fakes the catch-light on the pane's edge, and an inner top highlight (inset box-shadow) sells the thickness. The backdrop has actual objects behind the glass — orbs that drift slowly — because glass you can't see anything through is just a gray box.
## HTML
```html
<section class="bq-09" aria-label="Glassmorphism blockquote card demo">
  <div class="bq-09__stage">
    <div class="bq-09__orb bq-09__orb--a" aria-hidden="true"></div>
    <div class="bq-09__orb bq-09__orb--b" aria-hidden="true"></div>
    <div class="bq-09__orb bq-09__orb--c" aria-hidden="true"></div>
    <figure class="bq-09__glass">
      <blockquote>
        <p>“Good abstractions are like frosted glass — they hide the machinery without pretending it isn't there.”</p>
      </blockquote>
      <figcaption class="bq-09__by">
        <span class="bq-09__ava" aria-hidden="true">LN</span>
        <span><strong>Lena Novak</strong><br><em>Staff Engineer, Praxis Cloud</em></span>
      </figcaption>
    </figure>
    <p class="bq-09__chip" aria-hidden="true">backdrop-filter: blur(18px) saturate(160%) · edge light · inner bevel</p>
  </div>
</section>
```
## CSS
```css
.bq-09,
.bq-09 *,
.bq-09 *::before,
.bq-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ink: oklch(0.98 0.005 260);
  --mut: oklch(0.87 0.02 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-09__stage {
  position: relative;
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: linear-gradient(135deg,oklch(0.45 0.16 290),oklch(0.55 0.19 340) 55%,oklch(0.72 0.15 55));
  overflow: hidden;
}

.bq-09__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(2px);
}

.bq-09__orb--a {
  width: 280px;
  height: 280px;
  left: 12%;
  top: 14%;
  background: radial-gradient(circle at 32% 30%,oklch(0.85 0.12 200),oklch(0.6 0.18 250));
  animation: bq09-drift 16s ease-in-out infinite alternate;
}

.bq-09__orb--b {
  width: 190px;
  height: 190px;
  right: 14%;
  top: 22%;
  background: radial-gradient(circle at 35% 30%,oklch(0.9 0.13 95),oklch(0.7 0.19 30));
  animation: bq09-drift 13s ease-in-out infinite alternate-reverse;
}

.bq-09__orb--c {
  width: 230px;
  height: 230px;
  left: 38%;
  bottom: 8%;
  background: radial-gradient(circle at 30% 30%,oklch(0.88 0.1 330),oklch(0.55 0.2 310));
  animation: bq09-drift 19s ease-in-out infinite alternate;
}

@keyframes bq09-drift {
  from {
    translate: 0 0;
  }

  to {
    translate: 60px -40px;
  }
}

.bq-09__glass {
  position: relative;
  width: min(100%,520px);
  padding: clamp(26px,4vw,38px);
  border-radius: 22px;
  background: oklch(0.35 0.06 300);
  border: 1px solid oklch(1 0 0/.28);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.32),0 24px 50px oklch(0 0 0/.35);
}

@supports (backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px)) {
  .bq-09__glass {
    background: oklch(1 0 0/.1);
    -webkit-backdrop-filter: blur(18px) saturate(160%);
    backdrop-filter: blur(18px) saturate(160%);
  }
}

.bq-09__glass blockquote p {
  font-size: clamp(18px,2.4vw,23px);
  line-height: 1.55;
  font-weight: 600;
  letter-spacing: -.012em;
  text-wrap: balance;
  text-shadow: 0 1px 2px oklch(0 0 0/.18);
}

.bq-09__by {
  display: flex;
  align-items: center;
  gap: 13px;
  margin-top: 22px;
  font-size: 13.5px;
  line-height: 1.45;
  color: var(--mut);
}

.bq-09__by strong {
  color: var(--ink);
  font-weight: 700;
  font-size: 14px;
}

.bq-09__by em {
  font-style: normal;
  font-size: 12.5px;
}

.bq-09__ava {
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 800;
  background: oklch(1 0 0/.2);
  border: 1px solid oklch(1 0 0/.35);
  flex: none;
}

.bq-09__chip {
  position: relative;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--ink);
  padding: 7px 13px;
  border-radius: 99px;
  background: oklch(1 0 0/.14);
  border: 1px solid oklch(1 0 0/.25);
}

@media (prefers-reduced-motion: reduce) {
  .bq-09 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
