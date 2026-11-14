---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/startup-landing-page-hero-slide-in/"
title: "Startup Landing Page Hero Slide-In"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A YC-style startup landing hero where the announcement badge, headline, subhead, dual CTA row, and logo-strip social proof each slide up sequentially — the…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Startup Landing Page Hero Slide-In
Source: https://codefronts.com/motion/css-slide-in-animation/startup-landing-page-hero-slide-in/

A YC-style startup landing hero where the announcement badge, headline, subhead, dual CTA row, and logo-strip social proof each slide up sequentially — the layout used by Y Combinator startups, Product Hunt launches, and modern seed-stage product landing pages.
## HTML
```html
<div class="sl-15">
  <div class="sl-15__inner">
    <div class="sl-15__badge">
      <span class="sl-15__dot"></span>
      Launching on Product Hunt today
    </div>
    <h1 class="sl-15__headline">The fastest way to <span>ship components</span></h1>
    <p class="sl-15__sub">Copy-paste production-grade CSS collections. Zero framework tax. Zero npm install. Just working code — for teams that need to ship, not experiment.</p>
    <div class="sl-15__cta">
      <button class="sl-15__btn sl-15__btn--primary">Get started free →</button>
      <button class="sl-15__btn sl-15__btn--ghost">Watch 90-second demo</button>
    </div>
    <div class="sl-15__proof">
      <p class="sl-15__proof-label">Backed by 500+ product teams</p>
      <div class="sl-15__logos">
        <span>◆ LINEAR</span>
        <span>◈ VERCEL</span>
        <span>◇ STRIPE</span>
        <span>▲ RAYCAST</span>
        <span>● NOTION</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-15 {
  --bg: #0a0e1c;
  --text: #f0eeff;
  --sub: #a1a1b0;
  --purple: #a855f7;
  --pink: #ec4899;
  --good: #22c55e;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 64px 32px;
  background: radial-gradient(80% 100% at 20% 0%, rgba(168,85,247,.18) 0%, transparent 55%), radial-gradient(70% 90% at 100% 100%, rgba(236,72,153,.14) 0%, transparent 55%), var(--bg);
  color: var(--text);
}

.sl-15 *,
.sl-15 *::before,
.sl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-15 ::selection {
  background: var(--purple);
  color: #fff;
}

.sl-15__inner {
  max-width: 720px;
  text-align: center;
}

.sl-15__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(34,197,94,.14);
  border: 1px solid rgba(34,197,94,.3);
  font-size: .78rem;
  font-weight: 600;
  color: #a7f3d0;
  margin-bottom: 24px;
  opacity: 0;
  transform: translateY(30px);
  animation: sl-15-slide .6s cubic-bezier(.22,1,.36,1) .1s forwards;
}

.sl-15__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--good);
  box-shadow: 0 0 8px rgba(34,197,94,.7);
  animation: sl-15-pulse 2s ease-in-out infinite;
}

.sl-15__headline {
  font-size: clamp(2.2rem,5.5vw,3.6rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.05;
  margin-bottom: 22px;
  opacity: 0;
  transform: translateY(30px);
  animation: sl-15-slide .6s cubic-bezier(.22,1,.36,1) .3s forwards;
}

.sl-15__headline span {
  background: linear-gradient(135deg,var(--purple),var(--pink));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.sl-15__sub {
  font-size: 1.1rem;
  color: var(--sub);
  line-height: 1.55;
  max-width: 560px;
  margin: 0 auto 32px;
  opacity: 0;
  transform: translateY(30px);
  animation: sl-15-slide .6s cubic-bezier(.22,1,.36,1) .5s forwards;
}

.sl-15__cta {
  display: inline-flex;
  gap: 12px;
  align-items: center;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 48px;
  opacity: 0;
  transform: translateY(30px);
  animation: sl-15-slide .6s cubic-bezier(.22,1,.36,1) .7s forwards;
}

.sl-15__btn {
  padding: 13px 26px;
  border: none;
  border-radius: 10px;
  font-family: inherit;
  font-size: .95rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform .12s ease,box-shadow .18s ease;
}

.sl-15__btn--primary {
  background: linear-gradient(135deg,var(--purple),var(--pink));
  color: #fff;
  box-shadow: 0 12px 28px -8px rgba(168,85,247,.55);
}

.sl-15__btn--primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 32px -8px rgba(168,85,247,.7);
}

.sl-15__btn--ghost {
  background: rgba(255,255,255,.05);
  color: var(--text);
  border: 1px solid rgba(255,255,255,.14);
}

.sl-15__btn--ghost:hover {
  background: rgba(255,255,255,.09);
}

.sl-15__proof {
  opacity: 0;
  transform: translateY(30px);
  animation: sl-15-slide .6s cubic-bezier(.22,1,.36,1) .9s forwards;
}

.sl-15__proof-label {
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 14px;
}

.sl-15__logos {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 26px;
  opacity: .4;
}

.sl-15__logos span {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .85rem;
  font-weight: 700;
  letter-spacing: .08em;
  color: var(--text);
}

@keyframes sl-15-slide {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes sl-15-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: .9;
  }

  50% {
    transform: scale(1.4);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-15 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
