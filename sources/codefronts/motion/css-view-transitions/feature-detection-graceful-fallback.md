---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/feature-detection-graceful-fallback/"
title: "Feature Detection Graceful Fallback"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "Firefox has not shipped this API."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Detection Graceful Fallback
Source: https://codefronts.com/motion/css-view-transitions/feature-detection-graceful-fallback/

Firefox has not shipped this API. The one-line guard — if (!document.startViewTransition) { update(); return; } — is what separates a progressive enhancement from a broken page, and it has to run before any other transition code. This is the complete wrapper every other demo in the collection uses, with the un-transitioned path shown as the correct path rather than a degraded one.
## HTML
```html
<section class="vtr-17" aria-labelledby="vtr-17-heading">
  <fieldset class="vtr-17__theme">
    <legend class="vtr-17__themelegend">Theme</legend>
    <input class="vtr-17__themeinput" type="radio" name="vtr-17-theme" id="vtr-17-theme-auto" checked>
    <label class="vtr-17__themeopt" for="vtr-17-theme-auto">Auto</label>
    <input class="vtr-17__themeinput" type="radio" name="vtr-17-theme" id="vtr-17-theme-light">
    <label class="vtr-17__themeopt" for="vtr-17-theme-light">Light</label>
    <input class="vtr-17__themeinput" type="radio" name="vtr-17-theme" id="vtr-17-theme-dark">
    <label class="vtr-17__themeopt" for="vtr-17-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-17__stage">
    <header class="vtr-17__head">
      <p class="vtr-17__kicker">progressive enhancement</p>
      <h2 class="vtr-17__heading" id="vtr-17-heading">The guard clause, in full</h2>
    </header>

    <pre class="vtr-17__code"><code><span class="vtr-17__c">// the wrapper every demo in this collection uses</span>
<span class="vtr-17__k">let</span> running = <span class="vtr-17__v">false</span>;

<span class="vtr-17__k">async function</span> <span class="vtr-17__f">transition</span>(update, types) {
  <span class="vtr-17__c">// 1 · no API, or the user asked for less motion</span>
  <span class="vtr-17__k">if</span> (!document.startViewTransition ||
      matchMedia(<span class="vtr-17__s">'(prefers-reduced-motion: reduce)'</span>).matches) {
    update();
    <span class="vtr-17__k">return</span> <span class="vtr-17__v">null</span>;
  }
  <span class="vtr-17__c">// 2 · never stack two transitions</span>
  <span class="vtr-17__k">if</span> (running) <span class="vtr-17__k">return</span> <span class="vtr-17__v">null</span>;
  running = <span class="vtr-17__v">true</span>;
  <span class="vtr-17__k">const</span> t = document.<span class="vtr-17__f">startViewTransition</span>(
    types ? { update, types } : update
  );
  <span class="vtr-17__k">try</span> { <span class="vtr-17__k">await</span> t.finished; } <span class="vtr-17__k">finally</span> { running = <span class="vtr-17__v">false</span>; }
  <span class="vtr-17__k">return</span> t;
}</code></pre>

    <div class="vtr-17__run">
      <button class="vtr-17__btn" type="button" id="vtr-17-run">run transition(update)</button>
      <div class="vtr-17__out" id="vtr-17-panel">
        <p class="vtr-17__line"><span class="vtr-17__prompt">&gt;</span><span id="vtr-17-branch">awaiting call</span></p>
        <p class="vtr-17__line vtr-17__line--dim">api: <span id="vtr-17-api">checking</span> · reduced-motion: <span id="vtr-17-rm">checking</span></p>
        <p class="vtr-17__state" id="vtr-17-state">build 4118 · queued</p>
      </div>
    </div>

    <ul class="vtr-17__notes">
      <li>Firefox has not shipped the API. The DOM update still applies there, instantly.</li>
      <li>Detect the feature, never the browser — the check stays correct when support changes.</li>
      <li>The guard runs before any name assignment, so nothing is left attached.</li>
    </ul>
  </div>
</section>
```
## CSS
```css
.vtr-17 {
  --bg: #05080a;
  --surface: #0a1013;
  --line: #16241f;
  --ink: #d8f5e3;
  --muted: #5c8a72;
  --accent: #34e07f;
  --accent-soft: #0d2418;
  --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  background-image: repeating-linear-gradient(to bottom, rgba(52, 224, 127, 0.045) 0 1px, transparent 1px 3px);
  color: var(--ink);
  font-family: var(--font-display);
  color-scheme: dark light;
}

.vtr-17 *,
.vtr-17 *::before,
.vtr-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-17 {
    --surface: oklch(16% 0.02 160);
    --line: oklch(26% 0.035 160);
    --ink: oklch(93% 0.06 160);
    --muted: oklch(62% 0.07 160);
    --accent: oklch(82% 0.19 150);
    --accent-soft: oklch(24% 0.07 155);
  }
}

@media (prefers-color-scheme: light) {
  .vtr-17 {
    --bg: #f2f7f3;
    --surface: #ffffff;
    --line: #cfe3d6;
    --ink: #0a1f14;
    --muted: #4a6b58;
    --accent: #0f7a43;
    --accent-soft: #dff3e6;
    background-image: repeating-linear-gradient(to bottom, rgba(15, 122, 67, 0.04) 0 1px, transparent 1px 3px);
  }
}

.vtr-17[data-theme="light"] {
  --bg: #f2f7f3;
  --surface: #ffffff;
  --line: #cfe3d6;
  --ink: #0a1f14;
  --muted: #4a6b58;
  --accent: #0f7a43;
  --accent-soft: #dff3e6;
}

.vtr-17[data-theme="dark"] {
  --bg: #05080a;
  --surface: #0a1013;
  --line: #16241f;
  --ink: #d8f5e3;
  --muted: #5c8a72;
  --accent: #34e07f;
  --accent-soft: #0d2418;
}

.vtr-17__stage {
  max-width: 52rem;
  margin: 0 auto;
  padding: clamp(1rem, 3.5vw, 2rem) clamp(0.75rem, 3.5vw, 1.75rem);
  display: grid;
  gap: 0.75rem;
}

.vtr-17__kicker {
  margin: 0 0 0.2rem;
  font-size: 0.68rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-17__heading {
  margin: 0;
  font-size: clamp(1.1rem, 3.6vw, 1.5rem);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.vtr-17__code {
  margin: 0;
  padding: 0.75rem 0.85rem;
  overflow-x: auto;
  border: 1px solid var(--line);
  border-radius: 0.25rem;
  background: var(--surface);
  font-size: 0.7rem;
  line-height: 1.55;
}

.vtr-17__c {
  color: var(--muted);
}

.vtr-17__k {
  color: var(--accent);
}

.vtr-17__f {
  color: var(--ink);
  font-weight: 700;
}

.vtr-17__s {
  color: #9be7bf;
}

.vtr-17__v {
  color: #7ee8ae;
}

.vtr-17__run {
  display: grid;
  gap: 0.5rem;
}

.vtr-17__btn {
  justify-self: start;
  min-height: 44px;
  padding: 0 0.9rem;
  border: 1px solid var(--accent);
  border-radius: 0.2rem;
  background: var(--accent-soft);
  color: var(--accent);
  font-family: inherit;
  font-size: 0.76rem;
  cursor: pointer;
}

.vtr-17__btn:hover {
  background: var(--accent);
  color: var(--bg);
}

.vtr-17__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.vtr-17__out {
  padding: 0.6rem 0.7rem;
  border: 1px solid var(--line);
  border-radius: 0.25rem;
  background: var(--surface);
  display: grid;
  gap: 0.3rem;
  min-inline-size: 0;
}

.vtr-17__line {
  margin: 0;
  font-size: 0.72rem;
  word-break: break-word;
}

.vtr-17__line--dim {
  color: var(--muted);
  font-size: 0.68rem;
}

.vtr-17__prompt {
  color: var(--accent);
  margin-right: 0.4rem;
}

.vtr-17__state {
  margin: 0;
  padding: 0.5rem 0.6rem;
  border-left: 2px solid var(--accent);
  background: var(--accent-soft);
  font-size: 0.8rem;
  view-transition-name: vtr-17-state;
}

.vtr-17__notes {
  margin: 0;
  padding-left: 1.1rem;
  display: grid;
  gap: 0.3rem;
  font-size: 0.7rem;
  line-height: 1.5;
  color: var(--muted);
}

::view-transition-group(vtr-17-state) {
  animation-duration: 300ms;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-17-state) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-17 {
  position: relative;
}

.vtr-17__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.vtr-17__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-17__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-17__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.vtr-17__themeopt:hover {
  opacity: 0.85;
}

.vtr-17__themeinput:checked + .vtr-17__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-17__themeinput:focus-visible + .vtr-17__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-17:has(#vtr-17-theme-light:checked) {
  --bg: #f2f7f3;
  --surface: #ffffff;
  --line: #cfe3d6;
  --ink: #0a1f14;
  --muted: #4a6b58;
  --accent: #0f7a43;
  --accent-soft: #dff3e6;
}

.vtr-17:has(#vtr-17-theme-dark:checked) {
  --bg: #05080a;
  --surface: #0a1013;
  --line: #16241f;
  --ink: #d8f5e3;
  --muted: #5c8a72;
  --accent: #34e07f;
  --accent-soft: #0d2418;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-17');
  if (!root || root.dataset.vtr17) return;
  root.dataset.vtr17 = 'on';
  const state = root.querySelector('#vtr-17-state');
  const branch = root.querySelector('#vtr-17-branch');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const supported = typeof document.startViewTransition === 'function';
  root.querySelector('#vtr-17-api').textContent = supported ? 'available' : 'undefined';
  root.querySelector('#vtr-17-rm').textContent = reduce.matches ? 'reduce' : 'no-preference';
  const builds = [['build 4118 · queued', 'build 4118 · running on orbit-2'], ['build 4118 · running on orbit-2', 'build 4118 · passed in 2m 14s'], ['build 4118 · passed in 2m 14s', 'build 4118 · queued']];
  let i = 0, running = false;
  const update = () => { state.textContent = builds[i][1]; i = (i + 1) % builds.length; };
  root.querySelector('#vtr-17-run').addEventListener('click', async () => {
    if (!supported || reduce.matches) { update(); branch.textContent = 'guard hit · updated instantly'; return; }
    if (running) { branch.textContent = 'in flight · call ignored'; return; }
    running = true; branch.textContent = 'transition running';
    try { await document.startViewTransition(update).finished; branch.textContent = 'transition finished'; }
    finally { running = false; }
  });
})();
```
