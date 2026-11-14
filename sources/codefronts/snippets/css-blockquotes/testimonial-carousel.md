---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/testimonial-carousel/"
title: "JavaScript Testimonial Quote Slider CSS"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "A testimonial slider where CSS does the sliding and JS only advances the clock: the track is a scroll-snap container (overflow-x + scroll-snap-type: x…"
has_js: "true"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: JavaScript Testimonial Quote Slider CSS
Source: https://codefronts.com/snippets/css-blockquotes/testimonial-carousel/

A testimonial slider where CSS does the sliding and JS only advances the clock: the track is a scroll-snap container (overflow-x + scroll-snap-type: x mandatory), so swipe, trackpad, keyboard and scrollbar all work natively with momentum and rubber-banding no JS carousel reproduces. The dots are real anchor-free buttons wired by an 18-line IIFE that also autoplays — pausing on hover, on focus within, and permanently for prefers-reduced-motion users. Each slide is a full figure/blockquote card; the region carries the carousel ARIA pattern.
## HTML
```html
<section class="bq-23" aria-label="Testimonial quote slider demo">
  <div class="bq-23__stage">
    <div class="bq-23__slider" role="region" aria-roledescription="carousel" aria-label="Customer testimonials" id="bq23-slider">
      <div class="bq-23__track" tabindex="0" aria-label="Testimonials, scroll or use dots">
        <figure class="bq-23__slide" role="group" aria-label="1 of 3">
          <blockquote><p>“We replaced a 2,000-line carousel plugin with scroll-snap and a dozen lines of glue. Support tickets about the slider: zero since.”</p></blockquote>
          <figcaption><strong>Imogen Hart</strong> · Frontend Lead, Lumen Retail</figcaption>
        </figure>
        <figure class="bq-23__slide" role="group" aria-label="2 of 3">
          <blockquote><p>“The native swipe physics are the feature. No JS carousel ever matched the trackpad feel our users kept complaining about.”</p></blockquote>
          <figcaption><strong>Dario Fontaine</strong> · Product Engineer, Atlas Bank</figcaption>
        </figure>
        <figure class="bq-23__slide" role="group" aria-label="3 of 3">
          <blockquote><p>“Autoplay that actually pauses for hover, focus and reduced motion — our accessibility audit finally has an empty carousel section.”</p></blockquote>
          <figcaption><strong>Sofia Meloni</strong> · Design Systems, Fernwood</figcaption>
        </figure>
      </div>
      <div class="bq-23__dots" role="tablist" aria-label="Choose testimonial">
        <button type="button" class="bq-23__dot" aria-label="Show testimonial 1" aria-current="true"></button>
        <button type="button" class="bq-23__dot" aria-label="Show testimonial 2"></button>
        <button type="button" class="bq-23__dot" aria-label="Show testimonial 3"></button>
      </div>
    </div>
    <p class="bq-23__chip" aria-hidden="true">scroll-snap-type:x mandatory · JS only advances the clock · WCAG 2.2.2 pauses</p>
  </div>
</section>
```
## CSS
```css
.bq-23,
.bq-23 *,
.bq-23 *::before,
.bq-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.955 0.01 285);
  --card: oklch(1 0 0);
  --ink: oklch(0.26 0.02 290);
  --mut: oklch(0.52 0.02 290);
  --acc: oklch(0.55 0.18 295);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-23__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 55% at 50% 100%,oklch(0.9 0.04 295/.6),transparent),var(--bg);
  overflow-y: auto;
}

.bq-23__slider {
  width: min(100%,560px);
}

.bq-23__track {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 100%;
  gap: 18px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
  padding: 6px;
  border-radius: 24px;
}

.bq-23__track::-webkit-scrollbar {
  display: none;
}

.bq-23__track:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.bq-23__slide {
  scroll-snap-align: center;
  background: var(--card);
  border-radius: 20px;
  border: 1px solid oklch(0 0 0/.07);
  box-shadow: 0 3px 8px oklch(0.3 0.04 290/.07),0 18px 40px oklch(0.3 0.04 290/.1);
  padding: clamp(24px,4vw,34px);
  display: grid;
  align-content: center;
  gap: 18px;
  min-height: 230px;
}

.bq-23__slide blockquote p {
  font-size: clamp(16.5px,2.2vw,20px);
  line-height: 1.6;
  font-weight: 550;
  letter-spacing: -.008em;
  text-wrap: pretty;
}

.bq-23__slide figcaption {
  font-size: 13px;
  color: var(--mut);
}

.bq-23__slide figcaption strong {
  color: var(--acc);
  font-weight: 700;
}

.bq-23__dots {
  display: flex;
  justify-content: center;
  gap: 6px;
  margin-top: 16px;
}

.bq-23__dot {
  width: 28px;
  height: 28px;
  border: 0;
  background: none;
  border-radius: 99px;
  cursor: pointer;
  display: grid;
  place-items: center;
}

.bq-23__dot::before {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 99px;
  background: oklch(0.75 0.03 290);
  transition: width .3s cubic-bezier(.2,.7,.2,1),background .3s;
}

.bq-23__dot[aria-current="true"]::before {
  width: 26px;
  background: var(--acc);
}

.bq-23__dot:hover::before {
  background: var(--acc);
}

.bq-23__dot:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.bq-23__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: var(--card);
}

@media (prefers-reduced-motion: reduce) {
  .bq-23 * {
    transition-duration: .01ms !important;
  }

  .bq-23__track {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('bq23-slider');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const track = root.querySelector('.bq-23__track');
  const dots = [...root.querySelectorAll('.bq-23__dot')];
  const n = dots.length;
  let i = 0, raf = 0;
  const go = (k) => track.scrollTo({ left: track.clientWidth * ((k + n) % n), behavior: 'smooth' });
  dots.forEach((d, k) => d.addEventListener('click', () => go(k)));
  track.addEventListener('scroll', () => {
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      i = Math.round(track.scrollLeft / track.clientWidth);
      dots.forEach((d, k) => k === i ? d.setAttribute('aria-current', 'true') : d.removeAttribute('aria-current'));
    });
  });
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  setInterval(() => { if (!root.matches(':hover, :focus-within')) go(i + 1); }, 5000);
})();
```
