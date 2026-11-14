---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/job-application-and-resume-upload-form/"
title: "Job Application & Resume Upload Form"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A 4-step careers-page application — Personal → Experience → Resume → Review — with an icon-based visual stepper, a drag-and-drop CV dropzone…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Job Application & Resume Upload Form
Source: https://codefronts.com/components/css-multi-step-form/job-application-and-resume-upload-form/

A 4-step careers-page application — Personal → Experience → Resume → Review — with an icon-based visual stepper, a drag-and-drop CV dropzone (keyboard-accessible, with file-type/size feedback), and a final review card. Editorial serif headings give it a human, non-corporate feel candidates trust.
## HTML
```html
<section class="msf-03" aria-label="Job application demo">
  <form class="msf-03__card" novalidate>
    <header class="msf-03__head">
      <p class="msf-03__kicker">Senior Product Designer · Remote</p>
      <ol class="msf-03__stepper" style="--progress:0">
        <li class="msf-03__dot is-active" aria-current="step"><i><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-6 8-6s8 2 8 6"/></svg></i><span>Personal</span></li>
        <li class="msf-03__dot"><i><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg></i><span>Experience</span></li>
        <li class="msf-03__dot"><i><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg></i><span>Resume</span></li>
        <li class="msf-03__dot"><i><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></i><span>Review</span></li>
      </ol>
    </header>
    <fieldset class="msf-03__step">
      <h3 class="msf-03__title" tabindex="-1">Tell us who you are</h3>
      <div class="msf-03__grid">
        <label class="msf-03__field"><span>Full name</span><input type="text" name="name" autocomplete="name" required placeholder="Riley Chen"></label>
        <label class="msf-03__field"><span>Email</span><input type="email" name="email" autocomplete="email" required placeholder="[email protected]"></label>
        <label class="msf-03__field msf-03__field--full"><span>Portfolio or LinkedIn <em>(optional)</em></span><input type="url" name="link" placeholder="https://…"></label>
      </div>
      <div class="msf-03__nav"><span></span><button type="button" class="msf-03__next">Next: Experience</button></div>
    </fieldset>
    <fieldset class="msf-03__step" hidden>
      <h3 class="msf-03__title" tabindex="-1">Your experience</h3>
      <div class="msf-03__grid">
        <label class="msf-03__field"><span>Current / last role</span><input type="text" name="role" required placeholder="Product Designer at Loom"></label>
        <label class="msf-03__field"><span>Years of experience</span><select name="years" required><option value="">Select…</option><option>0–2 years</option><option>3–5 years</option><option>6–9 years</option><option>10+ years</option></select></label>
        <label class="msf-03__field msf-03__field--full"><span>Why this role? <em>(2–3 sentences)</em></span><textarea name="pitch" rows="4" required placeholder="What draws you to this work…"></textarea></label>
      </div>
      <div class="msf-03__nav"><button type="button" class="msf-03__back">Back</button><button type="button" class="msf-03__next">Next: Resume</button></div>
    </fieldset>
    <fieldset class="msf-03__step" hidden>
      <h3 class="msf-03__title" tabindex="-1">Attach your resume</h3>
      <label class="msf-03__drop" id="msf-03-drop">
        <input type="file" name="cv" id="msf-03-file" accept=".pdf,.doc,.docx" required>
        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16V4m0 0 4 4m-4-4-4 4"/><path d="M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/></svg>
        <b>Drop your CV here or <u>browse</u></b>
        <small>PDF or Word · up to 5 MB</small>
      </label>
      <p class="msf-03__filestatus" id="msf-03-status" role="status" aria-live="polite"></p>
      <div class="msf-03__nav"><button type="button" class="msf-03__back">Back</button><button type="button" class="msf-03__next">Next: Review</button></div>
    </fieldset>
    <fieldset class="msf-03__step" hidden>
      <h3 class="msf-03__title" tabindex="-1">Review your application</h3>
      <dl class="msf-03__review"></dl>
      <div class="msf-03__nav"><button type="button" class="msf-03__back">Back</button><button type="button" class="msf-03__next msf-03__next--go">Submit application</button></div>
    </fieldset>
    <div class="msf-03__done" hidden><b>✓</b><h3 tabindex="-1">Application sent</h3><p>We read every application and reply within a week.</p></div>
  </form>
</section>
```
## CSS
```css
.msf-03,
.msf-03 *,
.msf-03 *::before,
.msf-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-03 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.24 0.02 60);
  --brand: oklch(0.5 0.13 40);
  --line: oklch(0.88 0.015 60);
  --paper: oklch(0.985 0.006 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: oklch(0.95 0.012 80);
  display: grid;
  place-items: center;
}

.msf-03__card {
  width: min(680px,100%);
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 30px 34px 34px;
  box-shadow: 0 30px 60px -35px oklch(0.4 0.08 40/.4);
}

.msf-03__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--brand);
  margin-bottom: 18px;
}

.msf-03__stepper {
  position: relative;
  display: flex;
  justify-content: space-between;
  list-style: none;
  margin-bottom: 28px;
}

.msf-03__stepper::before {
  content: "";
  position: absolute;
  left: 16px;
  right: 16px;
  top: 16px;
  height: 2px;
  background: var(--line);
}

.msf-03__stepper::after {
  content: "";
  position: absolute;
  left: 16px;
  right: 16px;
  top: 16px;
  height: 2px;
  background: var(--brand);
  transform: scaleX(var(--progress));
  transform-origin: left;
  transition: transform .45s cubic-bezier(.4,0,.2,1);
}

.msf-03__dot {
  position: relative;
  z-index: 1;
  display: grid;
  justify-items: center;
  gap: 7px;
  font-size: 11.5px;
  font-weight: 700;
  color: oklch(0.55 0.02 60);
}

.msf-03__dot i {
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--paper);
  border: 2px solid var(--line);
  color: oklch(0.55 0.02 60);
  transition: all .3s;
}

.msf-03__dot.is-active {
  color: var(--brand);
}

.msf-03__dot.is-active i {
  border-color: var(--brand);
  color: var(--brand);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--brand) 14%,transparent);
}

.msf-03__dot.is-done i {
  background: var(--brand);
  border-color: var(--brand);
  color: #fff;
}

.msf-03__step {
  border: none;
}

.msf-03__step:not([hidden]) {
  animation: msf-03-in .35s cubic-bezier(.2,.8,.2,1);
}

.msf-03__title {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 24px;
  font-weight: 600;
  letter-spacing: -.01em;
  margin-bottom: 18px;
  outline: none;
}

.msf-03__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

@media (max-width: 560px) {
  .msf-03__grid {
    grid-template-columns: 1fr;
  }
}

.msf-03__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.45 0.02 60);
}

.msf-03__field em {
  font-weight: 400;
  font-style: normal;
  color: oklch(0.6 0.02 60);
}

.msf-03__field--full {
  grid-column: 1/-1;
}

.msf-03__field input,
.msf-03__field select,
.msf-03__field textarea {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 11px 13px;
  background: #fff;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  resize: vertical;
  transition: border-color .2s,box-shadow .2s;
}

.msf-03__field :is(input,select,textarea):focus-visible {
  outline: none;
  border-color: var(--brand);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--brand) 13%,transparent);
}

.msf-03__field :is(input,select,textarea)[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
  box-shadow: 0 0 0 4px oklch(0.55 0.2 25/.1);
}

.msf-03__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.19 25);
}

.msf-03__drop {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 34px 20px;
  border: 2px dashed var(--line);
  border-radius: 14px;
  background: #fff;
  color: oklch(0.5 0.03 40);
  cursor: pointer;
  transition: border-color .2s,background .2s,transform .2s;
}

.msf-03__drop:hover,
.msf-03__drop.is-over {
  border-color: var(--brand);
  background: color-mix(in oklab,var(--brand) 5%,white);
}

.msf-03__drop.is-over {
  transform: scale(1.01);
}

.msf-03__drop:focus-within {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.msf-03__drop input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.msf-03__drop b {
  font-size: 15px;
  color: var(--ink);
}

.msf-03__drop u {
  color: var(--brand);
}

.msf-03__drop small {
  font-size: 12px;
}

.msf-03__filestatus {
  min-height: 20px;
  margin-top: 10px;
  font-size: 13px;
  font-weight: 700;
}

.msf-03__filestatus.is-ok {
  color: oklch(0.5 0.14 155);
}

.msf-03__filestatus.is-bad {
  color: oklch(0.5 0.19 25);
}

.msf-03__review {
  display: grid;
  gap: 10px;
  font-size: 14px;
}

.msf-03__review div {
  display: grid;
  grid-template-columns: 130px 1fr;
  gap: 12px;
  padding: 11px 14px;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 10px;
}

.msf-03__review dt {
  font-weight: 700;
  color: oklch(0.5 0.02 60);
}

.msf-03__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-03__next,
.msf-03__back {
  font: inherit;
  font-weight: 700;
  cursor: pointer;
  border-radius: 999px;
  padding: 12px 24px;
  transition: transform .15s,background .2s;
}

.msf-03__next {
  border: none;
  color: #fff;
  background: var(--ink);
}

.msf-03__next:hover {
  transform: translateY(-1px);
  background: var(--brand);
}

.msf-03__next--go {
  background: var(--brand);
}

.msf-03__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--ink);
}

.msf-03__back:hover {
  border-color: var(--ink);
}

.msf-03__next:focus-visible,
.msf-03__back:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 2px;
}

.msf-03__done[hidden] {
  display: none;
}

.msf-03__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 36px 0 16px;
}

.msf-03__done b {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: var(--brand);
  color: #fff;
  font-size: 22px;
  animation: msf-03-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-03__done h3 {
  font-family: Georgia,serif;
  font-size: 22px;
}

.msf-03__done p {
  color: oklch(0.5 0.02 60);
  font-size: 14px;
}

@keyframes msf-03-in {
  from {
    opacity: 0;
    transform: translateX(12px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-03-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-03 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-03'); if (!root) return;
  const form = root.querySelector('.msf-03__card');
  const steps = [...root.querySelectorAll('.msf-03__step')];
  const dots = [...root.querySelectorAll('.msf-03__dot')];
  const stepper = root.querySelector('.msf-03__stepper');
  const drop = root.querySelector('#msf-03-drop'), file = root.querySelector('#msf-03-file'), status = root.querySelector('#msf-03-status');
  const OK_EXT = ['pdf','doc','docx'], MAX_MB = 5;
  let cur = 0, fileOk = false;
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-03__err').forEach(e => e.remove());
    if (fs.contains(file)) {
      if (!fileOk) { status.className = 'msf-03__filestatus is-bad'; status.textContent = 'Please attach a PDF or Word resume (max ' + MAX_MB + ' MB).'; drop.querySelector('input').focus(); return false; }
      return true;
    }
    fs.querySelectorAll('input[required],select[required],textarea[required]').forEach(el => {
      const bad = !el.checkValidity();
      el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-03__err'; err.setAttribute('role','alert');
        err.textContent = el.type==='email' && el.value ? 'That email doesn\u2019t look right \u2014 check for typos.' : 'Please complete the highlighted fields.';
        el.closest('.msf-03__grid').append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    dots.forEach((d,k) => {
      d.classList.toggle('is-active',k===i); d.classList.toggle('is-done',k<i);
      k===i ? d.setAttribute('aria-current','step') : d.removeAttribute('aria-current');
    });
    stepper.style.setProperty('--progress',(i/(steps.length-1)).toFixed(2));
    if (i === steps.length-1) buildReview();
    steps[i].querySelector('.msf-03__title').focus();
  };
  const checkFile = () => {
    const f = file.files[0]; if (!f) return;
    const ext = f.name.split('.').pop().toLowerCase();
    if (!OK_EXT.includes(ext)) { fileOk=false; status.className='msf-03__filestatus is-bad'; status.textContent='\u2715 ' + f.name + ' \u2014 only PDF/DOC/DOCX accepted.'; return; }
    if (f.size > MAX_MB*1048576) { fileOk=false; status.className='msf-03__filestatus is-bad'; status.textContent='\u2715 ' + f.name + ' is over ' + MAX_MB + ' MB.'; return; }
    fileOk = true; status.className='msf-03__filestatus is-ok';
    status.textContent = '\u2713 ' + f.name + ' (' + (f.size/1048576).toFixed(1) + ' MB) attached.';
  };
  file.addEventListener('change', checkFile);
  ['dragenter','dragover'].forEach(ev => drop.addEventListener(ev, e => { e.preventDefault(); drop.classList.add('is-over'); }));
  ['dragleave','drop'].forEach(ev => drop.addEventListener(ev, e => { e.preventDefault(); drop.classList.remove('is-over'); }));
  drop.addEventListener('drop', e => { if (e.dataTransfer.files.length) { file.files = e.dataTransfer.files; checkFile(); } });
  const buildReview = () => {
    const d = new FormData(form);
    root.querySelector('.msf-03__review').innerHTML =
      [['Name', d.get('name')],['Email', d.get('email')],['Role', d.get('role') + ' \u00b7 ' + d.get('years')],
       ['Resume', file.files[0] ? file.files[0].name : '\u2014'],['Pitch', d.get('pitch')]]
      .map(([k,v]) => '<div><dt>'+k+'</dt><dd>'+v+'</dd></div>').join('');
  };
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-03__next:not(.msf-03__next--go):not(.msf-03__submit):not(.msf-03__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-03__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-03__next--go, .msf-03__submit, .msf-03__skip')) return;

    e.preventDefault();
    steps.forEach(s => s.hidden = true);
    dots.forEach(d => { d.classList.add('is-done'); d.classList.remove('is-active'); });
    stepper.style.setProperty('--progress','1');
    const done = root.querySelector('.msf-03__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
