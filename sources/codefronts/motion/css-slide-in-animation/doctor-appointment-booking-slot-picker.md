---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/doctor-appointment-booking-slot-picker/"
title: "Doctor Appointment Booking Slot Picker"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A healthcare appointment scheduler where time slots slide in from below in a grid — the pattern used by Zocdoc, One Medical, Practice Fusion, and modern…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Doctor Appointment Booking Slot Picker
Source: https://codefronts.com/motion/css-slide-in-animation/doctor-appointment-booking-slot-picker/

A healthcare appointment scheduler where time slots slide in from below in a grid — the pattern used by Zocdoc, One Medical, Practice Fusion, and modern telehealth platforms.
## HTML
```html
<div class="sl-06">
  <div class="sl-06__card">
    <div class="sl-06__head">
      <div class="sl-06__doc">
        <div class="sl-06__ava">DR</div>
        <div>
          <h3>Dr. Sarah Chen, MD</h3>
          <p>Family Medicine · In-network with your plan</p>
        </div>
      </div>
      <div class="sl-06__rating">
        <span>★★★★★</span>
        <small>4.9 (528 reviews)</small>
      </div>
    </div>
    <div class="sl-06__day">
      <p class="sl-06__date">Wednesday, Nov 5</p>
      <p class="sl-06__note">30-min appointment · Video or in-person</p>
    </div>
    <div class="sl-06__slots">
      <button class="sl-06__slot">9:00 AM</button>
      <button class="sl-06__slot sl-06__slot--taken" disabled>9:30 AM</button>
      <button class="sl-06__slot">10:00 AM</button>
      <button class="sl-06__slot sl-06__slot--taken" disabled>10:30 AM</button>
      <button class="sl-06__slot sl-06__slot--selected">11:00 AM</button>
      <button class="sl-06__slot">11:30 AM</button>
      <button class="sl-06__slot">2:00 PM</button>
      <button class="sl-06__slot">2:30 PM</button>
      <button class="sl-06__slot">3:00 PM</button>
    </div>
    <button class="sl-06__cta">Confirm 11:00 AM appointment →</button>
  </div>
</div>
```
## CSS
```css
.sl-06 {
  --bg: #f0f7fc;
  --card: #fff;
  --accent: #3b82f6;
  --good: #10b981;
  --ink: #0f172a;
  --sub: #64748b;
  --line: #e2e8f0;
  --taken: #f1f5f9;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 100% at 50% 0%, rgba(59,130,246,.08) 0%, transparent 60%), var(--bg);
  color: var(--ink);
}

.sl-06 *,
.sl-06 *::before,
.sl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-06 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-06__card {
  width: min(560px,100%);
  padding: 32px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 24px 48px -20px rgba(15,23,42,.12);
}

.sl-06__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
}

.sl-06__doc {
  display: flex;
  align-items: center;
  gap: 14px;
}

.sl-06__ava {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  flex-shrink: 0;
  background: linear-gradient(135deg,#60a5fa,#3b82f6);
  color: #fff;
  font-size: .85rem;
  font-weight: 800;
  letter-spacing: .02em;
}

.sl-06__doc h3 {
  font-size: 1.02rem;
  font-weight: 700;
  letter-spacing: -.01em;
  margin-bottom: 2px;
}

.sl-06__doc p {
  font-size: .78rem;
  color: var(--sub);
}

.sl-06__rating span {
  color: #f59e0b;
  font-size: .85rem;
  letter-spacing: 1px;
  display: block;
}

.sl-06__rating small {
  font-size: .68rem;
  color: var(--sub);
  display: block;
  text-align: right;
}

.sl-06__day {
  padding: 14px 16px;
  background: rgba(59,130,246,.06);
  border-radius: 10px;
  margin-bottom: 18px;
}

.sl-06__date {
  font-size: .95rem;
  font-weight: 700;
  letter-spacing: -.01em;
  margin-bottom: 2px;
}

.sl-06__note {
  font-size: .78rem;
  color: var(--sub);
}

.sl-06__slots {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 8px;
  margin-bottom: 20px;
}

.sl-06__slot {
  padding: 10px 8px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font-family: inherit;
  font-size: .82rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  opacity: 0;
  transform: translateY(20px);
  animation: sl-06-slot .35s cubic-bezier(.22,1,.36,1) forwards;
  transition: border-color .15s ease,background .15s ease;
}

.sl-06__slot:hover:not(:disabled) {
  border-color: var(--accent);
  background: rgba(59,130,246,.06);
}

.sl-06__slot:nth-child(1) {
  animation-delay: .2s;
}

.sl-06__slot:nth-child(2) {
  animation-delay: .24s;
}

.sl-06__slot:nth-child(3) {
  animation-delay: .28s;
}

.sl-06__slot:nth-child(4) {
  animation-delay: .32s;
}

.sl-06__slot:nth-child(5) {
  animation-delay: .36s;
}

.sl-06__slot:nth-child(6) {
  animation-delay: .4s;
}

.sl-06__slot:nth-child(7) {
  animation-delay: .44s;
}

.sl-06__slot:nth-child(8) {
  animation-delay: .48s;
}

.sl-06__slot:nth-child(9) {
  animation-delay: .52s;
}

.sl-06__slot--taken {
  color: #cbd5e1;
  background: var(--taken);
  border-color: var(--taken);
  text-decoration: line-through;
  cursor: not-allowed;
}

.sl-06__slot--selected {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
  box-shadow: 0 6px 16px -6px rgba(59,130,246,.55);
}

.sl-06__cta {
  width: 100%;
  padding: 13px 22px;
  border: none;
  border-radius: 10px;
  background: var(--good);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  opacity: 0;
  animation: sl-06-fade .3s ease-out .7s forwards;
  transition: background .18s ease,transform .12s ease;
}

.sl-06__cta:hover {
  background: #059669;
  transform: translateY(-1px);
}

@keyframes sl-06-slot {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes sl-06-fade {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-06 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
