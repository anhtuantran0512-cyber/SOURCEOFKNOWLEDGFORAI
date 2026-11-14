---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/goal-tracker/"
title: "Fundraising Goal Progress Tracker with Milestones"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "A campaign bar that means something: milestone ticks at 25/50/75/100 with money labels, a callout pinned above the current amount, and a days-remaining pill."
has_js: "false"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fundraising Goal Progress Tracker with Milestones
Source: https://codefronts.com/components/css-progress-bars/goal-tracker/

A campaign bar that means something: milestone ticks at 25/50/75/100 with money labels, a callout pinned above the current amount, and a days-remaining pill. The pointer is positioned from the same --value as the fill, so they can never drift apart.
## HTML
```html
<div class="pb-17">
  <input class="pb-17__sr" type="checkbox" id="pb-17-dark">
  <label class="pb-17__theme" for="pb-17-dark" title="Switch light or dark theme">
    <svg class="pb-17__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-17__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="pb-17__vh">Switch light or dark theme</span>
  </label>

  <div class="pb-17__stage">
    <div class="pb-17__card">
      <header class="pb-17__head">
        <span class="pb-17__org">
          <span class="pb-17__orgMark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M12 20.2S4.2 15.6 4.2 10.2A4 4 0 0 1 12 8.4a4 4 0 0 1 7.8 1.8c0 5.4-7.8 10-7.8 10Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></span>
          <span class="pb-17__orgMeta"><span class="pb-17__orgName">Riverside Library Fund</span><span class="pb-17__orgSub">Organised by Jordan Lee</span></span>
        </span>
        <span class="pb-17__days"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.6" stroke="currentColor" stroke-width="1.7"/><path d="M12 7.6V12l3 1.9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>19 days left</span>
      </header>

      <p class="pb-17__amounts">
        <span class="pb-17__raised">&pound;62,450</span>
        <span class="pb-17__goal">raised of &pound;100,000 goal</span>
      </p>

      <div class="pb-17__barWrap">
        <p class="pb-17__callout">
          <span class="pb-17__calloutInner"><span class="pb-17__mono">&pound;62,450</span> raised</span>
        </p>
        <div class="pb-17__bar" role="progressbar" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100" aria-valuetext="62,450 pounds raised of a 100,000 pound goal" aria-label="Fundraising progress" style="--value:62.45">
          <span class="pb-17__fill"></span>
          <span class="pb-17__tick pb-17__tick--passed" style="--at:25"><b>&pound;25k</b></span>
          <span class="pb-17__tick pb-17__tick--passed" style="--at:50"><b>&pound;50k</b></span>
          <span class="pb-17__tick" style="--at:75"><b>&pound;75k</b></span>
          <span class="pb-17__tick pb-17__tick--end" style="--at:100"><b>&pound;100k goal</b></span>
        </div>
      </div>

      <div class="pb-17__stats">
        <p class="pb-17__stat"><span class="pb-17__statNum">1,284</span><span class="pb-17__statKey">donors</span></p>
        <p class="pb-17__stat"><span class="pb-17__statNum">&pound;48.6</span><span class="pb-17__statKey">average gift</span></p>
        <p class="pb-17__stat"><span class="pb-17__statNum">62%</span><span class="pb-17__statKey">of goal</span></p>
      </div>

      <div class="pb-17__actions">
        <button class="pb-17__btn pb-17__btn--primary" type="button">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 20.2S4.2 15.6 4.2 10.2A4 4 0 0 1 12 8.4a4 4 0 0 1 7.8 1.8c0 5.4-7.8 10-7.8 10Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>Donate
        </button>
        <button class="pb-17__btn" type="button">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8.5 13.5 15 17M15 7l-6.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="17.2" cy="5.6" r="2.4" stroke="currentColor" stroke-width="1.7"/><circle cx="6.4" cy="12" r="2.4" stroke="currentColor" stroke-width="1.7"/><circle cx="17.2" cy="18.4" r="2.4" stroke="currentColor" stroke-width="1.7"/></svg>Share
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-17 {
  --bg: #faf8f4;
  --card: #ffffff;
  --card2: #f7f5f1;
  --ink: #171310;
  --muted: rgba(23,19,16,.6);
  --line: rgba(23,19,16,.11);
  --track: rgba(23,19,16,.09);
  --accent: #0d9488;
  --accent-2: #14b8a6;
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

@supports (color: oklch(60% .12 180)) {
  .pb-17 {
    --accent: oklch(58% .11 183);
    --accent-2: oklch(70% .12 180);
  }
}

.pb-17 *,
.pb-17 *::before,
.pb-17 *::after {
  box-sizing: border-box;
}

.pb-17__sr {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pb-17__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pb-17__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(70% 55% at 90% 0%,color-mix(in srgb,var(--accent) 12%,transparent),transparent 58%);
}

.pb-17__theme {
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
  background: rgba(23,19,16,.05);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-17__theme:hover {
  transform: translateY(-1px);
}

.pb-17__sr:focus-visible + .pb-17__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-17__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-17__sun {
  display: block;
}

.pb-17__moon {
  display: none;
}

.pb-17__card {
  inline-size: min(42rem,100%);
  display: grid;
  gap: clamp(1.1rem,2.6vw,1.6rem);
  padding: clamp(1.4rem,3.4vw,2.3rem);
  border-radius: 1.4rem;
  border: 1px solid var(--line);
  background: var(--card);
  box-shadow: 0 1px 2px rgba(23,19,16,.05),0 26px 60px -40px rgba(23,19,16,.4);
}

.pb-17__head {
  display: flex;
  flex-wrap: wrap;
  gap: .8rem;
  align-items: center;
  justify-content: space-between;
}

.pb-17__org {
  display: flex;
  gap: .7rem;
  align-items: center;
}

.pb-17__orgMark {
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: .75rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 12%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 26%,transparent);
}

.pb-17__orgMark svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
}

.pb-17__orgMeta {
  display: grid;
  gap: .1rem;
}

.pb-17__orgName {
  font-size: .95rem;
  font-weight: 650;
  letter-spacing: -.01em;
}

.pb-17__orgSub {
  font-size: .76rem;
  color: var(--muted);
}

.pb-17__days {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .4rem .7rem;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: var(--card2);
  font-size: .78rem;
  font-weight: 600;
  color: var(--muted);
}

.pb-17__days svg {
  inline-size: .95rem;
  block-size: .95rem;
}

.pb-17__amounts {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: .55rem;
}

.pb-17__raised {
  font-size: clamp(2rem,6vw,3rem);
  font-weight: 700;
  letter-spacing: -.035em;
  color: var(--accent);
  font-variant-numeric: tabular-nums;
}

.pb-17__goal {
  font-size: .92rem;
  color: var(--muted);
}

.pb-17__barWrap {
  position: relative;
  padding-block: 2.4rem 2.2rem;
}

.pb-17__callout {
  position: absolute;
  inset-block-start: 0;
  margin: 0;
  inset-inline-start: clamp(4rem,calc(var(--value,0) * 1%),calc(100% - 4rem));
  transform: translateX(-50%);
}

.pb-17__barWrap {
  --value: 62.45;
}

.pb-17__calloutInner {
  position: relative;
  display: inline-block;
  white-space: nowrap;
  padding: .35rem .65rem;
  border-radius: .6rem;
  background: var(--ink);
  color: var(--card);
  font-size: .78rem;
  font-weight: 600;
  box-shadow: 0 8px 20px -12px rgba(23,19,16,.7);
}

.pb-17__calloutInner::after {
  content: "";
  position: absolute;
  inset-block-start: 100%;
  inset-inline-start: 50%;
  transform: translateX(-50%);
  border: .32rem solid transparent;
  border-block-start-color: var(--ink);
}

.pb-17__calloutInner .pb-17__mono {
  color: var(--card);
}

.pb-17__mono {
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
}

.pb-17__bar {
  position: relative;
  inline-size: 100%;
  block-size: .9rem;
  border-radius: 99px;
  background: var(--track);
  border: 1px solid var(--line);
  box-shadow: 0 1px 2px rgba(23,19,16,.12) inset;
}

.pb-17__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
  box-shadow: 0 0 16px -4px color-mix(in srgb,var(--accent) 60%,transparent);
  animation: pb-17-reveal .9s cubic-bezier(.4,0,.2,1) both;
}

@keyframes pb-17-reveal {
  from {
    inline-size: 0;
  }
}

.pb-17__tick {
  position: absolute;
  inset-block: -.4rem;
  inset-inline-start: calc(var(--at) * 1%);
  inline-size: 2px;
  background: color-mix(in srgb,var(--ink) 22%,transparent);
  border-radius: 2px;
}

.pb-17__tick b {
  position: absolute;
  inset-block-start: calc(100% + .35rem);
  inset-inline-start: 50%;
  transform: translateX(-50%);
  white-space: nowrap;
  font-size: .72rem;
  font-weight: 600;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-17__tick--passed {
  background: color-mix(in srgb,var(--accent) 75%,white);
}

.pb-17__tick--passed b {
  color: var(--accent);
}

.pb-17__tick--end {
  inline-size: 3px;
  background: var(--ink);
}

.pb-17__tick--end b {
  inset-inline-start: auto;
  inset-inline-end: 0;
  transform: none;
  color: var(--ink);
}

.pb-17__stats {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(7rem,1fr));
  gap: .6rem;
  padding-block: .2rem;
}

.pb-17__stat {
  margin: 0;
  display: grid;
  gap: .1rem;
  padding: .7rem .85rem;
  border-radius: .9rem;
  border: 1px solid var(--line);
  background: var(--card2);
}

.pb-17__statNum {
  font-size: 1.15rem;
  font-weight: 650;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.pb-17__statKey {
  font-family: var(--mono);
  font-size: .63rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.pb-17__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.pb-17__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.9rem;
  padding: .7rem 1.2rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: var(--card2);
  color: var(--ink);
  font: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform .18s,background .18s;
}

.pb-17__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.pb-17__btn:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
}

.pb-17__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-17__btn--primary {
  flex: 1 1 12rem;
  justify-content: center;
  background: var(--accent);
  border-color: transparent;
  color: #fff;
  box-shadow: 0 14px 30px -18px var(--accent);
}

.pb-17__btn--primary:hover {
  background: color-mix(in srgb,var(--accent) 88%,black);
}

.pb-17[data-theme="dark"],
.pb-17:has(#pb-17-dark:checked) {
  --bg: #0a0c0c;
  --card: #101414;
  --card2: #161b1b;
  --ink: #eaf3f1;
  --muted: rgba(234,243,241,.62);
  --line: rgba(234,243,241,.13);
  --track: rgba(234,243,241,.1);
  --accent: #2dd4bf;
  --accent-2: #5eead4;
}

.pb-17:has(#pb-17-dark:checked) .pb-17__theme {
  background: rgba(255,255,255,.07);
}

.pb-17:has(#pb-17-dark:checked) .pb-17__sun {
  display: none;
}

.pb-17:has(#pb-17-dark:checked) .pb-17__moon {
  display: block;
}

.pb-17:has(#pb-17-dark:checked) .pb-17__btn--primary {
  color: #05201c;
}

@media (prefers-color-scheme: dark) {
  .pb-17:not([data-theme="light"]):not(:has(#pb-17-dark:checked)) {
    --bg: #0a0c0c;
    --card: #101414;
    --card2: #161b1b;
    --ink: #eaf3f1;
    --muted: rgba(234,243,241,.62);
    --line: rgba(234,243,241,.13);
    --track: rgba(234,243,241,.1);
    --accent: #2dd4bf;
    --accent-2: #5eead4;
  }

  .pb-17:not([data-theme="light"]):not(:has(#pb-17-dark:checked)) .pb-17__theme {
    background: rgba(255,255,255,.07);
  }

  .pb-17:not([data-theme="light"]):not(:has(#pb-17-dark:checked)) .pb-17__sun {
    display: none;
  }

  .pb-17:not([data-theme="light"]):not(:has(#pb-17-dark:checked)) .pb-17__moon {
    display: block;
  }

  .pb-17:not([data-theme="light"]):not(:has(#pb-17-dark:checked)) .pb-17__btn--primary {
    color: #05201c;
  }

  .pb-17:not([data-theme="dark"]):has(#pb-17-dark:checked) {
    --bg: #faf8f4;
    --card: #ffffff;
    --card2: #f7f5f1;
    --ink: #171310;
    --muted: rgba(23,19,16,.6);
    --line: rgba(23,19,16,.11);
    --track: rgba(23,19,16,.09);
    --accent: #0d9488;
    --accent-2: #14b8a6;
  }

  .pb-17:not([data-theme="dark"]):has(#pb-17-dark:checked) .pb-17__theme {
    background: rgba(23,19,16,.05);
  }

  .pb-17:not([data-theme="dark"]):has(#pb-17-dark:checked) .pb-17__sun {
    display: block;
  }

  .pb-17:not([data-theme="dark"]):has(#pb-17-dark:checked) .pb-17__moon {
    display: none;
  }

  .pb-17:not([data-theme="dark"]):has(#pb-17-dark:checked) .pb-17__btn--primary {
    color: #fff;
  }
}

@media (max-width: 30rem) {
  .pb-17__tick:not(.pb-17__tick--end) b {
    font-size: .66rem;
  }

  .pb-17__barWrap {
    padding-block: 2.4rem 2.6rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-17 *,
    .pb-17 *::before,
    .pb-17 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-17__card,
    .pb-17__bar,
    .pb-17__btn,
    .pb-17__stat,
    .pb-17__theme,
    .pb-17__days {
    border-color: CanvasText;
    box-shadow: none;
  }

  .pb-17__fill {
    background: Highlight;
    box-shadow: none;
  }

  .pb-17__calloutInner {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
```
