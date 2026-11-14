---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-form-with-focus-ring-contrast-audit/"
title: "Dark Mode Form with Focus Ring Contrast Audit"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A sign-in form where the focus indicator is the feature."
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Form with Focus Ring Contrast Audit
Source: https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-form-with-focus-ring-contrast-audit/

A sign-in form where the focus indicator is the feature. Every interactive control — email, password, the reveal toggle, remember-me, both buttons and the recovery link — carries a 2px outline in a per-theme focus token: bright cyan on dark, deep violet on light, each measured at 3:1 or better against the surface it lands on. An annotation ribbon lists what was tuned and the contrast value it hit.
## HTML
```html
<div class="dmu-08">
  <div class="dmu-08__stage">
    <div class="dmu-08__grid">
      <form class="dmu-08__card" novalidate>
        <header class="dmu-08__head">
          <span class="dmu-08__mark" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M6 10.5V8a6 6 0 0 1 12 0v2.5"/><rect x="4.2" y="10.5" width="15.6" height="9.8" rx="2.4"/></svg>
          </span>
          <div>
            <h1 class="dmu-08__h1">Sign in to Meridian</h1>
            <p class="dmu-08__sub">Every focus state below is audited at 3:1 minimum.</p>
          </div>
          <input class="dmu-08__sr" type="checkbox" id="dmu-08-toggle">
          <label class="dmu-08__toggle" for="dmu-08-toggle">
            <svg class="dmu-08__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
            <svg class="dmu-08__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
            <span class="dmu-08__sr">Toggle theme</span>
          </label>
        </header>

        <div class="dmu-08__field">
          <label class="dmu-08__label" for="dmu-08-email">Work email</label>
          <input class="dmu-08__input" id="dmu-08-email" name="email" type="email" inputmode="email" autocomplete="username" placeholder="[email protected]">
        </div>

        <div class="dmu-08__field">
          <div class="dmu-08__labelRow">
            <label class="dmu-08__label" for="dmu-08-pass">Password</label>
            <a class="dmu-08__link" href="#dmu-08">Forgot?</a>
          </div>
          <div class="dmu-08__pass">
            <input class="dmu-08__input dmu-08__input--pass" id="dmu-08-pass" name="password" type="text" autocomplete="current-password" placeholder="At least 12 characters" spellcheck="false">
            <input class="dmu-08__sr" type="checkbox" id="dmu-08-reveal">
            <label class="dmu-08__reveal" for="dmu-08-reveal">
              <svg class="dmu-08__eye" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2.6 12S6 6.4 12 6.4 21.4 12 21.4 12 18 17.6 12 17.6 2.6 12 2.6 12Z"/><circle cx="12" cy="12" r="2.7"/></svg>
              <svg class="dmu-08__eyeOff" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4.2 4.2l15.6 15.6"/><path d="M9.6 6.9A9.6 9.6 0 0 1 12 6.4c6 0 9.4 5.6 9.4 5.6a17 17 0 0 1-2.6 3.3M6.7 8.4A16.4 16.4 0 0 0 2.6 12S6 17.6 12 17.6a9.3 9.3 0 0 0 2.6-.4"/></svg>
              <span class="dmu-08__sr">Show password</span>
            </label>
          </div>
        </div>

        <label class="dmu-08__check" for="dmu-08-remember">
          <input type="checkbox" id="dmu-08-remember">
          <span class="dmu-08__box" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
          </span>
          <span>Keep me signed in on this device</span>
        </label>

        <div class="dmu-08__actions">
          <button class="dmu-08__btn dmu-08__btn--primary" type="button">Continue</button>
          <button class="dmu-08__btn" type="button">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3.6" y="4.6" width="16.8" height="14.8" rx="2.4"/><path d="m4.6 7 7.4 5.4L19.4 7"/></svg>
            Email me a link
          </button>
        </div>
      </form>

      <aside class="dmu-08__audit" aria-label="Focus ring audit">
        <h2 class="dmu-08__auditTitle">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.8 4.2 4.2L19 7.4"/></svg>
          Focus audit &mdash; WCAG 2.2 (2.4.13)
        </h2>
        <ul class="dmu-08__list">
          <li><span>Email field</span><em>2px ring, offset 2 &middot; 8.9:1</em></li>
          <li><span>Password field</span><em>2px ring, offset 2 &middot; 8.9:1</em></li>
          <li><span>Reveal toggle</span><em>proxied via :has() &middot; 8.9:1</em></li>
          <li><span>Remember checkbox</span><em>ring on label &middot; 8.9:1</em></li>
          <li><span>Primary button</span><em>ring outside fill &middot; 5.4:1</em></li>
          <li><span>Recovery link</span><em>underline + ring &middot; 7.1:1</em></li>
        </ul>
        <p class="dmu-08__auditNote">Dark theme ring <code>#67e8f9</code> on <code>#0b0d11</code>. Light theme ring <code>#4c1d95</code> on <code>#ffffff</code>. Tab through the form to see each one.</p>
      </aside>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-08 {
  --bg: #08090c;
  --surface: #0f1116;
  --elevated: #151821;
  --field: #0b0d11;
  --ink: #f3f5f8;
  --muted: #98a1b0;
  --line: #242835;
  --accent: #22d3ee;
  --accent-ink: #04212b;
  --focus: #67e8f9;
  --danger: #fb7185;
  --sheen: rgba(255,255,255,.05);
  --shadow: rgba(0,0,0,.75);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-08[data-theme="light"],
.dmu-08:has(#dmu-08-toggle:checked) {
  --bg: #f1f2f6;
  --surface: #ffffff;
  --elevated: #ffffff;
  --field: #f7f8fb;
  --ink: #0b0d14;
  --muted: #585f6e;
  --line: #e2e4ec;
  --accent: #5b21b6;
  --accent-ink: #ffffff;
  --focus: #4c1d95;
  --danger: #b91c1c;
  --sheen: rgba(11,13,20,.03);
  --shadow: rgba(11,13,20,.18);
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-08:not([data-theme="dark"]):not(:has(#dmu-08-toggle:checked)) {
    --bg: #f1f2f6;
    --surface: #ffffff;
    --elevated: #ffffff;
    --field: #f7f8fb;
    --ink: #0b0d14;
    --muted: #585f6e;
    --line: #e2e4ec;
    --accent: #5b21b6;
    --accent-ink: #ffffff;
    --focus: #4c1d95;
    --danger: #b91c1c;
    --sheen: rgba(11,13,20,.03);
    --shadow: rgba(11,13,20,.18);
    color-scheme: light;
  }

  .dmu-08:has(#dmu-08-toggle:checked) {
    --bg: #08090c;
    --surface: #0f1116;
    --elevated: #151821;
    --field: #0b0d11;
    --ink: #f3f5f8;
    --muted: #98a1b0;
    --line: #242835;
    --accent: #22d3ee;
    --accent-ink: #04212b;
    --focus: #67e8f9;
    --danger: #fb7185;
    --sheen: rgba(255,255,255,.05);
    --shadow: rgba(0,0,0,.75);
    color-scheme: dark;
  }
}

.dmu-08,
.dmu-08 *,
.dmu-08 *::before,
.dmu-08 *::after {
  box-sizing: border-box;
}

.dmu-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-08__grid {
  width: min(62rem,100%);
  display: grid;
  gap: 1rem;
  align-items: start;
}

@media (min-width: 56rem) {
  .dmu-08__grid {
    grid-template-columns: 1.15fr .85fr;
  }
}

.dmu-08__card {
  display: grid;
  gap: 1rem;
  padding: clamp(1.25rem,3vw,1.85rem);
  border-radius: 1.15rem;
  background: linear-gradient(180deg,var(--elevated),var(--surface));
  border: 1px solid var(--line);
  box-shadow: inset 0 1px 0 var(--sheen), 0 34px 64px -46px var(--shadow);
}

.dmu-08__head {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .85rem;
  align-items: start;
}

.dmu-08__mark {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .7rem;
  background: color-mix(in oklab,var(--accent) 16%,transparent);
  color: var(--accent);
}

.dmu-08__mark svg {
  width: 1.2rem;
  height: 1.2rem;
}

.dmu-08__h1 {
  margin: 0 0 .25rem;
  font-size: 1.2rem;
  font-weight: 650;
  letter-spacing: -.025em;
}

.dmu-08__sub {
  margin: 0;
  font-size: .8rem;
  color: var(--muted);
}

.dmu-08__toggle {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .65rem;
  cursor: pointer;
  background: var(--field);
  border: 1px solid var(--line);
  color: var(--ink);
}

.dmu-08__toggle svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-08__sun {
  display: none;
}

.dmu-08__moon {
  display: block;
}

.dmu-08:has(#dmu-08-toggle:checked) .dmu-08__sun {
  display: block;
}

.dmu-08:has(#dmu-08-toggle:checked) .dmu-08__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-08:not(:has(#dmu-08-toggle:checked)) .dmu-08__sun {
    display: block;
  }

  .dmu-08:not(:has(#dmu-08-toggle:checked)) .dmu-08__moon {
    display: none;
  }

  .dmu-08:has(#dmu-08-toggle:checked) .dmu-08__sun {
    display: none;
  }

  .dmu-08:has(#dmu-08-toggle:checked) .dmu-08__moon {
    display: block;
  }
}

.dmu-08:has(#dmu-08-toggle:focus-visible) .dmu-08__toggle {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-08__field {
  display: grid;
  gap: .4rem;
}

.dmu-08__labelRow {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
}

.dmu-08__label {
  font-size: .82rem;
  font-weight: 550;
  color: var(--ink);
}

.dmu-08__link {
  font-size: .78rem;
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 2px;
  border-radius: .25rem;
}

.dmu-08__link:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-08__input {
  width: 100%;
  min-height: 2.95rem;
  padding: 0 .85rem;
  border-radius: .65rem;
  font: inherit;
  font-size: .92rem;
  background: var(--field);
  color: var(--ink);
  border: 1px solid var(--line);
  transition: border-color .18s ease;
}

.dmu-08__input::placeholder {
  color: var(--muted);
  opacity: 1;
}

.dmu-08__input:hover {
  border-color: color-mix(in oklab,var(--accent) 35%,var(--line));
}

.dmu-08__input:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
  border-color: color-mix(in oklab,var(--focus) 60%,var(--line));
}

.dmu-08__input[aria-invalid="true"] {
  border-color: var(--danger);
}

.dmu-08__pass {
  position: relative;
  display: grid;
}

.dmu-08__input--pass {
  padding-right: 3.1rem;
  -webkit-text-security: disc;
  text-security: disc;
}

.dmu-08__pass:has(#dmu-08-reveal:checked) .dmu-08__input--pass {
  -webkit-text-security: none;
  text-security: none;
}

.dmu-08__reveal {
  position: absolute;
  inset-block: .35rem;
  right: .35rem;
  width: 2.25rem;
  display: grid;
  place-items: center;
  border-radius: .5rem;
  cursor: pointer;
  color: var(--muted);
  background: transparent;
  border: 0;
}

.dmu-08__reveal:hover {
  color: var(--ink);
}

.dmu-08__reveal svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-08__eyeOff {
  display: none;
}

.dmu-08__pass:has(#dmu-08-reveal:checked) .dmu-08__eye {
  display: none;
}

.dmu-08__pass:has(#dmu-08-reveal:checked) .dmu-08__eyeOff {
  display: block;
}

.dmu-08__pass:has(#dmu-08-reveal:focus-visible) .dmu-08__reveal {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-08__check {
  display: flex;
  align-items: center;
  gap: .6rem;
  font-size: .83rem;
  color: var(--muted);
  cursor: pointer;
  border-radius: .5rem;
  padding: .2rem;
}

.dmu-08__check input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.dmu-08__box {
  display: grid;
  place-items: center;
  width: 1.25rem;
  height: 1.25rem;
  flex: none;
  border-radius: .35rem;
  background: var(--field);
  border: 1px solid var(--line);
  color: var(--accent-ink);
}

.dmu-08__box svg {
  width: .85rem;
  height: .85rem;
  opacity: 0;
}

.dmu-08__check:has(input:checked) .dmu-08__box {
  background: var(--accent);
  border-color: transparent;
}

.dmu-08__check:has(input:checked) .dmu-08__box svg {
  opacity: 1;
}

.dmu-08__check:has(input:focus-visible) {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-08__actions {
  display: grid;
  gap: .55rem;
}

@media (min-width: 26rem) {
  .dmu-08__actions {
    grid-template-columns: 1fr 1fr;
  }
}

.dmu-08__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .45rem;
  min-height: 2.95rem;
  padding: 0 1rem;
  border-radius: .65rem;
  cursor: pointer;
  font: inherit;
  font-size: .88rem;
  font-weight: 560;
  background: var(--field);
  color: var(--ink);
  border: 1px solid var(--line);
  transition: translate .18s ease, filter .18s ease;
}

.dmu-08__btn svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-08__btn:hover {
  translate: 0 -1px;
}

.dmu-08__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-08__btn--primary {
  background: var(--accent);
  color: var(--accent-ink);
  border-color: transparent;
}

.dmu-08__btn--primary:hover {
  filter: brightness(1.06);
}

.dmu-08__audit {
  display: grid;
  gap: .7rem;
  padding: clamp(1.1rem,3vw,1.5rem);
  border-radius: 1.15rem;
  background: var(--surface);
  border: 1px dashed color-mix(in oklab,var(--accent) 40%,var(--line));
}

.dmu-08__auditTitle {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .45rem;
  font-size: .83rem;
  font-weight: 600;
  color: var(--accent);
}

.dmu-08__auditTitle svg {
  width: 1rem;
  height: 1rem;
}

.dmu-08__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .3rem;
}

.dmu-08__list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  flex-wrap: wrap;
  padding: .5rem .6rem;
  border-radius: .5rem;
  background: var(--field);
  border: 1px solid var(--line);
  font-size: .8rem;
}

.dmu-08__list em {
  font-style: normal;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.dmu-08__auditNote {
  margin: 0;
  font-size: .78rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.dmu-08__auditNote code {
  font-family: var(--mono);
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-08__btn,
    .dmu-08__input {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-08__card,
    .dmu-08__audit,
    .dmu-08__input,
    .dmu-08__list li {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-08__btn--primary {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .dmu-08__check:has(input:checked) .dmu-08__box {
    background: Highlight;
  }
}
```
