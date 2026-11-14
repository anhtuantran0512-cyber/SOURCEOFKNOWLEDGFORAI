---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/floating-pill-navbar/"
title: "Floating Pill Navbar"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The css-floating-island-glass-sticky-navbar: a detached, capsule-shaped bar anchored top-centre, floating clear of the page edges with fully rounded ends, a…"
has_js: "false"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Pill Navbar
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/floating-pill-navbar/

The css-floating-island-glass-sticky-navbar: a detached, capsule-shaped bar anchored top-centre, floating clear of the page edges with fully rounded ends, a soft drop shadow and a frosted-glass fill. The 'island' look popularised by modern app landing pages — it feels like a physical lozenge hovering above the content.
## HTML
```html
<div class="gn-04">
  <div class="gn-04__stage">
    <header class="gn-04-pill">
      <a class="gn-04-brand" href="#">&#9673; Halo</a>
      <nav aria-label="Primary">
        <ul>
          <li><a href="#" aria-current="page">Home</a></li>
          <li><a href="#">Features</a></li>
          <li><a href="#">Team</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
    </header>
    <div class="gn-04-filler">
      <p><strong>Watch the island float.</strong></p>
      <p>The pill sits above the content as you scroll &mdash; a detached, capsule-shaped bar anchored top-centre with visible gaps on either side, so the page reads through underneath.</p>
      <p>This is the "floating island" pattern popularised by modern app landing pages. It feels like a physical lozenge hovering above the imagery, connected to nothing.</p>
      <p>The max-width plus <code>margin-inline:auto</code> is what sells it &mdash; the pill never spans the full width, so there is a visible slice of content flowing past on both sides.</p>
      <p>Under the pill the shadow is doubled: a tight dark shadow for the contact plane, a wide soft shadow for the float. Read together, the lozenge sits above the page rather than stuck to it.</p>
      <h3>Anatomy of the doubled shadow</h3>
      <p>The tight contact shadow (small blur radius, dark, close to the pill) reads as ambient occlusion &mdash; the pill is casting a shadow on the surface directly beneath it.</p>
      <p>The wide float shadow (large blur radius, faint, offset further) reads as elevation &mdash; the pill is well above the surface, so its shadow spreads and softens.</p>
      <p>Together they read as physically correct. Ship only one and the effect collapses: a single tight shadow makes the pill look stuck to the page; a single wide shadow makes it look weightless.</p>
      <p>Keep the contact shadow blur under 12px and the float shadow opacity under 0.2. Above those thresholds the shadow starts to compete with the pill itself.</p>
      <h3>Sub-pill active state</h3>
      <p>Inside the pill, the active link is a filled sub-pill &mdash; a smaller capsule with its own solid background &mdash; so navigation carries a visible selected state that echoes the outer shape.</p>
      <p>Hover states are also pill-shaped, giving the whole thing a cohesive rounded language across every interactive element. Nothing rectangular appears anywhere inside the pill.</p>
      <p>Because it is <code>sticky</code>, the island rides down with the scroll while the content flows underneath the transparent gaps at its sides &mdash; exactly what you are seeing now.</p>
      <p>Try anchoring the same markup to <code>bottom-centre</code> with <code>top:auto;bottom:16px</code> for a floating mobile-style tab bar. Same technique, opposite anchor.</p>
      <h3>When the floating island beats the full-width bar</h3>
      <p>Portfolio sites where the imagery is the star. The gap on either side lets full-bleed hero images breathe without being framed by a nav strip.</p>
      <p>Editorial magazines and long-form reading experiences. The pill reads as a small, ignorable UI affordance rather than a persistent frame around the content.</p>
      <p>Landing pages that shift between light and dark sections. A full-width bar has to commit to one theme and fight the sections that don't match; a floating pill can stay glass-neutral and read against everything.</p>
      <p>Mobile-first apps that mimic native tab-bar conventions. Anchor the pill to the bottom instead of the top and it reads as iOS-native tab navigation.</p>
      <h3>When it fails</h3>
      <p>Enterprise dashboards with dense information architecture. A pill can only carry 4-5 primary links; anything more forces a dropdown that breaks the minimalist promise.</p>
      <p>SaaS marketing sites with a Sign in + Get started + Book demo + Docs + Pricing lineup. Five items plus two CTAs is too much for a pill; use a full-width bar with the doubled shadow removed.</p>
      <p>Any product where accessibility auditors will Lighthouse the page. A pill with heavy shadow can fail contrast against certain background patches; use the full-width variant for compliance-critical products.</p>
      <p>Keep scrolling &mdash; the island demonstrates its floating behaviour by staying pinned as the content moves past it.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.gn-04 {
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  background: conic-gradient(from 210deg at 30% 20%,oklch(0.8 0.14 90),oklch(0.72 0.16 30),oklch(0.68 0.18 340),oklch(0.7 0.15 250),oklch(0.8 0.14 90));
}

.gn-04 * {
  box-sizing: border-box;
}

.gn-04__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  padding-bottom: 40px;
}

.gn-04-pill {
  position: sticky;
  top: 16px;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 18px;
  max-width: 520px;
  margin: 16px auto 0;
  padding: 8px 8px 8px 22px;
  border-radius: 999px;
  background: rgba(255,255,255,.5);
  border: 1px solid rgba(255,255,255,.65);
  box-shadow: 0 2px 8px rgba(40,20,60,.14),0 16px 40px rgba(40,20,60,.16);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  backdrop-filter: blur(16px) saturate(180%);
}

.gn-04-brand {
  font-weight: 800;
  font-size: 16px;
  letter-spacing: -.01em;
  color: oklch(0.3 0.07 300);
  text-decoration: none;
  white-space: nowrap;
}

.gn-04-pill nav ul {
  display: flex;
  gap: 4px;
  list-style: none;
  margin: 0;
  padding: 0;
  margin-inline-start: auto;
}

.gn-04-pill nav a {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 16px;
  border-radius: 999px;
  font: 600 14px/1 system-ui,sans-serif;
  color: oklch(0.36 0.03 300);
  text-decoration: none;
  transition: background-color .16s ease,color .16s ease;
}

.gn-04-pill nav a:hover {
  background: rgba(255,255,255,.6);
}

.gn-04-pill nav a[aria-current="page"] {
  color: #fff;
  background: oklch(0.55 0.22 345);
  box-shadow: 0 4px 12px oklch(0.55 0.22 345/.5);
}

.gn-04-pill a:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2.5px #fff,0 0 0 5px oklch(0.55 0.22 345);
}

.gn-04-filler {
  padding: 120px 28px 60px;
  max-width: 640px;
  margin-inline: auto;
  font: 500 15px/1.65 system-ui,sans-serif;
  color: rgba(30,10,40,.72);
}

.gn-04-filler p {
  margin: 0 0 16px;
}

.gn-04-filler p strong {
  color: rgba(30,10,40,.95);
  font-weight: 800;
}

.gn-04-filler h3 {
  margin: 28px 0 12px;
  font: 800 18px/1.25 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: rgba(30,10,40,.95);
}

.gn-04-filler code {
  background: rgba(255,255,255,.4);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
}

@media (max-width: 560px) {
  .gn-04-pill {
    max-width: calc(100% - 24px);
    gap: 8px;
    padding: 6px 6px 6px 16px;
  }

  .gn-04-brand {
    font-size: 14px;
  }

  .gn-04-pill nav ul {
    gap: 2px;
  }

  .gn-04-pill nav a {
    padding: 0 10px;
    font-size: 12px;
    height: 36px;
  }
}

@media (max-width: 400px) {
  .gn-04-pill nav a {
    padding: 0 8px;
    font-size: 11px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gn-04 * {
    transition: none;
  }
}
```
