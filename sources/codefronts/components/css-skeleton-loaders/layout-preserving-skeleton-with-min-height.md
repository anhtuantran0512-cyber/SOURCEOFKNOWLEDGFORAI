---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/layout-preserving-skeleton-with-min-height/"
title: "Layout-Preserving Skeleton with min-height"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "A skeleton that is shorter than its content doesn't prevent layout shift — it schedules one."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Layout-Preserving Skeleton with min-height
Source: https://codefronts.com/components/css-skeleton-loaders/layout-preserving-skeleton-with-min-height/

A skeleton that is shorter than its content doesn't prevent layout shift — it schedules one. Both columns here load the same article; the left one lets the content push the footer down, the right one declares min-height and aspect-ratio so nothing below it ever moves. Flip the switch and watch the ruler.
## HTML
```html
<div class="sk-10">
  <input class="sk-10__sr" type="checkbox" id="sk-10-load">
  <div class="sk-10__stage">
    <section class="sk-10__wrap" aria-labelledby="sk-10-h">
      <header class="sk-10__head">
        <p class="sk-10__eyebrow">Core Web Vitals · CLS</p>
        <h2 class="sk-10__h" id="sk-10-h">Reserve the space, or schedule the jump</h2>
        <p class="sk-10__sub">Same article, same skeleton, one difference: the right column declares <code>min-height</code> and <code>aspect-ratio</code>. Watch the ruler and the footer row, not the card.</p>
        <label class="sk-10__switch" for="sk-10-load">
          <span class="sk-10__track" aria-hidden="true"><span class="sk-10__thumb"></span></span>
          <span class="sk-10__switchtext">Simulate content arriving</span>
        </label>
      </header>

      <div class="sk-10__cols">
        <article class="sk-10__col sk-10__col--bad">
          <header class="sk-10__chead">
            <p class="sk-10__label">no reservation</p>
            <p class="sk-10__badge sk-10__badge--bad">CLS 0.19</p>
          </header>
          <div class="sk-10__slot sk-10__slot--loose" role="status" aria-live="polite">
            <span class="sk-10__vh">Loading article…</span>
            <div class="sk-10__skel" aria-hidden="true">
              <span class="sk-10__bar sk-10__bar--thumb"></span>
              <span class="sk-10__bar sk-10__bar--title"></span>
              <span class="sk-10__bar sk-10__bar--sm"></span>
              <span class="sk-10__bar sk-10__bar--sm" style="inline-size:56%"></span>
            </div>
            <div class="sk-10__real">
              <img class="sk-10__img" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&amp;fit=crop&amp;w=640&amp;h=360&amp;q=70" width="640" height="360" alt="Sunlight through a beech forest" loading="lazy" decoding="async">
              <h3 class="sk-10__title">Field data beats a stopwatch</h3>
              <p class="sk-10__copy">Sam Rivera pulled p75 CLS from RUM instead of the lab and found three routes where the loading shell was two rows shorter than the page it stood in for. The fix was six lines of CSS.</p>
              <p class="sk-10__by">Sam Rivera · Performance · 6 min read</p>
            </div>
          </div>
          <p class="sk-10__ruler" aria-hidden="true">footer baseline</p>
          <footer class="sk-10__foot">
            <span class="sk-10__fdot" aria-hidden="true"></span>
            <p class="sk-10__ftext">This row moves down 118px when the article lands.</p>
          </footer>
        </article>

        <article class="sk-10__col sk-10__col--good">
          <header class="sk-10__chead">
            <p class="sk-10__label sk-10__label--on">min-height: 19rem</p>
            <p class="sk-10__badge sk-10__badge--good">
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12.6 9.6 17 19 7.5" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
              CLS 0.00
            </p>
          </header>
          <div class="sk-10__slot sk-10__slot--fixed" role="status" aria-live="polite">
            <span class="sk-10__vh">Loading article…</span>
            <div class="sk-10__skel" aria-hidden="true">
              <span class="sk-10__bar sk-10__bar--media"></span>
              <span class="sk-10__bar sk-10__bar--title"></span>
              <span class="sk-10__bar sk-10__bar--sm"></span>
              <span class="sk-10__bar sk-10__bar--sm" style="inline-size:56%"></span>
            </div>
            <div class="sk-10__real">
              <img class="sk-10__img" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&amp;fit=crop&amp;w=640&amp;h=360&amp;q=70" width="640" height="360" alt="Sunlight through a beech forest" loading="lazy" decoding="async">
              <h3 class="sk-10__title">Field data beats a stopwatch</h3>
              <p class="sk-10__copy">Sam Rivera pulled p75 CLS from RUM instead of the lab and found three routes where the loading shell was two rows shorter than the page it stood in for. The fix was six lines of CSS.</p>
              <p class="sk-10__by">Sam Rivera · Performance · 6 min read</p>
            </div>
          </div>
          <p class="sk-10__ruler" aria-hidden="true">footer baseline</p>
          <footer class="sk-10__foot">
            <span class="sk-10__fdot" aria-hidden="true"></span>
            <p class="sk-10__ftext">This row never moves. The box was already the right size.</p>
          </footer>
        </article>
      </div>

      <aside class="sk-10__spec" aria-label="Recipe">
        <p class="sk-10__srow"><span class="sk-10__skey">slot</span><span class="sk-10__sval">min-block-size: 19rem (or clamp(16rem, 26vw, 22rem)) + contain: layout</span></p>
        <p class="sk-10__srow"><span class="sk-10__skey">media</span><span class="sk-10__sval">aspect-ratio: 16/9 + width/height attributes on every img</span></p>
        <p class="sk-10__srow"><span class="sk-10__skey">verify</span><span class="sk-10__sval">field p75 CLS from RUM, not a lab run — target 0.00</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-10 {
  --bg: #ffffff;
  --bg2: #f2f4f8;
  --surface: #fcfdff;
  --line: rgba(10,14,26,.12);
  --ink: #0a0e1a;
  --muted: rgba(10,14,26,.64);
  --faint: rgba(10,14,26,.45);
  --accent: #1d4ed8;
  --bad: #c2410c;
  --good: #0f7b4f;
  --sk: rgba(10,14,26,.09);
  --sheen: rgba(10,14,26,.16);
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
  background: radial-gradient(58% 40% at 90% -8%, rgba(29,78,216,.08) 0%, transparent 60%), linear-gradient(178deg,#fff 0%,var(--bg2) 100%);
}

.sk-10 *,
.sk-10 *::before,
.sk-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 260)) {
  .sk-10 {
    --ink: oklch(0.17 0.02 265);
    --muted: oklch(0.17 0.02 265 / .64);
    --faint: oklch(0.17 0.02 265 / .45);
    --accent: oklch(0.5 0.17 265);
    --bad: oklch(0.55 0.17 40);
    --good: oklch(0.52 0.13 155);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-10 {
    --sk: color-mix(in oklab, currentColor 9%, transparent);
    --sheen: color-mix(in oklab, currentColor 16%, transparent);
  }
}

.sk-10__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-10__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.sk-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-10__wrap {
  inline-size: min(74rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-10__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 47rem;
  justify-items: start;
}

.sk-10__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-10__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-10__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-10__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-10__switch {
  margin-block-start: .35rem;
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  gap: .7rem;
  cursor: pointer;
  font-size: .9rem;
  font-weight: 500;
}

.sk-10__track {
  inline-size: 2.9rem;
  block-size: 1.7rem;
  border-radius: 999px;
  background: var(--sk);
  border: 1px solid var(--line);
  display: flex;
  align-items: center;
  padding: .18rem;
  transition: background .2s ease;
}

.sk-10__thumb {
  inline-size: 1.25rem;
  block-size: 1.25rem;
  border-radius: 999px;
  background: #fff;
  box-shadow: 0 2px 6px rgba(10,14,26,.3);
  transition: translate .2s cubic-bezier(.2,.7,.3,1);
}

.sk-10:has(#sk-10-load:checked) .sk-10__track {
  background: var(--accent);
  border-color: var(--accent);
}

.sk-10:has(#sk-10-load:checked) .sk-10__thumb {
  translate: 1.2rem 0;
}

.sk-10__sr:focus-visible + .sk-10__stage .sk-10__track {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.sk-10__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(18rem,1fr));
  align-items: start;
}

.sk-10__col {
  display: grid;
  gap: .75rem;
  padding: clamp(1rem,1.9vw,1.4rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
  box-shadow: 0 22px 50px -38px rgba(10,14,26,.45);
}

.sk-10__col--bad {
  border-color: rgba(194,65,12,.3);
}

.sk-10__col--good {
  border-color: rgba(15,123,79,.32);
}

.sk-10__chead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .8rem;
  flex-wrap: wrap;
}

.sk-10__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--bad);
}

.sk-10__label--on {
  color: var(--good);
}

.sk-10__badge {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  padding: .3rem .65rem;
  border-radius: 999px;
  font-family: var(--mono);
  font-size: .72rem;
  font-variant-numeric: tabular-nums;
  border: 1px solid;
}

.sk-10__badge svg {
  inline-size: .9rem;
  block-size: .9rem;
}

.sk-10__badge--bad {
  color: var(--bad);
  border-color: rgba(194,65,12,.35);
  background: rgba(194,65,12,.08);
}

.sk-10__badge--good {
  color: var(--good);
  border-color: rgba(15,123,79,.35);
  background: rgba(15,123,79,.08);
}

.sk-10__slot {
  display: grid;
  gap: .7rem;
  padding: .9rem;
  border: 1px dashed var(--line);
  border-radius: .85rem;
  background: rgba(0,0,0,.015);
}

.sk-10__slot--fixed {
  min-block-size: 19rem;
  contain: layout;
}

.sk-10__real {
  display: none;
  gap: .7rem;
}

.sk-10:has(#sk-10-load:checked) .sk-10__skel {
  display: none;
}

.sk-10:has(#sk-10-load:checked) .sk-10__real {
  display: grid;
}

.sk-10__skel {
  display: grid;
  gap: .7rem;
}

.sk-10__img {
  inline-size: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
  border-radius: .6rem;
  background: var(--sk);
  display: block;
}

.sk-10__col--bad .sk-10__img {
  aspect-ratio: auto;
}

.sk-10__title {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.sk-10__copy {
  margin: 0;
  font-size: .88rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-10__by {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--faint);
}

.sk-10__ruler {
  margin: 0;
  padding-block-start: .4rem;
  border-block-start: 2px dashed var(--accent);
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
  opacity: .75;
}

.sk-10__foot {
  display: flex;
  align-items: center;
  gap: .6rem;
}

.sk-10__fdot {
  inline-size: .55rem;
  block-size: .55rem;
  border-radius: 999px;
  background: var(--accent);
  flex: none;
}

.sk-10__ftext {
  margin: 0;
  font-size: .82rem;
  color: var(--muted);
}

.sk-10__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-10__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-10-sheen 1.4s linear infinite;
}

@keyframes sk-10-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-10__bar--sm {
  block-size: .68rem;
}

.sk-10__bar--title {
  block-size: 1.25rem;
  inline-size: 78%;
  border-radius: 7px;
}

.sk-10__bar--media {
  block-size: auto;
  aspect-ratio: 16/9;
  border-radius: .6rem;
}

.sk-10__bar--thumb {
  block-size: 4.4rem;
  border-radius: .6rem;
}

.sk-10__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-10__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-10__skey {
  min-inline-size: 3.6rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-10__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-10[data-theme="dark"] {
  --bg: #07090f;
  --bg2: #0d1018;
  --surface: rgba(255,255,255,.03);
  --line: rgba(255,255,255,.11);
  --ink: #f2f5fb;
  --muted: rgba(242,245,251,.62);
  --faint: rgba(242,245,251,.42);
  --accent: #7aa2ff;
  --bad: #fb923c;
  --good: #4ade9a;
  background: linear-gradient(178deg,#0d1018 0%,#07090f 100%);
}

.sk-10[data-theme="dark"] .sk-10__slot {
  background: rgba(255,255,255,.02);
}

@media (prefers-color-scheme: dark) {
  .sk-10:not([data-theme="light"]) {
    --bg: #07090f;
    --bg2: #0d1018;
    --surface: rgba(255,255,255,.03);
    --line: rgba(255,255,255,.11);
    --ink: #f2f5fb;
    --muted: rgba(242,245,251,.62);
    --faint: rgba(242,245,251,.42);
    --accent: #7aa2ff;
    --bad: #fb923c;
    --good: #4ade9a;
    background: linear-gradient(178deg,#0d1018 0%,#07090f 100%);
  }

  .sk-10:not([data-theme="light"]) .sk-10__slot {
    background: rgba(255,255,255,.02);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-10__bar::after {
    animation: none;
    background: none;
  }

  .sk-10__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }

  .sk-10__thumb,
    .sk-10__track {
    transition: none;
  }
}

@media (forced-colors: active) {
  .sk-10__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-10__bar::after {
    animation: none;
    background: none;
  }

  .sk-10__col,
    .sk-10__slot,
    .sk-10__spec,
    .sk-10__badge,
    .sk-10__track {
    border-color: CanvasText;
  }
}
```
