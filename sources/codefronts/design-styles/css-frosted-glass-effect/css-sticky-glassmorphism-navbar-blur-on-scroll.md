---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/css-sticky-glassmorphism-navbar-blur-on-scroll/"
title: "CSS Sticky Glassmorphism Navbar Blur on Scroll"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A landing-page sticky navbar that starts fully transparent and morphs into a frosted glass bar as soon as the user scrolls past the hero — the pattern…"
has_js: "false"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Glassmorphism Navbar Blur on Scroll
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/css-sticky-glassmorphism-navbar-blur-on-scroll/

A landing-page sticky navbar that starts fully transparent and morphs into a frosted glass bar as soon as the user scrolls past the hero — the pattern Stripe, Linear, Vercel, and every 2026 marketing site ships. Real hero content (kicker + display headline + subhead + CTA + feature strip) so scrolling actually happens; the navbar transitions its background from transparent to `rgba(255,255,255,0.14)` with a 24px backdrop-filter blur once a sentinel element scrolls out of view. Zero JS libraries — a single IntersectionObserver watches one hidden sentinel div.
## HTML
```html
<div class="fg-03">
  <!-- Invisible sentinel — the IntersectionObserver watches this. -->
  <div class="fg-03__sentinel" id="fg-03-sentinel" aria-hidden="true"></div>

  <!-- Sticky navbar -->
  <nav class="fg-03__nav" id="fg-03-nav">
    <a href="#" class="fg-03__brand">
      <span class="fg-03__logo" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 2l2.09 6.26L20 9.27l-4.55 4.44L16.54 20 12 16.77 7.46 20l1.09-6.29L4 9.27l5.91-1.01L12 2z"/>
        </svg>
      </span>
      <span>Nebula</span>
    </a>
    <ul class="fg-03__links">
      <li><a href="#">Product</a></li>
      <li><a href="#">Features</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Docs</a></li>
      <li><a href="#">Blog</a></li>
    </ul>
    <div class="fg-03__actions">
      <a href="#" class="fg-03__nav-link">Sign in</a>
      <a href="#" class="fg-03__nav-cta">Start free</a>
    </div>
  </nav>

  <!-- Colorful hero backdrop -->
  <section class="fg-03__hero">
    <span class="fg-03__kicker">New · 2026 release</span>
    <h1 class="fg-03__headline">Build faster with<br><em>glass-clear</em> tools.</h1>
    <p class="fg-03__lede">The all-in-one platform for teams shipping design-forward products. Ships in 3 clicks. Free for the first 5 teammates.</p>
    <div class="fg-03__cta-row">
      <a href="#" class="fg-03__cta">Get started</a>
      <a href="#" class="fg-03__link">Watch demo →</a>
    </div>
    <div class="fg-03__metrics">
      <div><strong>2,400+</strong><span>teams</span></div>
      <div><strong>99.98%</strong><span>uptime</span></div>
      <div><strong>4.9 ★</strong><span>G2 rating</span></div>
    </div>
  </section>

  <!-- Feature strip below the fold -->
  <section class="fg-03__features">
    <h2>Why teams switch</h2>
    <div class="fg-03__feat-grid">
      <article>
        <span class="fg-03__feat-icon">⚡</span>
        <h3>Ship in seconds</h3>
        <p>Deploys go from 12 minutes to 90 seconds. Preview URLs auto-generated per branch.</p>
      </article>
      <article>
        <span class="fg-03__feat-icon">🔒</span>
        <h3>Enterprise ready</h3>
        <p>SOC 2 Type II, SSO, SCIM, audit logs. Ship it to your CISO on day one.</p>
      </article>
      <article>
        <span class="fg-03__feat-icon">✦</span>
        <h3>Beautiful by default</h3>
        <p>Designed by Vercel alumni. Every screen is production-ready before you touch it.</p>
      </article>
    </div>
  </section>
</div>
```
## CSS
```css
.fg-03,
.fg-03 *,
.fg-03 *::before,
.fg-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-03 ::selection {
  background: rgba(255,255,255,.28);
  color: #fff;
}

.fg-03 {
  --accent: #7c6cff;
  --ink: #0f172a;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",Roboto,sans-serif;
  color: #fff;
  background: radial-gradient(circle at 15% 20%, #fbbf24 0%, transparent 42%), radial-gradient(circle at 85% 25%, #ec4899 0%, transparent 45%), radial-gradient(circle at 30% 85%, #7c6cff 0%, transparent 50%), radial-gradient(circle at 80% 80%, #22d3ee 0%, transparent 48%), linear-gradient(135deg,#1e1b4b 0%,#312e81 100%);
  position: relative;
  overflow-x: hidden;
}

.fg-03__sentinel {
  position: absolute;
  top: 0;
  left: 0;
  width: 1px;
  height: 1px;
  pointer-events: none;
}
/* Navbar — starts transparent, morphs to frosted glass on scroll */

.fg-03__nav {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 14px clamp(20px,4vw,48px);
  background: transparent;
  border-bottom: 1px solid transparent;
  transition: background .35s cubic-bezier(.4,.2,.2,1), backdrop-filter .35s cubic-bezier(.4,.2,.2,1), -webkit-backdrop-filter .35s cubic-bezier(.4,.2,.2,1), border-color .35s cubic-bezier(.4,.2,.2,1);
  will-change: backdrop-filter;
}

.fg-03__nav.is-scrolled {
  background: rgba(255,255,255,0.14);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  backdrop-filter: blur(24px) saturate(180%);
  border-bottom-color: rgba(255,255,255,0.18);
  box-shadow: 0 8px 24px -12px rgba(0,0,0,0.28);
}

@supports not (backdrop-filter: blur(1px)) {
  .fg-03__nav.is-scrolled {
    background: rgba(15,15,30,0.86);
  }
}

.fg-03__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #fff;
  text-decoration: none;
  font-weight: 800;
  font-size: 1.05rem;
  letter-spacing: -.01em;
}

.fg-03__logo {
  width: 32px;
  height: 32px;
  border-radius: 9px;
  background: rgba(255,255,255,0.14);
  border: 1px solid rgba(255,255,255,0.22);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fg-03__links {
  list-style: none;
  display: flex;
  gap: clamp(14px,2vw,28px);
  margin: 0 auto;
}

.fg-03__links a {
  color: rgba(255,255,255,0.82);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 500;
  transition: color .15s;
}

.fg-03__links a:hover {
  color: #fff;
}

.fg-03__actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.fg-03__nav-link {
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 600;
}

.fg-03__nav-link:hover {
  color: #fff;
}

.fg-03__nav-cta {
  padding: 8px 16px;
  background: #fff;
  color: var(--ink);
  border-radius: 8px;
  text-decoration: none;
  font-size: .88rem;
  font-weight: 700;
  transition: transform .2s,background .2s;
}

.fg-03__nav-cta:hover {
  background: #f1f5f9;
  transform: translateY(-1px);
}
/* Hero */

.fg-03__hero {
  padding: clamp(60px,10vw,120px) clamp(20px,4vw,48px) clamp(60px,8vw,100px);
  max-width: 920px;
  margin: 0 auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.fg-03__kicker {
  display: inline-block;
  padding: 5px 14px;
  border-radius: 999px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.22);
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #fff;
}

.fg-03__headline {
  font-size: clamp(2rem,5vw,3.6rem);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1.05;
  color: #fff;
}

.fg-03__headline em {
  font-style: italic;
  color: #fbbf24;
  font-family: Georgia,"Times New Roman",serif;
  font-weight: 700;
}

.fg-03__lede {
  font-size: clamp(.98rem,1.4vw,1.15rem);
  color: rgba(255,255,255,0.78);
  line-height: 1.55;
  max-width: 52ch;
}

.fg-03__cta-row {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 8px;
}

.fg-03__cta {
  padding: 14px 26px;
  background: #fff;
  color: var(--ink);
  border-radius: 10px;
  text-decoration: none;
  font-size: .98rem;
  font-weight: 700;
  transition: transform .2s;
}

.fg-03__cta:hover {
  transform: translateY(-2px);
}

.fg-03__link {
  font-size: .94rem;
  color: #fff;
  text-decoration: none;
  font-weight: 600;
  border-bottom: 1px solid rgba(255,255,255,0.4);
  padding-bottom: 2px;
}

.fg-03__metrics {
  display: flex;
  gap: clamp(20px,3.4vw,44px);
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,0.14);
  width: 100%;
  justify-content: center;
}

.fg-03__metrics > div {
  display: flex;
  flex-direction: column;
  gap: 2px;
  align-items: center;
}

.fg-03__metrics strong {
  font-size: 1.4rem;
  font-weight: 900;
  letter-spacing: -.02em;
  color: #fff;
}

.fg-03__metrics span {
  font-size: .76rem;
  color: rgba(255,255,255,0.7);
  font-weight: 600;
}
/* Feature strip below the fold */

.fg-03__features {
  padding: clamp(40px,6vw,80px) clamp(20px,4vw,48px);
  max-width: 1080px;
  margin: 0 auto;
}

.fg-03__features h2 {
  font-size: clamp(1.4rem,2.6vw,1.9rem);
  font-weight: 800;
  letter-spacing: -.02em;
  color: #fff;
  margin-bottom: 24px;
  text-align: center;
}

.fg-03__feat-grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
}

.fg-03__feat-grid article {
  padding: 22px 20px;
  border-radius: 14px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.14);
}

.fg-03__feat-icon {
  display: inline-block;
  font-size: 1.6rem;
  margin-bottom: 10px;
}

.fg-03__feat-grid h3 {
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 6px;
}

.fg-03__feat-grid p {
  font-size: .86rem;
  color: rgba(255,255,255,0.72);
  line-height: 1.5;
}

@media (max-width: 860px) {
  .fg-03__links {
    display: none;
  }

  .fg-03__feat-grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fg-03__nav {
    transition: none;
  }

  .fg-03__cta,
    .fg-03__nav-cta {
    transition: none;
  }
}
```

## JavaScript
```js
// Sticky glassmorphism navbar — activates the frosted glass on scroll.
// IntersectionObserver watches a hidden sentinel at the top of the page;
// once the sentinel scrolls out of view, add .is-scrolled to the navbar.
// Zero libraries, ~8 lines of actual logic.
(function () {
  var nav = document.getElementById('fg-03-nav');
  var sentinel = document.getElementById('fg-03-sentinel');
  if (!nav || !sentinel || !('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function (entries) {
    // Sentinel intersecting viewport → user is at the top → transparent.
    // Sentinel NOT intersecting → user has scrolled → frosted glass.
    nav.classList.toggle('is-scrolled', !entries[0].isIntersecting);
  }, { threshold: 0 });
  io.observe(sentinel);
})();
```
