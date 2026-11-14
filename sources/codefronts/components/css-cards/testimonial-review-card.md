---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/testimonial-review-card/"
title: "Testimonial Review Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Customer quote card with 5 amber stars, a decorative giant serif quote-mark backdrop, blockquote, and cited avatar + name + role with a mini brand mark."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Testimonial Review Card
Source: https://codefronts.com/components/css-cards/testimonial-review-card/

Customer quote card with 5 amber stars, a decorative giant serif quote-mark backdrop, blockquote, and cited avatar + name + role with a mini brand mark.
## HTML
```html
<section class="card-08">
  <article class="card-08__card">
    <div class="card-08__glow" aria-hidden="true"></div>
    <div class="card-08__mesh" aria-hidden="true"></div>
    <span class="card-08__mark" aria-hidden="true">"</span>
    <header class="card-08__head">
      <div class="card-08__rating-block">
        <div class="card-08__stars" role="img" aria-label="Rated 4.9 out of 5">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
        </div>
        <span class="card-08__rating-score">4.9<span class="card-08__rating-max">/5</span></span>
      </div>
      <span class="card-08__pick">
        <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
        Staff pick
      </span>
    </header>
    <blockquote class="card-08__quote">
      We shipped 3× faster after switching. The team stopped worrying about infrastructure and started shipping features that actually move the needle.
    </blockquote>
    <div class="card-08__highlight" aria-hidden="true">
      <span></span>
    </div>
    <cite class="card-08__cite">
      <div class="card-08__avatar-wrap">
        <span class="card-08__avatar">PS</span>
        <span class="card-08__verify" aria-hidden="true">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        </span>
      </div>
      <div class="card-08__who">
        <div class="card-08__name-row">
          <span class="card-08__name">Priya Sharma</span>
          <svg class="card-08__verified" role="img" aria-label="Verified customer" width="12" height="12" viewBox="0 0 24 24" fill="none">
            <path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/>
            <path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <span class="card-08__role">
          CTO at
          <span class="card-08__company">
            <span class="card-08__logo" aria-hidden="true"></span>
            Meridian Labs
          </span>
        </span>
      </div>
    </cite>
    <div class="card-08__proof">
      <div class="card-08__proof-item">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        Verified customer
      </div>
      <time datetime="2026-06-14" class="card-08__date">Jun 14, 2026</time>
    </div>
    <footer class="card-08__foot">
      <div class="card-08__helpful">
        <button type="button" class="card-08__helpful-btn" aria-label="Mark helpful">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3H14z"/><line x1="6" y1="10" x2="6" y2="22"/></svg>
          Helpful · 234
        </button>
      </div>
      <a href="#reviews" class="card-08__more">
        See all 1,247 reviews
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </footer>
  </article>
</section>
```
## CSS
```css
.card-08 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 20%, rgba(245, 158, 11, 0.05) 0%, transparent 50%), radial-gradient(ellipse at 80% 80%, rgba(15, 118, 110, 0.05) 0%, transparent 50%), #f8f7f4;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #f59e0b;
}

.card-08 *,
.card-08 *::before,
.card-08 *::after {
  box-sizing: border-box;
}

.card-08__card {
  position: relative;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 22px;
  padding: 20px 22px 16px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(80, 60, 20, 0.2), 0 0 0 1px rgba(255, 255, 255, 0.5) inset, 0 -1px 0 rgba(0, 0, 0, 0.02) inset;
  transition: transform 0.35s ease, box-shadow 0.35s;
  isolation: isolate;
}

.card-08__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 40px 80px -30px rgba(80, 60, 20, 0.28), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}
/* aura glow */

.card-08__glow {
  position: absolute;
  top: -80px;
  right: -80px;
  width: 260px;
  height: 260px;
  background: radial-gradient(circle, rgba(245, 158, 11, 0.14) 0%, transparent 55%), radial-gradient(circle at 60% 60%, rgba(236, 72, 153, 0.08) 0%, transparent 55%);
  filter: blur(30px);
  pointer-events: none;
  z-index: -1;
}
/* subtle iridescent mesh diagonal */

.card-08__mesh {
  position: absolute;
  top: -30%;
  left: -20%;
  width: 60%;
  height: 160%;
  background: linear-gradient(115deg,
      transparent 30%,
      rgba(245, 158, 11, 0.03) 45%,
      rgba(236, 72, 153, 0.03) 50%,
      rgba(15, 118, 110, 0.03) 55%,
      transparent 70%);
  transform: rotate(15deg);
  pointer-events: none;
  z-index: 0;
}
/* huge decorative quote mark */

.card-08__mark {
  position: absolute;
  top: -20px;
  right: 12px;
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 140px;
  line-height: 1;
  color: rgba(245, 158, 11, 0.08);
  pointer-events: none;
  user-select: none;
  z-index: 0;
  font-weight: 700;
}
/* content goes above the mesh */

.card-08__head,
.card-08__quote,
.card-08__cite,
.card-08__proof,
.card-08__foot,
.card-08__highlight {
  position: relative;
  z-index: 1;
}
/* ── header row: rating + staff pick badge ── */

.card-08__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 14px;
}

.card-08__rating-block {
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-08__stars {
  display: inline-flex;
  gap: 2px;
  padding: 3px 6px;
  background: rgba(245, 158, 11, 0.10);
  border: 1px solid rgba(245, 158, 11, 0.22);
  border-radius: 999px;
}

.card-08__rating-score {
  font-size: 14px;
  font-weight: 800;
  color: #92400e;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}

.card-08__rating-max {
  font-size: 11px;
  color: #a1a1aa;
  font-weight: 600;
  margin-left: 1px;
}

.card-08__pick {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 9px;
  background: linear-gradient(180deg, #fef3c7 0%, #fde68a 100%);
  color: #78350f;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.10em;
  border-radius: 999px;
  border: 1px solid rgba(146, 64, 14, 0.22);
  text-transform: uppercase;
  box-shadow: 0 2px 4px rgba(245, 158, 11, 0.25);
}
/* ── main quote ── */

.card-08__quote {
  margin: 0 0 14px;
  font-size: 15.5px;
  font-weight: 500;
  line-height: 1.55;
  color: #1a1a1a;
  letter-spacing: -0.01em;
}
/* highlight strip under quote */

.card-08__highlight {
  height: 3px;
  margin: 0 0 18px;
  border-radius: 2px;
  background: rgba(245, 158, 11, 0.14);
  overflow: hidden;
  position: relative;
}

.card-08__highlight span {
  display: block;
  width: 65%;
  height: 100%;
  background: linear-gradient(90deg, #f59e0b, #ec4899);
  border-radius: 2px;
}
/* ── cite row (author) ── */

.card-08__cite {
  display: grid;
  grid-template-columns: 44px 1fr;
  gap: 12px;
  align-items: center;
  font-style: normal;
  margin-bottom: 14px;
}

.card-08__avatar-wrap {
  position: relative;
}

.card-08__avatar {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #f59e0b, #ef4444);
  color: #fff;
  font-size: 14px;
  font-weight: 800;
  border: 2px solid #fff;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.25);
  letter-spacing: -0.01em;
}

.card-08__verify {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #22c55e;
  border: 2px solid #fff;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(34, 197, 94, 0.35);
}

.card-08__who {
  display: flex;
  flex-direction: column;
  gap: 1px;
  min-width: 0;
}

.card-08__name-row {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.card-08__name {
  font-size: 13.5px;
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: -0.01em;
}

.card-08__verified {
  flex-shrink: 0;
}

.card-08__role {
  font-size: 11.5px;
  color: #6b6b7c;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.card-08__company {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  color: #1a1a1a;
  font-weight: 700;
  letter-spacing: -0.005em;
}

.card-08__logo {
  display: inline-block;
  width: 14px;
  height: 14px;
  border-radius: 4px;
  background: linear-gradient(135deg, transparent 40%, rgba(255, 255, 255, 0.4) 55%, transparent 70%), linear-gradient(135deg, #4338ca 0%, #a855f7 100%);
  box-shadow: 0 1px 3px rgba(67, 56, 202, 0.35);
  flex-shrink: 0;
}
/* ── proof row ── */

.card-08__proof {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 10px 12px;
  background: rgba(34, 197, 94, 0.05);
  border: 1px solid rgba(34, 197, 94, 0.16);
  border-radius: 10px;
  margin-bottom: 14px;
}

.card-08__proof-item {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  font-weight: 700;
  color: #059669;
  letter-spacing: -0.005em;
}

.card-08__proof-item svg {
  color: #22c55e;
  flex-shrink: 0;
}

.card-08__date {
  font-size: 10.5px;
  color: #6b6b7c;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.005em;
}
/* ── footer row ── */

.card-08__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding-top: 12px;
  border-top: 1px dashed rgba(0, 0, 0, 0.08);
}

.card-08__helpful {
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-08__helpful-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 10px;
  background: transparent;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 999px;
  color: #4b4b57;
  font: inherit;
  font-size: 11.5px;
  font-weight: 700;
  cursor: pointer;
  letter-spacing: -0.005em;
  transition: color 0.18s, background 0.18s, border-color 0.18s;
}

.card-08__helpful-btn:hover {
  color: #059669;
  background: rgba(34, 197, 94, 0.06);
  border-color: rgba(34, 197, 94, 0.24);
}

.card-08__helpful-btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-08__more {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 11.5px;
  font-weight: 700;
  color: #92400e;
  text-decoration: none;
  padding: 4px 8px;
  border-radius: 6px;
  transition: color 0.18s, background 0.18s;
}

.card-08__more:hover {
  color: #78350f;
  background: rgba(245, 158, 11, 0.06);
}

.card-08__more:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .card-08__card,
    .card-08__helpful-btn,
    .card-08__more {
    transition: none;
  }

  .card-08__card:hover {
    transform: none;
  }
}
```
