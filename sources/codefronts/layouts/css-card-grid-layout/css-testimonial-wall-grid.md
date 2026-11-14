---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-testimonial-wall-grid/"
title: "CSS Testimonial Wall Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "An asymmetric testimonial wall with one featured 2x2 hero quote and 5 supporting testimonial cards — each with customer avatar, name, role, company, star…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Testimonial Wall Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-testimonial-wall-grid/

An asymmetric testimonial wall with one featured 2x2 hero quote and 5 supporting testimonial cards — each with customer avatar, name, role, company, star rating, and quote. The exact pattern Vercel, Linear, and Stripe use on their homepages to stack social proof at scale.
## HTML
```html
<div class="cg-11">
  <div class="cg-11__head">
    <span class="cg-11__kicker">Customer love</span>
    <h2 class="cg-11__title">2,400+ teams ship faster.</h2>
  </div>
  <div class="cg-11__grid">

    <article class="cg-11__card cg-11__card--featured">
      <div class="cg-11__stars" aria-label="5 of 5 stars">★★★★★</div>
      <blockquote class="cg-11__quote">
        We replaced four tools with one. Our deploys went from 12 minutes to under 90 seconds, and the whole engineering team finally agrees on something. Worth every penny.
      </blockquote>
      <footer class="cg-11__attr">
        <div class="cg-11__avatar cg-11__avatar--1"></div>
        <div class="cg-11__who">
          <span class="cg-11__name">Maya Chen</span>
          <span class="cg-11__role">VP Engineering · <strong>Linear</strong></span>
        </div>
      </footer>
    </article>

    <article class="cg-11__card">
      <div class="cg-11__stars">★★★★★</div>
      <blockquote class="cg-11__quote">"The onboarding alone saved us a week. We were live in three hours."</blockquote>
      <footer class="cg-11__attr">
        <div class="cg-11__avatar cg-11__avatar--2"></div>
        <div class="cg-11__who">
          <span class="cg-11__name">Liam Okonkwo</span>
          <span class="cg-11__role">CTO · <strong>Plaid</strong></span>
        </div>
      </footer>
    </article>

    <article class="cg-11__card">
      <div class="cg-11__stars">★★★★★</div>
      <blockquote class="cg-11__quote">"Honestly the best support team I've worked with in 12 years of building SaaS."</blockquote>
      <footer class="cg-11__attr">
        <div class="cg-11__avatar cg-11__avatar--3"></div>
        <div class="cg-11__who">
          <span class="cg-11__name">Aria Patel</span>
          <span class="cg-11__role">Founder · <strong>Resend</strong></span>
        </div>
      </footer>
    </article>

    <article class="cg-11__card">
      <div class="cg-11__stars">★★★★<span class="cg-11__stars--dim">★</span></div>
      <blockquote class="cg-11__quote">"4 stars only because we keep finding new things we wish it did. It does most of them next quarter."</blockquote>
      <footer class="cg-11__attr">
        <div class="cg-11__avatar cg-11__avatar--4"></div>
        <div class="cg-11__who">
          <span class="cg-11__name">Noah Reyes</span>
          <span class="cg-11__role">Eng Lead · <strong>Vercel</strong></span>
        </div>
      </footer>
    </article>

    <article class="cg-11__card">
      <div class="cg-11__stars">★★★★★</div>
      <blockquote class="cg-11__quote">"Our incident response time dropped 73%. Board noticed."</blockquote>
      <footer class="cg-11__attr">
        <div class="cg-11__avatar cg-11__avatar--5"></div>
        <div class="cg-11__who">
          <span class="cg-11__name">Zoe Larsson</span>
          <span class="cg-11__role">SRE Manager · <strong>Stripe</strong></span>
        </div>
      </footer>
    </article>

    <article class="cg-11__card">
      <div class="cg-11__stars">★★★★★</div>
      <blockquote class="cg-11__quote">"We tried five alternatives. Came back here on day three."</blockquote>
      <footer class="cg-11__attr">
        <div class="cg-11__avatar cg-11__avatar--6"></div>
        <div class="cg-11__who">
          <span class="cg-11__name">Sam Okafor</span>
          <span class="cg-11__role">Product · <strong>Notion</strong></span>
        </div>
      </footer>
    </article>

  </div>
</div>
```
## CSS
```css
.cg-11,
.cg-11 *,
.cg-11 *::before,
.cg-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-11 ::selection {
  background: #0f172a;
  color: #fff;
}

.cg-11 {
  --bg: #f8fafc;
  --card: #ffffff;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --accent: #f59e0b;
  --feat-bg: #0f172a;
  --feat-ink: #f8fafc;
  min-height: 100vh;
  background: var(--bg);
  padding: clamp(32px,4vw,64px) clamp(20px,3vw,48px);
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",sans-serif;
  color: var(--ink);
}

.cg-11__head {
  text-align: center;
  margin-bottom: clamp(32px,4vw,48px);
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.cg-11__kicker {
  display: inline-block;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 10px;
}

.cg-11__title {
  font-size: clamp(1.8rem,3.4vw,2.6rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
}

.cg-11__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  grid-auto-rows: minmax(200px,auto);
  gap: clamp(14px,1.6vw,20px);
  max-width: 1180px;
  margin: 0 auto;
}

.cg-11__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: clamp(18px,2vw,24px);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 16px;
  transition: transform .25s,box-shadow .25s;
}

.cg-11__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 28px -14px rgba(15,23,42,.18);
}

.cg-11__card--featured {
  grid-column: span 2;
  grid-row: span 2;
  background: var(--feat-bg);
  color: var(--feat-ink);
  border-color: var(--feat-bg);
}

.cg-11__stars {
  color: var(--accent);
  font-size: .95rem;
  letter-spacing: .1em;
  font-feature-settings: "tnum";
}

.cg-11__stars--dim {
  color: rgba(100,116,139,.4);
}

.cg-11__card--featured .cg-11__stars {
  font-size: 1.1rem;
}

.cg-11__quote {
  font-size: clamp(.94rem,1.05vw,1rem);
  line-height: 1.5;
  color: var(--ink);
}

.cg-11__card--featured .cg-11__quote {
  color: var(--feat-ink);
  font-size: clamp(1.15rem,1.8vw,1.5rem);
  line-height: 1.35;
  font-weight: 500;
  letter-spacing: -.005em;
}

.cg-11__attr {
  display: flex;
  align-items: center;
  gap: 12px;
}

.cg-11__avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  flex-shrink: 0;
}

.cg-11__card--featured .cg-11__avatar {
  width: 48px;
  height: 48px;
}

.cg-11__avatar--1 {
  background: linear-gradient(135deg,#f9c1cf,#d97a99);
}

.cg-11__avatar--2 {
  background: linear-gradient(135deg,#a7c8e7,#5b8fd9);
}

.cg-11__avatar--3 {
  background: linear-gradient(135deg,#c5da9c,#7aa852);
}

.cg-11__avatar--4 {
  background: linear-gradient(135deg,#f7b88a,#d97f4f);
}

.cg-11__avatar--5 {
  background: linear-gradient(135deg,#c4b5fd,#9b87e5);
}

.cg-11__avatar--6 {
  background: linear-gradient(135deg,#fef0a3,#e6c54a);
}

.cg-11__who {
  display: flex;
  flex-direction: column;
  gap: 1px;
  min-width: 0;
}

.cg-11__name {
  font-size: .92rem;
  font-weight: 700;
}

.cg-11__role {
  font-size: .78rem;
  color: var(--muted);
}

.cg-11__card--featured .cg-11__role {
  color: rgba(248,250,252,.65);
}

.cg-11__role strong {
  font-weight: 700;
  color: var(--ink);
}

.cg-11__card--featured .cg-11__role strong {
  color: var(--feat-ink);
}

@media (max-width: 960px) {
  .cg-11__grid {
    grid-template-columns: repeat(2,1fr);
  }

  .cg-11__card--featured {
    grid-column: span 2;
    grid-row: span 1;
  }
}

@media (max-width: 560px) {
  .cg-11__grid {
    grid-template-columns: 1fr;
  }

  .cg-11__card--featured {
    grid-column: span 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-11__card {
    transition: none;
  }
}
```
