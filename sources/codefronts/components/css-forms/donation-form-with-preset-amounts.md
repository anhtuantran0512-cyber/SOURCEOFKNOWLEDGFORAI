---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/donation-form-with-preset-amounts/"
title: "Donation Form with Preset Amounts"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A nonprofit donation form designed around the psychology that actually moves people: a one-time/monthly toggle with a sliding pill indicator (pure :has()),…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Donation Form with Preset Amounts
Source: https://codefronts.com/components/css-forms/donation-form-with-preset-amounts/

A nonprofit donation form designed around the psychology that actually moves people: a one-time/monthly toggle with a sliding pill indicator (pure :has()), four preset amounts each paired with a concrete impact line, an “Other” amount that auto-selects as you type, an optional fee-cover that shows the exact extra, a tribute (in honour of) reveal, and a Donate button that always states the real total and frequency.
## HTML
```html
<div class="frm-11">
  <button type="button" class="frm-11__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-11__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-11__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-11__stage">
    <div class="frm-11__wrap">
      <div class="frm-11__card">
        <div class="frm-11__cause">
          <img src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=900&h=900&fit=crop&auto=format&q=70" width="900" height="900" alt="Smiling children gathered together outdoors" loading="lazy" decoding="async">
          <div class="frm-11__causetext">
            <p class="frm-11__tag">Clean Water Fund</p>
            <h2>Every gift brings safe water one step closer.</h2>
            <div class="frm-11__raised">
              <div class="frm-11__bar" role="progressbar" aria-valuemin="0" aria-valuemax="250000" aria-valuenow="182400" aria-label="Campaign progress"><i></i></div>
              <p><b>$182,400</b> raised of $250,000 · 2,140 donors</p>
            </div>
          </div>
        </div>
        <div class="frm-11__form" role="form" aria-labelledby="frm-11-title">
          <h3 id="frm-11-title">Choose your gift</h3>
          <fieldset class="frm-11__freq">
            <legend class="frm-11__sr">Frequency</legend>
            <label><input type="radio" name="frm-11-f" value="once" checked><span>One-time</span></label>
            <label><input type="radio" name="frm-11-f" value="monthly"><span>Monthly <em>♥</em></span></label>
          </fieldset>
          <fieldset class="frm-11__amts">
            <legend class="frm-11__sr">Amount</legend>
            <label><input type="radio" name="frm-11-a" value="25" data-impact="provides a family with a water filter"><span>$25</span></label>
            <label><input type="radio" name="frm-11-a" value="50" checked data-impact="gives 10 children clean water for a year"><span>$50</span></label>
            <label><input type="radio" name="frm-11-a" value="100" data-impact="trains a local well technician"><span>$100</span></label>
            <label><input type="radio" name="frm-11-a" value="250" data-impact="funds a school handwashing station"><span>$250</span></label>
            <label class="frm-11__other"><input type="radio" name="frm-11-a" value="other" data-impact="goes wherever the need is greatest" aria-label="Other amount"><span class="frm-11__cur" aria-hidden="true">$</span><input type="text" inputmode="decimal" class="frm-11__custom" placeholder="Other amount" aria-label="Custom amount in dollars"></label>
          </fieldset>
          <p class="frm-11__impact" aria-live="polite"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11Z"/></svg><span></span></p>
          <label class="frm-11__check"><input type="checkbox" id="frm-11-fee"><span>Add <b class="frm-11__feeamt">$1.75</b> to cover processing fees so 100% reaches the field.</span></label>
          <label class="frm-11__check"><input type="checkbox" id="frm-11-tribute"><span>Give in honour or memory of someone</span></label>
          <fieldset class="frm-11__tribute">
            <legend class="frm-11__sr">Tribute details</legend>
            <div class="frm-11__seg"><label><input type="radio" name="frm-11-t" checked><span>In honour of</span></label><label><input type="radio" name="frm-11-t"><span>In memory of</span></label></div>
            <label for="frm-11-hon" class="frm-11__sr">Honoree's name</label>
            <input id="frm-11-hon" type="text" placeholder="Honoree's full name">
          </fieldset>
          <button type="button" class="frm-11__donate"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"/></svg><span class="frm-11__label">Donate $50</span></button>
          <p class="frm-11__fine" role="status">Tax-deductible · Registered 501(c)(3) · Cancel monthly gifts anytime</p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&display=swap');

@property --frm-11-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.frm-11 {
  --bg: #f1f4ef;
  --card: #ffffff;
  --ink: #132017;
  --muted: #5c6b60;
  --line: #dfe6dc;
  --soft: #f6f9f4;
  --accent: #e8553d;
  --on-accent: #fff;
  --leaf: #1f7a4d;
  --sans: "Lexend",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
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
  .frm-11:not([data-theme="light"]) {
    --bg: #0c120e;
    --card: #131b16;
    --ink: #e8f0ea;
    --muted: #9aaba0;
    --line: #25322a;
    --soft: #18221c;
    --accent: #ff7a5f;
    --on-accent: #2a0a04;
    --leaf: #4ade80;
  }
}

.frm-11[data-theme="dark"] {
  --bg: #0c120e;
  --card: #131b16;
  --ink: #e8f0ea;
  --muted: #9aaba0;
  --line: #25322a;
  --soft: #18221c;
  --accent: #ff7a5f;
  --on-accent: #2a0a04;
  --leaf: #4ade80;
}

.frm-11,
.frm-11 *,
.frm-11 *::before,
.frm-11 *::after {
  box-sizing: border-box;
}

.frm-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3.5rem);
}

.frm-11__wrap {
  width: 100%;
  max-width: 60rem;
  container-type: inline-size;
}

.frm-11__card {
  display: grid;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.75rem;
  overflow: hidden;
  box-shadow: 0 40px 80px -45px rgba(19,32,23,.5);
}

@container (min-width: 46rem) {
  .frm-11__card {
    grid-template-columns: 1fr 1fr;
  }
}

.frm-11__cause {
  position: relative;
  display: grid;
  min-height: 16rem;
  background: #5b7a62;
  color: #fff;
}

.frm-11__cause img {
  grid-area: 1/1;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.frm-11__causetext {
  grid-area: 1/1;
  align-self: end;
  display: grid;
  gap: .9rem;
  padding: clamp(1.25rem,4cqi,2.25rem);
  background: linear-gradient(transparent, rgba(8,20,12,.88) 55%);
}

.frm-11__tag {
  margin: 0;
  justify-self: start;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: .35rem .7rem;
  border-radius: 99px;
  background: rgba(255,255,255,.18);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.frm-11 h2 {
  margin: 0;
  font-size: clamp(1.4rem,4cqi,2rem);
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.frm-11__raised {
  display: grid;
  gap: .5rem;
}

.frm-11__raised p {
  margin: 0;
  font-size: .85rem;
  opacity: .9;
  font-weight: 300;
}

.frm-11__raised b {
  font-weight: 600;
}

.frm-11__bar {
  height: .5rem;
  border-radius: 99px;
  background: rgba(255,255,255,.22);
  overflow: hidden;
}

.frm-11__bar i {
  display: block;
  height: 100%;
  width: var(--frm-11-p);
  border-radius: inherit;
  background: linear-gradient(90deg,#fde68a,#fb923c);
  animation: frm-11-fill 1.6s .3s var(--ease) forwards;
}

@keyframes frm-11-fill {
  to {
    --frm-11-p: 72.96%;
  }
}

.frm-11__form {
  display: grid;
  gap: 1.05rem;
  align-content: start;
  padding: clamp(1.25rem,4cqi,2.25rem);
}

.frm-11 h3 {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 600;
}

.frm-11 fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
}

.frm-11__freq {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  padding: .3rem;
  border-radius: 999px;
  background: var(--soft);
  border: 1px solid var(--line);
  isolation: isolate;
}

.frm-11__freq::before {
  content: '';
  position: absolute;
  z-index: -1;
  inset: .3rem auto .3rem .3rem;
  width: calc(50% - .3rem);
  border-radius: 999px;
  background: var(--ink);
  transition: translate .45s var(--ease);
}

.frm-11__freq:has([value="monthly"]:checked)::before {
  translate: 100% 0;
}

.frm-11__freq label {
  position: relative;
}

.frm-11 :is(.frm-11__freq,.frm-11__amts,.frm-11__seg) input[type="radio"] {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
  z-index: 1;
}

.frm-11__freq span {
  display: grid;
  place-items: center;
  grid-auto-flow: column;
  gap: .35rem;
  min-height: 2.75rem;
  font-weight: 500;
  font-size: .92rem;
  color: var(--muted);
  transition: color .3s;
}

.frm-11__freq em {
  font-style: normal;
  color: var(--accent);
}

.frm-11__freq input:checked + span {
  color: var(--card);
}

.frm-11__freq input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 999px;
}

.frm-11__amts {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .5rem;
}

.frm-11__amts label {
  position: relative;
}

.frm-11__amts > label:not(.frm-11__other) span {
  display: grid;
  place-items: center;
  min-height: 3.4rem;
  border-radius: 1rem;
  border: 1.5px solid var(--line);
  font-size: 1.15rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  transition: all .25s var(--ease);
}

.frm-11__amts label:hover span {
  border-color: color-mix(in oklab,var(--accent) 45%,var(--line));
}

.frm-11__amts input:checked + span {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 10%,var(--card));
  color: var(--accent);
  scale: 1.03;
  box-shadow: 0 8px 20px -12px var(--accent);
}

.frm-11__amts input:focus-visible + span {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.frm-11__other {
  grid-column: 1/-1;
  display: flex;
  align-items: center;
  border-radius: 1rem;
  border: 1.5px solid var(--line);
  transition: border-color .25s;
}

.frm-11__other input[type="radio"] {
  z-index: 0 !important;
}

.frm-11__other:has(input[type="radio"]:checked) {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 6%,var(--card));
}

.frm-11__other:focus-within {
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 18%,transparent);
}

.frm-11__cur {
  position: relative;
  z-index: 1;
  padding-left: 1.1rem;
  font-weight: 600;
  color: var(--muted);
  pointer-events: none;
}

.frm-11__custom {
  position: relative;
  z-index: 2;
  flex: 1;
  min-width: 0;
  min-height: 3.2rem;
  padding: 0 1rem 0 .35rem;
  border: 0;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: 1.05rem;
  font-weight: 500;
}

.frm-11__custom:focus {
  outline: none;
}

.frm-11__impact {
  display: flex;
  align-items: center;
  gap: .6rem;
  margin: 0;
  padding: .8rem 1rem;
  border-radius: 1rem;
  background: color-mix(in oklab,var(--leaf) 10%,var(--card));
  color: var(--leaf);
  font-size: .9rem;
  line-height: 1.4;
}

.frm-11__impact svg {
  flex: none;
  width: 1.25rem;
  height: 1.25rem;
  fill: currentColor;
}

.frm-11__impact span {
  color: var(--ink);
}

.frm-11__impact.is-swap {
  animation: frm-11-swap .45s var(--ease);
}

@keyframes frm-11-swap {
  from {
    opacity: .2;
    translate: 0 4px;
  }
}

.frm-11__check {
  display: flex;
  align-items: flex-start;
  gap: .65rem;
  font-size: .88rem;
  color: var(--muted);
  cursor: pointer;
  line-height: 1.45;
}

.frm-11__check input {
  flex: none;
  width: 1.15rem;
  height: 1.15rem;
  margin: .12rem 0 0;
  accent-color: var(--accent);
}

.frm-11__check b {
  color: var(--ink);
  font-weight: 600;
}

.frm-11__tribute {
  display: none;
  gap: .6rem;
  padding: 1rem;
  border-radius: 1rem;
  background: var(--soft);
  border: 1px solid var(--line);
}

.frm-11:has(#frm-11-tribute:checked) .frm-11__tribute {
  display: grid;
  animation: frm-11-swap .4s var(--ease);
}

.frm-11__seg {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .35rem;
}

.frm-11__seg label {
  position: relative;
}

.frm-11__seg span {
  display: grid;
  place-items: center;
  min-height: 2.5rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  font-size: .85rem;
  background: var(--card);
}

.frm-11__seg input:checked + span {
  border-color: var(--ink);
  font-weight: 600;
}

.frm-11__seg input:focus-visible + span {
  outline: 2px solid var(--accent);
}

.frm-11__tribute input[type="text"] {
  min-height: 2.9rem;
  padding: .6rem .9rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font: inherit;
}

.frm-11__tribute input[type="text"]:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 20%,transparent);
}

.frm-11__donate {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .6rem;
  min-height: 3.5rem;
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--on-accent);
  background: var(--accent);
  box-shadow: 0 14px 30px -14px var(--accent);
  transition: translate .2s var(--ease), filter .2s;
}

.frm-11__donate svg {
  width: 1.2rem;
  height: 1.2rem;
  fill: currentColor;
  transition: scale .3s var(--ease);
}

.frm-11__donate:hover {
  translate: 0 -2px;
  filter: brightness(1.05);
}

.frm-11__donate:hover svg {
  animation: frm-11-beat .8s ease-in-out infinite;
}

@keyframes frm-11-beat {
  0%,
    100% {
    scale: 1;
  }

  30% {
    scale: 1.25;
  }

  60% {
    scale: .95;
  }
}

.frm-11__donate:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-11__fine {
  margin: 0;
  text-align: center;
  font-size: .78rem;
  color: var(--muted);
}

.frm-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-11 *,
    .frm-11 *::before {
    animation: none !important;
    transition: none !important;
  }

  .frm-11__bar i {
    width: 72.96%;
  }
}

@media (forced-colors: active) {
  .frm-11__freq::before {
    background: Highlight;
  }

  .frm-11__amts input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-11__donate {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-11 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-11__theme {
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

.frm-11__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-11__theme:active {
  transform: scale(.94);
}

.frm-11__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-11__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-11__theme .frm-11__sun,
.frm-11__theme[aria-pressed="true"] .frm-11__moon {
  display: none;
}

.frm-11__theme[aria-pressed="true"] .frm-11__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-11__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-11__theme {
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
  document.querySelectorAll('.frm-11').forEach((root) => {
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
  const root = document.querySelector('.frm-11');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const fmt = (n) => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: n % 1 ? 2 : 0 }).format(n);
  const ONCE = [25, 50, 100, 250], MONTHLY = [10, 20, 35, 75];
  const presets = [...root.querySelectorAll('[name="frm-11-a"]:not([value="other"])')];
  const other = $('[name="frm-11-a"][value="other"]'), custom = $('.frm-11__custom'), fee = $('#frm-11-fee');
  const impact = $('.frm-11__impact'), label = $('.frm-11__label');
  const amount = () => { const c = $('[name="frm-11-a"]:checked'); return c === other ? Math.max(0, parseFloat(custom.value.replace(/[^0-9.]/g, '')) || 0) : Number(c.value); };
  const update = (swap) => {
    const monthly = $('[name="frm-11-f"]:checked').value === 'monthly', a = amount();
    const f = a ? Math.round((a * 0.029 + 0.3) * 100) / 100 : 0;
    $('.frm-11__feeamt').textContent = fmt(f);
    const total = a + (fee.checked ? f : 0);
    label.textContent = a ? 'Donate ' + fmt(total) + (monthly ? ' monthly' : '') : 'Enter an amount';
    impact.querySelector('span').textContent = (a ? fmt(a) + (monthly ? ' a month ' : ' ') : 'Your gift ') + $('[name="frm-11-a"]:checked').dataset.impact + '.';
    if (swap) { impact.classList.remove('is-swap'); void impact.offsetWidth; impact.classList.add('is-swap'); }
  };
  root.querySelectorAll('[name="frm-11-f"]').forEach((r) => r.addEventListener('change', () => {
    const set = r.value === 'monthly' ? MONTHLY : ONCE;
    presets.forEach((p, i) => { p.value = set[i]; p.nextElementSibling.textContent = fmt(set[i]); });
    update(true);
  }));
  root.querySelectorAll('[name="frm-11-a"]').forEach((r) => r.addEventListener('change', () => { if (r === other) custom.focus(); update(true); }));
  custom.addEventListener('focus', () => { if (!other.checked) { other.checked = true; update(true); } });
  custom.addEventListener('input', () => { other.checked = true; update(false); });
  fee.addEventListener('change', () => update(false));
  $('.frm-11__donate').addEventListener('click', () => {
    if (!amount()) { custom.focus(); return; }
    $('.frm-11__fine').textContent = 'Thank you! Redirecting to secure payment for ' + label.textContent.replace('Donate ', '') + '…';
  });
  update(false);
})();
```
