---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-ui-with-light-dark-css-function/"
title: "Dark Mode UI with light-dark CSS Function"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "The modern way to write a theme: no media query at all."
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode UI with light-dark CSS Function
Source: https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-ui-with-light-dark-css-function/

The modern way to write a theme: no media query at all. Set color-scheme: light dark and declare every token once as light-dark(<light>, <dark>). The function resolves against the element's effective colour scheme at compute time, so changing color-scheme anywhere re-themes the whole subtree — which makes the toggle a single property change instead of a second token block.
## HTML
```html
<div class="dmu-04">
  <div class="dmu-04__stage">
    <div class="dmu-04__shell">
      <header class="dmu-04__bar">
        <div class="dmu-04__id">
          <span class="dmu-04__mark" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="8.2"/><path d="M12 3.8a8.2 8.2 0 0 1 0 16.4Z" fill="currentColor" stroke="none"/></svg>
          </span>
          <div>
            <p class="dmu-04__name">light-dark()</p>
            <p class="dmu-04__sub">one token, both themes</p>
          </div>
        </div>
        <input class="dmu-04__sr" type="checkbox" id="dmu-04-toggle">
        <label class="dmu-04__switch" for="dmu-04-toggle">
          <svg class="dmu-04__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.6v2.2M12 19.2v2.2M2.6 12h2.2M19.2 12h2.2M5.4 5.4 7 7M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6"/></svg>
          <svg class="dmu-04__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
          <span>Invert scheme</span>
        </label>
      </header>

      <div class="dmu-04__grid">
        <section class="dmu-04__pane">
          <h1 class="dmu-04__h1">Zero media queries</h1>
          <p class="dmu-04__lede">Each token declares its light and dark value on one line. The switch changes a single property &mdash; <code>color-scheme</code> &mdash; and every token below re-resolves.</p>
          <dl class="dmu-04__tokens">
            <div><dt>--bg</dt><dd>light-dark(#f6f7f9, #0a0b0d)</dd></div>
            <div><dt>--surface</dt><dd>light-dark(#ffffff, #13151a)</dd></div>
            <div><dt>--ink</dt><dd>light-dark(#0a0b0d, #f2f4f7)</dd></div>
            <div><dt>--accent</dt><dd>light-dark(#0f766e, #5eead4)</dd></div>
          </dl>
        </section>

        <section class="dmu-04__pane dmu-04__pane--demo">
          <article class="dmu-04__card">
            <p class="dmu-04__cardTag">Inherits page scheme</p>
            <h2 class="dmu-04__cardTitle">Priya Sharma</h2>
            <p class="dmu-04__cardBody">Requested review on <code>theme.css</code> &mdash; 3 files changed.</p>
            <div class="dmu-04__actions">
              <button class="dmu-04__btn dmu-04__btn--primary" type="button">Approve</button>
              <button class="dmu-04__btn" type="button">Comment</button>
            </div>
          </article>
          <article class="dmu-04__card dmu-04__card--forceLight">
            <p class="dmu-04__cardTag">color-scheme: light</p>
            <h2 class="dmu-04__cardTitle">Locked panel</h2>
            <p class="dmu-04__cardBody">This subtree pins its own scheme, so its tokens never invert.</p>
            <div class="dmu-04__actions">
              <button class="dmu-04__btn dmu-04__btn--primary" type="button">Approve</button>
              <button class="dmu-04__btn" type="button">Comment</button>
            </div>
          </article>
        </section>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-04 {
  --bg: #0a0b0d;
  --surface: #13151a;
  --elevated: #191c22;
  --ink: #f2f4f7;
  --muted: #98a0ae;
  --line: #262a32;
  --accent: #5eead4;
  --accent-ink: #04211c;
  --wash: rgba(94,234,212,.12);
  --focus: #99f6e4;
  --shadow: rgba(0,0,0,.55);
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

@media (prefers-color-scheme: light) {
  .dmu-04:not([data-theme="dark"]):not(:has(#dmu-04-toggle:checked)) {
    --bg: #f6f7f9;
    --surface: #ffffff;
    --elevated: #ffffff;
    --ink: #0a0b0d;
    --muted: #5a616e;
    --line: #e4e7ec;
    --accent: #0f766e;
    --accent-ink: #ffffff;
    --wash: rgba(15,118,110,.10);
    --focus: #0f766e;
    --shadow: rgba(10,11,13,.14);
    color-scheme: light;
  }

  .dmu-04:has(#dmu-04-toggle:checked) {
    --bg: #0a0b0d;
    --surface: #13151a;
    --elevated: #191c22;
    --ink: #f2f4f7;
    --muted: #98a0ae;
    --line: #262a32;
    --accent: #5eead4;
    --accent-ink: #04211c;
    --wash: rgba(94,234,212,.12);
    --focus: #99f6e4;
    --shadow: rgba(0,0,0,.55);
    color-scheme: dark;
  }
}

@supports (background: light-dark(white, black)) {
  .dmu-04 {
    color-scheme: light dark;
    --bg: light-dark(#f6f7f9,#0a0b0d);
    --surface: light-dark(#ffffff,#13151a);
    --elevated: light-dark(#ffffff,#191c22);
    --ink: light-dark(#0a0b0d,#f2f4f7);
    --muted: light-dark(#5a616e,#98a0ae);
    --line: light-dark(#e4e7ec,#262a32);
    --accent: light-dark(#0f766e,#5eead4);
    --accent-ink: light-dark(#ffffff,#04211c);
    --wash: light-dark(rgba(15,118,110,.10),rgba(94,234,212,.12));
    --focus: light-dark(#0f766e,#99f6e4);
    --shadow: light-dark(rgba(10,11,13,.14),rgba(0,0,0,.55));
  }

  .dmu-04[data-theme="light"] {
    color-scheme: light;
  }

  .dmu-04[data-theme="dark"] {
    color-scheme: dark;
  }

  .dmu-04:has(#dmu-04-toggle:checked) {
    color-scheme: dark;
  }

  @media (prefers-color-scheme: dark) {
    .dmu-04:has(#dmu-04-toggle:checked) {
      color-scheme: light;
    }
  }

  .dmu-04__card--forceLight {
    color-scheme: light;
  }
}

.dmu-04,
.dmu-04 *,
.dmu-04 *::before,
.dmu-04 *::after {
  box-sizing: border-box;
}

.dmu-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-04__shell {
  width: min(66rem,100%);
  border-radius: 1.25rem;
  overflow: hidden;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 34px 70px -46px var(--shadow);
}

.dmu-04__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding: .9rem 1.15rem;
  border-bottom: 1px solid var(--line);
  background: var(--surface);
}

.dmu-04__id {
  display: flex;
  align-items: center;
  gap: .65rem;
}

.dmu-04__mark {
  display: grid;
  place-items: center;
  width: 2.1rem;
  height: 2.1rem;
  border-radius: .65rem;
  background: var(--wash);
  color: var(--accent);
}

.dmu-04__mark svg {
  width: 1.15rem;
  height: 1.15rem;
}

.dmu-04__name {
  margin: 0;
  font-family: var(--mono);
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.dmu-04__sub {
  margin: .1rem 0 0;
  font-size: .74rem;
  color: var(--muted);
}

.dmu-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-04__switch {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  cursor: pointer;
  user-select: none;
  min-height: 2.6rem;
  padding: 0 .9rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--elevated);
  color: var(--ink);
  font-size: .82rem;
  font-weight: 550;
  transition: border-color .2s ease, background-color .2s ease;
}

.dmu-04__switch:hover {
  border-color: color-mix(in oklab,var(--accent) 50%,var(--line));
}

.dmu-04__switch svg {
  width: 1rem;
  height: 1rem;
  color: var(--accent);
}

.dmu-04__sun {
  display: none;
}

.dmu-04__moon {
  display: block;
}

.dmu-04:has(#dmu-04-toggle:checked) .dmu-04__sun {
  display: block;
}

.dmu-04:has(#dmu-04-toggle:checked) .dmu-04__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-04:not(:has(#dmu-04-toggle:checked)) .dmu-04__sun {
    display: block;
  }

  .dmu-04:not(:has(#dmu-04-toggle:checked)) .dmu-04__moon {
    display: none;
  }

  .dmu-04:has(#dmu-04-toggle:checked) .dmu-04__sun {
    display: none;
  }

  .dmu-04:has(#dmu-04-toggle:checked) .dmu-04__moon {
    display: block;
  }
}

.dmu-04:has(#dmu-04-toggle:focus-visible) .dmu-04__switch {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-04__grid {
  display: grid;
}

@media (min-width: 58rem) {
  .dmu-04__grid {
    grid-template-columns: 1fr 1fr;
  }
}

.dmu-04__pane {
  padding: clamp(1.25rem,3vw,2rem);
  display: grid;
  gap: .75rem;
  align-content: start;
}

.dmu-04__pane--demo {
  gap: .85rem;
  background: var(--bg);
  border-top: 1px solid var(--line);
}

@media (min-width: 58rem) {
  .dmu-04__pane--demo {
    border-top: 0;
    border-left: 1px solid var(--line);
  }
}

.dmu-04__h1 {
  margin: 0;
  font-size: clamp(1.45rem,3vw,2rem);
  font-weight: 650;
  letter-spacing: -.03em;
}

.dmu-04__lede {
  margin: 0;
  color: var(--muted);
  font-size: .93rem;
  line-height: 1.65;
  max-width: 44ch;
  text-wrap: pretty;
}

.dmu-04__lede code,
.dmu-04__cardBody code {
  font-family: var(--mono);
  font-size: .9em;
  color: var(--accent);
}

.dmu-04__tokens {
  margin: .35rem 0 0;
  display: grid;
  gap: .3rem;
}

.dmu-04__tokens div {
  display: grid;
  grid-template-columns: 6.5rem 1fr;
  gap: .6rem;
  align-items: center;
  padding: .5rem .6rem;
  border-radius: .55rem;
  background: var(--elevated);
  border: 1px solid var(--line);
}

.dmu-04__tokens dt {
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--accent);
}

.dmu-04__tokens dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.dmu-04__card {
  display: grid;
  gap: .5rem;
  padding: 1.15rem;
  border-radius: .95rem;
  background: var(--surface);
  color: var(--ink);
  border: 1px solid var(--line);
  box-shadow: 0 16px 34px -30px var(--shadow);
}

.dmu-04__card--forceLight {
  --surface: #ffffff;
  --elevated: #ffffff;
  --ink: #0a0b0d;
  --muted: #5a616e;
  --line: #e4e7ec;
  --accent: #0f766e;
  --accent-ink: #ffffff;
  --wash: rgba(15,118,110,.10);
}

.dmu-04__cardTag {
  margin: 0;
  width: max-content;
  padding: .22rem .5rem;
  border-radius: .35rem;
  background: var(--wash);
  color: var(--accent);
  font-family: var(--mono);
  font-size: .67rem;
  letter-spacing: .06em;
}

.dmu-04__cardTitle {
  margin: 0;
  font-size: 1.02rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.dmu-04__cardBody {
  margin: 0;
  font-size: .85rem;
  line-height: 1.55;
  color: var(--muted);
}

.dmu-04__actions {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
  margin-top: .2rem;
}

.dmu-04__btn {
  min-height: 2.5rem;
  padding: 0 .95rem;
  border-radius: .55rem;
  cursor: pointer;
  font: inherit;
  font-size: .83rem;
  font-weight: 550;
  background: var(--elevated);
  color: var(--ink);
  border: 1px solid var(--line);
  transition: translate .18s ease, border-color .18s ease;
}

.dmu-04__btn:hover {
  translate: 0 -1px;
  border-color: color-mix(in oklab,var(--accent) 45%,var(--line));
}

.dmu-04__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-04__btn--primary {
  background: var(--accent);
  color: var(--accent-ink);
  border-color: transparent;
}

@media (prefers-reduced-motion: reduce) {
  .dmu-04__btn,
    .dmu-04__switch {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-04__shell,
    .dmu-04__card,
    .dmu-04__switch,
    .dmu-04__tokens div {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-04__btn {
    background: ButtonFace;
    color: ButtonText;
    border-color: ButtonText;
  }
}
```
