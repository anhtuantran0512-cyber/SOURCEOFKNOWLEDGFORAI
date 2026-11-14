---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-ui-with-data-theme-attribute-override/"
title: "Dark Mode UI with data-theme Attribute Override"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "The layer you add when a visitor needs to disagree with their operating system."
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode UI with data-theme Attribute Override
Source: https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-ui-with-data-theme-attribute-override/

The layer you add when a visitor needs to disagree with their operating system. A [data-theme] attribute wins over the media query, and a pure-CSS toggle — a visually hidden <input type="checkbox"> read by :has(:checked) — wins over both. Includes the nested-media flip-back rule, the one line that stops the toggle from silently doing nothing for visitors whose OS already matches your default.
## HTML
```html
<div class="dmu-02">
  <div class="dmu-02__stage">
    <div class="dmu-02__shell">
      <header class="dmu-02__bar">
        <div class="dmu-02__brand">
          <span class="dmu-02__logo" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 17 9 7l5 10"/><path d="M15 12h5"/></svg>
          </span>
          <span class="dmu-02__brandName">Atlas</span>
          <span class="dmu-02__scope">data-theme</span>
        </div>

        <input class="dmu-02__sr" type="checkbox" id="dmu-02-toggle">
        <label class="dmu-02__toggle" for="dmu-02-toggle">
          <span class="dmu-02__track" aria-hidden="true">
            <span class="dmu-02__knob">
              <svg class="dmu-02__sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.6v2.2M12 19.2v2.2M2.6 12h2.2M19.2 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6"/></svg>
              <svg class="dmu-02__moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
            </span>
          </span>
          <span class="dmu-02__toggleText">Theme</span>
        </label>
      </header>

      <div class="dmu-02__body">
        <section class="dmu-02__main">
          <p class="dmu-02__kicker">Project settings</p>
          <h1 class="dmu-02__title">Appearance</h1>
          <p class="dmu-02__lede">The attribute override beats the media query. The checkbox beats the attribute. Every visitor gets a switch that flips in both directions.</p>

          <div class="dmu-02__rows">
            <div class="dmu-02__row">
              <div>
                <p class="dmu-02__rowTitle">Match system preference</p>
                <p class="dmu-02__rowHint">Falls back to <code>prefers-color-scheme</code></p>
              </div>
              <span class="dmu-02__pill dmu-02__pill--on">Layer 1</span>
            </div>
            <div class="dmu-02__row">
              <div>
                <p class="dmu-02__rowTitle">Workspace override</p>
                <p class="dmu-02__rowHint">Set <code>data-theme</code> on the root element</p>
              </div>
              <span class="dmu-02__pill">Layer 2</span>
            </div>
            <div class="dmu-02__row">
              <div>
                <p class="dmu-02__rowTitle">In-page switch</p>
                <p class="dmu-02__rowHint">Read by <code>:has(:checked)</code>, zero script</p>
              </div>
              <span class="dmu-02__pill dmu-02__pill--accent">Layer 3</span>
            </div>
          </div>
        </section>

        <aside class="dmu-02__notes">
          <h2 class="dmu-02__notesTitle">Cascade order</h2>
          <ol class="dmu-02__steps">
            <li><span>1</span><code>@media (prefers-color-scheme)</code> &mdash; the default</li>
            <li><span>2</span><code>[data-theme="dark"|"light"]</code> &mdash; host override</li>
            <li><span>3</span><code>:has(:checked)</code> &mdash; the visitor wins</li>
          </ol>
          <p class="dmu-02__flip"><strong>Flip-back rule.</strong> Inside <code>@media (prefers-color-scheme: light)</code>, a <code>:has(:checked)</code> rule restores every dark token &mdash; otherwise the switch has nowhere to travel on a light-OS machine.</p>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-02 {
  --bg: #0a0a0c;
  --surface: #121218;
  --elevated: #17171f;
  --ink: #f4f4f5;
  --muted: #9d9daa;
  --line: #26262f;
  --accent: #a78bfa;
  --accent-soft: rgba(167,139,250,.14);
  --accent-ink: #120c22;
  --focus: #c4b5fd;
  --knob-bg: #1f1f29;
  --knob-ink: #e9d5ff;
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

.dmu-02[data-theme="light"],
.dmu-02:has(#dmu-02-toggle:checked) {
  --bg: #f7f7f9;
  --surface: #ffffff;
  --elevated: #ffffff;
  --ink: #0b0b0f;
  --muted: #5d6068;
  --line: #e4e4ea;
  --accent: #6d28d9;
  --accent-soft: rgba(109,40,217,.10);
  --accent-ink: #ffffff;
  --focus: #6d28d9;
  --knob-bg: #ffffff;
  --knob-ink: #6d28d9;
  --shadow: rgba(15,15,25,.12);
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-02:not([data-theme="dark"]):not(:has(#dmu-02-toggle:checked)) {
    --bg: #f7f7f9;
    --surface: #ffffff;
    --elevated: #ffffff;
    --ink: #0b0b0f;
    --muted: #5d6068;
    --line: #e4e4ea;
    --accent: #6d28d9;
    --accent-soft: rgba(109,40,217,.10);
    --accent-ink: #ffffff;
    --focus: #6d28d9;
    --knob-bg: #ffffff;
    --knob-ink: #6d28d9;
    --shadow: rgba(15,15,25,.12);
    color-scheme: light;
  }
  /* flip-back: light OS + checked restores the dark base in full */

  .dmu-02:has(#dmu-02-toggle:checked) {
    --bg: #0a0a0c;
    --surface: #121218;
    --elevated: #17171f;
    --ink: #f4f4f5;
    --muted: #9d9daa;
    --line: #26262f;
    --accent: #a78bfa;
    --accent-soft: rgba(167,139,250,.14);
    --accent-ink: #120c22;
    --focus: #c4b5fd;
    --knob-bg: #1f1f29;
    --knob-ink: #e9d5ff;
    --shadow: rgba(0,0,0,.55);
    color-scheme: dark;
  }
}

.dmu-02,
.dmu-02 *,
.dmu-02 *::before,
.dmu-02 *::after {
  box-sizing: border-box;
}

.dmu-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-02__shell {
  width: min(64rem,100%);
  border-radius: 1.25rem;
  overflow: hidden;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 color-mix(in oklab,var(--ink) 6%,transparent) inset, 0 30px 60px -40px var(--shadow);
}

.dmu-02__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding: .85rem 1.1rem;
  border-bottom: 1px solid var(--line);
  background: color-mix(in oklab,var(--surface) 88%,var(--ink) 3%);
}

.dmu-02__brand {
  display: flex;
  align-items: center;
  gap: .55rem;
}

.dmu-02__logo {
  display: grid;
  place-items: center;
  width: 1.9rem;
  height: 1.9rem;
  border-radius: .6rem;
  background: var(--accent-soft);
  color: var(--accent);
}

.dmu-02__logo svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-02__brandName {
  font-weight: 600;
  letter-spacing: -.02em;
}

.dmu-02__scope {
  font-family: var(--mono);
  font-size: .68rem;
  padding: .2rem .45rem;
  border-radius: .35rem;
  color: var(--muted);
  border: 1px solid var(--line);
}

.dmu-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-02__toggle {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  cursor: pointer;
  user-select: none;
  padding: .3rem;
  border-radius: .7rem;
}

.dmu-02__toggleText {
  font-size: .82rem;
  font-weight: 550;
  color: var(--muted);
}

.dmu-02__track {
  --knob: 1.45rem;
  position: relative;
  display: block;
  width: 3.3rem;
  height: 1.95rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
  border: 1px solid var(--line);
}

.dmu-02__knob {
  position: absolute;
  top: .2rem;
  left: .22rem;
  display: grid;
  place-items: center;
  width: var(--knob);
  height: var(--knob);
  border-radius: 50%;
  background: var(--knob-bg);
  color: var(--knob-ink);
  box-shadow: 0 2px 6px var(--shadow);
  transition: translate .28s cubic-bezier(.16,1,.3,1);
}

.dmu-02__knob svg {
  width: .85rem;
  height: .85rem;
}

.dmu-02__sun {
  display: none;
}

.dmu-02__moon {
  display: block;
}

.dmu-02:has(#dmu-02-toggle:checked) .dmu-02__knob {
  translate: 1.32rem 0;
}

.dmu-02:has(#dmu-02-toggle:checked) .dmu-02__sun {
  display: block;
}

.dmu-02:has(#dmu-02-toggle:checked) .dmu-02__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-02:not(:has(#dmu-02-toggle:checked)) .dmu-02__knob {
    translate: 1.32rem 0;
  }

  .dmu-02:not(:has(#dmu-02-toggle:checked)) .dmu-02__sun {
    display: block;
  }

  .dmu-02:not(:has(#dmu-02-toggle:checked)) .dmu-02__moon {
    display: none;
  }

  .dmu-02:has(#dmu-02-toggle:checked) .dmu-02__knob {
    translate: 0 0;
  }

  .dmu-02:has(#dmu-02-toggle:checked) .dmu-02__sun {
    display: none;
  }

  .dmu-02:has(#dmu-02-toggle:checked) .dmu-02__moon {
    display: block;
  }
}

.dmu-02__toggle:has(#dmu-02-toggle:focus-visible),
.dmu-02:has(#dmu-02-toggle:focus-visible) .dmu-02__toggle {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-02__body {
  display: grid;
  gap: 0;
  grid-template-columns: 1fr;
}

@media (min-width: 56rem) {
  .dmu-02__body {
    grid-template-columns: 1.55fr 1fr;
  }
}

.dmu-02__main {
  padding: clamp(1.25rem,3vw,2.1rem);
  display: grid;
  gap: .55rem;
  align-content: start;
}

.dmu-02__kicker {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
}

.dmu-02__title {
  margin: 0;
  font-size: clamp(1.5rem,3.4vw,2.15rem);
  font-weight: 650;
  letter-spacing: -.03em;
}

.dmu-02__lede {
  margin: 0 0 .6rem;
  color: var(--muted);
  font-size: .95rem;
  line-height: 1.6;
  max-width: 46ch;
  text-wrap: pretty;
}

.dmu-02__rows {
  display: grid;
  gap: .5rem;
}

.dmu-02__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .85rem .95rem;
  border-radius: .8rem;
  background: var(--elevated);
  border: 1px solid var(--line);
  transition: border-color .2s ease, translate .2s ease;
}

.dmu-02__row:hover {
  border-color: color-mix(in oklab,var(--accent) 45%,var(--line));
  translate: 0 -1px;
}

.dmu-02__rowTitle {
  margin: 0 0 .18rem;
  font-size: .9rem;
  font-weight: 550;
}

.dmu-02__rowHint {
  margin: 0;
  font-size: .78rem;
  color: var(--muted);
}

.dmu-02__rowHint code,
.dmu-02__steps code,
.dmu-02__flip code {
  font-family: var(--mono);
  font-size: .92em;
  color: var(--accent);
}

.dmu-02__pill {
  font-family: var(--mono);
  font-size: .68rem;
  padding: .28rem .5rem;
  border-radius: .4rem;
  color: var(--muted);
  border: 1px solid var(--line);
  white-space: nowrap;
}

.dmu-02__pill--on {
  color: var(--ink);
}

.dmu-02__pill--accent {
  color: var(--accent);
  border-color: color-mix(in oklab,var(--accent) 40%,transparent);
  background: var(--accent-soft);
}

.dmu-02__notes {
  padding: clamp(1.25rem,3vw,2.1rem);
  display: grid;
  gap: .85rem;
  align-content: start;
  background: color-mix(in oklab,var(--surface) 82%,var(--ink) 5%);
  border-top: 1px solid var(--line);
}

@media (min-width: 56rem) {
  .dmu-02__notes {
    border-top: 0;
    border-left: 1px solid var(--line);
  }
}

.dmu-02__notesTitle {
  margin: 0;
  font-size: .9rem;
  font-weight: 600;
}

.dmu-02__steps {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .5rem;
  counter-reset: none;
}

.dmu-02__steps li {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .82rem;
  color: var(--muted);
}

.dmu-02__steps li span {
  display: grid;
  place-items: center;
  width: 1.35rem;
  height: 1.35rem;
  flex: none;
  border-radius: .4rem;
  background: var(--accent-soft);
  color: var(--accent);
  font-family: var(--mono);
  font-size: .72rem;
}

.dmu-02__flip {
  margin: 0;
  font-size: .8rem;
  line-height: 1.65;
  color: var(--muted);
  padding: .8rem .9rem;
  border-radius: .7rem;
  background: var(--elevated);
  border: 1px dashed color-mix(in oklab,var(--accent) 45%,var(--line));
  text-wrap: pretty;
}

.dmu-02__flip strong {
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-02__knob,
    .dmu-02__row {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-02__shell,
    .dmu-02__row,
    .dmu-02__flip,
    .dmu-02__track {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-02__knob {
    background: ButtonText;
  }
}
```
