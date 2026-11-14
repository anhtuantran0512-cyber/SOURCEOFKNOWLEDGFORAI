---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/digital-business-card-vcard/"
title: "Digital Business Card VCard"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front shows a minimalist corporate name card with a holographic accent strip; back provides structured phone, email, and location contacts plus a decorative…"
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Digital Business Card VCard
Source: https://codefronts.com/components/css-flip-cards/digital-business-card-vcard/

Front shows a minimalist corporate name card with a holographic accent strip; back provides structured phone, email, and location contacts plus a decorative QR code.
## HTML
```html
<div class="fc-12">
  <div class="fc-12__label">Digital Business Card · Hover to flip</div>
  <div class="fc-12__scene">
    <div class="fc-12__card">
      <div class="fc-12__front">
        <div class="fc-12__holo"></div>
        <div class="fc-12__logo-mark">JD</div>
        <div class="fc-12__front-info">
          <div class="fc-12__person-name">James Dorian</div>
          <div class="fc-12__person-role">Chief Technology Officer</div>
          <div class="fc-12__divider-h"></div>
          <div class="fc-12__company">Nova Systems Inc.</div>
          <div class="fc-12__contact-mini">
            <div class="fc-12__cm"><span class="fc-12__cm-dot"></span>+1 (415) 555-0198</div>
            <div class="fc-12__cm"><span class="fc-12__cm-dot"></span>[email protected]</div>
          </div>
        </div>
        <div class="fc-12__front-hint">Hover →</div>
      </div>
      <div class="fc-12__back">
        <div class="fc-12__contact-grid">
          <div class="fc-12__contact-item">
            <div class="fc-12__ci-icon"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.43 2 2 0 0 1 3.6 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.6a16 16 0 0 0 6 6l.92-.92a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.73 16z"/></svg></div>
            <div class="fc-12__ci-text"><span class="fc-12__ci-label">Phone</span><span class="fc-12__ci-val">+1 (415) 555-0198</span></div>
          </div>
          <div class="fc-12__contact-item">
            <div class="fc-12__ci-icon"><svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/></svg></div>
            <div class="fc-12__ci-text"><span class="fc-12__ci-label">Email</span><span class="fc-12__ci-val">[email protected]</span></div>
          </div>
          <div class="fc-12__contact-item">
            <div class="fc-12__ci-icon"><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
            <div class="fc-12__ci-text"><span class="fc-12__ci-label">Office</span><span class="fc-12__ci-val">SF · Floor 22</span></div>
          </div>
        </div>
        <div class="fc-12__qr">
          <!-- QR code as SVG pattern -->
          <svg viewBox="0 0 21 21" fill="black">
            <!-- position detection patterns -->
            <rect x="0" y="0" width="7" height="7" fill="none" stroke="black" stroke-width="1"/>
            <rect x="2" y="2" width="3" height="3"/>
            <rect x="14" y="0" width="7" height="7" fill="none" stroke="black" stroke-width="1"/>
            <rect x="16" y="2" width="3" height="3"/>
            <rect x="0" y="14" width="7" height="7" fill="none" stroke="black" stroke-width="1"/>
            <rect x="2" y="16" width="3" height="3"/>
            <!-- data modules (decorative) -->
            <rect x="8" y="0" width="1" height="1"/><rect x="10" y="0" width="1" height="1"/><rect x="12" y="0" width="1" height="1"/>
            <rect x="9" y="2" width="1" height="1"/><rect x="11" y="2" width="1" height="1"/>
            <rect x="8" y="4" width="1" height="1"/><rect x="10" y="4" width="2" height="1"/><rect x="13" y="4" width="1" height="1"/>
            <rect x="7" y="7" width="1" height="1"/><rect x="9" y="7" width="2" height="1"/><rect x="12" y="7" width="1" height="1"/>
            <rect x="7" y="9" width="2" height="1"/><rect x="11" y="9" width="1" height="1"/><rect x="13" y="9" width="1" height="1"/>
            <rect x="8" y="11" width="1" height="1"/><rect x="10" y="11" width="2" height="1"/><rect x="14" y="11" width="1" height="1"/>
            <rect x="7" y="13" width="1" height="1"/><rect x="9" y="13" width="1" height="1"/><rect x="12" y="13" width="2" height="1"/>
            <rect x="8" y="14" width="2" height="1"/><rect x="12" y="14" width="1" height="1"/><rect x="14" y="14" width="1" height="1"/>
            <rect x="9" y="16" width="1" height="1"/><rect x="11" y="16" width="3" height="1"/>
            <rect x="8" y="18" width="2" height="1"/><rect x="12" y="18" width="1" height="1"/><rect x="14" y="18" width="1" height="1"/>
            <rect x="9" y="20" width="1" height="1"/><rect x="11" y="20" width="2" height="1"/><rect x="14" y="20" width="1" height="1"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-12,
.fc-12 *,
.fc-12 *::before,
.fc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-12 ::selection {
  background: #0891b2;
  color: #fff;
}

.fc-12 {
  --bg: #04080c;
  --cyan: #06b6d4;
  --slate: #94a3b8;
  --white: #f0f9ff;
  --card-w: 360px;
  --card-h: 220px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 60%,#040e18,#04080c 65%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 16px;
  color: var(--white);
}

.fc-12__label {
  font-size: 10px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(148,163,184,.4);
  font-weight: 600;
}

.fc-12__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-12__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fc-12__scene:hover .fc-12__card {
  transform: rotateY(180deg);
}

.fc-12__front,
.fc-12__back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-12__front {
  background: linear-gradient(135deg,#0a1520,#040e18);
  border: 1px solid rgba(6,182,212,.25);
  display: flex;
  align-items: center;
  padding: 24px 28px;
  gap: 20px;
  box-shadow: 0 0 40px rgba(6,182,212,.06);
}

.fc-12__front::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 160px;
  height: 100%;
  background: linear-gradient(to left,rgba(6,182,212,.05),transparent);
  pointer-events: none;
}
/* holographic strip */

.fc-12__holo {
  position: absolute;
  top: 0;
  right: 60px;
  width: 4px;
  height: 100%;
  background: linear-gradient(180deg,transparent,rgba(6,182,212,.4),rgba(139,92,246,.4),rgba(236,72,153,.4),transparent);
}

.fc-12__logo-mark {
  width: 60px;
  height: 60px;
  border-radius: 14px;
  flex-shrink: 0;
  background: linear-gradient(135deg,#0891b2,#0e7490);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  font-weight: 900;
  color: #fff;
  box-shadow: 0 0 20px rgba(6,182,212,.3);
}

.fc-12__front-info {
  flex: 1;
}

.fc-12__person-name {
  font-size: 20px;
  font-weight: 800;
  color: var(--white);
}

.fc-12__person-role {
  font-size: 11px;
  color: var(--cyan);
  font-weight: 600;
  letter-spacing: .06em;
  margin-top: 2px;
}

.fc-12__divider-h {
  height: 1px;
  background: rgba(255,255,255,.08);
  margin: 10px 0;
}

.fc-12__company {
  font-size: 13px;
  color: rgba(240,249,255,.6);
}

.fc-12__contact-mini {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-top: 8px;
}

.fc-12__cm {
  font-size: 11px;
  color: rgba(240,249,255,.4);
  display: flex;
  align-items: center;
  gap: 5px;
}

.fc-12__cm-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--cyan);
  opacity: .6;
}

.fc-12__front-hint {
  position: absolute;
  bottom: 12px;
  right: 16px;
  font-size: 9px;
  color: rgba(240,249,255,.2);
  letter-spacing: .08em;
}
/* BACK */

.fc-12__back {
  background: linear-gradient(135deg,#060e18,#040a12);
  border: 1px solid rgba(6,182,212,.2);
  transform: rotateY(180deg);
  display: flex;
  align-items: center;
  padding: 20px 24px;
  gap: 20px;
}

.fc-12__contact-grid {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.fc-12__contact-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.fc-12__ci-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: rgba(6,182,212,.1);
  border: 1px solid rgba(6,182,212,.2);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.fc-12__ci-icon svg {
  width: 14px;
  height: 14px;
  stroke: var(--cyan);
  stroke-width: 1.8;
  fill: none;
}

.fc-12__ci-text {
  display: flex;
  flex-direction: column;
}

.fc-12__ci-label {
  font-size: 9px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(240,249,255,.35);
}

.fc-12__ci-val {
  font-size: 12px;
  color: rgba(240,249,255,.8);
  font-weight: 600;
}

.fc-12__qr {
  width: 100px;
  height: 100px;
  border-radius: 10px;
  flex-shrink: 0;
  background: white;
  padding: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fc-12__qr svg {
  width: 100%;
  height: 100%;
}

@media (prefers-reduced-motion: reduce) {
  .fc-12__card {
    transition: none;
  }
}
```
