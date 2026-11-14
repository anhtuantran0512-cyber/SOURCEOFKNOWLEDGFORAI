---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/modal-open-close-transition/"
title: "Entry Transitions with starting-style"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "An element entering the DOM or the top layer has no previous computed value, so there is nothing for a transition to start from — which is why entry…"
has_js: "true"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Entry Transitions with starting-style
Source: https://codefronts.com/motion/css-transition-designs/modal-open-close-transition/

An element entering the DOM or the top layer has no previous computed value, so there is nothing for a transition to start from — which is why entry animations used to need a keyframe or a forced reflow. @starting-style declares that before-state. Shown on a deliberately plain <dialog>: the chrome is minimal because the lesson is the entry transition, not the modal.
## HTML
```html
<section class="trn-11" aria-labelledby="trn-11-heading">
  <div class="trn-11__stage">
    <div class="trn-11__theme">
      <input class="trn-11__themecb" type="checkbox" id="trn-11-theme">
      <label class="trn-11__themebtn" for="trn-11-theme">
        <span class="trn-11__themeico" aria-hidden="true">
          <svg class="trn-11__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-11__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-11__head">
      <p class="trn-11__kicker">@starting-style</p>
      <h2 class="trn-11__heading" id="trn-11-heading">Giving an entering element a frame to start from</h2>
      <p class="trn-11__sub">The dialog below is intentionally plain. What matters is that it enters and leaves with a transition and no keyframes.</p>
    </header>

    <div class="trn-11__card">
      <button class="trn-11__open" id="trn-11-open" type="button">Open access review</button>
      <dl class="trn-11__spec">
        <dt>entry</dt><dd>@starting-style { opacity: 0; transform: translateY(10px) scale(.98) }</dd>
        <dt>exit</dt><dd>transition: display .26s allow-discrete, overlay .26s allow-discrete</dd>
        <dt>backdrop</dt><dd>::backdrop gets its own @starting-style block</dd>
      </dl>
    </div>

    <dialog class="trn-11__dialog" id="trn-11-dialog" aria-labelledby="trn-11-dtitle" hidden>
      <h3 class="trn-11__dtitle" id="trn-11-dtitle">Access review</h3>
      <p class="trn-11__dbody">Sam Rivera requested write access to the Prism production warehouse. The grant expires in 30 days unless renewed.</p>
      <div class="trn-11__drow">
        <button class="trn-11__ghost" type="button" data-trn-11-close>Deny</button>
        <button class="trn-11__primary" type="button" data-trn-11-close>Approve for 30 days</button>
      </div>
    </dialog>

    <p class="trn-11__foot">Without <code>@starting-style</code> the panel appears at full opacity and only the exit animates — the classic half-built modal transition.</p>
  </div>
</section>
```
## CSS
```css
.trn-11 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f6f7f9;
  --page: oklch(0.97 0.003 264);
  --card: rgba(255, 255, 255, 0.72);
  --ink: #18181b;
  --ink: oklch(0.21 0.005 286);
  --muted: #62626b;
  --muted: oklch(0.5 0.008 286);
  --rule: #dcdce2;
  --rule: oklch(0.89 0.005 286);
  --accent: #6d4aff;
  --accent: oklch(0.56 0.22 288);
  --dur: 260ms;
  --font-display: "Geist", "SF Pro Display", system-ui, -apple-system, sans-serif;
  background: radial-gradient(60% 50% at 12% 8%, rgba(109, 74, 255, 0.16), transparent 70%), radial-gradient(50% 45% at 88% 30%, rgba(45, 212, 191, 0.14), transparent 70%), var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-11 *,
.trn-11 *::before,
.trn-11 *::after {
  box-sizing: border-box;
}

.trn-11__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(28px, 6vw, 64px) 16px;
}

.trn-11__head {
  inline-size: 100%;
  max-inline-size: 46rem;
  min-inline-size: 0;
  margin: 0 0 24px;
}

.trn-11__kicker {
  margin: 0 0 12px;
  font: 500 11.5px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.06em;
  color: var(--accent);
}

.trn-11__heading {
  margin: 0 0 10px;
  font: 600 clamp(24px, 4.6vw, 35px)/1.12 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.trn-11__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-11__card {
  inline-size: 100%;
  max-inline-size: 46rem;
  min-inline-size: 0;
  padding: 20px;
  background: var(--card);
  border: 1px solid rgba(255, 255, 255, 0.6);
  border-radius: 16px;
  -webkit-backdrop-filter: blur(14px) saturate(1.4);
  backdrop-filter: blur(14px) saturate(1.4);
  box-shadow: 0 20px 50px -30px rgba(24, 24, 27, 0.4);
}

.trn-11__open {
  min-height: 44px;
  padding: 0 20px;
  border: 0;
  border-radius: 10px;
  background: var(--accent);
  color: #fff;
  cursor: pointer;
  font: 600 14px/1 var(--font-display);
  letter-spacing: -0.01em;
  transition: transform 180ms cubic-bezier(.2, .8, .3, 1), box-shadow 180ms ease;
}

.trn-11__open:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 26px -14px var(--accent);
}

.trn-11__open:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.trn-11__spec {
  margin: 20px 0 0;
  display: grid;
  grid-template-columns: minmax(0, 5.5rem) minmax(0, 1fr);
}

.trn-11__spec dt {
  padding: 10px 12px 10px 0;
  border-block-start: 1px solid var(--rule);
  font: 500 11.5px/1.4 ui-monospace, Menlo, monospace;
  color: var(--accent);
  min-inline-size: 0;
}

.trn-11__spec dd {
  margin: 0;
  padding: 10px 0;
  border-block-start: 1px solid var(--rule);
  font: 400 11.5px/1.5 ui-monospace, Menlo, monospace;
  color: var(--muted);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.trn-11__dialog {
  inline-size: min(92vw, 27rem);
  padding: 22px;
  border: 1px solid var(--rule);
  border-radius: 16px;
  background: #fff;
  color: var(--ink);
  box-shadow: 0 30px 70px -40px rgba(24, 24, 27, 0.6);
}

.trn-11__dialog[hidden] {
  display: none;
}

.trn-11__dtitle {
  margin: 0 0 10px;
  font: 600 18px/1.2 var(--font-display);
  letter-spacing: -0.02em;
}

.trn-11__dbody {
  margin: 0 0 18px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-11__drow {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: flex-end;
}

.trn-11__ghost,
.trn-11__primary {
  min-height: 44px;
  padding: 0 16px;
  border-radius: 9px;
  font: 600 13.5px/1 var(--font-display);
  cursor: pointer;
  transition: background-color 160ms ease, color 160ms ease;
}

.trn-11__ghost {
  background: transparent;
  border: 1px solid var(--rule);
  color: var(--muted);
}

.trn-11__ghost:hover {
  background: var(--page);
  color: var(--ink);
}

.trn-11__primary {
  background: var(--accent);
  border: 0;
  color: #fff;
}

.trn-11__primary:hover {
  background: #5836e0;
}

.trn-11__ghost:focus-visible,
.trn-11__primary:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

@supports (transition-behavior: allow-discrete) {
  .trn-11__dialog {
    opacity: 0;
    transform: translateY(10px) scale(0.98);
    transition: opacity var(--dur) ease, transform var(--dur) cubic-bezier(.2, .8, .3, 1), display var(--dur) allow-discrete, overlay var(--dur) allow-discrete;
  }

  .trn-11__dialog[open] {
    opacity: 1;
    transform: translateY(0) scale(1);
  }

  @starting-style {
    .trn-11__dialog[open] {
      opacity: 0;
      transform: translateY(10px) scale(0.98);
    }
  }

  .trn-11__dialog::backdrop {
    background: rgba(24, 24, 27, 0.42);
    opacity: 0;
    transition: opacity var(--dur) ease, display var(--dur) allow-discrete, overlay var(--dur) allow-discrete;
  }

  .trn-11__dialog[open]::backdrop {
    opacity: 1;
  }

  @starting-style {
    .trn-11__dialog[open]::backdrop {
      opacity: 0;
    }
  }
}

.trn-11__foot {
  inline-size: 100%;
  max-inline-size: 46rem;
  margin: 20px 0 0;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

.trn-11__foot code {
  font: 400 11.5px/1 ui-monospace, Menlo, monospace;
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .trn-11__open {
    transition: box-shadow 140ms ease;
  }

  .trn-11__open:hover {
    transform: none;
  }

  @supports (transition-behavior: allow-discrete) {
    .trn-11__dialog {
      transform: none;
      transition: opacity 140ms ease, display 140ms allow-discrete, overlay 140ms allow-discrete;
    }

    .trn-11__dialog[open] {
      transform: none;
    }

    @starting-style {
      .trn-11__dialog[open] {
        opacity: 0;
        transform: none;
      }
    }
  }
}

@media (prefers-color-scheme: dark) {
  .trn-11 {
    --page: #0c0c0f;
    --page: oklch(0.16 0.005 286);
    --card: rgba(24, 24, 28, 0.66);
    --ink: #f2f2f5;
    --ink: oklch(0.96 0.003 286);
    --muted: #a0a0ac;
    --muted: oklch(0.72 0.008 286);
    --rule: #2a2a31;
    --rule: oklch(0.29 0.008 286);
    --accent: #9d84ff;
    --accent: oklch(0.74 0.16 290);
    background: radial-gradient(60% 50% at 12% 8%, rgba(157, 132, 255, 0.2), transparent 70%), radial-gradient(50% 45% at 88% 30%, rgba(45, 212, 191, 0.12), transparent 70%), var(--page);
  }

  .trn-11__card {
    border-color: rgba(255, 255, 255, 0.08);
  }

  .trn-11__dialog {
    background: #16161a;
  }

  .trn-11__open,
    .trn-11__primary {
    color: #0c0c0f;
  }

  .trn-11__primary:hover {
    background: #b6a2ff;
  }
}

[data-theme="dark"] .trn-11 {
  --page: #0c0c0f;
  --card: rgba(24, 24, 28, 0.66);
  --ink: #f2f2f5;
  --muted: #a0a0ac;
  --rule: #2a2a31;
  --accent: #9d84ff;
}

[data-theme="dark"] .trn-11__card {
  border-color: rgba(255, 255, 255, 0.08);
}

[data-theme="dark"] .trn-11__dialog {
  background: #16161a;
}

[data-theme="dark"] .trn-11__open,
[data-theme="dark"] .trn-11__primary {
  color: #0c0c0f;
}

.trn-11__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-11__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-11__themebtn {
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

.trn-11__themebtn:hover {
  color: var(--ink);
}

.trn-11__themecb:focus-visible + .trn-11__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-11__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-11__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-11__sun {
  opacity: 1;
}

.trn-11__moon {
  opacity: 0.34;
}

.trn-11:has(#trn-11-theme:checked) .trn-11__sun {
  opacity: 0.34;
}

.trn-11:has(#trn-11-theme:checked) .trn-11__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-11:has(#trn-11-theme:checked) {
    --page: #0c0c0f;
    --page: oklch(0.16 0.005 286);
    --card: rgba(24, 24, 28, 0.66);
    --ink: #f2f2f5;
    --ink: oklch(0.96 0.003 286);
    --muted: #a0a0ac;
    --muted: oklch(0.72 0.008 286);
    --rule: #2a2a31;
    --rule: oklch(0.29 0.008 286);
    --accent: #9d84ff;
    --accent: oklch(0.74 0.16 290);
    background: radial-gradient(60% 50% at 12% 8%, rgba(157, 132, 255, 0.2), transparent 70%), radial-gradient(50% 45% at 88% 30%, rgba(45, 212, 191, 0.12), transparent 70%), var(--page);
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__card {
    border-color: rgba(255, 255, 255, 0.08);
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__dialog {
    background: #16161a;
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__open,
    .trn-11:has(#trn-11-theme:checked) .trn-11__primary {
    color: #0c0c0f;
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__primary:hover {
    background: #b6a2ff;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-11:has(#trn-11-theme:checked) .trn-11__open,
    .trn-11:has(#trn-11-theme:checked) .trn-11__primary {
    color: #fff;
  }

  .trn-11:has(#trn-11-theme:checked) {
    --page: #f6f7f9;
    --page: oklch(0.97 0.003 264);
    --card: rgba(255, 255, 255, 0.72);
    --ink: #18181b;
    --ink: oklch(0.21 0.005 286);
    --muted: #62626b;
    --muted: oklch(0.5 0.008 286);
    --rule: #dcdce2;
    --rule: oklch(0.89 0.005 286);
    --accent: #6d4aff;
    --accent: oklch(0.56 0.22 288);
    --dur: 260ms;
    --font-display: "Geist", "SF Pro Display", system-ui, -apple-system, sans-serif;
    background: radial-gradient(60% 50% at 12% 8%, rgba(109, 74, 255, 0.16), transparent 70%), radial-gradient(50% 45% at 88% 30%, rgba(45, 212, 191, 0.14), transparent 70%), var(--page);
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__card {
    inline-size: 100%;
    max-inline-size: 46rem;
    min-inline-size: 0;
    padding: 20px;
    background: var(--card);
    border: 1px solid rgba(255, 255, 255, 0.6);
    border-radius: 16px;
    -webkit-backdrop-filter: blur(14px) saturate(1.4);
    backdrop-filter: blur(14px) saturate(1.4);
    box-shadow: 0 20px 50px -30px rgba(24, 24, 27, 0.4);
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__dialog {
    inline-size: min(92vw, 27rem);
    padding: 22px;
    border: 1px solid var(--rule);
    border-radius: 16px;
    background: #fff;
    color: var(--ink);
    box-shadow: 0 30px 70px -40px rgba(24, 24, 27, 0.6);
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__primary:hover {
    background: #5836e0;
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__sun {
    opacity: 1;
  }

  .trn-11:has(#trn-11-theme:checked) .trn-11__moon {
    opacity: 0.34;
  }
}
```

## JavaScript
```js
const trn11 = document.querySelector('.trn-11');
if (trn11) {
  const dialog = trn11.querySelector('#trn-11-dialog');
  const opener = trn11.querySelector('#trn-11-open');
  opener.addEventListener('click', () => {
    dialog.removeAttribute('hidden');
    if (typeof dialog.showModal === 'function') dialog.showModal();
    else dialog.setAttribute('open', '');
  });
  for (const btn of dialog.querySelectorAll('[data-trn-11-close]')) {
    btn.addEventListener('click', () => dialog.close());
  }
  dialog.addEventListener('close', () => {
    setTimeout(() => dialog.setAttribute('hidden', ''), 300);
  });
}
```
