---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/css-parallax-text-overlay-effect/"
title: "Parallax Text Overlay Texture Effect"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A magazine-scale headline with photographic texture moving inside the letterforms."
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Text Overlay Texture Effect
Source: https://codefronts.com/motion/css-parallax-designs/css-parallax-text-overlay-effect/

A magazine-scale headline with photographic texture moving inside the letterforms. The type is a knockout layer in mix-blend-mode: lighten over a photo plane that drifts on scroll, which keeps the moving part on the compositor instead of animating a background position inside the text.
## HTML
```html
<div class="plx-19">
  <section class="plx-19__stage" aria-labelledby="plx-19-title">
    <img class="plx-19__plate" src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=1600&auto=format&fit=crop" alt="" aria-hidden="true" loading="eager" decoding="async">
    <div class="plx-19__grain" aria-hidden="true"></div>
    <div class="plx-19__knock">
      <p class="plx-19__kicker">The Quarterly · Essay</p>
      <h1 class="plx-19__h1" id="plx-19-title">Weather<br>as a kind<br>of writing</h1>
      <p class="plx-19__byline">By Alex Chen</p>
    </div>
  </section>
  <main class="plx-19__body">
    <p class="plx-19__drop">Every landscape writer eventually admits that the weather is doing most of the work. It arranges the light, decides the palette, sets the tempo, and takes the credit for the sentence you spent an afternoon on.</p>
    <p class="plx-19__p">The headline above is not an image. It is live text — selectable, searchable, resizable — with a photograph showing through the letterforms because the layer holding the type is blending rather than filling. Scroll and the photograph moves inside the letters while the letters themselves stay exactly where they are.</p>
    <p class="plx-19__p">The technique is old — printers were knocking type out of tinted plates a century ago — and the only modern part is that the plate can move on the compositor without touching the type.</p>
    <h2 class="plx-19__h2">On restraint</h2>
    <p class="plx-19__p">It works once per page. Twice reads as a template, three times as a filter. The rest of this essay is set in plain ink for exactly that reason.</p>
  </main>
</div>
```
## CSS
```css
.plx-19 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Playfair Display", "Hoefler Text", "Georgia", "Times New Roman", serif;
  --font-body: Georgia, "Iowan Old Style", "Times New Roman", serif;
  --paper: #f4eee2;
  --ink: #14110c;
  --muted: #6e6455;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-19 * {
  box-sizing: border-box;
}

.plx-19__stage {
  position: relative;
  min-height: 100svh;
  overflow: clip;
  isolation: isolate;
  background: var(--paper);
}

.plx-19__plate {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 124%;
  object-fit: cover;
  object-position: 50% 68%;
  filter: contrast(1.32) brightness(0.74) saturate(1.05);
  will-change: transform;
  z-index: 1;
}

.plx-19__grain {
  position: absolute;
  inset: 0;
  z-index: 2;
  opacity: 0.22;
  background-image: radial-gradient(rgba(0,0,0,0.35) 0.5px, transparent 0.6px);
  background-size: 3px 3px;
  pointer-events: none;
}

.plx-19__knock {
  position: relative;
  z-index: 3;
  min-block-size: 100svh;
  padding: clamp(28px, 6vw, 88px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 18px;
  background: var(--paper);
  color: var(--ink);
}

@supports (mix-blend-mode: lighten) {
  .plx-19__knock {
    mix-blend-mode: lighten;
  }

  .plx-19__knock .plx-19__h1 {
    color: #000;
  }
}

.plx-19__kicker {
  margin: 0;
  font-family: var(--font-body);
  font-size: 11px;
  letter-spacing: 0.34em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-19__h1 {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(48px, 15vw, 168px);
  font-weight: 700;
  line-height: 0.86;
  letter-spacing: -0.035em;
}

.plx-19__byline {
  margin: 0;
  font-size: 13px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-19__body {
  position: relative;
  z-index: 4;
  background: var(--paper);
  padding: clamp(40px, 8vw, 104px) clamp(24px, 6vw, 88px) 130px;
  max-inline-size: 40rem;
}

.plx-19__drop {
  margin: 0 0 20px;
  font-size: clamp(17px, 3.8vw, 21px);
  line-height: 1.66;
  text-wrap: pretty;
}

.plx-19__drop::first-letter {
  float: left;
  font-family: var(--font-display);
  font-size: 3.6em;
  line-height: 0.8;
  padding-inline-end: 0.06em;
  padding-block-start: 0.04em;
}

.plx-19__p {
  margin: 0 0 18px;
  font-size: clamp(16px, 3.4vw, 18px);
  line-height: 1.78;
  color: #2c261d;
  text-wrap: pretty;
}

.plx-19__h2 {
  margin: 32px 0 14px;
  font-family: var(--font-display);
  font-size: clamp(22px, 4.6vw, 32px);
  font-weight: 700;
  letter-spacing: -0.015em;
}

@supports (animation-timeline: scroll()) {
  .plx-19__plate {
    animation: plx-19-drift linear both;
    animation-timeline: scroll(root);
    animation-range: 0 70%;
  }
}

@keyframes plx-19-drift {
  from {
    transform: translateY(0) scale(1.02);
  }

  to {
    transform: translateY(-140px) scale(1.1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-19__plate {
    animation: none !important;
    transform: none !important;
    block-size: 100%;
    will-change: auto;
  }
}
```
