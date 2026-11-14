---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/testimonial-customer-review-card/"
title: "Testimonial Customer Review Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front features a prominent client quote and star rating; back reveals the full client profile, company details, and a per-category rating breakdown."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Testimonial Customer Review Card
Source: https://codefronts.com/components/css-flip-cards/testimonial-customer-review-card/

Front features a prominent client quote and star rating; back reveals the full client profile, company details, and a per-category rating breakdown.
## HTML
```html
<div class="fc-11">
  <div class="fc-11__scene">
    <div class="fc-11__card">
      <div class="fc-11__front">
        <div class="fc-11__quote-mark">"</div>
        <div class="fc-11__quote">Switching to this platform <strong>cut our design-to-production time in half.</strong> The component library alone saved us three months of custom work.</div>
        <div class="fc-11__stars">
          <span class="fc-11__star">★</span><span class="fc-11__star">★</span>
          <span class="fc-11__star">★</span><span class="fc-11__star">★</span>
          <span class="fc-11__star">★</span>
        </div>
        <div class="fc-11__client-preview">
          <div class="fc-11__avatar-mini">MK</div>
          <div>
            <div class="fc-11__client-name">Marcus Klein</div>
            <div class="fc-11__client-title">VP of Engineering · Prism Labs</div>
          </div>
        </div>
        <div class="fc-11__front-hint">Hover for full profile →</div>
      </div>
      <div class="fc-11__back">
        <div class="fc-11__back-label">Reviewer Profile</div>
        <div class="fc-11__profile-card">
          <div class="fc-11__avatar-lg">MK</div>
          <div class="fc-11__full-name">Marcus Klein</div>
          <div class="fc-11__full-title">VP of Engineering · 12 years in SaaS infrastructure</div>
          <div class="fc-11__company-row">
            <div class="fc-11__company-dot">PL</div>
            <div>
              <div class="fc-11__company-name">Prism Labs</div>
              <div class="fc-11__company-size">Series B · 340 employees</div>
            </div>
          </div>
        </div>
        <div class="fc-11__rating-detail">
          <div class="fc-11__rating-row"><span class="fc-11__rating-lbl">Overall</span><span class="fc-11__rating-stars fc-11__full-stars">★★★★★</span></div>
          <div class="fc-11__rating-row"><span class="fc-11__rating-lbl">Ease of use</span><span class="fc-11__rating-stars fc-11__full-stars">★★★★★</span></div>
          <div class="fc-11__rating-row" style="margin-bottom:0"><span class="fc-11__rating-lbl">Support</span><span class="fc-11__rating-stars fc-11__full-stars">★★★★★</span></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-11,
.fc-11 *,
.fc-11 *::before,
.fc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-11 ::selection {
  background: #7c3aed;
  color: #fff;
}

.fc-11 {
  --bg: #09050f;
  --violet: #7c3aed;
  --pink: #db2777;
  --gold: #f59e0b;
  --white: #fdf4ff;
  --card-w: 360px;
  --card-h: 420px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 60% 40%,#12062a,#09050f 65%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-11__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-11__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .75s cubic-bezier(.4,0,.2,1);
}

.fc-11__scene:hover .fc-11__card {
  transform: rotateY(180deg);
}

.fc-11__front,
.fc-11__back {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-11__front {
  background: linear-gradient(145deg,#110822,#0d0518);
  border: 1px solid rgba(124,58,237,.25);
  display: flex;
  flex-direction: column;
  padding: 36px 32px;
  gap: 16px;
  box-shadow: 0 0 40px rgba(124,58,237,.06);
}

.fc-11__quote-mark {
  font-size: 80px;
  line-height: .7;
  color: rgba(124,58,237,.25);
  font-family: Georgia,serif;
  font-weight: 900;
  margin-bottom: -12px;
}

.fc-11__quote {
  font-size: 18px;
  font-weight: 600;
  line-height: 1.7;
  color: rgba(253,244,255,.85);
  flex: 1;
}

.fc-11__quote strong {
  background: linear-gradient(135deg,var(--violet),var(--pink));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fc-11__stars {
  display: flex;
  gap: 4px;
  margin-top: auto;
}

.fc-11__star {
  color: var(--gold);
  font-size: 18px;
}

.fc-11__client-preview {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,.07);
}

.fc-11__avatar-mini {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--violet),var(--pink));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  flex-shrink: 0;
}

.fc-11__client-name {
  font-size: 14px;
  font-weight: 700;
  color: var(--white);
}

.fc-11__client-title {
  font-size: 11px;
  color: rgba(253,244,255,.45);
}

.fc-11__front-hint {
  font-size: 10px;
  color: rgba(253,244,255,.2);
  letter-spacing: .08em;
  text-align: right;
}
/* BACK */

.fc-11__back {
  background: linear-gradient(145deg,#0f0120,#14022a);
  border: 1px solid rgba(219,39,119,.2);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 28px;
  gap: 14px;
}

.fc-11__back-label {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--pink);
  font-weight: 700;
}

.fc-11__profile-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 20px;
  border-radius: 16px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.07);
}

.fc-11__avatar-lg {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--violet),var(--pink));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  font-weight: 900;
  color: #fff;
  border: 3px solid rgba(124,58,237,.3);
}

.fc-11__full-name {
  font-size: 18px;
  font-weight: 800;
  color: var(--white);
}

.fc-11__full-title {
  font-size: 12px;
  color: rgba(253,244,255,.5);
  text-align: center;
}

.fc-11__company-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 10px;
  background: rgba(124,58,237,.1);
  border: 1px solid rgba(124,58,237,.2);
}

.fc-11__company-dot {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  background: linear-gradient(135deg,#4f46e5,#7c3aed);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 800;
  color: #fff;
  flex-shrink: 0;
}

.fc-11__company-name {
  font-size: 13px;
  font-weight: 700;
  color: rgba(253,244,255,.8);
}

.fc-11__company-size {
  font-size: 10px;
  color: rgba(253,244,255,.4);
}

.fc-11__rating-detail {
  padding: 14px;
  border-radius: 12px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.07);
}

.fc-11__rating-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}

.fc-11__rating-lbl {
  font-size: 11px;
  color: rgba(253,244,255,.5);
}

.fc-11__rating-stars {
  display: flex;
  gap: 2px;
  font-size: 13px;
}

.fc-11__full-stars {
  color: var(--gold);
}

@media (prefers-reduced-motion: reduce) {
  .fc-11__card {
    transition: none;
  }
}
```
