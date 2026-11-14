---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/uptime-sla-monitor/"
title: "SLA Uptime Percentage Indicator"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "The status-page header, rebuilt: 99.982% uptime counting up across four significant digits, a 90-day incident history strip, and an operational badge — all…"
has_js: "false"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SLA Uptime Percentage Indicator
Source: https://codefronts.com/motion/css-number-counter-animations/uptime-sla-monitor/

The status-page header, rebuilt: 99.982% uptime counting up across four significant digits, a 90-day incident history strip, and an operational badge — all in pure CSS. The interesting problem is decimals, because CSS counters are integers only; the fix is two counters and a literal separator, and it is exact.
## HTML
```html
<section class="cnc-16" aria-label="SLA uptime percentage indicator demo">
  <div class="cnc-16__stage">
    <article class="cnc-16__panel">
      <header class="cnc-16__top">
        <span class="cnc-16__badge"><span class="cnc-16__dot" aria-hidden="true"></span>All systems operational</span>
        <span class="cnc-16__region">us-east · eu-west · ap-south</span>
      </header>
      <p class="cnc-16__pct" aria-hidden="true"></p>
      <p class="cnc-16__sr">99.982 percent uptime over the last 90 days</p>
      <p class="cnc-16__sub">90-day uptime · SLA commitment 99.95%</p>
      <div class="cnc-16__strip" aria-hidden="true">
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span data-s="warn" title="14 Jun — 12 min elevated latency"></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span><span data-s="down" title="6 Jul — 4 min partial outage"></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span data-s="warn" title="2 Aug — 6 min degraded search"></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
      </div>
      <footer class="cnc-16__foot"><span>90 days ago</span><span>3 incidents · 22 min total</span><span>Today</span></footer>
    </article>
    <p class="cnc-16__chip" aria-hidden="true">two counters + literal separator · @counter-style pad · 90 CSS bars</p>
  </div>
</section>
```
## CSS
```css
@property --cnc-16-i {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --cnc-16-f {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@counter-style cnc-16-pad3 {
  system: numeric;
  symbols: '0' '1' '2' '3' '4' '5' '6' '7' '8' '9';
  pad: 3 '0';
}

.cnc-16,
.cnc-16 *,
.cnc-16 *::before,
.cnc-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-16-bg: oklch(0.16 0.015 240);
  --cnc-16-card: oklch(0.21 0.018 240);
  --cnc-16-ink: oklch(0.98 0.004 240);
  --cnc-16-mut: oklch(0.66 0.02 240);
  --cnc-16-ok: oklch(0.78 0.16 152);
  --cnc-16-warn: oklch(0.8 0.15 80);
  --cnc-16-bad: oklch(0.68 0.2 25);
  background: var(--cnc-16-bg);
  color: var(--cnc-16-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,48px);
}

.cnc-16__panel {
  width: min(100%,640px);
  padding: clamp(22px,4vw,32px);
  border-radius: 22px;
  background: var(--cnc-16-card);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.07),0 24px 56px oklch(0 0 0/.42);
}

.cnc-16__top {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.cnc-16__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cnc-16-ok) 15%,transparent);
  color: var(--cnc-16-ok);
  font-size: 12.5px;
  font-weight: 680;
}

.cnc-16__dot {
  position: relative;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
}

.cnc-16__dot::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: currentColor;
  animation: cnc-16-ping 2.4s cubic-bezier(0,0,.2,1) infinite;
}

@keyframes cnc-16-ping {
  0% {
    opacity: .6;
    scale: 1;
  }

  75%,
    100% {
    opacity: 0;
    scale: 3;
  }
}

.cnc-16__region {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-16-mut);
}

.cnc-16__pct {
  margin-top: 22px;
  font-size: clamp(44px,9vw,72px);
  font-weight: 750;
  letter-spacing: -.055em;
  line-height: 1;
  color: var(--cnc-16-ok);
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
  counter-reset: cnc-16-i var(--cnc-16-i) cnc-16-f var(--cnc-16-f);
  animation: cnc-16-count 2.6s cubic-bezier(.16,1,.3,1) both;
}

.cnc-16__pct::after {
  content: counter(cnc-16-i) "." counter(cnc-16-f,cnc-16-pad3) "%";
}

@keyframes cnc-16-count {
  from {
    --cnc-16-i: 0;
    --cnc-16-f: 0;
  }

  to {
    --cnc-16-i: 99;
    --cnc-16-f: 982;
  }
}

.cnc-16__sub {
  margin-top: 10px;
  font-size: 13px;
  color: var(--cnc-16-mut);
}

.cnc-16__strip {
  display: flex;
  gap: 2px;
  height: 44px;
  margin-top: 26px;
}

.cnc-16__strip span {
  flex: 1;
  border-radius: 3px;
  background: color-mix(in oklch,var(--cnc-16-ok) 55%,transparent);
  transform-origin: bottom;
  animation: cnc-16-rise .5s cubic-bezier(.16,1,.3,1) both;
  transition: background .2s,transform .2s;
}

.cnc-16__strip span:hover {
  background: var(--cnc-16-ok);
  transform: scaleY(1.08);
}

.cnc-16__strip span[data-s="warn"] {
  background: var(--cnc-16-warn);
}

.cnc-16__strip span[data-s="down"] {
  background: var(--cnc-16-bad);
}

@keyframes cnc-16-rise {
  from {
    transform: scaleY(.15);
    opacity: .2;
  }

  to {
    transform: scaleY(1);
    opacity: 1;
  }
}

.cnc-16__strip span:nth-child(3n) {
  animation-delay: .05s;
}

.cnc-16__strip span:nth-child(3n+1) {
  animation-delay: .12s;
}

.cnc-16__strip span:nth-child(5n) {
  animation-delay: .2s;
}

.cnc-16__foot {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  margin-top: 12px;
  font-size: 11.5px;
  color: var(--cnc-16-mut);
}

.cnc-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-16-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,560px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-16__pct {
    animation-duration: 1ms;
  }

  .cnc-16__strip span {
    animation: none;
  }

  .cnc-16__dot::after {
    animation: none;
    opacity: 0;
  }
}
```
