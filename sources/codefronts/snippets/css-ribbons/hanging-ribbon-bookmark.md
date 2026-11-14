---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/hanging-ribbon-bookmark/"
title: "Hanging Ribbon Bookmark"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "A cloth bookmark that drops over the top edge of the card when you save the article — it falls, overshoots, and settles with a two-beat pendulum swing,…"
has_js: "true"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hanging Ribbon Bookmark
Source: https://codefronts.com/snippets/css-ribbons/hanging-ribbon-bookmark/

A cloth bookmark that drops over the top edge of the card when you save the article — it falls, overshoots, and settles with a two-beat pendulum swing, exactly like a real ribbon marker in a book. One toggle button drives it, the state is aria-pressed (not a class), and the whole animation is transform-origin: top center plus five keyframes.
## HTML
```html
<section class="rib-11" aria-label="Hanging ribbon bookmark for article cards demo">
  <div class="rib-11__stage">
    <div class="rib-11__grid">
      <article class="rib-11__card">
        <div class="rib-11__thumb">
          <img class="rib-11__img" alt="Long exposure of a night highway seen from above" loading="lazy" decoding="async" width="620" height="400"
            src="https://images.unsplash.com/photo-1502920917128-1aa500764cbd?q=80&w=760&auto=format&fit=crop">
        </div>
        <button class="rib-11__save" type="button" aria-pressed="true" aria-label="Save this article">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path fill="currentColor" d="M6 2h12a2 2 0 0 1 2 2v18l-8-4.5L4 22V4a2 2 0 0 1 2-2Z"/></svg>
        </button>
        <span class="rib-11__bookmark" aria-hidden="true"><span class="rib-11__fold"></span></span>
        <div class="rib-11__body">
          <p class="rib-11__kicker">Infrastructure</p>
          <h3 class="rib-11__name">What we learned running edge functions in eleven regions</h3>
          <p class="rib-11__meta">Priya Raman · <time datetime="2026-07-28">28 Jul 2026</time> · 14 min</p>
        </div>
      </article>
      <article class="rib-11__card">
        <div class="rib-11__thumb">
          <img class="rib-11__img" alt="Close up of a mechanical keyboard lit from the side" loading="lazy" decoding="async" width="620" height="400"
            src="https://images.unsplash.com/photo-1587829741301-dc798b83add3?q=80&w=760&auto=format&fit=crop">
        </div>
        <button class="rib-11__save" type="button" aria-pressed="false" aria-label="Save this article">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path fill="currentColor" d="M6 2h12a2 2 0 0 1 2 2v18l-8-4.5L4 22V4a2 2 0 0 1 2-2Z"/></svg>
        </button>
        <span class="rib-11__bookmark" aria-hidden="true"><span class="rib-11__fold"></span></span>
        <div class="rib-11__body">
          <p class="rib-11__kicker">Craft</p>
          <h3 class="rib-11__name">The case for typing your own design tokens by hand</h3>
          <p class="rib-11__meta">Sam Okonjo · <time datetime="2026-07-11">11 Jul 2026</time> · 8 min</p>
        </div>
      </article>
    </div>
    <p class="rib-11__live" role="status">1 article saved</p>
    <p class="rib-11__chip" aria-hidden="true">transform-origin: top · decaying swing keyframes · aria-pressed as the state</p>
  </div>
</section>
```
## CSS
```css
.rib-11,
.rib-11 *,
.rib-11 *::before,
.rib-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-11-bg: #f3f1ee;
  --rib-11-bg: oklch(0.96 0.006 70);
  --rib-11-card: #fff;
  --rib-11-card: oklch(1 0 0);
  --rib-11-ink: #20211f;
  --rib-11-ink: oklch(0.25 0.008 90);
  --rib-11-mut: #6f716c;
  --rib-11-mut: oklch(0.57 0.01 90);
  --rib-11-acc: #c0392b;
  --rib-11-acc: oklch(0.55 0.18 25);
  --rib-11-drop: 104px;
  --rib-11-notch: 16px;
  background: var(--rib-11-bg);
  color: var(--rib-11-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(14px,2.6vw,22px);
  padding: clamp(28px,5vw,60px);
}

.rib-11__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(260px,1fr));
  gap: clamp(18px,3vw,26px);
  width: min(100%,820px);
  padding-block-start: 22px;
}

.rib-11__card {
  position: relative;
  overflow: visible;
  border-radius: 20px;
  background: var(--rib-11-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 18px 40px -22px oklch(0.3 0.02 90/.5);
  transition: box-shadow .4s;
}

.rib-11__card:hover {
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 54px -24px oklch(0.3 0.02 90/.55);
}

.rib-11__thumb {
  aspect-ratio: 16/10;
  border-radius: 20px 20px 0 0;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.86 0.02 70),oklch(0.8 0.03 50));
}

.rib-11__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.rib-11__save {
  position: absolute;
  z-index: 3;
  inset-block-start: 12px;
  inset-inline-start: 12px;
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 12px;
  background: oklch(0.15 0.01 90/.55);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  color: oklch(1 0 0/.62);
  cursor: pointer;
  transition: background .25s,color .25s,scale .2s;
}

.rib-11__save:hover {
  background: oklch(0.15 0.01 90/.72);
  scale: 1.05;
}

.rib-11__save[aria-pressed="true"] {
  color: oklch(0.98 0.02 25);
  background: color-mix(in oklch,var(--rib-11-acc) 78%,black);
}

.rib-11__save:focus-visible {
  outline: 3px solid var(--rib-11-acc);
  outline-offset: 3px;
}

.rib-11__bookmark {
  position: absolute;
  z-index: 2;
  inset-block-start: -16px;
  inset-inline-end: 30px;
  inline-size: 38px;
  block-size: 0;
  overflow: hidden;
  transform-origin: top center;
  background: linear-gradient(100deg,color-mix(in oklch,var(--rib-11-acc) 100%,white 10%),var(--rib-11-acc) 55%,color-mix(in oklch,var(--rib-11-acc) 84%,black 10%));
  clip-path: polygon(0 0,100% 0,100% 100%,50% calc(100% - var(--rib-11-notch)),0 100%);
  filter: drop-shadow(0 6px 10px oklch(0.3 0.08 25/.4));
  transition: block-size .5s cubic-bezier(.16,1,.3,1);
}

.rib-11__save[aria-pressed="true"]~.rib-11__bookmark {
  block-size: var(--rib-11-drop);
  animation: rib-11-swing .95s cubic-bezier(.34,1.2,.64,1) .12s;
}

@keyframes rib-11-swing {
  0% {
    rotate: 0deg;
  }

  35% {
    rotate: 5deg;
  }

  60% {
    rotate: -3.2deg;
  }

  80% {
    rotate: 1.4deg;
  }

  100% {
    rotate: 0deg;
  }
}

.rib-11__fold {
  position: absolute;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 16px;
  background: inherit;
  filter: brightness(.7);
  box-shadow: inset 0 -2px 3px oklch(0 0 0/.28);
}

.rib-11__body {
  display: grid;
  gap: 7px;
  padding: 17px 18px 20px;
}

.rib-11__kicker {
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--rib-11-acc);
}

.rib-11__name {
  font-size: 18px;
  font-weight: 620;
  line-height: 1.32;
  letter-spacing: -.02em;
  text-wrap: balance;
  padding-inline-end: 46px;
}

.rib-11__meta {
  font-size: 12.5px;
  color: var(--rib-11-mut);
}

.rib-11__live {
  font-size: 13px;
  color: var(--rib-11-mut);
  font-variant-numeric: tabular-nums;
  min-height: 1.2em;
}

.rib-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-11-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-11 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.rib-11__stage').forEach((stage) => {
    if (stage.dataset.wired) return;
    stage.dataset.wired = '1';
    const live = stage.querySelector('.rib-11__live');
    const buttons = [...stage.querySelectorAll('.rib-11__save')];
    const report = () => {
      const n = buttons.filter((b) => b.getAttribute('aria-pressed') === 'true').length;
      live.textContent = n === 0 ? 'No articles saved' : n + (n === 1 ? ' article saved' : ' articles saved');
    };
    buttons.forEach((btn) => {
      btn.addEventListener('click', () => {
        const next = btn.getAttribute('aria-pressed') !== 'true';
        btn.setAttribute('aria-pressed', String(next));
        // Re-trigger the swing only on a real state change.
        const ribbon = btn.nextElementSibling;
        ribbon.style.animation = 'none';
        void ribbon.offsetWidth;
        ribbon.style.animation = '';
        report();
      });
    });
    report();
  });
})();
```
