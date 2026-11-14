---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/multi-step-survey-and-feedback-questionnaire/"
title: "Multi-Step Survey & Feedback Questionnaire"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A one-question-per-screen micro-survey with buttery slide transitions, a 0–10 NPS scale, star-free satisfaction faces drawn in pure CSS-friendly SVG, and a…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Step Survey & Feedback Questionnaire
Source: https://codefronts.com/components/css-multi-step-form/multi-step-survey-and-feedback-questionnaire/

A one-question-per-screen micro-survey with buttery slide transitions, a 0–10 NPS scale, star-free satisfaction faces drawn in pure CSS-friendly SVG, and a keyboard flow where number keys answer the NPS question directly. The pacing pattern (Typeform-style) that gets survey completion rates over 80%.
## HTML
```html
<section class="msf-09" aria-label="Feedback survey demo">
  <form class="msf-09__card" novalidate>
    <div class="msf-09__topbar"><i style="--w:0"></i></div>
    <p class="msf-09__count" aria-live="polite">Question 1 of 4</p>
    <div class="msf-09__stage">
      <section class="msf-09__q is-current" data-q>
        <h3 class="msf-09__title" tabindex="-1">How was your experience with us today?</h3>
        <div class="msf-09__faces" role="radiogroup" aria-label="Experience rating">
          <label class="msf-09__face"><input type="radio" name="mood" value="Poor" data-advance><svg viewBox="0 0 48 48" width="44" height="44" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="17" cy="20" r="2.5" fill="currentColor"/><circle cx="31" cy="20" r="2.5" fill="currentColor"/><path d="M16 33q8-6 16 0" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg><span>Poor</span></label>
          <label class="msf-09__face"><input type="radio" name="mood" value="Okay" data-advance><svg viewBox="0 0 48 48" width="44" height="44" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="17" cy="20" r="2.5" fill="currentColor"/><circle cx="31" cy="20" r="2.5" fill="currentColor"/><path d="M16 31h16" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg><span>Okay</span></label>
          <label class="msf-09__face"><input type="radio" name="mood" value="Great" data-advance><svg viewBox="0 0 48 48" width="44" height="44" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="17" cy="20" r="2.5" fill="currentColor"/><circle cx="31" cy="20" r="2.5" fill="currentColor"/><path d="M16 29q8 8 16 0" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg><span>Great</span></label>
        </div>
      </section>
      <section class="msf-09__q" data-q hidden>
        <h3 class="msf-09__title" tabindex="-1">How likely are you to recommend us?</h3>
        <p class="msf-09__hint">0 = not at all · 10 = absolutely. Tip: just press a number key.</p>
        <div class="msf-09__nps" role="radiogroup" aria-label="0 to 10 recommendation score">
          <label><input type="radio" name="nps" value="0" data-advance><span>0</span></label><label><input type="radio" name="nps" value="1" data-advance><span>1</span></label><label><input type="radio" name="nps" value="2" data-advance><span>2</span></label><label><input type="radio" name="nps" value="3" data-advance><span>3</span></label><label><input type="radio" name="nps" value="4" data-advance><span>4</span></label><label><input type="radio" name="nps" value="5" data-advance><span>5</span></label><label><input type="radio" name="nps" value="6" data-advance><span>6</span></label><label><input type="radio" name="nps" value="7" data-advance><span>7</span></label><label><input type="radio" name="nps" value="8" data-advance><span>8</span></label><label><input type="radio" name="nps" value="9" data-advance><span>9</span></label><label><input type="radio" name="nps" value="10" data-advance><span>10</span></label>
        </div>
      </section>
      <section class="msf-09__q" data-q hidden>
        <h3 class="msf-09__title" tabindex="-1">What mattered most to you?</h3>
        <div class="msf-09__opts" role="radiogroup" aria-label="What mattered most">
          <label class="msf-09__opt"><input type="radio" name="why" value="Speed" data-advance><span>Speed — it was fast</span></label>
          <label class="msf-09__opt"><input type="radio" name="why" value="Quality" data-advance><span>Quality of the result</span></label>
          <label class="msf-09__opt"><input type="radio" name="why" value="Support" data-advance><span>The people who helped me</span></label>
          <label class="msf-09__opt"><input type="radio" name="why" value="Price" data-advance><span>Price and value</span></label>
        </div>
      </section>
      <section class="msf-09__q" data-q hidden>
        <h3 class="msf-09__title" tabindex="-1">Anything we should know? <em>(optional)</em></h3>
        <textarea class="msf-09__text" name="note" rows="4" maxlength="280" placeholder="Tell us in your own words…" aria-describedby="msf-09-counter"></textarea>
        <p class="msf-09__counter" id="msf-09-counter" aria-live="polite">0 / 280</p>
        <button type="button" class="msf-09__submit">Send feedback ↵</button>
      </section>
      <section class="msf-09__q msf-09__thanks" hidden><b>✳</b><h3 tabindex="-1">Thank you!</h3><p>Your feedback goes straight to the team.</p></section>
    </div>
    <footer class="msf-09__foot"><button type="button" class="msf-09__back" hidden>← Previous</button><span class="msf-09__brand">pulse·check</span></footer>
  </form>
</section>
```
## CSS
```css
.msf-09,
.msf-09 *,
.msf-09 *::before,
.msf-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-09 {
  width: 100%;
  min-height: 100vh;
  --vio: oklch(0.58 0.2 300);
  --ink: oklch(0.26 0.03 300);
  --mut: oklch(0.55 0.03 300);
  --line: oklch(0.9 0.015 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: linear-gradient(150deg,oklch(0.96 0.02 320),oklch(0.94 0.025 280));
  display: grid;
  place-items: center;
}

.msf-09__card {
  width: min(560px,100%);
  background: #fff;
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 30px 80px -35px oklch(0.45 0.15 300/.45);
}

.msf-09__topbar {
  height: 5px;
  background: var(--line);
}

.msf-09__topbar i {
  display: block;
  height: 100%;
  background: linear-gradient(90deg,var(--vio),oklch(0.65 0.18 340));
  transform: scaleX(var(--w));
  transform-origin: left;
  transition: transform .5s cubic-bezier(.4,0,.2,1);
}

.msf-09__count {
  padding: 18px 30px 0;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
}

.msf-09__stage {
  padding: 14px 30px 26px;
  min-height: 290px;
  display: grid;
}

.msf-09__q {
  grid-area: 1/1;
  border: none;
}

.msf-09__q.is-current:not([hidden]) {
  animation: msf-09-in .4s cubic-bezier(.2,.8,.2,1);
}

.msf-09__title {
  font-size: 23px;
  letter-spacing: -.015em;
  line-height: 1.25;
  margin-bottom: 20px;
  outline: none;
}

.msf-09__title em {
  font-style: normal;
  font-size: 15px;
  font-weight: 400;
  color: var(--mut);
}

.msf-09__hint {
  font-size: 13px;
  color: var(--mut);
  margin: -10px 0 16px;
}

.msf-09__faces {
  display: flex;
  gap: 14px;
}

.msf-09__face {
  display: grid;
  justify-items: center;
  gap: 8px;
  padding: 18px 22px;
  border: 2px solid var(--line);
  border-radius: 18px;
  cursor: pointer;
  color: var(--mut);
  font-size: 13px;
  font-weight: 700;
  transition: all .2s;
}

.msf-09__face input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-09__face:hover {
  transform: translateY(-3px);
  border-color: var(--vio);
  color: var(--vio);
}

.msf-09__face:has(:checked) {
  border-color: var(--vio);
  background: color-mix(in oklab,var(--vio) 9%,white);
  color: var(--vio);
}

.msf-09__face:has(:focus-visible) {
  outline: 3px solid var(--vio);
  outline-offset: 2px;
}

.msf-09__nps {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
}

.msf-09__nps label {
  position: relative;
  cursor: pointer;
}

.msf-09__nps input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-09__nps span {
  display: grid;
  place-items: center;
  width: 38px;
  height: 44px;
  border: 2px solid var(--line);
  border-radius: 10px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  transition: all .15s;
}

.msf-09__nps label:hover span {
  border-color: var(--vio);
  color: var(--vio);
  transform: translateY(-2px);
}

.msf-09__nps input:checked+span {
  background: var(--vio);
  border-color: var(--vio);
  color: #fff;
}

.msf-09__nps input:focus-visible+span {
  outline: 3px solid var(--vio);
  outline-offset: 2px;
}

.msf-09__opts {
  display: grid;
  gap: 9px;
}

.msf-09__opt {
  position: relative;
  display: block;
  padding: 15px 18px;
  border: 2px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
  transition: all .15s;
}

.msf-09__opt input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-09__opt:hover {
  border-color: var(--vio);
}

.msf-09__opt:has(:checked) {
  border-color: var(--vio);
  background: color-mix(in oklab,var(--vio) 8%,white);
}

.msf-09__opt:has(:checked) span::after {
  content: " ✓";
  color: var(--vio);
  font-weight: 800;
}

.msf-09__opt:has(:focus-visible) {
  outline: 3px solid var(--vio);
  outline-offset: 2px;
}

.msf-09__text {
  width: 100%;
  font: inherit;
  font-size: 15px;
  padding: 14px 16px;
  border: 2px solid var(--line);
  border-radius: 14px;
  resize: vertical;
  transition: border-color .2s,box-shadow .2s;
}

.msf-09__text:focus-visible {
  outline: none;
  border-color: var(--vio);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--vio) 15%,transparent);
}

.msf-09__counter {
  font-size: 12px;
  color: var(--mut);
  text-align: right;
  margin-top: 6px;
  font-variant-numeric: tabular-nums;
}

.msf-09__submit {
  margin-top: 14px;
  font: inherit;
  font-weight: 800;
  color: #fff;
  border: none;
  border-radius: 999px;
  padding: 14px 30px;
  cursor: pointer;
  background: linear-gradient(90deg,var(--vio),oklch(0.65 0.18 340));
  box-shadow: 0 14px 30px -12px var(--vio);
  transition: transform .15s,filter .2s;
}

.msf-09__submit:hover {
  transform: translateY(-1px);
  filter: brightness(1.08);
}

.msf-09__submit:focus-visible {
  outline: 3px solid var(--vio);
  outline-offset: 3px;
}

.msf-09__thanks[hidden] {
  display: none;
}

.msf-09__thanks {
  display: grid;
  justify-items: center;
  align-content: center;
  gap: 8px;
  text-align: center;
}

.msf-09__thanks b {
  font-size: 34px;
  color: var(--vio);
  animation: msf-09-spin .7s cubic-bezier(.34,1.56,.64,1);
}

.msf-09__thanks p {
  color: var(--mut);
  font-size: 14px;
}

.msf-09__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 30px;
  border-top: 1px solid var(--line);
}

.msf-09__back {
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  color: var(--mut);
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px 10px;
  border-radius: 8px;
}

.msf-09__back:hover {
  color: var(--vio);
}

.msf-09__back:focus-visible {
  outline: 3px solid var(--vio);
  outline-offset: 2px;
}

.msf-09__brand {
  font-size: 12px;
  font-weight: 800;
  color: var(--line);
  letter-spacing: .04em;
  margin-left: auto;
}

@keyframes msf-09-in {
  from {
    opacity: 0;
    transform: translateY(22px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-09-spin {
  from {
    transform: scale(.3) rotate(-90deg);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-09 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-09'); if (!root) return;
  const form = root.querySelector('.msf-09__card');
  const qs = [...root.querySelectorAll('[data-q]')];
  const bar = root.querySelector('.msf-09__topbar i');
  const count = root.querySelector('.msf-09__count');
  const back = root.querySelector('.msf-09__back');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const ADVANCE_MS = reduce ? 0 : 350;
  let cur = 0;
  const show = (i) => {
    cur = i;
    qs.forEach((q,k) => { q.hidden = k!==i; q.classList.toggle('is-current', k===i); });
    bar.style.setProperty('--w', (i/qs.length).toFixed(2));
    count.textContent = 'Question ' + (i+1) + ' of ' + qs.length;
    back.hidden = i === 0;
    qs[i].querySelector('.msf-09__title').focus();
  };
  root.addEventListener('change', e => {
    if (!e.target.matches('[data-advance]')) return;
    setTimeout(() => { if (!qs[cur].hidden && qs[cur].contains(e.target) && cur < qs.length-1) show(cur+1); }, ADVANCE_MS);
  });
  // number keys answer NPS directly
  root.addEventListener('keydown', e => {
    if (cur !== 1 || !/^[0-9]$/.test(e.key)) return;
    const r = root.querySelector('.msf-09__nps input[value="' + e.key + '"]');
    if (r) { r.checked = true; r.dispatchEvent(new Event('change', {bubbles:true})); }
  });
  back.addEventListener('click', () => show(cur-1));
  const ta = root.querySelector('.msf-09__text');
  ta.addEventListener('input', () => root.querySelector('#msf-09-counter').textContent = ta.value.length + ' / 280');
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-09__next--go, .msf-09__submit, .msf-09__skip')) return;

    e.preventDefault();
    qs.forEach(q => q.hidden = true);
    bar.style.setProperty('--w','1');
    count.textContent = 'Done'; back.hidden = true;
    const t = root.querySelector('.msf-09__thanks'); t.hidden = false; t.querySelector('h3').focus();
    });
})();
```
