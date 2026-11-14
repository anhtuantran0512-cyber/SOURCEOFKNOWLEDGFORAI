---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/letter-spacing-expansion-tracking-kerning/"
title: "Letter Spacing Expansion (Tracking / Kerning)"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "The fashion-magazine exhale: an uppercase masthead whose tracking breathes from .14em to .46em on hover, pulling air between the capitals. The bug every…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Letter Spacing Expansion (Tracking / Kerning)
Source: https://codefronts.com/motion/css-text-hover-effects/letter-spacing-expansion-tracking-kerning/

The fashion-magazine exhale: an uppercase masthead whose tracking breathes from .14em to .46em on hover, pulling air between the capitals. The bug every implementation ships — letter-spacing adds a phantom space AFTER the last letter, so 'centered' text drifts left as it expands — is fixed here with the one-line compensation (margin-right equal to minus the current spacing) transitioned in lockstep. Nav links do the restrained version, and the section number does the inverse: it TIGHTENS on hover, which reads as focus.
## HTML
```html
<section class="cth-15" aria-label="Letter spacing expansion demo">
  <div class="cth-15__stage">
    <div class="cth-15__scene">
      <p class="cth-15__no"><a href="#cth15-top" id="cth15-top">N&deg; 08</a></p>
      <h1 class="cth-15__masthead">
        <a class="cth-15__breathe" href="#cth15-top">MAISON</a>
        <a class="cth-15__breathe cth-15__breathe--b" href="#cth15-top">VERRE</a>
      </h1>
      <p class="cth-15__dek">The glass issue &mdash; transparency as a material, a metaphor, and a marketing problem.</p>
      <nav class="cth-15__nav" aria-label="Sections">
        <a href="#cth15-top">Essays</a><a href="#cth15-top">Objects</a><a href="#cth15-top">Ateliers</a><a href="#cth15-top">Archive</a>
      </nav>
      <p class="cth-15__hint">Hover the masthead &mdash; it expands around a stable center: <code>margin-right</code> mirrors <code>letter-spacing</code> to swallow the phantom trailing space. The issue number tightens instead.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-15,
.cth-15 *,
.cth-15 *::before,
.cth-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-15 {
  --bg: oklch(0.97 0.003 90);
  --ink: oklch(0.17 0.005 90);
  --mut: oklch(0.5 0.008 90);
  --line: oklch(0.88 0.005 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-15__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth15/inline-size;
}

.cth-15__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(16px,3cqi,26px);
}

.cth-15__no a {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  letter-spacing: .34em;
  margin-right: -.34em;
  color: var(--mut);
  text-decoration: none;
  transition: letter-spacing .5s cubic-bezier(.25,.8,.25,1),margin-right .5s cubic-bezier(.25,.8,.25,1),color .4s;
}

.cth-15__no a:hover,
.cth-15__no a:focus-visible {
  letter-spacing: .12em;
  margin-right: -.12em;
  color: var(--ink);
}

.cth-15__no a:focus-visible {
  outline: 1.5px solid var(--ink);
  outline-offset: 6px;
}

.cth-15__masthead {
  display: flex;
  flex-direction: column;
  line-height: 1.02;
}

.cth-15__breathe {
  display: block;
  font-size: clamp(50px,11.5cqi,116px);
  font-weight: 275;
  letter-spacing: .14em;
  margin-right: -.14em;
  color: inherit;
  text-decoration: none;
  transition: letter-spacing .7s cubic-bezier(.25,.8,.25,1),margin-right .7s cubic-bezier(.25,.8,.25,1),font-weight .7s ease;
}

.cth-15__breathe--b {
  font-weight: 600;
}

.cth-15__breathe:hover,
.cth-15__breathe:focus-visible {
  letter-spacing: .46em;
  margin-right: -.46em;
  font-weight: 340;
}

.cth-15__breathe--b:hover,
.cth-15__breathe--b:focus-visible {
  font-weight: 700;
}

.cth-15__breathe:focus-visible {
  outline: 1.5px solid var(--ink);
  outline-offset: 10px;
}

.cth-15__dek {
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 46ch;
  font-style: italic;
  font-family: Georgia,serif;
}

.cth-15__nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 4px;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  padding: 6px 0;
}

.cth-15__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 18px;
  font-size: 12px;
  font-weight: 650;
  letter-spacing: .18em;
  margin-right: -.18em;
  text-transform: uppercase;
  color: var(--mut);
  text-decoration: none;
  transition: letter-spacing .4s cubic-bezier(.25,.8,.25,1),margin-right .4s cubic-bezier(.25,.8,.25,1),color .3s;
}

.cth-15__nav a:hover,
.cth-15__nav a:focus-visible {
  letter-spacing: .3em;
  margin-right: -.3em;
  color: var(--ink);
}

.cth-15__nav a:focus-visible {
  outline: 1.5px solid var(--ink);
  outline-offset: -4px;
}

.cth-15__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 58ch;
}

.cth-15__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.92 0.004 90);
  padding: 1px 6px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cth-15 * {
    transition-duration: .01ms !important;
  }
}
```
