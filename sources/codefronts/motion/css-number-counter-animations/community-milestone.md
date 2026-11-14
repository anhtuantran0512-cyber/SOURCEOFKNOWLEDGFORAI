---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/community-milestone/"
title: "Community Growth & User Milestone Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "Social proof that earns its place: an overlapping avatar stack, a member count that climbs with a per-digit roll, a milestone ribbon that fires at each round…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Community Growth & User Milestone Counter
Source: https://codefronts.com/motion/css-number-counter-animations/community-milestone/

Social proof that earns its place: an overlapping avatar stack, a member count that climbs with a per-digit roll, a milestone ribbon that fires at each round thousand, and a 7-day growth bar chart drawn in pure CSS grid. Built for the 'Join 50,000+ developers' block that sits above every newsletter form.
## HTML
```html
<section class="cnc-14" aria-label="Community growth and milestone counter demo">
  <div class="cnc-14__stage">
    <article class="cnc-14__card">
      <div class="cnc-14__stack" aria-hidden="true">
        <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44">
        <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44">
        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44">
        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44">
        <span class="cnc-14__more">+9k</span>
      </div>
      <p class="cnc-14__count"><span class="cnc-14__num">0</span><span class="cnc-14__plus">+</span></p>
      <p class="cnc-14__label">developers building with Codefronts</p>
      <div class="cnc-14__chart" aria-hidden="true">
        <span style="--cnc-14-v:38"></span><span style="--cnc-14-v:52"></span><span style="--cnc-14-v:44"></span>
        <span style="--cnc-14-v:67"></span><span style="--cnc-14-v:71"></span><span style="--cnc-14-v:86"></span><span style="--cnc-14-v:100"></span>
      </div>
      <p class="cnc-14__foot"><b class="cnc-14__week">+1,842</b> joined in the last 7 days</p>
      <button class="cnc-14__cta" type="button">Join the community</button>
      <p class="cnc-14__ribbon" aria-hidden="true"></p>
      <p class="cnc-14__sr" role="status" aria-live="polite"></p>
    </article>
    <p class="cnc-14__chip" aria-hidden="true">descending z-index stack · floor() milestone crossing · grid bar chart, no library</p>
  </div>
</section>
```
## CSS
```css
.cnc-14,
.cnc-14 *,
.cnc-14 *::before,
.cnc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-14-bg: oklch(0.97 0.008 280);
  --cnc-14-card: oklch(1 0 0);
  --cnc-14-ink: oklch(0.2 0.02 280);
  --cnc-14-mut: oklch(0.55 0.02 280);
  --cnc-14-acc: oklch(0.58 0.2 285);
  background: var(--cnc-14-bg);
  color: var(--cnc-14-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,48px);
}

.cnc-14__card {
  position: relative;
  width: min(100%,420px);
  padding: clamp(22px,4vw,30px);
  border-radius: 24px;
  overflow: hidden;
  text-align: center;
  background: var(--cnc-14-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 60px oklch(0.35 0.06 285/.16);
}

.cnc-14__stack {
  display: flex;
  justify-content: center;
  align-items: center;
}

.cnc-14__stack img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--cnc-14-card);
  margin-left: -12px;
  background: oklch(0.86 0.03 280);
  transition: translate .25s cubic-bezier(.16,1,.3,1);
}

.cnc-14__stack img:first-child {
  margin-left: 0;
}

.cnc-14__stack img:nth-child(1) {
  z-index: 6;
}

.cnc-14__stack img:nth-child(2) {
  z-index: 5;
}

.cnc-14__stack img:nth-child(3) {
  z-index: 4;
}

.cnc-14__stack img:nth-child(4) {
  z-index: 3;
}

.cnc-14__stack img:nth-child(5) {
  z-index: 2;
}

.cnc-14__stack img:hover {
  translate: 0 -5px;
  z-index: 9;
}

.cnc-14__more {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  margin-left: -12px;
  border-radius: 50%;
  border: 3px solid var(--cnc-14-card);
  background: var(--cnc-14-acc);
  color: oklch(0.99 0 0);
  font-size: 11.5px;
  font-weight: 750;
  z-index: 1;
}

.cnc-14__count {
  display: flex;
  align-items: baseline;
  justify-content: center;
  margin-top: 20px;
  font-size: clamp(40px,8vw,58px);
  font-weight: 770;
  letter-spacing: -.05em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-14__plus {
  color: var(--cnc-14-acc);
}

.cnc-14__label {
  margin-top: 8px;
  font-size: 14px;
  color: var(--cnc-14-mut);
}

.cnc-14__chart {
  display: grid;
  grid-template-columns: repeat(7,1fr);
  align-items: end;
  gap: 6px;
  height: 64px;
  margin-top: 22px;
}

.cnc-14__chart span {
  height: calc(var(--cnc-14-v) * 1%);
  border-radius: 5px 5px 2px 2px;
  background: color-mix(in oklch,var(--cnc-14-acc) calc(var(--cnc-14-v) * 0.9%),oklch(0.9 0.02 285));
  transform-origin: bottom;
  animation: cnc-14-grow .8s cubic-bezier(.16,1,.3,1) both;
}

.cnc-14__chart span:nth-child(2) {
  animation-delay: .06s;
}

.cnc-14__chart span:nth-child(3) {
  animation-delay: .12s;
}

.cnc-14__chart span:nth-child(4) {
  animation-delay: .18s;
}

.cnc-14__chart span:nth-child(5) {
  animation-delay: .24s;
}

.cnc-14__chart span:nth-child(6) {
  animation-delay: .3s;
}

.cnc-14__chart span:nth-child(7) {
  animation-delay: .36s;
}

@keyframes cnc-14-grow {
  from {
    transform: scaleY(0);
    opacity: .4;
  }

  to {
    transform: scaleY(1);
    opacity: 1;
  }
}

.cnc-14__foot {
  margin-top: 12px;
  font-size: 12.5px;
  color: var(--cnc-14-mut);
}

.cnc-14__foot b {
  color: var(--cnc-14-acc);
  font-weight: 720;
  font-variant-numeric: tabular-nums;
}

.cnc-14__cta {
  width: 100%;
  min-height: 48px;
  margin-top: 20px;
  border: 0;
  border-radius: 14px;
  background: var(--cnc-14-ink);
  color: oklch(0.99 0 0);
  font: inherit;
  font-size: 14.5px;
  font-weight: 660;
  cursor: pointer;
  transition: background .2s,transform .2s;
}

.cnc-14__cta:hover {
  background: var(--cnc-14-acc);
  transform: translateY(-2px);
}

.cnc-14__cta:focus-visible {
  outline: 3px solid var(--cnc-14-acc);
  outline-offset: 3px;
}

.cnc-14__ribbon {
  position: absolute;
  top: 14px;
  right: -42px;
  width: 160px;
  padding: 6px 0;
  rotate: 38deg;
  text-align: center;
  background: var(--cnc-14-acc);
  color: oklch(0.99 0 0);
  font-size: 11.5px;
  font-weight: 750;
  letter-spacing: .04em;
  opacity: 0;
  translate: 0 -10px;
  transition: opacity .45s,translate .45s cubic-bezier(.16,1,.3,1);
}

.cnc-14__card[data-milestone] .cnc-14__ribbon {
  opacity: 1;
  translate: 0 0;
}

.cnc-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-14__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-14-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,480px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-14 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const nf = new Intl.NumberFormat('en-US');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.cnc-14__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const numEl = card.querySelector('.cnc-14__num');
    const ribbon = card.querySelector('.cnc-14__ribbon');
    const say = card.querySelector('.cnc-14__sr');
    let members = 50984;

    const roll = (from, to, ms = 1600) => {
      if (reduce) { numEl.textContent = nf.format(to); return; }
      const t0 = performance.now();
      const frame = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        numEl.textContent = nf.format(p === 1 ? to : Math.round(from + (to - from) * (1 - Math.pow(1 - p, 4))));
        if (p < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    };

    const grow = (by) => {
      const prev = members; members += by;
      if (Math.floor(members / 1000) > Math.floor(prev / 1000)) {   // crossing, not equality
        card.dataset.milestone = '1';
        ribbon.textContent = Math.floor(members / 1000) + 'k members';
        say.textContent = Math.floor(members / 1000) + ' thousand members reached';
        clearTimeout(card._mt);
        card._mt = setTimeout(() => delete card.dataset.milestone, 4200);
      }
      roll(prev, members, 700);
    };

    roll(members - 2400, members);
    const id = setInterval(() => { if (document.visibilityState === 'visible') grow(1 + Math.floor(Math.random() * 4)); }, 3200);
    card.querySelector('.cnc-14__cta').addEventListener('click', () => { grow(1); say.textContent = 'Welcome. You are member ' + nf.format(members); });
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
