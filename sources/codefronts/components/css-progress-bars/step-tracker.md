---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/step-tracker/"
title: "Multi Step Form Completion Progress Tracker"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "A five-step checkout tracker: numbered circles joined by a fill line that grows as you advance, completed steps checkmarked, the current step ringed,…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi Step Form Completion Progress Tracker
Source: https://codefronts.com/components/css-progress-bars/step-tracker/

A five-step checkout tracker: numbered circles joined by a fill line that grows as you advance, completed steps checkmarked, the current step ringed, upcoming steps muted. Every advance rewrites aria-valuenow so the progression is announced, not just drawn.
## HTML
```html
<div class="pb-12">
  <button class="pb-12__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-12__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-12__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-12__stage">
    <div class="pb-12__card">
      <header class="pb-12__head">
        <p class="pb-12__eyebrow"><span class="pb-12__badge">Checkout</span><span class="pb-12__mono" id="pb-12-pct">40% complete</span></p>
        <h2 class="pb-12__title" id="pb-12-title">Shipping address</h2>
        <p class="pb-12__lead" id="pb-12-lead">Where should we send order <span class="pb-12__mono">#CF-20941</span>?</p>
      </header>

      <div class="pb-12__trackWrap">
        <ol class="pb-12__steps" id="pb-12-steps" role="progressbar" aria-valuemin="1" aria-valuemax="5" aria-valuenow="2" aria-valuetext="Step 2 of 5: Address" aria-label="Checkout progress" style="--value:25">
          <span class="pb-12__line" aria-hidden="true"><span class="pb-12__lineFill"></span></span>
          <li class="pb-12__step" data-state="done">
            <span class="pb-12__circle"><span class="pb-12__num">1</span><svg class="pb-12__check" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="pb-12__label">Details</span>
          </li>
          <li class="pb-12__step" data-state="current" aria-current="step">
            <span class="pb-12__circle"><span class="pb-12__num">2</span><svg class="pb-12__check" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="pb-12__label">Address</span>
          </li>
          <li class="pb-12__step" data-state="upcoming">
            <span class="pb-12__circle"><span class="pb-12__num">3</span><svg class="pb-12__check" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="pb-12__label">Payment</span>
          </li>
          <li class="pb-12__step" data-state="upcoming">
            <span class="pb-12__circle"><span class="pb-12__num">4</span><svg class="pb-12__check" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="pb-12__label">Review</span>
          </li>
          <li class="pb-12__step" data-state="upcoming">
            <span class="pb-12__circle"><span class="pb-12__num">5</span><svg class="pb-12__check" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="pb-12__label">Confirm</span>
          </li>
        </ol>
      </div>

      <div class="pb-12__panel" id="pb-12-panel">
        <div class="pb-12__field"><span class="pb-12__fieldLabel">Full name</span><span class="pb-12__fieldValue">Priya Sharma</span></div>
        <div class="pb-12__field"><span class="pb-12__fieldLabel">Street</span><span class="pb-12__fieldValue">18 Alderney Row</span></div>
        <div class="pb-12__field"><span class="pb-12__fieldLabel">City</span><span class="pb-12__fieldValue">Bristol, BS1 4TR</span></div>
        <div class="pb-12__field"><span class="pb-12__fieldLabel">Country</span><span class="pb-12__fieldValue">United Kingdom</span></div>
      </div>

      <div class="pb-12__actions">
        <button class="pb-12__btn" type="button" id="pb-12-back">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M19 12H6M11.4 6.6 6 12l5.4 5.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Back
        </button>
        <button class="pb-12__btn pb-12__btn--primary" type="button" id="pb-12-next">
          Continue<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13M12.6 6.6 18 12l-5.4 5.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
      <p class="pb-12__live" id="pb-12-live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-12 {
  --bg: #f5f6f9;
  --card: #ffffff;
  --card2: #f7f8fb;
  --ink: #0c1119;
  --muted: rgba(12,17,25,.6);
  --line: rgba(12,17,25,.11);
  --track: rgba(12,17,25,.1);
  --accent: #5b21b6;
  --accent-2: #7c3aed;
  --ok: #047857;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% .2 300)) {
  .pb-12 {
    --accent: oklch(45% .2 300);
    --accent-2: oklch(58% .21 296);
    --ok: oklch(52% .13 162);
  }
}

.pb-12 *,
.pb-12 *::before,
.pb-12 *::after {
  box-sizing: border-box;
}

.pb-12__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(75% 55% at 8% 0%,color-mix(in srgb,var(--accent-2) 12%,transparent),transparent 58%), radial-gradient(65% 55% at 100% 100%,color-mix(in srgb,var(--accent) 10%,transparent),transparent 60%);
}

.pb-12__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(12,17,25,.05);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-12__theme:hover {
  transform: translateY(-1px);
}

.pb-12__theme:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 3px;
}

.pb-12__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-12__sun {
  display: block;
}

.pb-12__moon {
  display: none;
}

.pb-12__card {
  inline-size: min(44rem,100%);
  display: grid;
  gap: clamp(1.1rem,2.6vw,1.7rem);
  padding: clamp(1.4rem,3.4vw,2.4rem);
  border-radius: 1.5rem;
  border: 1px solid var(--line);
  background: var(--card);
  box-shadow: 0 1px 2px rgba(12,17,25,.05),0 28px 60px -40px rgba(12,17,25,.45);
}

.pb-12__head {
  display: grid;
  gap: .4rem;
}

.pb-12__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  align-items: center;
}

.pb-12__badge {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .26rem .5rem;
  border-radius: .4rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 10%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 26%,transparent);
}

.pb-12__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-12__title {
  margin: 0;
  font-size: clamp(1.4rem,3.3vw,2rem);
  line-height: 1.14;
  letter-spacing: -.022em;
  font-weight: 650;
}

.pb-12__lead {
  margin: 0;
  font-size: .9rem;
  color: var(--muted);
}

.pb-12__trackWrap {
  padding-inline: .2rem;
}

.pb-12__steps {
  position: relative;
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: .4rem;
}

.pb-12__line {
  position: absolute;
  inset-inline: 10%;
  inset-block-start: 1.35rem;
  block-size: 2px;
  background: var(--track);
  border-radius: 99px;
}

.pb-12__lineFill {
  display: block;
  block-size: 100%;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
  transition: inline-size .45s cubic-bezier(.4,0,.2,1);
}

.pb-12__step {
  position: relative;
  display: grid;
  justify-items: center;
  gap: .45rem;
}

.pb-12__circle {
  position: relative;
  z-index: 1;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  border-radius: 99px;
  border: 2px solid var(--track);
  background: var(--card);
  color: var(--muted);
  font-family: var(--mono);
  font-size: .9rem;
  font-weight: 600;
  transition: border-color .3s,background .3s,color .3s,box-shadow .3s;
}

.pb-12__circle svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  display: none;
}

.pb-12__label {
  font-size: .78rem;
  font-weight: 550;
  color: var(--muted);
  text-align: center;
}

.pb-12__step[data-state="done"] .pb-12__circle {
  border-color: transparent;
  background: var(--accent);
  color: #fff;
}

.pb-12__step[data-state="done"] .pb-12__num {
  display: none;
}

.pb-12__step[data-state="done"] .pb-12__check {
  display: block;
}

.pb-12__step[data-state="done"] .pb-12__label {
  color: var(--ink);
}

.pb-12__step[data-state="current"] .pb-12__circle {
  border-color: var(--accent-2);
  color: var(--accent);
  background: var(--card);
  box-shadow: 0 0 0 4px color-mix(in srgb,var(--accent-2) 20%,transparent);
}

.pb-12__step[data-state="current"] .pb-12__label {
  color: var(--ink);
  font-weight: 650;
}

.pb-12__panel {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: .15rem .9rem;
  padding: clamp(.9rem,2.2vw,1.3rem);
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  background: var(--card2);
}

.pb-12__field {
  display: grid;
  gap: .15rem;
  padding-block: .5rem;
}

.pb-12__fieldLabel {
  font-family: var(--mono);
  font-size: .63rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.pb-12__fieldValue {
  font-size: .92rem;
  font-weight: 550;
}

.pb-12__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  justify-content: flex-end;
}

.pb-12__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.9rem;
  padding: .7rem 1.2rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: var(--card2);
  color: var(--ink);
  font: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform .18s,background .18s;
}

.pb-12__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.pb-12__btn:hover:not([disabled]) {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
}

.pb-12__btn:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 3px;
}

.pb-12__btn[disabled] {
  opacity: .45;
  cursor: not-allowed;
}

.pb-12__btn--primary {
  background: var(--accent);
  border-color: transparent;
  color: #fff;
  box-shadow: 0 14px 30px -18px var(--accent);
}

.pb-12__btn--primary:hover {
  background: color-mix(in srgb,var(--accent) 88%,black);
}

.pb-12__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .8rem;
  color: var(--ok);
  font-weight: 550;
}

.pb-12[data-theme="dark"] {
  --bg: #0a0912;
  --card: #100e1b;
  --card2: #161327;
  --ink: #eeecfa;
  --muted: rgba(238,236,250,.62);
  --line: rgba(238,236,250,.13);
  --track: rgba(238,236,250,.14);
  --accent: #a78bfa;
  --accent-2: #c4b5fd;
  --ok: #34d399;
}

.pb-12[data-theme="dark"] .pb-12__theme {
  background: rgba(255,255,255,.07);
}

.pb-12[data-theme="dark"] .pb-12__sun {
  display: none;
}

.pb-12[data-theme="dark"] .pb-12__moon {
  display: block;
}

.pb-12[data-theme="dark"] .pb-12__step[data-state="done"] .pb-12__circle,
.pb-12[data-theme="dark"] .pb-12__btn--primary {
  color: #160c2a;
}

@media (prefers-color-scheme: dark) {
  .pb-12:not([data-theme="light"]) {
    --bg: #0a0912;
    --card: #100e1b;
    --card2: #161327;
    --ink: #eeecfa;
    --muted: rgba(238,236,250,.62);
    --line: rgba(238,236,250,.13);
    --track: rgba(238,236,250,.14);
    --accent: #a78bfa;
    --accent-2: #c4b5fd;
    --ok: #34d399;
  }

  .pb-12:not([data-theme="light"]) .pb-12__theme {
    background: rgba(255,255,255,.07);
  }

  .pb-12:not([data-theme="light"]) .pb-12__sun {
    display: none;
  }

  .pb-12:not([data-theme="light"]) .pb-12__moon {
    display: block;
  }

  .pb-12:not([data-theme="light"]) .pb-12__step[data-state="done"] .pb-12__circle,
    .pb-12:not([data-theme="light"]) .pb-12__btn--primary {
    color: #160c2a;
  }
}

@media (max-width: 30rem) {
  .pb-12__label {
    font-size: .68rem;
  }

  .pb-12__circle {
    inline-size: 2.4rem;
    block-size: 2.4rem;
    font-size: .82rem;
  }

  .pb-12__line {
    inset-block-start: 1.2rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-12 *,
    .pb-12 *::before,
    .pb-12 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-12__card,
    .pb-12__circle,
    .pb-12__btn,
    .pb-12__panel,
    .pb-12__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .pb-12__lineFill {
    background: Highlight;
  }

  .pb-12__step[data-state="done"] .pb-12__circle {
    background: Highlight;
    color: Canvas;
  }
}
```

