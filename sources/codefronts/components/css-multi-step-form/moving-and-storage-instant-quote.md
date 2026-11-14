---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/moving-and-storage-instant-quote/"
title: "Moving & Storage Instant Quote"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A friendly home-services quote flow — Route → Home size → Date → Contact — with a From/To route visual that fills in live as you type, icon cards for home…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Moving & Storage Instant Quote
Source: https://codefronts.com/components/css-multi-step-form/moving-and-storage-instant-quote/

A friendly home-services quote flow — Route → Home size → Date → Contact — with a From/To route visual that fills in live as you type, icon cards for home size, and native date input with flexible-date toggle. Built to feel like the estimate is being assembled in front of you.
## HTML
```html
<section class="msf-11" aria-label="Moving quote demo">
  <form class="msf-11__card" novalidate>
    <header class="msf-11__head">
      <span class="msf-11__logo">🚚 BoxCar Moving Co.</span>
      <div class="msf-11__route" aria-hidden="true"><b class="msf-11__from">?????</b><i></i><b class="msf-11__to">?????</b></div>
    </header>
    <div class="msf-11__dots" role="progressbar" aria-label="Quote progress" aria-valuemin="1" aria-valuemax="4" aria-valuenow="1"><i class="is-on"></i><i></i><i></i><i></i></div>
    <fieldset class="msf-11__step">
      <h3 class="msf-11__title" tabindex="-1">Where's the move?</h3>
      <div class="msf-11__grid">
        <label class="msf-11__field"><span>Pickup ZIP</span><input type="text" name="from" id="msf-11-from" inputmode="numeric" pattern="[0-9]{5}" maxlength="5" required placeholder="78701" aria-label="Pickup ZIP code"></label>
        <label class="msf-11__field"><span>Destination ZIP</span><input type="text" name="to" id="msf-11-to" inputmode="numeric" pattern="[0-9]{5}" maxlength="5" required placeholder="30301" aria-label="Destination ZIP code"></label>
      </div>
      <div class="msf-11__nav"><span></span><button type="button" class="msf-11__next">Next: home size</button></div>
    </fieldset>
    <fieldset class="msf-11__step" hidden>
      <h3 class="msf-11__title" tabindex="-1">How big is the place?</h3>
      <div class="msf-11__cards" role="radiogroup" aria-label="Home size">
        <label class="msf-11__size"><input type="radio" name="size" value="Studio" required><b>🛋️</b><span>Studio</span><small>≤ 600 sq ft</small></label>
        <label class="msf-11__size"><input type="radio" name="size" value="1-bedroom"><b>🚪</b><span>1 bed</span><small>≤ 850 sq ft</small></label>
        <label class="msf-11__size"><input type="radio" name="size" value="2-bedroom"><b>🏠</b><span>2 bed</span><small>≤ 1,300 sq ft</small></label>
        <label class="msf-11__size"><input type="radio" name="size" value="3+ bedroom"><b>🏡</b><span>3+ bed</span><small>1,300+ sq ft</small></label>
      </div>
      <label class="msf-11__extra"><input type="checkbox" name="storage" value="yes"><span>I also need storage between moves</span></label>
      <div class="msf-11__nav"><button type="button" class="msf-11__back">Back</button><button type="button" class="msf-11__next">Next: date</button></div>
    </fieldset>
    <fieldset class="msf-11__step" hidden>
      <h3 class="msf-11__title" tabindex="-1">When do we roll?</h3>
      <div class="msf-11__grid">
        <label class="msf-11__field"><span>Moving date</span><input type="date" name="date" id="msf-11-date" required></label>
        <label class="msf-11__extra msf-11__extra--tall"><input type="checkbox" name="flex" value="yes"><span>I'm flexible ± 3 days<br><small>Flexible dates often cost 10–15% less</small></span></label>
      </div>
      <div class="msf-11__nav"><button type="button" class="msf-11__back">Back</button><button type="button" class="msf-11__next">Next: contact</button></div>
    </fieldset>
    <fieldset class="msf-11__step" hidden>
      <h3 class="msf-11__title" tabindex="-1">Your instant quote is ready</h3>
      <p class="msf-11__echo" aria-live="polite"></p>
      <div class="msf-11__grid">
        <label class="msf-11__field"><span>Name</span><input type="text" name="name" autocomplete="name" required placeholder="Chris Parker"></label>
        <label class="msf-11__field"><span>Phone or email</span><input type="text" name="contact" required placeholder="(555) 010-2288"></label>
      </div>
      <div class="msf-11__nav"><button type="button" class="msf-11__back">Back</button><button type="button" class="msf-11__next msf-11__next--go">Get my quote</button></div>
    </fieldset>
    <div class="msf-11__done" hidden><b>🚚</b><h3 tabindex="-1">Quote on its way!</h3><p>A moving specialist will text you a guaranteed price within the hour.</p></div>
  </form>
</section>
```
## CSS
```css
.msf-11,
.msf-11 *,
.msf-11 *::before,
.msf-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-11 {
  width: 100%;
  min-height: 100vh;
  --org: oklch(0.68 0.17 50);
  --ink: oklch(0.27 0.02 50);
  --mut: oklch(0.52 0.02 50);
  --line: oklch(0.89 0.012 50);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: oklch(0.955 0.015 75);
  display: grid;
  place-items: center;
}

.msf-11__card {
  width: min(580px,100%);
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 24px 28px 28px;
  box-shadow: 0 24px 60px -30px oklch(0.5 0.12 50/.45);
}

.msf-11__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.msf-11__logo {
  font-weight: 800;
  font-size: 15px;
}

.msf-11__route {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: ui-monospace,monospace;
  font-size: 13px;
  font-weight: 700;
}

.msf-11__route b {
  padding: 6px 10px;
  border-radius: 8px;
  background: oklch(0.96 0.01 50);
  border: 1.5px dashed var(--line);
  color: var(--mut);
  letter-spacing: .06em;
  transition: all .3s;
}

.msf-11__route b.is-set {
  background: color-mix(in oklab,var(--org) 12%,white);
  border-style: solid;
  border-color: var(--org);
  color: var(--ink);
}

.msf-11__route i {
  width: 44px;
  height: 2px;
  background: repeating-linear-gradient(90deg,var(--mut) 0 6px,transparent 6px 12px);
}

.msf-11__route.is-live i {
  background: repeating-linear-gradient(90deg,var(--org) 0 6px,transparent 6px 12px);
  animation: msf-11-dash 1s linear infinite;
}

.msf-11__dots {
  display: flex;
  gap: 6px;
  margin-bottom: 20px;
}

.msf-11__dots i {
  height: 6px;
  flex: 1;
  border-radius: 99px;
  background: var(--line);
  transition: background .3s;
}

.msf-11__dots i.is-on {
  background: var(--org);
}

.msf-11__step {
  border: none;
}

.msf-11__step:not([hidden]) {
  animation: msf-11-in .35s cubic-bezier(.2,.8,.2,1);
}

.msf-11__title {
  font-size: 21px;
  letter-spacing: -.01em;
  margin-bottom: 16px;
}

.msf-11__title:focus {
  outline: none;
}

.msf-11__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

@media (max-width: 480px) {
  .msf-11__grid {
    grid-template-columns: 1fr;
  }
}

.msf-11__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--mut);
}

.msf-11__field input {
  font: inherit;
  font-weight: 600;
  color: var(--ink);
  padding: 12px 14px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-11__field input:focus-visible {
  outline: none;
  border-color: var(--org);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--org) 16%,transparent);
}

.msf-11__field input[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
}

.msf-11__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.19 25);
}

.msf-11__cards {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 10px;
}

@media (max-width: 520px) {
  .msf-11__cards {
    grid-template-columns: repeat(2,1fr);
  }
}

.msf-11__size {
  display: grid;
  justify-items: center;
  gap: 3px;
  text-align: center;
  padding: 16px 8px;
  border: 2px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  transition: all .2s;
}

.msf-11__size b {
  font-size: 24px;
}

.msf-11__size span {
  font-size: 13.5px;
  font-weight: 800;
}

.msf-11__size small {
  font-size: 11px;
  color: var(--mut);
}

.msf-11__size input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-11__size:hover {
  transform: translateY(-2px);
  border-color: color-mix(in oklab,var(--org) 50%,var(--line));
}

.msf-11__size:has(:checked) {
  border-color: var(--org);
  background: color-mix(in oklab,var(--org) 8%,white);
  box-shadow: 0 8px 18px -10px var(--org);
}

.msf-11__size:has(:focus-visible) {
  outline: 3px solid var(--org);
  outline-offset: 2px;
}

.msf-11__extra {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  margin-top: 14px;
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  padding: 12px 14px;
  border: 1.5px dashed var(--line);
  border-radius: 10px;
  transition: border-color .2s,background .2s;
}

.msf-11__extra input {
  width: 18px;
  height: 18px;
  accent-color: var(--org);
  flex: none;
  margin-top: 1px;
}

.msf-11__extra small {
  font-weight: 500;
  color: var(--mut);
}

.msf-11__extra:has(:checked) {
  border-color: var(--org);
  border-style: solid;
  background: color-mix(in oklab,var(--org) 6%,white);
}

.msf-11__extra:has(:focus-visible) {
  outline: 3px solid var(--org);
  outline-offset: 2px;
}

.msf-11__extra--tall {
  margin-top: 0;
  align-self: end;
}

.msf-11__echo {
  margin-bottom: 14px;
  padding: 13px 16px;
  border-radius: 12px;
  background: color-mix(in oklab,var(--org) 10%,white);
  border: 1.5px solid color-mix(in oklab,var(--org) 35%,white);
  font-size: 14px;
  line-height: 1.5;
}

.msf-11__echo b {
  color: oklch(0.5 0.15 50);
}

.msf-11__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.msf-11__next,
.msf-11__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 999px;
  padding: 12px 24px;
  transition: transform .15s,background .2s;
}

.msf-11__next {
  border: none;
  color: #fff;
  background: var(--org);
  box-shadow: 0 12px 26px -12px var(--org);
}

.msf-11__next:hover {
  transform: translateY(-1px);
  background: color-mix(in oklab,var(--org) 85%,black);
}

.msf-11__next--go {
  background: oklch(0.55 0.15 155);
}

.msf-11__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-11__back:hover {
  color: var(--ink);
  border-color: var(--mut);
}

.msf-11__next:focus-visible,
.msf-11__back:focus-visible {
  outline: 3px solid var(--org);
  outline-offset: 2px;
}

.msf-11__done[hidden] {
  display: none;
}

.msf-11__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 32px 0 10px;
}

.msf-11__done b {
  font-size: 38px;
  animation: msf-11-drive .8s cubic-bezier(.2,.8,.2,1);
}

.msf-11__done p {
  color: var(--mut);
  font-size: 14px;
}

@keyframes msf-11-in {
  from {
    opacity: 0;
    transform: translateX(14px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-11-dash {
  to {
    background-position: 12px 0;
  }
}

@keyframes msf-11-drive {
  from {
    transform: translateX(-70px);
    opacity: 0;
  }

  to {
    transform: none;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-11 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-11'); if (!root) return;
  const form = root.querySelector('.msf-11__card');
  const steps = [...root.querySelectorAll('.msf-11__step')];
  const dots = [...root.querySelectorAll('.msf-11__dots i')];
  const dotsWrap = root.querySelector('.msf-11__dots');
  let cur = 0;
  root.querySelector('#msf-11-date').min = new Date().toISOString().slice(0,10);
  // live route strip
  const from = root.querySelector('#msf-11-from'), to = root.querySelector('#msf-11-to');
  const routeFrom = root.querySelector('.msf-11__from'), routeTo = root.querySelector('.msf-11__to'), route = root.querySelector('.msf-11__route');
  const syncRoute = () => {
    routeFrom.textContent = from.value || '?????'; routeTo.textContent = to.value || '?????';
    routeFrom.classList.toggle('is-set', from.value.length === 5);
    routeTo.classList.toggle('is-set', to.value.length === 5);
    route.classList.toggle('is-live', from.value.length === 5 && to.value.length === 5);
  };
  [from, to].forEach(i => i.addEventListener('input', syncRoute));
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-11__err').forEach(e => e.remove());
    const group = fs.querySelector('[role="radiogroup"]');
    if (group && !group.querySelector(':checked')) {
      const err = document.createElement('p'); err.className='msf-11__err'; err.setAttribute('role','alert');
      err.textContent = 'Pick your home size to continue.'; group.after(err); return false;
    }
    fs.querySelectorAll('input[required]').forEach(el => {
      const bad = !el.checkValidity(); el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-11__err'; err.setAttribute('role','alert');
        err.textContent = el.type === 'date' ? 'Pick a moving date (today or later).' : el.pattern ? 'ZIP codes are 5 digits.' : 'Please complete the highlighted fields.';
        (el.closest('.msf-11__grid') || el.parentElement).append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    dots.forEach((d,k) => d.classList.toggle('is-on', k<=i));
    dotsWrap.setAttribute('aria-valuenow', i+1);
    if (i === steps.length-1) {
      const d = new FormData(form);
      const date = d.get('date') ? new Date(d.get('date')+'T12:00').toLocaleDateString('en-US',{month:'long',day:'numeric'}) : '';
      root.querySelector('.msf-11__echo').innerHTML =
        'Moving a <b>' + d.get('size') + '</b> from <b>' + d.get('from') + '</b> to <b>' + d.get('to') + '</b> on <b>' + date + '</b>' +
        (d.get('flex') ? ' <b>(flexible)</b>' : '') + (d.get('storage') ? ' \u00b7 with storage' : '') + '.';
    }
    steps[i].querySelector('.msf-11__title').focus();
  };
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-11__next:not(.msf-11__next--go):not(.msf-11__submit):not(.msf-11__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-11__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-11__next--go, .msf-11__submit, .msf-11__skip')) return;

    e.preventDefault();
    if (!validate(steps[cur])) return;
    steps.forEach(s => s.hidden = true);
    dots.forEach(d => d.classList.add('is-on'));
    const done = root.querySelector('.msf-11__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
