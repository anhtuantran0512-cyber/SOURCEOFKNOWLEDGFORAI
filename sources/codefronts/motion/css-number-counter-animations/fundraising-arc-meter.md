---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/fundraising-arc-meter/"
title: "Fundraising Progress & Donation Meter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A campaign meter that does the two things donation pages must do: show the raised total climbing toward a goal, and make the next contribution feel…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fundraising Progress & Donation Meter
Source: https://codefronts.com/motion/css-number-counter-animations/fundraising-arc-meter/

A campaign meter that does the two things donation pages must do: show the raised total climbing toward a goal, and make the next contribution feel consequential. Milestone pips light up as the bar passes them, a live donation feed slides in, and pledging visibly moves the bar — with the goal line, percentage and remaining amount all derived from one number.
## HTML
```html
<section class="cnc-11" aria-label="Fundraising progress and donation meter demo">
  <div class="cnc-11__stage">
    <article class="cnc-11__card" style="--cnc-11-p:0">
      <div class="cnc-11__hero">
        <img class="cnc-11__img" alt="Volunteers planting saplings in a reforestation project" loading="lazy" decoding="async"
          src="https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?q=80&w=900&auto=format&fit=crop">
        <span class="cnc-11__tag">14 days left</span>
      </div>
      <div class="cnc-11__body">
        <h3 class="cnc-11__title">Restore the Kinvara Woodland</h3>
        <p class="cnc-11__raised"><span class="cnc-11__cur">$</span><span class="cnc-11__num">0</span><span class="cnc-11__goal">raised of $250,000 goal</span></p>
        <div class="cnc-11__meter" role="meter" aria-valuemin="0" aria-valuemax="250000" aria-valuenow="0" aria-label="Amount raised toward goal">
          <span class="cnc-11__fill"></span>
          <span class="cnc-11__pip" style="left:25%" data-at="25"><b>25%</b></span>
          <span class="cnc-11__pip" style="left:50%" data-at="50"><b>50%</b></span>
          <span class="cnc-11__pip" style="left:75%" data-at="75"><b>75%</b></span>
        </div>
        <p class="cnc-11__stats"><b class="cnc-11__pct">0%</b> funded · <b class="cnc-11__donors">1,284</b> donors · <b class="cnc-11__left">$250,000</b> to go</p>
        <div class="cnc-11__acts">
          <button class="cnc-11__btn" type="button" data-give="50">Give $50</button>
          <button class="cnc-11__btn" type="button" data-give="250">Give $250</button>
          <button class="cnc-11__btn cnc-11__btn--solid" type="button" data-give="1000">Give $1,000</button>
        </div>
        <ul class="cnc-11__feed" aria-label="Recent donations"></ul>
        <p class="cnc-11__sr" role="status" aria-live="polite"></p>
      </div>
    </article>
    <p class="cnc-11__chip" aria-hidden="true">single ratio drives fill + pips + copy · @starting-style feed · role=meter</p>
  </div>
</section>
```
## CSS
```css
.cnc-11,
.cnc-11 *,
.cnc-11 *::before,
.cnc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-11-bg: oklch(0.96 0.012 145);
  --cnc-11-card: oklch(1 0 0);
  --cnc-11-ink: oklch(0.21 0.03 160);
  --cnc-11-mut: oklch(0.54 0.02 160);
  --cnc-11-acc: oklch(0.62 0.16 155);
  background: var(--cnc-11-bg);
  color: var(--cnc-11-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(16px,4vw,44px);
}

.cnc-11__card {
  width: min(100%,480px);
  border-radius: 24px;
  overflow: hidden;
  background: var(--cnc-11-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 60px oklch(0.4 0.05 160/.18);
}

.cnc-11__hero {
  position: relative;
  height: 168px;
  background: linear-gradient(140deg,oklch(0.82 0.09 150),oklch(0.7 0.12 175));
}

.cnc-11__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cnc-11__tag {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 6px 11px;
  border-radius: 99px;
  background: oklch(1 0 0/.9);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .02em;
}

.cnc-11__body {
  padding: clamp(18px,3.4vw,26px);
}

.cnc-11__title {
  font-size: 19px;
  font-weight: 680;
  letter-spacing: -.02em;
}

.cnc-11__raised {
  display: flex;
  align-items: baseline;
  gap: 4px;
  flex-wrap: wrap;
  margin-top: 14px;
  font-size: clamp(30px,5.6vw,40px);
  font-weight: 750;
  letter-spacing: -.045em;
  line-height: 1;
  color: var(--cnc-11-acc);
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-11__cur {
  font-size: .66em;
}

.cnc-11__goal {
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0;
  color: var(--cnc-11-mut);
  margin-left: 6px;
}

.cnc-11__meter {
  position: relative;
  height: 16px;
  margin-top: 36px;
  border-radius: 99px;
  background: oklch(0 0 0/.07);
}

.cnc-11__fill {
  position: absolute;
  inset: 0;
  border-radius: 99px;
  transform-origin: left center;
  transform: scaleX(min(1,var(--cnc-11-p,0)));
  background: linear-gradient(90deg,color-mix(in oklch,var(--cnc-11-acc) 70%,oklch(0.8 0.16 120)),var(--cnc-11-acc));
  transition: transform .9s cubic-bezier(.16,1,.3,1);
}

.cnc-11__pip {
  position: absolute;
  top: 50%;
  width: 4px;
  height: 16px;
  translate: -50% -50%;
  border-radius: 2px;
  background: oklch(1 0 0/.85);
  opacity: .55;
  transition: opacity .4s,scale .4s cubic-bezier(.16,1,.3,1);
}

.cnc-11__pip b {
  position: absolute;
  top: -22px;
  left: 50%;
  translate: -50% 0;
  font-size: 10.5px;
  font-weight: 700;
  color: var(--cnc-11-mut);
  opacity: 0;
  transition: opacity .4s;
}

.cnc-11__pip.is-hit {
  opacity: 1;
  scale: 1 1.45;
}

.cnc-11__pip.is-hit b {
  opacity: 1;
  color: var(--cnc-11-acc);
}

.cnc-11__stats {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--cnc-11-mut);
}

.cnc-11__stats b {
  color: var(--cnc-11-ink);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cnc-11__acts {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
}

.cnc-11__btn {
  flex: 1;
  min-width: 96px;
  min-height: 46px;
  border: 1px solid color-mix(in oklch,var(--cnc-11-acc) 40%,transparent);
  border-radius: 12px;
  background: transparent;
  color: var(--cnc-11-acc);
  font: inherit;
  font-size: 13.5px;
  font-weight: 680;
  cursor: pointer;
  transition: background .2s,transform .2s,color .2s;
}

.cnc-11__btn:hover {
  background: color-mix(in oklch,var(--cnc-11-acc) 12%,transparent);
  transform: translateY(-1px);
}

.cnc-11__btn--solid {
  background: var(--cnc-11-acc);
  border-color: transparent;
  color: oklch(0.99 0 0);
}

.cnc-11__btn--solid:hover {
  background: color-mix(in oklch,var(--cnc-11-acc) 86%,black);
  color: oklch(0.99 0 0);
}

.cnc-11__btn:focus-visible {
  outline: 3px solid var(--cnc-11-ink);
  outline-offset: 3px;
}

.cnc-11__feed {
  list-style: none;
  display: grid;
  gap: 6px;
  margin-top: 16px;
  min-height: 0;
}

.cnc-11__feed li {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 10px;
  background: color-mix(in oklch,var(--cnc-11-acc) 8%,transparent);
  font-size: 12.5px;
  color: var(--cnc-11-mut);
  transition: opacity .45s,translate .45s cubic-bezier(.16,1,.3,1);
  opacity: 1;
  translate: 0 0;
}

@starting-style {
  .cnc-11__feed li {
    opacity: 0;
    translate: 0 -8px;
  }
}

.cnc-11__feed b {
  color: var(--cnc-11-ink);
  font-weight: 680;
}

.cnc-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-11-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,480px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-11 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const nf = new Intl.NumberFormat('en-US');
  const money = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const NAMES = ['Priya S.', 'Tom H.', 'Aoife B.', 'Marcus L.', 'Dana K.', 'Yusuf A.', 'Ellie R.'];

  document.querySelectorAll('.cnc-11__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const GOAL = 250000;
    const numEl = card.querySelector('.cnc-11__num');
    const meter = card.querySelector('.cnc-11__meter');
    const pctEl = card.querySelector('.cnc-11__pct');
    const leftEl = card.querySelector('.cnc-11__left');
    const donorsEl = card.querySelector('.cnc-11__donors');
    const feed = card.querySelector('.cnc-11__feed');
    const say = card.querySelector('.cnc-11__sr');
    let raised = 0, donors = 1284, target = 162400;

    const roll = (from, to, ms = 1400) => {
      if (reduce) { numEl.textContent = nf.format(to); return; }
      const t0 = performance.now();
      const frame = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        numEl.textContent = nf.format(p === 1 ? to : Math.round(from + (to - from) * (1 - Math.pow(1 - p, 4))));
        if (p < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    };

    const render = () => {
      const p = raised / GOAL;
      card.style.setProperty('--cnc-11-p', p.toFixed(4));
      meter.setAttribute('aria-valuenow', raised);
      pctEl.textContent = Math.round(p * 100) + '%';
      leftEl.textContent = money.format(Math.max(0, GOAL - raised));
      donorsEl.textContent = nf.format(donors);
      card.querySelectorAll('.cnc-11__pip').forEach((pip) => pip.classList.toggle('is-hit', p * 100 >= +pip.dataset.at));
    };

    const addFeed = (name, amt) => {
      const li = document.createElement('li');
      li.innerHTML = '<b>' + name + '</b> gave ' + money.format(amt);
      feed.prepend(li);
      while (feed.children.length > 3) feed.lastElementChild.remove();
    };

    raised = target; roll(0, raised); render();
    ['Priya S.', 'Tom H.', 'Aoife B.'].forEach((n, i) => addFeed(n, [120, 50, 500][i]));

    card.querySelectorAll('.cnc-11__btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const amt = +btn.dataset.give, prev = raised;
        raised = Math.min(GOAL, raised + amt); donors++;
        roll(prev, raised, 700); render();
        addFeed('You', amt);
        say.textContent = 'Thank you. ' + money.format(raised) + ' raised, ' + Math.round(raised / GOAL * 100) + ' percent of goal';
      });
    });
    let i = 0;
    const id = setInterval(() => {
      if (document.visibilityState !== 'visible') return;
      const amt = [25, 50, 75, 100, 250][Math.floor(Math.random() * 5)];
      const prev = raised; raised = Math.min(GOAL, raised + amt); donors++;
      roll(prev, raised, 600); render(); addFeed(NAMES[i++ % NAMES.length], amt);
    }, 6000);
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
