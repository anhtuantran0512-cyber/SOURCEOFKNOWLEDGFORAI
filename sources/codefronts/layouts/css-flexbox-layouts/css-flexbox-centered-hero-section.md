---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-centered-hero-section/"
title: "CSS Flexbox Centered Hero Section"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A full-bleed hero section with perfect flex centering, animated gradient orbs, a headline group, subtext, and a CTA button row — demonstrating multi-axis…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Centered Hero Section
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-centered-hero-section/

A full-bleed hero section with perfect flex centering, animated gradient orbs, a headline group, subtext, and a CTA button row — demonstrating multi-axis flex alignment.
## HTML
```html
<div class="fl-10">
  <!-- Background effects -->
  <div class="fl-10__bg-orb fl-10__bg-orb--1"></div>
  <div class="fl-10__bg-orb fl-10__bg-orb--2"></div>
  <div class="fl-10__bg-orb fl-10__bg-orb--3"></div>
  <div class="fl-10__noise"></div>

  <!-- Star field -->
  <div class="fl-10__stars">
    <div class="fl-10__star" style="top:8%;left:12%;animation-delay:0s"></div>
    <div class="fl-10__star" style="top:15%;left:78%;animation-delay:-1s"></div>
    <div class="fl-10__star" style="top:72%;left:8%;animation-delay:-0.5s"></div>
    <div class="fl-10__star" style="top:55%;left:92%;animation-delay:-2s"></div>
    <div class="fl-10__star" style="top:88%;left:45%;animation-delay:-1.5s"></div>
    <div class="fl-10__star" style="top:30%;left:55%;animation-delay:-0.8s"></div>
  </div>

  <!-- Hero: flex column, align-items center, justify-content center -->
  <div class="fl-10__hero">
    <div class="fl-10__eyebrow">
      <div class="fl-10__eyebrow-dot"></div>
      CSS Flexbox · Perfect Centering
    </div>

    <h1 class="fl-10__headline">
      Center <span class="fl-10__hl-italic">anything</span> with<br>
      <span class="fl-10__hl-gradient">two lines of CSS</span>
    </h1>

    <p class="fl-10__subhead">
      The oldest CSS challenge — centering an element both horizontally and vertically — solved at last. <code style="color:rgba(255,255,255,0.6)">display: flex</code> + <code style="color:rgba(255,255,255,0.6)">align-items: center</code> + <code style="color:rgba(255,255,255,0.6)">justify-content: center</code>.
    </p>

    <div class="fl-10__ctas">
      <button class="fl-10__cta fl-10__cta--primary">Get started free →</button>
      <button class="fl-10__cta fl-10__cta--ghost">View demos</button>
    </div>

    <div class="fl-10__social-proof">
      <div class="fl-10__avatars">
        <div class="fl-10__avatar" style="background:linear-gradient(135deg,#a855f7,#6d28d9)">A</div>
        <div class="fl-10__avatar" style="background:linear-gradient(135deg,#38bdf8,#0284c7)">B</div>
        <div class="fl-10__avatar" style="background:linear-gradient(135deg,#f472b6,#be185d)">C</div>
        <div class="fl-10__avatar" style="background:linear-gradient(135deg,#34d399,#059669)">D</div>
      </div>
      <div class="fl-10__proof-text"><strong>12,400+</strong> developers using this pattern</div>
    </div>
  </div>

  <div class="fl-10__annotation">
    display: flex;<br>
    flex-direction: column;<br>
    align-items: center;<br>
    justify-content: center;
  </div>
</div>
```
## CSS
```css
.fl-10,
.fl-10 *,
.fl-10 *::before,
.fl-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-10 ::selection {
  background: #a855f7;
  color: #fff;
}

.fl-10 {
  --bg: #08000f;
  --accent: #a855f7;
  --accent2: #38bdf8;
  --accent3: #f472b6;
  --text: #fff;
  --muted: rgba(255,255,255,0.5);
  font-family: 'Bricolage Grotesque', sans-serif;
  background: var(--bg);
  min-height: 500px;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
}
/* Background glow orbs */

.fl-10__bg-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  pointer-events: none;
  animation: fl-10-drift 8s ease-in-out infinite;
}

.fl-10__bg-orb--1 {
  width: 300px;
  height: 300px;
  background: rgba(168,85,247,0.25);
  top: -80px;
  left: 30%;
  animation-delay: 0s;
}

.fl-10__bg-orb--2 {
  width: 250px;
  height: 250px;
  background: rgba(56,189,248,0.15);
  bottom: -60px;
  right: 20%;
  animation-delay: -4s;
}

.fl-10__bg-orb--3 {
  width: 200px;
  height: 200px;
  background: rgba(244,114,182,0.15);
  top: 40%;
  left: 5%;
  animation-delay: -2s;
}

@keyframes fl-10-drift {
  0%,
    100% {
    transform: translate(0,0) scale(1);
  }

  33% {
    transform: translate(20px,-15px) scale(1.05);
  }

  66% {
    transform: translate(-10px,10px) scale(0.98);
  }
}
/* Grid-noise texture via SVG */

.fl-10__noise {
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  pointer-events: none;
  opacity: 0.5;
}
/* ── THE FLEX CENTERING PATTERN ── */

.fl-10__hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* horizontal center */
  justify-content: center;
  /* vertical center */
  min-height: 500px;
  padding: 48px 24px;
  position: relative;
  z-index: 1;
  text-align: center;
  gap: 24px;
}

.fl-10__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(168,85,247,0.12);
  border: 1px solid rgba(168,85,247,0.25);
  border-radius: 20px;
  padding: 5px 14px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--accent);
}

.fl-10__eyebrow-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  animation: fl-10-pulse-dot 1.5s ease-in-out infinite;
}

@keyframes fl-10-pulse-dot {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.4;
    transform: scale(0.7);
  }
}

.fl-10__headline {
  font-size: clamp(1.8rem, 5vw, 3.2rem);
  font-weight: 800;
  color: var(--text);
  line-height: 1.1;
  letter-spacing: -0.03em;
  max-width: 600px;
}

.fl-10__headline .fl-10__hl-italic {
  font-family: 'Instrument Serif', serif;
  font-style: italic;
  font-weight: 400;
  color: var(--accent);
}

.fl-10__headline .fl-10__hl-gradient {
  background: linear-gradient(90deg, var(--accent2), var(--accent3));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fl-10__subhead {
  font-size: 0.92rem;
  color: var(--muted);
  line-height: 1.7;
  max-width: 440px;
  font-weight: 400;
}

.fl-10__ctas {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
}

.fl-10__cta {
  padding: 11px 24px;
  border-radius: 10px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  font-family: 'Bricolage Grotesque', sans-serif;
  border: none;
  transition: transform 0.2s, box-shadow 0.2s;
}

.fl-10__cta:hover {
  transform: translateY(-2px);
}

.fl-10__cta--primary {
  background: var(--accent);
  color: #fff;
  box-shadow: 0 0 30px rgba(168,85,247,0.3);
}

.fl-10__cta--primary:hover {
  box-shadow: 0 6px 40px rgba(168,85,247,0.5);
}

.fl-10__cta--ghost {
  background: rgba(255,255,255,0.06);
  color: rgba(255,255,255,0.7);
  border: 1px solid rgba(255,255,255,0.1);
}

.fl-10__cta--ghost:hover {
  background: rgba(255,255,255,0.1);
  color: #fff;
}

.fl-10__social-proof {
  display: flex;
  align-items: center;
  gap: 12px;
}

.fl-10__avatars {
  display: flex;
}

.fl-10__avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 2px solid var(--bg);
  margin-left: -8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.6rem;
  font-weight: 800;
  color: #fff;
}

.fl-10__avatars .fl-10__avatar:first-child {
  margin-left: 0;
}

.fl-10__proof-text {
  font-size: 0.72rem;
  color: var(--muted);
  font-weight: 500;
}

.fl-10__proof-text strong {
  color: var(--text);
}
/* Flex annotation overlay */

.fl-10__annotation {
  position: absolute;
  bottom: 14px;
  right: 16px;
  font-size: 0.62rem;
  font-family: 'Courier New', monospace;
  color: rgba(168,85,247,0.4);
  text-align: right;
  line-height: 1.8;
  pointer-events: none;
}
/* Responsive stars decoration */

.fl-10__stars {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fl-10__star {
  position: absolute;
  width: 2px;
  height: 2px;
  border-radius: 50%;
  background: rgba(255,255,255,0.6);
  animation: fl-10-twinkle 3s ease-in-out infinite;
}

@keyframes fl-10-twinkle {
  0%,
    100% {
    opacity: 0.6;
  }

  50% {
    opacity: 0.1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fl-10__bg-orb,
    .fl-10__eyebrow-dot,
    .fl-10__star {
    animation: none;
  }

  .fl-10__cta {
    transition: none;
  }
}
```
