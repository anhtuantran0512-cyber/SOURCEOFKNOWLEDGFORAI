---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/mortgage-pre-qualification-form/"
title: "Mortgage Pre-Qualification Form"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A pre-qualification form that earns the lead by being useful first: linked slider + number inputs for home price and down payment (in % and $), a loan-term…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mortgage Pre-Qualification Form
Source: https://codefronts.com/components/css-forms/mortgage-pre-qualification-form/

A pre-qualification form that earns the lead by being useful first: linked slider + number inputs for home price and down payment (in % and $), a loan-term segmented control, credit band chips, income and debts — and a live results panel with the monthly payment, an animated conic-gradient donut splitting principal & interest, tax, insurance and PMI, a colour-coded debt-to-income gauge, and a plain-English pre-qualification verdict.
## HTML
```html
<div class="frm-16">
  <button type="button" class="frm-16__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-16__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-16__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-16__stage">
    <div class="frm-16__wrap">
      <div class="frm-16__card">
        <div class="frm-16__form" role="form" aria-labelledby="frm-16-title">
          <p class="frm-16__eyebrow">Pre-qualify in 60 seconds · No credit impact</p>
          <h2 id="frm-16-title">How much home can you afford?</h2>
          <div class="frm-16__field">
            <div class="frm-16__lr"><label for="frm-16-price-n">Home price</label><div class="frm-16__money"><span aria-hidden="true">$</span><input id="frm-16-price-n" type="number" min="100000" max="2000000" step="5000" value="485000"></div></div>
            <input type="range" class="frm-16__range" data-pair="frm-16-price-n" min="100000" max="2000000" step="5000" value="485000" aria-label="Home price slider">
          </div>
          <div class="frm-16__field">
            <div class="frm-16__lr"><label for="frm-16-down-n">Down payment <b class="frm-16__downamt"></b></label><div class="frm-16__money"><input id="frm-16-down-n" type="number" min="3" max="60" step="1" value="20"><span aria-hidden="true">%</span></div></div>
            <input type="range" class="frm-16__range" data-pair="frm-16-down-n" min="3" max="60" step="1" value="20" aria-label="Down payment percent slider">
          </div>
          <fieldset class="frm-16__seg"><legend>Loan term</legend>
            <label><input type="radio" name="frm-16-t" value="15"><span>15 yr</span></label><label><input type="radio" name="frm-16-t" value="20"><span>20 yr</span></label><label><input type="radio" name="frm-16-t" value="30" checked><span>30 yr</span></label>
          </fieldset>
          <fieldset class="frm-16__seg frm-16__credit"><legend>Credit score</legend>
            <label><input type="radio" name="frm-16-c" value="760"><span>760+</span></label><label><input type="radio" name="frm-16-c" value="700" checked><span>700–759</span></label><label><input type="radio" name="frm-16-c" value="660"><span>660–699</span></label><label><input type="radio" name="frm-16-c" value="620"><span>620–659</span></label><label><input type="radio" name="frm-16-c" value="580"><span>&lt;620</span></label>
          </fieldset>
          <div class="frm-16__grid">
            <div class="frm-16__field"><label for="frm-16-inc">Annual household income</label><div class="frm-16__money frm-16__money--full"><span aria-hidden="true">$</span><input id="frm-16-inc" type="number" min="0" step="1000" value="142000"></div></div>
            <div class="frm-16__field"><label for="frm-16-debt">Monthly debts <span class="frm-16__opt">car, cards, loans</span></label><div class="frm-16__money frm-16__money--full"><span aria-hidden="true">$</span><input id="frm-16-debt" type="number" min="0" step="50" value="650"></div></div>
          </div>
        </div>
        <aside class="frm-16__out" aria-labelledby="frm-16-out-h">
          <figure class="frm-16__photo"><img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&h=400&fit=crop&auto=format&q=70" width="800" height="400" alt="Modern two-storey house with a pool at dusk" loading="lazy" decoding="async"></figure>
          <h3 id="frm-16-out-h" class="frm-16__sr">Your estimate</h3>
          <div class="frm-16__payrow">
            <div class="frm-16__donut" aria-hidden="true"><div><b class="frm-16__pay">$0</b><small>per month</small></div></div>
            <ul class="frm-16__legend">
              <li style="--c:var(--c1)"><span>Principal &amp; interest</span><b data-k="pi"></b></li>
              <li style="--c:var(--c2)"><span>Property tax</span><b data-k="tax"></b></li>
              <li style="--c:var(--c3)"><span>Home insurance</span><b data-k="ins"></b></li>
              <li style="--c:var(--c4)"><span>PMI</span><b data-k="pmi"></b></li>
            </ul>
          </div>
          <p class="frm-16__sr" aria-live="polite" id="frm-16-live"></p>
          <div class="frm-16__dti">
            <div class="frm-16__lr"><span>Debt-to-income</span><b class="frm-16__dtival">0%</b></div>
            <div class="frm-16__gauge" aria-hidden="true"><i></i><span style="left:36%"></span><span style="left:43%"></span></div>
          </div>
          <div class="frm-16__verdict" data-v="ok"><b class="frm-16__vtitle"></b><p class="frm-16__vtext"></p></div>
          <dl class="frm-16__facts"><div><dt>Loan amount</dt><dd data-k="loan"></dd></div><div><dt>Est. rate</dt><dd data-k="rate"></dd></div><div><dt>Max price (43% DTI)</dt><dd data-k="max"></dd></div></dl>
          <button type="button" class="frm-16__cta">Get pre-qualified</button>
          <p class="frm-16__fine">Estimates only — not a loan offer. Rates for illustration.</p>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&display=swap');

@property --frm-16-a {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

@property --frm-16-b {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

@property --frm-16-c {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

.frm-16 {
  --bg: #ecebe6;
  --card: #fbfaf7;
  --ink: #191a17;
  --muted: #6a6b63;
  --line: #e0ded6;
  --soft: #f2f1ec;
  --accent: #2f5d50;
  --on-accent: #fff;
  --c1: #2f5d50;
  --c2: #8fb3a5;
  --c3: #d6a45c;
  --c4: #c46b4f;
  --ok: #2f7d4a;
  --warn: #b7791f;
  --bad: #b33a2b;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-16:not([data-theme="light"]) {
    --bg: #0f100e;
    --card: #171815;
    --ink: #efeee8;
    --muted: #a3a49a;
    --line: #2a2b26;
    --soft: #1e1f1b;
    --accent: #7fc4ad;
    --on-accent: #0c1f19;
    --c1: #7fc4ad;
    --c2: #3f7466;
    --c3: #e0b06a;
    --c4: #e08466;
    --ok: #6fcf8f;
    --warn: #f0b54d;
    --bad: #ff7d6b;
  }
}

.frm-16[data-theme="dark"] {
  --bg: #0f100e;
  --card: #171815;
  --ink: #efeee8;
  --muted: #a3a49a;
  --line: #2a2b26;
  --soft: #1e1f1b;
  --accent: #7fc4ad;
  --on-accent: #0c1f19;
  --c1: #7fc4ad;
  --c2: #3f7466;
  --c3: #e0b06a;
  --c4: #e08466;
  --ok: #6fcf8f;
  --warn: #f0b54d;
  --bad: #ff7d6b;
}

.frm-16,
.frm-16 *,
.frm-16 *::before,
.frm-16 *::after {
  box-sizing: border-box;
}

.frm-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3.5rem);
}

.frm-16__wrap {
  width: 100%;
  max-width: 66rem;
  container-type: inline-size;
}

.frm-16__card {
  display: grid;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 40px 80px -45px rgba(25,26,23,.5);
}

@container (min-width: 54rem) {
  .frm-16__card {
    grid-template-columns: minmax(0,1.15fr) minmax(0,1fr);
  }
}

.frm-16__form {
  display: grid;
  gap: 1.3rem;
  align-content: start;
  padding: clamp(1.25rem,4cqi,2.5rem);
}

.frm-16__eyebrow {
  margin: 0;
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
}

.frm-16 h2 {
  margin: -.5rem 0 0;
  font-size: clamp(1.6rem,4.4cqi,2.4rem);
  font-weight: 800;
  letter-spacing: -.04em;
  line-height: 1.05;
  font-stretch: 110%;
}

.frm-16__field {
  display: grid;
  gap: .35rem;
}

.frm-16 label,
.frm-16 legend {
  font-size: .88rem;
  font-weight: 600;
}

.frm-16__opt {
  font-weight: 400;
  color: var(--muted);
}

.frm-16__downamt {
  font-weight: 500;
  color: var(--muted);
  margin-left: .3rem;
}

.frm-16__lr {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: .5rem;
}

.frm-16__money {
  display: flex;
  align-items: center;
  gap: .2rem;
  padding: 0 .75rem;
  min-height: 2.75rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: var(--soft);
  font-weight: 700;
  transition: border-color .2s, box-shadow .2s;
}

.frm-16__money:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 20%,transparent);
}

.frm-16__money span {
  color: var(--muted);
}

.frm-16__money input {
  width: 7.5rem;
  border: 0;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: 1.05rem;
  font-weight: 700;
  text-align: right;
  font-variant-numeric: tabular-nums;
  -moz-appearance: textfield;
}

.frm-16__money input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.frm-16__money input:focus {
  outline: none;
}

.frm-16__money--full input {
  width: 100%;
  text-align: left;
}

.frm-16__range {
  --fill: 50%;
  appearance: none;
  -webkit-appearance: none;
  width: 100%;
  height: 2.5rem;
  background: transparent;
  cursor: pointer;
}

.frm-16__range::-webkit-slider-runnable-track {
  height: .4rem;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent) var(--fill),var(--line) var(--fill));
}

.frm-16__range::-moz-range-track {
  height: .4rem;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent) var(--fill),var(--line) var(--fill));
}

.frm-16__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 1.6rem;
  height: 1.6rem;
  margin-top: -.6rem;
  border-radius: .5rem;
  background: var(--card);
  border: 2px solid var(--accent);
  box-shadow: 0 4px 10px -3px rgba(0,0,0,.3);
  rotate: 45deg;
  transition: scale .2s var(--ease);
}

.frm-16__range::-moz-range-thumb {
  width: 1.3rem;
  height: 1.3rem;
  border-radius: .4rem;
  background: var(--card);
  border: 2px solid var(--accent);
}

.frm-16__range:active::-webkit-slider-thumb {
  scale: 1.15;
}

.frm-16__range:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .4rem;
}

.frm-16 fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
}

.frm-16__seg legend {
  padding: 0;
  margin-bottom: .5rem;
}

.frm-16__seg {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .35rem;
}

.frm-16__credit {
  grid-template-columns: repeat(auto-fit,minmax(4.5rem,1fr));
}

.frm-16__seg label {
  position: relative;
}

.frm-16__seg input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-16__seg span {
  display: grid;
  place-items: center;
  min-height: 2.75rem;
  border-radius: .65rem;
  border: 1px solid var(--line);
  font-size: .88rem;
  font-weight: 600;
  transition: all .2s;
}

.frm-16__seg label:hover span {
  border-color: var(--muted);
}

.frm-16__seg input:checked + span {
  background: var(--ink);
  color: var(--card);
  border-color: var(--ink);
}

.frm-16__seg input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.frm-16__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,12rem),1fr));
}

.frm-16__out {
  display: grid;
  gap: 1.2rem;
  align-content: start;
  padding: clamp(1.25rem,4cqi,2.25rem);
  background: var(--soft);
  border-top: 1px solid var(--line);
}

@container (min-width: 54rem) {
  .frm-16__out {
    border-top: 0;
    border-left: 1px solid var(--line);
  }
}

.frm-16__photo {
  margin: calc(clamp(1.25rem,4cqi,2.25rem) * -1) calc(clamp(1.25rem,4cqi,2.25rem) * -1) 0;
  height: 9rem;
  background: #b9b4a6;
}

.frm-16__photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.frm-16__payrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1.25rem;
}

.frm-16__donut {
  --frm-16-a: 0%;
  flex: none;
  position: relative;
  display: grid;
  place-items: center;
  width: 9.5rem;
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(var(--c1) 0 var(--frm-16-a), var(--c2) 0 var(--frm-16-b), var(--c3) 0 var(--frm-16-c), var(--c4) 0);
  transition: --frm-16-a .7s var(--ease), --frm-16-b .7s var(--ease), --frm-16-c .7s var(--ease);
}

.frm-16__donut > div {
  display: grid;
  place-items: center;
  align-content: center;
  width: 72%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--soft);
  text-align: center;
}

.frm-16__pay {
  font-size: 1.45rem;
  font-weight: 800;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.frm-16__donut small {
  font-size: .72rem;
  color: var(--muted);
}

.frm-16__legend {
  flex: 1;
  min-width: 11rem;
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .45rem;
  font-size: .86rem;
}

.frm-16__legend li {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.frm-16__legend li::before {
  content: '';
  width: .7rem;
  height: .7rem;
  border-radius: .2rem;
  background: var(--c);
  flex: none;
}

.frm-16__legend span {
  flex: 1;
  color: var(--muted);
}

.frm-16__legend b {
  font-variant-numeric: tabular-nums;
}

.frm-16__dti {
  display: grid;
  gap: .5rem;
  font-size: .88rem;
  font-weight: 600;
}

.frm-16__gauge {
  position: relative;
  height: .6rem;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--ok) 0 36%,var(--warn) 36% 43%,var(--bad) 43%);
}

.frm-16__gauge i {
  position: absolute;
  top: 50%;
  left: var(--dti,0%);
  width: 1.1rem;
  height: 1.1rem;
  margin: -.55rem 0 0 -.55rem;
  border-radius: 50%;
  background: var(--card);
  border: 3px solid var(--ink);
  transition: left .6s var(--ease);
}

.frm-16__gauge span {
  position: absolute;
  top: -.25rem;
  bottom: -.25rem;
  width: 2px;
  background: var(--card);
}

.frm-16__verdict {
  padding: .9rem 1rem;
  border-radius: .9rem;
  border: 1px solid;
}

.frm-16__verdict[data-v="ok"] {
  color: var(--ok);
  background: color-mix(in oklab,var(--ok) 9%,var(--card));
}

.frm-16__verdict[data-v="warn"] {
  color: var(--warn);
  background: color-mix(in oklab,var(--warn) 10%,var(--card));
}

.frm-16__verdict[data-v="bad"] {
  color: var(--bad);
  background: color-mix(in oklab,var(--bad) 9%,var(--card));
}

.frm-16__verdict b {
  display: block;
  font-size: 1rem;
}

.frm-16__verdict p {
  margin: .25rem 0 0;
  color: var(--ink);
  font-size: .86rem;
  line-height: 1.45;
}

.frm-16__facts {
  margin: 0;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .5rem;
}

.frm-16__facts div {
  padding: .65rem .7rem;
  border-radius: .7rem;
  background: var(--card);
  border: 1px solid var(--line);
}

.frm-16__facts dt {
  font-size: .7rem;
  color: var(--muted);
  font-weight: 600;
}

.frm-16__facts dd {
  margin: .15rem 0 0;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  font-size: .95rem;
}

.frm-16__cta {
  min-height: 3.2rem;
  border: 0;
  border-radius: .85rem;
  cursor: pointer;
  font: inherit;
  font-weight: 700;
  font-size: 1rem;
  color: var(--on-accent);
  background: var(--accent);
  transition: translate .2s var(--ease), filter .2s;
}

.frm-16__cta:hover {
  translate: 0 -2px;
  filter: brightness(1.07);
}

.frm-16__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-16__fine {
  margin: -.6rem 0 0;
  text-align: center;
  font-size: .74rem;
  color: var(--muted);
}

.frm-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-16 * {
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-16__donut {
    border: 2px solid CanvasText;
  }

  .frm-16__seg input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-16__cta {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-16 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-16__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-16__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-16__theme:active {
  transform: scale(.94);
}

.frm-16__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-16__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-16__theme .frm-16__sun,
.frm-16__theme[aria-pressed="true"] .frm-16__moon {
  display: none;
}

.frm-16__theme[aria-pressed="true"] .frm-16__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-16__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-16__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-16').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-16');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  const RATES = { 760: .0612, 700: .0645, 660: .0689, 620: .0749, 580: .0839 }, TAX = .011, INS = 1600;
  const pmt = (loan, rate, years) => { const r = rate / 12, n = years * 12; return loan * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1); };
  const fill = (r) => r.style.setProperty('--fill', ((r.value - r.min) / (r.max - r.min)) * 100 + '%');
  root.querySelectorAll('.frm-16__range').forEach((r) => {
    const n = root.querySelector('#' + r.dataset.pair);
    r.addEventListener('input', () => { n.value = r.value; fill(r); calc(); });
    n.addEventListener('input', () => { r.value = n.value; fill(r); calc(); });
    fill(r);
  });
  root.addEventListener('change', calc);
  root.querySelectorAll('#frm-16-inc, #frm-16-debt').forEach((i) => i.addEventListener('input', calc));
  function calc() {
    const price = Number($('#frm-16-price-n').value) || 0, down = Math.min(60, Math.max(3, Number($('#frm-16-down-n').value) || 0)) / 100;
    const years = Number($('[name="frm-16-t"]:checked').value), band = $('[name="frm-16-c"]:checked').value;
    const rate = RATES[band] - (years === 15 ? .0065 : years === 20 ? .003 : 0);
    const loan = price * (1 - down), pi = pmt(loan, rate, years), tax = price * TAX / 12, ins = INS / 12, pmi = down < .2 ? loan * .005 / 12 : 0;
    const total = pi + tax + ins + pmi, income = (Number($('#frm-16-inc').value) || 0) / 12, debts = Number($('#frm-16-debt').value) || 0;
    const dti = income ? (total + debts) / income : 1;
    const d = $('.frm-16__donut'), a = pi / total * 100, b = a + tax / total * 100, c = b + ins / total * 100;
    d.style.setProperty('--frm-16-a', a + '%'); d.style.setProperty('--frm-16-b', b + '%'); d.style.setProperty('--frm-16-c', c + '%');
    $('.frm-16__pay').textContent = fmt.format(total);
    $('[data-k="pi"]').textContent = fmt.format(pi); $('[data-k="tax"]').textContent = fmt.format(tax);
    $('[data-k="ins"]').textContent = fmt.format(ins); $('[data-k="pmi"]').textContent = pmi ? fmt.format(pmi) : '—';
    $('.frm-16__downamt').textContent = '(' + fmt.format(price * down) + ')';
    $('[data-k="loan"]').textContent = fmt.format(loan); $('[data-k="rate"]').textContent = (rate * 100).toFixed(2) + '%';
    const budget = income * .43 - debts, perK = (pmt(1000 * (1 - down), rate, years) + 1000 * TAX / 12 + (down < .2 ? 1000 * (1 - down) * .005 / 12 : 0));
    $('[data-k="max"]').textContent = budget > ins ? fmt.format(Math.max(0, (budget - ins) / perK * 1000)) : '—';
    const pct = Math.round(dti * 100);
    $('.frm-16__dtival').textContent = pct + '%';
    $('.frm-16__gauge').style.setProperty('--dti', Math.min(100, pct) + '%');
    const v = $('.frm-16__verdict');
    if (dti <= .36) { v.dataset.v = 'ok'; $('.frm-16__vtitle').textContent = 'Likely to pre-qualify'; $('.frm-16__vtext').textContent = 'Your DTI is comfortably under 36%. Most lenders would see this as a strong application.'; }
    else if (dti <= .43) { v.dataset.v = 'warn'; $('.frm-16__vtitle').textContent = 'Borderline — but possible'; $('.frm-16__vtext').textContent = 'You\'re between 36% and 43% DTI. A larger down payment or paying off a debt would strengthen your file.'; }
    else { v.dataset.v = 'bad'; $('.frm-16__vtitle').textContent = 'Stretch for this price'; $('.frm-16__vtext').textContent = 'Above 43% DTI, most qualified mortgages won\'t fit. Try a lower price or longer term.'; }
    $('#frm-16-live').textContent = 'Estimated payment ' + fmt.format(total) + ' per month. ' + $('.frm-16__vtitle').textContent + '.';
  }
  $('.frm-16__cta').addEventListener('click', () => { $('.frm-16__cta').textContent = 'Great — we\'ll email your pre-qualification letter'; });
  calc();
})();
```
