---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/car-rental-and-travel-reservation/"
title: "Car Rental & Travel Reservation"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A travel-booking reservation flow — Vehicle → Protection → Driver → Confirm — with comparison-style vehicle cards (spec chips, per-day pricing), protection…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Car Rental & Travel Reservation
Source: https://codefronts.com/components/css-multi-step-form/car-rental-and-travel-reservation/

A travel-booking reservation flow — Vehicle → Protection → Driver → Confirm — with comparison-style vehicle cards (spec chips, per-day pricing), protection add-on toggles that reprice the trip live, and a boarding-pass style confirmation. The per-day × days math updates in a sticky trip bar on every step.
## HTML
```html
<section class="msf-15" aria-label="Car rental demo">
  <form class="msf-15__card" novalidate>
    <header class="msf-15__head">
      <div><span class="msf-15__logo">✈ DRIFT rentals</span><p class="msf-15__trip">SFO Airport · Jun 12 → Jun 16 <b>(4 days)</b></p></div>
      <ol class="msf-15__crumbs"><li class="is-active" aria-current="step">Vehicle</li><li>Protection</li><li>Driver</li><li>Confirm</li></ol>
    </header>
    <fieldset class="msf-15__step">
      <h3 class="msf-15__title" tabindex="-1">Choose your ride</h3>
      <div class="msf-15__fleet" role="radiogroup" aria-label="Vehicle">
        <label class="msf-15__car" data-rate="54"><input type="radio" name="car" value="Compact — Corolla or similar" required><div class="msf-15__carhead"><b>Compact</b><span>$54<i>/day</i></span></div><small>Corolla or similar</small><p class="msf-15__chips"><span>⛽ 38 mpg</span><span>👤 5</span><span>🧳 2</span></p></label>
        <label class="msf-15__car" data-rate="79"><input type="radio" name="car" value="SUV — RAV4 or similar"><div class="msf-15__carhead"><b>SUV</b><span>$79<i>/day</i></span></div><small>RAV4 or similar</small><p class="msf-15__chips"><span>⛽ 30 mpg</span><span>👤 5</span><span>🧳 4</span></p></label>
        <label class="msf-15__car" data-rate="129"><input type="radio" name="car" value="Electric — Model 3 or similar"><div class="msf-15__carhead"><b>Electric</b><span>$129<i>/day</i></span></div><small>Model 3 or similar</small><p class="msf-15__chips"><span>⚡ 270 mi</span><span>👤 5</span><span>🧳 3</span></p></label>
      </div>
      <div class="msf-15__nav"><span></span><button type="button" class="msf-15__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-15__step" hidden>
      <h3 class="msf-15__title" tabindex="-1">Protect the trip</h3>
      <div class="msf-15__addons">
        <label class="msf-15__toggle" data-rate="19"><div><b>Collision coverage</b><small>Zero deductible on any damage</small></div><span class="msf-15__price">+$19/day</span><i class="msf-15__switch" aria-hidden="true"></i><input type="checkbox" name="addon" value="Collision coverage"></label>
        <label class="msf-15__toggle" data-rate="11"><div><b>Roadside assist</b><small>Towing, lockout, flat tire</small></div><span class="msf-15__price">+$11/day</span><i class="msf-15__switch" aria-hidden="true"></i><input type="checkbox" name="addon" value="Roadside assist"></label>
        <label class="msf-15__toggle" data-rate="9"><div><b>Additional driver</b><small>Share the wheel legally</small></div><span class="msf-15__price">+$9/day</span><i class="msf-15__switch" aria-hidden="true"></i><input type="checkbox" name="addon" value="Additional driver"></label>
      </div>
      <div class="msf-15__nav"><button type="button" class="msf-15__back">Back</button><button type="button" class="msf-15__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-15__step" hidden>
      <h3 class="msf-15__title" tabindex="-1">Driver details</h3>
      <div class="msf-15__grid">
        <label class="msf-15__field"><span>Driver's full name</span><input type="text" name="driver" autocomplete="name" required placeholder="Casey Nakamura"></label>
        <label class="msf-15__field"><span>Age band</span><select name="age" required><option value="">Select…</option><option>25–69</option><option>21–24 (young driver fee)</option><option>70+</option></select></label>
        <label class="msf-15__field"><span>License number</span><input type="text" name="license" required placeholder="D8842-77190" style="font-family:ui-monospace,monospace"></label>
        <label class="msf-15__field"><span>Email for confirmation</span><input type="email" name="email" autocomplete="email" required placeholder="[email protected]"></label>
      </div>
      <div class="msf-15__nav"><button type="button" class="msf-15__back">Back</button><button type="button" class="msf-15__next">Review booking</button></div>
    </fieldset>
    <fieldset class="msf-15__step" hidden>
      <h3 class="msf-15__title" tabindex="-1">Confirm your reservation</h3>
      <div class="msf-15__ticket"></div>
      <div class="msf-15__nav"><button type="button" class="msf-15__back">Back</button><button type="button" class="msf-15__next msf-15__next--go">Book now — free cancellation</button></div>
    </fieldset>
    <div class="msf-15__done" hidden><b>✈</b><h3 tabindex="-1">You're booked!</h3><p class="msf-15__donemsg"></p></div>
    <footer class="msf-15__bar"><span>Trip total</span><b class="msf-15__total" aria-live="polite">$0</b></footer>
  </form>
</section>
```
## CSS
```css
.msf-15,
.msf-15 *,
.msf-15 *::before,
.msf-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-15 {
  width: 100%;
  min-height: 100vh;
  --sun: oklch(0.7 0.17 45);
  --sky: oklch(0.55 0.13 250);
  --ink: oklch(0.26 0.02 250);
  --mut: oklch(0.52 0.02 250);
  --line: oklch(0.9 0.008 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: linear-gradient(165deg,oklch(0.93 0.03 250),oklch(0.94 0.04 45));
  display: grid;
  place-items: center;
}

.msf-15__card {
  width: min(620px,100%);
  background: #fff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 30px 80px -35px oklch(0.45 0.12 250/.5);
}

.msf-15__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  padding: 20px 28px;
  background: linear-gradient(100deg,var(--sky),var(--sun));
  color: #fff;
}

.msf-15__logo {
  font-weight: 800;
  font-size: 15px;
  letter-spacing: .02em;
}

.msf-15__trip {
  font-size: 12.5px;
  opacity: .92;
}

.msf-15__crumbs {
  display: flex;
  gap: 12px;
  list-style: none;
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .05em;
}

.msf-15__crumbs li {
  opacity: .6;
  padding-bottom: 3px;
  border-bottom: 2px solid transparent;
}

.msf-15__crumbs li.is-active {
  opacity: 1;
  border-bottom-color: #fff;
}

.msf-15__crumbs li.is-done {
  opacity: .85;
}

.msf-15__crumbs li.is-done::after {
  content: " ✓";
}

.msf-15__step {
  border: none;
  padding: 24px 28px;
}

.msf-15__step:not([hidden]) {
  animation: msf-15-in .35s cubic-bezier(.2,.8,.2,1);
}

.msf-15__title {
  font-size: 20px;
  letter-spacing: -.01em;
  margin-bottom: 16px;
  outline: none;
}

.msf-15__fleet {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
}

@media (max-width: 560px) {
  .msf-15__fleet {
    grid-template-columns: 1fr;
  }
}

.msf-15__car {
  display: grid;
  gap: 6px;
  padding: 16px;
  border: 2px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  transition: all .18s;
}

.msf-15__car input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-15__carhead {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.msf-15__carhead b {
  font-size: 15px;
}

.msf-15__carhead span {
  font-weight: 800;
  color: var(--sky);
  font-variant-numeric: tabular-nums;
}

.msf-15__carhead i {
  font-style: normal;
  font-size: 11px;
  font-weight: 600;
  color: var(--mut);
}

.msf-15__car small {
  font-size: 12px;
  color: var(--mut);
}

.msf-15__chips {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 4px;
}

.msf-15__chips span {
  font-size: 10.5px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 99px;
  background: oklch(0.96 0.006 250);
  color: var(--mut);
}

.msf-15__car:hover {
  transform: translateY(-2px);
  border-color: color-mix(in oklab,var(--sky) 50%,var(--line));
}

.msf-15__car:has(:checked) {
  border-color: var(--sky);
  background: color-mix(in oklab,var(--sky) 6%,white);
  box-shadow: 0 10px 24px -14px var(--sky);
}

.msf-15__car:has(:focus-visible) {
  outline: 3px solid var(--sky);
  outline-offset: 2px;
}

.msf-15__addons {
  display: grid;
  gap: 10px;
}

.msf-15__toggle {
  position: relative;
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 14px;
  align-items: center;
  padding: 15px 18px;
  border: 2px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  transition: border-color .2s,background .2s;
}

.msf-15__toggle b {
  font-size: 14.5px;
  display: block;
}

.msf-15__toggle small {
  font-size: 12px;
  color: var(--mut);
}

.msf-15__price {
  font-size: 13px;
  font-weight: 800;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

.msf-15__toggle input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-15__switch {
  width: 44px;
  height: 26px;
  border-radius: 99px;
  background: var(--line);
  position: relative;
  transition: background .2s;
}

.msf-15__switch::after {
  content: "";
  position: absolute;
  left: 3px;
  top: 3px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 4px rgb(0 0 0/.3);
  transition: transform .2s cubic-bezier(.34,1.56,.64,1);
}

.msf-15__toggle:has(:checked) {
  border-color: var(--sky);
  background: color-mix(in oklab,var(--sky) 5%,white);
}

.msf-15__toggle:has(:checked) .msf-15__switch {
  background: var(--sky);
}

.msf-15__toggle:has(:checked) .msf-15__switch::after {
  transform: translateX(18px);
}

.msf-15__toggle:has(:checked) .msf-15__price {
  color: var(--sky);
}

.msf-15__toggle:has(:focus-visible) {
  outline: 3px solid var(--sky);
  outline-offset: 2px;
}

.msf-15__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 13px;
}

@media (max-width: 480px) {
  .msf-15__grid {
    grid-template-columns: 1fr;
  }
}

.msf-15__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--mut);
}

.msf-15__field input,
.msf-15__field select {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 11px 13px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-15__field :is(input,select):focus-visible {
  outline: none;
  border-color: var(--sky);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--sky) 14%,transparent);
}

.msf-15__field :is(input,select)[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
}

.msf-15__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.19 25);
  margin-top: 8px;
}

.msf-15__ticket {
  padding: 20px 22px;
  border-radius: 14px;
  background: oklch(0.97 0.008 250);
  border: 1.5px dashed color-mix(in oklab,var(--sky) 40%,var(--line));
  display: grid;
  gap: 8px;
  font-size: 14px;
}

.msf-15__ticket .msf-15__row {
  display: flex;
  justify-content: space-between;
  gap: 14px;
}

.msf-15__ticket .msf-15__row span:first-child {
  color: var(--mut);
  font-weight: 600;
}

.msf-15__ticket .msf-15__row span:last-child {
  font-weight: 700;
  text-align: right;
}

.msf-15__ticket .msf-15__row--total {
  border-top: 1.5px dashed var(--line);
  padding-top: 10px;
  font-size: 16px;
}

.msf-15__ticket .msf-15__row--total span:last-child {
  color: var(--sky);
}

.msf-15__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.msf-15__next,
.msf-15__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 999px;
  padding: 12px 24px;
  transition: transform .15s,filter .2s;
}

.msf-15__next {
  border: none;
  color: #fff;
  background: linear-gradient(100deg,var(--sky),var(--sun));
  box-shadow: 0 12px 28px -12px var(--sky);
}

.msf-15__next:hover {
  transform: translateY(-1px);
  filter: brightness(1.07);
}

.msf-15__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-15__back:hover {
  color: var(--ink);
}

.msf-15__next:focus-visible,
.msf-15__back:focus-visible {
  outline: 3px solid var(--sky);
  outline-offset: 2px;
}

.msf-15__done[hidden] {
  display: none;
}

.msf-15__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 34px 28px 14px;
}

.msf-15__done b {
  font-size: 34px;
  color: var(--sky);
  animation: msf-15-fly .7s cubic-bezier(.2,.8,.2,1);
}

.msf-15__done p {
  color: var(--mut);
  font-size: 14px;
}

.msf-15__bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 28px;
  border-top: 1px solid var(--line);
  background: oklch(0.975 0.006 250);
  font-size: 13px;
  color: var(--mut);
}

.msf-15__total {
  font-size: 19px;
  font-weight: 800;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

@keyframes msf-15-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-15-fly {
  from {
    transform: translate(-40px,20px) rotate(-20deg);
    opacity: 0;
  }

  to {
    transform: none;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-15 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-15'); if (!root) return;
  const form = root.querySelector('.msf-15__card');
  const steps = [...root.querySelectorAll('.msf-15__step')];
  const crumbs = [...root.querySelectorAll('.msf-15__crumbs li')];
  const total = root.querySelector('.msf-15__total');
  const DAYS = 4;
  let cur = 0;
  const fmt = n => '$' + n.toLocaleString('en-US');
  const price = () => {
    const car = root.querySelector('.msf-15__car:has(:checked)');
    let perDay = car ? +car.dataset.rate : 0;
    const addons = [...root.querySelectorAll('.msf-15__toggle:has(:checked)')];
    addons.forEach(a => perDay += +a.dataset.rate);
    return { perDay, sum: perDay * DAYS, car, addons };
  };
  const recalc = () => { total.textContent = fmt(price().sum); };
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-15__err').forEach(e => e.remove());
    const group = fs.querySelector('[role="radiogroup"]');
    if (group && !group.querySelector(':checked')) {
      const err = document.createElement('p'); err.className='msf-15__err'; err.setAttribute('role','alert');
      err.textContent = 'Pick a vehicle to continue.'; group.after(err); return false;
    }
    fs.querySelectorAll('input[required]:not([type="radio"]),select[required]').forEach(el => {
      const bad = !el.checkValidity(); el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-15__err'; err.setAttribute('role','alert');
        err.textContent = 'Please complete the highlighted fields.'; el.closest('.msf-15__grid').after(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    crumbs.forEach((c,k) => {
      c.classList.toggle('is-active',k===i); c.classList.toggle('is-done',k<i);
      k===i ? c.setAttribute('aria-current','step') : c.removeAttribute('aria-current');
    });
    if (i === steps.length-1) buildTicket();
    steps[i].querySelector('.msf-15__title').focus();
  };
  const buildTicket = () => {
    const d = new FormData(form), p = price();
    const rows = [
      ['Vehicle', d.get('car')],
      ['Protection', p.addons.length ? p.addons.map(a => a.querySelector('b').textContent).join(', ') : 'None'],
      ['Driver', d.get('driver') + ' \u00b7 ' + d.get('age')],
      ['Pickup', 'SFO Airport \u00b7 Jun 12, 10:00 AM'],
      ['Rate', fmt(p.perDay) + '/day \u00d7 ' + DAYS + ' days']];
    root.querySelector('.msf-15__ticket').innerHTML =
      rows.map(([k,v]) => '<div class="msf-15__row"><span>'+k+'</span><span>'+v+'</span></div>').join('') +
      '<div class="msf-15__row msf-15__row--total"><span>Total</span><span>'+fmt(p.sum)+'</span></div>';
  };
  root.addEventListener('change', recalc);
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-15__next:not(.msf-15__next--go):not(.msf-15__submit):not(.msf-15__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-15__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-15__next--go, .msf-15__submit, .msf-15__skip')) return;

    e.preventDefault();
    const d = new FormData(form);
    const code = 'DR-' + (d.get('driver')||'XX').split(' ').map(w => w[0]||'').join('').toUpperCase() + '-' + Math.floor(1000 + Math.random()*9000);
    steps.forEach(s => s.hidden = true);
    crumbs.forEach(c => { c.classList.add('is-done'); c.classList.remove('is-active'); });
    root.querySelector('.msf-15__donemsg').textContent = 'Confirmation ' + code + ' sent to ' + d.get('email') + '. Free cancellation until 24h before pickup.';
    const done = root.querySelector('.msf-15__done'); done.hidden = false; done.querySelector('h3').focus();
    });
  recalc();
})();
```
