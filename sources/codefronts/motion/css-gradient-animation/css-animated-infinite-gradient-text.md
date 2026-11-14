---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-animated-infinite-gradient-text/"
title: "CSS Animated Infinite Gradient Text"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "Multiple gradient text variants — a hero headline, sentence-level accents, animated stat counters, and a badge tag — all using background-clip: text with a…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Infinite Gradient Text
Source: https://codefronts.com/motion/css-gradient-animation/css-animated-infinite-gradient-text/

Multiple gradient text variants — a hero headline, sentence-level accents, animated stat counters, and a badge tag — all using background-clip: text with a sliding background-position keyframe to create a continuously flowing colour palette across the lettering.
## HTML
```html
<div class="ga-09">

  <div class="ga-09__tag-display">
    <span class="ga-09__tag-icon">✦</span>
    <span class="ga-09__tag-text ga-09__text">CSS background-clip gradient animation</span>
  </div>

  <div class="ga-09__hero">
    <span class="ga-09__pre">Build the future</span>
    <span class="ga-09__gradient-a ga-09__text">one pixel at a time.</span>
  </div>

  <p class="ga-09__sentence">
    Gradient text is great for
    <span class="ga-09__accent-b ga-09__text">hero headlines</span>,
    key statistics, and
    <span class="ga-09__accent-b ga-09__text" style="background-image:linear-gradient(90deg,#f97316,#eab308,#10b981,#f97316)">call-to-action</span>
    words that need to pop without colour conflicts.
  </p>

  <div class="ga-09__stats">
    <div class="ga-09__stat">
      <span class="ga-09__stat-num ga-09__stat-c1 ga-09__text">4.2M</span>
      <span class="ga-09__stat-label">Monthly users</span>
    </div>
    <div class="ga-09__stat">
      <span class="ga-09__stat-num ga-09__stat-c2 ga-09__text">99.98%</span>
      <span class="ga-09__stat-label">Uptime SLA</span>
    </div>
    <div class="ga-09__stat">
      <span class="ga-09__stat-num ga-09__stat-c3 ga-09__text">18ms</span>
      <span class="ga-09__stat-label">Avg. latency</span>
    </div>
  </div>

  <div class="ga-09__controls">
    <button class="ga-09__ctrl-btn" data-dur="12s">Slow</button>
    <button class="ga-09__ctrl-btn active" data-dur="5s">Normal</button>
    <button class="ga-09__ctrl-btn" data-dur="2.5s">Fast</button>
    <button class="ga-09__ctrl-btn" data-dur="1s">Blazing</button>
  </div>

</div>
```
## CSS
```css
.ga-09,
.ga-09 *,
.ga-09 *::before,
.ga-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-09 ::selection {
  background: rgba(168,85,247,.4);
  color: #fff;
}

.ga-09 {
  --bg: #060912;
  --dur: 5s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 48px;
  padding: 48px 24px;
}
/* ── Core gradient text technique ── */

.ga-09__text {
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  background-size: 300% 100%;
  animation: ga-09-slide var(--dur) linear infinite;
}

@keyframes ga-09-slide {
  0% {
    background-position: 0% 50%;
  }

  100% {
    background-position: -200% 50%;
  }
}
/* ── Variant A: hero headline ── */

.ga-09__hero {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ga-09__pre {
  font-size: clamp(2.4rem, 6vw, 4rem);
  font-weight: 900;
  line-height: 1.08;
  letter-spacing: -.035em;
  color: rgba(255,255,255,.9);
}

.ga-09__gradient-a {
  font-size: clamp(2.4rem, 6vw, 4rem);
  font-weight: 900;
  line-height: 1.08;
  letter-spacing: -.035em;
  background-image: linear-gradient(90deg,
      #a855f7, #ec4899, #f97316, #eab308, #10b981, #06b6d4, #6366f1, #a855f7
    );
}

.ga-09__gradient-a.ga-09__text {
  animation-duration: calc(var(--dur) * 1.4);
}
/* ── Variant B: word-level accents in a sentence ── */

.ga-09__sentence {
  font-size: clamp(1.15rem, 2.5vw, 1.5rem);
  font-weight: 600;
  color: rgba(255,255,255,.55);
  line-height: 1.6;
  text-align: center;
  max-width: 580px;
}

.ga-09__accent-b {
  font-weight: 800;
  background-image: linear-gradient(90deg,
      #06b6d4, #818cf8, #ec4899, #f97316, #06b6d4
    );
  display: inline;
}

.ga-09__accent-b.ga-09__text {
  animation-duration: calc(var(--dur) * .8);
}
/* ── Variant C: display counters / stats ── */

.ga-09__stats {
  display: flex;
  gap: 40px;
  flex-wrap: wrap;
  justify-content: center;
}

.ga-09__stat {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.ga-09__stat-num {
  font-size: clamp(2rem, 4vw, 2.8rem);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1;
}

.ga-09__stat-c1 {
  background-image: linear-gradient(90deg, #06b6d4, #6366f1, #a855f7, #06b6d4);
}

.ga-09__stat-c2 {
  background-image: linear-gradient(90deg, #10b981, #06b6d4, #818cf8, #10b981);
  animation-delay: -.8s;
}

.ga-09__stat-c3 {
  background-image: linear-gradient(90deg, #f97316, #ec4899, #a855f7, #f97316);
  animation-delay: -1.6s;
}

.ga-09__stat-label {
  font-size: .7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: rgba(255,255,255,.3);
}
/* ── Variant D: large display tag ── */

.ga-09__tag-display {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 8px 20px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.03);
}

.ga-09__tag-icon {
  font-size: .9rem;
}

.ga-09__tag-text {
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .05em;
  background-image: linear-gradient(90deg, #c084fc, #818cf8, #67e8f9, #34d399, #c084fc);
}
/* Speed palette buttons */

.ga-09__controls {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
}

.ga-09__ctrl-btn {
  padding: 5px 14px;
  border-radius: 7px;
  font-size: .73rem;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  border: 1px solid rgba(255,255,255,.1);
  background: rgba(255,255,255,.05);
  color: rgba(255,255,255,.4);
  cursor: pointer;
  transition: all .2s;
}

.ga-09__ctrl-btn.active,
.ga-09__ctrl-btn:hover {
  background: rgba(168,85,247,.15);
  border-color: rgba(168,85,247,.3);
  color: #d8b4fe;
}

@media (prefers-reduced-motion: reduce) {
  .ga-09__text {
    animation: none;
    background-position: 0% 50%;
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-09');
  w.querySelectorAll('.ga-09__ctrl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-09__ctrl-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.style.setProperty('--dur', btn.dataset.dur);
    });
  });
})();
```
