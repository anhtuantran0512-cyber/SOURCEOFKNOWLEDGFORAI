---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/number-counter-animation/"
title: "Transitioning Custom Properties with at-property"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "An unregistered custom property is an unparsed string to the engine, so transition: --angle 400ms does exactly nothing — the most common \"why won't my CSS…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transitioning Custom Properties with at-property
Source: https://codefronts.com/motion/css-transition-designs/number-counter-animation/

An unregistered custom property is an unparsed string to the engine, so transition: --angle 400ms does exactly nothing — the most common "why won't my CSS variable animate" question there is. Registering it with @property and a typed syntax makes it interpolable. The silent no-op sits beside the working version, both driven from the same hover.
## HTML
```html
<section class="trn-15" aria-labelledby="trn-15-heading">
  <div class="trn-15__stage">
    <div class="trn-15__theme">
      <input class="trn-15__themecb" type="checkbox" id="trn-15-theme">
      <label class="trn-15__themebtn" for="trn-15-theme">
        <span class="trn-15__themeico" aria-hidden="true">
          <svg class="trn-15__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-15__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-15__head">
      <p class="trn-15__kicker">@property</p>
      <h2 class="trn-15__heading" id="trn-15-heading">Why your CSS variable refuses to animate</h2>
      <p class="trn-15__sub">Both dials are hovered the same way and share a duration. Only one of them has a type.</p>
    </header>

    <div class="trn-15__pair">
      <article class="trn-15__card trn-15__card--plain">
        <p class="trn-15__label trn-15__label--bad">Unregistered — the transition never starts</p>
        <div class="trn-15__dial trn-15__dial--plain" aria-hidden="true"><span class="trn-15__hub">24 &rarr; 78</span></div>
        <div class="trn-15__bar"><span class="trn-15__barfill trn-15__barfill--plain"></span></div>
        <code class="trn-15__code">--trn-15-plain: 24%;
transition: --trn-15-plain 700ms ease;</code>
        <p class="trn-15__note">The engine holds this value as an untyped token sequence. There is no midpoint between two strings, so it snaps.</p>
      </article>

      <article class="trn-15__card trn-15__card--typed">
        <p class="trn-15__label trn-15__label--good">Registered &lt;percentage&gt; — interpolates</p>
        <div class="trn-15__dial trn-15__dial--typed" aria-hidden="true"><span class="trn-15__hub">24 &rarr; 78</span></div>
        <div class="trn-15__bar"><span class="trn-15__barfill trn-15__barfill--typed"></span></div>
        <code class="trn-15__code">@property --trn-15-sweep {
  syntax: '&lt;percentage&gt;';
  inherits: false;
  initial-value: 24%;
}</code>
        <p class="trn-15__note">One typed value drives the dial sweep, the bar width and the hub opacity — three outputs that cannot drift apart.</p>
      </article>
    </div>

    <p class="trn-15__foot">Register the name you own. Custom property registration is document-wide, so <code>--sweep</code> from two components is one type — prefix it.</p>
  </div>
</section>
```
## CSS
```css
@property --trn-15-sweep {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 24%;
}

.trn-15 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #120a20;
  --page: oklch(0.19 0.06 300);
  --card: #1b1030;
  --card: oklch(0.24 0.07 300);
  --ink: #f4eeff;
  --ink: oklch(0.96 0.02 300);
  --muted: #a495c4;
  --muted: oklch(0.73 0.05 300);
  --rule: #2d1f4d;
  --rule: oklch(0.31 0.075 300);
  --violet: #a35cff;
  --violet: oklch(0.66 0.23 300);
  --magenta: #ff4fbf;
  --magenta: oklch(0.7 0.24 340);
  --bad: #ff7a7a;
  --bad: oklch(0.74 0.16 20);
  --trn-15-plain: 24%;
  --font-display: "Neue Haas Grotesk", "Helvetica Neue", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-15 *,
.trn-15 *::before,
.trn-15 *::after {
  box-sizing: border-box;
}

.trn-15__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(26px, 5vw, 60px) 16px;
}

.trn-15__head {
  inline-size: 100%;
  max-inline-size: 56rem;
  min-inline-size: 0;
  margin: 0 0 26px;
}

.trn-15__kicker {
  margin: 0 0 12px;
  font: 500 11.5px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  color: var(--magenta);
}

.trn-15__heading {
  margin: 0 0 10px;
  font: 600 clamp(25px, 4.8vw, 38px)/1.1 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.trn-15__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-15__pair {
  inline-size: 100%;
  max-inline-size: 56rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 18px;
}

.trn-15__card {
  min-inline-size: 0;
  padding: 20px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 14px;
  transition: box-shadow 500ms ease;
}

.trn-15__card--typed:hover {
  box-shadow: 0 0 0 1px var(--violet), 0 24px 60px -30px var(--violet);
}

.trn-15__card--plain:hover {
  box-shadow: 0 0 0 1px var(--bad);
}

.trn-15__label {
  margin: 0 0 16px;
  font: 600 12px/1.4 ui-monospace, Menlo, monospace;
}

.trn-15__label--bad {
  color: var(--bad);
}

.trn-15__label--good {
  color: var(--violet);
}

.trn-15__dial {
  position: relative;
  inline-size: 148px;
  max-inline-size: 100%;
  aspect-ratio: 1;
  margin-inline: auto;
  border-radius: 50%;
  display: grid;
  place-items: center;
}

.trn-15__dial--plain {
  background: conic-gradient(var(--bad) 0 var(--trn-15-plain), rgba(255, 255, 255, 0.06) var(--trn-15-plain) 100%);
  transition: --trn-15-plain 700ms ease;
}

.trn-15__card--plain:hover .trn-15__dial--plain {
  --trn-15-plain: 78%;
}

.trn-15__dial--typed {
  background: conic-gradient(var(--violet) 0 var(--trn-15-sweep), var(--magenta) var(--trn-15-sweep) calc(var(--trn-15-sweep) + 6%), rgba(255, 255, 255, 0.06) calc(var(--trn-15-sweep) + 6%) 100%);
  transition: --trn-15-sweep 700ms cubic-bezier(.3, .8, .3, 1);
}

.trn-15__card--typed:hover .trn-15__dial--typed {
  --trn-15-sweep: 78%;
}

.trn-15__dial::after {
  content: "";
  position: absolute;
  inset: 18px;
  border-radius: 50%;
  background: var(--card);
}

.trn-15__hub {
  position: relative;
  z-index: 1;
  font: 600 15px/1 ui-monospace, Menlo, monospace;
  color: var(--ink);
}

.trn-15__bar {
  margin-block-start: 18px;
  block-size: 6px;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.07);
  overflow: hidden;
}

.trn-15__barfill {
  display: block;
  block-size: 100%;
  border-radius: 3px;
}

.trn-15__barfill--plain {
  inline-size: var(--trn-15-plain);
  background: var(--bad);
}

.trn-15__barfill--typed {
  inline-size: var(--trn-15-sweep);
  background: linear-gradient(90deg, var(--violet), var(--magenta));
}

.trn-15__code {
  display: block;
  margin-block-start: 16px;
  padding: 11px 12px;
  background: rgba(255, 255, 255, 0.04);
  border-radius: 8px;
  font: 400 11px/1.6 ui-monospace, Menlo, monospace;
  color: var(--ink);
  white-space: pre-wrap;
  overflow-wrap: anywhere;
}

.trn-15__note {
  margin: 12px 0 0;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-15__foot {
  inline-size: 100%;
  max-inline-size: 56rem;
  margin: 22px 0 0;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

.trn-15__foot code {
  font: 400 11.5px/1 ui-monospace, Menlo, monospace;
  color: var(--magenta);
}

@media (prefers-reduced-motion: reduce) {
  .trn-15__dial--typed {
    transition-duration: 200ms;
  }

  .trn-15__card {
    transition: none;
  }

  .trn-15__card--typed:hover,
    .trn-15__card--plain:hover {
    box-shadow: 0 0 0 1px var(--violet);
  }
}

@media (prefers-color-scheme: light) {
  .trn-15 {
    --page: #f9f5ff;
    --card: #ffffff;
    --ink: #180d2b;
    --muted: #5d4d7d;
    --rule: #e4daf6;
    --violet: #7328e0;
    --magenta: #cc1f92;
    --bad: #c22e2e;
  }

  .trn-15__dial--plain {
    background: conic-gradient(var(--bad) 0 var(--trn-15-plain), rgba(24, 13, 43, 0.08) var(--trn-15-plain) 100%);
  }

  .trn-15__dial--typed {
    background: conic-gradient(var(--violet) 0 var(--trn-15-sweep), var(--magenta) var(--trn-15-sweep) calc(var(--trn-15-sweep) + 6%), rgba(24, 13, 43, 0.08) calc(var(--trn-15-sweep) + 6%) 100%);
  }

  .trn-15__bar {
    background: rgba(24, 13, 43, 0.08);
  }

  .trn-15__code {
    background: rgba(24, 13, 43, 0.05);
  }
}

[data-theme="dark"] .trn-15 {
  --page: #120a20;
  --card: #1b1030;
  --ink: #f4eeff;
  --muted: #a495c4;
  --rule: #2d1f4d;
  --violet: #a35cff;
  --magenta: #ff4fbf;
  --bad: #ff7a7a;
}

[data-theme="dark"] .trn-15__bar {
  background: rgba(255, 255, 255, 0.07);
}

[data-theme="dark"] .trn-15__code {
  background: rgba(255, 255, 255, 0.04);
}

.trn-15__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-15__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-15__themebtn {
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

.trn-15__themebtn:hover {
  color: var(--ink);
}

.trn-15__themecb:focus-visible + .trn-15__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-15__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-15__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-15__sun {
  opacity: 0.34;
}

.trn-15__moon {
  opacity: 1;
}

.trn-15:has(#trn-15-theme:checked) .trn-15__sun {
  opacity: 1;
}

.trn-15:has(#trn-15-theme:checked) .trn-15__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-15:has(#trn-15-theme:checked) {
    --page: #f9f5ff;
    --card: #ffffff;
    --ink: #180d2b;
    --muted: #5d4d7d;
    --rule: #e4daf6;
    --violet: #7328e0;
    --magenta: #cc1f92;
    --bad: #c22e2e;
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__dial--plain {
    background: conic-gradient(var(--bad) 0 var(--trn-15-plain), rgba(24, 13, 43, 0.08) var(--trn-15-plain) 100%);
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__dial--typed {
    background: conic-gradient(var(--violet) 0 var(--trn-15-sweep), var(--magenta) var(--trn-15-sweep) calc(var(--trn-15-sweep) + 6%), rgba(24, 13, 43, 0.08) calc(var(--trn-15-sweep) + 6%) 100%);
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__bar {
    background: rgba(24, 13, 43, 0.08);
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__code {
    background: rgba(24, 13, 43, 0.05);
  }
}

@media (prefers-color-scheme: light) {
  .trn-15:has(#trn-15-theme:checked) {
    --page: #120a20;
    --page: oklch(0.19 0.06 300);
    --card: #1b1030;
    --card: oklch(0.24 0.07 300);
    --ink: #f4eeff;
    --ink: oklch(0.96 0.02 300);
    --muted: #a495c4;
    --muted: oklch(0.73 0.05 300);
    --rule: #2d1f4d;
    --rule: oklch(0.31 0.075 300);
    --violet: #a35cff;
    --violet: oklch(0.66 0.23 300);
    --magenta: #ff4fbf;
    --magenta: oklch(0.7 0.24 340);
    --bad: #ff7a7a;
    --bad: oklch(0.74 0.16 20);
    --trn-15-plain: 24%;
    --font-display: "Neue Haas Grotesk", "Helvetica Neue", system-ui, sans-serif;
    background: var(--page);
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__dial--plain {
    background: conic-gradient(var(--bad) 0 var(--trn-15-plain), rgba(255, 255, 255, 0.06) var(--trn-15-plain) 100%);
    transition: --trn-15-plain 700ms ease;
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__dial--typed {
    background: conic-gradient(var(--violet) 0 var(--trn-15-sweep), var(--magenta) var(--trn-15-sweep) calc(var(--trn-15-sweep) + 6%), rgba(255, 255, 255, 0.06) calc(var(--trn-15-sweep) + 6%) 100%);
    transition: --trn-15-sweep 700ms cubic-bezier(.3, .8, .3, 1);
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__bar {
    margin-block-start: 18px;
    block-size: 6px;
    border-radius: 3px;
    background: rgba(255, 255, 255, 0.07);
    overflow: hidden;
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__code {
    display: block;
    margin-block-start: 16px;
    padding: 11px 12px;
    background: rgba(255, 255, 255, 0.04);
    border-radius: 8px;
    font: 400 11px/1.6 ui-monospace, Menlo, monospace;
    color: var(--ink);
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__sun {
    opacity: 0.34;
  }

  .trn-15:has(#trn-15-theme:checked) .trn-15__moon {
    opacity: 1;
  }
}
```
