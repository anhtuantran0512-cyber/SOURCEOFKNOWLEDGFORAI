---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/progress-bar-animation/"
title: "Reduced Motion Transition Strategy"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "The reflexive @media (prefers-reduced-motion: reduce) { * { transition: none !important } } is the wrong answer: it removes the gentle fades that actually…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reduced Motion Transition Strategy
Source: https://codefronts.com/motion/css-transition-designs/progress-bar-animation/

The reflexive @media (prefers-reduced-motion: reduce) { * { transition: none !important } } is the wrong answer: it removes the gentle fades that actually reduce motion sickness, and it can strand elements mid-state when a transition was carrying them somewhere. The same component is shown under all three treatments, each labelled, with the current preference detected and displayed.
## HTML
```html
<section class="trn-22" aria-labelledby="trn-22-heading">
  <div class="trn-22__stage">
    <div class="trn-22__theme">
      <input class="trn-22__themecb" type="checkbox" id="trn-22-theme">
      <label class="trn-22__themebtn" for="trn-22-theme">
        <span class="trn-22__themeico" aria-hidden="true">
          <svg class="trn-22__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-22__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-22__head">
      <p class="trn-22__kicker">prefers-reduced-motion</p>
      <h2 class="trn-22__heading" id="trn-22-heading">Reduce the motion. Keep the feedback.</h2>
      <p class="trn-22__sub">One card, three treatments. Hover each; then flip your system's reduce-motion setting and hover them again.</p>
      <p class="trn-22__state">
        <span class="trn-22__on">Your system currently requests reduced motion.</span>
        <span class="trn-22__off">Your system currently allows full motion.</span>
      </p>
    </header>

    <div class="trn-22__grid">
      <article class="trn-22__col">
        <h3 class="trn-22__label trn-22__label--bad">Blanket transition: none</h3>
        <button class="trn-22__card trn-22__card--none" type="button">
          <span class="trn-22__ctitle">Quill retention job</span>
          <span class="trn-22__cmeta">Runs nightly &middot; 02:00 UTC</span>
          <span class="trn-22__cpill">Enabled</span>
        </button>
        <p class="trn-22__verdict">No movement, and no feedback either. The state change is invisible, and any transition carrying a discrete property is stranded.</p>
      </article>

      <article class="trn-22__col">
        <h3 class="trn-22__label trn-22__label--warn">Untouched full motion</h3>
        <button class="trn-22__card trn-22__card--full" type="button">
          <span class="trn-22__ctitle">Quill retention job</span>
          <span class="trn-22__cmeta">Runs nightly &middot; 02:00 UTC</span>
          <span class="trn-22__cpill">Enabled</span>
        </button>
        <p class="trn-22__verdict">Lift, scale and colour at full duration regardless of the preference. Fine for most, a genuine problem for some.</p>
      </article>

      <article class="trn-22__col">
        <h3 class="trn-22__label trn-22__label--good">Nuanced strategy</h3>
        <button class="trn-22__card trn-22__card--tuned" type="button">
          <span class="trn-22__ctitle">Quill retention job</span>
          <span class="trn-22__cmeta">Runs nightly &middot; 02:00 UTC</span>
          <span class="trn-22__cpill">Enabled</span>
        </button>
        <p class="trn-22__verdict">Keeps opacity and colour, drops the lift and the scale, halves the duration. The interaction still answers you.</p>
      </article>
    </div>

    <pre class="trn-22__snippet">@media (prefers-reduced-motion: reduce) {
  .trn-22__card--tuned { transition: background-color 150ms ease, border-color 150ms ease, opacity 150ms ease; }
  .trn-22__card--tuned:hover { transform: none; opacity: .92; }
}</pre>
  </div>
</section>
```
## CSS
```css
.trn-22 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f3f6f1;
  --page: oklch(0.96 0.012 145);
  --card: #ffffff;
  --surface: #e8eee4;
  --surface: oklch(0.93 0.016 140);
  --ink: #1b241c;
  --ink: oklch(0.25 0.016 150);
  --muted: #5c685c;
  --muted: oklch(0.5 0.016 150);
  --rule: #d5ded1;
  --rule: oklch(0.88 0.014 145);
  --green: #37734a;
  --green: oklch(0.5 0.1 155);
  --warn: #8c6a1c;
  --warn: oklch(0.53 0.1 90);
  --bad: #a24132;
  --bad: oklch(0.48 0.14 32);
  --font-display: "Hoefler Text", "Iowan Old Style", Georgia, serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-22 *,
.trn-22 *::before,
.trn-22 *::after {
  box-sizing: border-box;
}

.trn-22__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 6vw, 70px) 18px;
}

.trn-22__head {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  margin: 0 0 30px;
}

.trn-22__kicker {
  margin: 0 0 14px;
  font: 400 12px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.08em;
  color: var(--green);
}

.trn-22__heading {
  margin: 0 0 12px;
  font: 500 clamp(26px, 5vw, 40px)/1.08 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-22__sub {
  margin: 0 0 14px;
  max-inline-size: 52ch;
  font-size: 15px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-22__state {
  margin: 0;
  font: 400 12.5px/1.4 ui-monospace, Menlo, monospace;
  color: var(--ink);
}

.trn-22__on {
  display: none;
}

.trn-22__off {
  display: inline;
}

.trn-22__grid {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 24px;
}

.trn-22__col {
  min-inline-size: 0;
}

.trn-22__label {
  margin: 0 0 12px;
  font: 400 12.5px/1.4 ui-monospace, Menlo, monospace;
}

.trn-22__label--bad {
  color: var(--bad);
}

.trn-22__label--warn {
  color: var(--warn);
}

.trn-22__label--good {
  color: var(--green);
}

.trn-22__card {
  inline-size: 100%;
  display: grid;
  gap: 6px;
  justify-items: start;
  min-height: 96px;
  padding: 16px;
  text-align: start;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 4px;
  cursor: pointer;
}

.trn-22__card:focus-visible {
  outline: 2px solid var(--green);
  outline-offset: 3px;
}

.trn-22__ctitle {
  font: 500 16px/1.2 var(--font-display);
  color: var(--ink);
}

.trn-22__cmeta {
  font: 400 12px/1.3 ui-monospace, Menlo, monospace;
  color: var(--muted);
}

.trn-22__cpill {
  margin-block-start: 4px;
  padding: 3px 8px;
  background: var(--surface);
  border-radius: 2px;
  font: 400 11px/1.4 ui-monospace, Menlo, monospace;
  color: var(--green);
}

.trn-22__card--none {
  transition: transform 320ms cubic-bezier(.2, .8, .3, 1), background-color 320ms ease, border-color 320ms ease;
}

.trn-22__card--none:hover {
  transform: translateY(-4px) scale(1.02);
  background: var(--surface);
  border-color: var(--green);
}

.trn-22__card--full {
  transition: transform 320ms cubic-bezier(.2, .8, .3, 1), background-color 320ms ease, border-color 320ms ease;
}

.trn-22__card--full:hover {
  transform: translateY(-4px) scale(1.02);
  background: var(--surface);
  border-color: var(--green);
}

.trn-22__card--tuned {
  transition: transform 320ms cubic-bezier(.2, .8, .3, 1), background-color 320ms ease, border-color 320ms ease, opacity 320ms ease;
}

.trn-22__card--tuned:hover {
  transform: translateY(-4px) scale(1.02);
  background: var(--surface);
  border-color: var(--green);
}

.trn-22__verdict {
  margin: 12px 0 0;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-22__snippet {
  inline-size: 100%;
  max-inline-size: 58rem;
  margin: 30px 0 0;
  padding: 14px 16px;
  background: var(--surface);
  border-radius: 4px;
  font: 400 11.5px/1.7 ui-monospace, Menlo, monospace;
  color: var(--ink);
  overflow-x: auto;
}

@media (prefers-reduced-motion: reduce) {
  .trn-22__on {
    display: inline;
  }

  .trn-22__off {
    display: none;
  }

  .trn-22__card--none {
    transition: none;
  }

  .trn-22__card--none:hover {
    transform: none;
  }

  .trn-22__card--tuned {
    transition: background-color 150ms ease, border-color 150ms ease, opacity 150ms ease;
  }

  .trn-22__card--tuned:hover {
    transform: none;
    opacity: 0.92;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-22 {
    --page: #141a15;
    --page: oklch(0.2 0.014 150);
    --card: #1c231d;
    --card: oklch(0.24 0.016 150);
    --surface: #232b23;
    --surface: oklch(0.28 0.018 148);
    --ink: #e9efe8;
    --ink: oklch(0.95 0.012 150);
    --muted: #96a396;
    --muted: oklch(0.71 0.016 150);
    --rule: #2b332c;
    --rule: oklch(0.31 0.014 150);
    --green: #79cf94;
    --green: oklch(0.81 0.12 155);
    --warn: #d6b769;
    --bad: #ef8b74;
  }
}

[data-theme="dark"] .trn-22 {
  --page: #141a15;
  --card: #1c231d;
  --surface: #232b23;
  --ink: #e9efe8;
  --muted: #96a396;
  --rule: #2b332c;
  --green: #79cf94;
  --warn: #d6b769;
  --bad: #ef8b74;
}

.trn-22__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-22__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-22__themebtn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid currentColor;
  border-radius: 999px;
  cursor: pointer;
  color: var(--muted);
  font: 500 11px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: color 200ms ease, opacity 200ms ease;
}

.trn-22__themebtn:hover {
  color: var(--ink);
}

.trn-22__themecb:focus-visible + .trn-22__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-22__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-22__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-22__sun {
  opacity: 1;
}

.trn-22__moon {
  opacity: 0.34;
}

.trn-22:has(#trn-22-theme:checked) .trn-22__sun {
  opacity: 0.34;
}

.trn-22:has(#trn-22-theme:checked) .trn-22__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-22:has(#trn-22-theme:checked) {
    --page: #141a15;
    --page: oklch(0.2 0.014 150);
    --card: #1c231d;
    --card: oklch(0.24 0.016 150);
    --surface: #232b23;
    --surface: oklch(0.28 0.018 148);
    --ink: #e9efe8;
    --ink: oklch(0.95 0.012 150);
    --muted: #96a396;
    --muted: oklch(0.71 0.016 150);
    --rule: #2b332c;
    --rule: oklch(0.31 0.014 150);
    --green: #79cf94;
    --green: oklch(0.81 0.12 155);
    --warn: #d6b769;
    --bad: #ef8b74;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-22:has(#trn-22-theme:checked) {
    --page: #f3f6f1;
    --page: oklch(0.96 0.012 145);
    --card: #ffffff;
    --surface: #e8eee4;
    --surface: oklch(0.93 0.016 140);
    --ink: #1b241c;
    --ink: oklch(0.25 0.016 150);
    --muted: #5c685c;
    --muted: oklch(0.5 0.016 150);
    --rule: #d5ded1;
    --rule: oklch(0.88 0.014 145);
    --green: #37734a;
    --green: oklch(0.5 0.1 155);
    --warn: #8c6a1c;
    --warn: oklch(0.53 0.1 90);
    --bad: #a24132;
    --bad: oklch(0.48 0.14 32);
    --font-display: "Hoefler Text", "Iowan Old Style", Georgia, serif;
    background: var(--page);
  }

  .trn-22:has(#trn-22-theme:checked) .trn-22__sun {
    opacity: 1;
  }

  .trn-22:has(#trn-22-theme:checked) .trn-22__moon {
    opacity: 0.34;
  }
}
```
