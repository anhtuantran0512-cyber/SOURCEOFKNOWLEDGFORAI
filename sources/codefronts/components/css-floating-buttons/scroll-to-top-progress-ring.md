---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/scroll-to-top-progress-ring/"
title: "Scroll-to-Top Floating Button with SVG Progress Ring"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "Back-to-top with a reading-progress ring, and — for the first time — no scroll listener."
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-to-Top Floating Button with SVG Progress Ring
Source: https://codefronts.com/components/css-floating-buttons/scroll-to-top-progress-ring/

Back-to-top with a reading-progress ring, and — for the first time — no scroll listener. CSS scroll-driven animations tie stroke-dashoffset and the button's own entrance directly to the scroll position, so the ring is perfectly in sync at every frame and costs nothing on the main thread. Degrades to a plain always-visible button where the timeline is unsupported.
## HTML
```html
<section class="fb-12" aria-label="Scroll to top button with progress ring demo">
  <div class="fb-12__frame">
    <div class="fb-12__scroll" id="fb-12-scroll" tabindex="0" aria-label="Scrollable article">
      <span id="fb-12-top"></span>
      <header class="fb-12__hero">
        <p class="fb-12__eyebrow">animation-timeline: scroll()</p>
        <h2 class="fb-12__title">A ring that cannot fall out of sync</h2>
        <p class="fb-12__sub">The progress arc is bound to the scroll position itself, not to a listener guessing at it. Scroll and watch it fill.</p>
      </header>
      <article class="fb-12__body">
        <p>A scroll listener runs on the main thread, samples whenever the browser lets it, and drifts on a fast flick. A scroll-driven animation is evaluated by the compositor from the same value that positions the content — there is nothing to drift from.</p>
        <p>The ring's dash length is its circumference. For <code>r = 22</code> that is <code>2π × 22 ≈ 138.23</code>, stored as a custom property so the keyframes never need to know the number.</p>
        <p>Keep the button's reveal on the same timeline. Two animations sharing one scroll source can never disagree about whether the user has scrolled far enough.</p>
        <p>Notice the button is an anchor, not a button element. Back-to-top is navigation within the document, so a link is the honest semantic — and it works with script disabled.</p>
        <p>The smooth scroll comes from <code>scroll-behavior:smooth</code> on the container, wrapped in a reduced-motion query so that users who ask for less movement get an instant jump instead of a long glide.</p>
        <p>On a real page, put the same rules on <code>html</code> instead of a nested container and change <code>scroll(nearest block)</code> to <code>scroll(root block)</code>. Nothing else changes.</p>
        <p>Progress rings also work as read-time indicators on long-form articles, upload meters on media, and completion gauges in onboarding checklists. Same construction each time.</p>
        <p>You have reached the bottom. The ring is closed, and the button has been fully visible since roughly the first fifth of this article.</p>
      </article>
    </div>
    <a class="fb-12__btn" id="fb-12-btn" href="#fb-12-top" aria-label="Back to top">
      <svg class="fb-12__ringSvg" viewBox="0 0 52 52" aria-hidden="true" focusable="false">
        <circle class="fb-12__track" cx="26" cy="26" r="22" fill="none" stroke-width="3.5"/>
        <circle class="fb-12__ring" cx="26" cy="26" r="22" fill="none" stroke-width="3.5" stroke-linecap="round"/>
      </svg>
      <svg class="fb-12__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 19V6M6 12l6-6 6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </a>
  </div>
  <p class="fb-12__chip">stroke-dasharray 138.23 · reveal at 8–20% · anchor to #top</p>
</section>
```
## CSS
```css
.fb-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-12-bg);
  --fb-12-bg: oklch(0.96 0.012 85);
  --fb-12-brand: oklch(0.52 0.15 30);
  --fb-12-ink: oklch(0.24 0.03 60);
  --fb-12-mut: oklch(0.52 0.02 60);
  --fb-12-card: oklch(1 0 0);
  --fb-12-c: 138.23;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-12-ink);
  display: grid;
  place-items: center;
  align-content: center;
  gap: 16px;
  padding: clamp(18px,4vw,44px);
}

.fb-12 *,
.fb-12 *::before,
.fb-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-12__frame {
  position: relative;
  width: min(100%,600px);
  height: min(74svh,660px);
  border-radius: 26px;
  overflow: hidden;
  background: var(--fb-12-card);
  border: 1px solid oklch(0.24 0.03 60/.1);
  box-shadow: 0 26px 60px -32px oklch(0.24 0.03 60/.8);
}

.fb-12__scroll {
  height: 100%;
  overflow: auto;
  scroll-behavior: smooth;
  padding-bottom: 96px;
  scrollbar-width: thin;
}

.fb-12__scroll:focus-visible {
  outline: 3px solid var(--fb-12-brand);
  outline-offset: -3px;
}

.fb-12__hero {
  padding: clamp(28px,5vw,46px) clamp(20px,4vw,36px) 20px;
  display: grid;
  gap: 10px;
  background: linear-gradient(165deg,oklch(0.93 0.045 60),oklch(0.99 0.008 60));
}

.fb-12__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-12-brand);
}

.fb-12__title {
  font-size: clamp(24px,4vw,34px);
  line-height: 1.08;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-12__sub {
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--fb-12-mut);
  text-wrap: pretty;
}

.fb-12__body {
  display: grid;
  gap: 15px;
  padding: 22px clamp(20px,4vw,36px) 0;
}

.fb-12__body p {
  font-size: 14.5px;
  line-height: 1.74;
  color: oklch(0.37 0.02 60);
  text-wrap: pretty;
}

.fb-12__body code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.52 0.15 30/.1);
  padding: 2px 6px;
  border-radius: 6px;
}

.fb-12__btn {
  position: absolute;
  right: 20px;
  bottom: 20px;
  z-index: 3;
  display: grid;
  place-items: center;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: var(--fb-12-card);
  color: var(--fb-12-brand);
  text-decoration: none;
  box-shadow: 0 12px 30px -12px oklch(0.24 0.03 60/.85),0 1px 3px oklch(0.24 0.03 60/.16);
  transition: transform .26s cubic-bezier(.2,1.3,.4,1),box-shadow .26s ease;
}

.fb-12__btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 38px -12px oklch(0.24 0.03 60/.9);
}

.fb-12__btn:active {
  transform: scale(.93);
}

.fb-12__btn:focus-visible {
  outline: 3px solid var(--fb-12-brand);
  outline-offset: 3px;
}

.fb-12__ringSvg {
  position: absolute;
  inset: 4px;
  width: 52px;
  height: 52px;
  rotate: -90deg;
}

.fb-12__track {
  stroke: oklch(0.24 0.03 60/.12);
}

.fb-12__ring {
  stroke: var(--fb-12-brand);
  stroke-dasharray: var(--fb-12-c);
  stroke-dashoffset: calc(var(--fb-12-c) * (1 - var(--fb-12-p,0)));
  transition: stroke-dashoffset .12s linear;
}

.fb-12__arrow {
  width: 23px;
  height: 23px;
  position: relative;
  z-index: 2;
}

.fb-12__btn {
  opacity: 0;
  scale: .5;
  pointer-events: none;
  transition: opacity .28s ease,scale .28s cubic-bezier(.2,1.3,.4,1),transform .26s cubic-bezier(.2,1.3,.4,1),box-shadow .26s ease;
}

.fb-12__frame[data-fb-shown="1"] .fb-12__btn {
  opacity: 1;
  scale: 1;
  pointer-events: auto;
}

.fb-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-12-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.24 0.03 60/.14);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .fb-12__scroll {
    scroll-behavior: auto;
  }

  .fb-12__btn {
    transition: none;
  }
}
```

## JavaScript
```js

(() => {
  const scroller = document.getElementById('fb-12-scroll');
  const frame = scroller && scroller.closest('.fb-12__frame');
  const ring = frame && frame.querySelector('.fb-12__ring');
  if (!scroller || !frame || !ring || scroller.dataset.fbWired) return;
  scroller.dataset.fbWired = '1';
  let raf = 0;
  const update = () => {
    raf = 0;
    const max = scroller.scrollHeight - scroller.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, scroller.scrollTop / max)) : 0;
    ring.style.setProperty('--fb-12-p', p.toFixed(4));
    frame.dataset.fbShown = p > 0.08 ? '1' : '0';
  };
  scroller.addEventListener('scroll', () => {
    if (!raf) raf = requestAnimationFrame(update);
  }, { passive: true });
  update();
})();
        
```
