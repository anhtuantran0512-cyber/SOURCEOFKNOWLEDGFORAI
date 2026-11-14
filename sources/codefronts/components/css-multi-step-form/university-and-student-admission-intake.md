---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/university-and-student-admission-intake/"
title: "University & Student Admission Intake"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A collegiate admission portal flow — Applicant → Academics → Program → Documents — with a GPA field, program preference with live seat availability hints,…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: University & Student Admission Intake
Source: https://codefronts.com/components/css-multi-step-form/university-and-student-admission-intake/

A collegiate admission portal flow — Applicant → Academics → Program → Documents — with a GPA field, program preference with live seat availability hints, transcript upload, and a 'progress saved' affordance on every step. Styled with academic serif headings and a crest-like mark that feels institutional without being stuffy.
## HTML
```html
<section class="msf-12" aria-label="University admission demo">
  <form class="msf-12__card" novalidate>
    <header class="msf-12__head">
      <div class="msf-12__crest"><b>❖</b><div><h3>Alden State University</h3><p>Fall 2027 Undergraduate Application</p></div></div>
      <span class="msf-12__saved" aria-live="polite"></span>
    </header>
    <ol class="msf-12__tabs">
      <li class="is-active" aria-current="step">Applicant</li><li>Academics</li><li>Program</li><li>Documents</li>
    </ol>
    <fieldset class="msf-12__step">
      <h4 class="msf-12__title" tabindex="-1">Applicant information</h4>
      <div class="msf-12__grid">
        <label class="msf-12__field"><span>Full legal name</span><input type="text" name="name" autocomplete="name" required placeholder="Maya Okafor"></label>
        <label class="msf-12__field"><span>Email</span><input type="email" name="email" autocomplete="email" required placeholder="[email protected]"></label>
        <label class="msf-12__field"><span>Date of birth</span><input type="date" name="dob" autocomplete="bday" required></label>
        <label class="msf-12__field"><span>Citizenship</span><select name="citizen" required><option value="">Select…</option><option>U.S. citizen</option><option>Permanent resident</option><option>International</option></select></label>
      </div>
      <div class="msf-12__nav"><span></span><button type="button" class="msf-12__next">Save &amp; continue</button></div>
    </fieldset>
    <fieldset class="msf-12__step" hidden>
      <h4 class="msf-12__title" tabindex="-1">Academic background</h4>
      <div class="msf-12__grid">
        <label class="msf-12__field"><span>High school</span><input type="text" name="school" required placeholder="Lincoln High School"></label>
        <label class="msf-12__field"><span>Graduation year</span><select name="grad" required><option value="">Select…</option><option>2027</option><option>2026</option><option>2025</option><option>Earlier</option></select></label>
        <label class="msf-12__field"><span>GPA <em>(4.0 scale)</em></span><input type="number" name="gpa" id="msf-12-gpa" min="0" max="4" step="0.01" required placeholder="3.72"><small class="msf-12__gpahint" aria-live="polite"></small></label>
        <label class="msf-12__field"><span>SAT / ACT <em>(optional)</em></span><input type="text" name="test" placeholder="1380 SAT"></label>
      </div>
      <div class="msf-12__nav"><button type="button" class="msf-12__back">Back</button><button type="button" class="msf-12__next">Save &amp; continue</button></div>
    </fieldset>
    <fieldset class="msf-12__step" hidden>
      <h4 class="msf-12__title" tabindex="-1">Program preference</h4>
      <div class="msf-12__programs" role="radiogroup" aria-label="First-choice program">
        <label class="msf-12__prog" data-seats="14"><input type="radio" name="program" value="Computer Science" required><div><b>Computer Science, B.S.</b><small>College of Engineering</small></div><span class="msf-12__seats"></span></label>
        <label class="msf-12__prog" data-seats="52"><input type="radio" name="program" value="Business Administration"><div><b>Business Administration, B.B.A.</b><small>Alden School of Business</small></div><span class="msf-12__seats"></span></label>
        <label class="msf-12__prog" data-seats="8"><input type="radio" name="program" value="Nursing"><div><b>Nursing, B.S.N.</b><small>College of Health Sciences</small></div><span class="msf-12__seats"></span></label>
        <label class="msf-12__prog" data-seats="37"><input type="radio" name="program" value="Psychology"><div><b>Psychology, B.A.</b><small>College of Liberal Arts</small></div><span class="msf-12__seats"></span></label>
      </div>
      <div class="msf-12__nav"><button type="button" class="msf-12__back">Back</button><button type="button" class="msf-12__next">Save &amp; continue</button></div>
    </fieldset>
    <fieldset class="msf-12__step" hidden>
      <h4 class="msf-12__title" tabindex="-1">Upload your transcript</h4>
      <label class="msf-12__drop" id="msf-12-drop">
        <input type="file" id="msf-12-file" accept=".pdf" required>
        <b>📄 Drop your official transcript (PDF) or <u>browse</u></b>
        <small>One PDF · up to 10 MB · counselor-signed copies preferred</small>
      </label>
      <p class="msf-12__filestatus" role="status" aria-live="polite"></p>
      <div class="msf-12__nav"><button type="button" class="msf-12__back">Back</button><button type="button" class="msf-12__next msf-12__next--go">Submit application</button></div>
    </fieldset>
    <div class="msf-12__done" hidden><b>❖</b><h4 tabindex="-1">Application submitted</h4><p>Confirmation #ASU-27-88412. Decisions post March 15 on your portal.</p></div>
  </form>
</section>
```
## CSS
```css
.msf-12,
.msf-12 *,
.msf-12 *::before,
.msf-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-12 {
  width: 100%;
  min-height: 100vh;
  --navy: oklch(0.3 0.07 265);
  --crimson: oklch(0.5 0.17 20);
  --ink: oklch(0.25 0.02 265);
  --mut: oklch(0.5 0.02 265);
  --line: oklch(0.89 0.01 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: oklch(0.955 0.008 90);
  display: grid;
  place-items: center;
}

.msf-12__card {
  width: min(640px,100%);
  background: #fff;
  border: 1px solid var(--line);
  border-top: 5px solid var(--navy);
  border-radius: 12px;
  padding: 26px 32px 32px;
  box-shadow: 0 24px 60px -32px oklch(0.3 0.07 265/.45);
}

.msf-12__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  margin-bottom: 18px;
}

.msf-12__crest {
  display: flex;
  gap: 13px;
  align-items: center;
}

.msf-12__crest b {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--navy);
  color: oklch(0.85 0.08 90);
  font-size: 20px;
}

.msf-12__crest h3 {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 18px;
  color: var(--navy);
}

.msf-12__crest p {
  font-size: 12.5px;
  color: var(--mut);
}

.msf-12__saved {
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.14 155);
  opacity: 0;
  transition: opacity .3s;
}

.msf-12__saved.is-show {
  opacity: 1;
}

.msf-12__tabs {
  display: flex;
  list-style: none;
  border-bottom: 2px solid var(--line);
  margin-bottom: 22px;
}

.msf-12__tabs li {
  font-size: 13px;
  font-weight: 700;
  color: var(--mut);
  padding: 10px 16px;
  margin-bottom: -2px;
  border-bottom: 3px solid transparent;
  transition: color .2s,border-color .2s;
}

.msf-12__tabs li.is-active {
  color: var(--navy);
  border-bottom-color: var(--crimson);
}

.msf-12__tabs li.is-done {
  color: var(--navy);
}

.msf-12__tabs li.is-done::after {
  content: " ✓";
  color: oklch(0.5 0.14 155);
}

.msf-12__step {
  border: none;
}

.msf-12__step:not([hidden]) {
  animation: msf-12-in .3s ease;
}

.msf-12__title {
  font-family: Georgia,serif;
  font-size: 21px;
  font-weight: 600;
  color: var(--navy);
  margin-bottom: 16px;
  outline: none;
}

.msf-12__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

@media (max-width: 540px) {
  .msf-12__grid {
    grid-template-columns: 1fr;
  }
}

.msf-12__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--mut);
  align-content: start;
}

.msf-12__field em {
  font-weight: 400;
  font-style: normal;
}

.msf-12__field input,
.msf-12__field select {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 11px 13px;
  border: 1.5px solid var(--line);
  border-radius: 8px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-12__field :is(input,select):focus-visible {
  outline: none;
  border-color: var(--navy);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--navy) 13%,transparent);
}

.msf-12__field :is(input,select)[aria-invalid="true"] {
  border-color: var(--crimson);
}

.msf-12__gpahint {
  font-weight: 600;
  color: oklch(0.5 0.14 155);
  min-height: 16px;
}

.msf-12__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: var(--crimson);
}

.msf-12__programs {
  display: grid;
  gap: 9px;
}

.msf-12__prog {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  align-items: center;
  padding: 14px 16px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  cursor: pointer;
  transition: all .15s;
}

.msf-12__prog input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-12__prog b {
  font-size: 14.5px;
  display: block;
}

.msf-12__prog small {
  font-size: 12px;
  color: var(--mut);
}

.msf-12__prog:hover {
  border-color: var(--navy);
}

.msf-12__prog:has(:checked) {
  border-color: var(--navy);
  background: color-mix(in oklab,var(--navy) 5%,white);
  box-shadow: 0 0 0 1px var(--navy);
}

.msf-12__prog:has(:focus-visible) {
  outline: 3px solid var(--navy);
  outline-offset: 2px;
}

.msf-12__seats {
  font-size: 11px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 99px;
}

.msf-12__seats.is-low {
  background: color-mix(in oklab,var(--crimson) 12%,white);
  color: var(--crimson);
}

.msf-12__seats.is-ok {
  background: oklch(0.5 0.14 155/.12);
  color: oklch(0.45 0.13 155);
}

.msf-12__drop {
  display: grid;
  justify-items: center;
  gap: 6px;
  text-align: center;
  padding: 30px 20px;
  border: 2px dashed var(--line);
  border-radius: 12px;
  cursor: pointer;
  color: var(--mut);
  transition: border-color .2s,background .2s;
}

.msf-12__drop:hover,
.msf-12__drop.is-over {
  border-color: var(--navy);
  background: color-mix(in oklab,var(--navy) 4%,white);
}

.msf-12__drop:focus-within {
  outline: 3px solid var(--navy);
  outline-offset: 3px;
}

.msf-12__drop input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-12__drop b {
  font-size: 14.5px;
  color: var(--ink);
}

.msf-12__drop u {
  color: var(--navy);
}

.msf-12__drop small {
  font-size: 12px;
}

.msf-12__filestatus {
  min-height: 20px;
  margin-top: 10px;
  font-size: 13px;
  font-weight: 700;
}

.msf-12__filestatus.is-ok {
  color: oklch(0.5 0.14 155);
}

.msf-12__filestatus.is-bad {
  color: var(--crimson);
}

.msf-12__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-12__next,
.msf-12__back {
  font: inherit;
  font-weight: 700;
  cursor: pointer;
  border-radius: 8px;
  padding: 12px 24px;
  transition: background .2s,transform .15s;
}

.msf-12__next {
  border: none;
  color: #fff;
  background: var(--navy);
}

.msf-12__next:hover {
  background: color-mix(in oklab,var(--navy) 85%,black);
  transform: translateY(-1px);
}

.msf-12__next--go {
  background: var(--crimson);
}

.msf-12__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-12__back:hover {
  color: var(--navy);
  border-color: var(--navy);
}

.msf-12__next:focus-visible,
.msf-12__back:focus-visible {
  outline: 3px solid var(--crimson);
  outline-offset: 2px;
}

.msf-12__done[hidden] {
  display: none;
}

.msf-12__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 36px 0 12px;
}

.msf-12__done b {
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background: var(--navy);
  color: oklch(0.85 0.08 90);
  font-size: 24px;
  animation: msf-12-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-12__done h4 {
  font-family: Georgia,serif;
  font-size: 21px;
  color: var(--navy);
}

.msf-12__done p {
  color: var(--mut);
  font-size: 14px;
}

@keyframes msf-12-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-12-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-12 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-12'); if (!root) return;
  const form = root.querySelector('.msf-12__card');
  const steps = [...root.querySelectorAll('.msf-12__step')];
  const tabs = [...root.querySelectorAll('.msf-12__tabs li')];
  const saved = root.querySelector('.msf-12__saved');
  const file = root.querySelector('#msf-12-file'), drop = root.querySelector('#msf-12-drop'), status = root.querySelector('.msf-12__filestatus');
  let cur = 0, fileOk = false, saveTimer;
  // seat badges from data
  root.querySelectorAll('.msf-12__prog').forEach(p => {
    const s = +p.dataset.seats, b = p.querySelector('.msf-12__seats');
    b.textContent = s + ' seats left'; b.className = 'msf-12__seats ' + (s <= 15 ? 'is-low' : 'is-ok');
  });
  const saveDraft = () => { // point this at localStorage or your API in production
    saved.textContent = 'Draft saved \u2713'; saved.classList.add('is-show');
    clearTimeout(saveTimer); saveTimer = setTimeout(() => saved.classList.remove('is-show'), 2200);
  };
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-12__err').forEach(e => e.remove());
    const group = fs.querySelector('[role="radiogroup"]');
    if (group && !group.querySelector(':checked')) {
      const err = document.createElement('p'); err.className='msf-12__err'; err.setAttribute('role','alert');
      err.textContent = 'Select your first-choice program.'; group.after(err); return false;
    }
    if (fs.contains(file)) {
      if (!fileOk) { status.className='msf-12__filestatus is-bad'; status.textContent='Attach your transcript PDF to submit.'; file.focus(); return false; }
      return true;
    }
    fs.querySelectorAll('input[required],select[required]').forEach(el => {
      const bad = !el.checkValidity(); el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-12__err'; err.setAttribute('role','alert');
        err.textContent = el.name === 'gpa' ? 'GPA must be between 0.00 and 4.00.' : 'Please complete the highlighted fields.';
        el.closest('.msf-12__grid').append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    tabs.forEach((t,k) => {
      t.classList.toggle('is-active',k===i); t.classList.toggle('is-done',k<i);
      k===i ? t.setAttribute('aria-current','step') : t.removeAttribute('aria-current');
    });
    steps[i].querySelector('.msf-12__title').focus();
  };
  const gpa = root.querySelector('#msf-12-gpa'), hint = root.querySelector('.msf-12__gpahint');
  gpa.addEventListener('input', () => {
    const v = parseFloat(gpa.value);
    hint.textContent = !isNaN(v) && v >= 0 && v <= 4 ? (v >= 3.5 ? 'Strong \u2014 above our median admit.' : v >= 2.5 ? 'Within our typical admit range.' : 'Consider adding test scores.') : '';
  });
  const checkFile = () => {
    const f = file.files[0]; if (!f) return;
    if (!/\.pdf$/i.test(f.name)) { fileOk=false; status.className='msf-12__filestatus is-bad'; status.textContent='\u2715 Transcripts must be PDF.'; return; }
    if (f.size > 10*1048576) { fileOk=false; status.className='msf-12__filestatus is-bad'; status.textContent='\u2715 ' + f.name + ' is over 10 MB.'; return; }
    fileOk = true; status.className='msf-12__filestatus is-ok'; status.textContent='\u2713 ' + f.name + ' attached.';
  };
  file.addEventListener('change', checkFile);
  ['dragenter','dragover'].forEach(ev => drop.addEventListener(ev, e => { e.preventDefault(); drop.classList.add('is-over'); }));
  ['dragleave','drop'].forEach(ev => drop.addEventListener(ev, e => { e.preventDefault(); drop.classList.remove('is-over'); }));
  drop.addEventListener('drop', e => { if (e.dataTransfer.files.length) { file.files = e.dataTransfer.files; checkFile(); } });
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-12__next:not(.msf-12__next--go):not(.msf-12__submit):not(.msf-12__skip)')) { if (validate(steps[cur])) { saveDraft(); show(cur+1); } }
    if (e.target.closest('.msf-12__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-12__next--go, .msf-12__submit, .msf-12__skip')) return;

    e.preventDefault();
    if (!validate(steps[cur])) return;
    steps.forEach(s => s.hidden = true);
    tabs.forEach(t => { t.classList.add('is-done'); t.classList.remove('is-active'); });
    const done = root.querySelector('.msf-12__done'); done.hidden = false; done.querySelector('h4').focus();
    });
})();
```
