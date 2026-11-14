---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/nps-survey-form-with-follow-up-question/"
title: "NPS Survey Form with Follow-Up Question"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A Net Promoter Score survey with zero JavaScript."
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: NPS Survey Form with Follow-Up Question
Source: https://codefronts.com/components/css-forms/nps-survey-form-with-follow-up-question/

A Net Promoter Score survey with zero JavaScript. The 0–10 scale is eleven real radio buttons tinted along a red-amber-green ramp; choosing a score instantly reveals a different follow-up question for detractors (0–6), passives (7–8) and promoters (9–10) using :has(). A progress bar fills, the band label updates, and the thank-you state is driven by a checkbox — all declarative CSS.
## HTML
```html
<div class="frm-07">
  <button type="button" class="frm-07__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-07__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-07__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-07__stage">
    <div class="frm-07__card" role="form" aria-labelledby="frm-07-legend">
      <input type="checkbox" id="frm-07-sent" class="frm-07__sendbox" aria-label="Submit feedback">
      <div class="frm-07__survey">
        <div class="frm-07__top">
          <span class="frm-07__logo" aria-hidden="true">L</span>
          <span class="frm-07__step">Quick feedback · 30 seconds</span>
        </div>
        <div class="frm-07__progress" aria-hidden="true"><i></i></div>
        <fieldset class="frm-07__scalefs">
          <legend id="frm-07-legend">How likely are you to recommend Loop to a friend or colleague?</legend>
          <div class="frm-07__scale">
            <label style="--i:0"><input type="radio" name="frm-07-s" value="0" class="is-d"><span>0</span></label>
            <label style="--i:1"><input type="radio" name="frm-07-s" value="1" class="is-d"><span>1</span></label>
            <label style="--i:2"><input type="radio" name="frm-07-s" value="2" class="is-d"><span>2</span></label>
            <label style="--i:3"><input type="radio" name="frm-07-s" value="3" class="is-d"><span>3</span></label>
            <label style="--i:4"><input type="radio" name="frm-07-s" value="4" class="is-d"><span>4</span></label>
            <label style="--i:5"><input type="radio" name="frm-07-s" value="5" class="is-d"><span>5</span></label>
            <label style="--i:6"><input type="radio" name="frm-07-s" value="6" class="is-d"><span>6</span></label>
            <label style="--i:7"><input type="radio" name="frm-07-s" value="7" class="is-p"><span>7</span></label>
            <label style="--i:8"><input type="radio" name="frm-07-s" value="8" class="is-p"><span>8</span></label>
            <label style="--i:9"><input type="radio" name="frm-07-s" value="9" class="is-r"><span>9</span></label>
            <label style="--i:10"><input type="radio" name="frm-07-s" value="10" class="is-r"><span>10</span></label>
          </div>
          <div class="frm-07__ends" aria-hidden="true"><span>Not likely</span><span class="frm-07__band"></span><span>Extremely likely</span></div>
        </fieldset>
        <fieldset class="frm-07__q frm-07__q--d">
          <legend>We're sorry to hear that. What disappointed you most?</legend>
          <div class="frm-07__chips">
            <label><input type="checkbox"><span>Missing features</span></label>
            <label><input type="checkbox"><span>Too expensive</span></label>
            <label><input type="checkbox"><span>Bugs or slowness</span></label>
            <label><input type="checkbox"><span>Hard to learn</span></label>
            <label><input type="checkbox"><span>Support experience</span></label>
          </div>
          <label for="frm-07-d" class="frm-07__sub">What's one thing we should fix first?</label>
          <textarea id="frm-07-d" rows="3" placeholder="Be as blunt as you like — this goes straight to the product team."></textarea>
          <label class="frm-07__contact"><input type="checkbox"><span>It's OK to contact me about this</span></label>
        </fieldset>
        <fieldset class="frm-07__q frm-07__q--p">
          <legend>Thanks! What would make Loop a 10 for you?</legend>
          <label for="frm-07-p" class="frm-07__sub">One improvement, big or small</label>
          <textarea id="frm-07-p" rows="3" placeholder="e.g. Calendar sync, a better mobile app, cheaper team plans…"></textarea>
        </fieldset>
        <fieldset class="frm-07__q frm-07__q--r">
          <legend>Amazing. What do you love most about Loop?</legend>
          <div class="frm-07__chips">
            <label><input type="checkbox"><span>Speed</span></label>
            <label><input type="checkbox"><span>Design</span></label>
            <label><input type="checkbox"><span>Integrations</span></label>
            <label><input type="checkbox"><span>Support team</span></label>
          </div>
          <label for="frm-07-r" class="frm-07__sub">Mind if we quote you? <span>Optional</span></label>
          <textarea id="frm-07-r" rows="3" placeholder="A sentence we could share with other teams…"></textarea>
        </fieldset>
        <div class="frm-07__actions">
          <span class="frm-07__skip">You can skip any question.</span>
          <label for="frm-07-sent" class="frm-07__submit" aria-hidden="true">Send feedback</label>
        </div>
      </div>
      <div class="frm-07__thanks" role="status">
        <div class="frm-07__burst" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
        <h3>Thank you — that genuinely helps.</h3>
        <p>We read every response. Your feedback has been shared with the product team.</p>
        <label for="frm-07-sent" class="frm-07__again">Edit my answer</label>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

.frm-07 {
  --bg: #f4f1fb;
  --card: #ffffff;
  --ink: #1e1b2e;
  --muted: #6b6880;
  --line: #e7e3f3;
  --soft: #f7f5fd;
  --accent: #6d28d9;
  --on-accent: #fff;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(40rem 30rem at 15% 10%, #ffe4e6, transparent 60%), radial-gradient(40rem 30rem at 85% 90%, #dcfce7, transparent 60%), radial-gradient(40rem 30rem at 90% 10%, #e0e7ff, transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-07:not([data-theme="light"]) {
    --bg: #100e18;
    --card: #181524;
    --ink: #efecf8;
    --muted: #a29db8;
    --line: #2b2740;
    --soft: #1f1b2e;
    --accent: #a78bfa;
    --on-accent: #160a33;
  }

  .frm-07:not([data-theme="light"]) {
    background: radial-gradient(40rem 30rem at 15% 10%, #3b0d1a55, transparent 60%), radial-gradient(40rem 30rem at 85% 90%, #0b3b2255, transparent 60%), var(--bg);
  }
}

.frm-07[data-theme="dark"] {
  --bg: #100e18;
  --card: #181524;
  --ink: #efecf8;
  --muted: #a29db8;
  --line: #2b2740;
  --soft: #1f1b2e;
  --accent: #a78bfa;
  --on-accent: #160a33;
  background: var(--bg);
}

.frm-07,
.frm-07 *,
.frm-07 *::before,
.frm-07 *::after {
  box-sizing: border-box;
}

.frm-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-07__card {
  position: relative;
  width: 100%;
  max-width: 40rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.75rem;
  padding: clamp(1.25rem,5vw,2.5rem);
  box-shadow: 0 30px 70px -40px rgba(60,30,120,.45);
}

.frm-07__sendbox {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
  pointer-events: none;
}

.frm-07__survey {
  display: grid;
  gap: 1.4rem;
}

.frm-07__top {
  display: flex;
  align-items: center;
  gap: .7rem;
}

.frm-07__logo {
  display: grid;
  place-items: center;
  width: 2.2rem;
  height: 2.2rem;
  border-radius: .7rem;
  background: var(--ink);
  color: var(--card);
  font-weight: 800;
}

.frm-07__step {
  font-size: .82rem;
  font-weight: 600;
  color: var(--muted);
}

.frm-07__progress {
  height: .3rem;
  border-radius: 99px;
  background: var(--line);
  overflow: hidden;
  margin-top: -.4rem;
}

.frm-07__progress i {
  display: block;
  height: 100%;
  width: 100%;
  background: linear-gradient(90deg,#f43f5e,#f59e0b,#22c55e);
  scale: .08 1;
  transform-origin: left;
  transition: scale .6s var(--ease);
  border-radius: inherit;
}

.frm-07:has([name="frm-07-s"]:checked) .frm-07__progress i {
  scale: .6 1;
}

.frm-07:has(.frm-07__q textarea:not(:placeholder-shown)) .frm-07__progress i {
  scale: .92 1;
}

.frm-07 fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
}

.frm-07 legend {
  padding: 0;
  font-size: clamp(1.25rem,3.6vw,1.6rem);
  font-weight: 700;
  letter-spacing: -.025em;
  line-height: 1.25;
  text-wrap: balance;
  margin-bottom: 1.1rem;
}

.frm-07__scale {
  display: grid;
  grid-template-columns: repeat(11,minmax(0,1fr));
  gap: .35rem;
}

.frm-07__scale label {
  --h: calc(25 + var(--i) * 12.5);
  position: relative;
}

.frm-07__scale input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
  z-index: 1;
}

.frm-07__scale span {
  display: grid;
  place-items: center;
  aspect-ratio: 1/1.15;
  min-height: 2.75rem;
  border-radius: .8rem;
  font-weight: 700;
  font-size: clamp(.85rem,2.4vw,1.05rem);
  background: var(--soft);
  border: 1px solid var(--line);
  font-variant-numeric: tabular-nums;
  transition: background .25s, color .25s, translate .3s var(--ease), scale .3s var(--ease), box-shadow .25s;
}

.frm-07__scale label:hover span {
  translate: 0 -3px;
  border-color: oklch(70% .16 var(--h));
}

.frm-07__scale input:checked + span {
  background: oklch(72% .17 var(--h));
  color: oklch(20% .06 var(--h));
  border-color: transparent;
  scale: 1.08;
  translate: 0 -4px;
  box-shadow: 0 10px 20px -8px oklch(60% .18 var(--h));
}

.frm-07__scale input:focus-visible + span {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.frm-07__scale:has(:checked) input:not(:checked) + span {
  opacity: .55;
}

@media (max-width: 30rem) {
  .frm-07__scale {
    grid-template-columns: repeat(6,1fr);
  }

  .frm-07__scale span {
    aspect-ratio: auto;
  }
}

.frm-07__ends {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: .5rem;
  margin-top: .7rem;
  font-size: .78rem;
  font-weight: 600;
  color: var(--muted);
}

.frm-07__band::before {
  content: '';
  padding: .2rem .6rem;
  border-radius: 99px;
  font-size: .72rem;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.frm-07:has(.is-d:checked) .frm-07__band::before {
  content: 'Detractor';
  background: #ffe4e6;
  color: #9f1239;
}

.frm-07:has(.is-p:checked) .frm-07__band::before {
  content: 'Passive';
  background: #fef3c7;
  color: #92400e;
}

.frm-07:has(.is-r:checked) .frm-07__band::before {
  content: 'Promoter';
  background: #dcfce7;
  color: #166534;
}

.frm-07__q {
  display: none;
  gap: .8rem;
  padding: 1.25rem;
  border-radius: 1.25rem;
  background: var(--soft);
  border: 1px solid var(--line);
}

.frm-07__q legend {
  float: left;
  width: 100%;
  font-size: 1.05rem;
  margin-bottom: .2rem;
}

.frm-07:has(.is-d:checked) .frm-07__q--d,
.frm-07:has(.is-p:checked) .frm-07__q--p,
.frm-07:has(.is-r:checked) .frm-07__q--r {
  display: grid;
  animation: frm-07-in .55s var(--ease);
}

@keyframes frm-07-in {
  from {
    opacity: 0;
    translate: 0 12px;
    scale: .98;
  }
}

.frm-07__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .45rem;
}

.frm-07__chips label {
  position: relative;
}

.frm-07__chips input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-07__chips span {
  display: inline-flex;
  align-items: center;
  min-height: 2.5rem;
  padding: 0 .95rem;
  border-radius: 999px;
  background: var(--card);
  border: 1px solid var(--line);
  font-size: .88rem;
  font-weight: 600;
  transition: all .2s;
}

.frm-07__chips input:checked + span {
  background: var(--ink);
  color: var(--card);
  border-color: var(--ink);
}

.frm-07__chips input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.frm-07__sub {
  font-size: .85rem;
  font-weight: 600;
}

.frm-07__sub span {
  font-weight: 400;
  color: var(--muted);
}

.frm-07 textarea {
  width: 100%;
  padding: .8rem .95rem;
  border-radius: .9rem;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font: inherit;
  font-size: .95rem;
  line-height: 1.5;
  resize: vertical;
  field-sizing: content;
  min-height: 5.5rem;
}

.frm-07 textarea:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 18%,transparent);
}

.frm-07__contact {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .88rem;
  color: var(--muted);
  cursor: pointer;
  min-height: 2.5rem;
}

.frm-07__contact input {
  width: 1.1rem;
  height: 1.1rem;
  accent-color: var(--accent);
  margin: 0;
}

.frm-07__actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.frm-07__skip {
  font-size: .82rem;
  color: var(--muted);
}

.frm-07__submit,
.frm-07__again {
  display: inline-flex;
  align-items: center;
  min-height: 3rem;
  padding: 0 1.5rem;
  border-radius: 999px;
  background: var(--accent);
  color: var(--on-accent);
  font-weight: 700;
  cursor: pointer;
  transition: translate .2s var(--ease), opacity .2s, filter .2s;
  user-select: none;
}

.frm-07__submit:hover {
  translate: 0 -2px;
  filter: brightness(1.08);
}

.frm-07:not(:has([name="frm-07-s"]:checked)) .frm-07__submit {
  opacity: .4;
  pointer-events: none;
}

.frm-07:has(.frm-07__sendbox:focus-visible) .frm-07__submit,
.frm-07:has(.frm-07__sendbox:focus-visible) .frm-07__again {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-07__thanks {
  display: none;
  justify-items: center;
  text-align: center;
  gap: .6rem;
  padding: 2rem 0 1rem;
}

.frm-07__thanks h3 {
  margin: .8rem 0 0;
  font-size: 1.6rem;
  letter-spacing: -.03em;
}

.frm-07__thanks p {
  margin: 0 0 1rem;
  color: var(--muted);
  max-width: 26rem;
}

.frm-07__again {
  background: transparent;
  color: var(--ink);
  border: 1px solid var(--line);
}

.frm-07:has(.frm-07__sendbox:checked) .frm-07__survey {
  display: none;
}

.frm-07:has(.frm-07__sendbox:checked) .frm-07__thanks {
  display: grid;
  animation: frm-07-in .6s var(--ease);
}

.frm-07__burst {
  position: relative;
  width: 4.5rem;
  height: 4.5rem;
  border-radius: 50%;
  background: linear-gradient(135deg,#f472b6,#a78bfa,#34d399);
}

.frm-07__burst::after {
  content: '✓';
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #fff;
  font-size: 2rem;
  font-weight: 800;
}

.frm-07__burst i {
  position: absolute;
  left: 50%;
  top: 50%;
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: hsl(calc(var(--n,0) * 60) 80% 65%);
  opacity: 0;
}

.frm-07__burst i:nth-child(1) {
  --n: 0;
  --a: 0deg;
}

.frm-07__burst i:nth-child(2) {
  --n: 1;
  --a: 60deg;
}

.frm-07__burst i:nth-child(3) {
  --n: 2;
  --a: 120deg;
}

.frm-07__burst i:nth-child(4) {
  --n: 3;
  --a: 180deg;
}

.frm-07__burst i:nth-child(5) {
  --n: 4;
  --a: 240deg;
}

.frm-07__burst i:nth-child(6) {
  --n: 5;
  --a: 300deg;
}

.frm-07:has(.frm-07__sendbox:checked) .frm-07__burst i {
  animation: frm-07-burst .9s .15s var(--ease) both;
}

@keyframes frm-07-burst {
  0% {
    opacity: 1;
    transform: translate(-50%,-50%) rotate(var(--a)) translateY(0);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) rotate(var(--a)) translateY(-3.6rem);
  }
}

@media (prefers-reduced-motion: reduce) {
  .frm-07 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-07__scale input:checked + span,
    .frm-07__chips input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-07__submit,
    .frm-07__again {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-07 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-07__theme {
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

.frm-07__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-07__theme:active {
  transform: scale(.94);
}

.frm-07__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-07__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-07__theme .frm-07__sun,
.frm-07__theme[aria-pressed="true"] .frm-07__moon {
  display: none;
}

.frm-07__theme[aria-pressed="true"] .frm-07__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-07__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-07__theme {
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
  document.querySelectorAll('.frm-07').forEach((root) => {
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

```
