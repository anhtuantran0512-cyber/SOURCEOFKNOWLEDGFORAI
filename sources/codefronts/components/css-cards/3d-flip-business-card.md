---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/3d-flip-business-card/"
title: "3D Flip Business Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Landscape business card that flips on hover AND focus-within (keyboard-accessible)."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Business Card
Source: https://codefronts.com/components/css-cards/3d-flip-business-card/

Landscape business card that flips on hover AND focus-within (keyboard-accessible). Front shows avatar + name, back shows email/phone/site links. Reduced-motion disables the flip.
## HTML
```html
<section class="card-16">
  <div class="card-16__card" tabindex="0" aria-label="Business card for Alex Chen — flip to see contact details">
    <div class="card-16__inner">
      <div class="card-16__face card-16__front">
        <div class="card-16__brand" aria-hidden="true">
          <span class="card-16__mark"></span>
          <span class="card-16__brandname">CHEN &amp; CO</span>
        </div>
        <div class="card-16__id">
          <h3 class="card-16__name">Alex Chen</h3>
          <p class="card-16__role">Principal Designer</p>
        </div>
        <span class="card-16__hint">Hover to flip</span>
      </div>
      <div class="card-16__face card-16__back">
        <span class="card-16__backbrand">CHEN &amp; CO</span>
        <address class="card-16__contact">
          <div class="card-16__row">
            <svg class="card-16__ico" aria-hidden="true" focusable="false" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            <a href="mailto:[email protected]">[email protected]</a>
          </div>
          <div class="card-16__row">
            <svg class="card-16__ico" aria-hidden="true" focusable="false" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <a href="tel:+14155550142">+1 (415) 555-0142</a>
          </div>
          <div class="card-16__row">
            <svg class="card-16__ico" aria-hidden="true" focusable="false" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            <a href="#site">alexchen.design</a>
          </div>
        </address>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.card-16 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 30% 20%, #1e293b 0%, transparent 60%), radial-gradient(ellipse at 80% 80%, #0f172a 0%, transparent 60%), #050815;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #f5d97b;
  --gold: #d4b063;
  --gold-lite: #f5d97b;
}

.card-16 *,
.card-16 *::before,
.card-16 *::after {
  box-sizing: border-box;
}

.card-16__card {
  width: 360px;
  height: 220px;
  perspective: 1000px;
  border-radius: 14px;
}

.card-16__card:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 6px;
  border-radius: 14px;
}

.card-16__inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.7s cubic-bezier(0.34, 1.2, 0.64, 1);
  box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.6), 0 18px 36px -18px rgba(212, 176, 99, 0.35);
}

.card-16__card:hover .card-16__inner,
.card-16__card:focus-within .card-16__inner {
  transform: rotateY(180deg);
}

.card-16__face {
  position: absolute;
  inset: 0;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border-radius: 14px;
  padding: 26px 28px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: linear-gradient(135deg, rgba(212, 176, 99, 0.14) 0%, transparent 40%, transparent 60%, rgba(212, 176, 99, 0.06) 100%), linear-gradient(160deg, #16213e 0%, #0f172a 50%, #050815 100%);
  border: 1px solid rgba(212, 176, 99, 0.28);
}

.card-16__face::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 60%;
  height: 60%;
  background: radial-gradient(circle at top right, rgba(245, 217, 123, 0.18), transparent 60%);
  pointer-events: none;
}

.card-16__front {
  justify-content: space-between;
}

.card-16__back {
  transform: rotateY(180deg);
  justify-content: space-between;
}

.card-16__brand {
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-16__mark {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f5d97b 0%, #d4b063 50%, #9a7a3d 100%);
  box-shadow: inset 0 -2px 4px rgba(0, 0, 0, 0.25), inset 0 2px 4px rgba(255, 255, 255, 0.3), 0 2px 6px rgba(212, 176, 99, 0.35);
  position: relative;
}

.card-16__mark::before {
  content: '';
  position: absolute;
  inset: 8px;
  border-radius: 50%;
  background: linear-gradient(135deg, #050815, #16213e);
}

.card-16__mark::after {
  content: 'A';
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 15px;
  font-weight: 700;
  color: #f5d97b;
  text-shadow: 0 1px 2px rgba(0,0,0,0.6);
}

.card-16__brandname {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.24em;
  color: var(--gold);
  text-transform: uppercase;
}

.card-16__id {
  margin-bottom: 12px;
}

.card-16__name {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 26px;
  font-weight: 700;
  margin: 0 0 4px;
  color: #f8fafc;
  letter-spacing: -0.005em;
  line-height: 1.1;
}

.card-16__role {
  font-size: 11px;
  font-weight: 500;
  color: rgba(245, 217, 123, 0.85);
  margin: 0;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.card-16__hint {
  align-self: flex-end;
  font-size: 9.5px;
  color: rgba(148, 163, 184, 0.6);
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.card-16__backbrand {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: 0.28em;
  color: rgba(212, 176, 99, 0.75);
  text-transform: uppercase;
}

.card-16__contact {
  font-style: normal;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.card-16__row {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  padding-top: 4px;
  padding-bottom: 4px;
  border-bottom: 1px solid rgba(212, 176, 99, 0.14);
}

.card-16__row:last-child {
  border-bottom: 0;
}

.card-16__ico {
  color: var(--gold);
  flex-shrink: 0;
}

.card-16__row a {
  color: #e2e8f0;
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.01em;
  transition: color 0.18s;
}

.card-16__row a:hover {
  color: var(--gold-lite);
}

.card-16__row a:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
  border-radius: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .card-16__inner {
    transition: none;
  }

  .card-16__card:hover .card-16__inner,
    .card-16__card:focus-within .card-16__inner {
    transform: none;
  }
}
```
