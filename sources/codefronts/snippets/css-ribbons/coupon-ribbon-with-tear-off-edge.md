---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/coupon-ribbon-with-tear-off-edge/"
title: "Coupon Ribbon with Tear-Off Edge"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "A voucher with a real perforation: semicircular bites punched out of both edges and a dashed tear line between the stub and the body."
has_js: "true"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Coupon Ribbon with Tear-Off Edge
Source: https://codefronts.com/snippets/css-ribbons/coupon-ribbon-with-tear-off-edge/

A voucher with a real perforation: semicircular bites punched out of both edges and a dashed tear line between the stub and the body. The notches are carved with mask layers rather than covered with background-coloured circles, so the coupon sits correctly on any page colour, gradient or photograph. Copying the code is one button with proper success feedback.
## HTML
```html
<section class="rib-15" aria-label="Coupon ribbon with dashed tear off edge demo">
  <div class="rib-15__stage">
    <div class="rib-15__coupon">
      <div class="rib-15__stub">
        <span class="rib-15__pct">25<span>%</span></span>
        <span class="rib-15__off">OFF</span>
      </div>
      <span class="rib-15__tear" aria-hidden="true"></span>
      <div class="rib-15__body">
        <p class="rib-15__brand">Northbound Coffee Roasters</p>
        <h2 class="rib-15__title">Quarter off your first subscription box</h2>
        <p class="rib-15__terms">Valid until <time datetime="2026-09-30">30 Sep 2026</time> · One use per customer · Excludes gift cards</p>
        <div class="rib-15__coderow">
          <code class="rib-15__code" id="rib-15-code">FIRSTPOUR25</code>
          <button class="rib-15__copy" type="button" data-copy="FIRSTPOUR25">
            <svg class="rib-15__ic rib-15__ic--copy" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path fill="currentColor" d="M9 2h9a3 3 0 0 1 3 3v9h-2V5a1 1 0 0 0-1-1H9V2Zm-3 4h9a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V9a3 3 0 0 1 3-3Z"/></svg>
            <svg class="rib-15__ic rib-15__ic--ok" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path fill="currentColor" d="m9.6 16.4-4-4L4.2 13.8l5.4 5.4 10-10-1.4-1.4z"/></svg>
            <span class="rib-15__copytxt">Copy code</span>
          </button>
        </div>
      </div>
    </div>
    <p class="rib-15__live" role="status"></p>
    <p class="rib-15__chip" aria-hidden="true">mask-composite: intersect notches · dashed border tear line · clipboard with fallback</p>
  </div>
</section>
```
## CSS
```css
.rib-15,
.rib-15 *,
.rib-15 *::before,
.rib-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-15-ink: #211c16;
  --rib-15-ink: oklch(0.24 0.018 66);
  --rib-15-mut: #6d6357;
  --rib-15-mut: oklch(0.55 0.02 70);
  --rib-15-paper: #fffaf1;
  --rib-15-paper: oklch(0.99 0.014 88);
  --rib-15-acc: #b4442a;
  --rib-15-acc: oklch(0.55 0.17 38);
  --rib-15-r: 14px;
  --rib-15-x: 34%;
  background: #2b2015;
  background: linear-gradient(150deg,oklch(0.32 0.04 60),oklch(0.24 0.03 40));
  color: var(--rib-15-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(14px,3vw,22px);
  padding: clamp(20px,5vw,56px);
  background-image: radial-gradient(oklch(1 0 0/.045) 1px,transparent 1px);
  background-size: 18px 18px;
}

.rib-15__coupon {
  position: relative;
  display: grid;
  grid-template-columns: var(--rib-15-x) 1fr;
  width: min(100%,640px);
  border-radius: 20px;
  background: var(--rib-15-paper);
  filter: drop-shadow(0 24px 40px oklch(0 0 0/.5));
  -webkit-mask-image: radial-gradient(circle var(--rib-15-r) at var(--rib-15-x) 0,transparent 98%,#000 100%),radial-gradient(circle var(--rib-15-r) at var(--rib-15-x) 100%,transparent 98%,#000 100%);
  -webkit-mask-composite: source-in;
  mask-image: radial-gradient(circle var(--rib-15-r) at var(--rib-15-x) 0,transparent 98%,#000 100%),radial-gradient(circle var(--rib-15-r) at var(--rib-15-x) 100%,transparent 98%,#000 100%);
  mask-composite: intersect;
}

.rib-15__stub {
  display: grid;
  place-items: center;
  align-content: center;
  gap: 2px;
  padding: clamp(20px,4vw,30px) 10px;
  color: oklch(0.99 0.01 88);
  background: #b4442a;
  background: linear-gradient(160deg,color-mix(in oklch,var(--rib-15-acc) 100%,white 12%),var(--rib-15-acc) 60%,color-mix(in oklch,var(--rib-15-acc) 82%,black 12%));
  border-radius: 20px 0 0 20px;
}

.rib-15__pct {
  font-size: clamp(38px,8vw,58px);
  font-weight: 800;
  letter-spacing: -.05em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.rib-15__pct span {
  font-size: .46em;
  font-weight: 700;
  margin-inline-start: 2px;
}

.rib-15__off {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .3em;
  opacity: .9;
}

.rib-15__tear {
  position: absolute;
  inset-block: var(--rib-15-r);
  inset-inline-start: var(--rib-15-x);
  border-inline-start: 2px dashed color-mix(in oklch,var(--rib-15-ink) 24%,transparent);
  pointer-events: none;
}

.rib-15__body {
  display: grid;
  gap: 9px;
  padding: clamp(20px,4vw,30px);
}

.rib-15__brand {
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--rib-15-acc);
}

.rib-15__title {
  font-size: clamp(18px,3.4vw,24px);
  font-weight: 660;
  line-height: 1.22;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.rib-15__terms {
  font-size: 12px;
  line-height: 1.5;
  color: var(--rib-15-mut);
  text-wrap: pretty;
}

.rib-15__coderow {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-block-start: 6px;
}

.rib-15__code {
  flex: 1 1 150px;
  display: grid;
  place-items: center;
  min-height: 48px;
  padding-inline: 14px;
  border-radius: 11px;
  border: 2px dashed color-mix(in oklch,var(--rib-15-ink) 26%,transparent);
  background: color-mix(in oklch,var(--rib-15-acc) 6%,transparent);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: .12em;
  user-select: all;
}

.rib-15__copy {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 48px;
  padding-inline: 18px;
  border: 0;
  border-radius: 11px;
  background: var(--rib-15-ink);
  color: oklch(0.98 0.01 88);
  font: inherit;
  font-size: 14px;
  font-weight: 640;
  cursor: pointer;
  transition: background .25s,translate .2s;
}

.rib-15__copy:hover {
  translate: 0 -1px;
  background: color-mix(in oklch,var(--rib-15-ink) 82%,var(--rib-15-acc));
}

.rib-15__copy:focus-visible {
  outline: 3px solid var(--rib-15-acc);
  outline-offset: 3px;
}

.rib-15__copy[data-state="copied"] {
  background: oklch(0.5 0.13 152);
}

.rib-15__ic--ok,
.rib-15__copy[data-state="copied"] .rib-15__ic--copy {
  display: none;
}

.rib-15__copy[data-state="copied"] .rib-15__ic--ok {
  display: block;
}

.rib-15__live {
  font-size: 12.5px;
  color: oklch(0.85 0.02 80);
  min-height: 1.2em;
}

.rib-15__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: oklch(0.8 0.02 80);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
  text-align: center;
}

@media (max-width: 520px) {
  .rib-15__coupon {
    grid-template-columns: 1fr;
    --rib-15-x: 100%;
  }

  .rib-15__stub {
    border-radius: 20px 20px 0 0;
  }

  .rib-15__tear {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rib-15 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.rib-15__stage').forEach((stage) => {
    if (stage.dataset.wired) return;
    stage.dataset.wired = '1';
    const btn = stage.querySelector('.rib-15__copy');
    const live = stage.querySelector('.rib-15__live');
    const label = stage.querySelector('.rib-15__copytxt');
    const codeEl = stage.querySelector('.rib-15__code');
    let timer = 0;

    const confirm = (code) => {
      btn.dataset.state = 'copied';
      label.textContent = 'Copied';
      live.textContent = 'Discount code ' + code + ' copied to clipboard.';
      clearTimeout(timer);
      timer = setTimeout(() => { btn.dataset.state = ''; label.textContent = 'Copy code'; }, 1900);
    };

    btn.addEventListener('click', async () => {
      const code = btn.dataset.copy;
      try {
        // Requires a secure context (https / localhost) and a user gesture.
        await navigator.clipboard.writeText(code);
        confirm(code);
      } catch {
        // Fallback: select the code so the user can copy it manually.
        const range = document.createRange();
        range.selectNodeContents(codeEl);
        const sel = getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        live.textContent = 'Code selected — press Ctrl or Cmd + C to copy.';
      }
    });
  });
})();
```
