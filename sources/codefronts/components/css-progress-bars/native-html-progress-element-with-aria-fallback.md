---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/native-html-progress-element-with-aria-fallback/"
title: "Native HTML Progress Element with ARIA Fallback"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The decision primer: a real <progress value=\"68\" max=\"100\"> on the left, a custom role=\"progressbar\" div on the right, both at the same value so you can…"
has_js: "false"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Native HTML Progress Element with ARIA Fallback
Source: https://codefronts.com/components/css-progress-bars/native-html-progress-element-with-aria-fallback/

The decision primer: a real <progress value="68" max="100"> on the left, a custom role="progressbar" div on the right, both at the same value so you can compare what each one buys you. Includes the complete ::-webkit-progress-bar / ::-webkit-progress-value / ::-moz-progress-bar styling block that makes the native element look designed in every engine.
## HTML
```html
<div class="pb-01">
  <input class="pb-01__sr" type="checkbox" id="pb-01-light">
  <label class="pb-01__theme" for="pb-01-light" title="Switch light or dark theme">
    <svg class="pb-01__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-01__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="pb-01__vh">Switch light or dark theme</span>
  </label>

  <div class="pb-01__stage">
    <div class="pb-01__card">
      <header class="pb-01__head">
        <p class="pb-01__eyebrow"><span class="pb-01__badge">Primer</span><span class="pb-01__mono">value = 68 / max = 100</span></p>
        <h2 class="pb-01__title">Native <code>&lt;progress&gt;</code> or a custom bar?</h2>
        <p class="pb-01__lead">Same value, same visual weight, two entirely different accessibility contracts. Pick the left one unless the design makes it impossible.</p>
      </header>

      <div class="pb-01__grid">
        <section class="pb-01__pane pb-01__pane--native" aria-labelledby="pb-01-h-native">
          <h3 class="pb-01__paneTitle" id="pb-01-h-native"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 12.8l2.2 2.2L15.6 9.4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6"/></svg>Native element</h3>
          <label class="pb-01__label" for="pb-01-native">Deploying <span class="pb-01__mono">[email protected]</span></label>
          <progress class="pb-01__native" id="pb-01-native" value="68" max="100">68%</progress>
          <p class="pb-01__row"><span class="pb-01__mono pb-01__num">68%</span><span class="pb-01__hint">announced by AT automatically</span></p>
          <ul class="pb-01__notes">
            <li><strong>Role</strong><span>implicit <code>progressbar</code></span></li>
            <li><strong>Value</strong><span>read from <code>value</code>/<code>max</code></span></li>
            <li><strong>JS needed</strong><span>none</span></li>
          </ul>
        </section>

        <section class="pb-01__pane" aria-labelledby="pb-01-h-aria">
          <h3 class="pb-01__paneTitle"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 7.5h16M4 12h16M4 16.5h9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span id="pb-01-h-aria">ARIA fallback</span></h3>
          <p class="pb-01__label" id="pb-01-lbl">Deploying <span class="pb-01__mono">[email protected]</span></p>
          <div class="pb-01__bar" role="progressbar" aria-valuenow="68" aria-valuemin="0" aria-valuemax="100" aria-labelledby="pb-01-lbl" style="--value:68">
            <span class="pb-01__fill"><span class="pb-01__sheen"></span></span>
          </div>
          <p class="pb-01__row"><span class="pb-01__mono pb-01__num">68%</span><span class="pb-01__hint">you own every announcement</span></p>
          <ul class="pb-01__notes">
            <li><strong>Role</strong><span>explicit <code>role="progressbar"</code></span></li>
            <li><strong>Value</strong><span><code>aria-valuenow</code>, kept in sync by you</span></li>
            <li><strong>JS needed</strong><span>on every value change</span></li>
          </ul>
        </section>
      </div>

      <div class="pb-01__code">
        <p class="pb-01__codeHead"><span class="pb-01__mono">progress.css</span><span class="pb-01__tagline">three engines, one bar</span></p>
        <pre><code>.bar{ appearance:none; block-size:.9rem; border:0;
      border-radius:99px; background:var(--track); }

.bar::-webkit-progress-bar  { background:var(--track); }
.bar::-webkit-progress-value{ background:var(--accent); border-radius:99px; }
.bar::-moz-progress-bar     { background:var(--accent); border-radius:99px; }</code></pre>
      </div>

      <p class="pb-01__foot"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 8.2v.2m0 3.2v4.2" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.5"/></svg>Prefer <code>&lt;progress&gt;</code> when possible — assistive tech announces value automatically.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-01 {
  --bg: #080a0f;
  --card: #0d1017;
  --card2: #12161f;
  --ink: #eef1f7;
  --muted: rgba(238,241,247,.6);
  --line: rgba(238,241,247,.11);
  --track: rgba(238,241,247,.09);
  --accent: #a78bfa;
  --accent-2: #60a5fa;
  --ok: #34d399;
  --radius: 1.35rem;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(70% .18 295)) {
  .pb-01 {
    --accent: oklch(76% .16 295);
    --accent-2: oklch(74% .14 254);
    --ok: oklch(78% .15 162);
  }
}

.pb-01 *,
.pb-01 *::before,
.pb-01 *::after {
  box-sizing: border-box;
}

.pb-01__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(120% 80% at 12% -10%,color-mix(in srgb,var(--accent) 16%,transparent),transparent 62%), radial-gradient(90% 70% at 100% 0%,color-mix(in srgb,var(--accent-2) 12%,transparent),transparent 60%);
}

.pb-01__sr {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pb-01__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pb-01__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-01__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.11);
}

.pb-01__sr:focus-visible + .pb-01__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-01__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-01__sun {
  display: none;
}

.pb-01__moon {
  display: block;
}

.pb-01__card {
  inline-size: min(60rem,100%);
  display: grid;
  gap: clamp(1.1rem,2.6vw,1.8rem);
  padding: clamp(1.25rem,3.4vw,2.4rem);
  border-radius: var(--radius);
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 92%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 30px 70px -40px rgba(0,0,0,.9);
}

.pb-01__head {
  display: grid;
  gap: .55rem;
}

.pb-01__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .6rem;
  margin: 0;
}

.pb-01__badge {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .28rem .55rem;
  border-radius: .45rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 15%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 32%,transparent);
}

.pb-01__mono {
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-01__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,2.1rem);
  line-height: 1.12;
  letter-spacing: -.02em;
  font-weight: 650;
}

.pb-01__title code {
  font-family: var(--mono);
  font-size: .82em;
  color: var(--accent);
}

.pb-01__lead {
  margin: 0;
  max-inline-size: 46ch;
  font-size: clamp(.92rem,1.5vw,1.02rem);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-01__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(15.5rem,1fr));
  gap: clamp(.9rem,2vw,1.3rem);
}

.pb-01__pane {
  display: grid;
  gap: .7rem;
  align-content: start;
  padding: clamp(1rem,2.2vw,1.35rem);
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  background: var(--card2);
}

.pb-01__pane--native {
  border-color: color-mix(in srgb,var(--accent) 34%,transparent);
  box-shadow: 0 0 0 3px color-mix(in srgb,var(--accent) 9%,transparent);
}

.pb-01__paneTitle {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .45rem;
  font-size: .82rem;
  letter-spacing: .02em;
  font-weight: 600;
}

.pb-01__paneTitle svg {
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--accent);
}

.pb-01__pane--native .pb-01__paneTitle svg {
  color: var(--ok);
}

.pb-01__label {
  margin: 0;
  font-size: .86rem;
  color: var(--muted);
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
}

.pb-01__native {
  appearance: none;
  -webkit-appearance: none;
  display: block;
  inline-size: 100%;
  block-size: .9rem;
  border: 0;
  border-radius: 99px;
  overflow: hidden;
  background: var(--track);
  box-shadow: 0 1px 2px rgba(0,0,0,.35) inset;
}

.pb-01__native::-webkit-progress-bar {
  background: var(--track);
  border-radius: 99px;
}

.pb-01__native::-webkit-progress-value {
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
  border-radius: 99px;
  transition: inline-size .4s cubic-bezier(.4,0,.2,1);
}

.pb-01__native::-moz-progress-bar {
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
  border-radius: 99px;
}

.pb-01__bar {
  position: relative;
  inline-size: 100%;
  block-size: .9rem;
  border-radius: 99px;
  background: var(--track);
  border: 1px solid var(--line);
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(0,0,0,.35) inset;
}

.pb-01__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
  transition: inline-size .4s cubic-bezier(.4,0,.2,1);
  overflow: hidden;
}

.pb-01__sheen {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.5),transparent);
  transform: translateX(-100%);
  animation: pb-01-sheen 2.6s cubic-bezier(.4,0,.2,1) infinite;
}

@keyframes pb-01-sheen {
  0% {
    transform: translateX(-100%);
  }

  60%,
    100% {
    transform: translateX(220%);
  }
}

.pb-01__row {
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: .6rem;
  flex-wrap: wrap;
}

.pb-01__num {
  font-size: 1.05rem;
  color: var(--ink);
  font-weight: 600;
}

.pb-01__hint {
  font-size: .76rem;
  color: var(--muted);
}

.pb-01__notes {
  list-style: none;
  margin: .15rem 0 0;
  padding: 0;
  display: grid;
  gap: 0;
}

.pb-01__notes li {
  display: grid;
  grid-template-columns: 5.2rem 1fr;
  gap: .7rem;
  align-items: baseline;
  padding-block: .5rem;
  border-block-start: 1px solid var(--line);
}

.pb-01__notes strong {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 500;
}

.pb-01__notes span {
  font-size: .83rem;
  color: var(--ink);
}

.pb-01__notes code {
  font-family: var(--mono);
  font-size: .78em;
  color: var(--accent);
}

.pb-01__code {
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  background: #05070b;
  overflow: hidden;
}

.pb-01__codeHead {
  margin: 0;
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  padding: .65rem .95rem;
  border-block-end: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
}

.pb-01__tagline {
  font-size: .72rem;
  color: var(--muted);
}

.pb-01__code pre {
  margin: 0;
  padding: 1rem .95rem;
  overflow-x: auto;
}

.pb-01__code code {
  font-family: var(--mono);
  font-size: clamp(.7rem,1.05vw,.81rem);
  line-height: 1.75;
  color: rgba(238,241,247,.78);
  white-space: pre;
}

.pb-01__foot {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .85rem;
  color: var(--muted);
}

.pb-01__foot svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  flex: none;
  color: var(--accent);
}

.pb-01__foot code {
  font-family: var(--mono);
  font-size: .82em;
  color: var(--ink);
}

.pb-01[data-theme="light"],
.pb-01:has(#pb-01-light:checked) {
  --bg: #f6f7fb;
  --card: #ffffff;
  --card2: #f9fafc;
  --ink: #0b1020;
  --muted: rgba(11,16,32,.6);
  --line: rgba(11,16,32,.11);
  --track: rgba(11,16,32,.08);
  --accent: #7c3aed;
  --accent-2: #2563eb;
  --ok: #059669;
}

.pb-01:has(#pb-01-light:checked) .pb-01__theme {
  background: rgba(11,16,32,.05);
}

.pb-01:has(#pb-01-light:checked) .pb-01__code {
  background: #0b1020;
}

.pb-01:has(#pb-01-light:checked) .pb-01__code code {
  color: rgba(238,241,247,.82);
}

.pb-01:has(#pb-01-light:checked) .pb-01__sun {
  display: block;
}

.pb-01:has(#pb-01-light:checked) .pb-01__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .pb-01:not([data-theme="dark"]):not(:has(#pb-01-light:checked)) {
    --bg: #f6f7fb;
    --card: #ffffff;
    --card2: #f9fafc;
    --ink: #0b1020;
    --muted: rgba(11,16,32,.6);
    --line: rgba(11,16,32,.11);
    --track: rgba(11,16,32,.08);
    --accent: #7c3aed;
    --accent-2: #2563eb;
    --ok: #059669;
  }

  .pb-01:not([data-theme="dark"]):not(:has(#pb-01-light:checked)) .pb-01__code {
    background: #0b1020;
  }

  .pb-01:not([data-theme="dark"]):not(:has(#pb-01-light:checked)) .pb-01__theme {
    background: rgba(11,16,32,.05);
  }

  .pb-01:not([data-theme="dark"]):not(:has(#pb-01-light:checked)) .pb-01__sun {
    display: block;
  }

  .pb-01:not([data-theme="dark"]):not(:has(#pb-01-light:checked)) .pb-01__moon {
    display: none;
  }

  .pb-01:not([data-theme="light"]):has(#pb-01-light:checked) {
    --bg: #080a0f;
    --card: #0d1017;
    --card2: #12161f;
    --ink: #eef1f7;
    --muted: rgba(238,241,247,.6);
    --line: rgba(238,241,247,.11);
    --track: rgba(238,241,247,.09);
    --accent: #a78bfa;
    --accent-2: #60a5fa;
    --ok: #34d399;
  }

  .pb-01:not([data-theme="light"]):has(#pb-01-light:checked) .pb-01__theme {
    background: rgba(255,255,255,.06);
  }

  .pb-01:not([data-theme="light"]):has(#pb-01-light:checked) .pb-01__code {
    background: #05070b;
  }

  .pb-01:not([data-theme="light"]):has(#pb-01-light:checked) .pb-01__code code {
    color: rgba(238,241,247,.78);
  }

  .pb-01:not([data-theme="light"]):has(#pb-01-light:checked) .pb-01__sun {
    display: none;
  }

  .pb-01:not([data-theme="light"]):has(#pb-01-light:checked) .pb-01__moon {
    display: block;
  }
}

@media (max-width: 52rem) {
  .pb-01__notes li {
    grid-template-columns: 1fr;
    gap: .1rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-01 *,
    .pb-01 *::before,
    .pb-01 *::after {
    animation: none !important;
    transition: none !important;
  }

  .pb-01__sheen {
    display: none;
  }
}

@media (forced-colors: active) {
  .pb-01__card,
    .pb-01__pane,
    .pb-01__code,
    .pb-01__theme,
    .pb-01__bar {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-01__fill {
    background: Highlight;
  }
}
```
