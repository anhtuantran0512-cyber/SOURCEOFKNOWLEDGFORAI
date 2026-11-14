---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/pulse-button-cta/"
title: "Pulse Button CTA"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A primary call-to-action button with an infinite cyan pulse ring emitting from the button edge — the standard evergreen pattern for \"Sign up\" / \"Get started\"…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pulse Button CTA
Source: https://codefronts.com/motion/css-pulse-animation/pulse-button-cta/

A primary call-to-action button with an infinite cyan pulse ring emitting from the button edge — the standard evergreen pattern for "Sign up" / "Get started" / "Talk to sales" landing-page CTAs. Deep navy fintech palette (Stripe / Vercel / Linear landing-page convention) with electric cyan #00d4ff accent. The ring is a ::after pseudo-element animated via box-shadow outward-cast — button text stays perfectly readable through the pulse.
## HTML
```html
<div class="pl-01">
  <div class="pl-01__badge">Fintech · SaaS landing</div>
  <h2 class="pl-01__heading">Ship code, not compliance debt.</h2>
  <p class="pl-01__sub">Talk to an engineer today — get a live audit of your billing stack in 20 minutes.</p>
  <button class="pl-01__cta" type="button">
    <span>Book a call</span>
    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M5 12h14M13 5l7 7-7 7"/>
    </svg>
  </button>
  <div class="pl-01__meta">
    <span>SOC 2 Type II</span>
    <span aria-hidden="true">·</span>
    <span>PCI DSS Level 1</span>
    <span aria-hidden="true">·</span>
    <span>99.99% uptime</span>
  </div>
</div>
```
## CSS
```css
.pl-01 {
  --bg: #0a1128;
  --surface: #0f1a3d;
  --ink: #f0f4ff;
  --sub: #8892b8;
  --accent: #00d4ff;
  --accent-dark: #0891b2;
  --line: rgba(240,244,255,.08);
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 56px 32px;
  background: radial-gradient(60% 90% at 50% 60%, rgba(0,212,255,.10) 0%, transparent 65%), radial-gradient(80% 100% at 50% 0%, rgba(0,212,255,.06) 0%, transparent 55%), var(--bg);
  color: var(--ink);
  text-align: center;
}

.pl-01 *,
.pl-01 *::before,
.pl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-01 ::selection {
  background: var(--accent);
  color: var(--bg);
}

.pl-01__badge {
  display: inline-block;
  padding: 5px 12px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(0,212,255,.06);
  color: var(--accent);
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.pl-01__heading {
  max-width: 520px;
  font-size: clamp(1.6rem,4vw,2.4rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  margin-bottom: 12px;
}

.pl-01__sub {
  max-width: 460px;
  font-size: .95rem;
  color: var(--sub);
  line-height: 1.55;
  margin-bottom: 28px;
}

.pl-01__cta {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  border: none;
  border-radius: 9px;
  background: linear-gradient(180deg,var(--accent),var(--accent-dark));
  color: var(--bg);
  font-family: inherit;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.01em;
  cursor: pointer;
  transition: transform .15s ease,box-shadow .18s ease;
  z-index: 1;
}

.pl-01__cta > span {
  position: relative;
  z-index: 1;
}

.pl-01__cta svg {
  position: relative;
  z-index: 1;
}
/* Pulse ring — box-shadow animation, compositor-only, 60fps safe */

.pl-01__cta::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 9px;
  pointer-events: none;
  z-index: 0;
  animation: pl-01-pulse 1.8s cubic-bezier(.4,0,.2,1) infinite;
}

@keyframes pl-01-pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(0,212,255,.55);
  }

  70% {
    box-shadow: 0 0 0 18px rgba(0,212,255,0);
  }

  100% {
    box-shadow: 0 0 0 18px rgba(0,212,255,0);
  }
}

.pl-01__cta:hover {
  transform: translateY(-1px);
}

.pl-01__cta:active {
  transform: translateY(1px);
}

.pl-01__cta:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.pl-01__meta {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 24px;
  font-size: .75rem;
  color: var(--sub);
  font-weight: 500;
  letter-spacing: .02em;
}

@media (prefers-reduced-motion: reduce) {
  .pl-01__cta::after {
    animation: none!important;
  }
}
```
