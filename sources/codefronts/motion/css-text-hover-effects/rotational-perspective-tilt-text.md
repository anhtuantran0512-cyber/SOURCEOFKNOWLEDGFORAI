---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/rotational-perspective-tilt-text/"
title: "Rotational / Perspective Tilt Text"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "A headline that tilts TOWARD your cursor — up-left, down-right, wherever you approach from — with zero JavaScript."
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotational / Perspective Tilt Text
Source: https://codefronts.com/motion/css-text-hover-effects/rotational-perspective-tilt-text/

A headline that tilts TOWARD your cursor — up-left, down-right, wherever you approach from — with zero JavaScript. The trick: four invisible quadrant hover zones laid over the word, each one steering the sibling headline to a different rotateX/rotateY pose via the ~ combinator; glide across the word and the transitions blend poses continuously, faking full cursor tracking with four rules. The text-shadow slides opposite the tilt every time (light stays put, object turns), which is what convinces your eye it's one rigid object in space.
## HTML
```html
<section class="cth-22" aria-label="Perspective tilt text demo">
  <div class="cth-22__stage">
    <div class="cth-22__scene">
      <p class="cth-22__eyebrow">Pivot &mdash; the design systems summit</p>
      <div class="cth-22__tilt3d" tabindex="0" aria-label="PIVOT '26, tilting headline">
        <i class="cth-22__z cth-22__z--tl" aria-hidden="true"></i><i class="cth-22__z cth-22__z--tr" aria-hidden="true"></i><i class="cth-22__z cth-22__z--bl" aria-hidden="true"></i><i class="cth-22__z cth-22__z--br" aria-hidden="true"></i>
        <h1 class="cth-22__word" aria-hidden="true">PIVOT&rsquo;26</h1>
      </div>
      <p class="cth-22__sub">Approach the wordmark from any corner &mdash; it leans toward you. Four invisible hover quadrants, four poses, one transition blending them. No script.</p>
      <p class="cth-22__hint">The shadow always slides opposite the tilt &mdash; fixed lamp, turning object. <kbd>Tab</kbd> to it for the keyboard sway.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-22,
.cth-22 *,
.cth-22 *::before,
.cth-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-22 {
  --bg: oklch(0.94 0.006 260);
  --ink: oklch(0.22 0.02 270);
  --mut: oklch(0.5 0.015 265);
  --acc: oklch(0.55 0.19 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-22__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(80% 65% at 50% 30%,oklch(0.97 0.004 260),var(--bg) 75%);
  padding: clamp(20px,4vw,56px);
  container: cth22/inline-size;
}

.cth-22__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(18px,3.4cqi,28px);
}

.cth-22__eyebrow {
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-22__tilt3d {
  position: relative;
  perspective: 850px;
  padding: clamp(16px,3cqi,30px) clamp(20px,4cqi,44px);
  border-radius: 16px;
}

.cth-22__tilt3d:focus-visible {
  outline: 2.5px solid var(--acc);
  outline-offset: 4px;
}

.cth-22__z {
  position: absolute;
  width: 50%;
  height: 50%;
  z-index: 2;
}

.cth-22__z--tl {
  top: 0;
  left: 0;
}

.cth-22__z--tr {
  top: 0;
  right: 0;
}

.cth-22__z--bl {
  bottom: 0;
  left: 0;
}

.cth-22__z--br {
  bottom: 0;
  right: 0;
}

.cth-22__word {
  font-size: clamp(58px,13.5cqi,140px);
  font-weight: 900;
  letter-spacing: -.035em;
  line-height: 1;
  color: var(--ink);
  transform: rotateX(0) rotateY(0);
  text-shadow: 0 .06em .09em oklch(0.2 0.02 270/.22);
  transition: transform .5s cubic-bezier(.2,.8,.25,1),text-shadow .5s ease;
}

.cth-22__z--tl:hover ~ .cth-22__word {
  transform: rotateX(11deg) rotateY(-13deg);
  text-shadow: .07em .11em .13em oklch(0.2 0.02 270/.42);
}

.cth-22__z--tr:hover ~ .cth-22__word {
  transform: rotateX(11deg) rotateY(13deg);
  text-shadow: -.07em .11em .13em oklch(0.2 0.02 270/.42);
}

.cth-22__z--bl:hover ~ .cth-22__word {
  transform: rotateX(-11deg) rotateY(-13deg);
  text-shadow: .07em -.07em .13em oklch(0.2 0.02 270/.4);
}

.cth-22__z--br:hover ~ .cth-22__word {
  transform: rotateX(-11deg) rotateY(13deg);
  text-shadow: -.07em -.07em .13em oklch(0.2 0.02 270/.4);
}

.cth-22__tilt3d:focus-visible .cth-22__word {
  animation: cth22-sway 3.2s ease-in-out infinite;
}

@keyframes cth22-sway {
  0%,
    100% {
    transform: rotateX(9deg) rotateY(-11deg);
  }

  50% {
    transform: rotateX(-9deg) rotateY(11deg);
  }
}

.cth-22__sub {
  font-size: 15px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 52ch;
}

.cth-22__hint {
  font-size: 12.5px;
  color: var(--mut);
}

.cth-22__hint kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  border: 1px solid oklch(0.85 0.008 260);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 2px 6px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cth-22__word {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
