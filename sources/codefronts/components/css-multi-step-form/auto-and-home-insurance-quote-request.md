---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/auto-and-home-insurance-quote-request/"
title: "Auto & Home Insurance Quote Request"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A high-converting insurance quote wizard that opens with the lowest-friction question possible — just a ZIP code — before asking for anything personal."
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Auto & Home Insurance Quote Request
Source: https://codefronts.com/components/css-multi-step-form/auto-and-home-insurance-quote-request/

A high-converting insurance quote wizard that opens with the lowest-friction question possible — just a ZIP code — before asking for anything personal. Features a segmented progress bar, one-question-per-screen pacing, and an auto-advance on choice selection that makes the form feel half as long as it is.
## HTML
```html
<section class="msf-05" aria-label="Insurance quote demo">
  <form class="msf-05__card" novalidate>
    <header class="msf-05__head">
      <span class="msf-05__logo">◈ SafeHarbor</span>
      <div class="msf-05__segs" role="progressbar" aria-label="Quote progress" aria-valuemin="1" aria-valuemax="4" aria-valuenow="1"><i class="is-on"></i><i></i><i></i><i></i></div>
    </header>
    <fieldset class="msf-05__step">
      <h3 class="msf-05__title" tabindex="-1">Let's find your rate.<br>Where do you live?</h3>
      <label class="msf-05__zip"><span>ZIP code</span><input type="text" name="zip" inputmode="numeric" autocomplete="postal-code" pattern="[0-9]{5}" required placeholder="90210" maxlength="5"></label>
      <div class="msf-05__nav"><span></span><button type="button" class="msf-05__next">See my options →</button></div>
    </fieldset>
    <fieldset class="msf-05__step" hidden>
      <h3 class="msf-05__title" tabindex="-1">What are we covering?</h3>
      <div class="msf-05__cards" role="radiogroup" aria-label="Coverage type">
        <label class="msf-05__opt" data-advance><input type="radio" name="cover" value="Auto" required><b>🚗</b><span>Auto</span><small>Car, truck or SUV</small></label>
        <label class="msf-05__opt" data-advance><input type="radio" name="cover" value="Home" required><b>🏡</b><span>Home</span><small>Own or renting</small></label>
        <label class="msf-05__opt" data-advance><input type="radio" name="cover" value="Bundle" required><b>✦</b><span>Bundle</span><small>Save up to 25%</small></label>
      </div>
      <div class="msf-05__nav"><button type="button" class="msf-05__back">← Back</button><button type="button" class="msf-05__next">Continue →</button></div>
    </fieldset>
    <fieldset class="msf-05__step" hidden>
      <h3 class="msf-05__title" tabindex="-1">Quick details</h3>
      <div class="msf-05__grid">
        <label class="msf-05__field"><span>Vehicle year</span><select name="vyear" required><option value="">Select…</option><option>2024–2026</option><option>2020–2023</option><option>2015–2019</option><option>Older than 2015</option></select></label>
        <label class="msf-05__field"><span>Current insurer</span><select name="insurer" required><option value="">Select…</option><option>Not insured yet</option><option>GEICO</option><option>State Farm</option><option>Progressive</option><option>Other</option></select></label>
      </div>
      <div class="msf-05__nav"><button type="button" class="msf-05__back">← Back</button><button type="button" class="msf-05__next">Almost done →</button></div>
    </fieldset>
    <fieldset class="msf-05__step" hidden>
      <h3 class="msf-05__title" tabindex="-1">Where should we send your quotes?</h3>
      <div class="msf-05__grid">
        <label class="msf-05__field"><span>Name</span><input type="text" name="name" autocomplete="name" required placeholder="Taylor Reed"></label>
        <label class="msf-05__field"><span>Email</span><input type="email" name="email" autocomplete="email" required placeholder="[email protected]"></label>
      </div>
      <div class="msf-05__nav"><button type="button" class="msf-05__back">← Back</button><button type="button" class="msf-05__next msf-05__next--go">Show my quotes</button></div>
    </fieldset>
    <div class="msf-05__done" hidden><b>◈</b><h3 tabindex="-1">3 quotes found</h3><p>Comparing carriers in your area — check your inbox in a minute.</p></div>
    <footer class="msf-05__trust">⏱ Takes 2 minutes &nbsp;·&nbsp; 🔒 No spam calls, ever</footer>
  </form>
</section>
```
## CSS
```css
.msf-05,
.msf-05 *,
.msf-05 *::before,
.msf-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-05 {
  width: 100%;
  min-height: 100vh;
  --teal: oklch(0.55 0.12 210);
  --ink: oklch(0.25 0.03 230);
  --line: oklch(0.9 0.01 210);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: linear-gradient(160deg,oklch(0.96 0.015 210),oklch(0.93 0.02 190));
  display: grid;
  place-items: center;
}

.msf-05__card {
  width: min(560px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 26px 30px;
  box-shadow: 0 30px 70px -35px oklch(0.45 0.1 210/.5);
}

.msf-05__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}

.msf-05__logo {
  font-weight: 800;
  color: var(--teal);
  letter-spacing: -.01em;
}

.msf-05__segs {
  display: flex;
  gap: 6px;
}

.msf-05__segs i {
  width: 34px;
  height: 6px;
  border-radius: 99px;
  background: var(--line);
  transition: background .3s;
}

.msf-05__segs i.is-on {
  background: var(--teal);
}

.msf-05__step {
  border: none;
}

.msf-05__step:not([hidden]) {
  animation: msf-05-in .35s cubic-bezier(.2,.8,.2,1);
}

.msf-05__title {
  font-size: 23px;
  letter-spacing: -.015em;
  line-height: 1.25;
  margin-bottom: 20px;
  outline: none;
}

.msf-05__zip {
  display: grid;
  gap: 7px;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.5 0.02 210);
  max-width: 220px;
}

.msf-05__zip input {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: .12em;
  color: var(--ink);
  padding: 12px 16px;
  border: 2px solid var(--line);
  border-radius: 12px;
  width: 100%;
  font-variant-numeric: tabular-nums;
  transition: border-color .2s,box-shadow .2s;
}

.msf-05__zip input:focus-visible {
  outline: none;
  border-color: var(--teal);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--teal) 15%,transparent);
}

.msf-05__zip input[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
}

.msf-05__cards {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
}

@media (max-width: 480px) {
  .msf-05__cards {
    grid-template-columns: 1fr;
  }
}

.msf-05__opt {
  display: grid;
  justify-items: center;
  gap: 4px;
  text-align: center;
  padding: 18px 12px;
  border: 2px solid var(--line);
  border-radius: 16px;
  cursor: pointer;
  transition: border-color .2s,background .2s,transform .15s,box-shadow .2s;
}

.msf-05__opt b {
  font-size: 26px;
}

.msf-05__opt span {
  font-size: 14px;
  font-weight: 800;
}

.msf-05__opt small {
  font-size: 11.5px;
  color: oklch(0.55 0.02 210);
}

.msf-05__opt input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-05__opt:hover {
  transform: translateY(-2px);
  border-color: color-mix(in oklab,var(--teal) 50%,var(--line));
}

.msf-05__opt:has(:checked) {
  border-color: var(--teal);
  background: color-mix(in oklab,var(--teal) 7%,white);
  box-shadow: 0 8px 20px -10px var(--teal);
}

.msf-05__opt:has(:focus-visible) {
  outline: 3px solid var(--teal);
  outline-offset: 2px;
}

.msf-05__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

@media (max-width: 480px) {
  .msf-05__grid {
    grid-template-columns: 1fr;
  }
}

.msf-05__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.5 0.02 210);
}

.msf-05__field input,
.msf-05__field select {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 11px 13px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-05__field :is(input,select):focus-visible {
  outline: none;
  border-color: var(--teal);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--teal) 15%,transparent);
}

.msf-05__field :is(input,select)[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
}

.msf-05__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.19 25);
}

.msf-05__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-05__next,
.msf-05__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 999px;
  padding: 13px 26px;
  transition: transform .15s,background .2s,color .2s;
}

.msf-05__next {
  border: none;
  color: #fff;
  background: var(--teal);
  box-shadow: 0 12px 26px -12px var(--teal);
}

.msf-05__next:hover {
  transform: translateY(-1px);
  background: color-mix(in oklab,var(--teal) 85%,black);
}

.msf-05__next--go {
  background: oklch(0.6 0.15 155);
}

.msf-05__back {
  border: none;
  background: none;
  color: oklch(0.5 0.02 210);
}

.msf-05__back:hover {
  color: var(--ink);
}

.msf-05__next:focus-visible,
.msf-05__back:focus-visible {
  outline: 3px solid var(--teal);
  outline-offset: 2px;
}

.msf-05__done[hidden] {
  display: none;
}

.msf-05__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 30px 0 10px;
}

.msf-05__done b {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: var(--teal);
  color: #fff;
  font-size: 22px;
  animation: msf-05-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-05__done p {
  color: oklch(0.5 0.02 210);
  font-size: 14px;
}

.msf-05__trust {
  margin-top: 22px;
  padding-top: 16px;
  border-top: 1px solid var(--line);
  text-align: center;
  font-size: 12px;
  color: oklch(0.55 0.02 210);
}

@keyframes msf-05-in {
  from {
    opacity: 0;
    transform: translateX(16px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-05-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-05 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-05'); if (!root) return;
  const form = root.querySelector('.msf-05__card');
  const steps = [...root.querySelectorAll('.msf-05__step')];
  const segsWrap = root.querySelector('.msf-05__segs');
  const segs = [...segsWrap.querySelectorAll('i')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let cur = 0;
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-05__err').forEach(e => e.remove());
    const radios = fs.querySelector('[role="radiogroup"]');
    if (radios && !fs.querySelector('input[type="radio"]:checked')) {
      const err = document.createElement('p'); err.className='msf-05__err'; err.setAttribute('role','alert');
      err.textContent = 'Pick an option to continue.'; radios.after(err); return false;
    }
    fs.querySelectorAll('input[required]:not([type="radio"]),select[required]').forEach(el => {
      const bad = !el.checkValidity();
      el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-05__err'; err.setAttribute('role','alert');
        err.textContent = el.name === 'zip' ? 'Enter a 5-digit ZIP code.' : 'Please complete the highlighted fields.';
        (el.closest('.msf-05__grid') || el.parentElement).append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    segs.forEach((sg,k) => sg.classList.toggle('is-on', k<=i));
    segsWrap.setAttribute('aria-valuenow', i+1);
    steps[i].querySelector('.msf-05__title').focus();
  };
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-05__next:not(.msf-05__next--go):not(.msf-05__submit):not(.msf-05__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-05__back')) show(cur-1);
    // auto-advance on card click (not keyboard cycling)
    const opt = e.target.closest('.msf-05__opt[data-advance]');
    if (opt && opt.querySelector('input').checked) {
      setTimeout(() => { if (steps[cur].contains(opt)) show(cur+1); }, reduce ? 0 : 320);
    }
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-05__next--go, .msf-05__submit, .msf-05__skip')) return;

    e.preventDefault();
    steps.forEach(s => s.hidden = true);
    segs.forEach(sg => sg.classList.add('is-on'));
    const done = root.querySelector('.msf-05__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
