---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/healthcare-and-medical-intake-form/"
title: "Healthcare & Medical Intake Form"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A calm, WCAG-first patient intake flow — Personal → Medical history → Emergency contact → Consent — with large touch targets, a typed-signature consent step,…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Healthcare & Medical Intake Form
Source: https://codefronts.com/components/css-multi-step-form/healthcare-and-medical-intake-form/

A calm, WCAG-first patient intake flow — Personal → Medical history → Emergency contact → Consent — with large touch targets, a typed-signature consent step, and 'None of these' logic on the history checklist. Healthcare forms serve the widest possible audience, so every pattern here is chosen for maximum accessibility.
## HTML
```html
<section class="msf-08" aria-label="Patient intake demo">
  <form class="msf-08__card" novalidate>
    <header class="msf-08__head">
      <div class="msf-08__id"><b>+</b><div><h3>Riverbend Family Clinic</h3><p>New patient intake · All information is confidential</p></div></div>
      <ol class="msf-08__list">
        <li class="is-active" aria-current="step"><i>1</i>Personal</li>
        <li><i>2</i>History</li>
        <li><i>3</i>Emergency</li>
        <li><i>4</i>Consent</li>
      </ol>
    </header>
    <fieldset class="msf-08__step">
      <legend class="msf-08__title" tabindex="-1">Personal information</legend>
      <div class="msf-08__grid">
        <label class="msf-08__field"><span>Legal full name</span><input type="text" name="name" id="msf-08-name" autocomplete="name" required placeholder="Jane Doe"></label>
        <label class="msf-08__field"><span>Date of birth</span><input type="date" name="dob" autocomplete="bday" required></label>
        <label class="msf-08__field"><span>Phone</span><input type="tel" name="phone" autocomplete="tel" required placeholder="(555) 123-4567"></label>
        <label class="msf-08__field"><span>Preferred pharmacy <em>(optional)</em></span><input type="text" name="pharmacy" placeholder="Walgreens on 5th Ave"></label>
      </div>
      <div class="msf-08__nav"><span></span><button type="button" class="msf-08__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-08__step" hidden>
      <legend class="msf-08__title" tabindex="-1">Medical history</legend>
      <p class="msf-08__help">Check everything that applies to you. If nothing applies, check the last option.</p>
      <div class="msf-08__checks" role="group" aria-label="Conditions">
        <label class="msf-08__check"><input type="checkbox" name="cond" value="High blood pressure"><span>High blood pressure</span></label>
        <label class="msf-08__check"><input type="checkbox" name="cond" value="Diabetes"><span>Diabetes</span></label>
        <label class="msf-08__check"><input type="checkbox" name="cond" value="Asthma or COPD"><span>Asthma or COPD</span></label>
        <label class="msf-08__check"><input type="checkbox" name="cond" value="Heart condition"><span>Heart condition</span></label>
        <label class="msf-08__check"><input type="checkbox" name="cond" value="Allergies to medication"><span>Allergies to medication</span></label>
        <label class="msf-08__check msf-08__check--none"><input type="checkbox" name="cond" value="None" data-none><span>None of these apply to me</span></label>
      </div>
      <label class="msf-08__field msf-08__field--gap"><span>Current medications <em>(optional)</em></span><textarea name="meds" rows="2" placeholder="Name and dose, e.g. Lisinopril 10mg daily"></textarea></label>
      <div class="msf-08__nav"><button type="button" class="msf-08__back">Back</button><button type="button" class="msf-08__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-08__step" hidden>
      <legend class="msf-08__title" tabindex="-1">Emergency contact</legend>
      <div class="msf-08__grid">
        <label class="msf-08__field"><span>Contact name</span><input type="text" name="ec-name" required placeholder="John Doe"></label>
        <label class="msf-08__field"><span>Relationship</span><select name="ec-rel" required><option value="">Select…</option><option>Spouse / partner</option><option>Parent</option><option>Child</option><option>Sibling</option><option>Friend</option></select></label>
        <label class="msf-08__field"><span>Contact phone</span><input type="tel" name="ec-phone" required placeholder="(555) 987-6543"></label>
      </div>
      <div class="msf-08__nav"><button type="button" class="msf-08__back">Back</button><button type="button" class="msf-08__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-08__step" hidden>
      <legend class="msf-08__title" tabindex="-1">Consent &amp; signature</legend>
      <div class="msf-08__consent"><p>I consent to treatment and confirm the information provided is accurate to the best of my knowledge. I understand my records are protected under HIPAA.</p></div>
      <div class="msf-08__grid">
        <label class="msf-08__field"><span>Type your legal name to sign</span><input type="text" name="sig" id="msf-08-sig" required placeholder="Jane Doe" autocomplete="off"></label>
        <label class="msf-08__field"><span>Date</span><input type="date" name="sigdate" id="msf-08-sigdate" required></label>
      </div>
      <p class="msf-08__sigpreview" aria-hidden="true"></p>
      <div class="msf-08__nav"><button type="button" class="msf-08__back">Back</button><button type="button" class="msf-08__next msf-08__next--go">Sign &amp; submit</button></div>
    </fieldset>
    <div class="msf-08__done" hidden><b>+</b><h3 tabindex="-1">You're checked in</h3><p>The front desk has your file. Please have a seat — we'll call you shortly.</p></div>
  </form>
</section>
```
## CSS
```css
.msf-08,
.msf-08 *,
.msf-08 *::before,
.msf-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-08 {
  width: 100%;
  min-height: 100vh;
  --med: oklch(0.48 0.09 220);
  --ink: oklch(0.22 0.02 230);
  --mut: oklch(0.45 0.02 230);
  --line: oklch(0.88 0.01 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 16px;
  color: var(--ink);
  padding: 48px 20px;
  background: oklch(0.96 0.008 210);
  display: grid;
  place-items: center;
}

.msf-08__card {
  width: min(660px,100%);
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 28px 32px 32px;
  box-shadow: 0 20px 50px -30px oklch(0.4 0.06 220/.45);
}

.msf-08__head {
  display: grid;
  gap: 20px;
  margin-bottom: 24px;
  padding-bottom: 22px;
  border-bottom: 2px solid var(--line);
}

.msf-08__id {
  display: flex;
  gap: 14px;
  align-items: center;
}

.msf-08__id b {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--med);
  color: #fff;
  font-size: 26px;
  font-weight: 400;
}

.msf-08__id h3 {
  font-size: 18px;
}

.msf-08__id p {
  font-size: 13px;
  color: var(--mut);
}

.msf-08__list {
  display: flex;
  gap: 6px;
  list-style: none;
  flex-wrap: wrap;
}

.msf-08__list li {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--mut);
  padding: 9px 14px;
  border-radius: 99px;
  background: oklch(0.955 0.008 210);
}

.msf-08__list li i {
  display: grid;
  place-items: center;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #fff;
  border: 2px solid var(--line);
  font-size: 11.5px;
  font-style: normal;
}

.msf-08__list li.is-active {
  background: color-mix(in oklab,var(--med) 12%,white);
  color: var(--med);
}

.msf-08__list li.is-active i {
  border-color: var(--med);
  color: var(--med);
}

.msf-08__list li.is-done i {
  background: var(--med);
  border-color: var(--med);
  color: #fff;
}

.msf-08__step {
  border: none;
}

.msf-08__step:not([hidden]) {
  animation: msf-08-in .3s ease;
}

.msf-08__title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 16px;
  outline: none;
}

.msf-08__help {
  font-size: 14px;
  color: var(--mut);
  margin-bottom: 14px;
}

.msf-08__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

@media (max-width: 540px) {
  .msf-08__grid {
    grid-template-columns: 1fr;
  }
}

.msf-08__field {
  display: grid;
  gap: 7px;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--mut);
}

.msf-08__field em {
  font-weight: 400;
  font-style: normal;
}

.msf-08__field--gap {
  margin-top: 16px;
}

.msf-08__field input,
.msf-08__field select,
.msf-08__field textarea {
  font: inherit;
  color: var(--ink);
  padding: 13px 14px;
  min-height: 48px;
  border: 2px solid var(--line);
  border-radius: 10px;
  resize: vertical;
  transition: border-color .2s,box-shadow .2s;
}

.msf-08__field :is(input,select,textarea):focus-visible {
  outline: none;
  border-color: var(--med);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--med) 18%,transparent);
}

.msf-08__field :is(input,select,textarea)[aria-invalid="true"] {
  border-color: oklch(0.5 0.19 25);
  background: oklch(0.5 0.19 25/.04);
}

.msf-08__err {
  grid-column: 1/-1;
  font-size: 14px;
  font-weight: 700;
  color: oklch(0.48 0.18 25);
}

.msf-08__checks {
  display: grid;
  gap: 8px;
}

.msf-08__check {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 16px;
  min-height: 48px;
  border: 2px solid var(--line);
  border-radius: 10px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
  transition: border-color .15s,background .15s;
}

.msf-08__check input {
  width: 20px;
  height: 20px;
  accent-color: var(--med);
  flex: none;
}

.msf-08__check:hover {
  border-color: color-mix(in oklab,var(--med) 40%,var(--line));
}

.msf-08__check:has(:checked) {
  border-color: var(--med);
  background: color-mix(in oklab,var(--med) 7%,white);
}

.msf-08__check:has(:focus-visible) {
  outline: 3px solid var(--med);
  outline-offset: 2px;
}

.msf-08__check--none {
  border-style: dashed;
}

.msf-08__consent {
  padding: 16px 18px;
  border: 2px solid var(--line);
  border-radius: 10px;
  background: oklch(0.97 0.006 210);
  font-size: 14px;
  line-height: 1.55;
  color: var(--mut);
  margin-bottom: 16px;
}

.msf-08__sigpreview {
  min-height: 34px;
  margin-top: 12px;
  font-family: 'Segoe Script','Brush Script MT',cursive;
  font-size: 24px;
  color: var(--med);
}

.msf-08__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-08__next,
.msf-08__back {
  font: inherit;
  font-weight: 700;
  cursor: pointer;
  border-radius: 10px;
  padding: 14px 28px;
  min-height: 48px;
  transition: background .2s,transform .15s;
}

.msf-08__next {
  border: none;
  color: #fff;
  background: var(--med);
}

.msf-08__next:hover {
  background: color-mix(in oklab,var(--med) 85%,black);
  transform: translateY(-1px);
}

.msf-08__next--go {
  background: oklch(0.5 0.14 155);
}

.msf-08__back {
  border: 2px solid var(--line);
  background: none;
  color: var(--ink);
}

.msf-08__back:hover {
  border-color: var(--med);
  color: var(--med);
}

.msf-08__next:focus-visible,
.msf-08__back:focus-visible {
  outline: 3px solid var(--med);
  outline-offset: 2px;
}

.msf-08__done[hidden] {
  display: none;
}

.msf-08__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 36px 0 14px;
}

.msf-08__done b {
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  border-radius: 14px;
  background: oklch(0.5 0.14 155);
  color: #fff;
  font-size: 28px;
  animation: msf-08-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-08__done p {
  color: var(--mut);
  font-size: 15px;
}

@keyframes msf-08-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes msf-08-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-08 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-08'); if (!root) return;
  const form = root.querySelector('.msf-08__card');
  const steps = [...root.querySelectorAll('.msf-08__step')];
  const tabs = [...root.querySelectorAll('.msf-08__list li')];
  let cur = 0;
  root.querySelector('#msf-08-sigdate').value = new Date().toISOString().slice(0,10);
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-08__err').forEach(e => e.remove());
    const checks = fs.querySelector('.msf-08__checks');
    if (checks && !checks.querySelector(':checked')) {
      const err = document.createElement('p'); err.className='msf-08__err'; err.setAttribute('role','alert');
      err.textContent = 'Please check at least one option (\u201cNone of these\u201d counts).';
      checks.after(err); return false;
    }
    fs.querySelectorAll('input[required],select[required]').forEach(el => {
      let bad = !el.checkValidity();
      if (el.id === 'msf-08-sig') {
        const name = root.querySelector('#msf-08-name').value;
        const norm = s => s.trim().toLowerCase().replace(/\s+/g,' ');
        if (norm(el.value) !== norm(name)) bad = true;
      }
      el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-08__err'; err.setAttribute('role','alert');
        err.textContent = el.id === 'msf-08-sig' && el.value
          ? 'Signature must match the legal name from step 1 (\u201c' + root.querySelector('#msf-08-name').value + '\u201d).'
          : 'Please complete the highlighted fields.';
        el.closest('.msf-08__grid').append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    tabs.forEach((t,k) => {
      t.classList.toggle('is-active',k===i); t.classList.toggle('is-done',k<i);
      t.querySelector('i').textContent = k<i ? '\u2713' : k+1;
      k===i ? t.setAttribute('aria-current','step') : t.removeAttribute('aria-current');
    });
    steps[i].querySelector('.msf-08__title').focus();
  };
  // exclusive "None of these" logic
  root.addEventListener('change', e => {
    if (!e.target.matches('.msf-08__checks input')) return;
    const boxes = [...root.querySelectorAll('.msf-08__checks input')];
    if (e.target.hasAttribute('data-none') && e.target.checked) boxes.forEach(b => { if (b !== e.target) b.checked = false; });
    else if (e.target.checked) boxes.find(b => b.hasAttribute('data-none')).checked = false;
  });
  // live signature preview
  const sig = root.querySelector('#msf-08-sig');
  sig.addEventListener('input', () => root.querySelector('.msf-08__sigpreview').textContent = sig.value);
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-08__next:not(.msf-08__next--go):not(.msf-08__submit):not(.msf-08__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-08__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-08__next--go, .msf-08__submit, .msf-08__skip')) return;

    e.preventDefault();
    if (!validate(steps[cur])) return;
    steps.forEach(s => s.hidden = true);
    tabs.forEach(t => { t.classList.add('is-done'); t.classList.remove('is-active'); t.querySelector('i').textContent='\u2713'; });
    const done = root.querySelector('.msf-08__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
