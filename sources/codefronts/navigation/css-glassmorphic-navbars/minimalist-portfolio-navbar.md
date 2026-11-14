---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/minimalist-portfolio-navbar/"
title: "Minimalist Portfolio Navbar"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The minimal-frosted-glass-nav-bar every designer portfolio and photography showcase wants: an ultra-clean, very-low-opacity glass strip that barely tints the…"
has_js: "false"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Portfolio Navbar
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/minimalist-portfolio-navbar/

The minimal-frosted-glass-nav-bar every designer portfolio and photography showcase wants: an ultra-clean, very-low-opacity glass strip that barely tints the work behind it, letting the imagery lead while the navigation stays present, quiet and readable. Restraint over effect — the anti-maximalist glass navbar.
## HTML
```html
<div class="gn-11">
  <div class="gn-11__stage">
    <header class="gn-11-bar">
      <a class="gn-11-brand" href="#">Ava Reyes</a>
      <nav aria-label="Primary">
        <ul>
          <li><a href="#" aria-current="page">Work</a></li>
          <li><a href="#">Studio</a></li>
          <li><a href="#">Journal</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
    </header>
    <div class="gn-11-body">
      <div class="gn-11-grid">
        <figure class="gn-11-tile" aria-hidden="true"></figure>
        <figure class="gn-11-tile" aria-hidden="true"></figure>
        <figure class="gn-11-tile" aria-hidden="true"></figure>
        <figure class="gn-11-tile" aria-hidden="true"></figure>
        <figure class="gn-11-tile" aria-hidden="true"></figure>
        <figure class="gn-11-tile" aria-hidden="true"></figure>
      </div>
      <div class="gn-11-copy">
        <h2>Ultra-clean glass over full-bleed portfolio work</h2>
        <p>The sticky bar barely tints the imagery underneath. A near-clear <code>rgba(255,255,255,.14)</code> fill lets the work read straight through &mdash; the navigation is present, quiet, readable.</p>
        <p>A light <code>backdrop-filter:blur(8px)</code> is just enough to lift the letterforms off busy photography without frosting the work into obscurity.</p>
        <p>No border box, no shadow, no CTA &mdash; only a hairline bottom rule to separate nav from canvas. Type does the work: tight letter-spacing, small logo, generous <code>gap</code>, low-key underline that grows from the centre on hover.</p>
        <p>Because the fill is so light, legibility rides on the <code>text-shadow</code> plus the blur softening high-frequency detail directly under the strip.</p>
        <p>The active link is marked by a small persistent underline, not a filled pill &mdash; anything heavier would break the minimalist contract.</p>
        <h3>Minimalism as constraint, not decoration</h3>
        <p>Every element removed makes the imagery louder. No border box means no visible frame competing with the composition. No shadow means no fake elevation implying the header sits above the work.</p>
        <p>No CTA means no commercial intrusion into the reading experience. Portfolio sites are trust-builders, not conversion funnels &mdash; the visitor decides to reach out, not the button.</p>
        <p>Every restraint has a payoff. The imagery reads first. The navigation reads only when the visitor looks for it. The header stops being chrome and becomes a service.</p>
        <h3>The centre-grow underline in detail</h3>
        <p>The underline pseudo-element sits below each link at <code>transform: scaleX(0)</code> with <code>transform-origin: center</code>. On hover, it transitions to <code>scaleX(1)</code> &mdash; growing from the centre outward instead of unfurling from the left.</p>
        <p>Setting <code>transform-origin: center</code> is the key. Forgetting it makes the underline grow from the left, which reads as directional and pushy. From the centre, it reads as balanced and confident.</p>
        <p>Duration around 250ms with an ease-out curve. Faster reads as accidental; slower reads as ceremonial. 250ms is the sweet spot for &ldquo;yes, I noticed you&rdquo;.</p>
        <h3>When the near-clear fill works</h3>
        <p>Over dark photography with strong tonal range. The white glass tints subtly without competing with the imagery's own light-dark story.</p>
        <p>Over hero video with limited palette range. The light tint reads as unified with the video's atmospheric colour.</p>
        <p>Over animated backgrounds where an opaque bar would break the ambient motion. The near-clear fill keeps the motion continuous.</p>
        <h3>When it fails</h3>
        <p>Over predominantly white imagery. The nearly-clear glass over a light background makes text almost invisible. Test with your lightest hero image, not your darkest.</p>
        <p>Over very busy imagery with high-frequency detail. The light blur can't hide it, and the text ends up sitting on visual noise.</p>
        <p>For products that require a visible CTA. Portfolio pattern doesn't include one; if you need one, use Demo 01 or Demo 04 instead.</p>
        <h3>Real portfolio sites shipping this pattern</h3>
        <p>Awwwards site-of-the-day winners frequently use it. It signals that the designer understands restraint, which is what awards judges respond to.</p>
        <p>Photography portfolio sites (Bruce Munro, David LaChapelle, high-end wedding photographers). The imagery must lead; the chrome must serve.</p>
        <p>Design agency landing pages that want to signal seniority. Junior agencies show off their design system in the chrome; senior agencies let the client work show it.</p>
        <p>Editorial magazines and long-form journalism. The Read.cv variant is exactly this pattern with a hairline separator and no CTA.</p>
        <p>Keep scrolling &mdash; the sticky bar stays present, stays quiet, stays out of the way of the imagery below.</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.gn-11 {
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  background: linear-gradient(200deg,oklch(0.55 0.09 40) 0%,oklch(0.35 0.07 20) 40%,oklch(0.22 0.05 265) 100%);
}

.gn-11 * {
  box-sizing: border-box;
}

.gn-11__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  scroll-behavior: smooth;
}

.gn-11-bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 34px;
  height: 60px;
  padding: 0 26px;
  background: rgba(255,255,255,.12);
  border-bottom: 1px solid rgba(255,255,255,.18);
  -webkit-backdrop-filter: blur(8px) saturate(130%);
  backdrop-filter: blur(8px) saturate(130%);
}

.gn-11-brand {
  font-weight: 700;
  font-size: 15px;
  letter-spacing: .02em;
  color: #fff;
  text-decoration: none;
  text-shadow: 0 1px 8px rgba(0,0,0,.35);
}

.gn-11-bar nav ul {
  display: flex;
  gap: 26px;
  list-style: none;
  margin: 0;
  padding: 0;
  margin-inline-start: auto;
}

.gn-11-bar nav a {
  position: relative;
  display: inline-flex;
  align-items: center;
  height: 60px;
  font: 500 14px/1 system-ui,sans-serif;
  letter-spacing: .01em;
  color: rgba(255,255,255,.82);
  text-decoration: none;
  text-shadow: 0 1px 6px rgba(0,0,0,.3);
  transition: color .2s ease;
}

.gn-11-bar nav a::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 18px;
  height: 1.5px;
  background: #fff;
  transform: scaleX(0);
  transform-origin: center;
  transition: transform .25s ease;
}

.gn-11-bar nav a:hover {
  color: #fff;
}

.gn-11-bar nav a:hover::after {
  transform: scaleX(1);
}

.gn-11-bar nav a[aria-current="page"] {
  color: #fff;
}

.gn-11-bar nav a[aria-current="page"]::after {
  transform: scaleX(1);
  opacity: .7;
}

.gn-11-bar a:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
  border-radius: 3px;
}

.gn-11-body {
  padding: 0;
}

.gn-11-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(180px,1fr));
  gap: 6px;
  padding: 6px;
}

.gn-11-tile {
  margin: 0;
  aspect-ratio: 4/5;
  border-radius: 6px;
}

.gn-11-tile:nth-child(1) {
  background: radial-gradient(120% 100% at 30% 20%,oklch(0.72 0.14 45),oklch(0.4 0.09 25));
}

.gn-11-tile:nth-child(2) {
  background: radial-gradient(120% 100% at 70% 30%,oklch(0.55 0.15 320),oklch(0.28 0.08 285));
}

.gn-11-tile:nth-child(3) {
  background: radial-gradient(120% 100% at 40% 60%,oklch(0.6 0.13 200),oklch(0.32 0.08 240));
}

.gn-11-tile:nth-child(4) {
  background: radial-gradient(120% 100% at 60% 40%,oklch(0.65 0.12 90),oklch(0.35 0.08 55));
}

.gn-11-tile:nth-child(5) {
  background: radial-gradient(120% 100% at 50% 70%,oklch(0.7 0.13 30),oklch(0.3 0.09 350));
}

.gn-11-tile:nth-child(6) {
  background: radial-gradient(120% 100% at 30% 30%,oklch(0.58 0.14 270),oklch(0.24 0.07 260));
}

.gn-11-copy {
  padding: 32px 28px 80px;
  max-width: 640px;
  margin-inline: auto;
  color: rgba(255,255,255,.82);
}

.gn-11-copy h2 {
  margin: 20px 0 12px;
  font: 800 22px/1.2 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
  text-shadow: 0 1px 8px rgba(0,0,0,.4);
}

.gn-11-copy h3 {
  margin: 28px 0 12px;
  font: 700 18px/1.25 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
  text-shadow: 0 1px 8px rgba(0,0,0,.4);
}

.gn-11-copy p {
  margin: 0 0 14px;
  font: 500 15px/1.65 system-ui,sans-serif;
  text-shadow: 0 1px 6px rgba(0,0,0,.3);
}

.gn-11-copy code {
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.22);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
  color: #fff;
  text-shadow: none;
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
}

@media (max-width: 640px) {
  .gn-11-bar {
    gap: 14px;
    padding: 0 16px;
    height: 52px;
  }

  .gn-11-brand {
    font-size: 14px;
  }

  .gn-11-bar nav ul {
    gap: 14px;
  }

  .gn-11-bar nav a {
    font-size: 12px;
    height: 52px;
  }
}

@media (max-width: 400px) {
  .gn-11-bar nav ul {
    gap: 10px;
  }

  .gn-11-bar nav a {
    font-size: 11px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gn-11-bar nav a,
    .gn-11-bar nav a::after {
    transition: none;
  }
}
```
