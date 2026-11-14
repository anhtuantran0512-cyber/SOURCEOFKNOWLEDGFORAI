---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/css-gradient-badges-status-pills/"
title: "CSS Gradient Badges & Status Pills"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A full badge system on a mock release-dashboard: soft-tint status pills with pulsing gradient dots, plan badges (PRO gold, BETA aurora), gradient-outline…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Badges & Status Pills
Source: https://codefronts.com/design-styles/css-gradient-ui/css-gradient-badges-status-pills/

A full badge system on a mock release-dashboard: soft-tint status pills with pulsing gradient dots, plan badges (PRO gold, BETA aurora), gradient-outline tags and a live counter — every pattern themed by one hue variable.
## HTML
```html
<div class="cgu-04-group">
<section class="cgu-04" aria-label="CSS gradient badge and status pill demos">
  <div class="cgu-04__inner">
    <header class="cgu-04__head">
      <p class="cgu-04__eyebrow">04 · Badges &amp; pills</p>
      <h2 class="cgu-04__title">A status system from one hue variable</h2>
      <p class="cgu-04__sub">Soft-tint pills, plan badges, outline tags and counters — each themed by a single <code>--h</code> value.</p>
    </header>
    <div class="cgu-04__board">
      <div class="cgu-04__toolbar">
        <nav class="cgu-04__tabs" aria-label="Release views">
          <button class="cgu-04__tab is-active" type="button">Deployments <span class="cgu-04__count">24</span></button>
          <button class="cgu-04__tab" type="button">Incidents <span class="cgu-04__count cgu-04__count--hot">3</span></button>
          <button class="cgu-04__tab" type="button">Approvals</button>
        </nav>
        <div class="cgu-04__plans">
          <span class="cgu-04__plan cgu-04__plan--pro">PRO</span>
          <span class="cgu-04__plan cgu-04__plan--beta">BETA</span>
          <span class="cgu-04__plan cgu-04__plan--new">NEW</span>
        </div>
      </div>
      <ul class="cgu-04__rows">
        <li class="cgu-04__row"><span class="cgu-04__svc">api-gateway <em>v2.14.0</em></span><span class="cgu-04__tags"><span class="cgu-04__tag">edge</span><span class="cgu-04__tag">canary</span></span><span class="cgu-04__pill" style="--h:150"><i class="cgu-04__dot cgu-04__dot--live" aria-hidden="true"></i>Deployed</span></li>
        <li class="cgu-04__row"><span class="cgu-04__svc">billing-worker <em>v1.9.2</em></span><span class="cgu-04__tags"><span class="cgu-04__tag">cron</span></span><span class="cgu-04__pill" style="--h:85"><i class="cgu-04__dot" aria-hidden="true"></i>Degraded</span></li>
        <li class="cgu-04__row"><span class="cgu-04__svc">auth-service <em>v3.0.1</em></span><span class="cgu-04__tags"><span class="cgu-04__tag">core</span><span class="cgu-04__tag">sso</span></span><span class="cgu-04__pill" style="--h:25"><i class="cgu-04__dot cgu-04__dot--live" aria-hidden="true"></i>Failed</span></li>
        <li class="cgu-04__row"><span class="cgu-04__svc">search-index <em>v0.8.0</em></span><span class="cgu-04__tags"><span class="cgu-04__tag">ml</span></span><span class="cgu-04__pill" style="--h:250"><i class="cgu-04__dot" aria-hidden="true"></i>Queued</span></li>
        <li class="cgu-04__row"><span class="cgu-04__svc">cdn-purger <em>v1.2.7</em></span><span class="cgu-04__tags"><span class="cgu-04__tag">edge</span></span><span class="cgu-04__pill" style="--h:320"><i class="cgu-04__dot" aria-hidden="true"></i>Rolling back</span></li>
      </ul>
    </div>
    <p class="cgu-04__foot">State is never color-only — every pill pairs its hue with a text label for accessibility.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-04-group {
  display: block;
  width: 100%;
}

.cgu-04,
.cgu-04 *,
.cgu-04 *::before,
.cgu-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-04 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: radial-gradient(100% 80% at 80% 0%,#131a2e 0%,#0b0d16 60%);
}

.cgu-04__inner {
  width: min(920px,100%);
  display: grid;
  gap: 38px;
}

.cgu-04__head {
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cgu-04__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #5eead4;
}

.cgu-04__title {
  font-size: clamp(27px,4vw,44px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  text-wrap: balance;
}

.cgu-04__sub {
  max-width: 54ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
}

.cgu-04__sub code,
.cgu-04__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12.5px;
  color: #99f6e4;
  background: rgba(94,234,212,.08);
  padding: 1px 5px;
  border-radius: 5px;
}

.cgu-04__board {
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.028);
  overflow: hidden;
}

.cgu-04__toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255,255,255,.07);
}

.cgu-04__tabs {
  display: flex;
  gap: 6px;
}

.cgu-04__tab {
  display: flex;
  align-items: center;
  gap: 8px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 650;
  color: #a7abc8;
  background: transparent;
  border: none;
  border-radius: 10px;
  padding: 9px 14px;
  cursor: pointer;
  transition: background .25s,color .25s;
}

.cgu-04__tab:hover {
  background: rgba(255,255,255,.06);
  color: #eef0ff;
}

.cgu-04__tab.is-active {
  color: #fff;
  background: linear-gradient(135deg,rgba(94,234,212,.16),rgba(129,140,248,.16));
  box-shadow: inset 0 0 0 1px rgba(94,234,212,.25);
}

.cgu-04__tab:focus-visible {
  outline: 2px solid #5eead4;
  outline-offset: 2px;
}

.cgu-04__count {
  font-size: 11px;
  font-weight: 800;
  min-width: 22px;
  text-align: center;
  padding: 2px 7px;
  border-radius: 9999px;
  background: linear-gradient(135deg,#334155,#1e293b);
  color: #cbd5e1;
}

.cgu-04__count--hot {
  background: linear-gradient(135deg,#f43f5e,#fb923c);
  color: #fff;
  animation: cgu04-breathe 2.2s ease-in-out infinite;
}

.cgu-04__plans {
  display: flex;
  gap: 8px;
}

.cgu-04__plan {
  position: relative;
  overflow: hidden;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .14em;
  padding: 5px 12px;
  border-radius: 8px;
  color: #1a1206;
}

.cgu-04__plan--pro {
  background: linear-gradient(135deg,#fde68a,#f59e0b 55%,#fbbf24);
}

.cgu-04__plan--pro::after {
  content: "";
  position: absolute;
  inset: 0 auto 0 -60%;
  width: 40%;
  background: linear-gradient(105deg,transparent,rgba(255,255,255,.75),transparent);
  transform: skewX(-16deg);
  animation: cgu04-shine 3.4s ease-in-out infinite;
}

.cgu-04__plan--beta {
  color: #fff;
  background: linear-gradient(135deg,#818cf8,#e879f9);
}

.cgu-04__plan--new {
  color: #052e2b;
  background: linear-gradient(135deg,#5eead4,#34d399);
}

.cgu-04__rows {
  list-style: none;
  display: grid;
}

.cgu-04__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  padding: 15px 20px;
  border-bottom: 1px solid rgba(255,255,255,.05);
  transition: background .25s;
}

.cgu-04__row:last-child {
  border-bottom: none;
}

.cgu-04__row:hover {
  background: rgba(255,255,255,.03);
}

.cgu-04__svc {
  flex: 1 1 200px;
  font-size: 14.5px;
  font-weight: 650;
}

.cgu-04__svc em {
  font-style: normal;
  font-size: 12px;
  color: #7c81a3;
  margin-left: 8px;
  font-family: ui-monospace,Menlo,monospace;
}

.cgu-04__tags {
  display: flex;
  gap: 6px;
}

.cgu-04__tag {
  font-size: 11px;
  font-weight: 650;
  padding: 3.5px 10px;
  border-radius: 9999px;
  color: #c7d2fe;
  border: 1px solid transparent;
  background: linear-gradient(#0e1020,#0e1020) padding-box,linear-gradient(135deg,#38bdf8,#a78bfa) border-box;
  white-space: nowrap;
}

.cgu-04__pill {
  --h: 150;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: 9999px;
  white-space: nowrap;
  background: linear-gradient(135deg,oklch(0.28 0.06 var(--h) / .55),oklch(0.22 0.04 var(--h) / .35));
  color: oklch(0.85 0.11 var(--h));
  border: 1px solid oklch(0.6 0.12 var(--h) / .35);
}

.cgu-04__dot {
  position: relative;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: linear-gradient(135deg,oklch(0.8 0.16 var(--h)),oklch(0.65 0.18 var(--h)));
}

.cgu-04__dot--live::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: oklch(0.75 0.16 var(--h));
  animation: cgu04-pulse 1.8s cubic-bezier(.2,.7,.4,1) infinite;
}

.cgu-04__foot {
  text-align: center;
  font-size: 13px;
  color: #7c81a3;
}

@keyframes cgu04-pulse {
  0% {
    transform: scale(1);
    opacity: .9;
  }

  100% {
    transform: scale(3.2);
    opacity: 0;
  }
}

@keyframes cgu04-shine {
  0%,
    55% {
    left: -60%;
  }

  85%,
    100% {
    left: 130%;
  }
}

@keyframes cgu04-breathe {
  0%,
    100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.12);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-04__dot--live::before,
    .cgu-04__plan--pro::after,
    .cgu-04__count--hot {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pills, dots, plan badges and counters are pure CSS; each status is themed by a single --h hue custom property in oklch(). */
```
