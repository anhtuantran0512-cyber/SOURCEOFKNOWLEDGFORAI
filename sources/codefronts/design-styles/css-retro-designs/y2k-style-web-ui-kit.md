---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/y2k-style-web-ui-kit/"
title: "Y2K Aqua Gloss Interface Kit"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "The early-2000s gel look, built correctly: glossy pill buttons, translucent panels over a pinstriped ground, and a candy-stripe progress bar that flows."
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Y2K Aqua Gloss Interface Kit
Source: https://codefronts.com/design-styles/css-retro-designs/y2k-style-web-ui-kit/

The early-2000s gel look, built correctly: glossy pill buttons, translucent panels over a pinstriped ground, and a candy-stripe progress bar that flows. The gloss is the interesting part &mdash; it is a stack of four separate highlights, not one gradient, which is why most attempts at this style look like a coloured button with a shine on it.
## HTML
```html
<section class="rt-18" aria-labelledby="rt-18-title">
  <h2 class="rt-18__sr" id="rt-18-title">Y2K aqua gloss interface kit</h2>

  <div class="rt-18__theme">
    <input class="rt-18__theme-input" type="checkbox" id="rt-18-theme">
    <label class="rt-18__theme-label" for="rt-18-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-18__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-18__stage">
    <header class="rt-18__head">
      <p class="rt-18__kicker">Gel surfaces &middot; four light events per control</p>
      <h3 class="rt-18__h">Aqua Kit</h3>
    </header>

    <div class="rt-18__grid">
      <article class="rt-18__panel" aria-labelledby="rt-18-p1">
        <h4 class="rt-18__panel-h" id="rt-18-p1">Pill buttons</h4>
        <div class="rt-18__row">
          <button class="rt-18__pill" type="button">Continue</button>
          <button class="rt-18__pill rt-18__pill--g" type="button">Install</button>
          <button class="rt-18__pill rt-18__pill--r" type="button">Cancel</button>
        </div>
        <div class="rt-18__row">
          <button class="rt-18__orb" type="button" aria-label="Play"><span class="rt-18__orb-g rt-18__orb-g--play" aria-hidden="true"></span></button>
          <button class="rt-18__orb rt-18__orb--g" type="button" aria-label="Stop"><span class="rt-18__orb-g rt-18__orb-g--stop" aria-hidden="true"></span></button>
          <button class="rt-18__orb rt-18__orb--r" type="button" aria-label="Eject"><span class="rt-18__orb-g rt-18__orb-g--eject" aria-hidden="true"></span></button>
        </div>
        <p class="rt-18__note">Specular cap, bounce light, rim light, contact shadow. Four layers, one surface.</p>
      </article>

      <article class="rt-18__panel rt-18__panel--frost" aria-labelledby="rt-18-p2">
        <h4 class="rt-18__panel-h" id="rt-18-p2">Progress</h4>
        <div class="rt-18__prog" role="progressbar" aria-valuenow="68" aria-valuemin="0" aria-valuemax="100" aria-label="Installing, 68 percent">
          <span class="rt-18__prog-f"></span>
        </div>
        <p class="rt-18__prog-l">Installing components &mdash; 68%</p>
        <div class="rt-18__prog rt-18__prog--sm" role="progressbar" aria-valuenow="24" aria-valuemin="0" aria-valuemax="100" aria-label="Downloading, 24 percent">
          <span class="rt-18__prog-f" style="--rt-18-v: 24%"></span>
        </div>
        <p class="rt-18__prog-l">Downloading &mdash; 24%</p>
      </article>

      <article class="rt-18__panel" aria-labelledby="rt-18-p3">
        <h4 class="rt-18__panel-h" id="rt-18-p3">Toggles and tabs</h4>
        <div class="rt-18__row">
          <span class="rt-18__toggle">
            <input class="rt-18__toggle-cb" type="checkbox" id="rt-18-t1" checked>
            <label class="rt-18__toggle-lb" for="rt-18-t1"><span class="rt-18__knob" aria-hidden="true"></span>Sound</label>
          </span>
          <span class="rt-18__toggle">
            <input class="rt-18__toggle-cb" type="checkbox" id="rt-18-t2">
            <label class="rt-18__toggle-lb" for="rt-18-t2"><span class="rt-18__knob" aria-hidden="true"></span>Shuffle</label>
          </span>
        </div>
        <div class="rt-18__tabs" role="tablist" aria-label="Library view">
          <button class="rt-18__tab rt-18__tab--on" type="button" role="tab" aria-selected="true">Albums</button>
          <button class="rt-18__tab" type="button" role="tab" aria-selected="false">Artists</button>
          <button class="rt-18__tab" type="button" role="tab" aria-selected="false">Genres</button>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-18 {
  --rt-18-hue: 208;
  --rt-18-gel: #2f97e8;
  --rt-18-gel-d: #0b5ba6;
  --rt-18-gel-l: #a9defc;
  --rt-18-green: #4fb62f;
  --rt-18-green-d: #216d10;
  --rt-18-red: #e8543a;
  --rt-18-red-d: #a3260f;
  --rt-18-sans: ui-rounded, "Lucida Grande", "Segoe UI", system-ui, -apple-system, sans-serif;
  --rt-18-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --rt-18-bg: #eef3f8;
  --rt-18-bg: oklch(96% 0.011 240);
  --rt-18-stripe: #e3ebf3;
  --rt-18-surface: #ffffff;
  --rt-18-ink: #14202b;
  --rt-18-ink: oklch(21% 0.02 245);
  --rt-18-ink-2: #4a5a68;
  --rt-18-ink-2: oklch(45% 0.024 245);
  --rt-18-line: #b3c3d1;
  --rt-18-line: oklch(79% 0.021 245);
  --rt-18-acc: #0a5ba8;
  --rt-18-acc: oklch(44% 0.16 245);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--rt-18-bg);
  background-image: repeating-linear-gradient(180deg, var(--rt-18-stripe) 0 1px, rgba(0,0,0,0) 1px 4px);
  color: var(--rt-18-ink);
  font-family: var(--rt-18-sans);
  -webkit-text-size-adjust: 100%;
}

.rt-18 *,
.rt-18 *::before,
.rt-18 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-18 {
    --rt-18-bg: #0e1620;
    --rt-18-bg: oklch(19% 0.018 245);
    --rt-18-stripe: #16212e;
    --rt-18-surface: #1a2634;
    --rt-18-ink: #eef4fa;
    --rt-18-ink: oklch(96% 0.008 245);
    --rt-18-ink-2: #a5b4c2;
    --rt-18-ink-2: oklch(75% 0.018 245);
    --rt-18-line: #38495a;
    --rt-18-line: oklch(38% 0.024 245);
    --rt-18-acc: #7ec2ff;
    --rt-18-acc: oklch(80% 0.12 245);
  }
}

.rt-18[data-theme="dark"],
.rt-18:has(.rt-18__theme-input:checked) {
  --rt-18-bg: #0e1620;
  --rt-18-bg: oklch(19% 0.018 245);
  --rt-18-stripe: #16212e;
  --rt-18-surface: #1a2634;
  --rt-18-ink: #eef4fa;
  --rt-18-ink: oklch(96% 0.008 245);
  --rt-18-ink-2: #a5b4c2;
  --rt-18-ink-2: oklch(75% 0.018 245);
  --rt-18-line: #38495a;
  --rt-18-line: oklch(38% 0.024 245);
  --rt-18-acc: #7ec2ff;
  --rt-18-acc: oklch(80% 0.12 245);
}

@media (prefers-color-scheme: light) {
  .rt-18:has(.rt-18__theme-input:checked) {
    --rt-18-bg: #0e1620;
    --rt-18-bg: oklch(19% 0.018 245);
    --rt-18-stripe: #16212e;
    --rt-18-surface: #1a2634;
    --rt-18-ink: #eef4fa;
    --rt-18-ink: oklch(96% 0.008 245);
    --rt-18-ink-2: #a5b4c2;
    --rt-18-ink-2: oklch(75% 0.018 245);
    --rt-18-line: #38495a;
    --rt-18-line: oklch(38% 0.024 245);
    --rt-18-acc: #7ec2ff;
    --rt-18-acc: oklch(80% 0.12 245);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-18:has(.rt-18__theme-input:checked) {
    --rt-18-bg: #eef3f8;
    --rt-18-bg: oklch(96% 0.011 240);
    --rt-18-stripe: #e3ebf3;
    --rt-18-surface: #ffffff;
    --rt-18-ink: #14202b;
    --rt-18-ink: oklch(21% 0.02 245);
    --rt-18-ink-2: #4a5a68;
    --rt-18-ink-2: oklch(45% 0.024 245);
    --rt-18-line: #b3c3d1;
    --rt-18-line: oklch(79% 0.021 245);
    --rt-18-acc: #0a5ba8;
    --rt-18-acc: oklch(44% 0.16 245);
  }
}

.rt-18__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-18__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-18__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-18__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  border-radius: 50%;
  color: #ffffff;
  background: linear-gradient(180deg, var(--rt-18-gel-l) 0%, var(--rt-18-gel) 48%, var(--rt-18-gel-d) 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), inset 0 -2px 4px rgba(0,0,0,0.25), 0 2px 5px rgba(10,50,90,0.35);
}

.rt-18__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-18__theme-input:focus-visible + .rt-18__theme-label {
  outline: 2px solid var(--rt-18-acc);
  outline-offset: 3px;
}

.rt-18__stage {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: clamp(3.75rem, 3rem + 3vw, 5rem) clamp(0.85rem, 0.5rem + 2vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
}

.rt-18__head {
  min-inline-size: 0;
  display: grid;
  gap: 0.3rem;
}

.rt-18__kicker {
  margin: 0;
  font-family: var(--rt-18-mono);
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--rt-18-ink-2);
}

.rt-18__h {
  margin: 0;
  font-size: clamp(1.8rem, 1rem + 5vw, 3.4rem);
  line-height: 1;
  font-weight: 700;
  letter-spacing: -0.03em;
  min-inline-size: 0;
  background-image: linear-gradient(180deg, #6cc4f7 0%, #1a76c8 52%, #0a4f92 100%);
  color: var(--rt-18-acc);
}

@supports ((-webkit-background-clip: text) or (background-clip: text)) {
  .rt-18__h {
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

.rt-18__grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.1rem;
  align-items: start;
}

.rt-18__panel {
  min-inline-size: 0;
  border-radius: 12px;
  padding: clamp(0.9rem, 0.7rem + 1vw, 1.3rem);
  background: var(--rt-18-surface);
  border: 1px solid var(--rt-18-line);
  display: grid;
  gap: 0.9rem;
  align-content: start;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.85), 0 10px 22px -14px rgba(12, 48, 84, 0.55);
}

@supports ((-webkit-backdrop-filter: blur(8px)) or (backdrop-filter: blur(8px))) {
  .rt-18__panel--frost {
    background: color-mix(in srgb, var(--rt-18-surface) 62%, transparent);
    -webkit-backdrop-filter: blur(10px) saturate(1.3);
    backdrop-filter: blur(10px) saturate(1.3);
  }
}

.rt-18__panel-h {
  margin: 0;
  font-size: 0.75rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--rt-18-ink-2);
}

.rt-18__row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  align-items: center;
  min-inline-size: 0;
}

.rt-18__pill {
  position: relative;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 0.6rem 1.4rem;
  border: 0;
  cursor: pointer;
  border-radius: 999px;
  overflow: hidden;
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 30, 60, 0.55);
  background: linear-gradient(180deg, var(--rt-18-gel) 0%, var(--rt-18-gel-d) 100%);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.45), inset 0 -6px 10px -4px rgba(255,255,255,0.4), 0 1px 0 rgba(255,255,255,0.7), 0 4px 10px -3px rgba(8, 44, 82, 0.55);
}

.rt-18__pill::before {
  content: "";
  position: absolute;
  inset-block-start: 2px;
  inset-inline: 5px;
  block-size: 42%;
  border-radius: 999px 999px 60% 60% / 999px 999px 100% 100%;
  background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(255,255,255,0.16));
  pointer-events: none;
}

.rt-18__pill--g {
  background: linear-gradient(180deg, var(--rt-18-green) 0%, var(--rt-18-green-d) 100%);
}

.rt-18__pill--r {
  background: linear-gradient(180deg, var(--rt-18-red) 0%, var(--rt-18-red-d) 100%);
}

.rt-18__pill:active {
  box-shadow: inset 0 3px 7px rgba(0, 24, 48, 0.5), inset 0 0 0 1px rgba(255,255,255,0.3);
}

.rt-18__pill:focus-visible {
  outline: 2px solid var(--rt-18-acc);
  outline-offset: 3px;
}

.rt-18__orb {
  position: relative;
  inline-size: 52px;
  block-size: 52px;
  border: 0;
  cursor: pointer;
  border-radius: 50%;
  display: grid;
  place-items: center;
  overflow: hidden;
  background: radial-gradient(circle at 50% 120%, rgba(255,255,255,0.5), rgba(255,255,255,0) 55%), linear-gradient(180deg, var(--rt-18-gel) 0%, var(--rt-18-gel-d) 100%);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.5), 0 1px 0 rgba(255,255,255,0.75), 0 5px 12px -4px rgba(8,44,82,0.6);
}

.rt-18__orb::before {
  content: "";
  position: absolute;
  inset-block-start: 3px;
  inset-inline: 8px;
  block-size: 40%;
  border-radius: 50%;
  background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(255,255,255,0.1));
  pointer-events: none;
}

.rt-18__orb--g {
  background: radial-gradient(circle at 50% 120%, rgba(255,255,255,0.5), rgba(255,255,255,0) 55%), linear-gradient(180deg, var(--rt-18-green), var(--rt-18-green-d));
}

.rt-18__orb--r {
  background: radial-gradient(circle at 50% 120%, rgba(255,255,255,0.5), rgba(255,255,255,0) 55%), linear-gradient(180deg, var(--rt-18-red), var(--rt-18-red-d));
}

.rt-18__orb:active {
  box-shadow: inset 0 3px 8px rgba(0,24,48,0.55);
}

.rt-18__orb:focus-visible {
  outline: 2px solid var(--rt-18-acc);
  outline-offset: 3px;
}

.rt-18__orb-g {
  position: relative;
  z-index: 1;
  inline-size: 14px;
  block-size: 14px;
  background: #ffffff;
}

.rt-18__orb-g--play {
  clip-path: polygon(6% 0, 100% 50%, 6% 100%);
}

.rt-18__orb-g--stop {
  clip-path: inset(0);
}

.rt-18__orb-g--eject {
  clip-path: polygon(50% 0, 100% 58%, 0 58%, 0 76%, 100% 76%, 100% 58%);
}

.rt-18__prog {
  block-size: 22px;
  border-radius: 999px;
  overflow: hidden;
  min-inline-size: 0;
  background: linear-gradient(180deg, #cfd9e2, #eef3f8);
  box-shadow: inset 0 2px 4px rgba(10, 40, 70, 0.35), 0 1px 0 rgba(255,255,255,0.8);
}

.rt-18__prog--sm {
  block-size: 16px;
}

.rt-18__prog-f {
  --rt-18-v: 68%;
  display: block;
  block-size: 100%;
  inline-size: var(--rt-18-v);
  border-radius: 999px;
  background: repeating-linear-gradient(45deg, rgba(255,255,255,0.42) 0 10px, rgba(255,255,255,0) 10px 20px), linear-gradient(180deg, var(--rt-18-gel-l) 0%, var(--rt-18-gel) 45%, var(--rt-18-gel-d) 100%);
  background-size: 28px 28px, auto;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.85);
  animation: rt-18-flow 900ms linear infinite;
}

@keyframes rt-18-flow {
  to {
    background-position: 28px 0, 0 0;
  }
}

.rt-18__prog-l {
  margin: 0;
  font-size: 0.8rem;
  color: var(--rt-18-ink-2);
  min-inline-size: 0;
}

.rt-18__toggle {
  position: relative;
  display: inline-block;
}

.rt-18__toggle-cb {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 44px;
  block-size: 44px;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.rt-18__toggle-lb {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  min-block-size: 44px;
  cursor: pointer;
  font-size: 0.85rem;
  color: var(--rt-18-ink);
  padding-inline-end: 0.4rem;
}

.rt-18__knob {
  inline-size: 52px;
  block-size: 28px;
  flex: none;
  border-radius: 999px;
  position: relative;
  background: linear-gradient(180deg, #c3cfda, #e9eff5);
  box-shadow: inset 0 2px 4px rgba(10,40,70,0.35);
  transition: background 140ms ease;
}

.rt-18__knob::after {
  content: "";
  position: absolute;
  inset-block: 2px;
  inset-inline-start: 2px;
  inline-size: 24px;
  border-radius: 50%;
  background: linear-gradient(180deg, #ffffff, #cfd9e2);
  box-shadow: 0 1px 3px rgba(8,44,82,0.5);
  transition: inset-inline-start 140ms ease;
}

.rt-18__toggle-cb:checked + .rt-18__toggle-lb .rt-18__knob {
  background: linear-gradient(180deg, var(--rt-18-gel), var(--rt-18-gel-d));
}

.rt-18__toggle-cb:checked + .rt-18__toggle-lb .rt-18__knob::after {
  inset-inline-start: 26px;
}

.rt-18__toggle-cb:focus-visible + .rt-18__toggle-lb .rt-18__knob {
  outline: 2px solid var(--rt-18-acc);
  outline-offset: 3px;
}

.rt-18__tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  min-inline-size: 0;
}

.rt-18__tab {
  min-block-size: 44px;
  min-inline-size: 44px;
  flex: 1 1 auto;
  padding: 0.5rem 0.9rem;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: 0.82rem;
  color: var(--rt-18-ink);
  border-radius: 8px 8px 0 0;
  background: linear-gradient(180deg, #f6f9fc, #d5dfe8);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), inset 0 -1px 0 rgba(10,40,70,0.18);
}

.rt-18__tab--on {
  color: #ffffff;
  background: linear-gradient(180deg, var(--rt-18-gel), var(--rt-18-gel-d));
  text-shadow: 0 -1px 0 rgba(0,30,60,0.5);
}

.rt-18__tab:focus-visible {
  outline: 2px solid var(--rt-18-acc);
  outline-offset: -4px;
}

.rt-18__note {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.55;
  color: var(--rt-18-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .rt-18__prog-f {
    animation: none;
  }

  .rt-18__knob,
    .rt-18__knob::after {
    transition: none;
  }
}

@media (min-width: 50rem) {
  .rt-18__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 72rem) {
  .rt-18__grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
```
