---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/newsletter-signup-form-inline-to-stacked/"
title: "Newsletter Signup Form, Inline to Stacked"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "The newsletter form that adapts to whatever slot you drop it into — a hero, a sidebar, a footer column — using container queries instead of viewport media…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Newsletter Signup Form, Inline to Stacked
Source: https://codefronts.com/components/css-forms/newsletter-signup-form-inline-to-stacked/

The newsletter form that adapts to whatever slot you drop it into — a hero, a sidebar, a footer column — using container queries instead of viewport media queries. It morphs through three layouts: a single pill (input and button fused), a split row, and a full-width stack. Drag the handle on the frame to watch it reflow live, with a width readout showing which layout is active.
## HTML
```html
<div class="frm-05">
  <button type="button" class="frm-05__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-05__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-05__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-05__stage">
    <div class="frm-05__demo">
      <p class="frm-05__tip" aria-hidden="true"><span class="frm-05__w">—</span> · <span class="frm-05__mode">layout</span> · drag the corner ↘</p>
      <div class="frm-05__frame">
        <div class="frm-05__card" role="form" aria-labelledby="frm-05-title">
          <div class="frm-05__issue" aria-hidden="true"><span>No. 142</span><span>Every Friday</span></div>
          <h2 id="frm-05-title" class="frm-05__title">The Friday <em>Fold.</em></h2>
          <p class="frm-05__lede">One email a week on front-end craft — new CSS, honest benchmarks, and one thing worth stealing. Read by 48,000 developers.</p>
          <div class="frm-05__row">
            <label for="frm-05-email" class="frm-05__sr">Email address</label>
            <input id="frm-05-email" type="email" autocomplete="email" required placeholder="[email protected]" aria-describedby="frm-05-note">
            <button class="frm-05__btn" type="button"><span>Subscribe</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
          </div>
          <fieldset class="frm-05__topics">
            <legend class="frm-05__sr">Topics you're interested in</legend>
            <label><input type="checkbox" checked><span>CSS</span></label>
            <label><input type="checkbox"><span>Accessibility</span></label>
            <label><input type="checkbox"><span>Performance</span></label>
            <label><input type="checkbox"><span>Design systems</span></label>
          </fieldset>
          <p class="frm-05__note" id="frm-05-note">No spam. Unsubscribe in one click.</p>
          <p class="frm-05__status" role="status" aria-live="polite"></p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400;12..96,600;12..96,800&display=swap');

.frm-05 {
  --bg: #ecebe4;
  --paper: #fbfaf5;
  --ink: #0d0d0b;
  --muted: #56554e;
  --field: #ffffff;
  --accent: #c6f432;
  --on-accent: #0d0d0b;
  --bad: #d4380d;
  --sans: "Bricolage Grotesque",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(circle at 1px 1px, color-mix(in oklab,var(--ink) 14%,transparent) 1px, transparent 0) 0 0 / 22px 22px, var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-05:not([data-theme="light"]) {
    --bg: #0f0f0d;
    --paper: #181815;
    --ink: #f4f3ea;
    --muted: #a8a698;
    --field: #22221e;
    --accent: #c6f432;
    --on-accent: #0d0d0b;
    --bad: #ff7a45;
  }
}

.frm-05[data-theme="dark"] {
  --bg: #0f0f0d;
  --paper: #181815;
  --ink: #f4f3ea;
  --muted: #a8a698;
  --field: #22221e;
  --accent: #c6f432;
  --on-accent: #0d0d0b;
  --bad: #ff7a45;
}

.frm-05,
.frm-05 *,
.frm-05 *::before,
.frm-05 *::after {
  box-sizing: border-box;
}

.frm-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.frm-05__demo {
  width: 100%;
  max-width: 64rem;
  display: grid;
  gap: .75rem;
}

.frm-05__tip {
  margin: 0;
  font-size: .8rem;
  font-weight: 600;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.frm-05__mode {
  color: var(--ink);
  background: var(--accent);
  color: var(--on-accent);
  padding: .1rem .45rem;
  border-radius: .3rem;
}

.frm-05__frame {
  container: frm-05 / inline-size;
  resize: horizontal;
  overflow: hidden;
  width: 100%;
  min-width: 17rem;
  max-width: 100%;
  border-radius: 1.75rem;
  background: var(--paper);
  box-shadow: 0 0 0 2px var(--ink), 10px 10px 0 var(--ink);
}

.frm-05__card {
  display: grid;
  gap: 1.1rem;
  padding: clamp(1.25rem,6cqi,3.5rem);
}

.frm-05__issue {
  display: flex;
  justify-content: space-between;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
  padding-bottom: .9rem;
  border-bottom: 2px solid var(--ink);
}

.frm-05__title {
  margin: 0;
  font-size: clamp(2rem,10cqi,5.5rem);
  font-weight: 800;
  line-height: .92;
  letter-spacing: -.045em;
  font-variation-settings: 'opsz' 96;
  text-wrap: balance;
}

.frm-05__title em {
  font-style: normal;
  background: linear-gradient(transparent 58%, var(--accent) 58% 92%, transparent 92%);
  padding: 0 .05em;
}

.frm-05__lede {
  margin: 0;
  max-width: 38rem;
  font-size: clamp(1rem,2.4cqi,1.2rem);
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.frm-05__row {
  display: grid;
  gap: .6rem;
  margin-top: .4rem;
}

.frm-05__row input {
  width: 100%;
  min-height: 3.4rem;
  padding: 0 1.2rem;
  border: 0;
  border-radius: 1rem;
  background: var(--field);
  color: var(--ink);
  font: inherit;
  font-size: 1.05rem;
  box-shadow: inset 0 0 0 2px var(--ink);
  transition: box-shadow .2s;
}

.frm-05__row input::placeholder {
  color: color-mix(in oklab,var(--muted) 80%,transparent);
}

.frm-05__row input:focus-visible {
  outline: none;
  box-shadow: inset 0 0 0 3px var(--ink), 0 0 0 5px var(--accent);
}

.frm-05__row input:user-invalid {
  box-shadow: inset 0 0 0 2px var(--bad);
}

.frm-05__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .55rem;
  min-height: 3.4rem;
  padding: 0 1.6rem;
  border: 0;
  border-radius: 1rem;
  cursor: pointer;
  font: inherit;
  font-size: 1.05rem;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--on-accent);
  background: var(--accent);
  box-shadow: inset 0 0 0 2px var(--ink), 4px 4px 0 var(--ink);
  transition: translate .15s var(--ease), box-shadow .15s var(--ease);
}

.frm-05__btn svg {
  width: 1.2rem;
  height: 1.2rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: translate .3s var(--ease);
}

.frm-05__btn:hover {
  translate: -2px -2px;
  box-shadow: inset 0 0 0 2px var(--ink), 6px 6px 0 var(--ink);
}

.frm-05__btn:hover svg {
  translate: 3px 0;
}

.frm-05__btn:active {
  translate: 3px 3px;
  box-shadow: inset 0 0 0 2px var(--ink), 0 0 0 var(--ink);
}

.frm-05__btn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

@container frm-05 (min-width: 30rem) {
  .frm-05__row {
    grid-template-columns: minmax(0,1fr) auto;
  }
}

@container frm-05 (min-width: 44rem) {
  .frm-05__row {
    gap: 0;
    padding: .4rem;
    border-radius: 999px;
    background: var(--field);
    box-shadow: inset 0 0 0 2px var(--ink);
    transition: box-shadow .2s;
  }

  .frm-05__row:focus-within {
    box-shadow: inset 0 0 0 3px var(--ink), 0 0 0 5px var(--accent);
  }

  .frm-05__row input {
    box-shadow: none !important;
    background: transparent;
    border-radius: 999px;
  }

  .frm-05__row input:focus-visible {
    box-shadow: none;
  }

  .frm-05__btn {
    border-radius: 999px;
    box-shadow: inset 0 0 0 2px var(--ink);
  }

  .frm-05__btn:hover {
    translate: 0;
    box-shadow: inset 0 0 0 2px var(--ink);
    filter: brightness(1.05);
  }

  .frm-05__btn:active {
    translate: 0;
    scale: .97;
  }
}

@container frm-05 (max-width: 29.99rem) {
  .frm-05__btn {
    width: 100%;
  }

  .frm-05__issue span:last-child {
    display: none;
  }
}

.frm-05__topics {
  border: 0;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .45rem;
}

.frm-05__topics label {
  position: relative;
  cursor: pointer;
}

.frm-05__topics input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-05__topics span {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.4rem;
  padding: 0 .9rem;
  border-radius: 999px;
  font-size: .88rem;
  font-weight: 600;
  box-shadow: inset 0 0 0 1.5px color-mix(in oklab,var(--ink) 40%,transparent);
  transition: background .2s, box-shadow .2s;
}

.frm-05__topics span::before {
  content: '+';
  font-weight: 800;
  transition: rotate .3s var(--ease);
}

.frm-05__topics input:checked + span {
  background: var(--ink);
  color: var(--paper);
  box-shadow: none;
}

.frm-05__topics input:checked + span::before {
  content: '✓';
}

.frm-05__topics input:focus-visible + span {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.frm-05__note {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.frm-05__status {
  margin: 0;
  font-weight: 600;
}

.frm-05__status:empty {
  display: none;
}

.frm-05__status[data-ok="true"] {
  padding: .9rem 1.1rem;
  border-radius: 1rem;
  background: var(--accent);
  color: var(--on-accent);
  animation: frm-05-pop .5s var(--ease);
}

.frm-05__status[data-ok="false"] {
  color: var(--bad);
}

@keyframes frm-05-pop {
  from {
    scale: .95;
    opacity: 0;
  }
}

.frm-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (hover: none) {
  .frm-05__frame {
    resize: none;
  }

  .frm-05__tip {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .frm-05 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .frm-05__frame {
    border: 2px solid CanvasText;
  }

  .frm-05__btn {
    border: 2px solid ButtonText;
  }

  .frm-05__topics input:checked + span {
    background: Highlight;
    color: HighlightText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-05 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-05__theme {
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

.frm-05__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-05__theme:active {
  transform: scale(.94);
}

.frm-05__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-05__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-05__theme .frm-05__sun,
.frm-05__theme[aria-pressed="true"] .frm-05__moon {
  display: none;
}

.frm-05__theme[aria-pressed="true"] .frm-05__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-05__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-05__theme {
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
  document.querySelectorAll('.frm-05').forEach((root) => {
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
  const root = document.querySelector('.frm-05');
  if (!root) return;
  const frame = root.querySelector('.frm-05__frame'), w = root.querySelector('.frm-05__w'), mode = root.querySelector('.frm-05__mode');
  const rem = parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
  new ResizeObserver(([e]) => {
    const px = Math.round(e.contentBoxSize ? e.contentBoxSize[0].inlineSize : e.contentRect.width);
    w.textContent = px + 'px';
    mode.textContent = px >= 44 * rem ? 'fused pill' : px >= 30 * rem ? 'split row' : 'stacked';
  }).observe(frame);
  const email = root.querySelector('#frm-05-email'), status = root.querySelector('.frm-05__status');
  const go = () => {
    if (!email.checkValidity() || !email.value) { status.dataset.ok = 'false'; status.textContent = 'Please enter a valid email address.'; email.focus(); return; }
    status.dataset.ok = 'true';
    status.textContent = 'Almost there — check ' + email.value + ' and confirm your subscription.';
  };
  root.querySelector('.frm-05__btn').addEventListener('click', go);
  email.addEventListener('keydown', (e) => { if (e.key === 'Enter') go(); });
})();
```
