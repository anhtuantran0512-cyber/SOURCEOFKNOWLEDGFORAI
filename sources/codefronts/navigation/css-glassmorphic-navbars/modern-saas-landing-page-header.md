---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/modern-saas-landing-page-header/"
title: "Modern SaaS Landing Page Header"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The tailwind-css-glassmorphism-navbar-example that everyone actually searches for: a clean floating glass header sitting over a vibrant gradient hero, brand…"
has_js: "false"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern SaaS Landing Page Header
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/modern-saas-landing-page-header/

The tailwind-css-glassmorphism-navbar-example that everyone actually searches for: a clean floating glass header sitting over a vibrant gradient hero, brand mark on the left, primary links in the middle, and a high-contrast gradient CTA on the right. This is the workhorse SaaS marketing header — legible, sticky, and built to convert.
## HTML
```html
<div class="gn-01">
  <div class="gn-01__stage">
    <header class="gn-01-bar">
      <a class="gn-01-brand" href="#">&#9670; Nimbus</a>
      <nav class="gn-01-nav" aria-label="Primary">
        <ul>
          <li><a href="#">Product</a></li>
          <li><a href="#">Pricing</a></li>
          <li><a href="#">Docs</a></li>
          <li><a href="#">Blog</a></li>
        </ul>
      </nav>
      <div class="gn-01-actions">
        <a class="gn-01-ghost" href="#">Sign in</a>
        <a class="gn-01-cta" href="#">Start free</a>
      </div>
    </header>
    <div class="gn-01-hero">
      <p class="gn-01-eyebrow">Ship faster</p>
      <h2>The workspace your whole team ships from.</h2>
    </div>
    <div class="gn-01-body">
      <p>The floating glass header stays pinned to the top as you scroll. Translucent white fill + <code>backdrop-filter:blur(16px) saturate(180%)</code> + a 1px hairline &mdash; the classic trio.</p>
      <p>The <code>saturate(180%)</code> boost is the secret sauce most Tailwind snippets miss. Plain <code>blur()</code> alone looks grey and dead; boosting saturation makes the frosted pane feel like it's actually made of the colours behind it.</p>
      <p>Dark link text stays high-contrast even as the gradient shifts underneath, because the fill is white-ish and &ge;45% opaque. The blur alone is never enough to guarantee contrast; the fill opacity is the actual floor.</p>
      <p>The CTA is a linear-gradient pill with its own coloured shadow so it reads as the single most important control on the page. It lifts on hover with a subtle <code>translateY(-2px)</code>.</p>
      <p>For a darker product, flip the fill to <code>rgba(17,17,20,.5)</code> and link colour to near-white &mdash; the same structure works as a dark SaaS header without changing a single selector.</p>
      <p>Tailwind users: the class equivalent is <code>sticky top-4 backdrop-blur-xl backdrop-saturate-150 bg-white/50 border border-white/60 rounded-2xl shadow-lg</code>. Every declaration maps to a utility class or arbitrary value.</p>
      <h3>Why saturate matters more than blur radius</h3>
      <p>Increasing the blur radius past 20-24px starts to cost frames on low-end Android hardware. Increasing the saturation stops at zero cost &mdash; saturation is a colour matrix operation, not a spatial convolution.</p>
      <p>Practical range: <code>blur(12px)</code> at <code>saturate(180%)</code> reads as premium and stays smooth. <code>blur(24px)</code> at <code>saturate(120%)</code> reads as heavy privacy-glass but taxes older devices. Pick the trade-off deliberately.</p>
      <p>Test the header over your <em>lightest</em> hero, not your darkest. Dark heroes hide contrast bugs; light heroes reveal them.</p>
      <h3>Layout hygiene for sticky glass headers</h3>
      <p>The header must have a fixed <code>height</code> declaration (56px in this demo). Sticky elements with intrinsic height can shift as fonts swap in &mdash; a real Cumulative Layout Shift hit that Google's Core Web Vitals reports.</p>
      <p>Keep the sticky header out of ancestors with <code>overflow:hidden</code> on the block axis. This is the single most common sticky-fails-silently bug &mdash; the header renders once at the top and never moves.</p>
      <p>Give the containing element a defined block-size (the outer wrapper here is <code>min-height:100vh</code>). Sticky without a resolvable containing block behaves like static.</p>
      <p>Above 1200px viewport, consider raising the nav's max-width to keep the CTA anchored to the right edge rather than floating in a wide gap. Below 640px, collapse the primary links into a hamburger and keep the CTA prominent.</p>
      <h3>Real SaaS marketing sites shipping this pattern</h3>
      <p>Stripe uses a variant with heavier saturation over its animated gradient hero. Linear uses a near-black variant with cyan accent. Vercel uses white glass with brand purple CTA. Superhuman uses navy glass with peach CTA. Framer uses a pill variant of the same recipe (see Demo 04).</p>
      <p>Every one of them ships the same three-declaration recipe: translucent fill + <code>backdrop-filter:blur() saturate()</code> + 1px hairline. The palette differs; the structure doesn't.</p>
      <p>Keep scrolling &mdash; the sticky bar demonstrates its main job by staying pinned as the content flows underneath it.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.gn-01 {
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  background: radial-gradient(120% 120% at 12% 0%,oklch(0.72 0.2 300) 0%,oklch(0.65 0.19 260) 40%,oklch(0.7 0.16 200) 100%);
}

.gn-01 * {
  box-sizing: border-box;
}

.gn-01__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  scroll-behavior: smooth;
  padding: 20px;
}

.gn-01-bar {
  position: sticky;
  top: 12px;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 12px 14px 12px 20px;
  border-radius: 16px;
  background: rgba(255,255,255,.5);
  border: 1px solid rgba(255,255,255,.6);
  box-shadow: 0 8px 30px rgba(20,10,50,.18);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  backdrop-filter: blur(16px) saturate(180%);
}

.gn-01-brand {
  font-weight: 800;
  font-size: 17px;
  letter-spacing: -.02em;
  color: oklch(0.28 0.08 285);
  text-decoration: none;
}

.gn-01-nav {
  margin-inline: auto;
}

.gn-01-nav ul {
  display: flex;
  gap: 6px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.gn-01-nav a {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 14px;
  border-radius: 10px;
  font: 600 14px/1 system-ui,sans-serif;
  color: oklch(0.32 0.03 285);
  text-decoration: none;
  transition: background-color .16s ease,color .16s ease;
}

.gn-01-nav a:hover {
  background: rgba(255,255,255,.55);
  color: oklch(0.24 0.09 285);
}

.gn-01-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.gn-01-ghost {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 14px;
  border-radius: 10px;
  font: 600 14px/1 system-ui,sans-serif;
  color: oklch(0.3 0.05 285);
  text-decoration: none;
}

.gn-01-ghost:hover {
  background: rgba(255,255,255,.5);
}

.gn-01-cta {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 20px;
  border-radius: 11px;
  font: 700 14px/1 system-ui,sans-serif;
  color: #fff;
  text-decoration: none;
  background: linear-gradient(135deg,oklch(0.62 0.24 20),oklch(0.6 0.23 340));
  box-shadow: 0 8px 20px oklch(0.6 0.23 350/.5);
  transition: transform .16s ease,box-shadow .16s ease;
}

.gn-01-cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 26px oklch(0.6 0.23 350/.6);
}

.gn-01-cta:focus-visible,
.gn-01-nav a:focus-visible,
.gn-01-ghost:focus-visible {
  outline: 2.5px solid #fff;
  outline-offset: 2px;
}

.gn-01-hero {
  padding: 56px 14px 28px;
  max-width: 560px;
}

.gn-01-eyebrow {
  margin: 0 0 10px;
  font: 700 12px/1 system-ui,sans-serif;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(255,255,255,.85);
}

.gn-01-hero h2 {
  margin: 0;
  font: 800 34px/1.08 system-ui,sans-serif;
  letter-spacing: -.02em;
  color: #fff;
  text-shadow: 0 2px 20px rgba(20,0,40,.25);
  text-wrap: balance;
}

.gn-01-body {
  padding: 32px 14px 80px;
  max-width: 640px;
  color: rgba(255,255,255,.9);
  text-shadow: 0 1px 6px rgba(30,0,50,.3);
}

.gn-01-body p {
  margin: 0 0 14px;
  font: 500 15px/1.65 system-ui,sans-serif;
}

.gn-01-body h3 {
  margin: 28px 0 12px;
  font: 800 18px/1.25 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
  text-shadow: 0 1px 12px rgba(30,0,50,.4);
}

.gn-01-body code {
  background: rgba(255,255,255,.28);
  border: 1px solid rgba(255,255,255,.4);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
  color: #fff;
  text-shadow: none;
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
}

@media (max-width: 640px) {
  .gn-01-bar {
    gap: 8px;
    padding: 8px 8px 8px 14px;
  }

  .gn-01-nav {
    display: none;
  }

  .gn-01-brand {
    font-size: 15px;
  }

  .gn-01-ghost {
    display: none;
  }

  .gn-01-cta {
    padding: 0 14px;
    font-size: 13px;
    height: 36px;
  }

  .gn-01-hero h2 {
    font-size: 26px;
  }
}

@media (max-width: 400px) {
  .gn-01-actions {
    gap: 6px;
  }

  .gn-01-brand {
    font-size: 14px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gn-01 * {
    transition: none;
  }
}
```
