---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/saas-landing-page-key-stats-counter/"
title: "SaaS Landing Page Key Stats Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "The hero stat row every SaaS marketing page ships — 99.98% uptime, 12,480 teams, 4.9 rating — counting up on load with zero JavaScript. A registered…"
has_js: "false"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Landing Page Key Stats Counter
Source: https://codefronts.com/motion/css-number-counter-animations/saas-landing-page-key-stats-counter/

The hero stat row every SaaS marketing page ships — 99.98% uptime, 12,480 teams, 4.9 rating — counting up on load with zero JavaScript. A registered @property integer is animated by the style engine and printed as text through counter(), so the numbers are genuinely interpolated rather than swapped between hardcoded strings. Staggered animation-delay gives the row a choreographed cascade instead of four things firing at once.
## HTML
```html
<section class="cnc-01" aria-label="SaaS landing page key stats counter demo">
  <div class="cnc-01__stage">
    <p class="cnc-01__eyebrow">Trusted at scale</p>
    <h2 class="cnc-01__head">Numbers that hold up<br>under production load</h2>
    <dl class="cnc-01__row">
      <div class="cnc-01__stat">
        <dd class="cnc-01__val"><span class="cnc-01__num" aria-hidden="true"></span><span class="cnc-01__suf">%</span><span class="cnc-01__sr">99.98 percent</span></dd>
        <dt class="cnc-01__key">Uptime, 12-month rolling</dt>
      </div>
      <div class="cnc-01__stat">
        <dd class="cnc-01__val"><span class="cnc-01__num" aria-hidden="true"></span><span class="cnc-01__suf">k</span><span class="cnc-01__sr">12.4 thousand</span></dd>
        <dt class="cnc-01__key">Teams onboarded</dt>
      </div>
      <div class="cnc-01__stat">
        <dd class="cnc-01__val"><span class="cnc-01__num" aria-hidden="true"></span><span class="cnc-01__suf">ms</span><span class="cnc-01__sr">42 milliseconds</span></dd>
        <dt class="cnc-01__key">Median API response</dt>
      </div>
      <div class="cnc-01__stat">
        <dd class="cnc-01__val"><span class="cnc-01__pre">4.</span><span class="cnc-01__num" aria-hidden="true"></span><span class="cnc-01__sr">4.9 out of 5</span></dd>
        <dt class="cnc-01__key">Average review score</dt>
      </div>
    </dl>
    <p class="cnc-01__chip" aria-hidden="true">@property &lt;integer&gt; · counter-reset var() · content:counter() · staggered delay</p>
  </div>
</section>
```
## CSS
```css
@property --cnc-01-n {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.cnc-01,
.cnc-01 *,
.cnc-01 *::before,
.cnc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-01-bg: oklch(0.17 0.02 265);
  --cnc-01-ink: oklch(0.98 0.004 260);
  --cnc-01-mut: oklch(0.68 0.02 265);
  --cnc-01-acc: oklch(0.82 0.17 158);
  background: var(--cnc-01-bg);
  color: var(--cnc-01-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(14px,2vw,20px);
  padding: clamp(24px,6vw,72px);
  text-align: center;
  background: radial-gradient(90% 70% at 50% 0%,color-mix(in oklch,var(--cnc-01-acc) 16%,transparent),transparent 70%);
}

.cnc-01__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--cnc-01-acc);
}

.cnc-01__head {
  font-size: clamp(26px,4.4vw,46px);
  font-weight: 680;
  line-height: 1.1;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.cnc-01__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(168px,1fr));
  gap: clamp(18px,3vw,10px);
  width: min(100%,940px);
  margin-top: clamp(14px,3vw,30px);
  padding: clamp(20px,3vw,30px) 0;
  border-block: 1px solid oklch(1 0 0/.12);
}

.cnc-01__stat {
  display: grid;
  gap: 8px;
  padding: 0 clamp(10px,2vw,22px);
  border-left: 1px solid oklch(1 0 0/.09);
}

.cnc-01__stat:first-child {
  border-left: 0;
}

.cnc-01__val {
  display: flex;
  align-items: baseline;
  justify-content: center;
  font-size: clamp(38px,5.6vw,60px);
  font-weight: 700;
  letter-spacing: -.045em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-01__num::after {
  content: counter(cnc-01-n);
}

.cnc-01__pre,
.cnc-01__suf {
  color: var(--cnc-01-acc);
}

.cnc-01__suf {
  font-size: .5em;
  font-weight: 640;
  margin-left: 2px;
  letter-spacing: 0;
}

.cnc-01__key {
  font-size: 13px;
  line-height: 1.4;
  color: var(--cnc-01-mut);
  text-wrap: balance;
}

.cnc-01__num {
  counter-reset: cnc-01-n var(--cnc-01-n);
  animation: var(--cnc-01-kf) 2.2s cubic-bezier(.16,1,.3,1) both;
}

.cnc-01__stat:nth-child(1) .cnc-01__num {
  --cnc-01-kf: cnc-01-a;
  animation-delay: .05s;
}

.cnc-01__stat:nth-child(2) .cnc-01__num {
  --cnc-01-kf: cnc-01-b;
  animation-delay: .17s;
}

.cnc-01__stat:nth-child(3) .cnc-01__num {
  --cnc-01-kf: cnc-01-c;
  animation-delay: .29s;
}

.cnc-01__stat:nth-child(4) .cnc-01__num {
  --cnc-01-kf: cnc-01-d;
  animation-delay: .41s;
}

@keyframes cnc-01-a {
  from {
    --cnc-01-n: 0;
  }

  to {
    --cnc-01-n: 99;
  }
}

@keyframes cnc-01-b {
  from {
    --cnc-01-n: 0;
  }

  to {
    --cnc-01-n: 12;
  }
}

@keyframes cnc-01-c {
  from {
    --cnc-01-n: 0;
  }

  to {
    --cnc-01-n: 42;
  }
}

@keyframes cnc-01-d {
  from {
    --cnc-01-n: 0;
  }

  to {
    --cnc-01-n: 9;
  }
}

.cnc-01__stat {
  animation: cnc-01-rise .8s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--cnc-01-i,0) * .12s);
}

.cnc-01__stat:nth-child(2) {
  --cnc-01-i: 1;
}

.cnc-01__stat:nth-child(3) {
  --cnc-01-i: 2;
}

.cnc-01__stat:nth-child(4) {
  --cnc-01-i: 3;
}

@keyframes cnc-01-rise {
  from {
    opacity: 0;
    transform: translateY(14px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.cnc-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-01__chip {
  margin-top: clamp(10px,2vw,18px);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-01-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
}

@supports not (background: paint(x)) {
  .cnc-01__num::after {
    content: counter(cnc-01-n);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnc-01__num {
    animation-duration: 1ms;
  }

  .cnc-01__stat {
    animation: none;
  }
}
```
