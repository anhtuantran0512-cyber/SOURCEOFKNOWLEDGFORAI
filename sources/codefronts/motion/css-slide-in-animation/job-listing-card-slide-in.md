---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/job-listing-card-slide-in/"
title: "Job Listing Card Slide-In"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "Three job posting cards that slide up from below, each showing company logo/name, job title, location, salary range, work-arrangement badges (Remote / Hybrid…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Job Listing Card Slide-In
Source: https://codefronts.com/motion/css-slide-in-animation/job-listing-card-slide-in/

Three job posting cards that slide up from below, each showing company logo/name, job title, location, salary range, work-arrangement badges (Remote / Hybrid / On-site), and "Apply now" CTA — the layout used by Indeed, LinkedIn Jobs, Wellfound, and Ashby.
## HTML
```html
<div class="sl-12">
  <div class="sl-12__inner">
    <div class="sl-12__head">
      <p class="sl-12__kicker">Software Engineering · San Francisco Bay Area</p>
      <h2>3 new jobs match your search</h2>
    </div>
    <article class="sl-12__job">
      <div class="sl-12__avatar" style="--g:linear-gradient(135deg,#0a66c2,#0284c7)">L</div>
      <div class="sl-12__body">
        <div class="sl-12__topline">
          <span class="sl-12__new">New</span>
          <span class="sl-12__posted">Posted 2 days ago</span>
        </div>
        <h3>Senior Frontend Engineer</h3>
        <p class="sl-12__co">Linear · San Francisco, CA</p>
        <div class="sl-12__chips">
          <span class="sl-12__chip sl-12__chip--rem">Remote (US)</span>
          <span class="sl-12__chip sl-12__chip--full">Full-time</span>
          <span class="sl-12__chip">Series B</span>
        </div>
        <div class="sl-12__salary">$180K – $240K + equity</div>
      </div>
      <button class="sl-12__apply">Apply</button>
    </article>
    <article class="sl-12__job">
      <div class="sl-12__avatar" style="--g:linear-gradient(135deg,#22c55e,#0a8754)">S</div>
      <div class="sl-12__body">
        <div class="sl-12__topline">
          <span class="sl-12__posted">Posted 5 days ago</span>
        </div>
        <h3>Staff Software Engineer, Platform</h3>
        <p class="sl-12__co">Stripe · Multiple locations</p>
        <div class="sl-12__chips">
          <span class="sl-12__chip sl-12__chip--hyb">Hybrid</span>
          <span class="sl-12__chip sl-12__chip--full">Full-time</span>
          <span class="sl-12__chip">Public</span>
        </div>
        <div class="sl-12__salary">$220K – $320K + equity + bonus</div>
      </div>
      <button class="sl-12__apply">Apply</button>
    </article>
    <article class="sl-12__job">
      <div class="sl-12__avatar" style="--g:linear-gradient(135deg,#f43f5e,#c026d3)">V</div>
      <div class="sl-12__body">
        <div class="sl-12__topline">
          <span class="sl-12__posted">Posted 1 week ago</span>
        </div>
        <h3>Full-Stack Engineer (Founding Team)</h3>
        <p class="sl-12__co">Vercel · Palo Alto, CA</p>
        <div class="sl-12__chips">
          <span class="sl-12__chip sl-12__chip--onsite">On-site</span>
          <span class="sl-12__chip sl-12__chip--full">Full-time</span>
          <span class="sl-12__chip">Seed</span>
        </div>
        <div class="sl-12__salary">$160K – $200K + significant equity</div>
      </div>
      <button class="sl-12__apply">Apply</button>
    </article>
  </div>
</div>
```
## CSS
```css
.sl-12 {
  --bg: #f5f7fa;
  --card: #fff;
  --navy: #0a2540;
  --good: #16a34a;
  --ink: #0a2540;
  --sub: #5b6b7d;
  --line: #e1e6ee;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 90% at 20% 0%, rgba(10,37,64,.05) 0%, transparent 55%), var(--bg);
  color: var(--ink);
}

.sl-12 *,
.sl-12 *::before,
.sl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-12 ::selection {
  background: var(--navy);
  color: #fff;
}

.sl-12__inner {
  width: 100%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sl-12__head {
  margin-bottom: 8px;
}

.sl-12__kicker {
  font-size: .72rem;
  font-weight: 600;
  color: var(--sub);
  margin-bottom: 4px;
}

.sl-12__head h2 {
  font-size: 1.3rem;
  font-weight: 800;
  letter-spacing: -.02em;
}

.sl-12__job {
  display: grid;
  grid-template-columns: 56px 1fr auto;
  gap: 16px;
  padding: 18px 20px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  box-shadow: 0 6px 16px -10px rgba(10,37,64,.12);
  opacity: 0;
  transform: translateY(30px);
  animation: sl-12-job .55s cubic-bezier(.22,1,.36,1) forwards;
  transition: transform .18s ease,box-shadow .18s ease;
}

.sl-12__job:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px -10px rgba(10,37,64,.2);
}

.sl-12__job:nth-child(2) {
  animation-delay: .2s;
}

.sl-12__job:nth-child(3) {
  animation-delay: .35s;
}

.sl-12__job:nth-child(4) {
  animation-delay: .5s;
}

.sl-12__avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  border-radius: 10px;
  background: var(--g,#333);
  color: #fff;
  font-size: 1.3rem;
  font-weight: 800;
}

.sl-12__body {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
}

.sl-12__topline {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 2px;
}

.sl-12__new {
  padding: 2px 7px;
  border-radius: 4px;
  background: rgba(22,163,74,.15);
  color: var(--good);
  font-size: .62rem;
  font-weight: 800;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.sl-12__posted {
  font-size: .7rem;
  color: var(--sub);
}

.sl-12__body h3 {
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.01em;
  line-height: 1.2;
}

.sl-12__co {
  font-size: .82rem;
  color: var(--sub);
  margin-bottom: 4px;
}

.sl-12__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-bottom: 4px;
}

.sl-12__chip {
  padding: 3px 8px;
  border-radius: 5px;
  background: rgba(148,163,184,.12);
  color: var(--sub);
  font-size: .68rem;
  font-weight: 600;
}

.sl-12__chip--rem {
  background: rgba(34,197,94,.14);
  color: #0a8754;
}

.sl-12__chip--hyb {
  background: rgba(59,130,246,.14);
  color: #1d4ed8;
}

.sl-12__chip--onsite {
  background: rgba(245,158,11,.14);
  color: #b45309;
}

.sl-12__chip--full {
  background: rgba(139,92,246,.12);
  color: #7c3aed;
}

.sl-12__salary {
  font-size: .85rem;
  font-weight: 700;
  color: var(--good);
  font-variant-numeric: tabular-nums;
  letter-spacing: -.005em;
  margin-top: 2px;
}

.sl-12__apply {
  align-self: center;
  padding: 10px 22px;
  border: 1px solid var(--navy);
  border-radius: 8px;
  background: var(--navy);
  color: #fff;
  font-family: inherit;
  font-size: .82rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .18s ease;
}

.sl-12__apply:hover {
  background: #0f3660;
}

@keyframes sl-12-job {
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
  .sl-12__job {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 640px) {
  .sl-12__job {
    grid-template-columns: 48px 1fr;
    grid-template-rows: auto auto;
  }

  .sl-12__avatar {
    width: 48px;
    height: 48px;
  }

  .sl-12__apply {
    grid-column: 1/-1;
    width: 100%;
  }
}
```
