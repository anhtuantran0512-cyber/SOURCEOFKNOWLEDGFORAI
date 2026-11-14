---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/fitness-class-schedule-slide-in/"
title: "Fitness Class Schedule Slide-In"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "Four fitness class time-slots that slide in from the left in sequence, each showing time, class type, instructor, duration, spots-remaining indicator, and…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fitness Class Schedule Slide-In
Source: https://codefronts.com/motion/css-slide-in-animation/fitness-class-schedule-slide-in/

Four fitness class time-slots that slide in from the left in sequence, each showing time, class type, instructor, duration, spots-remaining indicator, and difficulty level — the layout used by ClassPass, Peloton, Mindbody, and boutique fitness studios.
## HTML
```html
<div class="sl-14">
  <div class="sl-14__inner">
    <div class="sl-14__head">
      <p class="sl-14__kicker">Thursday · Nov 6</p>
      <h2>Today's classes</h2>
    </div>
    <div class="sl-14__list">
      <div class="sl-14__slot">
        <div class="sl-14__time">6:00<small>AM</small></div>
        <div class="sl-14__body">
          <h3>HIIT Cardio Blast</h3>
          <p>Alex Rivera · 45 min · <span class="sl-14__diff">●●○</span> Intermediate</p>
        </div>
        <div class="sl-14__book">
          <span class="sl-14__spots sl-14__spots--low">3 spots left!</span>
          <button class="sl-14__btn">Book</button>
        </div>
      </div>
      <div class="sl-14__slot">
        <div class="sl-14__time">8:30<small>AM</small></div>
        <div class="sl-14__body">
          <h3>Sunrise Yoga Flow</h3>
          <p>Maya Chen · 60 min · <span class="sl-14__diff">●○○</span> All levels</p>
        </div>
        <div class="sl-14__book">
          <span class="sl-14__spots">12 spots open</span>
          <button class="sl-14__btn">Book</button>
        </div>
      </div>
      <div class="sl-14__slot">
        <div class="sl-14__time">12:15<small>PM</small></div>
        <div class="sl-14__body">
          <h3>Power Cycle · 45</h3>
          <p>Jordan Kim · 45 min · <span class="sl-14__diff">●●●</span> Advanced</p>
        </div>
        <div class="sl-14__book">
          <span class="sl-14__spots sl-14__spots--waitlist">Waitlist</span>
          <button class="sl-14__btn sl-14__btn--ghost">Join</button>
        </div>
      </div>
      <div class="sl-14__slot">
        <div class="sl-14__time">6:00<small>PM</small></div>
        <div class="sl-14__body">
          <h3>Strength &amp; Core</h3>
          <p>Sarah Martinez · 50 min · <span class="sl-14__diff">●●○</span> Intermediate</p>
        </div>
        <div class="sl-14__book">
          <span class="sl-14__spots">8 spots open</span>
          <button class="sl-14__btn">Book</button>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-14 {
  --bg: #0f0f10;
  --panel: #1a1a1c;
  --card: #242426;
  --lime: #a3e635;
  --warn: #f97316;
  --text: #f4f4f5;
  --sub: #a1a1aa;
  --line: rgba(255,255,255,.08);
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 90% at 20% 0%, rgba(163,230,53,.06) 0%, transparent 55%), var(--bg);
  color: var(--text);
}

.sl-14 *,
.sl-14 *::before,
.sl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-14 ::selection {
  background: var(--lime);
  color: #0f0f10;
}

.sl-14__inner {
  width: 100%;
  max-width: 720px;
}

.sl-14__head {
  margin-bottom: 20px;
}

.sl-14__kicker {
  font-size: .7rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--lime);
  margin-bottom: 6px;
}

.sl-14__head h2 {
  font-size: clamp(1.5rem,3vw,2rem);
  font-weight: 900;
  letter-spacing: -.02em;
}

.sl-14__list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.sl-14__slot {
  display: grid;
  grid-template-columns: 84px 1fr auto;
  gap: 16px;
  align-items: center;
  padding: 16px 20px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  opacity: 0;
  transform: translateX(-40px);
  animation: sl-14-slot .55s cubic-bezier(.22,1,.36,1) forwards;
  transition: transform .18s ease,background .18s ease;
}

.sl-14__slot:hover {
  transform: translateX(4px);
  background: #2a2a2c;
}

.sl-14__slot:nth-child(1) {
  animation-delay: .15s;
}

.sl-14__slot:nth-child(2) {
  animation-delay: .3s;
}

.sl-14__slot:nth-child(3) {
  animation-delay: .45s;
}

.sl-14__slot:nth-child(4) {
  animation-delay: .6s;
}

.sl-14__time {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 1.75rem;
  font-weight: 800;
  letter-spacing: -.03em;
  color: var(--text);
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

.sl-14__time small {
  font-size: .75rem;
  font-weight: 600;
  color: var(--sub);
  margin-left: 2px;
}

.sl-14__body h3 {
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.01em;
  margin-bottom: 3px;
}

.sl-14__body p {
  font-size: .78rem;
  color: var(--sub);
  line-height: 1.4;
}

.sl-14__diff {
  color: var(--lime);
  letter-spacing: 2px;
  font-weight: 800;
  margin-right: 2px;
}

.sl-14__book {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
  min-width: 110px;
}

.sl-14__spots {
  font-size: .72rem;
  font-weight: 700;
  color: var(--sub);
  letter-spacing: .02em;
}

.sl-14__spots--low {
  color: var(--warn);
}

.sl-14__spots--waitlist {
  color: #a1a1aa;
}

.sl-14__btn {
  padding: 8px 20px;
  border: none;
  border-radius: 8px;
  background: var(--lime);
  color: #0f0f10;
  font-family: inherit;
  font-size: .82rem;
  font-weight: 800;
  cursor: pointer;
  transition: filter .18s ease;
}

.sl-14__btn:hover {
  filter: brightness(1.08);
}

.sl-14__btn--ghost {
  background: transparent;
  color: var(--text);
  border: 1px solid var(--line);
}

.sl-14__btn--ghost:hover {
  background: rgba(255,255,255,.06);
}

@keyframes sl-14-slot {
  from {
    opacity: 0;
    transform: translateX(-40px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-14__slot {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 560px) {
  .sl-14__slot {
    grid-template-columns: 64px 1fr;
    grid-template-rows: auto auto;
  }

  .sl-14__time {
    font-size: 1.4rem;
  }

  .sl-14__book {
    grid-column: 1/-1;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    min-width: auto;
  }
}
```
