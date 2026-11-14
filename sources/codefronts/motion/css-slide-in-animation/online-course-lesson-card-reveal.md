---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/online-course-lesson-card-reveal/"
title: "Online Course Lesson Card Reveal"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "Four EdTech online-course lesson cards that slide up from below in a grid, each showing a subject-colored thumbnail, course title, instructor name, star…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Online Course Lesson Card Reveal
Source: https://codefronts.com/motion/css-slide-in-animation/online-course-lesson-card-reveal/

Four EdTech online-course lesson cards that slide up from below in a grid, each showing a subject-colored thumbnail, course title, instructor name, star rating, student count, hours, and price — the layout used by Udemy, Coursera, Skillshare, and Domestika.
## HTML
```html
<div class="sl-11">
  <div class="sl-11__inner">
    <div class="sl-11__head">
      <p class="sl-11__kicker">Popular in Web Development</p>
      <h2>Trending courses this week</h2>
    </div>
    <div class="sl-11__grid">
      <article class="sl-11__card">
        <div class="sl-11__thumb" style="--g:linear-gradient(135deg,#8b5cf6,#6366f1)">
          <span class="sl-11__badge">Bestseller</span>
        </div>
        <div class="sl-11__body">
          <span class="sl-11__cat">Web Development</span>
          <h3>Modern CSS: From Zero to Production</h3>
          <p class="sl-11__inst">Alex Rivera · Senior Engineer</p>
          <div class="sl-11__meta">
            <span class="sl-11__stars">★★★★★</span>
            <strong>4.8</strong>
            <small>(12.4K students)</small>
          </div>
          <div class="sl-11__foot">
            <span class="sl-11__hrs">28 hrs · 142 lessons</span>
            <div class="sl-11__price"><strong>$19.99</strong><del>$99.99</del></div>
          </div>
        </div>
      </article>
      <article class="sl-11__card">
        <div class="sl-11__thumb" style="--g:linear-gradient(135deg,#f97316,#dc2626)">
          <span class="sl-11__badge">Bestseller</span>
        </div>
        <div class="sl-11__body">
          <span class="sl-11__cat">JavaScript</span>
          <h3>React &amp; Next.js: The Complete Guide 2027</h3>
          <p class="sl-11__inst">Maya Chen · Full-Stack Lead</p>
          <div class="sl-11__meta">
            <span class="sl-11__stars">★★★★★</span>
            <strong>4.9</strong>
            <small>(8.7K students)</small>
          </div>
          <div class="sl-11__foot">
            <span class="sl-11__hrs">42 hrs · 218 lessons</span>
            <div class="sl-11__price"><strong>$24.99</strong><del>$129.99</del></div>
          </div>
        </div>
      </article>
      <article class="sl-11__card">
        <div class="sl-11__thumb" style="--g:linear-gradient(135deg,#10b981,#0891b2)"></div>
        <div class="sl-11__body">
          <span class="sl-11__cat">DevOps</span>
          <h3>AWS Solutions Architect: Real-World Practice</h3>
          <p class="sl-11__inst">Jordan Kim · Cloud Architect</p>
          <div class="sl-11__meta">
            <span class="sl-11__stars">★★★★☆</span>
            <strong>4.6</strong>
            <small>(3.2K students)</small>
          </div>
          <div class="sl-11__foot">
            <span class="sl-11__hrs">18 hrs · 87 lessons</span>
            <div class="sl-11__price"><strong>$14.99</strong><del>$79.99</del></div>
          </div>
        </div>
      </article>
      <article class="sl-11__card">
        <div class="sl-11__thumb" style="--g:linear-gradient(135deg,#ec4899,#8b5cf6)"></div>
        <div class="sl-11__body">
          <span class="sl-11__cat">Design</span>
          <h3>UI/UX Design: Systems, Tokens &amp; Accessibility</h3>
          <p class="sl-11__inst">Sarah Martinez · Design Lead, Figma</p>
          <div class="sl-11__meta">
            <span class="sl-11__stars">★★★★★</span>
            <strong>4.7</strong>
            <small>(2.1K students)</small>
          </div>
          <div class="sl-11__foot">
            <span class="sl-11__hrs">22 hrs · 108 lessons</span>
            <div class="sl-11__price"><strong>$16.99</strong><del>$89.99</del></div>
          </div>
        </div>
      </article>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-11 {
  --bg: #faf9fc;
  --card: #fff;
  --accent: #8b5cf6;
  --sale: #f97316;
  --ink: #1a1a2e;
  --sub: #6b7280;
  --line: #e5e7eb;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 90% at 20% 0%, rgba(139,92,246,.06) 0%, transparent 55%), var(--bg);
  color: var(--ink);
}

.sl-11 *,
.sl-11 *::before,
.sl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-11 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-11__inner {
  width: 100%;
  max-width: 960px;
}

.sl-11__head {
  margin-bottom: 24px;
}

.sl-11__kicker {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.sl-11__head h2 {
  font-size: clamp(1.4rem,2.8vw,1.8rem);
  font-weight: 800;
  letter-spacing: -.02em;
}

.sl-11__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 18px;
}

.sl-11__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 8px 20px -12px rgba(139,92,246,.15);
  opacity: 0;
  transform: translateY(30px);
  animation: sl-11-card .55s cubic-bezier(.22,1,.36,1) forwards;
  transition: transform .18s ease,box-shadow .18s ease;
}

.sl-11__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 28px -12px rgba(139,92,246,.22);
}

.sl-11__card:nth-child(1) {
  animation-delay: .12s;
}

.sl-11__card:nth-child(2) {
  animation-delay: .24s;
}

.sl-11__card:nth-child(3) {
  animation-delay: .36s;
}

.sl-11__card:nth-child(4) {
  animation-delay: .48s;
}

.sl-11__thumb {
  position: relative;
  aspect-ratio: 16/9;
  background: var(--g,#ccc);
}

.sl-11__badge {
  position: absolute;
  top: 10px;
  left: 10px;
  padding: 4px 10px;
  border-radius: 4px;
  background: var(--sale);
  color: #fff;
  font-size: .65rem;
  font-weight: 800;
  letter-spacing: .04em;
  text-transform: uppercase;
}

.sl-11__body {
  padding: 16px 18px 18px;
}

.sl-11__cat {
  display: inline-block;
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.sl-11__body h3 {
  font-size: .98rem;
  font-weight: 700;
  letter-spacing: -.01em;
  line-height: 1.25;
  margin-bottom: 4px;
}

.sl-11__inst {
  font-size: .78rem;
  color: var(--sub);
  margin-bottom: 8px;
}

.sl-11__meta {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 14px;
}

.sl-11__stars {
  color: #f59e0b;
  font-size: .82rem;
  letter-spacing: 1px;
  line-height: 1;
}

.sl-11__meta strong {
  font-size: .85rem;
  font-weight: 800;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.sl-11__meta small {
  font-size: .72rem;
  color: var(--sub);
}

.sl-11__foot {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 8px;
  padding-top: 12px;
  border-top: 1px solid var(--line);
}

.sl-11__hrs {
  font-size: .72rem;
  color: var(--sub);
  font-variant-numeric: tabular-nums;
}

.sl-11__price {
  display: flex;
  align-items: baseline;
  gap: 6px;
}

.sl-11__price strong {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.sl-11__price del {
  font-size: .78rem;
  color: var(--sub);
  text-decoration: line-through;
  font-variant-numeric: tabular-nums;
}

@keyframes sl-11-card {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-11__card {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 640px) {
  .sl-11__grid {
    grid-template-columns: 1fr;
  }
}
```
