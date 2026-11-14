---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-button-with-animated-toast-notification/"
title: "CSS Copy Button with Animated Toast Notification"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "When the button is far from where the user is looking, the confirmation has to come to them."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy Button with Animated Toast Notification
Source: https://codefronts.com/snippets/css-copy-button/css-copy-button-with-animated-toast-notification/

When the button is far from where the user is looking, the confirmation has to come to them. A minimal toast slides up from the bottom, announces itself politely, and dismisses after 2.4&nbsp;s &mdash; and rapid clicks restart the timer instead of stacking toasts. The toast is intentionally plain: the button is still the subject.
## HTML
```html
<div class="cpy-16">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-16__sr" type="checkbox" id="cpy-16-dark">
  <label class="cpy-16__theme" for="cpy-16-dark" title="Switch light or dark theme">
    <svg class="cpy-16__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-16__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-16__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-16__stage">
    <div class="cpy-16__card">
      <p class="cpy-16__eyebrow">Toast confirmation</p>
      <h2 class="cpy-16__title">Feedback that travels</h2>
      <p class="cpy-16__lead">The button is at the top of a long page; the confirmation appears where the user is looking. Click it repeatedly &mdash; you get one toast that restarts, never a stack.</p>

      <div class="cpy-16__row">
        <div class="cpy-16__meta">
          <span class="cpy-16__key">Invite code</span>
          <code class="cpy-16__value" id="cpy-16-value">CF-2027-TEAM-9X4K</code>
        </div>
        <button class="cpy-16__btn" type="button">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          Copy invite code
        </button>
      </div>
      <p class="cpy-16__note">The toast is deliberately minimal &mdash; one line, one icon, no actions. The button stays the subject.</p>
    </div>
  </div>

  <div class="cpy-16__toast" id="cpy-16-toast" role="status" aria-live="polite" data-open="0" data-kind="ok" hidden>
    <svg class="cpy-16__tok" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <span class="cpy-16__ttext">Copied to clipboard</span>
  </div>
</div>
```
## CSS
```css
.cpy-16 {
  --bg: #f6f7f9;
  --panel: #ffffff;
  --panel2: #f0f2f6;
  --ink: #0b0e17;
  --muted: #5a6270;
  --line: rgba(11,14,23,.12);
  --accent: #4f46e5;
  --ok: #15803d;
  --err: #dc2626;
  --dur: 200ms;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cpy-16 *,
.cpy-16 *::before,
.cpy-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-16 {
    --accent: oklch(.53 .21 274);
    --ok: oklch(.55 .15 149);
    --err: oklch(.58 .21 25);
  }
}

.cpy-16__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-16__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-16__theme {
  position: absolute;
  inset-block-start: clamp(1rem,3vw,1.75rem);
  inset-inline-end: clamp(1rem,3vw,1.75rem);
  z-index: 3;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.6);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: var(--ink);
  cursor: pointer;
}

.cpy-16__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-16__moon {
  display: none;
}

.cpy-16__sr:focus-visible + .cpy-16__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-16__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-16__card {
  inline-size: min(100%,34rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .85rem;
  box-shadow: 0 1px 2px rgba(11,14,23,.05),0 28px 55px -36px rgba(11,14,23,.34);
}

.cpy-16__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-16__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-16__lead {
  margin: 0 0 .3rem;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-16__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1.1rem;
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--panel2);
}

.cpy-16__meta {
  display: grid;
  gap: .2rem;
  min-inline-size: 0;
}

.cpy-16__key {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-16__value {
  font-family: var(--mono);
  font-size: clamp(.9rem,2.4vw,1.1rem);
  letter-spacing: .02em;
  user-select: all;
}

.cpy-16__btn {
  flex: none;
  min-block-size: 2.85rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding-inline: 1.1rem;
  border: 1px solid transparent;
  border-radius: .8rem;
  background: var(--accent);
  color: #fff;
  font: inherit;
  font-size: .9rem;
  font-weight: 560;
  cursor: pointer;
  transition: background var(--dur),scale var(--dur);
}

.cpy-16__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.cpy-16__btn:hover {
  background: color-mix(in srgb,var(--accent) 88%,#000);
}

.cpy-16__btn:active {
  scale: .975;
}

.cpy-16__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.cpy-16__note {
  margin: 0;
  font-size: .84rem;
  line-height: 1.55;
  color: var(--muted);
}

.cpy-16__toast {
  position: fixed;
  inset-block-end: clamp(1rem,4vw,2rem);
  inset-inline: 0;
  z-index: 20;
  margin-inline: auto;
  inline-size: max-content;
  max-inline-size: calc(100% - 2rem);
  display: flex;
  align-items: center;
  gap: .55rem;
  padding: .7rem 1rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: var(--ink);
  color: var(--panel);
  font-size: .88rem;
  font-weight: 540;
  box-shadow: 0 18px 40px -20px rgba(0,0,0,.5);
  opacity: 0;
  translate: 0 .9rem;
  transition: opacity 180ms ease,translate 180ms ease;
}

.cpy-16__toast[hidden] {
  display: none;
}

.cpy-16__toast[data-open="1"] {
  opacity: 1;
  translate: 0 0;
  transition-duration: 220ms;
}

.cpy-16__tok {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  color: #4ade80;
  flex: none;
}

.cpy-16__toast[data-kind="err"] .cpy-16__tok {
  color: #fda4af;
}

@media not (prefers-color-scheme: dark) {
  .cpy-16:has(#cpy-16-dark:checked) {
    --bg: #07080f;
    --panel: #0d1017;
    --panel2: #161a24;
    --ink: #e9ebf3;
    --muted: rgba(233,235,243,.6);
    --line: rgba(233,235,243,.14);
    --accent: #818cf8;
    --ok: #6ee7a8;
  }

  .cpy-16:has(#cpy-16-dark:checked) .cpy-16__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-16:has(#cpy-16-dark:checked) .cpy-16__sun {
    display: none;
  }

  .cpy-16:has(#cpy-16-dark:checked) .cpy-16__moon {
    display: block;
  }

  .cpy-16:has(#cpy-16-dark:checked) .cpy-16__toast {
    background: #1b2030;
    color: #e9ebf3;
  }

  .cpy-16:has(#cpy-16-dark:checked) .cpy-16__btn {
    color: #0b0e17;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-16:not([data-theme="light"]):not(:has(#cpy-16-dark:checked)) {
    --bg: #07080f;
    --panel: #0d1017;
    --panel2: #161a24;
    --ink: #e9ebf3;
    --muted: rgba(233,235,243,.6);
    --line: rgba(233,235,243,.14);
    --accent: #818cf8;
    --ok: #6ee7a8;
  }

  .cpy-16__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-16__sun {
    display: none;
  }

  .cpy-16__moon {
    display: block;
  }

  .cpy-16:has(#cpy-16-dark:checked) .cpy-16__sun {
    display: block;
  }

  .cpy-16:has(#cpy-16-dark:checked) .cpy-16__moon {
    display: none;
  }

  .cpy-16__toast {
    background: #1b2030;
    color: #e9ebf3;
  }

  .cpy-16__btn {
    color: #0b0e17;
  }
}

.cpy-16[data-theme="dark"] {
  --bg: #07080f;
  --panel: #0d1017;
  --panel2: #161a24;
  --ink: #e9ebf3;
  --muted: rgba(233,235,243,.6);
  --line: rgba(233,235,243,.14);
  --accent: #818cf8;
  --ok: #6ee7a8;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-16 *,
    .cpy-16 *::before,
    .cpy-16 *::after {
    transition: none !important;
    animation: none !important;
  }

  .cpy-16__toast {
    translate: 0 0;
  }
}

@media (forced-colors: active) {
  .cpy-16__card,
    .cpy-16__row,
    .cpy-16__btn,
    .cpy-16__theme,
    .cpy-16__toast {
    border: 1px solid CanvasText;
    background: Canvas;
    color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```

## JavaScript
```js
const cpy16 = document.querySelector('.cpy-16');
if (cpy16) {
  const btn = cpy16.querySelector('.cpy-16__btn');
  const value = cpy16.querySelector('#cpy-16-value');
  const toast = cpy16.querySelector('#cpy-16-toast');
  const text = cpy16.querySelector('.cpy-16__ttext');
  let hide, strip;
  const show = (message, kind) => {
    text.textContent = message;
    toast.dataset.kind = kind;
    toast.hidden = false;
    requestAnimationFrame(() => { toast.dataset.open = '1'; });   // one frame, or no transition
    clearTimeout(hide); clearTimeout(strip);                       // restart, never stack
    hide = setTimeout(() => {
      toast.dataset.open = '0';
      strip = setTimeout(() => { toast.hidden = true; }, 220);
    }, 2400);
  };
  btn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(value.textContent.trim());
      show('Copied to clipboard', 'ok');
    } catch {
      show('Copy blocked - press Ctrl C instead', 'err');
    }
  });
}
```
