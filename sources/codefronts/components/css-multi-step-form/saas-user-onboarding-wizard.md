---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/saas-user-onboarding-wizard/"
title: "SaaS User Onboarding Wizard"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A dark, product-grade onboarding wizard with a vertical sidebar stepper — Account → Workspace → Invite your team — the pattern used by modern SaaS tools."
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS User Onboarding Wizard
Source: https://codefronts.com/components/css-multi-step-form/saas-user-onboarding-wizard/

A dark, product-grade onboarding wizard with a vertical sidebar stepper — Account → Workspace → Invite your team — the pattern used by modern SaaS tools. Includes email-chip team invites, a live workspace-URL preview, and per-step completion ticks in the rail.
## HTML
```html
<section class="msf-02" aria-label="SaaS onboarding demo">
  <form class="msf-02__card" novalidate>
    <aside class="msf-02__rail">
      <span class="msf-02__logo">▲ northbeam</span>
      <ol class="msf-02__vsteps" style="--vprogress:0">
        <li class="msf-02__vstep is-active" aria-current="step"><i></i><div><b>Your account</b><small>Name and role</small></div></li>
        <li class="msf-02__vstep"><i></i><div><b>Workspace</b><small>Name your HQ</small></div></li>
        <li class="msf-02__vstep"><i></i><div><b>Invite the team</b><small>Better together</small></div></li>
      </ol>
      <p class="msf-02__hint">Setup takes about a minute. You can change everything later.</p>
    </aside>
    <div class="msf-02__main">
      <fieldset class="msf-02__step">
        <h3 class="msf-02__title" tabindex="-1">Welcome! First, about you</h3>
        <label class="msf-02__field"><span>Full name</span><input type="text" name="fullname" autocomplete="name" required placeholder="Sam Rivera"></label>
        <label class="msf-02__field"><span>What best describes your role?</span>
          <select name="role" required><option value="">Choose one…</option><option>Engineering</option><option>Design</option><option>Product</option><option>Marketing</option><option>Founder / Exec</option></select></label>
        <div class="msf-02__nav"><span></span><button type="button" class="msf-02__next">Continue →</button></div>
      </fieldset>
      <fieldset class="msf-02__step" hidden>
        <h3 class="msf-02__title" tabindex="-1">Name your workspace</h3>
        <label class="msf-02__field"><span>Company or team name</span><input type="text" name="company" id="msf-02-company" required placeholder="Acme Labs"></label>
        <p class="msf-02__url">Your workspace URL&ensp;<b id="msf-02-url">acme-labs<span>.northbeam.io</span></b></p>
        <div class="msf-02__nav"><button type="button" class="msf-02__back">← Back</button><button type="button" class="msf-02__next">Continue →</button></div>
      </fieldset>
      <fieldset class="msf-02__step" hidden>
        <h3 class="msf-02__title" tabindex="-1">Invite your teammates</h3>
        <div class="msf-02__chipbox" id="msf-02-chipbox">
          <ul class="msf-02__chips" id="msf-02-chips" aria-label="Pending invites"></ul>
          <input type="email" id="msf-02-email" placeholder="[email protected] — press Enter" aria-describedby="msf-02-chiphelp">
        </div>
        <p class="msf-02__help" id="msf-02-chiphelp">Type an email and press <kbd>Enter</kbd>. We'll send invites when you finish.</p>
        <div class="msf-02__nav"><button type="button" class="msf-02__back">← Back</button><div class="msf-02__navr"><button type="button" class="msf-02__skip">Skip for now</button><button type="button" class="msf-02__next msf-02__next--go">Launch workspace ✦</button></div></div>
      </fieldset>
      <div class="msf-02__done" hidden><b>✦</b><h3 tabindex="-1">You're in!</h3><p>Your workspace is ready and invites are on the way.</p></div>
    </div>
  </form>
</section>
```
## CSS
```css
.msf-02,
.msf-02 *,
.msf-02 *::before,
.msf-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-02 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.75 0.16 165);
  --bg: oklch(0.17 0.015 260);
  --panel: oklch(0.21 0.018 260);
  --line: oklch(0.32 0.02 260);
  --txt: oklch(0.93 0.005 260);
  --mut: oklch(0.65 0.015 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--txt);
  padding: 48px 20px;
  background: radial-gradient(100% 140% at 80% 0%,oklch(0.24 0.04 200),var(--bg) 55%);
  display: grid;
  place-items: center;
}

.msf-02__card {
  width: min(820px,100%);
  display: grid;
  grid-template-columns: 280px 1fr;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 40px 80px -40px rgb(0 0 0/.6);
}

@media (max-width: 700px) {
  .msf-02__card {
    grid-template-columns: 1fr;
  }

  .msf-02__rail {
    border-right: none;
    border-bottom: 1px solid var(--line);
  }
}

.msf-02__rail {
  padding: 28px 24px;
  border-right: 1px solid var(--line);
  background: color-mix(in oklab,var(--panel) 70%,black);
  display: grid;
  gap: 28px;
  align-content: start;
}

.msf-02__logo {
  font-weight: 800;
  letter-spacing: -.01em;
}

.msf-02__vsteps {
  position: relative;
  list-style: none;
  display: grid;
  gap: 26px;
}

.msf-02__vsteps::before {
  content: "";
  position: absolute;
  left: 11px;
  top: 12px;
  bottom: 12px;
  width: 2px;
  background: var(--line);
}

.msf-02__vsteps::after {
  content: "";
  position: absolute;
  left: 11px;
  top: 12px;
  bottom: 12px;
  width: 2px;
  background: var(--accent);
  transform: scaleY(var(--vprogress));
  transform-origin: top;
  transition: transform .45s cubic-bezier(.4,0,.2,1);
}

.msf-02__vstep {
  position: relative;
  z-index: 1;
  display: flex;
  gap: 14px;
  align-items: flex-start;
  color: var(--mut);
}

.msf-02__vstep i {
  flex: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 2px solid var(--line);
  background: var(--panel);
  display: grid;
  place-items: center;
  font-size: 12px;
  font-style: normal;
  transition: all .3s;
}

.msf-02__vstep b {
  display: block;
  font-size: 14px;
  color: var(--txt);
}

.msf-02__vstep small {
  font-size: 12px;
}

.msf-02__vstep.is-active i {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 20%,transparent);
}

.msf-02__vstep.is-active b {
  color: var(--accent);
}

.msf-02__vstep.is-done i {
  background: var(--accent);
  border-color: var(--accent);
  color: oklch(0.2 0.02 260);
}

.msf-02__vstep.is-done i::before {
  content: "✓";
  font-weight: 800;
}

.msf-02__hint {
  font-size: 12px;
  color: var(--mut);
  line-height: 1.5;
}

.msf-02__main {
  padding: 32px;
}

.msf-02__step[hidden] {
  display: none;
}

.msf-02__step {
  border: none;
  display: grid;
  gap: 16px;
}

.msf-02__step:not([hidden]) {
  animation: msf-02-in .35s cubic-bezier(.2,.8,.2,1);
}

.msf-02__title {
  font-size: 21px;
  letter-spacing: -.01em;
  outline: none;
}

.msf-02__field {
  display: grid;
  gap: 7px;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
}

.msf-02__field input,
.msf-02__field select {
  font: inherit;
  font-weight: 500;
  color: var(--txt);
  padding: 12px 14px;
  background: oklch(0.16 0.015 260);
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-02__field input:focus-visible,
.msf-02__field select:focus-visible,
.msf-02__chipbox:focus-within {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 16%,transparent);
}

.msf-02__field input[aria-invalid="true"],
.msf-02__field select[aria-invalid="true"] {
  border-color: oklch(0.6 0.19 25);
}

.msf-02__err {
  font-size: 12px;
  font-weight: 600;
  color: oklch(0.72 0.16 25);
}

.msf-02__url {
  font-size: 13px;
  color: var(--mut);
}

.msf-02__url b {
  color: var(--accent);
  font-family: ui-monospace,monospace;
}

.msf-02__url b span {
  color: var(--mut);
}

.msf-02__chipbox {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 10px;
  background: oklch(0.16 0.015 260);
  border: 1.5px solid var(--line);
  border-radius: 12px;
}

.msf-02__chips {
  display: contents;
  list-style: none;
}

.msf-02__chips li {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  padding: 6px 8px 6px 12px;
  border-radius: 999px;
  background: color-mix(in oklab,var(--accent) 18%,transparent);
  color: var(--accent);
  animation: msf-02-in .25s;
}

.msf-02__chips button {
  border: none;
  cursor: pointer;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: color-mix(in oklab,var(--accent) 30%,transparent);
  color: var(--accent);
  font-size: 11px;
  line-height: 1;
}

.msf-02__chips button:hover {
  background: var(--accent);
  color: oklch(0.2 0.02 260);
}

.msf-02__chipbox input {
  flex: 1;
  min-width: 220px;
  font: inherit;
  color: var(--txt);
  background: none;
  border: none;
  outline: none;
  padding: 6px;
}

.msf-02__help {
  font-size: 12px;
  color: var(--mut);
}

.msf-02__help kbd {
  font-family: ui-monospace,monospace;
  padding: 1px 5px;
  border: 1px solid var(--line);
  border-radius: 4px;
  font-size: 11px;
}

.msf-02__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-top: 8px;
}

.msf-02__navr {
  display: flex;
  gap: 10px;
  align-items: center;
}

.msf-02__next,
.msf-02__back,
.msf-02__skip {
  font: inherit;
  font-weight: 700;
  cursor: pointer;
  border-radius: 10px;
  padding: 12px 20px;
  transition: transform .15s,background .2s,color .2s;
}

.msf-02__next {
  border: none;
  color: oklch(0.2 0.02 260);
  background: var(--accent);
  box-shadow: 0 12px 28px -12px var(--accent);
}

.msf-02__next:hover {
  transform: translateY(-1px);
}

.msf-02__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-02__back:hover {
  color: var(--txt);
  border-color: var(--mut);
}

.msf-02__skip {
  border: none;
  background: none;
  color: var(--mut);
  text-decoration: underline;
  padding: 12px 6px;
}

.msf-02__skip:hover {
  color: var(--txt);
}

.msf-02__next:focus-visible,
.msf-02__back:focus-visible,
.msf-02__skip:focus-visible,
.msf-02__chips button:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.msf-02__done[hidden] {
  display: none;
}

.msf-02__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 40px 0;
}

.msf-02__done b {
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  border-radius: 16px;
  background: var(--accent);
  color: oklch(0.2 0.02 260);
  font-size: 24px;
  animation: msf-02-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-02__done p {
  color: var(--mut);
  font-size: 14px;
}

@keyframes msf-02-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-02-pop {
  from {
    transform: scale(.4) rotate(-20deg);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-02 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-02'); if (!root) return;
  const steps = [...root.querySelectorAll('.msf-02__step')];
  const rail = [...root.querySelectorAll('.msf-02__vstep')];
  const vsteps = root.querySelector('.msf-02__vsteps');
  let cur = 0;
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-02__err').forEach(e => e.remove());
    fs.querySelectorAll('input[required],select[required]').forEach(el => {
      const bad = !el.checkValidity();
      el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-02__err'; err.setAttribute('role','alert');
        err.textContent = 'This field is required to continue.';
        el.closest('.msf-02__field').append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k !== i);
    rail.forEach((d,k) => {
      d.classList.toggle('is-active', k===i); d.classList.toggle('is-done', k<i);
      d.querySelector('i').textContent = k<i ? '' : k+1;
      k===i ? d.setAttribute('aria-current','step') : d.removeAttribute('aria-current');
    });
    vsteps.style.setProperty('--vprogress', (i/(steps.length-1)).toFixed(2));
    steps[i].querySelector('.msf-02__title').focus();
  };
  rail.forEach((d,k) => d.querySelector('i').textContent = k+1);
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-02__next:not(.msf-02__next--go):not(.msf-02__submit):not(.msf-02__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-02__back')) show(cur-1);
  });
  // live workspace URL preview
  const company = root.querySelector('#msf-02-company'), url = root.querySelector('#msf-02-url');
  company.addEventListener('input', () => {
    const slug = company.value.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/(^-|-$)/g,'') || 'your-team';
    url.innerHTML = slug + '<span>.northbeam.io</span>';
  });
  // email chip input
  const email = root.querySelector('#msf-02-email'), chips = root.querySelector('#msf-02-chips');
  const addChip = () => {
    const v = email.value.trim().replace(/,$/,'');
    if (!v) return;
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) { email.setAttribute('aria-invalid','true'); return; }
    email.removeAttribute('aria-invalid');
    const li = document.createElement('li');
    li.innerHTML = v + ' <button type="button" aria-label="Remove ' + v + '">✕</button>';
    li.querySelector('button').addEventListener('click', () => li.remove());
    chips.append(li); email.value = '';
  };
  email.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ',') { e.preventDefault(); addChip(); } });
  email.addEventListener('blur', addChip);
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-02__next--go, .msf-02__submit, .msf-02__skip')) return;

    e.preventDefault();
    steps.forEach(s => s.hidden = true);
    rail.forEach(d => { d.classList.add('is-done'); d.classList.remove('is-active'); d.querySelector('i').textContent=''; });
    vsteps.style.setProperty('--vprogress','1');
    const done = root.querySelector('.msf-02__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
