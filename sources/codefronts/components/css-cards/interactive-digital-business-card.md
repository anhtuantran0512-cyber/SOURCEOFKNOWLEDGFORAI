---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/interactive-digital-business-card/"
title: "Interactive Digital Business Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Landscape vCard: 48px avatar + name/role on the left, address block with tap-to-email + tap-to-call and a Save vCard pill on the right."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Digital Business Card
Source: https://codefronts.com/components/css-cards/interactive-digital-business-card/

Landscape vCard: 48px avatar + name/role on the left, address block with tap-to-email + tap-to-call and a Save vCard pill on the right. Radial accent glow top-right.
## HTML
```html
<section class="card-13">
  <article class="card-13__card">
    <div class="card-13__sheen" aria-hidden="true"></div>
    <div class="card-13__mesh" aria-hidden="true"></div>
    <header class="card-13__head">
      <div class="card-13__brand">
        <span class="card-13__mark" aria-hidden="true"></span>
        <span class="card-13__brandname">SASHA LIN</span>
      </div>
      <span class="card-13__status">
        <span class="card-13__statusdot" aria-hidden="true"></span>
        Open to opportunities
      </span>
    </header>
    <div class="card-13__body">
      <h3 class="card-13__name">
        Sasha Lin
        <svg class="card-13__verified" aria-label="Verified" role="img" width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M12 2L14 4L17 3L18 6L21 7L20 10L22 12L20 14L21 17L18 18L17 21L14 20L12 22L10 20L7 21L6 18L3 17L4 14L2 12L4 10L3 7L6 6L7 3L10 4Z" fill="#a5b4fc"/><path d="M9 12L11 14L15 10" stroke="#0a0b12" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </h3>
      <p class="card-13__role">Head of Partnerships &middot; Stripe</p>
      <p class="card-13__bio">Helping fintechs ship revenue infrastructure. Previously YC, Notion.</p>
      <ul class="card-13__chips" aria-label="Focus areas">
        <li>Fintech</li>
        <li>Product</li>
        <li>Growth</li>
      </ul>
    </div>
    <footer class="card-13__foot">
      <div class="card-13__actions">
        <a class="card-13__cta" href="#connect">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 12h8M12 8v8"/></svg>
          Connect
        </a>
        <a class="card-13__save" href="#vcard" aria-label="Save vCard">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        </a>
      </div>
      <div class="card-13__social" aria-label="Social links">
        <a href="mailto:[email protected]" aria-label="Email">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3,7 12,13 21,7"/></svg>
        </a>
        <a href="#linkedin" aria-label="LinkedIn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.03-1.85-3.03-1.85 0-2.13 1.44-2.13 2.94v5.66H9.37V9h3.4v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.46zM5.34 7.43c-1.14 0-2.06-.93-2.06-2.06 0-1.14.93-2.06 2.06-2.06 1.14 0 2.06.93 2.06 2.06.01 1.14-.92 2.06-2.06 2.06zm1.78 13.02H3.56V9h3.55v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.22.79 24 1.77 24h20.45c.99 0 1.78-.78 1.78-1.73V1.73C24 .77 23.21 0 22.22 0z"/></svg>
        </a>
        <a href="#twitter" aria-label="X">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </a>
      </div>
    </footer>
    <div class="card-13__qr" aria-hidden="true">
      <div class="card-13__qr-inner">
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.card-13 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 30% 20%, rgba(165, 180, 252, 0.08) 0%, transparent 50%), radial-gradient(ellipse at 80% 80%, rgba(236, 72, 153, 0.06) 0%, transparent 50%), #05060d;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #a5b4fc;
  --accent: #a5b4fc;
  --accent-2: #f472b6;
}

.card-13 *,
.card-13 *::before,
.card-13 *::after {
  box-sizing: border-box;
}

.card-13__card {
  position: relative;
  width: 100%;
  max-width: 360px;
  min-height: 220px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.02) 0%, transparent 40%), linear-gradient(160deg, #14152a 0%, #0d0e1c 100%);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 20px;
  padding: 22px 22px 18px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.02) inset, 0 1px 0 rgba(255, 255, 255, 0.05) inset;
  isolation: isolate;
  transition: transform 0.35s ease, box-shadow 0.35s;
}

.card-13__card:hover {
  transform: translateY(-2px);
  box-shadow: 0 40px 70px -30px rgba(0, 0, 0, 0.9), 0 0 0 1px rgba(165, 180, 252, 0.14) inset, 0 1px 0 rgba(255, 255, 255, 0.05) inset;
}
/* Iridescent diagonal sheen */

.card-13__sheen {
  position: absolute;
  top: -50%;
  left: -20%;
  width: 60%;
  height: 200%;
  background: linear-gradient(115deg,
      transparent 30%,
      rgba(165, 180, 252, 0.06) 45%,
      rgba(244, 114, 182, 0.05) 50%,
      rgba(34, 211, 238, 0.06) 55%,
      transparent 70%);
  transform: rotate(15deg);
  pointer-events: none;
  z-index: 0;
}
/* Corner mesh gradient */

.card-13__mesh {
  position: absolute;
  top: -60px;
  right: -60px;
  width: 220px;
  height: 220px;
  background: radial-gradient(circle at 30% 30%, rgba(165, 180, 252, 0.32) 0%, transparent 55%), radial-gradient(circle at 60% 70%, rgba(244, 114, 182, 0.18) 0%, transparent 55%);
  filter: blur(24px);
  pointer-events: none;
  z-index: 0;
}
/* All content above the sheen/mesh */

.card-13__head,
.card-13__body,
.card-13__foot,
.card-13__qr {
  position: relative;
  z-index: 1;
}

.card-13__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.card-13__brand {
  display: flex;
  align-items: center;
  gap: 8px;
}

.card-13__mark {
  position: relative;
  width: 22px;
  height: 22px;
  border-radius: 7px;
  background: linear-gradient(135deg, #a5b4fc 0%, #6366f1 50%, #4338ca 100%);
  box-shadow: 0 0 0 1px rgba(165, 180, 252, 0.35), 0 4px 12px rgba(99, 102, 241, 0.35);
}

.card-13__mark::after {
  content: '';
  position: absolute;
  inset: 4px;
  border-radius: 4px;
  background: linear-gradient(135deg, transparent 40%, rgba(255, 255, 255, 0.4) 55%, transparent 65%);
}

.card-13__brandname {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: rgba(255, 255, 255, 0.85);
}

.card-13__status {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 10px;
  font-weight: 500;
  color: #a1a1aa;
  padding: 4px 8px;
  background: rgba(52, 211, 153, 0.10);
  border: 1px solid rgba(52, 211, 153, 0.22);
  border-radius: 999px;
}

.card-13__statusdot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #34d399;
  box-shadow: 0 0 8px #34d399;
  animation: card-13-pulse 2.4s ease-in-out infinite;
}

.card-13__body {
  margin-bottom: 18px;
}

.card-13__name {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 24px;
  font-weight: 700;
  color: #fafafa;
  margin: 0 0 4px;
  letter-spacing: -0.02em;
  line-height: 1.1;
  background: linear-gradient(180deg, #ffffff 0%, #d4d4de 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-13__verified {
  flex-shrink: 0;
}

.card-13__role {
  font-size: 12.5px;
  font-weight: 500;
  color: #d4d4d8;
  margin: 0 0 8px;
}

.card-13__bio {
  font-size: 12px;
  color: #a1a1aa;
  margin: 0 0 12px;
  line-height: 1.5;
}

.card-13__chips {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.card-13__chips li {
  font-size: 10.5px;
  font-weight: 600;
  color: #c7d2fe;
  padding: 3px 9px;
  background: rgba(165, 180, 252, 0.10);
  border: 1px solid rgba(165, 180, 252, 0.18);
  border-radius: 999px;
  letter-spacing: 0.01em;
}

.card-13__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.card-13__actions {
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-13__cta {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-height: 36px;
  padding: 8px 14px;
  background: linear-gradient(180deg, #ecfdf5 0%, #a5b4fc 100%);
  color: #06070c;
  text-decoration: none;
  font-size: 12px;
  font-weight: 700;
  border-radius: 999px;
  box-shadow: 0 4px 12px rgba(165, 180, 252, 0.28), 0 0 0 1px rgba(255, 255, 255, 0.14) inset;
  transition: transform 0.18s, box-shadow 0.18s;
  letter-spacing: -0.005em;
}

.card-13__cta:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(165, 180, 252, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.2) inset;
}

.card-13__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-13__save {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.05);
  color: #d4d4d8;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 50%;
  text-decoration: none;
  transition: background 0.18s, color 0.18s, border-color 0.18s;
}

.card-13__save:hover {
  background: rgba(165, 180, 252, 0.12);
  color: var(--accent);
  border-color: rgba(165, 180, 252, 0.32);
}

.card-13__save:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-13__social {
  display: flex;
  align-items: center;
  gap: 4px;
}

.card-13__social a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  color: #71717a;
  border-radius: 8px;
  text-decoration: none;
  transition: color 0.18s, background 0.18s;
}

.card-13__social a:hover {
  color: var(--accent);
  background: rgba(255, 255, 255, 0.04);
}

.card-13__social a:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* Decorative QR icon in top-right */

.card-13__qr {
  position: absolute;
  top: 22px;
  right: 22px;
  width: 40px;
  height: 40px;
  padding: 4px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  display: none;
}

.card-13__qr-inner {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(5, 1fr);
  gap: 1px;
}

.card-13__qr-inner span {
  background: rgba(255, 255, 255, 0.6);
  border-radius: 1px;
}
/* Random QR checkerboard pattern */

.card-13__qr-inner span:nth-child(2n) {
  background: transparent;
}

.card-13__qr-inner span:nth-child(3n) {
  background: rgba(255, 255, 255, 0.55);
}

.card-13__qr-inner span:nth-child(4n) {
  background: transparent;
}

.card-13__qr-inner span:nth-child(1),
.card-13__qr-inner span:nth-child(5),
.card-13__qr-inner span:nth-child(21),
.card-13__qr-inner span:nth-child(25) {
  background: rgba(255, 255, 255, 0.7);
}

@keyframes card-13-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-13__statusdot {
    animation: none;
  }

  .card-13__card,
    .card-13__cta,
    .card-13__save,
    .card-13__social a {
    transition: none;
  }

  .card-13__card:hover {
    transform: none;
  }

  .card-13__cta:hover {
    transform: none;
  }
}
```