## JavaScript
```js
const pb12 = document.querySelector('.pb-12');
if (pb12) {
  const q = (s) => pb12.querySelector(s);
  const list = q('#pb-12-steps'), steps = [...pb12.querySelectorAll('.pb-12__step')];
  const CONTENT = [
    { t: 'Your details', l: 'Tell us who the order is for.', f: [['Full name','Priya Sharma'],['Email','[email protected]'],['Phone','+44 7700 900 812'],['Account','Team workspace']] },
    { t: 'Shipping address', l: 'Where should we send order <span class="pb-12__mono">#CF-20941</span>?', f: [['Full name','Priya Sharma'],['Street','18 Alderney Row'],['City','Bristol, BS1 4TR'],['Country','United Kingdom']] },
    { t: 'Payment', l: 'Charged once, no stored card.', f: [['Method','Visa ending 4291'],['Expiry','04 / 29'],['Billing','Same as shipping'],['Total','GBP 148.00']] },
    { t: 'Review order', l: 'Last look before we place it.', f: [['Items','3 items'],['Delivery','Tue 18 Aug'],['Shipping','Free'],['Total','GBP 148.00']] },
    { t: 'Confirm', l: 'Everything checks out.', f: [['Order','#CF-20941'],['Status','Ready to place'],['Receipt','[email protected]'],['Total','GBP 148.00']] },
  ];
  let i = 1;
  const render = () => {
    steps.forEach((s, n) => {
      s.dataset.state = n < i ? 'done' : n === i ? 'current' : 'upcoming';
      if (n === i) s.setAttribute('aria-current', 'step'); else s.removeAttribute('aria-current');
    });
    const c = CONTENT[i], name = steps[i].querySelector('.pb-12__label').textContent;
    list.style.setProperty('--value', (i / (steps.length - 1)) * 100);
    list.setAttribute('aria-valuenow', i + 1);
    list.setAttribute('aria-valuetext', 'Step ' + (i + 1) + ' of ' + steps.length + ': ' + name);
    q('#pb-12-title').textContent = c.t; q('#pb-12-lead').innerHTML = c.l;
    q('#pb-12-pct').textContent = Math.round((i / (steps.length - 1)) * 100) + '% complete';
    q('#pb-12-panel').innerHTML = c.f.map((r) => '<div class="pb-12__field"><span class="pb-12__fieldLabel">' + r[0] + '</span><span class="pb-12__fieldValue">' + r[1] + '</span></div>').join('');
    q('#pb-12-back').disabled = i === 0;
    q('#pb-12-next').firstChild.textContent = i === steps.length - 1 ? 'Place order' : 'Continue';
    q('#pb-12-live').textContent = 'Step ' + (i + 1) + ' of ' + steps.length + ': ' + name;
  };
  const go = (d) => { i = Math.max(0, Math.min(steps.length - 1, i + d)); render(); };
  q('#pb-12-next').addEventListener('click', () => go(1));
  q('#pb-12-back').addEventListener('click', () => go(-1));
  list.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight') go(1); else if (e.key === 'ArrowLeft') go(-1); });
  q('.pb-12__theme').addEventListener('click', (e) => {
    const dark = pb12.dataset.theme !== 'dark';
    pb12.dataset.theme = dark ? 'dark' : 'light';
    e.currentTarget.setAttribute('aria-pressed', String(dark));
  });
  render();
}
```
