---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/contractor-and-home-improvement-booking/"
title: "Contractor & Home Improvement Booking"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A local-services booking wizard — Service → Scope → Urgency → Contact — built around big icon-card selection at every step, the pattern that makes…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Contractor & Home Improvement Booking
Source: https://codefronts.com/components/css-multi-step-form/contractor-and-home-improvement-booking/

A local-services booking wizard — Service → Scope → Urgency → Contact — built around big icon-card selection at every step, the pattern that makes trade-services forms tappable with a thumb from a job site. Includes an urgency selector that reorders the promise copy ('today' vs 'this week') on the final step.
## HTML
```html
<section class="msf-13" aria-label="Contractor booking demo">
  <form class="msf-13__card" novalidate>
    <header class="msf-13__head">
      <span class="msf-13__logo"><b>⚒</b> TrueNorth Home Services</span>
      <span class="msf-13__stars" aria-label="Rated 4.9 out of 5">★★★★★ <i>4.9 · 2,300 jobs</i></span>
    </header>
    <div class="msf-13__bar"><i style="--w:.25"></i></div>
    <fieldset class="msf-13__step">
      <h3 class="msf-13__title" tabindex="-1">What needs fixing?</h3>
      <div class="msf-13__cards" role="radiogroup" aria-label="Service type">
        <label class="msf-13__opt"><input type="radio" name="service" value="HVAC" required><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><rect x="3" y="5" width="18" height="9" rx="2"/><path d="M7 17c0 1.5-1 2-1 2m6-2c0 1.5-1 2-1 2m6-2c0 1.5-1 2-1 2M7 9.5h10"/></svg><span>HVAC</span></label>
        <label class="msf-13__opt"><input type="radio" name="service" value="Plumbing"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v6m0 0c-3 0-5 2-5 5v1h10v-1c0-3-2-5-5-5Z"/><path d="M5 18h14M9 15v-1m6 1v-1"/></svg><span>Plumbing</span></label>
        <label class="msf-13__opt"><input type="radio" name="service" value="Roofing"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m3 12 9-8 9 8"/><path d="M5.5 10v9h13v-9"/></svg><span>Roofing</span></label>
        <label class="msf-13__opt"><input type="radio" name="service" value="Electrical"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6l1-8Z"/></svg><span>Electrical</span></label>
      </div>
      <div class="msf-13__nav"><span></span><button type="button" class="msf-13__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-13__step" hidden>
      <h3 class="msf-13__title" tabindex="-1">What's the scope?</h3>
      <div class="msf-13__scopes" role="radiogroup" aria-label="Project scope">
        <div class="msf-13__scopeset" data-for="HVAC"><label class="msf-13__row"><input type="radio" name="scope-HVAC" value="No cooling / heating"><span>No cooling or heating at all</span></label><label class="msf-13__row"><input type="radio" name="scope-HVAC" value="Weak airflow / noise"><span>Weak airflow or strange noise</span></label><label class="msf-13__row"><input type="radio" name="scope-HVAC" value="New system install"><span>New system install or replacement</span></label></div>
        <div class="msf-13__scopeset" data-for="Plumbing" hidden><label class="msf-13__row"><input type="radio" name="scope-Plumbing" value="Active leak"><span>Active leak or burst pipe</span></label><label class="msf-13__row"><input type="radio" name="scope-Plumbing" value="Clog / drainage"><span>Clog or slow drainage</span></label><label class="msf-13__row"><input type="radio" name="scope-Plumbing" value="Fixture install"><span>Fixture install or remodel</span></label></div>
        <div class="msf-13__scopeset" data-for="Roofing" hidden><label class="msf-13__row"><input type="radio" name="scope-Roofing" value="Active leak"><span>Active leak — water coming in</span></label><label class="msf-13__row"><input type="radio" name="scope-Roofing" value="Storm damage"><span>Storm damage / missing shingles</span></label><label class="msf-13__row"><input type="radio" name="scope-Roofing" value="Full replacement"><span>Full roof replacement quote</span></label></div>
        <div class="msf-13__scopeset" data-for="Electrical" hidden><label class="msf-13__row"><input type="radio" name="scope-Electrical" value="Outage / sparks"><span>Partial outage, sparks or burning smell</span></label><label class="msf-13__row"><input type="radio" name="scope-Electrical" value="Panel upgrade"><span>Panel upgrade / EV charger</span></label><label class="msf-13__row"><input type="radio" name="scope-Electrical" value="New wiring"><span>New wiring or fixtures</span></label></div>
      </div>
      <div class="msf-13__nav"><button type="button" class="msf-13__back">Back</button><button type="button" class="msf-13__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-13__step" hidden>
      <h3 class="msf-13__title" tabindex="-1">How soon?</h3>
      <div class="msf-13__cards msf-13__cards--3" role="radiogroup" aria-label="Urgency">
        <label class="msf-13__opt"><input type="radio" name="when" value="today" required><b>🔥</b><span>Today</span><small>Emergency dispatch</small></label>
        <label class="msf-13__opt"><input type="radio" name="when" value="this week"><b>📅</b><span>This week</span><small>Next opening</small></label>
        <label class="msf-13__opt"><input type="radio" name="when" value="just planning"><b>📐</b><span>Planning</span><small>Quote only</small></label>
      </div>
      <div class="msf-13__nav"><button type="button" class="msf-13__back">Back</button><button type="button" class="msf-13__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-13__step" hidden>
      <h3 class="msf-13__title" tabindex="-1">Where do we send the pro?</h3>
      <p class="msf-13__echo" aria-live="polite"></p>
      <div class="msf-13__grid">
        <label class="msf-13__field"><span>Name</span><input type="text" name="name" autocomplete="name" required placeholder="Pat Sullivan"></label>
        <label class="msf-13__field"><span>Phone</span><input type="tel" name="phone" autocomplete="tel" required placeholder="(555) 010-4477"></label>
        <label class="msf-13__field msf-13__field--full"><span>Street address</span><input type="text" name="addr" autocomplete="street-address" required placeholder="14 Cedar Lane"></label>
      </div>
      <div class="msf-13__nav"><button type="button" class="msf-13__back">Back</button><button type="button" class="msf-13__next msf-13__next--go">Book my pro</button></div>
    </fieldset>
    <div class="msf-13__done" hidden><b>⚒</b><h3 tabindex="-1">You're booked</h3><p class="msf-13__donemsg"></p></div>
  </form>
</section>
```
## CSS
```css
.msf-13,
.msf-13 *,
.msf-13 *::before,
.msf-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-13 {
  width: 100%;
  min-height: 100vh;
  --work: oklch(0.75 0.15 85);
  --ink: oklch(0.24 0.015 260);
  --mut: oklch(0.5 0.015 260);
  --line: oklch(0.89 0.008 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: oklch(0.28 0.02 260);
  display: grid;
  place-items: center;
}

.msf-13__card {
  width: min(580px,100%);
  background: #fff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 40px 80px -40px rgb(0 0 0/.7);
}

.msf-13__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  padding: 18px 26px;
  background: var(--ink);
  color: #fff;
}

.msf-13__logo {
  font-weight: 800;
  font-size: 15px;
  display: flex;
  gap: 9px;
  align-items: center;
}

.msf-13__logo b {
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: var(--work);
  color: var(--ink);
  font-size: 16px;
}

.msf-13__stars {
  font-size: 12px;
  color: var(--work);
}

.msf-13__stars i {
  font-style: normal;
  color: oklch(0.75 0.01 260);
}

.msf-13__bar {
  height: 4px;
  background: var(--line);
}

.msf-13__bar i {
  display: block;
  height: 100%;
  background: var(--work);
  transform: scaleX(var(--w));
  transform-origin: left;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.msf-13__step {
  border: none;
  padding: 24px 26px 28px;
}

.msf-13__step:not([hidden]) {
  animation: msf-13-in .3s cubic-bezier(.2,.8,.2,1);
}

.msf-13__title {
  font-size: 21px;
  letter-spacing: -.01em;
  margin-bottom: 16px;
  outline: none;
}

.msf-13__cards {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 10px;
}

.msf-13__cards--3 {
  grid-template-columns: repeat(3,1fr);
}

@media (max-width: 520px) {
  .msf-13__cards {
    grid-template-columns: repeat(2,1fr);
  }

  .msf-13__cards--3 {
    grid-template-columns: 1fr;
  }
}

.msf-13__opt {
  display: grid;
  justify-items: center;
  gap: 5px;
  text-align: center;
  padding: 18px 10px;
  border: 2px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  color: var(--mut);
  transition: all .18s;
}

.msf-13__opt b {
  font-size: 22px;
}

.msf-13__opt svg {
  color: var(--ink);
}

.msf-13__opt span {
  font-size: 13.5px;
  font-weight: 800;
  color: var(--ink);
}

.msf-13__opt small {
  font-size: 11px;
}

.msf-13__opt input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-13__opt:hover {
  transform: translateY(-2px);
  border-color: color-mix(in oklab,var(--work) 65%,var(--line));
}

.msf-13__opt:has(:checked) {
  border-color: oklch(0.6 0.13 85);
  background: color-mix(in oklab,var(--work) 14%,white);
  box-shadow: 0 8px 20px -12px oklch(0.6 0.13 85);
}

.msf-13__opt:has(:focus-visible) {
  outline: 3px solid oklch(0.6 0.13 85);
  outline-offset: 2px;
}

.msf-13__scopes {
  display: grid;
}

.msf-13__scopeset {
  display: grid;
  gap: 9px;
}

.msf-13__row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  min-height: 48px;
  border: 2px solid var(--line);
  border-radius: 12px;
  cursor: pointer;
  font-size: 14.5px;
  font-weight: 600;
  transition: all .15s;
}

.msf-13__row input {
  width: 18px;
  height: 18px;
  accent-color: oklch(0.55 0.12 85);
  flex: none;
}

.msf-13__row:hover {
  border-color: color-mix(in oklab,var(--work) 65%,var(--line));
}

.msf-13__row:has(:checked) {
  border-color: oklch(0.6 0.13 85);
  background: color-mix(in oklab,var(--work) 10%,white);
}

.msf-13__row:has(:focus-visible) {
  outline: 3px solid oklch(0.6 0.13 85);
  outline-offset: 2px;
}

.msf-13__echo {
  margin-bottom: 14px;
  padding: 12px 15px;
  border-radius: 10px;
  background: color-mix(in oklab,var(--work) 14%,white);
  border: 1.5px solid color-mix(in oklab,var(--work) 45%,white);
  font-size: 13.5px;
  font-weight: 600;
}

.msf-13__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 13px;
}

@media (max-width: 480px) {
  .msf-13__grid {
    grid-template-columns: 1fr;
  }
}

.msf-13__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--mut);
}

.msf-13__field--full {
  grid-column: 1/-1;
}

.msf-13__field input {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 12px 13px;
  min-height: 46px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-13__field input:focus-visible {
  outline: none;
  border-color: oklch(0.6 0.13 85);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--work) 30%,transparent);
}

.msf-13__field input[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
}

.msf-13__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.19 25);
  margin-top: 8px;
}

.msf-13__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.msf-13__next,
.msf-13__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 10px;
  padding: 13px 26px;
  min-height: 48px;
  transition: transform .15s,background .2s;
}

.msf-13__next {
  border: none;
  color: var(--ink);
  background: var(--work);
  box-shadow: 0 12px 26px -12px oklch(0.6 0.13 85);
}

.msf-13__next:hover {
  transform: translateY(-1px);
  background: color-mix(in oklab,var(--work) 85%,white);
}

.msf-13__next--go {
  background: var(--ink);
  color: #fff;
}

.msf-13__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-13__back:hover {
  color: var(--ink);
  border-color: var(--mut);
}

.msf-13__next:focus-visible,
.msf-13__back:focus-visible {
  outline: 3px solid oklch(0.6 0.13 85);
  outline-offset: 2px;
}

.msf-13__done[hidden] {
  display: none;
}

.msf-13__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 36px 26px;
}

.msf-13__done b {
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  border-radius: 14px;
  background: var(--work);
  color: var(--ink);
  font-size: 24px;
  animation: msf-13-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-13__done p {
  color: var(--mut);
  font-size: 14px;
}

@keyframes msf-13-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-13-pop {
  from {
    transform: scale(.4) rotate(-15deg);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-13 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-13'); if (!root) return;
  const form = root.querySelector('.msf-13__card');
  const steps = [...root.querySelectorAll('.msf-13__step')];
  const bar = root.querySelector('.msf-13__bar i');
  let cur = 0;
  // branch: show only the scope set for the chosen service
  root.addEventListener('change', e => {
    if (!e.target.matches('[name="service"]')) return;
    root.querySelectorAll('.msf-13__scopeset').forEach(set => {
      const on = set.dataset.for === e.target.value;
      set.hidden = !on;
      if (!on) set.querySelectorAll('input').forEach(r => r.checked = false); // clear stale branch
    });
  });
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-13__err').forEach(e => e.remove());
    const group = fs.querySelector('[role="radiogroup"]');
    if (group && ![...group.querySelectorAll('input')].some(r => r.checked && !r.closest('[hidden]'))) {
      const err = document.createElement('p'); err.className='msf-13__err'; err.setAttribute('role','alert');
      err.textContent = 'Pick an option to continue.'; group.after(err); return false;
    }
    fs.querySelectorAll('input[required]:not([type="radio"])').forEach(el => {
      const bad = !el.checkValidity(); el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-13__err'; err.setAttribute('role','alert');
        err.textContent = 'Please complete the highlighted fields.'; el.closest('.msf-13__grid').after(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    bar.style.setProperty('--w', ((i+1)/steps.length).toFixed(2));
    if (i === steps.length-1) {
      const d = new FormData(form);
      root.querySelector('.msf-13__echo').textContent =
        'A ' + (d.get('service')||'').toLowerCase() + ' pro will call you ' + (d.get('when')==='just planning' ? 'to schedule a free quote' : d.get('when')) + '.';
    }
    steps[i].querySelector('.msf-13__title').focus();
  };
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-13__next:not(.msf-13__next--go):not(.msf-13__submit):not(.msf-13__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-13__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-13__next--go, .msf-13__submit, .msf-13__skip')) return;

    e.preventDefault();
    if (!validate(steps[cur])) return;
    const d = new FormData(form);
    steps.forEach(s => s.hidden = true);
    bar.style.setProperty('--w','1');
    root.querySelector('.msf-13__donemsg').textContent =
      'Your ' + (d.get('service')||'').toLowerCase() + ' pro calls ' + d.get('phone') + ' ' + (d.get('when')==='just planning' ? 'within 24h' : d.get('when')) + '. Job #TN-8841.';
    const done = root.querySelector('.msf-13__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
