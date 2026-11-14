---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/3d-pop-out-character-card/"
title: "3D Pop-Out Character Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Sneaker product tile with a resting 3D tilt. On hover the card tilts further and the CSS-drawn sneaker pops up out of the frame with a widening shadow."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Pop-Out Character Card
Source: https://codefronts.com/components/css-cards/3d-pop-out-character-card/

Sneaker product tile with a resting 3D tilt. On hover the card tilts further and the CSS-drawn sneaker pops up out of the frame with a widening shadow.
## HTML
```html
<section class="card-19">
  <div class="card-19__stage" aria-hidden="true">
    <div class="card-19__stage-glow"></div>
    <div class="card-19__stage-grid"></div>
  </div>

  <article class="card-19__card">
    <div class="card-19__hero">
      <div class="card-19__hero-bg" aria-hidden="true"></div>
      <div class="card-19__hero-turntable" aria-hidden="true">
        <div class="card-19__turntable-ring"></div>
        <div class="card-19__turntable-ring card-19__turntable-ring--2"></div>
      </div>

      <div class="card-19__badges">
        <span class="card-19__badge card-19__badge--drop">
          <span class="card-19__badge-dot" aria-hidden="true"></span>
          LIVE DROP
        </span>
        <span class="card-19__badge card-19__badge--ar">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          AR
        </span>
      </div>

      <button type="button" class="card-19__wish" aria-label="Add to wishlist">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
      </button>

      <img class="card-19__sneaker" src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&q=85&auto=format&fit=crop" alt="Nova Runner 04 Cloudmist sneaker" loading="lazy" decoding="async">
      <div class="card-19__shadow" aria-hidden="true"></div>

      <div class="card-19__angles" aria-label="View angles">
        <span class="card-19__angle card-19__angle--active"></span>
        <span class="card-19__angle"></span>
        <span class="card-19__angle"></span>
        <span class="card-19__angle"></span>
        <span class="card-19__angle-count">1 / 4</span>
      </div>

      <div class="card-19__spec">
        <span class="card-19__spec-label">DROP CLOSES</span>
        <span class="card-19__spec-val">
          <span>02</span><em>H</em><span>47</span><em>M</em><span>13</span><em>S</em>
        </span>
      </div>
    </div>

    <div class="card-19__body">
      <div class="card-19__title-row">
        <div>
          <p class="card-19__chip">SNEAKERS · NEW DROP · SS27</p>
          <h3 class="card-19__title">Nova Runner 04 <span class="card-19__title-color">· Cloudmist</span></h3>
          <div class="card-19__rating">
            <div class="card-19__stars" aria-hidden="true">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            </div>
            <span class="card-19__rating-num">4.9</span>
            <span class="card-19__rating-count">· 2,847 reservations</span>
          </div>
        </div>
        <div class="card-19__price-block">
          <span class="card-19__price">$189</span>
          <span class="card-19__price-note">
            or 4× $47<span class="card-19__price-note-brand">·klarna</span>
          </span>
        </div>
      </div>

      <ul class="card-19__tags">
        <li><span class="card-19__tag-dot" aria-hidden="true"></span>Ethical</li>
        <li>Portugal-made</li>
        <li>Recycled 62%</li>
      </ul>

      <div class="card-19__colors">
        <span class="card-19__colors-label">
          COLOR
          <em class="card-19__colors-name">Cloudmist</em>
        </span>
        <div class="card-19__swatches">
          <button type="button" class="card-19__swatch card-19__swatch--active" aria-label="Cloudmist"><span class="card-19__swatch-c" style="background:linear-gradient(135deg,#e5e7eb,#f9fafb)"></span></button>
          <button type="button" class="card-19__swatch" aria-label="Ember"><span class="card-19__swatch-c" style="background:linear-gradient(135deg,#ea580c,#7c2d12)"></span></button>
          <button type="button" class="card-19__swatch" aria-label="Midnight"><span class="card-19__swatch-c" style="background:linear-gradient(135deg,#1e293b,#0f172a)"></span></button>
          <button type="button" class="card-19__swatch" aria-label="Amethyst"><span class="card-19__swatch-c" style="background:linear-gradient(135deg,#a855f7,#4c1d95)"></span></button>
          <button type="button" class="card-19__swatch card-19__swatch--soldout" aria-label="Sage — sold out"><span class="card-19__swatch-c" style="background:linear-gradient(135deg,#84cc16,#365314)"></span></button>
        </div>
      </div>

      <div class="card-19__ctas">
        <button type="button" class="card-19__cta card-19__cta--primary">
          <span class="card-19__cta-sheen" aria-hidden="true"></span>
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          <span>Reserve for $189</span>
          <span class="card-19__cta-arrow" aria-hidden="true">→</span>
        </button>
        <button type="button" class="card-19__cta card-19__cta--ghost" aria-label="View in AR">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
        </button>
      </div>

      <div class="card-19__foot">
        <div class="card-19__foot-avatars" aria-hidden="true">
          <span class="card-19__fa card-19__fa--1"></span>
          <span class="card-19__fa card-19__fa--2"></span>
          <span class="card-19__fa card-19__fa--3"></span>
        </div>
        <span class="card-19__foot-text">
          <strong>2,847</strong> reserving now · ships Mar 12
        </span>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.card-19 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 15%, rgba(234, 88, 12, 0.08) 0%, transparent 45%), radial-gradient(ellipse at 80% 85%, rgba(120, 53, 15, 0.08) 0%, transparent 45%), linear-gradient(180deg, #f5f0e8 0%, #ebe1cf 100%);
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #ea580c;
  perspective: 2000px;
  overflow: hidden;
}

.card-19 *,
.card-19 *::before,
.card-19 *::after {
  box-sizing: border-box;
}
/* stage */

.card-19__stage {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.card-19__stage-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 700px;
  height: 700px;
  background: radial-gradient(circle, rgba(234, 88, 12, 0.14) 0%, transparent 55%);
  filter: blur(60px);
}

.card-19__stage-grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(120, 53, 15, 0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(120, 53, 15, 0.05) 1px, transparent 1px);
  background-size: 40px 40px;
  mask-image: radial-gradient(ellipse at center, black 20%, transparent 65%);
  -webkit-mask-image: radial-gradient(ellipse at center, black 20%, transparent 65%);
}
/* card container with 3D tilt */

.card-19__card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 380px;
  background: #fff;
  border-radius: 26px;
  border: 1px solid rgba(0, 0, 0, 0.05);
  overflow: hidden;
  transform: perspective(2000px) rotateX(4deg) rotateY(-4deg);
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.34, 1.2, 0.64, 1), box-shadow 0.6s;
  box-shadow: 0 40px 80px -30px rgba(80, 40, 20, 0.4), 0 20px 40px -20px rgba(234, 88, 12, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.6);
}

.card-19__card:hover {
  transform: perspective(2000px) rotateX(2deg) rotateY(-8deg) translateY(-6px);
  box-shadow: 0 60px 100px -30px rgba(80, 40, 20, 0.5), 0 30px 50px -20px rgba(234, 88, 12, 0.32), inset 0 1px 0 rgba(255, 255, 255, 0.6);
}
/* ── hero photo section ── */

.card-19__hero {
  position: relative;
  aspect-ratio: 1.4/1;
  overflow: visible;
  border-radius: 26px 26px 0 0;
  transform-style: preserve-3d;
  isolation: isolate;
}

.card-19__hero-bg {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 60% 40%, #fed7aa 0%, transparent 55%), linear-gradient(160deg, #ffe4c4 0%, #fdba74 60%, #ea580c 100%);
  overflow: hidden;
  border-radius: 26px 26px 0 0;
}
/* turntable rings — subtle concentric on hero bg */

.card-19__hero-turntable {
  position: absolute;
  bottom: 12%;
  left: 50%;
  transform: translateX(-50%);
  width: 320px;
  height: 320px;
  pointer-events: none;
}

.card-19__turntable-ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1px dashed rgba(120, 53, 15, 0.18);
  animation: card-19-spin 30s linear infinite;
}

.card-19__turntable-ring--2 {
  inset: 20%;
  border-color: rgba(120, 53, 15, 0.14);
  animation-direction: reverse;
  animation-duration: 20s;
}
/* badges + wishlist */

.card-19__badges {
  position: absolute;
  top: 14px;
  left: 14px;
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
  z-index: 4;
}

.card-19__badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  padding: 4px 8px;
  border-radius: 6px;
  text-transform: uppercase;
}

.card-19__badge--drop {
  background: rgba(220, 38, 38, 0.95);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: 0 2px 8px rgba(220, 38, 38, 0.3);
}

.card-19__badge-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #fff;
  animation: card-19-blink 1.4s ease-in-out infinite;
}

.card-19__badge--ar {
  background: rgba(255, 255, 255, 0.85);
  color: #7c2d12;
  border: 1px solid rgba(120, 53, 15, 0.2);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.card-19__wish {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 34px;
  height: 34px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.85);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 50%;
  color: #1a1a1a;
  cursor: pointer;
  transition: color 0.18s, transform 0.18s;
  z-index: 4;
}

.card-19__wish:hover {
  color: #dc2626;
  transform: scale(1.08);
}

.card-19__wish:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* sneaker: pops out of the frame */

.card-19__sneaker {
  position: absolute;
  bottom: 8%;
  left: 50%;
  width: 80%;
  height: 75%;
  transform: translateX(-50%) translateZ(80px) rotate(-6deg);
  object-fit: contain;
  filter: drop-shadow(0 14px 18px rgba(80, 30, 10, 0.3)) drop-shadow(0 6px 8px rgba(80, 30, 10, 0.2));
  transition: transform 0.6s cubic-bezier(0.34, 1.2, 0.64, 1), filter 0.6s;
  pointer-events: none;
  z-index: 3;
}

.card-19__card:hover .card-19__sneaker {
  transform: translateX(-50%) translateZ(150px) rotate(-8deg) scale(1.08);
  filter: drop-shadow(0 22px 26px rgba(80, 30, 10, 0.36)) drop-shadow(0 10px 14px rgba(80, 30, 10, 0.24));
}
/* soft ground shadow */

.card-19__shadow {
  position: absolute;
  bottom: 4%;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 20px;
  background: radial-gradient(ellipse, rgba(80, 30, 10, 0.5), transparent 65%);
  filter: blur(10px);
  transition: width 0.6s, opacity 0.6s;
  z-index: 2;
  pointer-events: none;
}

.card-19__card:hover .card-19__shadow {
  width: 68%;
  opacity: 0.8;
}
/* view angles */

.card-19__angles {
  position: absolute;
  bottom: 12px;
  right: 14px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px 4px 6px;
  background: rgba(255, 255, 255, 0.85);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border-radius: 999px;
  z-index: 4;
}

.card-19__angle {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: rgba(120, 53, 15, 0.3);
}

.card-19__angle--active {
  width: 12px;
  border-radius: 999px;
  background: #7c2d12;
}

.card-19__angle-count {
  margin-left: 4px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 700;
  color: #7c2d12;
  letter-spacing: 0.02em;
  font-variant-numeric: tabular-nums;
}
/* countdown/spec chip bottom-left */

.card-19__spec {
  position: absolute;
  bottom: 12px;
  left: 14px;
  display: flex;
  flex-direction: column;
  gap: 1px;
  padding: 5px 10px;
  background: rgba(255, 255, 255, 0.85);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border-radius: 8px;
  z-index: 4;
}

.card-19__spec-label {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 8px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #9a3412;
  text-transform: uppercase;
}

.card-19__spec-val {
  display: inline-flex;
  align-items: baseline;
  gap: 1px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 12px;
  font-weight: 800;
  color: #7c2d12;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
}

.card-19__spec-val em {
  font-style: normal;
  font-size: 8px;
  color: rgba(154, 52, 18, 0.6);
  margin: 0 2px 0 0;
}
/* ── body ── */

.card-19__body {
  padding: 16px 18px 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: linear-gradient(180deg, #fff 0%, #fafaf7 100%);
  transform: translateZ(30px);
  transform-style: preserve-3d;
}

.card-19__title-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  align-items: start;
}

.card-19__chip {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #ea580c;
  margin: 0 0 4px;
}

.card-19__title {
  font-size: 17px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.02em;
  line-height: 1.2;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-19__title-color {
  color: #ea580c;
  font-weight: 700;
  background: none;
  -webkit-text-fill-color: initial;
}

.card-19__rating {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  margin-top: 4px;
  font-size: 10.5px;
}

.card-19__stars {
  display: inline-flex;
  gap: 1px;
  margin-right: 3px;
}

.card-19__rating-num {
  font-weight: 800;
  color: #92400e;
  letter-spacing: -0.01em;
  font-variant-numeric: tabular-nums;
}

.card-19__rating-count {
  color: #a1a1aa;
  letter-spacing: -0.005em;
}

.card-19__price-block {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 1px;
}

.card-19__price {
  font-size: 24px;
  font-weight: 800;
  color: #1a1a1a;
  letter-spacing: -0.03em;
  font-variant-numeric: tabular-nums;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-19__price-note {
  font-size: 9.5px;
  color: #6b6b7c;
  letter-spacing: -0.005em;
}

.card-19__price-note-brand {
  color: #ea580c;
  font-weight: 700;
  margin-left: 3px;
}
/* tags */

.card-19__tags {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.card-19__tags li {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10.5px;
  font-weight: 700;
  color: #365314;
  padding: 3px 8px;
  background: rgba(132, 204, 22, 0.10);
  border: 1px solid rgba(132, 204, 22, 0.24);
  border-radius: 999px;
  letter-spacing: -0.005em;
}

.card-19__tags li:nth-child(2) {
  color: #7c2d12;
  background: rgba(234, 88, 12, 0.08);
  border-color: rgba(234, 88, 12, 0.22);
}

.card-19__tags li:nth-child(3) {
  color: #4b4b57;
  background: rgba(0, 0, 0, 0.03);
  border-color: rgba(0, 0, 0, 0.08);
}

.card-19__tag-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #84cc16;
  box-shadow: 0 0 4px #84cc16;
}
/* colors */

.card-19__colors {
  padding: 10px 12px;
  background: rgba(0, 0, 0, 0.02);
  border: 1px solid rgba(0, 0, 0, 0.04);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.card-19__colors-label {
  display: flex;
  flex-direction: column;
  gap: 1px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #6b6b7c;
  text-transform: uppercase;
}

.card-19__colors-name {
  font-style: normal;
  font-family: 'Inter', sans-serif;
  font-size: 11.5px;
  font-weight: 800;
  color: #1a1a1a;
  text-transform: none;
  letter-spacing: -0.01em;
}

.card-19__swatches {
  display: flex;
  gap: 4px;
}

.card-19__swatch {
  position: relative;
  width: 24px;
  height: 24px;
  padding: 3px;
  border: 1.5px solid transparent;
  border-radius: 50%;
  background: transparent;
  cursor: pointer;
  transition: transform 0.18s, border-color 0.18s;
}

.card-19__swatch-c {
  display: block;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3), inset 0 -1px 0 rgba(0, 0, 0, 0.15);
}

.card-19__swatch:hover {
  transform: scale(1.12);
}

.card-19__swatch--active {
  border-color: #ea580c;
}

.card-19__swatch--soldout::after {
  content: '';
  position: absolute;
  inset: 3px;
  border-radius: 50%;
  background: linear-gradient(45deg, transparent 45%, rgba(220, 38, 38, 0.8) 45%, rgba(220, 38, 38, 0.8) 55%, transparent 55%);
}

.card-19__swatch:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* CTAs */

.card-19__ctas {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 6px;
}

.card-19__cta {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 44px;
  padding: 10px 16px;
  border: 0;
  border-radius: 14px;
  font: 800 13px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.01em;
  transition: transform 0.2s, box-shadow 0.2s;
  overflow: hidden;
}

.card-19__cta--primary {
  background: linear-gradient(180deg, #ea580c 0%, #9a3412 100%);
  color: #fff;
  box-shadow: 0 6px 16px rgba(234, 88, 12, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.14) inset, 0 -1px 0 rgba(80, 30, 10, 0.4) inset;
}

.card-19__cta--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 24px rgba(234, 88, 12, 0.55), 0 0 0 1px rgba(255, 255, 255, 0.28) inset, 0 -1px 0 rgba(80, 30, 10, 0.4) inset;
}

.card-19__cta-sheen {
  position: absolute;
  top: 0;
  left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(115deg, transparent 30%, rgba(255,255,255,0.4) 50%, transparent 70%);
  transition: left 0.6s ease;
}

.card-19__cta--primary:hover .card-19__cta-sheen {
  left: 130%;
}

.card-19__cta-arrow {
  transition: transform 0.2s;
}

.card-19__cta--primary:hover .card-19__cta-arrow {
  transform: translateX(4px);
}

.card-19__cta--ghost {
  min-width: 44px;
  background: #fff;
  color: #7c2d12;
  border: 1px solid rgba(120, 53, 15, 0.14);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
}

.card-19__cta--ghost:hover {
  background: rgba(234, 88, 12, 0.06);
  border-color: rgba(234, 88, 12, 0.22);
}

.card-19__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* foot with social proof */

.card-19__foot {
  display: flex;
  align-items: center;
  gap: 8px;
  padding-top: 10px;
  border-top: 1px dashed rgba(0, 0, 0, 0.06);
}

.card-19__foot-avatars {
  display: flex;
}

.card-19__fa {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 1.5px solid #fff;
  margin-left: -6px;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.06);
}

.card-19__fa:first-child {
  margin-left: 0;
}

.card-19__fa--1 {
  background: linear-gradient(135deg, #f472b6, #ec4899);
}

.card-19__fa--2 {
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
}

.card-19__fa--3 {
  background: linear-gradient(135deg, #34d399, #10b981);
}

.card-19__foot-text {
  font-size: 10.5px;
  color: #6b6b7c;
  letter-spacing: -0.005em;
}

.card-19__foot-text strong {
  color: #dc2626;
  font-weight: 800;
}

@keyframes card-19-spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes card-19-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.5;
    transform: scale(0.8);
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-19__turntable-ring,
    .card-19__badge-dot,
    .card-19__tag-dot {
    animation: none;
  }

  .card-19__card,
    .card-19__sneaker,
    .card-19__shadow,
    .card-19__wish,
    .card-19__cta,
    .card-19__cta-arrow,
    .card-19__cta-sheen,
    .card-19__swatch {
    transition: none;
  }

  .card-19__card:hover {
    transform: perspective(2000px) rotateX(4deg) rotateY(-4deg);
  }

  .card-19__card:hover .card-19__sneaker {
    transform: translateX(-50%) translateZ(80px) rotate(-6deg);
  }

  .card-19__card:hover .card-19__shadow {
    width: 60%;
    opacity: 1;
  }

  .card-19__wish:hover,
    .card-19__cta--primary:hover,
    .card-19__swatch:hover {
    transform: none;
  }

  .card-19__cta--primary:hover .card-19__cta-arrow {
    transform: none;
  }

  .card-19__cta--primary:hover .card-19__cta-sheen {
    left: -100%;
  }
}
```
