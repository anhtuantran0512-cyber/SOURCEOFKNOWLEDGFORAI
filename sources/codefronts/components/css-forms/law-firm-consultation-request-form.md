---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/law-firm-consultation-request-form/"
title: "Law Firm Consultation Request Form"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A consultation request with the gravitas a law firm needs: an attorney profile with credentials beside a calm, editorial form."
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Law Firm Consultation Request Form
Source: https://codefronts.com/components/css-forms/law-firm-consultation-request-form/

A consultation request with the gravitas a law firm needs: an attorney profile with credentials beside a calm, editorial form. Practice-area cards, preferred contact method, an urgent-deadline toggle that reveals a court-date field, an opposing-party field for conflict checks, availability chips, a confidentiality note placed exactly where people hesitate, and the required “no attorney–client relationship” acknowledgement.
## HTML
```html
<div class="frm-17">
  <button type="button" class="frm-17__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-17__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-17__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-17__stage">
    <div class="frm-17__wrap">
      <div class="frm-17__card">
        <aside class="frm-17__aside">
          <p class="frm-17__firm">Whitcombe &amp; Hale <span>LLP</span></p>
          <figure class="frm-17__atty">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=480&fit=crop&crop=faces&auto=format&q=75" width="400" height="480" alt="Portrait of managing partner Daniel Hale" loading="lazy" decoding="async">
            <figcaption><b>Daniel Hale</b><span>Managing Partner</span></figcaption>
          </figure>
          <blockquote>“You'll speak with an attorney — not a call centre — within one business day.”</blockquote>
          <ul class="frm-17__creds"><li>Admitted in NY, NJ &amp; CA</li><li>27 years in practice</li><li>Free, confidential 30-min consultation</li></ul>
        </aside>
        <div class="frm-17__form" role="form" aria-labelledby="frm-17-title">
          <h2 id="frm-17-title">Request a consultation</h2>
          <p class="frm-17__lede">Tell us briefly what's happening. Everything you share is kept strictly confidential.</p>
          <div class="frm-17__grid">
            <div class="frm-17__field"><label for="frm-17-n">Full name</label><input id="frm-17-n" autocomplete="name" required></div>
            <div class="frm-17__field"><label for="frm-17-e">Email</label><input id="frm-17-e" type="email" autocomplete="email" required></div>
            <div class="frm-17__field"><label for="frm-17-p">Phone</label><input id="frm-17-p" type="tel" autocomplete="tel" required></div>
            <div class="frm-17__field"><label for="frm-17-st">State / jurisdiction</label><select id="frm-17-st"><option>New York</option><option>New Jersey</option><option>California</option><option>Other</option></select></div>
          </div>
          <fieldset class="frm-17__areas"><legend>Practice area</legend>
            <label><input type="radio" name="frm-17-a" value="family" required><span><b>Family &amp; divorce</b><small>Custody, separation, support</small></span></label>
            <label><input type="radio" name="frm-17-a" value="employment"><span><b>Employment</b><small>Dismissal, discrimination, contracts</small></span></label>
            <label><input type="radio" name="frm-17-a" value="injury"><span><b>Personal injury</b><small>Accidents, medical negligence</small></span></label>
            <label><input type="radio" name="frm-17-a" value="estate"><span><b>Wills &amp; estates</b><small>Probate, trusts, disputes</small></span></label>
            <label><input type="radio" name="frm-17-a" value="business"><span><b>Business</b><small>Formation, disputes, M&amp;A</small></span></label>
            <label><input type="radio" name="frm-17-a" value="immigration"><span><b>Immigration</b><small>Visas, green cards, appeals</small></span></label>
          </fieldset>
          <div class="frm-17__urgent">
            <label class="frm-17__switch"><input type="checkbox" id="frm-17-urg" role="switch"><i aria-hidden="true"></i><span>I have a court date or legal deadline</span></label>
            <div class="frm-17__court"><label for="frm-17-cd">Date of hearing or deadline</label><input id="frm-17-cd" type="date"></div>
          </div>
          <div class="frm-17__field"><label for="frm-17-op">Other party's name <span class="frm-17__opt">For our conflict check</span></label><input id="frm-17-op" placeholder="Person or company, if any"></div>
          <div class="frm-17__field">
            <p class="frm-17__conf"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>Protected and confidential. Share only a brief outline — details can wait for the call.</p>
            <div class="frm-17__lr"><label for="frm-17-sum">Brief summary of your matter</label><span class="frm-17__wc" aria-hidden="true">0 words</span></div>
            <textarea id="frm-17-sum" rows="4" required aria-describedby="frm-17-wc-live"></textarea>
            <p class="frm-17__sr" id="frm-17-wc-live" aria-live="polite"></p>
          </div>
          <fieldset class="frm-17__chips"><legend>Best time to reach you</legend>
            <label><input type="checkbox" checked><span>Morning</span></label><label><input type="checkbox"><span>Afternoon</span></label><label><input type="checkbox"><span>Evening</span></label>
            <label><input type="radio" name="frm-17-via" value="phone" checked><span>By phone</span></label><label><input type="radio" name="frm-17-via" value="video"><span>Video call</span></label><label><input type="radio" name="frm-17-via" value="email"><span>Email</span></label>
          </fieldset>
          <label class="frm-17__ack"><input type="checkbox" required><span>I understand that submitting this form does not create an attorney–client relationship.</span></label>
          <button type="button" class="frm-17__send">Request my consultation</button>
          <div class="frm-17__done" hidden tabindex="-1"><b>Request received</b><p>Your reference is <strong class="frm-17__ref"></strong>. An attorney will contact you within one business day.</p></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Public+Sans:wght@400;500;600&display=swap');

.frm-17 {
  --bg: #ebe8df;
  --card: #fdfbf6;
  --ink: #1b211d;
  --muted: #5f665f;
  --line: #e1dccf;
  --soft: #f6f3ec;
  --accent: #1f4a3a;
  --on-accent: #f8f4ea;
  --brass: #a8834a;
  --bad: #a3271b;
  --serif: "Newsreader",ui-serif,Georgia,serif;
  --sans: "Public Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
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
  .frm-17:not([data-theme="light"]) {
    --bg: #0e1210;
    --card: #151a17;
    --ink: #ece8de;
    --muted: #a3a99f;
    --line: #29302b;
    --soft: #1a201c;
    --accent: #8cc5ad;
    --on-accent: #0b1c15;
    --brass: #d1ab6e;
    --bad: #ff8a7a;
  }
}

.frm-17[data-theme="dark"] {
  --bg: #0e1210;
  --card: #151a17;
  --ink: #ece8de;
  --muted: #a3a99f;
  --line: #29302b;
  --soft: #1a201c;
  --accent: #8cc5ad;
  --on-accent: #0b1c15;
  --brass: #d1ab6e;
  --bad: #ff8a7a;
}

.frm-17,
.frm-17 *,
.frm-17 *::before,
.frm-17 *::after {
  box-sizing: border-box;
}

.frm-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3.5rem);
}

.frm-17__wrap {
  width: 100%;
  max-width: 66rem;
  container-type: inline-size;
}

.frm-17__card {
  display: grid;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: .75rem;
  overflow: hidden;
  box-shadow: 0 40px 80px -45px rgba(20,30,25,.5);
}

@container (min-width: 52rem) {
  .frm-17__card {
    grid-template-columns: 19rem minmax(0,1fr);
  }
}

.frm-17__aside {
  display: grid;
  align-content: start;
  gap: 1.25rem;
  padding: clamp(1.25rem,4cqi,2.25rem);
  background: #183a2e;
  color: #efe9da;
}

.frm-17[data-theme="dark"] .frm-17__aside {
  background: #0f241c;
}

.frm-17__firm {
  margin: 0;
  font: 500 1.35rem var(--serif);
  letter-spacing: .01em;
}

.frm-17__firm span {
  font-size: .75rem;
  letter-spacing: .2em;
  color: var(--brass);
  margin-left: .3rem;
}

.frm-17__atty {
  margin: 0;
  display: grid;
  gap: .7rem;
}

.frm-17__atty img {
  width: 100%;
  max-width: 15rem;
  aspect-ratio: 5/6;
  height: auto;
  object-fit: cover;
  border-radius: .35rem;
  background: #2a4a3e;
  filter: grayscale(.25) contrast(1.05);
  box-shadow: 0 0 0 1px rgba(255,255,255,.08), .5rem .5rem 0 -.1rem color-mix(in oklab,var(--brass) 40%,transparent);
}

@container (max-width: 51.99rem) {
  .frm-17__atty {
    grid-template-columns: 5rem 1fr;
    align-items: center;
  }

  .frm-17__atty img {
    width: 5rem;
    aspect-ratio: 1;
    border-radius: 50%;
    box-shadow: none;
  }
}

.frm-17__atty figcaption {
  display: grid;
}

.frm-17__atty b {
  font: 500 1.15rem var(--serif);
}

.frm-17__atty span {
  font-size: .8rem;
  color: #b9c4bc;
}

.frm-17 blockquote {
  margin: 0;
  font: italic 400 1.1rem/1.45 var(--serif);
  color: #f4ecd8;
  border-left: 2px solid var(--brass);
  padding-left: 1rem;
}

.frm-17__creds {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .5rem;
  font-size: .85rem;
  color: #cbd4cd;
}

.frm-17__creds li {
  display: flex;
  gap: .55rem;
}

.frm-17__creds li::before {
  content: '§';
  color: var(--brass);
  font-family: var(--serif);
}

.frm-17__form {
  display: grid;
  gap: 1.2rem;
  align-content: start;
  padding: clamp(1.25rem,4cqi,2.5rem);
}

.frm-17 h2 {
  margin: 0;
  font: 400 clamp(1.8rem,4.5cqi,2.5rem)/1.05 var(--serif);
  letter-spacing: -.01em;
}

.frm-17__lede {
  margin: -.6rem 0 0;
  color: var(--muted);
  line-height: 1.55;
}

.frm-17__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
}

.frm-17__field {
  display: grid;
  gap: .4rem;
}

.frm-17 label,
.frm-17 legend {
  font-size: .84rem;
  font-weight: 600;
}

.frm-17__opt {
  font-weight: 400;
  color: var(--muted);
}

.frm-17 input:not([type="radio"]):not([type="checkbox"]),
.frm-17 select,
.frm-17 textarea {
  width: 100%;
  min-height: 2.9rem;
  padding: .6rem .85rem;
  border-radius: .35rem;
  border: 1px solid var(--line);
  background: var(--soft);
  color: var(--ink);
  font: inherit;
  font-size: .97rem;
  transition: border-color .2s, box-shadow .2s;
}

.frm-17 textarea {
  resize: vertical;
  line-height: 1.55;
}

.frm-17 :is(input,select,textarea):focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 20%,transparent);
}

.frm-17 :user-invalid:not(fieldset) {
  border-color: var(--bad);
}

.frm-17 fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
}

.frm-17 legend {
  padding: 0;
  margin-bottom: .6rem;
}

.frm-17__areas {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,14rem),1fr));
  gap: .5rem;
}

.frm-17__areas legend {
  grid-column: 1/-1;
}

.frm-17__areas label,
.frm-17__chips label {
  position: relative;
}

.frm-17__areas input,
.frm-17__chips input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-17__areas span {
  display: grid;
  gap: .1rem;
  padding: .8rem 2.6rem .8rem .95rem;
  border: 1px solid var(--line);
  border-radius: .4rem;
  position: relative;
  transition: border-color .2s, background .2s;
}

.frm-17__areas b {
  font: 500 1.02rem var(--serif);
}

.frm-17__areas small {
  font-size: .78rem;
  color: var(--muted);
}

.frm-17__areas span::after {
  content: '';
  position: absolute;
  right: .95rem;
  top: 50%;
  width: .45rem;
  height: .85rem;
  margin-top: -.55rem;
  border-right: 2px solid var(--accent);
  border-bottom: 2px solid var(--accent);
  rotate: 45deg;
  scale: 0;
  transition: scale .3s var(--ease);
}

.frm-17__areas label:hover span {
  border-color: var(--muted);
}

.frm-17__areas label:has(:checked) span {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 6%,var(--card));
}

.frm-17__areas label:has(:checked) span::after {
  scale: 1;
}

.frm-17__areas input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.frm-17__urgent {
  display: grid;
  gap: .8rem;
  padding: .9rem 1rem;
  border-radius: .4rem;
  border: 1px dashed color-mix(in oklab,var(--brass) 60%,var(--line));
  background: color-mix(in oklab,var(--brass) 5%,var(--card));
}

.frm-17__switch {
  display: flex;
  align-items: center;
  gap: .75rem;
  cursor: pointer;
  position: relative;
  min-height: 2.5rem;
}

.frm-17__switch input {
  position: absolute;
  opacity: 0;
  width: 2.6rem;
  height: 1.5rem;
  margin: 0;
  cursor: pointer;
}

.frm-17__switch i {
  flex: none;
  width: 2.6rem;
  height: 1.5rem;
  border-radius: 99px;
  background: var(--line);
  position: relative;
  transition: background .25s;
}

.frm-17__switch i::after {
  content: '';
  position: absolute;
  top: .15rem;
  left: .15rem;
  width: 1.2rem;
  height: 1.2rem;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0,0,0,.3);
  transition: translate .35s var(--ease);
}

.frm-17__switch input:checked + i {
  background: var(--brass);
}

.frm-17__switch input:checked + i::after {
  translate: 1.1rem 0;
}

.frm-17__switch input:focus-visible + i {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.frm-17__court {
  display: none;
  gap: .4rem;
}

.frm-17__urgent:has(:checked) .frm-17__court {
  display: grid;
  animation: frm-17-in .35s var(--ease);
}

@keyframes frm-17-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }
}

.frm-17__conf {
  display: flex;
  align-items: center;
  gap: .55rem;
  margin: 0 0 .35rem;
  font-size: .82rem;
  color: var(--accent);
}

.frm-17__conf svg {
  width: 1.05rem;
  height: 1.05rem;
  flex: none;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
}

.frm-17__lr {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.frm-17__wc {
  font-size: .78rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.frm-17__wc.is-long {
  color: var(--brass);
  font-weight: 600;
}

.frm-17__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}

.frm-17__chips legend {
  width: 100%;
}

.frm-17__chips label:nth-of-type(4) {
  margin-left: auto;
}

.frm-17__chips span {
  display: inline-flex;
  align-items: center;
  min-height: 2.5rem;
  padding: 0 .95rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  font-size: .85rem;
  transition: all .2s;
}

.frm-17__chips input:checked + span {
  background: var(--accent);
  border-color: var(--accent);
  color: var(--on-accent);
}

.frm-17__chips input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 36rem) {
  .frm-17__chips label:nth-of-type(4) {
    margin-left: 0;
  }
}

.frm-17__ack {
  display: flex;
  gap: .65rem;
  align-items: flex-start;
  font-weight: 400 !important;
  color: var(--muted);
  line-height: 1.45;
  cursor: pointer;
}

.frm-17__ack input {
  flex: none;
  width: 1.15rem;
  height: 1.15rem;
  margin: .12rem 0 0;
  accent-color: var(--accent);
}

.frm-17__send {
  min-height: 3.2rem;
  border: 0;
  border-radius: .35rem;
  cursor: pointer;
  font: inherit;
  font-weight: 600;
  font-size: 1rem;
  letter-spacing: .02em;
  color: var(--on-accent);
  background: var(--accent);
  box-shadow: inset 0 -3px 0 color-mix(in oklab,black 25%,transparent);
  transition: filter .2s, translate .2s var(--ease);
}

.frm-17__send:hover {
  filter: brightness(1.12);
  translate: 0 -1px;
}

.frm-17__send:focus-visible {
  outline: 2px solid var(--brass);
  outline-offset: 3px;
}

.frm-17__done {
  outline: none;
  padding: 1rem 1.1rem;
  border-left: 3px solid var(--brass);
  background: var(--soft);
  animation: frm-17-in .4s var(--ease);
}

.frm-17__done[hidden] {
  display: none;
}

.frm-17__done b {
  font: 500 1.2rem var(--serif);
}

.frm-17__done p {
  margin: .3rem 0 0;
  color: var(--muted);
}

.frm-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-17 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-17__areas label:has(:checked) span {
    outline: 2px solid Highlight;
  }

  .frm-17__chips input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-17__send {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-17 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-17__theme {
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

.frm-17__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-17__theme:active {
  transform: scale(.94);
}

.frm-17__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-17__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-17__theme .frm-17__sun,
.frm-17__theme[aria-pressed="true"] .frm-17__moon {
  display: none;
}

.frm-17__theme[aria-pressed="true"] .frm-17__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-17__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-17__theme {
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
  document.querySelectorAll('.frm-17').forEach((root) => {
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
  const root = document.querySelector('.frm-17');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const WORDS = 250;
  const urg = $('#frm-17-urg'), court = $('#frm-17-cd');
  court.min = new Date().toISOString().slice(0, 10);
  urg.addEventListener('change', () => { court.required = urg.checked; if (urg.checked) court.focus(); });
  const sum = $('#frm-17-sum'), wc = $('.frm-17__wc'), live = $('#frm-17-wc-live');
  let warned = false;
  sum.addEventListener('input', () => {
    const n = (sum.value.trim().match(/\S+/g) || []).length, long = n > WORDS;
    wc.textContent = n + ' word' + (n === 1 ? '' : 's') + (long ? ' — feel free to save details for the call' : '');
    wc.classList.toggle('is-long', long);
    if (long !== warned) { live.textContent = long ? 'Over ' + WORDS + ' words. You can share more details on the call.' : ''; warned = long; }
  });
  $('.frm-17__send').addEventListener('click', () => {
    const bad = [...root.querySelectorAll('[required]')].find((f) => f.type === 'radio' ? !root.querySelector('[name="' + f.name + '"]:checked') : !f.checkValidity());
    if (bad) { bad.focus(); if (bad.reportValidity) bad.reportValidity(); return; }
    $('.frm-17__ref').textContent = 'WH-' + new Date().getFullYear() + '-' + String(Math.floor(Math.random() * 90000) + 10000);
    const done = $('.frm-17__done'); done.hidden = false; $('.frm-17__send').hidden = true; done.focus();
  });
})();
```
