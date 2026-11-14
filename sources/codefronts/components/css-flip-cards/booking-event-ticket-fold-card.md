---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/booking-event-ticket-fold-card/"
title: "Booking Event Ticket Fold Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A concert ticket split into two halves that bi-fold inward like a book page, each half rotating around its centre edge to reveal the ticket details on the back."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Booking Event Ticket Fold Card
Source: https://codefronts.com/components/css-flip-cards/booking-event-ticket-fold-card/

A concert ticket split into two halves that bi-fold inward like a book page, each half rotating around its centre edge to reveal the ticket details on the back.
## HTML
```html
<div class="fc-22">
  <div class="fc-22__scene">
    <div class="fc-22__book">

      <!-- LEFT HALF -->
      <div class="fc-22__half fc-22__half--left">
        <!-- FRONT face -->
        <div class="fc-22__front-left">
          <div class="fc-22__event-cat">Live Concert · 2025</div>
          <div class="fc-22__event-name">Neon Pulse<br>World Tour</div>
          <div class="fc-22__event-sub">The Meridian Arena · San Francisco</div>
          <div class="fc-22__meta-row">
            <div class="fc-22__meta">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
              Sat, Nov 29 · 8:00 PM
            </div>
          </div>
          <div class="fc-22__meta-row">
            <div class="fc-22__meta">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              Floor · General Admission
            </div>
          </div>
        </div>
        <!-- BACK face (rotated 180deg inside) -->
        <div class="fc-22__back-left">
          <div class="fc-22__back-cat">Ticket Details</div>
          <div class="fc-22__back-title">Neon Pulse · SF</div>
          <div class="fc-22__detail-grid">
            <div class="fc-22__detail-item">
              <div class="fc-22__di-label">Date</div>
              <div class="fc-22__di-val">Nov 29</div>
            </div>
            <div class="fc-22__detail-item">
              <div class="fc-22__di-label">Doors</div>
              <div class="fc-22__di-val fc-22__di-val--sky">6:30 PM</div>
            </div>
            <div class="fc-22__detail-item">
              <div class="fc-22__di-label">Zone</div>
              <div class="fc-22__di-val">Floor A</div>
            </div>
            <div class="fc-22__detail-item">
              <div class="fc-22__di-label">Price</div>
              <div class="fc-22__di-val fc-22__di-val--sky">$149</div>
            </div>
          </div>
        </div>
      </div><!-- /left half -->

      <!-- RIGHT HALF (stub) -->
      <div class="fc-22__half fc-22__half--right">
        <div class="fc-22__perfs">
          <div class="fc-22__perf"></div>
          <div class="fc-22__perf"></div>
          <div class="fc-22__perf"></div>
          <div class="fc-22__perf"></div>
          <div class="fc-22__perf"></div>
        </div>
        <!-- FRONT stub -->
        <div class="fc-22__front-right">
          <div class="fc-22__qr-wrap">
            <!-- mini QR SVG -->
            <svg viewBox="0 0 17 17" width="56" height="56" fill="black">
              <rect x="0" y="0" width="5" height="5" fill="none" stroke="black" stroke-width=".8"/>
              <rect x="1.5" y="1.5" width="2" height="2"/>
              <rect x="12" y="0" width="5" height="5" fill="none" stroke="black" stroke-width=".8"/>
              <rect x="13.5" y="1.5" width="2" height="2"/>
              <rect x="0" y="12" width="5" height="5" fill="none" stroke="black" stroke-width=".8"/>
              <rect x="1.5" y="13.5" width="2" height="2"/>
              <rect x="6" y="0" width="1" height="1"/><rect x="7" y="1" width="1" height="1"/>
              <rect x="9" y="0" width="1" height="1"/><rect x="10" y="1" width="1" height="1"/>
              <rect x="6" y="2" width="2" height="1"/><rect x="9" y="3" width="1" height="1"/>
              <rect x="6" y="6" width="1" height="1"/><rect x="8" y="6" width="1" height="1"/><rect x="10" y="6" width="1" height="1"/>
              <rect x="7" y="7" width="2" height="1"/><rect x="11" y="7" width="1" height="1"/>
              <rect x="6" y="8" width="1" height="1"/><rect x="9" y="8" width="1" height="1"/><rect x="12" y="8" width="1" height="1"/>
              <rect x="6" y="10" width="2" height="1"/><rect x="10" y="10" width="1" height="1"/>
              <rect x="7" y="12" width="1" height="1"/><rect x="9" y="12" width="1" height="1"/><rect x="11" y="12" width="1" height="1"/>
              <rect x="6" y="13" width="1" height="1"/><rect x="10" y="13" width="2" height="1"/>
              <rect x="6" y="15" width="1" height="1"/><rect x="8" y="15" width="1" height="1"/><rect x="11" y="15" width="1" height="1"/>
              <rect x="12" y="6" width="5" height="5" fill="none" stroke="black" stroke-width=".8"/>
              <rect x="13.5" y="7.5" width="2" height="2"/>
            </svg>
          </div>
          <div class="fc-22__seat">B14</div>
          <div class="fc-22__seat-label">Seat</div>
          <div class="fc-22__stub-label">Scan at entry</div>
        </div>
        <!-- BACK stub -->
        <div class="fc-22__back-right">
          <div class="fc-22__barcode">
            <div class="fc-22__bar" style="width:2px;height:52px"></div>
            <div class="fc-22__bar" style="width:3px;height:40px"></div>
            <div class="fc-22__bar" style="width:2px;height:52px"></div>
            <div class="fc-22__bar" style="width:1px;height:32px"></div>
            <div class="fc-22__bar" style="width:3px;height:48px"></div>
            <div class="fc-22__bar" style="width:2px;height:44px"></div>
            <div class="fc-22__bar" style="width:1px;height:52px"></div>
            <div class="fc-22__bar" style="width:2px;height:36px"></div>
            <div class="fc-22__bar" style="width:3px;height:52px"></div>
            <div class="fc-22__bar" style="width:1px;height:44px"></div>
            <div class="fc-22__bar" style="width:2px;height:40px"></div>
            <div class="fc-22__bar" style="width:3px;height:52px"></div>
            <div class="fc-22__bar" style="width:1px;height:34px"></div>
            <div class="fc-22__bar" style="width:2px;height:48px"></div>
          </div>
          <div class="fc-22__barcode-num">4829-1104-B14</div>
          <div class="fc-22__back-seat">B14</div>
          <div class="fc-22__back-seat-label">Confirmed Seat</div>
          <div class="fc-22__valid-badge">
            <span class="fc-22__valid-dot"></span>Valid Entry
          </div>
        </div>
      </div><!-- /right half -->

      <div class="fc-22__spine"></div>
    </div><!-- /book -->
    <div class="fc-22__fold-hint">Hover to unfold</div>
  </div><!-- /scene -->
</div>
```
## CSS
```css
.fc-22,
.fc-22 *,
.fc-22 *::before,
.fc-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-22 ::selection {
  background: #f97316;
  color: #fff;
}

.fc-22 {
  --bg: #07080f;
  --orange: #f97316;
  --amber: #fbbf24;
  --sky: #38bdf8;
  --rose: #fb7185;
  --white: #fff7ed;
  --card-w: 420px;
  --card-h: 200px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 30%,#1a0e00,#07080f 65%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 28px;
  color: var(--white);
}
/* ══════════════════════════════════════════
   PAGE-FOLD MECHANISM
   The card is split into LEFT half and RIGHT half.
   Each half is a flex child inside the card wrapper.
   On hover:
     • Left half rotates  rotateY(-180deg) around its RIGHT edge  (transform-origin: right)
     • Right half rotates rotateY( 180deg) around its LEFT  edge  (transform-origin: left)
   Both use preserve-3d so their ::before back-faces show through.
   Result: a bi-fold page-turn that meets in the middle.
══════════════════════════════════════════ */

.fc-22__scene {
  width: var(--card-w);
  height: var(--card-h);
  position: relative;
  /* perspective on the scene keeps both halves in one shared 3D space */
  perspective: 1400px;
  perspective-origin: 50% 50%;
  cursor: pointer;
}
/* Outer wrapper — just a flex row holding the two halves */

.fc-22__book {
  width: 100%;
  height: 100%;
  display: flex;
  position: relative;
}
/* ── shared half styles ── */

.fc-22__half {
  width: 50%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}
/* LEFT half pivots around its right edge. Background/border now live
   on each face div (front/back) — keeping them on the half itself would
   show as a solid coloured rectangle through transparent regions when
   the half rotates 180°. */

.fc-22__half--left {
  transform-origin: right center;
}
/* RIGHT half pivots around its left edge. Background/border on each
   face div (front/back) — see comment on --left above. */

.fc-22__half--right {
  transform-origin: left center;
}
/* On hover: left folds away (rotates around right edge by -180deg),
             right folds away (rotates around left edge by +180deg) */

.fc-22__scene:hover .fc-22__half--left {
  transform: rotateY(-180deg);
}

.fc-22__scene:hover .fc-22__half--right {
  transform: rotateY(180deg);
}
/* ── FRONT content — lives on the element itself (z-index front face) ── */

.fc-22__front-left {
  position: absolute;
  inset: 0;
  background: linear-gradient(160deg,#1e1000,#120900);
  border: 1px solid rgba(249,115,22,.25);
  border-right: none;
  border-radius: 12px 0 0 12px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 20px 20px 20px 24px;
  gap: 8px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.fc-22__front-right {
  position: absolute;
  inset: 0;
  background: linear-gradient(160deg,#120900,#0d0700);
  border: 1px solid rgba(249,115,22,.25);
  border-left: 1px dashed rgba(249,115,22,.3);
  border-radius: 0 12px 12px 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 16px;
  gap: 10px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}
/* ── BACK content — ::before pseudo, pre-rotated 180deg so it faces inward ── */
/* Back content lives in .fc-22__back-* divs pre-rotated 180deg. */

.fc-22__back-left,
.fc-22__back-right {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.fc-22__back-left {
  background: linear-gradient(160deg,#0a1a28,#061020);
  border-radius: 12px 0 0 12px;
  padding: 20px 18px 20px 24px;
  gap: 8px;
  border-right: 1px dashed rgba(56,189,248,.3);
}

.fc-22__back-right {
  background: linear-gradient(160deg,#061020,#04090f);
  border-radius: 0 12px 12px 0;
  padding: 16px;
  gap: 10px;
  align-items: center;
}
/* ── FRONT — left content ── */

.fc-22__event-cat {
  font-size: 9px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--orange);
  font-weight: 700;
}

.fc-22__event-name {
  font-size: 19px;
  font-weight: 900;
  color: var(--white);
  line-height: 1.15;
}

.fc-22__event-sub {
  font-size: 11px;
  color: rgba(255,247,237,.5);
}

.fc-22__meta-row {
  display: flex;
  gap: 14px;
  margin-top: 4px;
}

.fc-22__meta {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  color: rgba(255,247,237,.55);
}

.fc-22__meta svg {
  flex-shrink: 0;
  opacity: .7;
}
/* ── FRONT — right content (stub) ── */

.fc-22__qr-wrap {
  width: 68px;
  height: 68px;
  background: #fff;
  border-radius: 8px;
  padding: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fc-22__stub-label {
  font-size: 9px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(255,247,237,.35);
  text-align: center;
}

.fc-22__seat {
  font-size: 22px;
  font-weight: 900;
  color: var(--amber);
  text-align: center;
  line-height: 1;
}

.fc-22__seat-label {
  font-size: 9px;
  color: rgba(255,247,237,.35);
  letter-spacing: .1em;
  text-transform: uppercase;
}

.fc-22__fold-hint {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 9px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,247,237,.2);
  white-space: nowrap;
}
/* ── BACK — left content ── */

.fc-22__back-cat {
  font-size: 9px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--sky);
  font-weight: 700;
}

.fc-22__back-title {
  font-size: 17px;
  font-weight: 900;
  color: var(--white);
  line-height: 1.2;
}

.fc-22__detail-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-top: 4px;
}

.fc-22__detail-item {
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 8px;
  padding: 8px 10px;
}

.fc-22__di-label {
  font-size: 9px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,247,237,.35);
  margin-bottom: 2px;
}

.fc-22__di-val {
  font-size: 13px;
  font-weight: 700;
  color: var(--white);
}

.fc-22__di-val--sky {
  color: var(--sky);
}
/* ── BACK — right content ── */

.fc-22__barcode {
  display: flex;
  gap: 2px;
  align-items: flex-end;
  height: 52px;
}

.fc-22__bar {
  border-radius: 1px;
  background: var(--white);
}

.fc-22__barcode-num {
  font-size: 9px;
  letter-spacing: .08em;
  color: rgba(255,247,237,.35);
  font-family: 'Courier New',monospace;
  margin-top: 4px;
}

.fc-22__back-seat {
  font-size: 28px;
  font-weight: 900;
  color: var(--sky);
  line-height: 1;
}

.fc-22__back-seat-label {
  font-size: 9px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(255,247,237,.35);
}

.fc-22__valid-badge {
  display: flex;
  align-items: center;
  gap: 5px;
  background: rgba(56,189,248,.1);
  border: 1px solid rgba(56,189,248,.25);
  border-radius: 20px;
  padding: 4px 10px;
  font-size: 10px;
  font-weight: 700;
  color: var(--sky);
}

.fc-22__valid-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--sky);
}
/* Centre join shadow — gives the fold a spine */

.fc-22__spine {
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(180deg,transparent,rgba(249,115,22,.25),transparent);
  transform: translateX(-50%);
  pointer-events: none;
  z-index: 10;
}
/* Perforations on the right half left edge */

.fc-22__perfs {
  position: absolute;
  left: -1px;
  top: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 10px 0;
  pointer-events: none;
  z-index: 5;
}

.fc-22__perf {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--bg);
  border: 1px solid rgba(249,115,22,.2);
  margin-left: -5px;
}

@media (max-width: 480px) {
  .fc-22 {
    --card-w: 340px;
    --card-h: 180px;
  }

  .fc-22__event-name {
    font-size: 15px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fc-22__half--left,
    .fc-22__half--right {
    transition: none;
  }
}
```
