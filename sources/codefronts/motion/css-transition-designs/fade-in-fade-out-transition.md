---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/fade-in-fade-out-transition/"
title: "Transition to Display None with allow-discrete"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "For twenty years an element set to display: none vanished on the spot and any fade-out was lost, which is why hiding used to mean visibility plus a delay."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transition to Display None with allow-discrete
Source: https://codefronts.com/motion/css-transition-designs/fade-in-fade-out-transition/

For twenty years an element set to display: none vanished on the spot and any fade-out was lost, which is why hiding used to mean visibility plus a delay. transition-behavior: allow-discrete flips the discrete property at the end of the transition instead of the start. Two toasts, both labelled: one fades out correctly, one snaps.
## HTML
```html
<section class="trn-08" aria-labelledby="trn-08-heading">
  <div class="trn-08__stage">
    <div class="trn-08__theme">
      <input class="trn-08__themecb" type="checkbox" id="trn-08-theme">
      <label class="trn-08__themebtn" for="trn-08-theme">
        <span class="trn-08__themeico" aria-hidden="true">
          <svg class="trn-08__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-08__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-08__head">
      <p class="trn-08__kicker">transition-behavior</p>
      <h2 class="trn-08__heading" id="trn-08-heading">Hiding an element without losing the fade</h2>
      <p class="trn-08__sub">One checkbox, two toasts. Uncheck it and watch which one leaves gracefully.</p>
    </header>

    <div class="trn-08__panel">
      <input class="trn-08__input" type="checkbox" id="trn-08-show" checked>
      <label class="trn-08__toggle" for="trn-08-show">
        <span class="trn-08__dot" aria-hidden="true"></span>
        <span class="trn-08__toggletext">Toast visible</span>
      </label>

      <div class="trn-08__pair">
        <div class="trn-08__slot">
          <p class="trn-08__label trn-08__label--good">display + allow-discrete — fades, then unmounts</p>
          <output class="trn-08__toast trn-08__toast--good" aria-live="polite">
            <svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true"><circle cx="10" cy="10" r="8.4" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m6.4 10.3 2.5 2.5 4.7-5" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>
            <span><strong>Deploy queued</strong><br>Basalt &middot; production &middot; 4192</span>
          </output>
          <code class="trn-08__code">transition: opacity 320ms ease, display 320ms allow-discrete;</code>
        </div>

        <div class="trn-08__slot">
          <p class="trn-08__label trn-08__label--bad">display alone — snaps out, fade never runs</p>
          <output class="trn-08__toast trn-08__toast--bad" aria-live="off">
            <svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true"><path d="M10 2.6 18 17H2L10 2.6Z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 7.6v4.2M10 13.7v1" stroke="currentColor" stroke-width="1.6"/></svg>
            <span><strong>Deploy queued</strong><br>Basalt &middot; production &middot; 4192</span>
          </output>
          <code class="trn-08__code">transition: opacity 320ms ease;</code>
        </div>
      </div>

      <p class="trn-08__foot">Entry is a separate problem: <code>allow-discrete</code> makes the element exist in time, but it needs <code>@starting-style</code> to have a value to fade up from. Demo 11 covers that half.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.trn-08 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #211d18;
  --page: oklch(0.24 0.014 68);
  --card: #2b261f;
  --card: oklch(0.29 0.016 70);
  --ink: #f7f1e6;
  --ink: oklch(0.96 0.016 82);
  --muted: #a99e8c;
  --muted: oklch(0.73 0.022 80);
  --rule: #3d372d;
  --rule: oklch(0.35 0.018 72);
  --amber: #f0a828;
  --amber: oklch(0.79 0.145 76);
  --good: #7ad39a;
  --good: oklch(0.82 0.12 155);
  --bad: #ef7f60;
  --bad: oklch(0.72 0.15 40);
  --font-display: "Inter Tight", "Helvetica Neue", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-08 *,
.trn-08 *::before,
.trn-08 *::after {
  box-sizing: border-box;
}

.trn-08__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(24px, 5vw, 54px) 14px;
}

.trn-08__head {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  margin: 0 0 20px;
}

.trn-08__kicker {
  margin: 0 0 10px;
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--amber);
}

.trn-08__heading {
  margin: 0 0 8px;
  font: 700 clamp(22px, 4.2vw, 32px)/1.12 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-08__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 14px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-08__panel {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  padding: 14px;
  background: var(--card);
  border-radius: 8px;
  box-shadow: 0 10px 0 -4px rgba(0, 0, 0, 0.35);
}

.trn-08__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-08__toggle {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid var(--rule);
  border-radius: 6px;
  cursor: pointer;
  font: 600 11.5px/1 var(--font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  transition: color 180ms ease, border-color 180ms ease;
}

.trn-08__input:checked + .trn-08__toggle {
  color: var(--amber);
  border-color: var(--amber);
}

.trn-08__input:focus-visible + .trn-08__toggle {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-08__dot {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: var(--rule);
  transition: background-color 180ms ease;
}

.trn-08__input:checked + .trn-08__toggle .trn-08__dot {
  background: var(--amber);
}

.trn-08__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 12px;
  margin-block-start: 14px;
}

.trn-08__slot {
  min-inline-size: 0;
}

.trn-08__label {
  margin: 0 0 8px;
  font: 600 11px/1.4 ui-monospace, Menlo, monospace;
}

.trn-08__label--good {
  color: var(--good);
}

.trn-08__label--bad {
  color: var(--bad);
}

.trn-08__toast {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  min-inline-size: 0;
  min-height: 60px;
  padding: 11px 12px;
  background: var(--page);
  border: 1px solid var(--rule);
  border-radius: 6px;
  font-size: 12.5px;
  line-height: 1.4;
  color: var(--muted);
  visibility: hidden;
  opacity: 0;
  transition: opacity 320ms ease, visibility 0s linear 320ms;
}

.trn-08__toast svg {
  flex: none;
  margin-block-start: 1px;
}

.trn-08__toast strong {
  color: var(--ink);
  font: 600 13px/1.3 var(--font-display);
}

.trn-08__toast--good {
  border-inline-start: 3px solid var(--good);
  color: var(--muted);
}

.trn-08__toast--good svg {
  color: var(--good);
}

.trn-08__toast--bad {
  border-inline-start: 3px solid var(--bad);
}

.trn-08__toast--bad svg {
  color: var(--bad);
}

.trn-08:has(#trn-08-show:checked) .trn-08__toast {
  visibility: visible;
  opacity: 1;
  transition: opacity 320ms ease, visibility 0s linear 0s;
}

@supports (transition-behavior: allow-discrete) {
  .trn-08__toast--good {
    display: none;
    visibility: visible;
    transition: opacity 320ms ease, display 320ms allow-discrete;
  }

  .trn-08:has(#trn-08-show:checked) .trn-08__toast--good {
    display: flex;
    opacity: 1;
  }

  .trn-08__toast--bad {
    display: none;
    visibility: visible;
    transition: opacity 320ms ease;
  }

  .trn-08:has(#trn-08-show:checked) .trn-08__toast--bad {
    display: flex;
    opacity: 1;
  }
}

.trn-08__code {
  display: block;
  margin-block-start: 9px;
  padding: 8px 9px;
  background: var(--page);
  border: 1px dashed var(--rule);
  border-radius: 4px;
  font: 400 10.5px/1.5 ui-monospace, Menlo, monospace;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.trn-08__foot {
  margin: 14px 0 0;
  font-size: 12px;
  line-height: 1.55;
  color: var(--muted);
}

.trn-08__foot code {
  font: 400 11px/1 ui-monospace, Menlo, monospace;
  color: var(--amber);
}

@media (prefers-reduced-motion: reduce) {
  .trn-08__toast {
    transition: opacity 140ms ease, visibility 0s linear 140ms;
  }

  .trn-08:has(#trn-08-show:checked) .trn-08__toast {
    transition: opacity 140ms ease, visibility 0s linear 0s;
  }
}

@supports (transition-behavior: allow-discrete) {
  @media (prefers-reduced-motion: reduce) {
    .trn-08__toast--good {
      transition: opacity 140ms ease, display 140ms allow-discrete;
    }
  }
}

@media (prefers-color-scheme: light) {
  .trn-08 {
    --page: #f6f1e7;
    --card: #fffdf7;
    --ink: #221d15;
    --muted: #6c6252;
    --rule: #ded5c4;
    --amber: #a86a06;
    --good: #23724a;
    --bad: #b8482a;
  }

  .trn-08__panel {
    box-shadow: 0 10px 0 -4px rgba(34, 29, 21, 0.1);
  }
}

[data-theme="dark"] .trn-08 {
  --page: #211d18;
  --card: #2b261f;
  --ink: #f7f1e6;
  --muted: #a99e8c;
  --rule: #3d372d;
  --amber: #f0a828;
  --good: #7ad39a;
  --bad: #ef7f60;
}

[data-theme="dark"] .trn-08__panel {
  box-shadow: 0 10px 0 -4px rgba(0, 0, 0, 0.35);
}

.trn-08__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-08__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-08__themebtn {
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

.trn-08__themebtn:hover {
  color: var(--ink);
}

.trn-08__themecb:focus-visible + .trn-08__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-08__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-08__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-08__sun {
  opacity: 0.34;
}

.trn-08__moon {
  opacity: 1;
}

.trn-08:has(#trn-08-theme:checked) .trn-08__sun {
  opacity: 1;
}

.trn-08:has(#trn-08-theme:checked) .trn-08__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-08:has(#trn-08-theme:checked) {
    --page: #f6f1e7;
    --card: #fffdf7;
    --ink: #221d15;
    --muted: #6c6252;
    --rule: #ded5c4;
    --amber: #a86a06;
    --good: #23724a;
    --bad: #b8482a;
  }

  .trn-08:has(#trn-08-theme:checked) .trn-08__panel {
    box-shadow: 0 10px 0 -4px rgba(34, 29, 21, 0.1);
  }
}

@media (prefers-color-scheme: light) {
  .trn-08:has(#trn-08-theme:checked) {
    --page: #211d18;
    --page: oklch(0.24 0.014 68);
    --card: #2b261f;
    --card: oklch(0.29 0.016 70);
    --ink: #f7f1e6;
    --ink: oklch(0.96 0.016 82);
    --muted: #a99e8c;
    --muted: oklch(0.73 0.022 80);
    --rule: #3d372d;
    --rule: oklch(0.35 0.018 72);
    --amber: #f0a828;
    --amber: oklch(0.79 0.145 76);
    --good: #7ad39a;
    --good: oklch(0.82 0.12 155);
    --bad: #ef7f60;
    --bad: oklch(0.72 0.15 40);
    --font-display: "Inter Tight", "Helvetica Neue", system-ui, sans-serif;
    background: var(--page);
  }

  .trn-08:has(#trn-08-theme:checked) .trn-08__panel {
    inline-size: 100%;
    max-inline-size: 54rem;
    min-inline-size: 0;
    padding: 14px;
    background: var(--card);
    border-radius: 8px;
    box-shadow: 0 10px 0 -4px rgba(0, 0, 0, 0.35);
  }

  .trn-08:has(#trn-08-theme:checked) .trn-08__sun {
    opacity: 0.34;
  }

  .trn-08:has(#trn-08-theme:checked) .trn-08__moon {
    opacity: 1;
  }
}
```
