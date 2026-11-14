---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/job-application-form-with-resume-upload/"
title: "Job Application Form with Resume Upload"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A careers-page application broken into three calm steps — About you, Résumé, Final questions — with a step indicator that is a real ordered list…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Job Application Form with Resume Upload
Source: https://codefronts.com/components/css-forms/job-application-form-with-resume-upload/

A careers-page application broken into three calm steps — About you, Résumé, Final questions — with a step indicator that is a real ordered list (aria-current="step"), per-step native validation, a résumé drop zone restricted to PDF/DOC/DOCX up to 5 MB that turns into a file card with replace/remove, an optional cover-letter, work-authorisation radios, and a review screen before submit.
## HTML
```html
<div class="frm-08" data-step="1">
  <button type="button" class="frm-08__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-08__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-08__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-08__stage">
    <div class="frm-08__card">
      <header class="frm-08__job">
        <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=900&h=360&fit=crop&auto=format&q=70" width="900" height="360" alt="Product team collaborating around a table with laptops" loading="lazy" decoding="async">
        <div class="frm-08__jobtext">
          <p class="frm-08__co">Fieldnote · Design team</p>
          <h2>Senior Product Designer</h2>
          <ul class="frm-08__tags" aria-label="Job details"><li>Remote · US / UK</li><li>Full-time</li><li>$145k–$175k</li></ul>
        </div>
      </header>
      <ol class="frm-08__steps" aria-label="Application progress">
        <li aria-current="step"><span class="frm-08__n">1</span>About you</li>
        <li><span class="frm-08__n">2</span>Résumé</li>
        <li><span class="frm-08__n">3</span>Final questions</li>
      </ol>
      <div class="frm-08__body" role="form" aria-label="Job application">
        <fieldset class="frm-08__step" data-i="1">
          <legend tabindex="-1">About you</legend>
          <div class="frm-08__grid">
            <div class="frm-08__field"><label for="frm-08-fn">First name</label><input id="frm-08-fn" autocomplete="given-name" required></div>
            <div class="frm-08__field"><label for="frm-08-ln">Last name</label><input id="frm-08-ln" autocomplete="family-name" required></div>
          </div>
          <div class="frm-08__grid">
            <div class="frm-08__field"><label for="frm-08-em">Email</label><input id="frm-08-em" type="email" autocomplete="email" required></div>
            <div class="frm-08__field"><label for="frm-08-ph">Phone</label><input id="frm-08-ph" type="tel" autocomplete="tel" placeholder="+1 555 010 1234"></div>
          </div>
          <div class="frm-08__field"><label for="frm-08-loc">Current location</label><input id="frm-08-loc" autocomplete="address-level2" placeholder="City, country" required></div>
          <div class="frm-08__field"><label for="frm-08-li">LinkedIn or portfolio URL</label><input id="frm-08-li" type="url" placeholder="https://" autocomplete="url"></div>
        </fieldset>
        <fieldset class="frm-08__step" data-i="2" hidden>
          <legend tabindex="-1">Résumé</legend>
          <div class="frm-08__resume">
            <label class="frm-08__dz">
              <input type="file" id="frm-08-cv" accept=".pdf,.doc,.docx" required aria-describedby="frm-08-cv-hint">
              <span class="frm-08__dzicon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"/><path d="M14 3v5h5M12 17v-6M9.5 13.5 12 11l2.5 2.5"/></svg></span>
              <b>Upload your résumé</b>
              <span id="frm-08-cv-hint">PDF, DOC or DOCX · max 5 MB</span>
            </label>
            <div class="frm-08__file">
              <span class="frm-08__ficon" aria-hidden="true">PDF</span>
              <div><b class="frm-08__fname">resume.pdf</b><small class="frm-08__fsize">—</small></div>
              <div class="frm-08__factions"><label for="frm-08-cv" class="frm-08__link">Replace</label><button type="button" class="frm-08__link frm-08__rm">Remove</button></div>
            </div>
          </div>
          <p class="frm-08__msg" aria-live="polite"></p>
          <div class="frm-08__field"><label for="frm-08-cl">Cover letter <span class="frm-08__opt">Optional</span></label><textarea id="frm-08-cl" rows="5" placeholder="Tell us about a product decision you're proud of and why."></textarea></div>
        </fieldset>
        <fieldset class="frm-08__step" data-i="3" hidden>
          <legend tabindex="-1">Final questions</legend>
          <fieldset class="frm-08__radios">
            <legend>Are you authorised to work in the US or UK?</legend>
            <label><input type="radio" name="frm-08-auth" value="Yes" required><span>Yes</span></label>
            <label><input type="radio" name="frm-08-auth" value="Requires sponsorship"><span>I'll need sponsorship</span></label>
          </fieldset>
          <div class="frm-08__grid">
            <div class="frm-08__field"><label for="frm-08-start">Earliest start date</label><input id="frm-08-start" type="date" required></div>
            <div class="frm-08__field"><label for="frm-08-src">How did you hear about us?</label><select id="frm-08-src"><option>LinkedIn</option><option>Referral</option><option>Company website</option><option>Dribbble</option><option>Other</option></select></div>
          </div>
          <div class="frm-08__review" aria-label="Review your application">
            <h3>Review</h3>
            <dl><div><dt>Name</dt><dd data-review="name"></dd></div><div><dt>Email</dt><dd data-review="email"></dd></div><div><dt>Résumé</dt><dd data-review="cv"></dd></div></dl>
          </div>
        </fieldset>
        <div class="frm-08__done" hidden tabindex="-1">
          <span aria-hidden="true">✓</span><h3>Application received</h3><p>We'll review it within 5 working days. Keep an eye on your inbox.</p>
        </div>
        <div class="frm-08__nav">
          <button type="button" class="frm-08__back">Back</button>
          <button type="button" class="frm-08__next">Continue</button>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Young+Serif&family=Hanken+Grotesk:wght@400;500;600;700&display=swap');

.frm-08 {
  --bg: #f5efe6;
  --card: #fffcf7;
  --ink: #2a1d15;
  --muted: #7a6758;
  --line: #eadfce;
  --soft: #f8f2e8;
  --accent: #c2502b;
  --on-accent: #fff;
  --ok: #3f7d4e;
  --bad: #b42318;
  --serif: "Young Serif",ui-serif,Georgia,serif;
  --sans: "Hanken Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-08:not([data-theme="light"]) {
    --bg: #17110d;
    --card: #1f1813;
    --ink: #f4e9dc;
    --muted: #b19c88;
    --line: #3a2d23;
    --soft: #271e17;
    --accent: #f07a4f;
    --on-accent: #2a0f04;
    --ok: #7bc58b;
    --bad: #ff8a7a;
  }
}

.frm-08[data-theme="dark"] {
  --bg: #17110d;
  --card: #1f1813;
  --ink: #f4e9dc;
  --muted: #b19c88;
  --line: #3a2d23;
  --soft: #271e17;
  --accent: #f07a4f;
  --on-accent: #2a0f04;
  --ok: #7bc58b;
  --bad: #ff8a7a;
}

.frm-08,
.frm-08 *,
.frm-08 *::before,
.frm-08 *::after {
  box-sizing: border-box;
}

.frm-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-08__card {
  width: 100%;
  max-width: 42rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.75rem;
  overflow: hidden;
  box-shadow: 0 30px 70px -40px rgba(70,35,10,.5);
}

.frm-08__job {
  position: relative;
  display: grid;
}

.frm-08__job img {
  grid-area: 1/1;
  width: 100%;
  height: 12rem;
  object-fit: cover;
  background: #c9b49c;
}

.frm-08__jobtext {
  grid-area: 1/1;
  align-self: end;
  padding: 1.5rem clamp(1.25rem,5vw,2.25rem);
  color: #fff;
  background: linear-gradient(transparent, rgba(30,15,5,.85));
}

.frm-08__co {
  margin: 0 0 .35rem;
  font-size: .8rem;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  opacity: .85;
}

.frm-08 h2 {
  margin: 0;
  font: 400 clamp(1.6rem,5vw,2.2rem)/1.1 var(--serif);
  letter-spacing: -.01em;
}

.frm-08__tags {
  list-style: none;
  margin: .8rem 0 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}

.frm-08__tags li {
  font-size: .78rem;
  font-weight: 600;
  padding: .3rem .65rem;
  border-radius: 99px;
  background: rgba(255,255,255,.18);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.frm-08__steps {
  list-style: none;
  margin: 0;
  padding: 1.1rem clamp(1.25rem,5vw,2.25rem);
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .5rem;
  border-bottom: 1px solid var(--line);
  counter-reset: s;
}

.frm-08__steps li {
  position: relative;
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .85rem;
  font-weight: 600;
  color: var(--muted);
}

.frm-08__steps li:not(:last-child)::after {
  content: '';
  flex: 1;
  height: 2px;
  border-radius: 2px;
  background: var(--line);
  margin-inline: .25rem;
}

.frm-08__steps li.is-done::after {
  background: var(--accent);
}

.frm-08__n {
  display: grid;
  place-items: center;
  flex: none;
  width: 1.75rem;
  height: 1.75rem;
  border-radius: 50%;
  border: 1.5px solid var(--line);
  font-size: .8rem;
  background: var(--card);
  transition: all .3s var(--ease);
}

.frm-08__steps li[aria-current="step"] {
  color: var(--ink);
}

.frm-08__steps li[aria-current="step"] .frm-08__n {
  border-color: var(--accent);
  color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 15%,transparent);
}

.frm-08__steps li.is-done .frm-08__n {
  background: var(--accent);
  border-color: var(--accent);
  color: var(--on-accent);
  font-size: 0;
}

.frm-08__steps li.is-done .frm-08__n::before {
  content: '✓';
  font-size: .8rem;
}

@media (max-width: 34rem) {
  .frm-08__steps li {
    font-size: 0;
    gap: 0;
  }

  .frm-08__steps li[aria-current="step"] {
    font-size: .85rem;
    gap: .55rem;
  }
}

.frm-08__body {
  display: grid;
  gap: 1.25rem;
  padding: clamp(1.25rem,5vw,2.25rem);
}

.frm-08__step {
  border: 0;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1.05rem;
  min-width: 0;
  animation: frm-08-in .45s var(--ease);
}

.frm-08__step[hidden] {
  display: none;
}

@keyframes frm-08-in {
  from {
    opacity: 0;
    translate: 14px 0;
  }
}

.frm-08__step > legend {
  padding: 0;
  margin-bottom: .3rem;
  font: 400 1.45rem var(--serif);
  outline: none;
}

.frm-08__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
}

.frm-08__field {
  display: grid;
  gap: .4rem;
}

.frm-08 label {
  font-size: .86rem;
  font-weight: 600;
}

.frm-08__opt {
  font-weight: 400;
  color: var(--muted);
}

.frm-08 input:not([type="radio"]):not([type="file"]),
.frm-08 select,
.frm-08 textarea {
  width: 100%;
  min-height: 3rem;
  padding: .7rem .95rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: var(--soft);
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  transition: border-color .2s, box-shadow .25s var(--ease), background .2s;
}

.frm-08 textarea {
  resize: vertical;
  line-height: 1.55;
}

.frm-08 :is(input,select,textarea):focus-visible {
  outline: none;
  border-color: var(--accent);
  background: var(--card);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 18%,transparent);
}

.frm-08 input:user-invalid {
  border-color: var(--bad);
}

.frm-08__dz {
  position: relative;
  display: grid;
  justify-items: center;
  gap: .35rem;
  padding: 2rem 1rem;
  text-align: center;
  border: 1.5px dashed color-mix(in oklab,var(--accent) 45%,var(--line));
  border-radius: 1.1rem;
  background: color-mix(in oklab,var(--accent) 4%,var(--soft));
  cursor: pointer;
  transition: background .2s, border-color .2s;
}

.frm-08__dz:hover {
  background: color-mix(in oklab,var(--accent) 9%,var(--soft));
}

.frm-08__dz:focus-within {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.frm-08__dz input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
  width: 100%;
}

.frm-08__dz span:not(.frm-08__dzicon) {
  font-size: .82rem;
  font-weight: 400;
  color: var(--muted);
}

.frm-08__dzicon svg {
  width: 2.2rem;
  height: 2.2rem;
  fill: none;
  stroke: var(--accent);
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-08__file {
  display: none;
  grid-template-columns: auto 1fr auto;
  gap: .9rem;
  align-items: center;
  padding: 1rem;
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  background: var(--soft);
  animation: frm-08-in .4s var(--ease);
}

.frm-08__resume:has(input:valid) .frm-08__dz {
  display: none;
}

.frm-08__resume:has(input:valid) .frm-08__file {
  display: grid;
}

.frm-08__ficon {
  display: grid;
  place-items: center;
  width: 2.75rem;
  height: 3.25rem;
  border-radius: .5rem;
  background: var(--accent);
  color: var(--on-accent);
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .05em;
  clip-path: polygon(0 0,72% 0,100% 22%,100% 100%,0 100%);
}

.frm-08__file b {
  display: block;
  font-size: .95rem;
  word-break: break-all;
}

.frm-08__file small {
  color: var(--muted);
  font-size: .8rem;
}

.frm-08__factions {
  display: flex;
  gap: .25rem;
}

.frm-08__link {
  min-height: 2.5rem;
  display: inline-flex;
  align-items: center;
  padding: 0 .7rem;
  border: 0;
  border-radius: .6rem;
  background: transparent;
  color: var(--accent);
  font: inherit;
  font-size: .85rem;
  font-weight: 600;
  cursor: pointer;
}

.frm-08__link:hover {
  background: color-mix(in oklab,var(--accent) 10%,transparent);
}

.frm-08__link:focus-visible {
  outline: 2px solid var(--accent);
}

.frm-08__msg {
  margin: -.4rem 0 0;
  font-size: .82rem;
  color: var(--bad);
}

.frm-08__msg:empty {
  display: none;
}

.frm-08__radios {
  border: 0;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.frm-08__radios legend {
  padding: 0;
  margin-bottom: .55rem;
  font-size: .86rem;
  font-weight: 600;
}

.frm-08__radios label {
  position: relative;
}

.frm-08__radios input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-08__radios span {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-height: 2.9rem;
  padding: 0 1.1rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: var(--soft);
  font-weight: 500;
  transition: all .2s;
}

.frm-08__radios span::before {
  content: '';
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
  border: 1.5px solid var(--muted);
  transition: border .25s var(--ease);
}

.frm-08__radios input:checked + span {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 8%,var(--card));
}

.frm-08__radios input:checked + span::before {
  border: 5px solid var(--accent);
}

.frm-08__radios input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.frm-08__review {
  padding: 1.1rem 1.25rem;
  border-radius: 1rem;
  background: var(--soft);
  border: 1px solid var(--line);
}

.frm-08__review h3 {
  margin: 0 0 .6rem;
  font: 400 1.05rem var(--serif);
}

.frm-08__review dl {
  margin: 0;
  display: grid;
  gap: .4rem;
}

.frm-08__review dl div {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  font-size: .9rem;
}

.frm-08__review dt {
  color: var(--muted);
}

.frm-08__review dd {
  margin: 0;
  font-weight: 600;
  text-align: right;
  word-break: break-word;
}

.frm-08__nav {
  display: flex;
  justify-content: space-between;
  gap: .75rem;
  padding-top: 1.1rem;
  border-top: 1px solid var(--line);
}

.frm-08__back,
.frm-08__next {
  min-height: 3rem;
  padding: 0 1.4rem;
  border-radius: .85rem;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
  transition: translate .2s var(--ease), filter .2s, background .2s;
}

.frm-08__back {
  border: 1px solid var(--line);
  background: transparent;
  color: var(--ink);
}

.frm-08__back:hover {
  background: var(--soft);
}

.frm-08[data-step="1"] .frm-08__back {
  visibility: hidden;
}

.frm-08__next {
  border: 0;
  background: var(--accent);
  color: var(--on-accent);
  margin-left: auto;
  box-shadow: 0 10px 22px -12px var(--accent);
}

.frm-08__next:hover {
  translate: 0 -2px;
  filter: brightness(1.06);
}

.frm-08__back:focus-visible,
.frm-08__next:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-08__done {
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .4rem;
  padding: 1.5rem 0;
  outline: none;
  animation: frm-08-in .5s var(--ease);
}

.frm-08__done[hidden] {
  display: none;
}

.frm-08__done span {
  display: grid;
  place-items: center;
  width: 3.75rem;
  height: 3.75rem;
  border-radius: 50%;
  background: var(--ok);
  color: #fff;
  font-size: 1.6rem;
  font-weight: 700;
}

.frm-08__done h3 {
  margin: .6rem 0 0;
  font: 400 1.6rem var(--serif);
}

.frm-08__done p {
  margin: 0;
  color: var(--muted);
}

.frm-08.is-sent .frm-08__nav {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .frm-08 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-08__steps li.is-done .frm-08__n,
    .frm-08__radios input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-08__next {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-08 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-08__theme {
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

.frm-08__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-08__theme:active {
  transform: scale(.94);
}

.frm-08__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-08__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-08__theme .frm-08__sun,
.frm-08__theme[aria-pressed="true"] .frm-08__moon {
  display: none;
}

.frm-08__theme[aria-pressed="true"] .frm-08__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-08__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-08__theme {
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
  document.querySelectorAll('.frm-08').forEach((root) => {
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
  const root = document.querySelector('.frm-08');
  if (!root) return;
  const steps = [...root.querySelectorAll('.frm-08__step')], dots = [...root.querySelectorAll('.frm-08__steps li')];
  const next = root.querySelector('.frm-08__next'), back = root.querySelector('.frm-08__back');
  const cv = root.querySelector('#frm-08-cv'), msg = root.querySelector('.frm-08__msg'), MAX_MB = 5;
  let i = 0;
  const show = (n) => {
    i = n;
    steps.forEach((s, j) => { s.hidden = j !== i; });
    dots.forEach((d, j) => { d.classList.toggle('is-done', j < i); if (j === i) d.setAttribute('aria-current', 'step'); else d.removeAttribute('aria-current'); });
    root.dataset.step = i + 1;
    next.textContent = i === steps.length - 1 ? 'Submit application' : 'Continue';
    if (i === steps.length - 1) {
      const v = (id) => root.querySelector(id).value;
      root.querySelector('[data-review="name"]').textContent = v('#frm-08-fn') + ' ' + v('#frm-08-ln');
      root.querySelector('[data-review="email"]').textContent = v('#frm-08-em');
      root.querySelector('[data-review="cv"]').textContent = cv.files[0] ? cv.files[0].name : '—';
    }
    steps[i].querySelector('legend').focus();
  };
  next.addEventListener('click', () => {
    const bad = [...steps[i].querySelectorAll('input, select, textarea')].find((f) => !f.checkValidity());
    if (bad) { if (bad === cv) { msg.textContent = 'Please upload your résumé to continue.'; cv.focus(); } else bad.reportValidity(); return; }
    if (i < steps.length - 1) return show(i + 1);
    steps.forEach((s) => { s.hidden = true; });
    dots.forEach((d) => { d.classList.add('is-done'); d.removeAttribute('aria-current'); });
    root.classList.add('is-sent');
    const done = root.querySelector('.frm-08__done'); done.hidden = false; done.focus();
  });
  back.addEventListener('click', () => { if (i > 0) show(i - 1); });
  cv.addEventListener('change', () => {
    const f = cv.files[0]; msg.textContent = '';
    if (!f) return;
    if (f.size > MAX_MB * 1048576 || !/\.(pdf|docx?)$/i.test(f.name)) {
      msg.textContent = f.name + ' isn\'t a PDF/DOC under ' + MAX_MB + ' MB.'; cv.value = ''; return;
    }
    root.querySelector('.frm-08__fname').textContent = f.name;
    root.querySelector('.frm-08__fsize').textContent = (f.size / 1024).toFixed(0) + ' KB · ready to send';
    root.querySelector('.frm-08__ficon').textContent = f.name.split('.').pop().toUpperCase();
  });
  root.querySelector('.frm-08__rm').addEventListener('click', () => { cv.value = ''; cv.focus(); });
  const start = root.querySelector('#frm-08-start'); start.min = new Date().toISOString().slice(0, 10);
})();
```
