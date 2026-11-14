---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/image-zoom-hover-transition/"
title: "Transitioning Transform Scale Without Layout Shift"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "An editorial image card that scales inside an overflow: hidden frame, so the zoom never touches the surrounding layout."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transitioning Transform Scale Without Layout Shift
Source: https://codefronts.com/motion/css-transition-designs/image-zoom-hover-transition/

An editorial image card that scales inside an overflow: hidden frame, so the zoom never touches the surrounding layout. Covers the two traps that make hand-rolled zooms look broken: scaling the media instead of a wrapper leaves the frame's rounded corners cutting the wrong shape, and scaling text rasterises it at the old size so captions go soft mid-transition.
## HTML
```html
<section class="trn-05" aria-labelledby="trn-05-heading">
  <div class="trn-05__stage">
    <div class="trn-05__theme">
      <input class="trn-05__themecb" type="checkbox" id="trn-05-theme">
      <label class="trn-05__themebtn" for="trn-05-theme">
        <span class="trn-05__themeico" aria-hidden="true">
          <svg class="trn-05__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-05__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-05__head">
      <p class="trn-05__kicker">Field notes / 08</p>
      <h2 class="trn-05__heading" id="trn-05-heading">A zoom that moves nothing around it</h2>
      <p class="trn-05__sub">Hover or focus a card. The frame is fixed; only the layer inside it scales.</p>
    </header>

    <div class="trn-05__grid">
      <article class="trn-05__card">
        <a class="trn-05__frame" href="#trn-05-heading" aria-label="Read: The warehouse that runs on Fridays">
          <span class="trn-05__zoom trn-05__zoom--a" aria-hidden="true">
            <span class="trn-05__ph">Photograph placeholder &middot; 3:2</span>
          </span>
        </a>
        <p class="trn-05__meta">Infrastructure &middot; 6 min</p>
        <h3 class="trn-05__title"><a href="#trn-05-heading">The warehouse that runs on Fridays</a></h3>
        <p class="trn-05__dek">Meridian moved every nightly job to a single window and cut its on-call pages by two thirds.</p>
        <p class="trn-05__byline">Priya Sharma</p>
      </article>

      <article class="trn-05__card">
        <a class="trn-05__frame" href="#trn-05-heading" aria-label="Read: Sable's twelve-person platform team">
          <span class="trn-05__zoom trn-05__zoom--b" aria-hidden="true">
            <span class="trn-05__ph">Photograph placeholder &middot; 3:2</span>
          </span>
        </a>
        <p class="trn-05__meta">Teams &middot; 9 min</p>
        <h3 class="trn-05__title"><a href="#trn-05-heading">Sable's twelve-person platform team</a></h3>
        <p class="trn-05__dek">What changed when review moved from a weekly board to the pull request itself.</p>
        <p class="trn-05__byline">Jordan Lee</p>
      </article>
    </div>

    <p class="trn-05__foot">The caption sits outside the scaled wrapper on purpose — type inside a scaling layer is rasterised at 1&times; and stretched, which reads as blur.</p>
  </div>
</section>
```
## CSS
```css
.trn-05 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #fbfaf7;
  --page: oklch(0.98 0.005 90);
  --ink: #14130f;
  --ink: oklch(0.19 0.008 80);
  --muted: #5f5c54;
  --muted: oklch(0.49 0.01 85);
  --rule: #ddd9d0;
  --rule: oklch(0.89 0.008 88);
  --wash: #ebe7de;
  --wash: oklch(0.93 0.01 88);
  --accent: #14130f;
  --zoom: 1.07;
  --font-display: "Iowan Old Style", "Palatino Linotype", Georgia, "Times New Roman", serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-05 *,
.trn-05 *::before,
.trn-05 *::after {
  box-sizing: border-box;
}

.trn-05__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 6vw, 72px) 18px;
}

.trn-05__head {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  margin: 0 0 34px;
  padding-block-end: 20px;
  border-block-end: 1px solid var(--ink);
}

.trn-05__kicker {
  margin: 0 0 14px;
  font: 400 11.5px/1 system-ui, sans-serif;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-05__heading {
  margin: 0 0 12px;
  font: 400 clamp(28px, 5.6vw, 46px)/1.06 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-05__sub {
  margin: 0;
  max-inline-size: 46ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-05__grid {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 40px;
}

.trn-05__card {
  min-inline-size: 0;
}

.trn-05__frame {
  display: block;
  position: relative;
  aspect-ratio: 3 / 2;
  margin-block-end: 16px;
  overflow: hidden;
  isolation: isolate;
  border-radius: 3px;
  background: var(--wash);
}

.trn-05__frame:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.trn-05__zoom {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  transition: transform 620ms cubic-bezier(.22, .68, .28, 1), filter 620ms ease;
}

.trn-05__zoom--a {
  background: linear-gradient(140deg, #cfc6b5 0%, #a99e8b 55%, #7d7466 100%);
  transform-origin: 50% 32%;
}

.trn-05__zoom--b {
  background: linear-gradient(140deg, #c3ccc6 0%, #97a49d 55%, #6c7873 100%);
  transform-origin: 62% 40%;
}

.trn-05__frame:hover .trn-05__zoom,
.trn-05__frame:focus-visible .trn-05__zoom {
  transform: scale(var(--zoom));
  filter: saturate(1.06);
}

.trn-05__ph {
  padding: 0 12px;
  font: 400 11px/1.4 system-ui, sans-serif;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: rgba(20, 19, 15, 0.55);
  text-align: center;
}

.trn-05__meta {
  margin: 0 0 8px;
  font: 500 11px/1 system-ui, sans-serif;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-05__title {
  margin: 0 0 10px;
  font: 400 clamp(20px, 3vw, 25px)/1.18 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.trn-05__title a {
  color: var(--ink);
  text-decoration: none;
  border-block-end: 1px solid transparent;
  transition: border-color 220ms ease, color 220ms ease;
}

.trn-05__title a:hover {
  border-color: var(--ink);
}

.trn-05__title a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.trn-05__dek {
  margin: 0 0 12px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-05__byline {
  margin: 0;
  font: 400 12.5px/1 var(--font-display);
  font-style: italic;
  color: var(--muted);
}

.trn-05__foot {
  inline-size: 100%;
  max-inline-size: 54rem;
  margin: 40px 0 0;
  padding-block-start: 18px;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .trn-05__zoom {
    transition: filter 180ms ease, opacity 180ms ease;
  }

  .trn-05__frame:hover .trn-05__zoom,
    .trn-05__frame:focus-visible .trn-05__zoom {
    transform: none;
    filter: brightness(1.06) saturate(1.1);
  }
}

@media (prefers-color-scheme: dark) {
  .trn-05 {
    --page: #131211;
    --page: oklch(0.19 0.005 80);
    --ink: #f4f1ea;
    --ink: oklch(0.96 0.008 88);
    --muted: #a49f95;
    --muted: oklch(0.71 0.012 86);
    --rule: #302e2a;
    --wash: #23211e;
    --accent: #f4f1ea;
  }

  .trn-05__ph {
    color: rgba(244, 241, 234, 0.62);
  }

  .trn-05__zoom--a {
    background: linear-gradient(140deg, #4b463c 0%, #33302a 55%, #221f1b 100%);
  }

  .trn-05__zoom--b {
    background: linear-gradient(140deg, #3d4642 0%, #2c3330 55%, #1e2321 100%);
  }
}

[data-theme="dark"] .trn-05 {
  --page: #131211;
  --ink: #f4f1ea;
  --muted: #a49f95;
  --rule: #302e2a;
  --wash: #23211e;
  --accent: #f4f1ea;
}

[data-theme="dark"] .trn-05__ph {
  color: rgba(244, 241, 234, 0.62);
}

[data-theme="dark"] .trn-05__zoom--a {
  background: linear-gradient(140deg, #4b463c 0%, #33302a 55%, #221f1b 100%);
}

[data-theme="dark"] .trn-05__zoom--b {
  background: linear-gradient(140deg, #3d4642 0%, #2c3330 55%, #1e2321 100%);
}

.trn-05__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-05__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-05__themebtn {
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

.trn-05__themebtn:hover {
  color: var(--ink);
}

.trn-05__themecb:focus-visible + .trn-05__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-05__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-05__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-05__sun {
  opacity: 1;
}

.trn-05__moon {
  opacity: 0.34;
}

.trn-05:has(#trn-05-theme:checked) .trn-05__sun {
  opacity: 0.34;
}

.trn-05:has(#trn-05-theme:checked) .trn-05__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-05:has(#trn-05-theme:checked) {
    --page: #131211;
    --page: oklch(0.19 0.005 80);
    --ink: #f4f1ea;
    --ink: oklch(0.96 0.008 88);
    --muted: #a49f95;
    --muted: oklch(0.71 0.012 86);
    --rule: #302e2a;
    --wash: #23211e;
    --accent: #f4f1ea;
  }

  .trn-05:has(#trn-05-theme:checked) .trn-05__ph {
    color: rgba(244, 241, 234, 0.62);
  }

  .trn-05:has(#trn-05-theme:checked) .trn-05__zoom--a {
    background: linear-gradient(140deg, #4b463c 0%, #33302a 55%, #221f1b 100%);
  }

  .trn-05:has(#trn-05-theme:checked) .trn-05__zoom--b {
    background: linear-gradient(140deg, #3d4642 0%, #2c3330 55%, #1e2321 100%);
  }
}

@media (prefers-color-scheme: dark) {
  .trn-05:has(#trn-05-theme:checked) {
    --page: #fbfaf7;
    --page: oklch(0.98 0.005 90);
    --ink: #14130f;
    --ink: oklch(0.19 0.008 80);
    --muted: #5f5c54;
    --muted: oklch(0.49 0.01 85);
    --rule: #ddd9d0;
    --rule: oklch(0.89 0.008 88);
    --wash: #ebe7de;
    --wash: oklch(0.93 0.01 88);
    --accent: #14130f;
    --zoom: 1.07;
    --font-display: "Iowan Old Style", "Palatino Linotype", Georgia, "Times New Roman", serif;
    background: var(--page);
  }

  .trn-05:has(#trn-05-theme:checked) .trn-05__ph {
    padding: 0 12px;
    font: 400 11px/1.4 system-ui, sans-serif;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: rgba(20, 19, 15, 0.55);
    text-align: center;
  }

  .trn-05:has(#trn-05-theme:checked) .trn-05__zoom--a {
    background: linear-gradient(140deg, #cfc6b5 0%, #a99e8b 55%, #7d7466 100%);
    transform-origin: 50% 32%;
  }

  .trn-05:has(#trn-05-theme:checked) .trn-05__zoom--b {
    background: linear-gradient(140deg, #c3ccc6 0%, #97a49d 55%, #6c7873 100%);
    transform-origin: 62% 40%;
  }

  .trn-05:has(#trn-05-theme:checked) .trn-05__sun {
    opacity: 1;
  }

  .trn-05:has(#trn-05-theme:checked) .trn-05__moon {
    opacity: 0.34;
  }
}
```
