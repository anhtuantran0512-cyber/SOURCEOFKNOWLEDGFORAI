---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/animated-border-glow-gradient-border-glass/"
title: "Animated Border Glow / Gradient Border Glass"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The glassmorphism-navbar-gradient-border effect: a frosted-glass bar framed by a continuous animated gradient border that rotates around the pane like a…"
has_js: "false"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Border Glow / Gradient Border Glass
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/animated-border-glow-gradient-border-glass/

The glassmorphism-navbar-gradient-border effect: a frosted-glass bar framed by a continuous animated gradient border that rotates around the pane like a light chasing its edge. Built with a typed @property custom property and a conic-gradient, so the border animates smoothly with zero JavaScript.
## HTML
```html
<div class="gn-08">
  <div class="gn-08__stage">
    <header class="gn-08-frame">
      <div class="gn-08-bar">
        <a class="gn-08-brand" href="#">Prism</a>
        <nav aria-label="Primary">
          <ul>
            <li><a href="#" aria-current="page">Studio</a></li>
            <li><a href="#">Gallery</a></li>
            <li><a href="#">Shop</a></li>
            <li><a href="#">Info</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <div class="gn-08-body">
      <h2>Watch the border chase &sect; the frame stays lit while you scroll</h2>
      <p>The sticky frame keeps its rotating gradient border visible the whole way down the page. Because <code>@property --angle</code> is registered as a typed <code>&lt;angle&gt;</code>, CSS can actually interpolate it &mdash; untyped custom properties snap between values.</p>
      <p>A pseudo-element sits behind the bar, one <code>--border-width</code> larger on every side, filled with a <code>conic-gradient(from var(--angle), &hellip;)</code>. The gradient rotates through 360deg; the only visible slice is the thin frame peeking around the glass bar in front.</p>
      <p>The gradient stops ARE the palette. Two or three saturated hues at a few positions read as a chasing highlight; a full oklch hue wheel reads as an iridescent ring.</p>
      <h3>The @property gate</h3>
      <p>Registered custom properties are the entire reason this animation works. Without <code>@property</code>, the browser treats <code>--angle</code> as a plain string and cannot interpolate it &mdash; the keyframe animation would snap from 0deg to 360deg with no intermediate frames.</p>
      <p>The registration tells the browser: this variable is an <code>&lt;angle&gt;</code> type, has an initial value of 0deg, and does not inherit. Now CSS can smoothly tween it, and the conic-gradient re-renders continuously.</p>
      <p>This is CSS Houdini territory &mdash; the ability to define new typed primitives. Baseline support arrived in 2024 (Firefox 128 was the last major engine). For older browsers, the border shows a static gradient at the initial angle &mdash; a graceful fallback that still looks intentional.</p>
      <h3>Mask-composite is the second half of the trick</h3>
      <p>The gradient pseudo-element fills the entire frame area, not just the border. To reveal only the border, use <code>mask-composite:exclude</code> with two masks: one for the outer edge, one for the inner content area. The subtraction leaves only the ring.</p>
      <p>This is the same technique CSS Tricks documented for gradient borders. Combined with the rotating <code>--angle</code>, it creates the lit-edge illusion without any actual border property.</p>
      <p>The alternative &mdash; a real <code>border-image</code> with an animated gradient &mdash; doesn't work because <code>border-image</code> cannot animate its gradient angle directly. The conic + mask + <code>@property</code> route is the only way in current CSS.</p>
      <h3>Polish moves</h3>
      <p>Add a <code>filter:blur(6px)</code> on the gradient pseudo-element to convert the crisp border into a soft glow halo. Or a matching <code>box-shadow</code> to bleed the colour outward for a bigger lit-edge feel.</p>
      <p>Speed via the animation duration: 6s is an elegant drift, 2s is an energetic gamer-RGB spin. Freeze one segment as an accent by dropping the animation entirely for a static gradient border.</p>
      <p>Animate <code>--angle</code> on hover only rather than continuously. The border comes alive when the user engages the nav and stays quiet otherwise &mdash; better for battery on mobile and less visually noisy on long-form content pages.</p>
      <p>A constantly-spinning border repaints every frame &mdash; respect <code>prefers-reduced-motion</code> and consider pausing it when off-screen for battery.</p>
      <h3>Where iridescent borders belong</h3>
      <p>NFT marketplaces and Web3 wallet-connect flows. The rotating rainbow reads as blockchain / crypto premium and matches audience expectation.</p>
      <p>Dev-tool marketing pages (Cursor, Warp, Zed, Raycast). The iridescent border reads as &ldquo;this is a crafted product&rdquo; without needing prose to say it.</p>
      <p>AI/LLM product landing pages. The gradient signals novelty and generative aesthetics without leaning on the tired holographic-mesh clich&eacute;.</p>
      <p>Gaming portals. Full RGB spin at 2s duration reads as gamer aesthetic instantly &mdash; the audience welcomes the energy.</p>
      <h3>Where it doesn't belong</h3>
      <p>Fintech dashboards for regulated audiences (banking, insurance). The animation reads as gimmicky and undermines the trust signal these products need.</p>
      <p>Healthcare and public-sector sites. Same reasoning &mdash; the accessibility-first audience needs quiet chrome, not chasing lights.</p>
      <p>Legal firm websites. ABA Model Rule 7.1 requires substantiated claims; a spinning iridescent border sends the wrong signal about seriousness.</p>
      <p>Enterprise dashboards where the user spends 8 hours a day. The animation would be genuinely irritating over that duration. Reserve for marketing surfaces, not the product itself.</p>
      <p>Keep scrolling &mdash; the sticky frame stays lit, stays glass, and demonstrates its behaviour across the full page height.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@property --gn08-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.gn-08 {
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  background: radial-gradient(90% 120% at 15% 0%,oklch(0.3 0.12 285),oklch(0.16 0.06 265) 70%);
}

.gn-08 * {
  box-sizing: border-box;
}

.gn-08__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  scroll-behavior: smooth;
  padding: 28px 24px;
}

.gn-08-frame {
  --border-width: 2px;
  position: sticky;
  top: 0;
  z-index: 5;
  width: 100%;
  border-radius: 16px;
  padding: var(--border-width);
}

.gn-08-frame::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: var(--border-width);
  background: conic-gradient(from var(--gn08-angle),oklch(0.75 0.2 30),oklch(0.75 0.19 320),oklch(0.78 0.16 250),oklch(0.82 0.18 160),oklch(0.75 0.2 30));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  animation: gn08spin 6s linear infinite;
  filter: drop-shadow(0 0 8px oklch(0.7 0.2 300/.5));
}

@keyframes gn08spin {
  to {
    --gn08-angle: 360deg;
  }
}

.gn-08-bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 0 18px;
  height: 58px;
  border-radius: 14px;
  background: rgba(20,16,40,.5);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
  backdrop-filter: blur(16px) saturate(160%);
}

.gn-08-brand {
  font-weight: 800;
  font-size: 17px;
  letter-spacing: -.01em;
  color: #fff;
  text-decoration: none;
}

.gn-08-bar nav ul {
  display: flex;
  gap: 4px;
  list-style: none;
  margin: 0;
  padding: 0;
  margin-inline-start: auto;
}

.gn-08-bar nav a {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 14px;
  border-radius: 9px;
  font: 600 14px/1 system-ui,sans-serif;
  color: rgba(240,240,255,.82);
  text-decoration: none;
  transition: background-color .15s ease,color .15s ease;
}

.gn-08-bar nav a:hover {
  background: rgba(255,255,255,.12);
  color: #fff;
}

.gn-08-bar nav a[aria-current="page"] {
  color: #fff;
  background: rgba(255,255,255,.14);
}

.gn-08-bar a:focus-visible {
  outline: 2.5px solid oklch(0.8 0.16 300);
  outline-offset: 2px;
}

.gn-08-body {
  padding: 32px 8px 80px;
  max-width: 640px;
  margin-inline: auto;
  color: rgba(240,240,255,.86);
}

.gn-08-body h2 {
  margin: 20px 0 14px;
  font: 800 22px/1.2 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
}

.gn-08-body h3 {
  margin: 28px 0 12px;
  font: 700 18px/1.25 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
}

.gn-08-body p {
  margin: 0 0 14px;
  font: 500 15px/1.65 system-ui,sans-serif;
}

.gn-08-body code {
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.18);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
  color: #fff;
}

@media (max-width: 560px) {
  .gn-08__stage {
    padding: 20px 16px;
  }

  .gn-08-bar {
    gap: 10px;
    padding: 0 12px;
    height: 52px;
  }

  .gn-08-brand {
    font-size: 15px;
  }

  .gn-08-bar nav ul {
    gap: 2px;
  }

  .gn-08-bar nav a {
    padding: 0 10px;
    font-size: 12px;
    height: 36px;
  }
}

@media (max-width: 400px) {
  .gn-08-bar nav a {
    padding: 0 8px;
    font-size: 11px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gn-08-frame::before {
    animation: none;
    --gn08-angle: 120deg;
  }
}
```
