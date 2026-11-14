---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/b2b-lead-qualification-and-booking/"
title: "B2B Lead Qualification & Booking"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "An enterprise intake wizard in a crisp, utility-first visual style: company size and budget tier as segmented radio cards, a goals multi-select with checkbox…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: B2B Lead Qualification & Booking
Source: https://codefronts.com/components/css-multi-step-form/b2b-lead-qualification-and-booking/

An enterprise intake wizard in a crisp, utility-first visual style: company size and budget tier as segmented radio cards, a goals multi-select with checkbox chips, and a booking-style final step with time-slot pills. Qualifies the lead before it ever shows the calendar — exactly how agencies and B2B SaaS teams gate their sales time.
## HTML
```html
<section class="msf-06" aria-label="B2B lead qualification demo">
  <form class="msf-06__card" novalidate>
    <header class="msf-06__head">
      <div><p class="msf-06__kicker">Northwind Partners</p><h3 class="msf-06__h">Let's see if we're a fit</h3></div>
      <div class="msf-06__count"><span aria-live="polite">Step <b class="msf-06__n">1</b> of 4</span><div class="msf-06__bar"><i style="--w:.25"></i></div></div>
    </header>
    <fieldset class="msf-06__step">
      <legend class="msf-06__title" tabindex="-1">How big is your team?</legend>
      <div class="msf-06__segrow" role="radiogroup" aria-label="Company size">
        <label class="msf-06__seg"><input type="radio" name="size" value="1–10" required><span>1–10</span></label>
        <label class="msf-06__seg"><input type="radio" name="size" value="11–50"><span>11–50</span></label>
        <label class="msf-06__seg"><input type="radio" name="size" value="51–200"><span>51–200</span></label>
        <label class="msf-06__seg"><input type="radio" name="size" value="201–1000"><span>201–1k</span></label>
        <label class="msf-06__seg"><input type="radio" name="size" value="1000+"><span>1k+</span></label>
      </div>
      <div class="msf-06__nav"><span></span><button type="button" class="msf-06__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-06__step" hidden>
      <legend class="msf-06__title" tabindex="-1">What's your budget range?</legend>
      <div class="msf-06__tiers" role="radiogroup" aria-label="Budget tier">
        <label class="msf-06__tier"><input type="radio" name="budget" value="Under $10k" required><b>Under $10k</b><small>Starter engagement</small></label>
        <label class="msf-06__tier"><input type="radio" name="budget" value="$10k–$50k"><b>$10k–$50k</b><small>Most common</small></label>
        <label class="msf-06__tier"><input type="radio" name="budget" value="$50k+"><b>$50k+</b><small>Full partnership</small></label>
      </div>
      <div class="msf-06__nav"><button type="button" class="msf-06__back">Back</button><button type="button" class="msf-06__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-06__step" hidden>
      <legend class="msf-06__title" tabindex="-1">What should we focus on? <em>Pick any</em></legend>
      <div class="msf-06__chips" role="group" aria-label="Primary goals">
        <label class="msf-06__chip"><input type="checkbox" name="goal" value="More qualified leads"><span>More qualified leads</span></label>
        <label class="msf-06__chip"><input type="checkbox" name="goal" value="Rebrand / new site"><span>Rebrand / new site</span></label>
        <label class="msf-06__chip"><input type="checkbox" name="goal" value="Conversion optimization"><span>Conversion optimization</span></label>
        <label class="msf-06__chip"><input type="checkbox" name="goal" value="Product design"><span>Product design</span></label>
        <label class="msf-06__chip"><input type="checkbox" name="goal" value="SEO & content"><span>SEO &amp; content</span></label>
      </div>
      <div class="msf-06__nav"><button type="button" class="msf-06__back">Back</button><button type="button" class="msf-06__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-06__step" hidden>
      <legend class="msf-06__title" tabindex="-1">Book your strategy call</legend>
      <p class="msf-06__echo" aria-live="polite"></p>
      <div class="msf-06__grid">
        <label class="msf-06__field"><span>Work email</span><input type="email" name="email" autocomplete="email" required placeholder="[email protected]"></label>
        <label class="msf-06__field"><span>Company</span><input type="text" name="company" autocomplete="organization" required placeholder="Acme Inc."></label>
      </div>
      <p class="msf-06__slotlabel">Tomorrow's openings</p>
      <div class="msf-06__slots" role="radiogroup" aria-label="Call time">
        <label class="msf-06__slot"><input type="radio" name="slot" value="9:00 AM" required><span>9:00 AM</span></label>
        <label class="msf-06__slot"><input type="radio" name="slot" value="11:30 AM"><span>11:30 AM</span></label>
        <label class="msf-06__slot"><input type="radio" name="slot" value="2:00 PM"><span>2:00 PM</span></label>
        <label class="msf-06__slot"><input type="radio" name="slot" value="4:30 PM"><span>4:30 PM</span></label>
      </div>
      <div class="msf-06__nav"><button type="button" class="msf-06__back">Back</button><button type="button" class="msf-06__next msf-06__next--go">Confirm call</button></div>
    </fieldset>
    <div class="msf-06__done" hidden><b>✓</b><h3 tabindex="-1">Call booked</h3><p>Calendar invite sent. We'll come prepared with ideas for your goals.</p></div>
  </form>
</section>
```
## CSS
```css
.msf-06,
.msf-06 *,
.msf-06 *::before,
.msf-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-06 {
  width: 100%;
  min-height: 100vh;
  --indigo: oklch(0.5 0.19 275);
  --ink: oklch(0.28 0.02 275);
  --mut: oklch(0.55 0.02 275);
  --line: oklch(0.91 0.008 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: oklch(0.965 0.006 275);
  display: grid;
  place-items: center;
}

.msf-06__card {
  width: min(600px,100%);
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 26px 30px 30px;
  box-shadow: 0 1px 2px oklch(0.28 0.02 275/.06),0 20px 50px -30px oklch(0.28 0.02 275/.3);
}

.msf-06__head {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.msf-06__kicker {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--indigo);
}

.msf-06__h {
  font-size: 20px;
  letter-spacing: -.01em;
}

.msf-06__count {
  display: grid;
  justify-items: end;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
}

.msf-06__count b {
  color: var(--ink);
}

.msf-06__bar {
  width: 140px;
  height: 4px;
  border-radius: 99px;
  background: var(--line);
  overflow: hidden;
}

.msf-06__bar i {
  display: block;
  height: 100%;
  background: var(--indigo);
  transform: scaleX(var(--w));
  transform-origin: left;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.msf-06__step {
  border: none;
}

.msf-06__step:not([hidden]) {
  animation: msf-06-in .3s cubic-bezier(.2,.8,.2,1);
}

.msf-06__title {
  font-size: 17px;
  font-weight: 800;
  margin-bottom: 16px;
  outline: none;
}

.msf-06__title em {
  font-style: normal;
  font-weight: 500;
  font-size: 13px;
  color: var(--mut);
}

.msf-06__segrow {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  border: 1.5px solid var(--line);
  border-radius: 10px;
  overflow: hidden;
}

@media (max-width: 480px) {
  .msf-06__segrow {
    grid-template-columns: repeat(3,1fr);
  }
}

.msf-06__seg {
  position: relative;
  text-align: center;
  font-size: 13.5px;
  font-weight: 700;
  padding: 13px 6px;
  cursor: pointer;
  border-right: 1.5px solid var(--line);
  transition: background .15s,color .15s;
}

.msf-06__seg:last-child {
  border-right: none;
}

.msf-06__seg input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-06__seg:hover {
  background: oklch(0.97 0.006 275);
}

.msf-06__seg:has(:checked) {
  background: var(--indigo);
  color: #fff;
}

.msf-06__seg:has(:focus-visible) {
  outline: 3px solid var(--indigo);
  outline-offset: -3px;
  z-index: 1;
}

.msf-06__tiers {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
}

@media (max-width: 520px) {
  .msf-06__tiers {
    grid-template-columns: 1fr;
  }
}

.msf-06__tier {
  display: grid;
  gap: 3px;
  padding: 16px 14px;
  border: 1.5px solid var(--line);
  border-radius: 12px;
  cursor: pointer;
  transition: all .2s;
}

.msf-06__tier b {
  font-size: 15px;
}

.msf-06__tier small {
  font-size: 12px;
  color: var(--mut);
}

.msf-06__tier input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-06__tier:hover {
  border-color: color-mix(in oklab,var(--indigo) 45%,var(--line));
  transform: translateY(-1px);
}

.msf-06__tier:has(:checked) {
  border-color: var(--indigo);
  background: color-mix(in oklab,var(--indigo) 6%,white);
  box-shadow: 0 0 0 1px var(--indigo);
}

.msf-06__tier:has(:focus-visible) {
  outline: 3px solid var(--indigo);
  outline-offset: 2px;
}

.msf-06__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.msf-06__chip {
  position: relative;
  font-size: 13.5px;
  font-weight: 700;
  padding: 10px 16px;
  border: 1.5px solid var(--line);
  border-radius: 999px;
  cursor: pointer;
  transition: all .15s;
}

.msf-06__chip input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-06__chip:hover {
  border-color: color-mix(in oklab,var(--indigo) 45%,var(--line));
}

.msf-06__chip:has(:checked) {
  border-color: var(--indigo);
  background: var(--indigo);
  color: #fff;
}

.msf-06__chip:has(:checked) span::before {
  content: "✓ ";
}

.msf-06__chip:has(:focus-visible) {
  outline: 3px solid var(--indigo);
  outline-offset: 2px;
}

.msf-06__echo {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
  margin-bottom: 14px;
  padding: 10px 14px;
  background: oklch(0.97 0.006 275);
  border-radius: 8px;
}

.msf-06__echo b {
  color: var(--indigo);
}

.msf-06__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 16px;
}

@media (max-width: 480px) {
  .msf-06__grid {
    grid-template-columns: 1fr;
  }
}

.msf-06__field {
  display: grid;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
}

.msf-06__field input {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 10px 12px;
  border: 1.5px solid var(--line);
  border-radius: 8px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-06__field input:focus-visible {
  outline: none;
  border-color: var(--indigo);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--indigo) 15%,transparent);
}

.msf-06__field input[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
}

.msf-06__err {
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.19 25);
  margin-top: 10px;
}

.msf-06__slotlabel {
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
  margin-bottom: 8px;
}

.msf-06__slots {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.msf-06__slot {
  position: relative;
  font-size: 13.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  padding: 10px 18px;
  border: 1.5px solid var(--line);
  border-radius: 8px;
  cursor: pointer;
  transition: all .15s;
}

.msf-06__slot input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-06__slot:hover {
  border-color: var(--indigo);
}

.msf-06__slot:has(:checked) {
  border-color: var(--indigo);
  background: var(--indigo);
  color: #fff;
}

.msf-06__slot:has(:focus-visible) {
  outline: 3px solid var(--indigo);
  outline-offset: 2px;
}

.msf-06__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-06__next,
.msf-06__back {
  font: inherit;
  font-weight: 700;
  cursor: pointer;
  border-radius: 8px;
  padding: 11px 22px;
  transition: transform .15s,background .2s;
}

.msf-06__next {
  border: none;
  color: #fff;
  background: var(--ink);
}

.msf-06__next:hover {
  background: var(--indigo);
  transform: translateY(-1px);
}

.msf-06__next--go {
  background: var(--indigo);
}

.msf-06__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-06__back:hover {
  color: var(--ink);
  border-color: var(--mut);
}

.msf-06__next:focus-visible,
.msf-06__back:focus-visible {
  outline: 3px solid var(--indigo);
  outline-offset: 2px;
}

.msf-06__done[hidden] {
  display: none;
}

.msf-06__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 32px 0 10px;
}

.msf-06__done b {
  display: grid;
  place-items: center;
  width: 50px;
  height: 50px;
  border-radius: 12px;
  background: var(--indigo);
  color: #fff;
  font-size: 22px;
  animation: msf-06-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-06__done p {
  color: var(--mut);
  font-size: 14px;
}

@keyframes msf-06-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-06-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-06 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-06'); if (!root) return;
  const form = root.querySelector('.msf-06__card');
  const steps = [...root.querySelectorAll('.msf-06__step')];
  const n = root.querySelector('.msf-06__n'), bar = root.querySelector('.msf-06__bar i');
  let cur = 0;
  const validate = (fs) => {
    fs.querySelectorAll('.msf-06__err').forEach(e => e.remove());
    const group = fs.querySelector('[role="radiogroup"]');
    if (group && group.querySelector('[required]') && !group.querySelector(':checked')) {
      const err = document.createElement('p'); err.className='msf-06__err'; err.setAttribute('role','alert');
      err.textContent = 'Choose an option to continue.'; group.after(err); return false;
    }
    let ok = true;
    fs.querySelectorAll('input[required]:not([type="radio"])').forEach(el => {
      const bad = !el.checkValidity(); el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-06__err'; err.setAttribute('role','alert');
        err.textContent = 'Please complete the highlighted fields.'; el.closest('.msf-06__grid').after(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    n.textContent = i+1;
    bar.style.setProperty('--w', ((i+1)/steps.length).toFixed(2));
    if (i === steps.length-1) echo();
    steps[i].querySelector('.msf-06__title').focus();
  };
  const echo = () => {
    const d = new FormData(form);
    const goals = d.getAll('goal');
    root.querySelector('.msf-06__echo').innerHTML =
      'Routing you to the right strategist: <b>' + d.get('size') + ' team</b> \u00b7 <b>' + d.get('budget') + '</b>' +
      (goals.length ? ' \u00b7 focused on <b>' + goals.join(', ') + '</b>' : '');
  };
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-06__next:not(.msf-06__next--go):not(.msf-06__submit):not(.msf-06__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-06__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-06__next--go, .msf-06__submit, .msf-06__skip')) return;

    e.preventDefault();
    if (!validate(steps[cur])) return;
    steps.forEach(s => s.hidden = true);
    n.textContent = steps.length; bar.style.setProperty('--w','1');
    const done = root.querySelector('.msf-06__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
