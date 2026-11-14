---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/subscription-trial-expiry-countdown-banner/"
title: "Subscription Trial Expiry Countdown Banner"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "An in-app trial banner that escalates as the window closes: a calm purple state with seven days left, a magenta critical state inside the last two days, and…"
has_js: "false"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Subscription Trial Expiry Countdown Banner
Source: https://codefronts.com/snippets/css-countdown-timers/subscription-trial-expiry-countdown-banner/

An in-app trial banner that escalates as the window closes: a calm purple state with seven days left, a magenta critical state inside the last two days, and a depleting bar in both. Dismissal is a checkbox and a :has() rule, so it costs no script — and this is an authenticated surface, not a site-wide promo bar.
## HTML
```html
<section class="cdt-13" aria-labelledby="cdt-13-title">
  <input class="cdt-13__tgl" type="checkbox" id="cdt-13-theme">
  <label class="cdt-13__tglbtn" for="cdt-13-theme">
    <svg class="cdt-13__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-13__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-13__darktext">Dark mode</span><span class="cdt-13__lighttext">Light mode</span>
  </label>
  <div class="cdt-13__stage">
    <h2 class="cdt-13__title" id="cdt-13-title">Trial banner · two escalation states</h2>

    <div class="cdt-13__app">
      <div class="cdt-13__chrome" aria-hidden="true"><span>Quill</span><em>Nova workspace · Alex Chen</em></div>

      <div class="cdt-13__wrap">
        <input class="cdt-13__x" type="checkbox" id="cdt-13-d1">
        <div class="cdt-13__banner" data-state="calm" style="--left: 58%" role="timer">
          <span class="cdt-13__ico" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="17" height="17"><circle cx="10" cy="10" r="7.6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 6v4.3l2.8 1.7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
          </span>
          <p class="cdt-13__copy"><strong><time datetime="P7D">7 days left</time> in your trial.</strong> Keep unlimited documents and version history by adding a plan.</p>
          <div class="cdt-13__act"><button class="cdt-13__btn" type="button">Choose a plan</button></div>
          <label class="cdt-13__close" for="cdt-13-d1" title="Dismiss for this session"><span class="cdt-13__srlabel">Dismiss trial banner for this session</span><svg viewBox="0 0 14 14" width="13" height="13" aria-hidden="true"><path d="M2.5 2.5l9 9M11.5 2.5l-9 9" stroke="currentColor" stroke-width="1.6"/></svg></label>
          <div class="cdt-13__bar" aria-hidden="true"><i></i></div>
        </div>
      </div>

      <div class="cdt-13__wrap">
        <input class="cdt-13__x" type="checkbox" id="cdt-13-d2">
        <div class="cdt-13__banner" data-state="critical" style="--left: 9%" role="timer">
          <span class="cdt-13__ico" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="17" height="17"><path d="M10 2.4 1.6 16.6h16.8L10 2.4Z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 7.4v4.1M10 13.4v1" stroke="currentColor" stroke-width="1.5"/></svg>
          </span>
          <p class="cdt-13__copy"><strong><time datetime="PT41H">41 hours left</time> — then editing locks.</strong> Your documents stay safe and read-only. No card on file yet.</p>
          <div class="cdt-13__act"><button class="cdt-13__btn" type="button">Add payment method</button></div>
          <label class="cdt-13__close" for="cdt-13-d2" title="Dismiss for this session"><span class="cdt-13__srlabel">Dismiss trial banner for this session</span><svg viewBox="0 0 14 14" width="13" height="13" aria-hidden="true"><path d="M2.5 2.5l9 9M11.5 2.5l-9 9" stroke="currentColor" stroke-width="1.6"/></svg></label>
          <div class="cdt-13__bar" aria-hidden="true"><i></i></div>
        </div>
      </div>

      <div class="cdt-13__doc" aria-hidden="true">
        <span class="cdt-13__h"></span><span></span><span></span><span class="cdt-13__short"></span>
      </div>
    </div>

    <p class="cdt-13__note">An authenticated in-app surface scoped to one workspace, not a site-wide promo bar. Dismissal is a checkbox plus a <code>:has()</code> rule, so it lasts for the session and costs no script.</p>
  </div>
</section>
```
## CSS
```css
.cdt-13 {
  --page: #f7f5fd;
  --app: #ffffff;
  --ink: #191430;
  --muted: #675e8c;
  --rule: #e6e1f5;
  --accent: #6d3ce0;
  --crit: #d61f7a;
  --font-display: "Space Grotesk", "Geist", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-13 {
    --page: oklch(97% 0.014 300);
    --app: oklch(100% 0 0);
    --ink: oklch(23% 0.06 300);
    --muted: oklch(50% 0.06 300);
    --rule: oklch(92% 0.02 300);
    --accent: oklch(52% 0.22 295);
    --crit: oklch(56% 0.24 350);
  }
}

.cdt-13 *,
.cdt-13 *::before,
.cdt-13 *::after {
  box-sizing: border-box;
}

.cdt-13__stage {
  display: grid;
  gap: 18px;
  align-content: center;
  min-height: 100vh;
  max-inline-size: 880px;
  margin-inline: auto;
  padding: clamp(16px, 4vw, 48px);
}

.cdt-13__title {
  margin: 0;
  font: 600 clamp(18px, 3vw, 24px)/1.2 var(--font-display);
  letter-spacing: -0.02em;
}

.cdt-13__app {
  padding: 12px;
  background: var(--app);
  border: 1px solid var(--rule);
  border-radius: 16px;
  box-shadow: 0 20px 46px -30px rgba(109, 60, 224, 0.5);
}

.cdt-13__chrome {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 4px 10px;
  padding: 6px 6px 14px;
  border-block-end: 1px solid var(--rule);
}

.cdt-13__chrome span {
  font: 700 14px/1 var(--font-display);
}

.cdt-13__chrome em {
  font: 500 11.5px/1 var(--font-display);
  font-style: normal;
  color: var(--muted);
}

.cdt-13__wrap {
  margin-block-start: 12px;
}

.cdt-13__x {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-13__wrap:has(.cdt-13__x:checked) .cdt-13__banner {
  display: none;
}

.cdt-13__x:focus-visible + .cdt-13__banner .cdt-13__close {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdt-13__banner {
  position: relative;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 6px 10px;
  padding: 12px 40px 14px 12px;
  border-radius: 12px;
  overflow: hidden;
  background: rgba(109, 60, 224, 0.08);
  border: 1px solid rgba(109, 60, 224, 0.24);
  color: var(--accent);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-13__banner {
    background: color-mix(in oklab, var(--accent) 9%, var(--app));
    border-color: color-mix(in oklab, var(--accent) 28%, var(--app));
  }
}

.cdt-13__banner[data-state="critical"] {
  background: rgba(214, 31, 122, 0.1);
  border-color: rgba(214, 31, 122, 0.3);
  color: var(--crit);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-13__banner[data-state="critical"] {
    background: color-mix(in oklab, var(--crit) 11%, var(--app));
    border-color: color-mix(in oklab, var(--crit) 32%, var(--app));
  }
}

.cdt-13__ico {
  display: flex;
  padding-block-start: 1px;
}

.cdt-13__copy {
  grid-column: 2;
  margin: 0;
  min-inline-size: 0;
  font-size: 13px;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-13__copy strong {
  color: inherit;
  font-weight: 600;
}

.cdt-13__banner[data-state="critical"] .cdt-13__copy strong {
  font-weight: 700;
}

.cdt-13__copy time {
  font-variant-numeric: tabular-nums;
}

.cdt-13__act {
  grid-column: 2;
}

.cdt-13__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 11px 16px;
  border: 0;
  border-radius: 9px;
  background: var(--accent);
  color: #fff;
  font: 600 13px/1 var(--font-display);
  cursor: pointer;
}

.cdt-13__banner[data-state="critical"] .cdt-13__btn {
  background: var(--crit);
}

.cdt-13__btn:hover {
  filter: brightness(1.08);
}

.cdt-13__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.cdt-13__close {
  position: absolute;
  inset-block-start: 8px;
  inset-inline-end: 8px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 9px;
  color: inherit;
  cursor: pointer;
}

.cdt-13__close:hover {
  background: rgba(0, 0, 0, 0.06);
}

.cdt-13__srlabel {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-13__bar {
  position: absolute;
  inset-block-end: 0;
  inset-inline: 0;
  block-size: 3px;
  background: rgba(0, 0, 0, 0.08);
}

.cdt-13__bar i {
  display: block;
  block-size: 100%;
  inline-size: var(--left, 50%);
  background: currentColor;
  transition: inline-size 0.6s linear;
}

.cdt-13__doc {
  display: grid;
  gap: 10px;
  padding: 22px 8px 10px;
}

.cdt-13__doc span {
  display: block;
  block-size: 11px;
  border-radius: 6px;
  background: var(--rule);
}

.cdt-13__doc .cdt-13__h {
  inline-size: 42%;
  block-size: 18px;
}

.cdt-13__doc .cdt-13__short {
  inline-size: 64%;
}

.cdt-13__note {
  margin: 0;
  font-size: 12px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-13__note code {
  padding: 1px 5px;
  border-radius: 4px;
  background: var(--rule);
  font: 500 11px/1.4 ui-monospace, Menlo, monospace;
}

@media (prefers-reduced-motion: reduce) {
  .cdt-13__bar i {
    transition: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-13 {
  position: relative;
}

.cdt-13__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-13__tglbtn {
  position: absolute;
  inset-block-end: 14px;
  inset-inline-end: 14px;
  z-index: 20;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 12px 14px;
  border: 1px solid currentColor;
  border-radius: 10px;
  background: transparent;
  color: inherit;
  font: 600 11px/1 system-ui, sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: 0.62;
}

.cdt-13__tglbtn:hover {
  opacity: 1;
}

.cdt-13__tgl:focus-visible + .cdt-13__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-13__tglbtn svg {
  flex: none;
}

.cdt-13__sun,
.cdt-13__lighttext {
  display: none;
}

.cdt-13:has(.cdt-13__tgl:checked) .cdt-13__moon,
.cdt-13:has(.cdt-13__tgl:checked) .cdt-13__darktext {
  display: none;
}

.cdt-13:has(.cdt-13__tgl:checked) .cdt-13__sun {
  display: block;
}

.cdt-13:has(.cdt-13__tgl:checked) .cdt-13__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-13__tglbtn {
    padding: 12px;
  }

  .cdt-13__darktext,
    .cdt-13__lighttext,
    .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__darktext,
    .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-13:has(.cdt-13__tgl:checked) {
    --page: #100c1c;
    --app: #181329;
    --ink: #efeaff;
    --muted: #a599cc;
    --rule: #271f42;
    --accent: #a684ff;
    --crit: #ff5fa8;
  }

  .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__btn {
    color: #100c1c;
    background: var(--accent);
  }

  .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__banner[data-state="critical"] .cdt-13__btn {
    color: #100c1c;
    background: var(--crit);
  }

  .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__close:hover {
    background: rgba(255, 255, 255, 0.08);
  }

  .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__bar {
    background: rgba(255, 255, 255, 0.1);
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-13 {
    --page: #100c1c;
    --app: #181329;
    --ink: #efeaff;
    --muted: #a599cc;
    --rule: #271f42;
    --accent: #a684ff;
    --crit: #ff5fa8;
  }

  .cdt-13__btn {
    color: #100c1c;
    background: var(--accent);
  }

  .cdt-13__banner[data-state="critical"] .cdt-13__btn {
    color: #100c1c;
    background: var(--crit);
  }

  .cdt-13__close:hover {
    background: rgba(255, 255, 255, 0.08);
  }

  .cdt-13__bar {
    background: rgba(255, 255, 255, 0.1);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-13:has(.cdt-13__tgl:checked) {
    --page: oklch(97% 0.014 300);
    --app: oklch(100% 0 0);
    --ink: oklch(23% 0.06 300);
    --muted: oklch(50% 0.06 300);
    --rule: oklch(92% 0.02 300);
    --accent: oklch(52% 0.22 295);
    --crit: oklch(56% 0.24 350);
  }

  .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__btn {
    color: #fff;
    background: var(--accent);
  }

  .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__banner[data-state="critical"] .cdt-13__btn {
    color: #fff;
    background: var(--crit);
  }

  .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__close:hover {
    background: rgba(0, 0, 0, 0.06);
  }

  .cdt-13:has(.cdt-13__tgl:checked) .cdt-13__bar {
    background: rgba(0, 0, 0, 0.08);
  }
}

[data-theme="dark"] .cdt-13 {
  --page: #100c1c;
  --app: #181329;
  --ink: #efeaff;
  --muted: #a599cc;
  --rule: #271f42;
  --accent: #a684ff;
  --crit: #ff5fa8;
}

[data-theme="dark"] .cdt-13 .cdt-13__btn {
  color: #100c1c;
}
```
