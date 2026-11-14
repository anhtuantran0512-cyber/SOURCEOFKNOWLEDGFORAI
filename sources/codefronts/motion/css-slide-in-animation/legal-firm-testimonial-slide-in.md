---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/legal-firm-testimonial-slide-in/"
title: "Legal Firm Testimonial Slide-In"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A prestige legal firm testimonial section where two client testimonials slide in from opposite sides — the trust-signal layout used by BigLaw firms, boutique…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Legal Firm Testimonial Slide-In
Source: https://codefronts.com/motion/css-slide-in-animation/legal-firm-testimonial-slide-in/

A prestige legal firm testimonial section where two client testimonials slide in from opposite sides — the trust-signal layout used by BigLaw firms, boutique legal practices, and high-net-worth financial advisors.
## HTML
```html
<div class="sl-08">
  <div class="sl-08__inner">
    <p class="sl-08__kicker">Client testimonials</p>
    <h2 class="sl-08__title">Trusted by leading Fortune 500 general counsel</h2>
    <div class="sl-08__row">
      <blockquote class="sl-08__quote">
        <span class="sl-08__q" aria-hidden="true">"</span>
        <p>"Their M&A team closed a $2.4B cross-border deal in six weeks — a timeline that would have taken 18 months at previous firms we've retained."</p>
        <footer>
          <div class="sl-08__ava" style="--g:linear-gradient(135deg,#4a5f7a,#0a2540)">JR</div>
          <div>
            <strong>Jonathan Reeves</strong>
            <em>General Counsel, Meridian Capital Group</em>
            <span class="sl-08__rank">Fortune 250 client since 2018</span>
          </div>
        </footer>
      </blockquote>
      <blockquote class="sl-08__quote">
        <span class="sl-08__q" aria-hidden="true">"</span>
        <p>"After 15 years working with top-tier BigLaw, this firm consistently delivered outcomes we did not think possible. Best litigation counsel in the industry."</p>
        <footer>
          <div class="sl-08__ava" style="--g:linear-gradient(135deg,#b8934a,#6b5528)">EM</div>
          <div>
            <strong>Elena Martinez, Esq.</strong>
            <em>Chief Legal Officer, Ashworth Industries</em>
            <span class="sl-08__rank">Chambers-ranked in M&A · 2024</span>
          </div>
        </footer>
      </blockquote>
    </div>
    <p class="sl-08__disc">Prior results do not guarantee similar outcome. Case matters vary.</p>
  </div>
</div>
```
## CSS
```css
.sl-08 {
  --bg: #faf9f5;
  --card: #fff;
  --navy: #0a2540;
  --gold: #b8934a;
  --ink: #0a2540;
  --sub: #5c6b80;
  --line: #e6e2d6;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 100% at 50% 0%, rgba(10,37,64,.04) 0%, transparent 60%), var(--bg);
  color: var(--ink);
}

.sl-08 *,
.sl-08 *::before,
.sl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-08 ::selection {
  background: var(--navy);
  color: #fff;
}

.sl-08__inner {
  width: 100%;
  max-width: 960px;
  text-align: center;
}

.sl-08__kicker {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: .85rem;
  font-weight: 400;
  font-style: italic;
  letter-spacing: .05em;
  color: var(--gold);
  margin-bottom: 8px;
}

.sl-08__title {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: clamp(1.6rem,3.2vw,2.2rem);
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.2;
  margin-bottom: 36px;
}

.sl-08__row {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 24px;
  margin-bottom: 32px;
}

.sl-08__quote {
  position: relative;
  padding: 32px 30px 28px;
  border-radius: 2px;
  background: var(--card);
  border-left: 3px solid var(--gold);
  box-shadow: 0 12px 28px -14px rgba(10,37,64,.18);
  text-align: left;
}

.sl-08__quote:nth-child(1) {
  opacity: 0;
  transform: translateX(-40px);
  animation: sl-08-left .65s cubic-bezier(.22,1,.36,1) .2s forwards;
}

.sl-08__quote:nth-child(2) {
  opacity: 0;
  transform: translateX(40px);
  animation: sl-08-right .65s cubic-bezier(.22,1,.36,1) .4s forwards;
}

.sl-08__q {
  position: absolute;
  top: 8px;
  left: 20px;
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 5rem;
  line-height: 1;
  color: var(--gold);
  opacity: .2;
}

.sl-08__quote p {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.05rem;
  font-weight: 400;
  line-height: 1.55;
  color: var(--ink);
  margin-bottom: 22px;
  position: relative;
  z-index: 1;
}

.sl-08__quote footer {
  display: flex;
  align-items: center;
  gap: 14px;
  padding-top: 16px;
  border-top: 1px solid var(--line);
}

.sl-08__ava {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  flex-shrink: 0;
  background: var(--g,#333);
  color: #fff;
  font-family: 'Playfair Display',Georgia,serif;
  font-size: .85rem;
  font-weight: 800;
  letter-spacing: .02em;
}

.sl-08__quote strong {
  display: block;
  font-size: .9rem;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -.01em;
}

.sl-08__quote em {
  display: block;
  font-size: .78rem;
  color: var(--sub);
  font-style: normal;
  margin-top: 1px;
}

.sl-08__rank {
  display: inline-block;
  margin-top: 4px;
  font-size: .68rem;
  font-weight: 600;
  color: var(--gold);
  letter-spacing: .02em;
}

.sl-08__disc {
  font-size: .72rem;
  color: var(--sub);
  font-style: italic;
  opacity: 0;
  animation: sl-08-fade .3s ease-out .8s forwards;
}

@keyframes sl-08-left {
  from {
    opacity: 0;
    transform: translateX(-40px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes sl-08-right {
  from {
    opacity: 0;
    transform: translateX(40px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes sl-08-fade {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-08 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 720px) {
  .sl-08__row {
    grid-template-columns: 1fr;
  }
}
```
