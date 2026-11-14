---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/hotel-travel-booking-card/"
title: "Hotel Travel Booking Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Hotel booking tile with CSS-drawn arched lobby, amenity pills with icons, nightly + total pricing, guest/date summary, primary book CTA and secondary details…"
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hotel Travel Booking Card
Source: https://codefronts.com/components/css-cards/hotel-travel-booking-card/

Hotel booking tile with CSS-drawn arched lobby, amenity pills with icons, nightly + total pricing, guest/date summary, primary book CTA and secondary details link.
## HTML
```html
<section class="card-05" aria-label="Hotel booking">
  <article class="card-05__card">
    <div class="card-05__gallery">
      <div class="card-05__cell card-05__cell--main">
        <img class="card-05__img" src="https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1000&q=80&auto=format&fit=crop" alt="The Everly hotel exterior" loading="lazy" decoding="async">
        <span class="card-05__super">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          SUPERHOST
        </span>
        <button type="button" class="card-05__wish" aria-label="Add to wishlist">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
        </button>
      </div>
      <div class="card-05__cell card-05__cell--a">
        <img class="card-05__img" src="https://images.unsplash.com/photo-1590490360182-c33d57733427?w=400&q=80&auto=format&fit=crop" alt="Hotel room interior" loading="lazy" decoding="async">
      </div>
      <div class="card-05__cell card-05__cell--b">
        <img class="card-05__img" src="https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=400&q=80&auto=format&fit=crop" alt="Hotel bathroom" loading="lazy" decoding="async">
      </div>
      <div class="card-05__cell card-05__cell--more">
        <img class="card-05__img" src="https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=400&q=80&auto=format&fit=crop" alt="Hotel pool" loading="lazy" decoding="async">
        <span class="card-05__more-overlay">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
          +32 photos
        </span>
      </div>
    </div>

    <div class="card-05__body">
      <div class="card-05__title-row">
        <div class="card-05__title-block">
          <div class="card-05__eyebrow-row">
            <span class="card-05__cat">BOUTIQUE HOTEL</span>
            <span class="card-05__dot" aria-hidden="true">·</span>
            <span class="card-05__district">Shibuya</span>
          </div>
          <h3 class="card-05__name">The Everly, Tokyo</h3>
          <p class="card-05__loc">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            0.4 mi from Shibuya Crossing
          </p>
        </div>
        <div class="card-05__rating">
          <span class="card-05__rating-num">4.9</span>
          <span class="card-05__rating-max">/ 5</span>
          <div class="card-05__rating-bar" aria-hidden="true">
            <span class="card-05__rating-fill"></span>
          </div>
          <span class="card-05__rating-count">2,847 reviews</span>
        </div>
      </div>

      <ul class="card-05__amen">
        <li>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12a10 10 0 0 1 14 0"/><path d="M8.5 15.5a5 5 0 0 1 7 0"/><line x1="12" y1="19" x2="12" y2="19"/></svg>
          Wi-Fi
        </li>
        <li>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12h20M2 8h20M2 16h20"/></svg>
          Pool
        </li>
        <li>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>
          Breakfast
        </li>
        <li>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M8 21V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v16"/></svg>
          Gym
        </li>
        <li class="card-05__amen-more">+8 more</li>
      </ul>

      <div class="card-05__stay">
        <div class="card-05__stay-block">
          <span class="card-05__stay-label">Check-in</span>
          <span class="card-05__stay-val">Jul 12</span>
        </div>
        <div class="card-05__stay-arrow" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </div>
        <div class="card-05__stay-block">
          <span class="card-05__stay-label">Check-out</span>
          <span class="card-05__stay-val">Jul 15</span>
        </div>
        <div class="card-05__stay-block">
          <span class="card-05__stay-label">Guests</span>
          <span class="card-05__stay-val">2 adults</span>
        </div>
      </div>

      <div class="card-05__price-block">
        <div class="card-05__price-rows">
          <div class="card-05__price-line">
            <span>$184 × 3 nights</span>
            <span>$552</span>
          </div>
          <div class="card-05__price-line">
            <span>Cleaning fee</span>
            <span>$32</span>
          </div>
          <div class="card-05__price-line card-05__price-line--save">
            <span>Weekend discount</span>
            <span>−$24</span>
          </div>
          <div class="card-05__price-line card-05__price-line--total">
            <span>Total (USD)</span>
            <span>$560</span>
          </div>
        </div>
        <div class="card-05__flexible">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
          Free cancellation until Jul 10
        </div>
      </div>

      <div class="card-05__foot">
        <div class="card-05__urgency">
          <span class="card-05__urgency-dot" aria-hidden="true"></span>
          <strong>17 people</strong> looking now
        </div>
        <button type="button" class="card-05__cta">
          Reserve
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.card-05 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 15%, rgba(236, 72, 153, 0.05) 0%, transparent 45%), radial-gradient(ellipse at 80% 85%, rgba(15, 118, 110, 0.05) 0%, transparent 45%), linear-gradient(180deg, #e8f2ef 0%, #cde0d9 100%);
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #ec4899;
  --accent: #ec4899;
}

.card-05 *,
.card-05 *::before,
.card-05 *::after {
  box-sizing: border-box;
}

.card-05__card {
  width: 100%;
  max-width: 460px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(20, 80, 60, 0.24), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  transition: transform 0.35s ease, box-shadow 0.35s;
}

.card-05__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 40px 80px -30px rgba(20, 80, 60, 0.34);
}
/* ── gallery grid: 2 columns × 2 rows. Main spans both rows on the left, 3 small cells stack on the right ── */

.card-05__gallery {
  display: grid;
  grid-template-columns: 1.7fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 3px;
  height: 260px;
  padding: 3px;
  background: #f4ede4;
}

.card-05__cell {
  position: relative;
  overflow: hidden;
  min-width: 0;
  min-height: 0;
}

.card-05__cell--main {
  grid-column: 1;
  grid-row: 1 / 3;
  border-radius: 20px 6px 6px 20px;
}

.card-05__cell--a {
  grid-column: 2;
  grid-row: 1;
  border-radius: 6px 20px 6px 6px;
}

.card-05__cell--b {
  grid-column: 3;
  grid-row: 1;
  border-radius: 6px 6px 6px 6px;
}

.card-05__cell--more {
  grid-column: 2 / 4;
  grid-row: 2;
  border-radius: 6px 6px 20px 6px;
}

.card-05__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.card-05__cell:hover .card-05__img {
  transform: scale(1.05);
}

.card-05__super {
  position: absolute;
  top: 12px;
  left: 12px;
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 4px 9px;
  background: rgba(255, 255, 255, 0.95);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border-radius: 999px;
  color: #b91c1c;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  border: 1px solid rgba(255, 255, 255, 0.6);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.14);
  z-index: 2;
}

.card-05__super svg {
  color: #dc2626;
}

.card-05__wish {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 36px;
  height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.95);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 50%;
  color: #1a1a1a;
  cursor: pointer;
  transition: color 0.18s, transform 0.18s;
  z-index: 2;
}

.card-05__wish:hover {
  color: #dc2626;
  transform: scale(1.08);
}

.card-05__wish:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-05__more-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  background: rgba(0, 0, 0, 0.5);
  -webkit-backdrop-filter: blur(2px);
  backdrop-filter: blur(2px);
  color: #fff;
  font: 800 11px 'Inter', sans-serif;
  letter-spacing: -0.005em;
  z-index: 2;
  pointer-events: none;
}
/* ── body ── */

.card-05__body {
  padding: 18px 20px 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.card-05__title-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.card-05__title-block {
  min-width: 0;
}

.card-05__eyebrow-row {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 3px;
}

.card-05__cat {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #0f766e;
}

.card-05__dot {
  color: #cbd5e1;
}

.card-05__district {
  font-size: 10.5px;
  font-weight: 700;
  color: #6b6b7c;
}

.card-05__name {
  font-size: 20px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0 0 3px;
  letter-spacing: -0.025em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-05__loc {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 11.5px;
  color: #6b6b7c;
  margin: 0;
}

.card-05__loc svg {
  color: #0f766e;
  flex-shrink: 0;
}

.card-05__rating {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 3px;
  padding: 8px 10px;
  background: linear-gradient(180deg, #f0fdf4 0%, #dcfce7 100%);
  border: 1px solid rgba(15, 118, 110, 0.16);
  border-radius: 12px;
  min-width: 88px;
  flex-shrink: 0;
}

.card-05__rating-num {
  font-size: 20px;
  font-weight: 800;
  color: #0f766e;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.03em;
  line-height: 1;
}

.card-05__rating-max {
  font-size: 10px;
  color: #059669;
  font-weight: 700;
}

.card-05__rating-bar {
  width: 60px;
  height: 3px;
  background: rgba(15, 118, 110, 0.14);
  border-radius: 2px;
  overflow: hidden;
}

.card-05__rating-fill {
  display: block;
  width: 92%;
  height: 100%;
  background: linear-gradient(90deg, #14b8a6, #0f766e);
  border-radius: 2px;
}

.card-05__rating-count {
  font-size: 9.5px;
  color: #0f766e;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.005em;
}

.card-05__amen {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.card-05__amen li {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10.5px;
  font-weight: 700;
  color: #0f766e;
  padding: 4px 8px;
  background: rgba(15, 118, 110, 0.08);
  border: 1px solid rgba(15, 118, 110, 0.18);
  border-radius: 999px;
  letter-spacing: -0.005em;
}

.card-05__amen-more {
  color: #6b6b7c !important;
  background: transparent !important;
  border-color: rgba(0, 0, 0, 0.1) !important;
}

.card-05__stay {
  display: grid;
  grid-template-columns: 1fr 20px 1fr 1fr;
  gap: 8px;
  padding: 10px 12px;
  background: linear-gradient(180deg, #fafafd 0%, #f4f4f0 100%);
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 12px;
  align-items: center;
}

.card-05__stay-block {
  display: flex;
  flex-direction: column;
  gap: 1px;
  min-width: 0;
}

.card-05__stay-label {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: #9ca3af;
  text-transform: uppercase;
}

.card-05__stay-val {
  font-size: 12.5px;
  font-weight: 800;
  color: #1a1a1a;
  letter-spacing: -0.01em;
  font-variant-numeric: tabular-nums;
}

.card-05__stay-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #cbd5e1;
}

.card-05__price-block {
  padding: 12px 14px;
  background: linear-gradient(180deg, #fdfef9 0%, #f0f9f5 100%);
  border: 1px solid rgba(15, 118, 110, 0.14);
  border-radius: 12px;
}

.card-05__price-rows {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.card-05__price-line {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11.5px;
  color: #4b4b57;
  font-variant-numeric: tabular-nums;
}

.card-05__price-line--save {
  color: #059669;
  font-weight: 700;
}

.card-05__price-line--total {
  padding-top: 8px;
  margin-top: 4px;
  border-top: 1px dashed rgba(0, 0, 0, 0.1);
  color: #1a1a1a;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: -0.01em;
}

.card-05__flexible {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  margin-top: 8px;
  font-size: 10.5px;
  font-weight: 700;
  color: #059669;
  letter-spacing: -0.005em;
}

.card-05__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-top: 4px;
}

.card-05__urgency {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  color: #6b6b7c;
}

.card-05__urgency strong {
  color: #dc2626;
  font-weight: 800;
}

.card-05__urgency-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #dc2626;
  box-shadow: 0 0 8px #dc2626;
  animation: card-05-blink 1.6s ease-in-out infinite;
}

.card-05__cta {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-height: 40px;
  padding: 10px 20px;
  border-radius: 999px;
  border: 0;
  background: linear-gradient(180deg, #ec4899 0%, #be185d 100%);
  color: #fff;
  font: 800 13px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.01em;
  box-shadow: 0 6px 16px rgba(236, 72, 153, 0.35), 0 0 0 1px rgba(255, 255, 255, 0.14) inset;
  transition: transform 0.18s, box-shadow 0.18s;
}

.card-05__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 22px rgba(236, 72, 153, 0.45), 0 0 0 1px rgba(255, 255, 255, 0.2) inset;
}

.card-05__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

@keyframes card-05-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.4;
    transform: scale(0.8);
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-05__card,
    .card-05__img,
    .card-05__cta,
    .card-05__wish {
    transition: none;
  }

  .card-05__card:hover {
    transform: none;
  }

  .card-05__cta:hover,
    .card-05__wish:hover {
    transform: none;
  }

  .card-05__urgency-dot {
    animation: none;
  }
}
```
