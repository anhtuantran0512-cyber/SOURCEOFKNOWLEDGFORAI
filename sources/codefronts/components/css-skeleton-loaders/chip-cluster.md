---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/chip-cluster/"
title: "Chip Cluster Filter Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "Eight pill placeholders of deliberately uneven widths, wrapping like the real filter row they stand in for — the faceted-search pattern from every e-commerce…"
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Chip Cluster Filter Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/chip-cluster/

Eight pill placeholders of deliberately uneven widths, wrapping like the real filter row they stand in for — the faceted-search pattern from every e-commerce and issue-tracker UI. Uneven widths are the entire point: equal pills read as a loading widget, uneven ones read as words you cannot make out yet.
## HTML
```html
<div class="sk-22">
  <div class="sk-22__stage">
    <section class="sk-22__wrap" aria-labelledby="sk-22-h">
      <header class="sk-22__head">
        <p class="sk-22__eyebrow">faceted search · 8 chips</p>
        <h2 class="sk-22__h" id="sk-22-h">Uneven pills read as words. Even ones read as a widget.</h2>
        <p class="sk-22__sub">Widths are set in <code>ch</code> from the real label lengths, the height matches the resolved control exactly, and the cluster wraps the same way — so the results grid below never moves.</p>
      </header>

      <div class="sk-22__panel">
        <div class="sk-22__group">
          <p class="sk-22__glabel">Category</p>
          <ul class="sk-22__cluster" role="status" aria-live="polite">
            <span class="sk-22__vh">Loading category filters…</span>
            <li class="sk-22__chip" style="--w:5ch;  --i:0" aria-hidden="true"></li>
            <li class="sk-22__chip" style="--w:9ch;  --i:1" aria-hidden="true"></li>
            <li class="sk-22__chip" style="--w:7ch;  --i:2" aria-hidden="true"></li>
            <li class="sk-22__chip" style="--w:13ch; --i:3" aria-hidden="true"></li>
            <li class="sk-22__chip" style="--w:6ch;  --i:4" aria-hidden="true"></li>
            <li class="sk-22__chip" style="--w:11ch; --i:5" aria-hidden="true"></li>
            <li class="sk-22__chip" style="--w:8ch;  --i:6" aria-hidden="true"></li>
            <li class="sk-22__chip" style="--w:15ch; --i:7" aria-hidden="true"></li>
          </ul>
        </div>

        <div class="sk-22__group">
          <p class="sk-22__glabel">Availability</p>
          <ul class="sk-22__cluster">
            <li><button class="sk-22__real is-on" type="button" aria-pressed="true">In stock</button></li>
            <li><button class="sk-22__real" type="button" aria-pressed="false">Ships today</button></li>
            <li><button class="sk-22__real" type="button" aria-pressed="false">Pickup nearby</button></li>
          </ul>
          <p class="sk-22__gnote">Facet labels come from your own config — render them instantly, skeleton only the values you had to fetch.</p>
        </div>
      </div>

      <aside class="sk-22__spec" aria-label="Recipe">
        <p class="sk-22__srow"><span class="sk-22__skey">width</span><span class="sk-22__sval">inline-size: var(--w) in ch — 5ch, 9ch, 13ch… from real label lengths</span></p>
        <p class="sk-22__srow"><span class="sk-22__skey">height</span><span class="sk-22__sval">block-size: 2.25rem — identical to the resolved chip, so the bar never grows</span></p>
        <p class="sk-22__srow"><span class="sk-22__skey">wrap</span><span class="sk-22__sval">flex-wrap: wrap + gap .6rem — the same reflow as the resolved row</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-22 {
  --chip-h: 2.25rem;
  --bg: #060809;
  --bg2: #0d1012;
  --surface: rgba(255,255,255,.032);
  --raise: rgba(255,255,255,.06);
  --line: rgba(255,255,255,.1);
  --ink: #f4f7f7;
  --muted: rgba(244,247,247,.62);
  --faint: rgba(244,247,247,.42);
  --accent: #7dd3fc;
  --sk: rgba(244,247,247,.1);
  --sheen: rgba(244,247,247,.18);
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
  background: radial-gradient(56% 40% at 18% -6%, rgba(125,211,252,.12) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-22 *,
.sk-22 *::before,
.sk-22 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 230)) {
  .sk-22 {
    --ink: oklch(0.97 0.005 210);
    --muted: oklch(0.97 0.005 210 / .62);
    --faint: oklch(0.97 0.005 210 / .42);
    --accent: oklch(0.84 0.1 232);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-22 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 18%, transparent);
  }
}

.sk-22__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-22__wrap {
  inline-size: min(60rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-22__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
}

.sk-22__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-22__h {
  margin: 0;
  font-size: clamp(1.55rem,3.4vw,2.3rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.08;
  text-wrap: balance;
}

.sk-22__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-22__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-22__panel {
  display: grid;
  gap: 1.4rem;
  padding: clamp(1.1rem,2.2vw,1.6rem);
  border: 1px solid var(--line);
  border-radius: 1.15rem;
  background: var(--surface);
  box-shadow: 0 28px 66px -46px rgba(0,0,0,.9);
}

.sk-22__group {
  display: grid;
  gap: .7rem;
}

.sk-22__glabel {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-22__cluster {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.sk-22__gnote {
  margin: .2rem 0 0;
  font-size: .85rem;
  line-height: 1.55;
  color: var(--muted);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.sk-22__chip {
  display: block;
  position: relative;
  overflow: hidden;
  inline-size: var(--w,8ch);
  block-size: var(--chip-h);
  border-radius: 999px;
  background: var(--sk);
}

.sk-22__chip::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-22-sheen 1.4s linear infinite;
  animation-delay: calc(var(--i,0) * -.14s);
}

@keyframes sk-22-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-22__real {
  min-block-size: var(--chip-h);
  padding: .4rem 1rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .86rem;
  color: var(--muted);
  background: var(--raise);
  border: 1px solid var(--line);
  transition: background .18s ease, color .18s ease;
}

.sk-22__real:hover {
  color: var(--ink);
  background: rgba(255,255,255,.1);
}

.sk-22__real:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.sk-22__real.is-on {
  background: var(--accent);
  border-color: var(--accent);
  color: #04222e;
}

.sk-22__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-22__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-22__skey {
  min-inline-size: 3.8rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-22__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-22[data-theme="light"] {
  --bg: #f7fafb;
  --bg2: #fff;
  --surface: #ffffff;
  --raise: rgba(6,14,18,.05);
  --line: rgba(6,14,18,.11);
  --ink: #060e12;
  --muted: rgba(6,14,18,.62);
  --faint: rgba(6,14,18,.44);
  --accent: #0369a1;
  background: linear-gradient(178deg,#fff 0%,#ecf3f6 100%);
}

.sk-22[data-theme="light"] .sk-22__real.is-on {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .sk-22:not([data-theme="dark"]) {
    --bg: #f7fafb;
    --bg2: #fff;
    --surface: #ffffff;
    --raise: rgba(6,14,18,.05);
    --line: rgba(6,14,18,.11);
    --ink: #060e12;
    --muted: rgba(6,14,18,.62);
    --faint: rgba(6,14,18,.44);
    --accent: #0369a1;
    background: linear-gradient(178deg,#fff 0%,#ecf3f6 100%);
  }

  .sk-22:not([data-theme="dark"]) .sk-22__real.is-on {
    color: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-22__chip::after {
    animation: none;
    background: none;
  }

  .sk-22__chip {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }

  .sk-22__real {
    transition: none;
  }
}

@media (forced-colors: active) {
  .sk-22__chip {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-22__chip::after {
    animation: none;
    background: none;
  }

  .sk-22__panel,
    .sk-22__spec,
    .sk-22__real {
    border-color: CanvasText;
  }
}
```
