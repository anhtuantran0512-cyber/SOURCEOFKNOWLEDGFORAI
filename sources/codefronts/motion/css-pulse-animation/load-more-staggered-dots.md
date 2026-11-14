---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/load-more-staggered-dots/"
title: "Load More Staggered Dots"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "An infinite-scroll feed pagination indicator — three horizontal slate dots pulsing in a staggered sequence at the bottom of a feed container, signaling…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Load More Staggered Dots
Source: https://codefronts.com/motion/css-pulse-animation/load-more-staggered-dots/

An infinite-scroll feed pagination indicator — three horizontal slate dots pulsing in a staggered sequence at the bottom of a feed container, signaling "loading more content, hang on." Neutral off-white canvas (#fafafa) with slate (#475569) dots and light gray ghost cards above (representing already-loaded content). Twitter / Threads / Reddit infinite-scroll aesthetic — quiet, minimal, honest.
## HTML
```html
<div class="pl-13">
  <div class="pl-13__feed">
    <div class="pl-13__card">
      <div class="pl-13__card-head">
        <span class="pl-13__avatar" aria-hidden="true"></span>
        <div>
          <div class="pl-13__name">Priya Iyer</div>
          <div class="pl-13__stamp">2 min ago · Threads</div>
        </div>
      </div>
      <div class="pl-13__text pl-13__text--wide"></div>
      <div class="pl-13__text pl-13__text--mid"></div>
    </div>
    <div class="pl-13__card">
      <div class="pl-13__card-head">
        <span class="pl-13__avatar" aria-hidden="true" style="background:linear-gradient(135deg,#f97316,#ea580c)"></span>
        <div>
          <div class="pl-13__name">Marcus Chen</div>
          <div class="pl-13__stamp">8 min ago · Design</div>
        </div>
      </div>
      <div class="pl-13__text pl-13__text--wide"></div>
      <div class="pl-13__text pl-13__text--short"></div>
    </div>
    <div class="pl-13__card">
      <div class="pl-13__card-head">
        <span class="pl-13__avatar" aria-hidden="true" style="background:linear-gradient(135deg,#a78bfa,#7c3aed)"></span>
        <div>
          <div class="pl-13__name">Kodachi</div>
          <div class="pl-13__stamp">14 min ago · Ambient</div>
        </div>
      </div>
      <div class="pl-13__text pl-13__text--wide"></div>
      <div class="pl-13__text pl-13__text--mid"></div>
      <div class="pl-13__text pl-13__text--short"></div>
    </div>
    <div class="pl-13__loader" role="status" aria-live="polite" aria-label="Loading more posts">
      <div class="pl-13__dots" aria-hidden="true">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <span class="pl-13__loader-text">Loading more</span>
    </div>
  </div>
</div>
```
## CSS
```css
.pl-13 {
  --page-bg: #fafafa;
  --card: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --dot: #475569;
  --placeholder: #e2e8f0;
  --line: #e5e5e5;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: start center;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.pl-13 *,
.pl-13 *::before,
.pl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-13 ::selection {
  background: var(--dot);
  color: #fff;
}

.pl-13__feed {
  width: min(500px,100%);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.pl-13__card {
  padding: 14px 16px;
  border-radius: 10px;
  background: var(--card);
  border: 1px solid var(--line);
  box-shadow: 0 1px 2px rgba(15,23,42,.04);
  opacity: .85;
}

.pl-13__card-head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.pl-13__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  flex-shrink: 0;
  background: linear-gradient(135deg,#3b82f6,#1e40af);
}

.pl-13__name {
  font-size: .82rem;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -.005em;
}

.pl-13__stamp {
  font-size: .7rem;
  color: var(--sub);
  margin-top: 1px;
}

.pl-13__text {
  height: 10px;
  border-radius: 3px;
  background: var(--placeholder);
  margin-bottom: 6px;
}

.pl-13__text--wide {
  width: 95%;
}

.pl-13__text--mid {
  width: 72%;
}

.pl-13__text--short {
  width: 48%;
}

.pl-13__loader {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 20px 0;
}

.pl-13__dots {
  display: flex;
  gap: 6px;
  height: 8px;
}

.pl-13__dots span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--dot);
  animation: pl-13-dot 1.4s ease-in-out infinite;
}

.pl-13__dots span:nth-child(1) {
  animation-delay: 0s;
}

.pl-13__dots span:nth-child(2) {
  animation-delay: .2s;
}

.pl-13__dots span:nth-child(3) {
  animation-delay: .4s;
}

@keyframes pl-13-dot {
  0%,
    100% {
    transform: translateY(0);
    opacity: .4;
  }

  40% {
    transform: translateY(-8px);
    opacity: 1;
  }
}

.pl-13__loader-text {
  font-size: .75rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

@media (prefers-reduced-motion: reduce) {
  .pl-13__dots span {
    animation: none!important;
    transform: none!important;
    opacity: 1!important;
  }
}
```
