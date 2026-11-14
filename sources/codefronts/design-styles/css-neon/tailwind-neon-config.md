---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/tailwind-neon-config/"
title: "Tailwind Neon Glow Utility Recipe"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "The three-layer stack expressed as a utility, in both the v3 @layer utilities form and the v4 @theme form, with the rendered result built in plain CSS so it…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Glow Utility Recipe
Source: https://codefronts.com/design-styles/css-neon/tailwind-neon-config/

The three-layer stack expressed as a utility, in both the v3 @layer utilities form and the v4 @theme form, with the rendered result built in plain CSS so it runs anywhere. Includes the part most recipes skip: why an arbitrary-value shadow is the wrong place for a glow, and how additive blending changes what the utility should contain.
## HTML
```html
<section class="nn-17" aria-labelledby="nn-17-heading">
  <div class="nn-17__stage">
    <div class="nn-17__theme">
      <input class="nn-17__tin" type="checkbox" id="nn-17-theme">
      <label class="nn-17__tlab" for="nn-17-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-17__head">
      <p class="nn-17__kicker">utility, not arbitrary value</p>
      <h2 class="nn-17__heading" id="nn-17-heading">One shadow token, three layers, every hue</h2>
      <p class="nn-17__sub">The rendered result is plain CSS so it runs here. The two blocks below are what you paste into a Tailwind project.</p>
    </header>

    <div class="nn-17__demo">
      <div class="nn-17__chip">Sync 4 repositories</div>
      <div class="nn-17__chip nn-17__chip--b">Open channel</div>
      <p class="nn-17__note">The two chips overlap their halos. With <span class="nn-17__code">mix-blend-screen</span> the overlap brightens instead of going dull.</p>
    </div>

    <div class="nn-17__blocks">
      <div class="nn-17__block">
        <p class="nn-17__blabel">v4 &mdash; @theme</p>
        <pre class="nn-17__pre"><code>@theme &#123;
  --color-glow: oklch(85% .15 195);
  --shadow-glow:
    0 0 6px --alpha(var(--color-glow) / 90%),
    0 0 18px --alpha(var(--color-glow) / 45%),
    0 0 48px --alpha(var(--color-glow) / 22%);
&#125;

&lt;span class="shadow-glow mix-blend-screen"&gt;&lt;/span&gt;</code></pre>
      </div>
      <div class="nn-17__block">
        <p class="nn-17__blabel">v3 &mdash; theme.extend</p>
        <pre class="nn-17__pre"><code>// tailwind.config.js
theme: &#123; extend: &#123; boxShadow: &#123;
  glow: [
    '0 0 6px rgba(34,211,238,.9)',
    '0 0 18px rgba(34,211,238,.45)',
    '0 0 48px rgba(34,211,238,.22)'
  ].join(', ')
&#125; &#125; &#125;</code></pre>
      </div>
    </div>

    <p class="nn-17__rule">Name the stack once. A glow split across three utilities, or pasted as an arbitrary value, loses the layer relationships that make it read as light.</p>
  </div>
</section>
```
## CSS
```css
.nn-17 {
  --nn-17-bad: #f4a4a4;
  --nn-17-warn: #f0c88a;
  --nn-17-spec-neon: #22d3ee;
}

@media (prefers-color-scheme: light) {
  .nn-17 {
    --nn-17-bad: #a12a20;
    --nn-17-warn: #78490a;
  }

  .nn-17:has(#nn-17-theme:checked) {
    --nn-17-bad: #f4a4a4;
    --nn-17-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-17:has(#nn-17-theme:checked) {
    --nn-17-bad: #a12a20;
    --nn-17-warn: #78490a;
  }
}

.nn-17[data-theme="light"] {
  --nn-17-bad: #a12a20;
  --nn-17-warn: #78490a;
}

.nn-17 {
  --nn-17-spec-ink: #eef3fa;
  --nn-17-spec-dim: #93a1b5;
}

.nn-17__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-17__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-17__tlab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 44px;
  padding: 0 .8rem;
  border: 1px solid currentColor;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: .7;
}

.nn-17__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-17__tlab:hover {
  opacity: 1;
}

.nn-17__tin:focus-visible + .nn-17__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-17:has(#nn-17-theme:checked) {
    --nn-17-bg: #0b0f16;
    --nn-17-panel: #111722;
    --nn-17-line: #202a3a;
    --nn-17-ink: #eef3fa;
    --nn-17-muted: #93a1b5;
    --nn-17-base: #22d3ee;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-17:has(#nn-17-theme:checked) {
    --nn-17-bg: #eaedf2;
    --nn-17-panel: #ffffff;
    --nn-17-line: #c7ccd6;
    --nn-17-ink: #101620;
    --nn-17-muted: #4b5566;
    --nn-17-base: #05627a;
  }
}

.nn-17 {
  --nn-17-hue: 195;
  --nn-17-bg: #0b0f16;
  --nn-17-panel: #111722;
  --nn-17-line: #202a3a;
  --nn-17-ink: #eef3fa;
  --nn-17-muted: #93a1b5;
  --nn-17-base: #22d3ee;
  --nn-17-core: rgba(34, 211, 238, .9);
  --nn-17-halo: rgba(34, 211, 238, .45);
  --nn-17-bloom: rgba(34, 211, 238, .22);
  --nn-17-font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-17-bg);
  color: var(--nn-17-ink);
  font-family: system-ui, sans-serif;
}

.nn-17 *,
.nn-17 *::before,
.nn-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-17 {
    --nn-17-bg: oklch(16% 0.018 255);
    --nn-17-panel: oklch(20% 0.022 255);
    --nn-17-line: oklch(30% 0.026 255);
    --nn-17-ink: oklch(96% 0.012 255);
    --nn-17-muted: oklch(73% 0.022 255);
    --nn-17-base: oklch(85% 0.15 var(--nn-17-hue));
  }
}

@supports (color: color-mix(in oklab, red, blue)) {
  .nn-17 {
    --nn-17-core: color-mix(in oklab, var(--nn-17-base) 90%, transparent);
    --nn-17-halo: color-mix(in oklab, var(--nn-17-base) 45%, transparent);
    --nn-17-bloom: color-mix(in oklab, var(--nn-17-base) 22%, transparent);
  }
}

@media (prefers-color-scheme: light) {
  .nn-17 {
    --nn-17-bg: #eaedf2;
    --nn-17-panel: #ffffff;
    --nn-17-line: #c7ccd6;
    --nn-17-ink: #101620;
    --nn-17-muted: #4b5566;
    --nn-17-base: #05627a;
  }
}

.nn-17[data-theme="light"] {
  --nn-17-bg: #eaedf2;
  --nn-17-panel: #ffffff;
  --nn-17-line: #c7ccd6;
  --nn-17-ink: #101620;
  --nn-17-muted: #4b5566;
  --nn-17-base: #05627a;
}

.nn-17[data-theme="dark"] {
  --nn-17-bad: #f4a4a4;
  --nn-17-warn: #f0c88a;
  --nn-17-bg: #0b0f16;
  --nn-17-panel: #111722;
  --nn-17-line: #202a3a;
  --nn-17-ink: #eef3fa;
  --nn-17-muted: #93a1b5;
  --nn-17-base: #22d3ee;
}

.nn-17__stage {
  max-width: 64rem;
  margin: 0 auto;
  padding: clamp(1rem, 3vw, 1.35rem) clamp(.75rem, 3vw, 1.35rem) clamp(1.5rem, 4vw, 1.85rem);
  display: grid;
  gap: clamp(.85rem, 2.5vw, 1.1rem);
}

.nn-17__kicker {
  margin: 0 0 .3rem;
  font-family: var(--nn-17-font-display);
  font-size: .68rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--nn-17-base);
}

.nn-17__heading {
  margin: 0;
  font-family: var(--nn-17-font-display);
  font-size: clamp(1.2rem, 4.2vw, 1.7rem);
  font-weight: 500;
  letter-spacing: -.01em;
  text-wrap: balance;
}

.nn-17__sub {
  margin: .4rem 0 0;
  max-width: 40rem;
  font-size: .85rem;
  line-height: 1.55;
  color: var(--nn-17-muted);
  text-wrap: pretty;
}

.nn-17__demo {
  position: relative;
  isolation: isolate;
  display: flex;
  align-items: center;
  gap: 0;
  flex-wrap: wrap;
  padding: clamp(1.25rem, 5vw, 2rem) clamp(1rem, 4vw, 1.5rem);
  border: 1px solid var(--nn-17-line);
  border-radius: .25rem;
  background: var(--nn-17-panel);
}

.nn-17__chip {
  position: relative;
  padding: .55rem .9rem;
  border: 1px solid var(--nn-17-spec-neon);
  border-radius: .2rem;
  background: #0e141d;
  color: var(--nn-17-spec-ink);
  font-family: var(--nn-17-font-display);
  font-size: .78rem;
  mix-blend-mode: screen;
  box-shadow: 0 0 .38rem var(--nn-17-core), 0 0 1.1rem var(--nn-17-halo), 0 0 clamp(1.75rem, 8vw, 3rem) var(--nn-17-bloom);
}

.nn-17__chip--b {
  margin-left: -1.25rem;
}

.nn-17__note {
  margin: .75rem 0 0;
  flex: 1 1 100%;
  font-size: .76rem;
  line-height: 1.5;
  color: var(--nn-17-muted);
  min-inline-size: 0;
}

.nn-17__code {
  font-family: var(--nn-17-font-display);
  color: var(--nn-17-base);
}

.nn-17__blocks {
  display: grid;
  gap: .75rem;
  grid-template-columns: 1fr;
}

@media (min-width: 52rem) {
  .nn-17__blocks {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-17__block {
  display: grid;
  gap: .45rem;
  padding: .8rem .9rem;
  border: 1px solid var(--nn-17-line);
  border-radius: .25rem;
  background: var(--nn-17-panel);
  min-inline-size: 0;
}

.nn-17__blabel {
  margin: 0;
  font-family: var(--nn-17-font-display);
  font-size: .66rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--nn-17-muted);
}

.nn-17__pre {
  margin: 0;
  overflow-x: auto;
  font-family: var(--nn-17-font-display);
  font-size: .7rem;
  line-height: 1.65;
  color: var(--nn-17-base);
}

.nn-17__rule {
  margin: 0;
  padding: .85rem 1rem;
  border: 1px solid var(--nn-17-line);
  border-left: 2px solid var(--nn-17-base);
  border-radius: .2rem;
  font-size: .82rem;
  line-height: 1.6;
  color: var(--nn-17-ink);
  text-wrap: pretty;
}
```
