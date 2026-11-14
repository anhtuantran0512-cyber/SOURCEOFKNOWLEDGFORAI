---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/magnetic-button-effect/"
title: "Interruptible Transitions and Reverse Playback"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "What happens when a transition is interrupted mid-flight: it reverses from wherever it currently is, because the running value is the new start value."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interruptible Transitions and Reverse Playback
Source: https://codefronts.com/motion/css-transition-designs/magnetic-button-effect/

What happens when a transition is interrupted mid-flight: it reverses from wherever it currently is, because the running value is the new start value. A keyframe timeline restarts from frame zero instead. Sweep the pointer on and off the pad below to feel the difference — this is the strongest argument for transitions over animations in interactive UI.
## HTML
```html
<section class="trn-20" aria-labelledby="trn-20-heading">
  <div class="trn-20__stage">
    <div class="trn-20__theme">
      <input class="trn-20__themecb" type="checkbox" id="trn-20-theme">
      <label class="trn-20__themebtn" for="trn-20-theme">
        <span class="trn-20__themeico" aria-hidden="true">
          <svg class="trn-20__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-20__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-20__head">
      <p class="trn-20__kicker">interruption</p>
      <h2 class="trn-20__heading" id="trn-20-heading">Sweep across, then back, quickly</h2>
      <p class="trn-20__sub">Long durations on purpose. Leave either pad halfway through and watch where the motion resumes from.</p>
    </header>

    <div class="trn-20__pair">
      <article class="trn-20__pad trn-20__pad--trans" tabindex="0">
        <p class="trn-20__label">Transition — reverses from the current value</p>
        <div class="trn-20__lane">
          <span class="trn-20__mark trn-20__mark--t" style="--d: 0ms"></span>
          <span class="trn-20__mark trn-20__mark--t" style="--d: 40ms"></span>
          <span class="trn-20__mark trn-20__mark--t" style="--d: 80ms"></span>
        </div>
        <p class="trn-20__read">Interrupt at 40% and the return trip starts at 40%. Nothing jumps.</p>
      </article>

      <article class="trn-20__pad trn-20__pad--anim" tabindex="0">
        <p class="trn-20__label trn-20__label--alt">Keyframe animation — restarts at 0%</p>
        <div class="trn-20__lane">
          <span class="trn-20__mark trn-20__mark--a"></span>
        </div>
        <p class="trn-20__read">Re-entering re-triggers the timeline from its first frame, so the marker snaps home before travelling again.</p>
      </article>
    </div>

    <p class="trn-20__foot">State-driven motion belongs to transitions. Self-scheduled motion — spinners, ambient pulses — belongs to keyframes. The interruption behaviour is the reason.</p>
  </div>
</section>
```
## CSS
```css
.trn-20 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #2a1220;
  --page: oklch(0.26 0.07 15);
  --card: #3a1826;
  --ink: #fff2e8;
  --ink: oklch(0.96 0.02 55);
  --muted: #d8a08e;
  --muted: oklch(0.78 0.07 40);
  --amber: #ffb03a;
  --amber: oklch(0.82 0.16 70);
  --coral: #ff6b4a;
  --coral: oklch(0.72 0.19 35);
  --dur: 1100ms;
  --font-display: "Archivo", "Roboto Condensed", "Oswald", system-ui, sans-serif;
  background: linear-gradient(155deg, #40182a 0%, var(--page) 45%, #1c0d18 100%);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-20 *,
.trn-20 *::before,
.trn-20 *::after {
  box-sizing: border-box;
}

.trn-20__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 6vw, 72px) 18px;
}

.trn-20__head {
  inline-size: 100%;
  max-inline-size: 56rem;
  min-inline-size: 0;
  margin: 0 0 32px;
}

.trn-20__kicker {
  margin: 0 0 14px;
  font: 700 11px/1 var(--font-display);
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--amber);
}

.trn-20__heading {
  margin: 0 0 12px;
  font: 700 clamp(27px, 5.4vw, 44px)/1.02 var(--font-display);
  letter-spacing: -0.015em;
  text-transform: uppercase;
  text-wrap: balance;
}

.trn-20__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-20__pair {
  inline-size: 100%;
  max-inline-size: 56rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 22px;
}

.trn-20__pad {
  min-inline-size: 0;
  padding: 24px;
  background: var(--card);
  border: 1px solid rgba(255, 176, 58, 0.24);
  border-radius: 4px;
  box-shadow: 8px 8px 0 rgba(0, 0, 0, 0.35);
}

.trn-20__pad:focus-visible {
  outline: 2px solid var(--amber);
  outline-offset: 3px;
}

.trn-20__label {
  margin: 0 0 20px;
  font: 700 12px/1.4 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--amber);
}

.trn-20__label--alt {
  color: var(--coral);
}

.trn-20__lane {
  position: relative;
  display: grid;
  gap: 12px;
  padding: 4px 0;
}

.trn-20__mark {
  display: block;
  inline-size: 34px;
  block-size: 34px;
  border-radius: 3px;
}

.trn-20__mark--t {
  background: linear-gradient(135deg, var(--amber), var(--coral));
  transition: transform var(--dur) cubic-bezier(.3, .7, .3, 1);
  transition-delay: var(--d);
}

.trn-20__pad--trans:hover .trn-20__mark--t,
.trn-20__pad--trans:focus-visible .trn-20__mark--t {
  transform: translateX(calc(100% * 3.4));
}

.trn-20__mark--a {
  background: var(--coral);
}

.trn-20__pad--anim:hover .trn-20__mark--a,
.trn-20__pad--anim:focus-visible .trn-20__mark--a {
  animation: trn-20-travel var(--dur) cubic-bezier(.3, .7, .3, 1) forwards;
}

@keyframes trn-20-travel {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(calc(100% * 3.4));
  }
}

.trn-20__read {
  margin: 22px 0 0;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-20__foot {
  inline-size: 100%;
  max-inline-size: 56rem;
  margin: 32px 0 0;
  padding-block-start: 20px;
  border-block-start: 1px solid rgba(255, 176, 58, 0.2);
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .trn-20__mark--t {
    transition: opacity 160ms ease, background-color 160ms ease;
  }

  .trn-20__pad--trans:hover .trn-20__mark--t,
    .trn-20__pad--trans:focus-visible .trn-20__mark--t {
    transform: none;
    opacity: 0.72;
  }

  .trn-20__pad--anim:hover .trn-20__mark--a,
    .trn-20__pad--anim:focus-visible .trn-20__mark--a {
    animation: none;
    opacity: 0.72;
  }
}

@media (prefers-color-scheme: light) {
  .trn-20 {
    --page: #fff6f0;
    --card: #ffffff;
    --ink: #35131f;
    --muted: #8a5343;
    --amber: #b06a00;
    --coral: #c33c1c;
    background: linear-gradient(155deg, #fff1e6 0%, var(--page) 45%, #ffe6da 100%);
  }

  .trn-20__pad {
    border-color: rgba(176, 106, 0, 0.24);
    box-shadow: 8px 8px 0 rgba(53, 19, 31, 0.1);
  }

  .trn-20__foot {
    border-block-start-color: rgba(176, 106, 0, 0.24);
  }
}

[data-theme="dark"] .trn-20 {
  --page: #2a1220;
  --card: #3a1826;
  --ink: #fff2e8;
  --muted: #d8a08e;
  --amber: #ffb03a;
  --coral: #ff6b4a;
  background: linear-gradient(155deg, #40182a 0%, var(--page) 45%, #1c0d18 100%);
}

[data-theme="dark"] .trn-20__pad {
  border-color: rgba(255, 176, 58, 0.24);
  box-shadow: 8px 8px 0 rgba(0, 0, 0, 0.35);
}

.trn-20__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-20__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-20__themebtn {
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

.trn-20__themebtn:hover {
  color: var(--ink);
}

.trn-20__themecb:focus-visible + .trn-20__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-20__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-20__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-20__sun {
  opacity: 0.34;
}

.trn-20__moon {
  opacity: 1;
}

.trn-20:has(#trn-20-theme:checked) .trn-20__sun {
  opacity: 1;
}

.trn-20:has(#trn-20-theme:checked) .trn-20__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-20:has(#trn-20-theme:checked) {
    --page: #fff6f0;
    --card: #ffffff;
    --ink: #35131f;
    --muted: #8a5343;
    --amber: #b06a00;
    --coral: #c33c1c;
    background: linear-gradient(155deg, #fff1e6 0%, var(--page) 45%, #ffe6da 100%);
  }

  .trn-20:has(#trn-20-theme:checked) .trn-20__pad {
    border-color: rgba(176, 106, 0, 0.24);
    box-shadow: 8px 8px 0 rgba(53, 19, 31, 0.1);
  }

  .trn-20:has(#trn-20-theme:checked) .trn-20__foot {
    border-block-start-color: rgba(176, 106, 0, 0.24);
  }
}

@media (prefers-color-scheme: light) {
  .trn-20:has(#trn-20-theme:checked) {
    --page: #2a1220;
    --page: oklch(0.26 0.07 15);
    --card: #3a1826;
    --ink: #fff2e8;
    --ink: oklch(0.96 0.02 55);
    --muted: #d8a08e;
    --muted: oklch(0.78 0.07 40);
    --amber: #ffb03a;
    --amber: oklch(0.82 0.16 70);
    --coral: #ff6b4a;
    --coral: oklch(0.72 0.19 35);
    --dur: 1100ms;
    --font-display: "Archivo", "Roboto Condensed", "Oswald", system-ui, sans-serif;
    background: linear-gradient(155deg, #40182a 0%, var(--page) 45%, #1c0d18 100%);
  }

  .trn-20:has(#trn-20-theme:checked) .trn-20__pad {
    min-inline-size: 0;
    padding: 24px;
    background: var(--card);
    border: 1px solid rgba(255, 176, 58, 0.24);
    border-radius: 4px;
    box-shadow: 8px 8px 0 rgba(0, 0, 0, 0.35);
  }

  .trn-20:has(#trn-20-theme:checked) .trn-20__foot {
    inline-size: 100%;
    max-inline-size: 56rem;
    margin: 32px 0 0;
    padding-block-start: 20px;
    border-block-start: 1px solid rgba(255, 176, 58, 0.2);
    font-size: 12.5px;
    line-height: 1.6;
    color: var(--muted);
  }

  .trn-20:has(#trn-20-theme:checked) .trn-20__sun {
    opacity: 0.34;
  }

  .trn-20:has(#trn-20-theme:checked) .trn-20__moon {
    opacity: 1;
  }
}
```
