---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/insurance-quote-request-form/"
title: "Insurance Quote Request Form"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A three-step lead-gen quote form built for conversion: big icon radio cards to pick coverage (Auto, Home, Life, Renters), a details step whose questions…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Insurance Quote Request Form
Source: https://codefronts.com/components/css-forms/insurance-quote-request-form/

A three-step lead-gen quote form built for conversion: big icon radio cards to pick coverage (Auto, Home, Life, Renters), a details step whose questions change based on that choice, a coverage-level slider, and a sticky live estimate that recalculates a monthly price range as you go. A segmented progress bar, Back/Next with per-step validation, and a clear privacy promise right where people hesitate.
## HTML
```html
<div class="frm-12" data-step="1">
  <button type="button" class="frm-12__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-12__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-12__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-12__stage">
    <div class="frm-12__wrap">
      <div class="frm-12__card">
        <div class="frm-12__main" role="form" aria-labelledby="frm-12-title">
          <p class="frm-12__eyebrow">Free quote · 2 minutes</p>
          <h2 id="frm-12-title">Let's find you better coverage</h2>
          <div class="frm-12__prog" aria-hidden="true"><i></i><i></i><i></i></div>
          <p class="frm-12__stepname" aria-live="polite">Step 1 of 3 · Coverage</p>
          <fieldset class="frm-12__step" data-i="1">
            <legend class="frm-12__sr">What would you like to insure?</legend>
            <div class="frm-12__types">
              <label><input type="radio" name="frm-12-type" value="auto" checked><span><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M5 20v-4l3-6h16l3 6v4"/><rect x="3" y="16" width="26" height="6" rx="2"/><circle cx="9" cy="23" r="2.5"/><circle cx="23" cy="23" r="2.5"/></svg><b>Auto</b><small>Cars &amp; motorbikes</small></span></label>
              <label><input type="radio" name="frm-12-type" value="home"><span><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M4 15 16 5l12 10"/><path d="M7 13v13h18V13"/><path d="M13 26v-7h6v7"/></svg><b>Home</b><small>Buildings &amp; contents</small></span></label>
              <label><input type="radio" name="frm-12-type" value="life"><span><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 27s-10-6-10-14a5.5 5.5 0 0 1 10-3 5.5 5.5 0 0 1 10 3c0 8-10 14-10 14Z"/><path d="M9 16h4l2-3 2 6 2-3h4"/></svg><b>Life</b><small>Term &amp; whole life</small></span></label>
              <label><input type="radio" name="frm-12-type" value="renters"><span><svg viewBox="0 0 32 32" aria-hidden="true"><rect x="6" y="4" width="20" height="24" rx="2"/><path d="M11 9h3M18 9h3M11 14h3M18 14h3M11 19h3M18 19h3M14 28v-4h4v4"/></svg><b>Renters</b><small>Your belongings</small></span></label>
            </div>
          </fieldset>
          <fieldset class="frm-12__step" data-i="2" hidden>
            <legend class="frm-12__sr">Tell us a little more</legend>
            <div class="frm-12__grid">
              <div class="frm-12__field"><label for="frm-12-zip">ZIP / postcode</label><input id="frm-12-zip" autocomplete="postal-code" required placeholder="10001"></div>
              <div class="frm-12__field"><label for="frm-12-age">Your age</label><select id="frm-12-age" required><option value="">Select</option><option value="1.35">18–24</option><option value="1.1">25–34</option><option value="1" selected>35–49</option><option value="1.05">50–64</option><option value="1.3">65+</option></select></div>
            </div>
            <div class="frm-12__cond frm-12__cond--auto frm-12__grid">
              <div class="frm-12__field"><label for="frm-12-yr">Vehicle year</label><input id="frm-12-yr" type="number" min="1990" max="2027" value="2022" required></div>
              <div class="frm-12__field"><label for="frm-12-mi">Annual mileage</label><select id="frm-12-mi"><option>Under 7,500</option><option selected>7,500–12,000</option><option>12,000+</option></select></div>
            </div>
            <div class="frm-12__cond frm-12__cond--home frm-12__grid">
              <div class="frm-12__field"><label for="frm-12-hv">Rebuild value ($)</label><input id="frm-12-hv" type="number" min="50000" step="10000" value="350000" required></div>
              <div class="frm-12__field"><label for="frm-12-built">Year built</label><input id="frm-12-built" type="number" min="1800" max="2027" value="1998"></div>
            </div>
            <div class="frm-12__cond frm-12__cond--life frm-12__grid">
              <div class="frm-12__field"><label for="frm-12-term">Term length</label><select id="frm-12-term"><option>10 years</option><option selected>20 years</option><option>30 years</option></select></div>
              <div class="frm-12__field"><label for="frm-12-smk">Tobacco use in last 12 months?</label><select id="frm-12-smk"><option>No</option><option>Yes</option></select></div>
            </div>
            <div class="frm-12__cond frm-12__cond--renters frm-12__grid">
              <div class="frm-12__field"><label for="frm-12-cv">Contents value ($)</label><input id="frm-12-cv" type="number" min="5000" step="1000" value="25000" required></div>
            </div>
            <div class="frm-12__field">
              <div class="frm-12__lr"><label for="frm-12-level">Coverage level</label><output for="frm-12-level" class="frm-12__lvl">Standard</output></div>
              <input id="frm-12-level" type="range" min="1" max="3" step="1" value="2" aria-valuetext="Standard">
              <div class="frm-12__ticks" aria-hidden="true"><span>Basic</span><span>Standard</span><span>Premium</span></div>
            </div>
          </fieldset>
          <fieldset class="frm-12__step" data-i="3" hidden>
            <legend class="frm-12__sr">Where should we send your quote?</legend>
            <div class="frm-12__grid">
              <div class="frm-12__field"><label for="frm-12-n">Full name</label><input id="frm-12-n" autocomplete="name" required></div>
              <div class="frm-12__field"><label for="frm-12-e">Email</label><input id="frm-12-e" type="email" autocomplete="email" required></div>
            </div>
            <div class="frm-12__field"><label for="frm-12-p">Phone <span class="frm-12__opt">Optional — only if you'd like a call</span></label><input id="frm-12-p" type="tel" autocomplete="tel"></div>
            <label class="frm-12__consent"><input type="checkbox" required><span>I agree to be contacted about my quote. No spam, and we never sell your data.</span></label>
          </fieldset>
          <div class="frm-12__done" hidden tabindex="-1"><h3>Your quote is on its way</h3><p>We've emailed your personalised quote. A licensed advisor is available if you have questions.</p></div>
          <div class="frm-12__nav">
            <button type="button" class="frm-12__back">Back</button>
            <button type="button" class="frm-12__next">Continue<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
          </div>
        </div>
        <aside class="frm-12__est" aria-labelledby="frm-12-est-h">
          <p id="frm-12-est-h" class="frm-12__estlabel">Estimated premium</p>
          <p class="frm-12__price" aria-live="polite"><b class="frm-12__lo">$0</b>–<b class="frm-12__hi">$0</b><small>/mo</small></p>
          <ul class="frm-12__perks"><li>No obligation, no credit check</li><li>Compare 12+ A-rated insurers</li><li>Switch and save in minutes</li></ul>
          <p class="frm-12__disc">Indicative only. Your final price depends on underwriting.</p>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@400;500;600;700;800&display=swap');

.frm-12 {
  --bg: #eef3fa;
  --card: #ffffff;
  --ink: #0b1b33;
  --muted: #5a6a82;
  --line: #dde5f0;
  --soft: #f5f8fc;
  --accent: #1d5bd8;
  --on-accent: #fff;
  --sky: #7cc4ff;
  --ok: #0f9d6b;
  --sans: "Red Hat Display",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
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
  .frm-12:not([data-theme="light"]) {
    --bg: #07101e;
    --card: #0d1a2d;
    --ink: #e6eefb;
    --muted: #93a3bd;
    --line: #1d2d46;
    --soft: #112138;
    --accent: #5b8cff;
    --on-accent: #04122e;
    --sky: #7cc4ff;
    --ok: #34d399;
  }
}

.frm-12[data-theme="dark"] {
  --bg: #07101e;
  --card: #0d1a2d;
  --ink: #e6eefb;
  --muted: #93a3bd;
  --line: #1d2d46;
  --soft: #112138;
  --accent: #5b8cff;
  --on-accent: #04122e;
  --sky: #7cc4ff;
  --ok: #34d399;
}

.frm-12,
.frm-12 *,
.frm-12 *::before,
.frm-12 *::after {
  box-sizing: border-box;
}

.frm-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3.5rem);
}

.frm-12__wrap {
  width: 100%;
  max-width: 62rem;
  container-type: inline-size;
}

.frm-12__card {
  display: grid;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 40px 80px -45px rgba(11,27,51,.45);
}

@container (min-width: 50rem) {
  .frm-12__card {
    grid-template-columns: minmax(0,1fr) 18rem;
  }
}

.frm-12__main {
  display: grid;
  gap: 1.1rem;
  align-content: start;
  padding: clamp(1.25rem,4cqi,2.5rem);
}

.frm-12__eyebrow {
  margin: 0;
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
}

.frm-12 h2 {
  margin: -.4rem 0 0;
  font-size: clamp(1.5rem,4cqi,2.1rem);
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1.1;
}

.frm-12__prog {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .35rem;
}

.frm-12__prog i {
  height: .35rem;
  border-radius: 99px;
  background: var(--line);
  position: relative;
  overflow: hidden;
}

.frm-12__prog i::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--accent);
  scale: 0 1;
  transform-origin: left;
  transition: scale .6s var(--ease);
}

.frm-12__prog i:first-child::after,
.frm-12[data-step="2"] .frm-12__prog i:nth-child(-n+2)::after,
.frm-12[data-step="3"] .frm-12__prog i::after,
.frm-12[data-step="4"] .frm-12__prog i::after {
  scale: 1 1;
}

.frm-12__stepname {
  margin: -.5rem 0 0;
  font-size: .85rem;
  font-weight: 600;
  color: var(--muted);
}

.frm-12__step {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
  display: grid;
  gap: 1rem;
  animation: frm-12-in .45s var(--ease);
}

.frm-12__step[hidden] {
  display: none;
}

@keyframes frm-12-in {
  from {
    opacity: 0;
    translate: 0 10px;
  }
}

.frm-12__types {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,9rem),1fr));
  gap: .7rem;
}

.frm-12__types label {
  position: relative;
}

.frm-12__types input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
  z-index: 1;
}

.frm-12__types span {
  display: grid;
  justify-items: start;
  gap: .15rem;
  padding: 1.1rem;
  border-radius: 1.1rem;
  border: 1.5px solid var(--line);
  background: var(--soft);
  transition: all .25s var(--ease);
}

.frm-12__types svg {
  width: 2.25rem;
  height: 2.25rem;
  margin-bottom: .6rem;
  fill: none;
  stroke: var(--muted);
  stroke-width: 1.6;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: stroke .25s, translate .35s var(--ease);
}

.frm-12__types b {
  font-weight: 700;
}

.frm-12__types small {
  font-size: .78rem;
  color: var(--muted);
}

.frm-12__types label:hover span {
  border-color: color-mix(in oklab,var(--accent) 40%,var(--line));
}

.frm-12__types label:hover svg {
  translate: 0 -2px;
}

.frm-12__types input:checked + span {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 7%,var(--card));
  box-shadow: 0 12px 24px -16px var(--accent);
}

.frm-12__types input:checked + span svg {
  stroke: var(--accent);
}

.frm-12__types input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.frm-12__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,12rem),1fr));
}

.frm-12__cond {
  display: none;
}

.frm-12:has([value="auto"]:checked) .frm-12__cond--auto,
.frm-12:has([value="home"]:checked) .frm-12__cond--home,
.frm-12:has([value="life"]:checked) .frm-12__cond--life,
.frm-12:has([value="renters"]:checked) .frm-12__cond--renters {
  display: grid;
}

.frm-12__field {
  display: grid;
  gap: .4rem;
}

.frm-12 label {
  font-size: .86rem;
  font-weight: 600;
}

.frm-12__opt {
  font-weight: 400;
  color: var(--muted);
}

.frm-12 input:is([type="text"],:not([type]),[type="email"],[type="tel"],[type="number"]),
.frm-12 select {
  width: 100%;
  min-height: 3rem;
  padding: .65rem .9rem;
  border-radius: .75rem;
  border: 1px solid var(--line);
  background: var(--soft);
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  transition: border-color .2s, box-shadow .2s;
}

.frm-12 :is(input,select):focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 18%,transparent);
}

.frm-12 :user-invalid {
  border-color: #dc2626;
}

.frm-12__lr {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.frm-12__lvl {
  font-weight: 700;
  color: var(--accent);
  font-size: .9rem;
}

.frm-12 input[type="range"] {
  --fill: 50%;
  appearance: none;
  -webkit-appearance: none;
  width: 100%;
  height: 2.75rem;
  background: transparent;
  cursor: pointer;
}

.frm-12 input[type="range"]::-webkit-slider-runnable-track {
  height: .45rem;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent) var(--fill),var(--line) var(--fill));
}

.frm-12 input[type="range"]::-moz-range-track {
  height: .45rem;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent) var(--fill),var(--line) var(--fill));
}

.frm-12 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 1.5rem;
  height: 1.5rem;
  margin-top: -.53rem;
  border-radius: 50%;
  background: var(--card);
  border: 3px solid var(--accent);
  box-shadow: 0 4px 10px -3px var(--accent);
  transition: scale .2s var(--ease);
}

.frm-12 input[type="range"]::-moz-range-thumb {
  width: 1.2rem;
  height: 1.2rem;
  border-radius: 50%;
  background: var(--card);
  border: 3px solid var(--accent);
}

.frm-12 input[type="range"]:active::-webkit-slider-thumb {
  scale: 1.15;
}

.frm-12 input[type="range"]:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .5rem;
}

.frm-12__ticks {
  display: flex;
  justify-content: space-between;
  font-size: .75rem;
  color: var(--muted);
  margin-top: -.4rem;
}

.frm-12__consent {
  display: flex;
  gap: .65rem;
  align-items: flex-start;
  font-weight: 400 !important;
  color: var(--muted);
  line-height: 1.45;
  cursor: pointer;
}

.frm-12__consent input {
  flex: none;
  width: 1.15rem;
  height: 1.15rem;
  margin: .12rem 0 0;
  accent-color: var(--accent);
}

.frm-12__nav {
  display: flex;
  justify-content: space-between;
  gap: .75rem;
  padding-top: .5rem;
}

.frm-12__back,
.frm-12__next {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-height: 3.1rem;
  padding: 0 1.4rem;
  border-radius: .85rem;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
  transition: translate .2s var(--ease), filter .2s, background .2s;
}

.frm-12__back {
  border: 1px solid var(--line);
  background: transparent;
  color: var(--ink);
}

.frm-12__back:hover {
  background: var(--soft);
}

.frm-12[data-step="1"] .frm-12__back,
.frm-12[data-step="4"] .frm-12__nav {
  visibility: hidden;
}

.frm-12[data-step="4"] .frm-12__nav {
  display: none;
}

.frm-12__next {
  margin-left: auto;
  border: 0;
  background: var(--accent);
  color: var(--on-accent);
  box-shadow: 0 12px 24px -12px var(--accent);
}

.frm-12__next svg {
  width: 1.1rem;
  height: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: translate .3s var(--ease);
}

.frm-12__next:hover {
  translate: 0 -2px;
}

.frm-12__next:hover svg {
  translate: 3px 0;
}

.frm-12__back:focus-visible,
.frm-12__next:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-12__done {
  outline: none;
  padding: 1rem 1.25rem;
  border-radius: 1rem;
  background: color-mix(in oklab,var(--ok) 10%,var(--card));
  border: 1px solid color-mix(in oklab,var(--ok) 35%,transparent);
  animation: frm-12-in .45s var(--ease);
}

.frm-12__done[hidden] {
  display: none;
}

.frm-12__done h3 {
  margin: 0 0 .3rem;
  color: var(--ok);
}

.frm-12__done p {
  margin: 0;
  color: var(--muted);
}

.frm-12__est {
  position: relative;
  display: grid;
  align-content: start;
  gap: 1rem;
  padding: clamp(1.25rem,4cqi,2.25rem);
  color: #eaf2ff;
  background: radial-gradient(20rem 16rem at 100% 0%, color-mix(in oklab,var(--sky) 45%,transparent), transparent 70%), linear-gradient(160deg,#0f2f6b,#0a1a3a);
  overflow: hidden;
}

.frm-12__est::after {
  content: '';
  position: absolute;
  right: -3rem;
  bottom: -3rem;
  width: 10rem;
  height: 10rem;
  border-radius: 50%;
  border: 1.5rem solid rgba(255,255,255,.05);
}

.frm-12__estlabel {
  margin: 0;
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  opacity: .75;
}

.frm-12__price {
  margin: 0;
  font-size: clamp(2rem,6cqi,2.6rem);
  font-weight: 800;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

.frm-12__price small {
  font-size: 1rem;
  font-weight: 500;
  opacity: .7;
  margin-left: .2rem;
}

.frm-12__perks {
  list-style: none;
  margin: 0;
  padding: 1rem 0 0;
  display: grid;
  gap: .55rem;
  border-top: 1px solid rgba(255,255,255,.12);
  font-size: .88rem;
}

.frm-12__perks li {
  display: flex;
  gap: .55rem;
}

.frm-12__perks li::before {
  content: '✓';
  color: var(--sky);
  font-weight: 800;
}

.frm-12__disc {
  margin: 0;
  font-size: .75rem;
  opacity: .65;
}

.frm-12__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-12 *,
    .frm-12 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-12__types input:checked + span {
    outline: 2px solid Highlight;
  }

  .frm-12__prog i::after {
    background: Highlight;
  }

  .frm-12__est {
    background: Canvas;
    color: CanvasText;
    border-left: 1px solid CanvasText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-12 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-12__theme {
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

.frm-12__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-12__theme:active {
  transform: scale(.94);
}

.frm-12__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-12__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-12__theme .frm-12__sun,
.frm-12__theme[aria-pressed="true"] .frm-12__moon {
  display: none;
}

.frm-12__theme[aria-pressed="true"] .frm-12__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-12__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-12__theme {
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
  document.querySelectorAll('.frm-12').forEach((root) => {
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
  const root = document.querySelector('.frm-12');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const steps = [...root.querySelectorAll('.frm-12__step')], names = ['Coverage', 'Details', 'Contact'];
  const BASE = { auto: 92, home: 68, life: 34, renters: 16 }, LEVEL = [0, .72, 1, 1.45], LVL_NAME = ['', 'Basic', 'Standard', 'Premium'];
  let i = 0, shown = [0, 0];
  const range = $('#frm-12-level');
  const type = () => $('[name="frm-12-type"]:checked').value;
  const syncCond = () => root.querySelectorAll('.frm-12__cond').forEach((c) => {
    const on = c.classList.contains('frm-12__cond--' + type());
    c.querySelectorAll('input, select').forEach((f) => { f.disabled = !on; });
  });
  const tween = (lo, hi) => {
    const from = shown.slice(), t0 = performance.now();
    const step = (t) => {
      const k = Math.min(1, (t - t0) / 450), e = 1 - Math.pow(1 - k, 3);
      $('.frm-12__lo').textContent = '$' + Math.round(from[0] + (lo - from[0]) * e);
      $('.frm-12__hi').textContent = '$' + Math.round(from[1] + (hi - from[1]) * e);
      if (k < 1) requestAnimationFrame(step); else shown = [lo, hi];
    };
    requestAnimationFrame(step);
  };
  const estimate = () => {
    const age = Number($('#frm-12-age').value) || 1, lvl = LEVEL[range.value], t = type();
    let base = BASE[t] * age * lvl;
    if (t === 'home') base *= (Number($('#frm-12-hv').value) || 350000) / 350000;
    if (t === 'renters') base *= (Number($('#frm-12-cv').value) || 25000) / 25000;
    if (t === 'life' && $('#frm-12-smk').value === 'Yes') base *= 2.1;
    if (t === 'auto') base *= Math.max(.8, 1 + (2022 - (Number($('#frm-12-yr').value) || 2022)) * -0.01);
    tween(Math.round(base * .88), Math.round(base * 1.18));
  };
  const setRange = () => {
    range.style.setProperty('--fill', ((range.value - 1) / 2) * 100 + '%');
    $('.frm-12__lvl').textContent = LVL_NAME[range.value]; range.setAttribute('aria-valuetext', LVL_NAME[range.value]);
  };
  const show = (n) => {
    i = n; steps.forEach((s, j) => { s.hidden = j !== i; });
    root.dataset.step = i + 1;
    $('.frm-12__stepname').textContent = 'Step ' + (i + 1) + ' of ' + steps.length + ' · ' + names[i];
    $('.frm-12__next').firstChild.textContent = i === steps.length - 1 ? 'Get my quote' : 'Continue';
    const first = steps[i].querySelector('input:not([disabled]), select:not([disabled])'); if (first) first.focus();
  };
  $('.frm-12__next').addEventListener('click', () => {
    const bad = [...steps[i].querySelectorAll('input, select')].find((f) => !f.disabled && !f.checkValidity());
    if (bad) { bad.reportValidity(); return; }
    if (i < steps.length - 1) return show(i + 1);
    steps.forEach((s) => { s.hidden = true; }); root.dataset.step = 4;
    $('.frm-12__stepname').textContent = 'Done';
    const d = $('.frm-12__done'); d.hidden = false; d.focus();
  });
  $('.frm-12__back').addEventListener('click', () => { if (i > 0) show(i - 1); });
  root.addEventListener('input', () => { setRange(); estimate(); });
  root.addEventListener('change', (e) => { if (e.target.name === 'frm-12-type') syncCond(); estimate(); });
  syncCond(); setRange(); estimate();
})();
```
