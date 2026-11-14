---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/scroll-triggered-glass-effect/"
title: "Scroll-Triggered Glass Effect"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The transparent-navbar-turn-to-frosted-glass-on-scroll pattern, done the 2027 way: a header that is fully transparent over a full-screen hero image and melts…"
has_js: "true"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Triggered Glass Effect
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/scroll-triggered-glass-effect/

The transparent-navbar-turn-to-frosted-glass-on-scroll pattern, done the 2027 way: a header that is fully transparent over a full-screen hero image and melts into a sticky frosted-glass bar as the user scrolls — driven entirely by CSS scroll-driven animations (animation-timeline: scroll()), no scroll listener, no layout thrash. A copy-paste IntersectionObserver fallback is included for older engines.
## HTML
```html
<div class="gn-02">
  <div class="gn-02__stage">
    <header class="gn-02-bar">
      <a class="gn-02-brand" href="#">Vista</a>
      <nav aria-label="Primary">
        <ul>
          <li><a href="#">Stays</a></li>
          <li><a href="#">Experiences</a></li>
          <li><a href="#" aria-current="page">Guides</a></li>
        </ul>
      </nav>
    </header>
    <section class="gn-02-hero"><h2>Wake up somewhere better.</h2></section>
    <section class="gn-02-body">
      <p>Scroll &mdash; the transparent bar frosts into glass as you move down the page.</p>
      <p>All of it driven by <code>animation-timeline: scroll()</code>, no JS on the modern path. The browser interpolates the keyframes from the scroll position; there is no <code>scroll</code> listener anywhere.</p>
      <p>Every glass surface pairs <code>backdrop-filter: blur() saturate()</code> with a semi-transparent fill and a 1px hairline &mdash; the trio that makes the pane read as physical glass rather than a washed-out box.</p>
      <p>The <code>animation-range</code> value is the tuning dial: shorten it to frost sooner, lengthen it to keep the transparent state longer while the hero is still in view.</p>
      <p>Everything runs on the compositor, so scrolling stays at 60fps even as the frost re-samples the moving content behind it.</p>
      <h3>Why this beats the JS scroll-handler pattern</h3>
      <p>The 2018-2023 pattern was: attach a <code>scroll</code> event listener, read <code>window.scrollY</code>, imperatively toggle a class past a threshold. That reads the DOM on every scroll frame and forces a style recalc.</p>
      <p>On a real mid-tier Android device, that pattern tanks Interaction to Next Paint by 20-40ms per frame. On a high-end desktop you never notice; in the field, Google's Core Web Vitals report catches it.</p>
      <p>Scroll-driven animations move the entire computation to the compositor thread. The main thread stays free for touch handlers, text input, hydration &mdash; the things that actually matter for INP.</p>
      <h3>The IntersectionObserver fallback</h3>
      <p>For engines without scroll-driven animations (before Chrome 115, Firefox 129, Safari 26), the fallback uses a 1px sentinel element inserted at the top of the hero. An <code>IntersectionObserver</code> toggles <code>.is-stuck</code> on the bar when the sentinel leaves the viewport.</p>
      <p>Detection is a single line: <code>if (!CSS.supports('animation-timeline: scroll()'))</code>. Modern browsers get the CSS path; older ones get identical visual behaviour via 8 lines of JS. See the JS tab for the copy-paste snippet.</p>
      <p>The observer callback runs once per intersection change, not per scroll frame. Even in the fallback path, the main thread stays quiet.</p>
      <h3>Design decisions worth knowing</h3>
      <p>Keep the transparent-state text light (white with a subtle text-shadow) and the frosted-state text dark. Interpolating <code>color</code> across the range handles the crossover automatically as the fill lightens.</p>
      <p>Extend the animation to tween more than fill + blur. Shrinking the bar's <code>height</code> from 72px to 56px as it frosts is a common polish move &mdash; but keep it above 48px for touch targets to stay compliant.</p>
      <p>Add a <code>box-shadow</code> that only appears in the frosted state to lift the bar off the page. A tight, low-opacity shadow reads as elevation without competing with the frost itself.</p>
      <p>Test with a slow-motion scroll (Chrome DevTools has a slow-scroll toggle) to confirm the interpolation looks smooth across the full range, not just at the endpoints.</p>
      <p>Keep scrolling &mdash; the bar stays pinned and frosted, letting content pass underneath cleanly.</p>
    </section>
  </div>
</div>
```
## CSS
```css
.gn-02 {
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  background: radial-gradient(130% 120% at 20% 10%,oklch(0.7 0.14 40),oklch(0.4 0.13 300) 60%,oklch(0.25 0.08 260));
}

.gn-02 * {
  box-sizing: border-box;
}

.gn-02__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  scroll-behavior: smooth;
}

.gn-02-bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 0 20px;
  height: 60px;
  color: #fff;
  background: transparent;
  border-bottom: 1px solid transparent;
  animation: gn02frost linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0 200px;
}

@keyframes gn02frost {
  to {
    background: rgba(255,255,255,.55);
    color: oklch(0.28 0.03 250);
    border-bottom-color: rgba(255,255,255,.5);
    -webkit-backdrop-filter: blur(14px) saturate(170%);
    backdrop-filter: blur(14px) saturate(170%);
    box-shadow: 0 6px 24px rgba(20,20,40,.14);
  }
}

.gn-02-bar.is-stuck {
  background: rgba(255,255,255,.55);
  color: oklch(0.28 0.03 250);
  border-bottom-color: rgba(255,255,255,.5);
  -webkit-backdrop-filter: blur(14px) saturate(170%);
  backdrop-filter: blur(14px) saturate(170%);
  box-shadow: 0 6px 24px rgba(20,20,40,.14);
}

.gn-02-brand {
  font-weight: 800;
  font-size: 18px;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.gn-02-bar nav ul {
  display: flex;
  gap: 8px;
  list-style: none;
  margin: 0;
  padding: 0;
  margin-inline-start: auto;
}

.gn-02-bar nav a {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 12px;
  border-radius: 9px;
  font: 600 14px/1 system-ui,sans-serif;
  color: inherit;
  text-decoration: none;
  transition: background-color .16s ease;
}

.gn-02-bar nav a:hover {
  background: rgba(127,127,127,.16);
}

.gn-02-bar a:focus-visible {
  outline: 2.5px solid currentColor;
  outline-offset: 2px;
}

.gn-02-hero {
  height: 280px;
  display: flex;
  align-items: flex-end;
  padding: 28px;
  background: linear-gradient(180deg,oklch(0.45 0.09 250/.15),oklch(0.2 0.05 260/.55)),radial-gradient(130% 120% at 20% 10%,oklch(0.7 0.14 40),oklch(0.4 0.13 300) 60%,oklch(0.25 0.08 260));
}

.gn-02-hero h2 {
  margin: 0;
  font: 800 30px/1.05 system-ui,sans-serif;
  letter-spacing: -.02em;
  color: #fff;
  text-shadow: 0 2px 18px rgba(0,0,0,.4);
}

.gn-02-body {
  padding: 32px 28px 80px;
  background: oklch(0.98 0.005 250);
  min-height: 900px;
}

.gn-02-body p {
  margin: 0 0 14px;
  font: 400 16px/1.6 system-ui,sans-serif;
  color: oklch(0.4 0.02 250);
}

.gn-02-body h3 {
  margin: 28px 0 12px;
  font: 700 19px/1.25 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: oklch(0.24 0.03 250);
}

.gn-02-body code {
  background: oklch(0.94 0.01 250);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
}

@media (max-width: 560px) {
  .gn-02-bar {
    gap: 12px;
    padding: 0 14px;
    height: 52px;
  }

  .gn-02-brand {
    font-size: 16px;
  }

  .gn-02-bar nav ul {
    gap: 2px;
  }

  .gn-02-bar nav a {
    padding: 0 8px;
    font-size: 13px;
  }

  .gn-02-hero {
    height: 220px;
    padding: 20px;
  }

  .gn-02-hero h2 {
    font-size: 22px;
  }
}

@media (max-width: 400px) {
  .gn-02-bar nav a {
    padding: 0 6px;
    font-size: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gn-02-bar {
    animation: none;
    background: rgba(255,255,255,.55);
    color: oklch(0.28 0.03 250);
    -webkit-backdrop-filter: blur(14px);
    backdrop-filter: blur(14px);
  }
}
```

## JavaScript
```js
/* Modern path is pure CSS (animation-timeline: scroll()). Progressive-enhancement fallback for
   engines without scroll-driven animations — a 1px sentinel toggles .is-stuck on the header: */
if (!CSS.supports('animation-timeline: scroll()')) {
  const scroller = document.querySelector('.gn-02__stage');
  const bar = scroller.querySelector('.gn-02-bar');
  const sentinel = document.createElement('div');
  sentinel.style.cssText = 'position:absolute;top:180px;height:1px;width:1px';
  scroller.prepend(sentinel);
  new IntersectionObserver(
    ([e]) => bar.classList.toggle('is-stuck', !e.isIntersecting),
    { root: scroller }
  ).observe(sentinel);
}
```
