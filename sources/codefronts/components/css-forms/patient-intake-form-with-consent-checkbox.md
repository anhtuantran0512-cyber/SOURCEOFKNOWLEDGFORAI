---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/patient-intake-form-with-consent-checkbox/"
title: "Patient Intake Form with Consent Checkbox"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A new-patient intake designed for accessibility first — set in Atkinson Hyperlegible, the typeface created for low-vision readers."
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Patient Intake Form with Consent Checkbox
Source: https://codefronts.com/components/css-forms/patient-intake-form-with-consent-checkbox/

A new-patient intake designed for accessibility first — set in Atkinson Hyperlegible, the typeface created for low-vision readers. Numbered sections with a live completion meter, a 0–10 pain slider that describes the level in words, allergy and insurance questions that reveal follow-ups only when relevant, and a consent block where the checkbox unlocks only after the full text has been scrolled, followed by a typed e-signature preview.
## HTML
```html
<div class="frm-15">
  <button type="button" class="frm-15__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-15__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-15__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-15__stage">
    <div class="frm-15__card" role="form" aria-labelledby="frm-15-title">
      <header class="frm-15__head">
        <div class="frm-15__clinic"><span aria-hidden="true">+</span>Harbor Family Clinic</div>
        <h2 id="frm-15-title">New patient intake</h2>
        <p>About 6 minutes. Your information is encrypted and only seen by your care team.</p>
        <div class="frm-15__meter"><div class="frm-15__bar" aria-hidden="true"><i></i></div><span class="frm-15__pct" aria-live="polite">0% complete</span></div>
      </header>
      <section class="frm-15__sec" aria-labelledby="frm-15-s1"><h3 id="frm-15-s1"><span>1</span>About you</h3>
        <div class="frm-15__grid">
          <div class="frm-15__field"><label for="frm-15-fn">Legal first name</label><input id="frm-15-fn" autocomplete="given-name" required></div>
          <div class="frm-15__field"><label for="frm-15-ln">Last name</label><input id="frm-15-ln" autocomplete="family-name" required></div>
          <div class="frm-15__field"><label for="frm-15-dob">Date of birth</label><input id="frm-15-dob" type="date" autocomplete="bday" required></div>
          <div class="frm-15__field"><label for="frm-15-ph">Mobile phone</label><input id="frm-15-ph" type="tel" autocomplete="tel" required></div>
        </div>
      </section>
      <section class="frm-15__sec" aria-labelledby="frm-15-s2"><h3 id="frm-15-s2"><span>2</span>Today's visit</h3>
        <div class="frm-15__field"><label for="frm-15-why">Main reason for your visit</label><textarea id="frm-15-why" rows="2" required placeholder="e.g. Persistent cough for two weeks"></textarea></div>
        <div class="frm-15__field">
          <div class="frm-15__lr"><label for="frm-15-pain">Current pain level</label><output class="frm-15__painout" for="frm-15-pain">0 — No pain</output></div>
          <input id="frm-15-pain" type="range" min="0" max="10" value="0" aria-valuetext="0 — No pain">
          <div class="frm-15__ticks" aria-hidden="true"><span>0</span><span>5</span><span>10</span></div>
        </div>
      </section>
      <section class="frm-15__sec" aria-labelledby="frm-15-s3"><h3 id="frm-15-s3"><span>3</span>Medical history</h3>
        <fieldset class="frm-15__q">
          <legend>Do you have any allergies to medicines, foods or latex?</legend>
          <div class="frm-15__yn"><label><input type="radio" name="frm-15-al" value="no" required><span>No</span></label><label><input type="radio" name="frm-15-al" value="yes"><span>Yes</span></label></div>
          <div class="frm-15__reveal"><label for="frm-15-ald">Please list them and the reaction</label><textarea id="frm-15-ald" rows="2" placeholder="e.g. Penicillin — hives"></textarea></div>
        </fieldset>
        <fieldset class="frm-15__chips"><legend>Ongoing conditions <span class="frm-15__opt">Select any</span></legend>
          <label><input type="checkbox"><span>Asthma</span></label><label><input type="checkbox"><span>Diabetes</span></label><label><input type="checkbox"><span>High blood pressure</span></label><label><input type="checkbox"><span>Heart condition</span></label><label><input type="checkbox"><span>Anxiety / depression</span></label>
        </fieldset>
      </section>
      <section class="frm-15__sec" aria-labelledby="frm-15-s4"><h3 id="frm-15-s4"><span>4</span>Insurance</h3>
        <fieldset class="frm-15__q">
          <legend>How will you pay for today's visit?</legend>
          <div class="frm-15__yn"><label><input type="radio" name="frm-15-ins" value="yes" checked><span>Insurance</span></label><label><input type="radio" name="frm-15-ins" value="self"><span>Self-pay</span></label></div>
          <div class="frm-15__reveal frm-15__grid">
            <div class="frm-15__field"><label for="frm-15-prov">Insurance provider</label><input id="frm-15-prov" placeholder="e.g. Aetna, BUPA, Medibank"></div>
            <div class="frm-15__field"><label for="frm-15-mem">Member ID</label><input id="frm-15-mem" spellcheck="false"></div>
          </div>
        </fieldset>
      </section>
      <section class="frm-15__sec" aria-labelledby="frm-15-s5"><h3 id="frm-15-s5"><span>5</span>Consent</h3>
        <div class="frm-15__terms" tabindex="0" role="region" aria-label="Consent to treatment and privacy notice">
          <h4>Consent to treatment</h4>
          <p>I consent to examination and treatment by the clinicians of Harbor Family Clinic, including routine diagnostic procedures. I understand I may ask questions and refuse any part of my care at any time.</p>
          <h4>Use of health information</h4>
          <p>My health information will be used to provide care, arrange payment and run clinic operations, as described in the Notice of Privacy Practices. It will not be sold or used for marketing.</p>
          <h4>Financial responsibility</h4>
          <p>I am responsible for charges not covered by my insurer, including co-pays and deductibles. Missed appointments without 24 hours' notice may incur a fee.</p>
          <h4>Communication</h4>
          <p>The clinic may contact me by phone, SMS or email for reminders and results. I can change these preferences at any time.</p>
          <span class="frm-15__end" aria-hidden="true"></span>
        </div>
        <p class="frm-15__scrollhint" aria-live="polite">Scroll to the end of the consent text to continue.</p>
        <label class="frm-15__consent"><input type="checkbox" id="frm-15-consent" disabled required><span>I have read and agree to the consent and privacy notice above.</span></label>
        <div class="frm-15__field"><label for="frm-15-sig">Type your full name as signature</label><input id="frm-15-sig" required autocomplete="name"></div>
        <div class="frm-15__sigpad" aria-hidden="true"><span class="frm-15__sigtext">Your signature</span><small class="frm-15__sigdate"></small></div>
      </section>
      <button type="button" class="frm-15__submit">Submit intake form</button>
      <p class="frm-15__status" role="status"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Caveat:wght@500&display=swap');

.frm-15 {
  --bg: #eaf3f2;
  --card: #ffffff;
  --ink: #0d2624;
  --muted: #4a6461;
  --line: #d3e3e1;
  --soft: #f3f9f8;
  --accent: #0f766e;
  --on-accent: #fff;
  --warn: #b45309;
  --bad: #b91c1c;
  --sans: "Atkinson Hyperlegible",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --script: "Caveat","Brush Script MT",cursive;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  font-size: 1.0625rem;
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-15:not([data-theme="light"]) {
    --bg: #071312;
    --card: #0d1d1c;
    --ink: #e3f2f0;
    --muted: #9ab8b4;
    --line: #1f3533;
    --soft: #112624;
    --accent: #2dd4bf;
    --on-accent: #032220;
    --warn: #fbbf24;
    --bad: #f87171;
  }
}

.frm-15[data-theme="dark"] {
  --bg: #071312;
  --card: #0d1d1c;
  --ink: #e3f2f0;
  --muted: #9ab8b4;
  --line: #1f3533;
  --soft: #112624;
  --accent: #2dd4bf;
  --on-accent: #032220;
  --warn: #fbbf24;
  --bad: #f87171;
}

.frm-15,
.frm-15 *,
.frm-15 *::before,
.frm-15 *::after {
  box-sizing: border-box;
}

.frm-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3.5rem);
}

.frm-15__card {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 1.5rem;
  padding: clamp(1.25rem,5vw,2.5rem);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  box-shadow: 0 30px 70px -40px rgba(13,38,36,.45);
}

.frm-15__head {
  display: grid;
  gap: .6rem;
}

.frm-15__clinic {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-weight: 700;
  color: var(--accent);
}

.frm-15__clinic span {
  display: grid;
  place-items: center;
  width: 1.8rem;
  height: 1.8rem;
  border-radius: .5rem;
  background: var(--accent);
  color: var(--on-accent);
  font-size: 1.3rem;
  line-height: 1;
}

.frm-15 h2 {
  margin: .2rem 0 0;
  font-size: clamp(1.6rem,4vw,2.1rem);
  letter-spacing: -.01em;
}

.frm-15__head p {
  margin: 0;
  color: var(--muted);
  line-height: 1.5;
}

.frm-15__meter {
  display: flex;
  align-items: center;
  gap: .9rem;
  margin-top: .4rem;
}

.frm-15__bar {
  flex: 1;
  height: .5rem;
  border-radius: 99px;
  background: var(--line);
  overflow: hidden;
}

.frm-15__bar i {
  display: block;
  height: 100%;
  background: var(--accent);
  border-radius: inherit;
  scale: var(--done,0) 1;
  transform-origin: left;
  transition: scale .5s var(--ease);
}

.frm-15__pct {
  font-size: .9rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  min-width: 7.5rem;
  text-align: right;
}

.frm-15__sec {
  display: grid;
  gap: 1.05rem;
  padding-top: 1.4rem;
  border-top: 1px solid var(--line);
}

.frm-15 h3 {
  display: flex;
  align-items: center;
  gap: .65rem;
  margin: 0;
  font-size: 1.2rem;
}

.frm-15 h3 span {
  display: grid;
  place-items: center;
  width: 1.9rem;
  height: 1.9rem;
  border-radius: 50%;
  background: var(--soft);
  border: 1.5px solid var(--accent);
  color: var(--accent);
  font-size: .95rem;
}

.frm-15__sec.is-done h3 span {
  background: var(--accent);
  color: var(--on-accent);
  font-size: 0;
}

.frm-15__sec.is-done h3 span::before {
  content: '✓';
  font-size: .95rem;
}

.frm-15__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
}

.frm-15__field {
  display: grid;
  gap: .45rem;
}

.frm-15 label,
.frm-15 legend {
  font-weight: 700;
  font-size: 1rem;
}

.frm-15__opt {
  font-weight: 400;
  color: var(--muted);
  font-size: .9rem;
}

.frm-15 input:not([type="radio"]):not([type="checkbox"]):not([type="range"]),
.frm-15 textarea {
  width: 100%;
  min-height: 3.1rem;
  padding: .7rem .95rem;
  border-radius: .75rem;
  border: 2px solid var(--line);
  background: var(--soft);
  color: var(--ink);
  font: inherit;
  transition: border-color .2s, box-shadow .2s;
}

.frm-15 textarea {
  resize: vertical;
  line-height: 1.5;
}

.frm-15 :is(input,textarea):focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 22%,transparent);
}

.frm-15 :user-invalid:not(fieldset) {
  border-color: var(--bad);
}

.frm-15__lr {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: .5rem;
  align-items: baseline;
}

.frm-15__painout {
  font-weight: 700;
  color: var(--pc,var(--accent));
}

.frm-15 input[type="range"] {
  --fill: 0%;
  --pc: #16a34a;
  appearance: none;
  -webkit-appearance: none;
  width: 100%;
  height: 2.75rem;
  background: transparent;
  cursor: pointer;
}

.frm-15 input[type="range"]::-webkit-slider-runnable-track {
  height: .6rem;
  border-radius: 99px;
  background: linear-gradient(90deg,#16a34a,#eab308 50%,#dc2626);
}

.frm-15 input[type="range"]::-moz-range-track {
  height: .6rem;
  border-radius: 99px;
  background: linear-gradient(90deg,#16a34a,#eab308 50%,#dc2626);
}

.frm-15 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 1.75rem;
  height: 1.75rem;
  margin-top: -.575rem;
  border-radius: 50%;
  background: var(--card);
  border: 4px solid var(--pc);
  box-shadow: 0 3px 8px rgba(0,0,0,.25);
}

.frm-15 input[type="range"]::-moz-range-thumb {
  width: 1.3rem;
  height: 1.3rem;
  border-radius: 50%;
  background: var(--card);
  border: 4px solid var(--pc);
}

.frm-15 input[type="range"]:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: .5rem;
}

.frm-15__ticks {
  display: flex;
  justify-content: space-between;
  font-size: .85rem;
  color: var(--muted);
  margin-top: -.4rem;
}

.frm-15 fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
}

.frm-15 legend {
  padding: 0;
  margin-bottom: .6rem;
}

.frm-15__q {
  display: grid;
  gap: .8rem;
}

.frm-15__yn {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.frm-15__yn label,
.frm-15__chips label {
  position: relative;
}

.frm-15__yn input,
.frm-15__chips input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-15__yn span {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-height: 3rem;
  min-width: 7rem;
  padding: 0 1.1rem;
  border-radius: .75rem;
  border: 2px solid var(--line);
  font-weight: 700;
  transition: all .2s;
}

.frm-15__yn span::before {
  content: '';
  width: 1.1rem;
  height: 1.1rem;
  border-radius: 50%;
  border: 2px solid var(--muted);
  transition: border .2s var(--ease);
}

.frm-15__yn input:checked + span {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 9%,var(--card));
}

.frm-15__yn input:checked + span::before {
  border: 6px solid var(--accent);
}

.frm-15 :is(.frm-15__yn,.frm-15__chips) input:focus-visible + span {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.frm-15__reveal {
  display: none;
  gap: .45rem;
}

.frm-15__q:has([value="yes"]:checked) .frm-15__reveal {
  display: grid;
  animation: frm-15-in .35s var(--ease);
}

@keyframes frm-15-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }
}

.frm-15__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.frm-15__chips legend {
  width: 100%;
}

.frm-15__chips span {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.75rem;
  padding: 0 1rem;
  border-radius: 999px;
  border: 2px solid var(--line);
  font-size: .95rem;
  transition: all .2s;
}

.frm-15__chips input:checked + span {
  border-color: var(--accent);
  background: var(--accent);
  color: var(--on-accent);
}

.frm-15__chips input:checked + span::before {
  content: '✓';
}

.frm-15__terms {
  max-height: 11rem;
  overflow: auto;
  padding: 1rem 1.15rem;
  border-radius: .9rem;
  border: 2px solid var(--line);
  background: var(--soft);
  line-height: 1.6;
  font-size: .95rem;
  scrollbar-gutter: stable;
}

.frm-15__terms:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.frm-15__terms h4 {
  margin: .9rem 0 .25rem;
  font-size: 1rem;
}

.frm-15__terms h4:first-child {
  margin-top: 0;
}

.frm-15__terms p {
  margin: 0;
  color: var(--muted);
}

.frm-15__end {
  display: block;
  height: 1px;
}

.frm-15__scrollhint {
  margin: -.4rem 0 0;
  font-size: .9rem;
  color: var(--warn);
  font-weight: 700;
}

.frm-15__scrollhint.is-ok {
  color: var(--accent);
}

.frm-15__consent {
  display: flex;
  align-items: flex-start;
  gap: .75rem;
  padding: 1rem;
  border-radius: .9rem;
  border: 2px solid var(--line);
  cursor: pointer;
  transition: border-color .2s, background .2s;
}

.frm-15__consent input {
  flex: none;
  width: 1.4rem;
  height: 1.4rem;
  margin: .05rem 0 0;
  accent-color: var(--accent);
}

.frm-15__consent:has(input:disabled) {
  opacity: .55;
  cursor: not-allowed;
}

.frm-15__consent:has(input:checked) {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 7%,var(--card));
}

.frm-15__sigpad {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  min-height: 5rem;
  padding: .5rem 1rem .6rem;
  border-bottom: 2px solid var(--ink);
  background: repeating-linear-gradient(transparent 0 1.95rem, color-mix(in oklab,var(--line) 70%,transparent) 1.95rem 2rem);
}

.frm-15__sigpad::before {
  content: '✕';
  position: absolute;
  left: .2rem;
  bottom: .6rem;
  color: var(--muted);
  font-size: .9rem;
}

.frm-15__sigtext {
  font: 500 2.4rem/1 var(--script);
  color: var(--accent);
  padding-left: 1rem;
  opacity: .35;
}

.frm-15__sigtext.is-on {
  opacity: 1;
}

.frm-15__sigdate {
  color: var(--muted);
  font-size: .85rem;
}

.frm-15__submit {
  min-height: 3.4rem;
  border: 0;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--on-accent);
  background: var(--accent);
  transition: opacity .2s, translate .2s var(--ease);
}

.frm-15__card:not(:has(#frm-15-consent:checked)) .frm-15__submit {
  opacity: .5;
}

.frm-15__submit:hover {
  translate: 0 -2px;
}

.frm-15__submit:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.frm-15__status {
  margin: -.6rem 0 0;
  font-weight: 700;
  text-align: center;
}

.frm-15__status:empty {
  display: none;
}

.frm-15__status[data-ok="true"] {
  color: var(--accent);
}

.frm-15__status[data-ok="false"] {
  color: var(--bad);
}

@media (prefers-reduced-motion: reduce) {
  .frm-15 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-15__yn input:checked + span,
    .frm-15__chips input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-15__bar i {
    background: Highlight;
  }

  .frm-15__submit {
    border: 2px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-15 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-15__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-15__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-15__theme:active {
  transform: scale(.94);
}

.frm-15__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-15__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-15__theme .frm-15__sun,
.frm-15__theme[aria-pressed="true"] .frm-15__moon {
  display: none;
}

.frm-15__theme[aria-pressed="true"] .frm-15__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-15__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-15__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-15').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-15');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const PAIN = ['No pain', 'Very mild', 'Mild', 'Uncomfortable', 'Moderate', 'Distracting', 'Moderate to severe', 'Severe', 'Very severe', 'Intense', 'Worst imaginable'];
  const pain = $('#frm-15-pain'), out = $('.frm-15__painout');
  const setPain = () => {
    const v = Number(pain.value), hue = 140 - v * 14, c = 'hsl(' + hue + ' 75% 38%)';
    out.textContent = v + ' — ' + PAIN[v]; pain.setAttribute('aria-valuetext', out.textContent);
    pain.style.setProperty('--pc', c); out.style.setProperty('--pc', c);
  };
  pain.addEventListener('input', setPain); setPain();
  const consent = $('#frm-15-consent'), hint = $('.frm-15__scrollhint'), terms = $('.frm-15__terms');
  new IntersectionObserver(([e]) => {
    if (e.isIntersecting && consent.disabled) { consent.disabled = false; hint.textContent = 'Thanks for reading — you can now give consent.'; hint.classList.add('is-ok'); }
  }, { root: terms, threshold: 1 }).observe($('.frm-15__end'));
  const sig = $('#frm-15-sig'), sigText = $('.frm-15__sigtext');
  $('.frm-15__sigdate').textContent = new Intl.DateTimeFormat('en-US', { dateStyle: 'medium' }).format(new Date());
  sig.addEventListener('input', () => { sigText.textContent = sig.value || 'Your signature'; sigText.classList.toggle('is-on', !!sig.value); });
  const secs = [...root.querySelectorAll('.frm-15__sec')];
  const progress = () => {
    let done = 0, total = 0;
    secs.forEach((s) => {
      const req = [...s.querySelectorAll('[required]')], seen = new Set();
      const ok = req.filter((f) => { if (f.type === 'radio') { if (seen.has(f.name)) return false; seen.add(f.name); return !!s.querySelector('[name="' + f.name + '"]:checked'); } return f.type === 'checkbox' ? f.checked : f.value.trim() && f.checkValidity(); }).length;
      const count = req.filter((f) => f.type !== 'radio').length + seen.size || 1;
      total += req.length ? count : 0; done += ok;
      s.classList.toggle('is-done', !req.length ? false : ok === count);
    });
    const pct = total ? Math.round((done / total) * 100) : 0;
    root.style.setProperty('--done', pct / 100); $('.frm-15__pct').textContent = pct + '% complete';
  };
  root.addEventListener('input', progress); root.addEventListener('change', progress); progress();
  $('.frm-15__submit').addEventListener('click', () => {
    const status = $('.frm-15__status');
    const bad = [...root.querySelectorAll('[required]')].find((f) => f.type === 'radio' ? !root.querySelector('[name="' + f.name + '"]:checked') : !f.checkValidity());
    if (bad) { status.dataset.ok = 'false'; status.textContent = consent.disabled ? 'Please read the consent text to the end.' : 'A few required answers are missing.'; (consent.disabled ? terms : bad).focus(); return; }
    status.dataset.ok = 'true'; status.textContent = 'Submitted securely. Please arrive 10 minutes early — see you soon.';
  });
})();
```
