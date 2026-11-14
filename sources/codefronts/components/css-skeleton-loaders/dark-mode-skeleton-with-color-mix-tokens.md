---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/dark-mode-skeleton-with-color-mix-tokens/"
title: "Dark Mode Skeleton with color-mix Tokens"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "Stop shipping two skeleton palettes."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Skeleton with color-mix Tokens
Source: https://codefronts.com/components/css-skeleton-loaders/dark-mode-skeleton-with-color-mix-tokens/

Stop shipping two skeleton palettes. color-mix(in oklab, currentColor 8%, transparent) derives the fill from whatever text colour the surface already inherits, so one class renders correctly on a near-black product surface and on white — no [data-theme] overrides for the bars themselves. Flip the toggle and watch identical markup re-tune itself.
## HTML
```html
<div class="sk-04">
  <input class="sk-04__sr" type="checkbox" id="sk-04-theme">
  <div class="sk-04__stage">
    <section class="sk-04__wrap" aria-labelledby="sk-04-h">
      <header class="sk-04__head">
        <p class="sk-04__eyebrow">color-mix() · oklab</p>
        <h2 class="sk-04__h" id="sk-04-h">One token. Both themes. No override rule.</h2>
        <p class="sk-04__sub">The bars never name a colour — they mix 8% of the inherited <code>currentColor</code> into transparency, so the fill follows the surface it lands on.</p>
        <label class="sk-04__switch" for="sk-04-theme">
          <span class="sk-04__knob" aria-hidden="true">
            <svg class="sk-04__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.2M12 19v2.2M2.8 12H5M19 12h2.2M5.4 5.4 7 7M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="sk-04__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.4 14.3A8.3 8.3 0 0 1 9.7 3.6 8.5 8.5 0 1 0 20.4 14.3Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
          </span>
          <span class="sk-04__switchtext">Flip theme</span>
        </label>
      </header>

      <div class="sk-04__cols">
        <article class="sk-04__surface sk-04__surface--dark" role="status" aria-live="polite">
          <span class="sk-04__vh">Loading team activity on dark surface…</span>
          <p class="sk-04__label">surface · oklch(0.18 0.01 275)</p>
          <div class="sk-04__group" aria-hidden="true">
            <div class="sk-04__row"><span class="sk-04__bar sk-04__avatar"></span><div class="sk-04__ident"><span class="sk-04__bar" style="inline-size:7.5rem"></span><span class="sk-04__bar sk-04__bar--sm" style="inline-size:4.5rem"></span></div></div>
            <span class="sk-04__bar sk-04__bar--sm"></span>
            <span class="sk-04__bar sk-04__bar--sm" style="inline-size:72%"></span>
            <div class="sk-04__chips"><span class="sk-04__bar sk-04__chip" style="inline-size:4.5rem"></span><span class="sk-04__bar sk-04__chip" style="inline-size:3.2rem"></span><span class="sk-04__bar sk-04__chip" style="inline-size:5.4rem"></span></div>
          </div>
          <p class="sk-04__derived">currentColor ≈ <span>#f5f6fa</span> → fill lifts <em>above</em> the surface</p>
        </article>

        <article class="sk-04__surface sk-04__surface--light" role="status" aria-live="polite">
          <span class="sk-04__vh">Loading team activity on light surface…</span>
          <p class="sk-04__label">surface · oklch(0.99 0.002 275)</p>
          <div class="sk-04__group" aria-hidden="true">
            <div class="sk-04__row"><span class="sk-04__bar sk-04__avatar"></span><div class="sk-04__ident"><span class="sk-04__bar" style="inline-size:7.5rem"></span><span class="sk-04__bar sk-04__bar--sm" style="inline-size:4.5rem"></span></div></div>
            <span class="sk-04__bar sk-04__bar--sm"></span>
            <span class="sk-04__bar sk-04__bar--sm" style="inline-size:72%"></span>
            <div class="sk-04__chips"><span class="sk-04__bar sk-04__chip" style="inline-size:4.5rem"></span><span class="sk-04__bar sk-04__chip" style="inline-size:3.2rem"></span><span class="sk-04__bar sk-04__chip" style="inline-size:5.4rem"></span></div>
          </div>
          <p class="sk-04__derived">currentColor ≈ <span>#0b0d14</span> → fill sinks <em>below</em> the surface</p>
        </article>
      </div>

      <aside class="sk-04__spec" aria-label="Token values">
        <p class="sk-04__srow"><span class="sk-04__skey">--sk</span><span class="sk-04__sval">color-mix(in oklab, currentColor 8%, transparent)</span></p>
        <p class="sk-04__srow"><span class="sk-04__skey">--sheen</span><span class="sk-04__sval">color-mix(in oklab, currentColor 15%, transparent)</span></p>
        <p class="sk-04__srow"><span class="sk-04__skey">--line</span><span class="sk-04__sval">color-mix(in oklab, currentColor 12%, transparent)</span></p>
        <p class="sk-04__srow"><span class="sk-04__skey">theme</span><span class="sk-04__sval">:has(:checked) override + prefers-color-scheme default</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-04 {
  --bg: #0b0a12;
  --bg2: #141326;
  --panel: rgba(255,255,255,.03);
  --line: rgba(255,255,255,.11);
  --ink: #f5f6fa;
  --muted: rgba(245,246,250,.62);
  --faint: rgba(245,246,250,.42);
  --accent: #a78bfa;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(70% 48% at 82% -8%, rgba(167,139,250,.16) 0%, transparent 62%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 60%);
}

.sk-04 *,
.sk-04 *::before,
.sk-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .sk-04 {
    --bg: oklch(0.14 0.02 295);
    --bg2: oklch(0.21 0.05 292);
    --ink: oklch(0.97 0.005 292);
    --muted: oklch(0.97 0.005 292 / .62);
    --faint: oklch(0.97 0.005 292 / .42);
    --accent: oklch(0.78 0.14 300);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-04 {
    --line: color-mix(in oklab, currentColor 12%, transparent);
  }
}

.sk-04__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-04__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.sk-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-04__wrap {
  inline-size: min(74rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-04__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
  justify-items: start;
}

.sk-04__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-04__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-04__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-04__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-04__switch {
  margin-block-start: .35rem;
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  padding: .45rem .95rem .45rem .5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--panel);
  cursor: pointer;
  font-size: .88rem;
  font-weight: 500;
  color: var(--ink);
  transition: background .18s ease;
}

.sk-04__switch:hover {
  background: rgba(255,255,255,.07);
}

.sk-04__knob {
  inline-size: 1.85rem;
  block-size: 1.85rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: var(--accent);
  color: #17102b;
  flex: none;
}

.sk-04__knob svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sk-04__moon {
  display: none;
}

.sk-04__sr:focus-visible + .sk-04__stage .sk-04__switch {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.sk-04__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.sk-04__surface {
  display: grid;
  gap: 1rem;
  align-content: start;
  padding: clamp(1.05rem,2vw,1.5rem);
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  min-block-size: 19rem;
}

.sk-04__surface--dark {
  background: #161726;
  color: #f5f6fa;
  border-color: rgba(255,255,255,.12);
}

.sk-04__surface--light {
  background: #fdfdff;
  color: #0b0d14;
  border-color: rgba(11,13,20,.12);
}

@supports (color: oklch(0.7 0.1 300)) {
  .sk-04__surface--dark {
    background: oklch(0.18 0.022 285);
  }

  .sk-04__surface--light {
    background: oklch(0.99 0.002 285);
  }
}

.sk-04__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .67rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  opacity: .55;
}

.sk-04__group {
  display: grid;
  gap: .7rem;
}

.sk-04__row {
  display: flex;
  align-items: center;
  gap: .85rem;
  margin-block-end: .15rem;
}

.sk-04__ident {
  display: grid;
  gap: .45rem;
  min-inline-size: 0;
}

.sk-04__chips {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
  margin-block-start: .2rem;
}

.sk-04__derived {
  margin: auto 0 0;
  padding-block-start: .9rem;
  border-block-start: 1px solid;
  border-color: color-mix(in oklab, currentColor 12%, transparent);
  font-family: var(--mono);
  font-size: .7rem;
  line-height: 1.6;
  opacity: .7;
}

.sk-04__derived span {
  font-weight: 500;
  opacity: 1;
}

.sk-04__derived em {
  font-style: normal;
  text-decoration: underline;
  text-underline-offset: .2em;
}

.sk-04__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .85rem;
  inline-size: 100%;
  border-radius: 6px;
  background: rgba(128,128,128,.16);
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-04__bar {
    background: color-mix(in oklab, currentColor 8%, transparent);
  }
}

.sk-04__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, rgba(128,128,128,.22) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-04-sheen 1.4s linear infinite;
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-04__bar::after {
    background: linear-gradient(100deg, transparent 18%, color-mix(in oklab, currentColor 15%, transparent) 50%, transparent 82%);
  }
}

@keyframes sk-04-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-04__bar--sm {
  block-size: .7rem;
}

.sk-04__avatar {
  inline-size: 2.6rem;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}

.sk-04__chip {
  block-size: 1.6rem;
  border-radius: 999px;
}

.sk-04__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--panel);
  display: grid;
  gap: .45rem;
}

.sk-04__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-04__skey {
  min-inline-size: 4.5rem;
  color: var(--accent);
  font-size: .7rem;
}

.sk-04__sval {
  color: var(--muted);
  word-break: break-word;
}
/* pure-CSS theme flip */

.sk-04[data-theme="light"],
.sk-04:has(#sk-04-theme:checked) {
  --bg: #f6f5fb;
  --bg2: #fff;
  --panel: rgba(12,10,26,.028);
  --line: rgba(12,10,26,.11);
  --ink: #0c0a1a;
  --muted: rgba(12,10,26,.62);
  --faint: rgba(12,10,26,.44);
  --accent: #6d28d9;
  background: radial-gradient(70% 48% at 82% -8%, rgba(109,40,217,.1) 0%, transparent 62%), linear-gradient(178deg,#fff 0%,#eeecf8 100%);
}

.sk-04:has(#sk-04-theme:checked) .sk-04__sun {
  display: none;
}

.sk-04:has(#sk-04-theme:checked) .sk-04__moon {
  display: block;
}

.sk-04:has(#sk-04-theme:checked) .sk-04__knob {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .sk-04:not([data-theme="dark"]):not(:has(#sk-04-theme:checked)) {
    --bg: #f6f5fb;
    --bg2: #fff;
    --panel: rgba(12,10,26,.028);
    --line: rgba(12,10,26,.11);
    --ink: #0c0a1a;
    --muted: rgba(12,10,26,.62);
    --faint: rgba(12,10,26,.44);
    --accent: #6d28d9;
    background: radial-gradient(70% 48% at 82% -8%, rgba(109,40,217,.1) 0%, transparent 62%), linear-gradient(178deg,#fff 0%,#eeecf8 100%);
  }

  .sk-04:not([data-theme="dark"]):not(:has(#sk-04-theme:checked)) .sk-04__knob {
    color: #fff;
  }
  /* flip-back: on light OS + checked toggle, restore dark base so the switch has somewhere to go */

  .sk-04:has(#sk-04-theme:checked) {
    --bg: #0b0a12;
    --bg2: #141326;
    --panel: rgba(255,255,255,.03);
    --line: rgba(255,255,255,.11);
    --ink: #f5f6fa;
    --muted: rgba(245,246,250,.62);
    --faint: rgba(245,246,250,.42);
    --accent: #a78bfa;
    background: radial-gradient(70% 48% at 82% -8%, rgba(167,139,250,.16) 0%, transparent 62%), linear-gradient(178deg,#141326 0%,#0b0a12 60%);
  }
}

@supports (color: oklch(0.7 0.1 300)) {
  @media (prefers-color-scheme: light) {
    .sk-04:has(#sk-04-theme:checked) {
      --bg: oklch(0.14 0.02 295);
      --bg2: oklch(0.21 0.05 292);
      --ink: oklch(0.97 0.005 292);
      --muted: oklch(0.97 0.005 292 / .62);
      --faint: oklch(0.97 0.005 292 / .42);
      --accent: oklch(0.78 0.14 300);
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-04__bar::after {
    animation: none;
    background: none;
  }

  .sk-04__bar {
    background: rgba(128,128,128,.24);
  }

  .sk-04__switch {
    transition: none;
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  @media (prefers-reduced-motion: reduce) {
    .sk-04__bar {
      background: color-mix(in oklab, currentColor 14%, transparent);
    }
  }
}

@media (forced-colors: active) {
  .sk-04__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-04__bar::after {
    animation: none;
    background: none;
  }

  .sk-04__surface,
    .sk-04__spec,
    .sk-04__switch {
    border-color: CanvasText;
  }
}
```
