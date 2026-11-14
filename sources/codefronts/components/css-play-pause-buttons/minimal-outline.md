---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/minimal-outline/"
title: "Minimalist Line-Art Outline Button"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "Restraint as a technique: a hairline circle, a stroked triangle and a lot of air."
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Line-Art Outline Button
Source: https://codefronts.com/components/css-play-pause-buttons/minimal-outline/

Restraint as a technique: a hairline circle, a stroked triangle and a lot of air. On hover the ring draws itself around the button with stroke-dashoffset — the line-art equivalent of a fill animation — and on play the triangle becomes two strokes with rounded caps. Perfect for editorial sites, portfolios and premium brands where a filled button would feel loud.
## HTML
```html
<section class="pp-16" aria-label="Minimalist line art outline play button demo">
  <div class="pp-16__stage">
    <figure class="pp-16__unit">
      <input class="pp-16-chk" type="checkbox" id="pp-16-toggle" aria-label="Play or pause the essay audio">
      <label class="pp-16__btn" for="pp-16-toggle">
        <svg viewBox="0 0 120 120" width="132" height="132" aria-hidden="true">
          <circle class="pp-16__base" cx="60" cy="60" r="54" fill="none" stroke="currentColor" stroke-width="1" opacity=".14"/>
          <circle class="pp-16__draw" cx="60" cy="60" r="54" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round"/>
          <path class="pp-16__p" d="M50 43l26 17-26 17z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/>
          <path class="pp-16__q" d="M52 44v32M68 44v32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
        </svg>
      </label>
      <figcaption class="pp-16__cap">
        <p class="pp-16__label">Listen to this essay</p>
        <p class="pp-16__meta">14 min · read by the author</p>
      </figcaption>
    </figure>
    <p class="pp-16__chip" aria-hidden="true">stroke-dasharray = 2πr · dashoffset draw · hover + focus-visible parity</p>
  </div>
</section>
```
## CSS
```css
.pp-16,
.pp-16 *,
.pp-16 *::before,
.pp-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-16-bg);
  --pp-16-bg: oklch(0.98 0.004 85);
  --pp-16-ink: oklch(0.22 0.01 80);
  --pp-16-mut: oklch(0.55 0.012 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-16-ink);
}

.pp-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
}

.pp-16__unit {
  display: grid;
  justify-items: center;
  gap: 26px;
}

.pp-16-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-16__btn {
  display: grid;
  place-items: center;
  padding: 6px;
  border-radius: 50%;
  color: var(--pp-16-ink);
  cursor: pointer;
}

.pp-16__draw {
  stroke-dasharray: 339.3;
  stroke-dashoffset: 339.3;
  rotate: -90deg;
  transform-origin: 60px 60px;
  transition: stroke-dashoffset .8s cubic-bezier(.65,0,.35,1);
}

.pp-16__btn:hover .pp-16__draw {
  stroke-dashoffset: 0;
}

.pp-16-chk:focus-visible+.pp-16__btn .pp-16__draw {
  stroke-dashoffset: 0;
}

.pp-16-chk:focus-visible+.pp-16__btn {
  outline: 2px solid var(--pp-16-ink);
  outline-offset: 6px;
}

.pp-16__p,
.pp-16__q {
  transition: opacity .35s,scale .45s cubic-bezier(.34,1.3,.5,1);
  transform-origin: 60px 60px;
}

.pp-16__q {
  opacity: 0;
  scale: .86;
}

.pp-16-chk:checked+.pp-16__btn .pp-16__draw {
  stroke-dashoffset: 0;
}

.pp-16-chk:checked+.pp-16__btn .pp-16__p {
  opacity: 0;
  scale: .86;
}

.pp-16-chk:checked+.pp-16__btn .pp-16__q {
  opacity: 1;
  scale: 1;
}

.pp-16__cap {
  text-align: center;
}

.pp-16__label {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.pp-16__meta {
  font-size: 13px;
  color: var(--pp-16-mut);
  margin-top: 8px;
}

.pp-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-16-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0.22 0.01 80/.16);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-16 * {
    transition-duration: .01ms !important;
  }
}
```
