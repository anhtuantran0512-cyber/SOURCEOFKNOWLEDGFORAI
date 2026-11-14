---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/category-pill-badge-with-icon-css/"
title: "Category Pill Badge with Icon CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "A complete category-pill color system driven by one number."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Category Pill Badge with Icon CSS
Source: https://codefronts.com/snippets/css-tags-chips/category-pill-badge-with-icon-css/

A complete category-pill color system driven by one number. Each pill sets a single --h hue custom property; oklch() and color-mix() derive its icon color, text color, tint background and border automatically, so every category lands at mathematically identical contrast — something hand-picked hex palettes never achieve. Inline SVG icons ride currentColor, three sizes share one ruleset, and tinted / solid / outline / frosted-on-photo variants are each a four-line override.
## HTML
```html
<section class="ctc-04" aria-label="Category pill badge with icon demo">
  <div class="ctc-04__stage">
    <div class="ctc-04__wrap">
      <header class="ctc-04__head">
        <p class="ctc-04__kicker">Icon pills · one hue variable each</p>
        <h1>Six categories, zero hex codes</h1>
      </header>
      <nav class="ctc-04__wall" aria-label="Category pills">
        <a class="ctc-04__pill" style="--h:150" href="#ctc04"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5V5.5M9 8h6"/></svg>Guides</a>
        <a class="ctc-04__pill" style="--h:255" href="#ctc04"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m8 7-5 5 5 5M16 7l5 5-5 5"/></svg>Engineering</a>
        <a class="ctc-04__pill" style="--h:40" href="#ctc04"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 5 14h6l-1 8 8-12h-6z"/></svg>Opinion</a>
        <a class="ctc-04__pill" style="--h:320" href="#ctc04"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="9" cy="9.5" r="1.2"/><circle cx="15" cy="9.5" r="1.2"/><path d="M12 21c0-4 2-5 5-5 2.4 0 4-1 4-4"/></svg>Design</a>
        <a class="ctc-04__pill" style="--h:205" href="#ctc04"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8h3l2-3h8l2 3h3v12H3z"/><circle cx="12" cy="13.5" r="3.5"/></svg>Photography</a>
        <a class="ctc-04__pill" style="--h:95" href="#ctc04"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.2 2.2M16.2 16.2l2.2 2.2M18.4 5.6l-2.2 2.2M7.8 16.2l-2.2 2.2"/><circle cx="12" cy="12" r="3.4"/></svg>Field notes</a>
      </nav>
      <div class="ctc-04__row">
        <div class="ctc-04__cell"><p>Sizes — one <code>--s</code> scale factor</p><div class="ctc-04__group">
          <span class="ctc-04__pill" style="--h:255;--s:.8"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m8 7-5 5 5 5M16 7l5 5-5 5"/></svg>Small</span>
          <span class="ctc-04__pill" style="--h:255"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m8 7-5 5 5 5M16 7l5 5-5 5"/></svg>Medium</span>
          <span class="ctc-04__pill" style="--h:255;--s:1.25"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m8 7-5 5 5 5M16 7l5 5-5 5"/></svg>Large</span>
        </div></div>
        <div class="ctc-04__cell"><p>Variants — token math, not new palettes</p><div class="ctc-04__group">
          <span class="ctc-04__pill" style="--h:150"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5V5.5M9 8h6"/></svg>Tinted</span>
          <span class="ctc-04__pill ctc-04__pill--solid" style="--h:150"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5V5.5M9 8h6"/></svg>Solid</span>
          <span class="ctc-04__pill ctc-04__pill--outline" style="--h:150"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5V5.5M9 8h6"/></svg>Outline</span>
        </div></div>
      </div>
      <figure class="ctc-04__photo" style="--img:url(https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1100&q=60)">
        <figcaption>On photography, switch to the frosted variant — 85% white mix + <code>backdrop-filter</code></figcaption>
        <span class="ctc-04__pill ctc-04__pill--glass" style="--h:205"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8h3l2-3h8l2 3h3v12H3z"/><circle cx="12" cy="13.5" r="3.5"/></svg>Photography</span>
        <span class="ctc-04__pill ctc-04__pill--glass" style="--h:95"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.2 2.2M16.2 16.2l2.2 2.2M18.4 5.6l-2.2 2.2M7.8 16.2l-2.2 2.2"/><circle cx="12" cy="12" r="3.4"/></svg>Golden hour</span>
      </figure>
      <p class="ctc-04__note">Every pill is <code>style="--h:205"</code> and nothing else — background, border, text and icon all derive via <code>color-mix()</code>, so contrast is identical across the family.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-04,
.ctc-04 *,
.ctc-04 *::before,
.ctc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-04 {
  --bg: oklch(0.97 0.006 85);
  --ink: oklch(0.24 0.02 60);
  --mut: oklch(0.51 0.02 60);
  --line: oklch(0.9 0.01 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-04__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 50cqi at 15% -10%,oklch(0.9 0.05 150/.5),transparent 65%),radial-gradient(60cqi 50cqi at 110% 115%,oklch(0.9 0.05 320/.45),transparent 60%),var(--bg);
  container: ctc04/inline-size;
}

.ctc-04__wrap {
  width: min(780px,100%);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.ctc-04__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.58 0.14 255);
}

.ctc-04__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin-top: 6px;
}

.ctc-04__wall {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.ctc-04__pill {
  --s: 1;
  --c: oklch(0.62 0.14 var(--h,255));
  display: inline-flex;
  align-items: center;
  gap: calc(7px*var(--s));
  min-height: calc(44px*var(--s));
  padding: 0 calc(17px*var(--s));
  border-radius: 99px;
  font-size: calc(13.5px*var(--s));
  font-weight: 700;
  text-decoration: none;
  color: color-mix(in oklch,var(--c) 72%,var(--ink));
  background: color-mix(in oklch,var(--c) 13%,transparent);
  border: 1px solid color-mix(in oklch,var(--c) 28%,transparent);
  transition: background .2s,translate .2s,box-shadow .2s;
}

.ctc-04__pill svg {
  width: calc(14px*var(--s));
  height: calc(14px*var(--s));
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: rotate .25s cubic-bezier(.34,1.56,.64,1);
}

a.ctc-04__pill:hover,
a.ctc-04__pill:focus-visible {
  background: color-mix(in oklch,var(--c) 20%,transparent);
  translate: 0 -2px;
  box-shadow: 0 8px 18px -10px var(--c);
}

a.ctc-04__pill:hover svg,
a.ctc-04__pill:focus-visible svg {
  rotate: -12deg;
}

a.ctc-04__pill:focus-visible {
  outline: 2px solid var(--c);
  outline-offset: 2px;
}

.ctc-04__pill--solid {
  background: var(--c);
  color: color-mix(in oklch,var(--c) 8%,oklch(0.99 0 0));
  border-color: transparent;
  box-shadow: 0 6px 14px -8px var(--c);
}

.ctc-04__pill--outline {
  background: transparent;
  border: 1.5px solid color-mix(in oklch,var(--c) 55%,transparent);
}

.ctc-04__pill--glass {
  color: oklch(0.25 0.03 var(--h));
  background: color-mix(in oklch,oklch(0.98 0.005 85) 85%,var(--c));
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border-color: oklch(1 0 0/.55);
  box-shadow: 0 4px 14px oklch(0.2 0.02 60/.22);
}

.ctc-04__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.ctc-04__cell {
  border: 1px dashed var(--line);
  border-radius: 16px;
  padding: 16px;
  background: oklch(1 0 0/.5);
}

.ctc-04__cell p {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 12px;
}

.ctc-04__cell p code,
.ctc-04__note code,
.ctc-04__photo code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .92em;
  text-transform: none;
  letter-spacing: 0;
  background: oklch(0.93 0.01 80);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.ctc-04__group {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 9px;
}

.ctc-04__photo {
  position: relative;
  border-radius: 18px;
  overflow: clip;
  min-height: 150px;
  display: flex;
  align-items: flex-end;
  gap: 9px;
  padding: 16px;
  background-image: var(--img,none),linear-gradient(140deg,oklch(0.75 0.1 205),oklch(0.5 0.12 260));
  background-size: cover;
  background-position: center 60%;
}

.ctc-04__photo figcaption {
  position: absolute;
  top: 12px;
  left: 14px;
  right: 14px;
  font-size: 11.5px;
  font-weight: 600;
  color: oklch(0.99 0 0/.95);
  text-shadow: 0 1px 8px oklch(0 0 0/.5);
}

.ctc-04__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid oklch(0.62 0.14 255);
  padding-left: 12px;
}

@container ctc04 (width < 620px) {
  .ctc-04__row {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-04 * {
    transition-duration: .01ms !important;
  }
}
```
