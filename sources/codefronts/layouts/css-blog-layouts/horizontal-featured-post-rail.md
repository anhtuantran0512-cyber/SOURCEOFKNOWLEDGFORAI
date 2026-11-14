---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/horizontal-featured-post-rail/"
title: "Horizontal Featured Post Rail"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A featured rail that is a scroller, not a carousel — native scrolling, native keyboard support, native momentum on touch, with scroll-snap-type: x mandatory…"
has_js: "true"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Featured Post Rail
Source: https://codefronts.com/layouts/css-blog-layouts/horizontal-featured-post-rail/

A featured rail that is a scroller, not a carousel — native scrolling, native keyboard support, native momentum on touch, with scroll-snap-type: x mandatory doing the alignment. A scroll-driven progress bar tracks position in pure CSS, and the arrow buttons are eight lines of scrollBy for mouse users who want them.
## HTML
```html
<div class="bl-20">
  <div class="bl-20__stage">
    <header class="bl-20__head">
      <div>
        <p class="bl-20__eyebrow">Featured this month</p>
        <h2>Six pieces worth your commute</h2>
      </div>
      <div class="bl-20__arrows">
        <button type="button" data-dir="-1" aria-label="Scroll to previous posts">
          <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12 4.5 6.5 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <button type="button" data-dir="1" aria-label="Scroll to next posts">
          <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M8 4.5 13.5 10 8 15.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </header>

    <ul class="bl-20__rail" data-rail tabindex="0" aria-label="Featured posts, horizontally scrollable">
      <li class="bl-20__card">
        <a href="#">
          <span class="bl-20__media"><img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="800" height="600" loading="lazy" decoding="async"></span>
          <span class="bl-20__num">01</span>
          <span class="bl-20__cat">Systems</span>
          <strong>The design system that fit on one page</strong>
          <span class="bl-20__ex">Twelve tokens, four components, and a rule about when to stop.</span>
          <span class="bl-20__meta">June Park · 9 min</span>
        </a>
      </li>
      <li class="bl-20__card">
        <a href="#">
          <span class="bl-20__media"><img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="800" height="600" loading="lazy" decoding="async"></span>
          <span class="bl-20__num">02</span>
          <span class="bl-20__cat">Performance</span>
          <strong>What we found after deleting 90% of our JavaScript</strong>
          <span class="bl-20__ex">A migration diary, with the three regressions we did not predict.</span>
          <span class="bl-20__meta">Dev Okoro · 14 min</span>
        </a>
      </li>
      <li class="bl-20__card">
        <a href="#">
          <span class="bl-20__media"><img src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="800" height="600" loading="lazy" decoding="async"></span>
          <span class="bl-20__num">03</span>
          <span class="bl-20__cat">Craft</span>
          <strong>Scroll-driven animation is a layout tool now</strong>
          <span class="bl-20__ex">Five patterns that used to need an observer and no longer do.</span>
          <span class="bl-20__meta">Rhea Nandi · 11 min</span>
        </a>
      </li>
      <li class="bl-20__card">
        <a href="#">
          <span class="bl-20__media"><img src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="800" height="600" loading="lazy" decoding="async"></span>
          <span class="bl-20__num">04</span>
          <span class="bl-20__cat">Accessibility</span>
          <strong>Twelve screen-reader bugs we shipped, ranked by shame</strong>
          <span class="bl-20__ex">Each one with the test that would have caught it in a minute.</span>
          <span class="bl-20__meta">Marcus Hale · 16 min</span>
        </a>
      </li>
      <li class="bl-20__card">
        <a href="#">
          <span class="bl-20__media"><img src="https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="800" height="600" loading="lazy" decoding="async"></span>
          <span class="bl-20__num">05</span>
          <span class="bl-20__cat">Process</span>
          <strong>Writing the changelog before the code</strong>
          <span class="bl-20__ex">A planning trick that keeps scope honest and docs current.</span>
          <span class="bl-20__meta">Lena Ostrowski · 7 min</span>
        </a>
      </li>
      <li class="bl-20__card">
        <a href="#">
          <span class="bl-20__media"><img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="800" height="600" loading="lazy" decoding="async"></span>
          <span class="bl-20__num">06</span>
          <span class="bl-20__cat">Interview</span>
          <strong>“We shipped less and grew faster”</strong>
          <span class="bl-20__ex">Mira Solberg on the year her team wrote almost no product code.</span>
          <span class="bl-20__meta">Transcript · 34 min</span>
        </a>
      </li>
    </ul>

    <div class="bl-20__track" aria-hidden="true"><div class="bl-20__progress"></div></div>
    <p class="bl-20__hint">Native scroller: swipe, shift-scroll, or Tab through the cards — snap points, momentum and keyboard support all come from the browser.</p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Newsreader:opsz,[email protected],400&display=swap');

.bl-20 {
  --bg: #0c0c10;
  --surface: #16161c;
  --text: #f3f3f6;
  --muted: #9698a4;
  --line: #26262f;
  --acc: #c4b5fd;
  --acc-2: #f0abfc;
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-20 {
    --bg: oklch(14% .008 285);
    --surface: oklch(20% .012 285);
    --text: oklch(96% .004 285);
    --muted: oklch(66% .014 285);
    --line: oklch(27% .014 285);
    --acc: oklch(80% .12 295);
    --acc-2: oklch(80% .14 330);
  }
}

@media (prefers-color-scheme: light) {
  .bl-20:not([data-theme="dark"]) {
    --bg: #f8f8fa;
    --surface: #ffffff;
    --text: #111116;
    --muted: #5f6270;
    --line: #e4e4ea;
    --acc: #5b21b6;
    --acc-2: #a21caf;
  }
}

.bl-20[data-theme="light"] {
  --bg: #f8f8fa;
  --surface: #ffffff;
  --text: #111116;
  --muted: #5f6270;
  --line: #e4e4ea;
  --acc: #5b21b6;
  --acc-2: #a21caf;
}

.bl-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-20,
.bl-20 *,
.bl-20 *::before,
.bl-20 *::after {
  box-sizing: border-box;
}

.bl-20 a {
  color: inherit;
  text-decoration: none;
}

.bl-20 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.bl-20__stage {
  min-height: 100svh;
  display: grid;
  align-content: center;
  gap: 1.5rem;
  padding-block: clamp(2rem,6vw,4rem);
  max-width: 100rem;
  margin-inline: auto;
}

.bl-20__head {
  display: flex;
  flex-wrap: wrap;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
  padding-inline: clamp(1.25rem,5vw,4rem);
}

.bl-20__eyebrow {
  margin: 0 0 .35rem;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-20__head h2 {
  margin: 0;
  font-size: clamp(1.75rem,4.5vw,3rem);
  font-weight: 800;
  line-height: 1.02;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.bl-20__arrows {
  display: flex;
  gap: .5rem;
}

.bl-20__arrows button {
  width: 2.75rem;
  height: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 1px solid var(--line);
  border-radius: 50%;
  background: var(--surface);
  color: var(--text);
  transition: border-color .18s ease, color .18s ease, scale .18s cubic-bezier(.16,1,.3,1);
}

.bl-20__arrows button svg {
  width: 1.15rem;
  height: 1.15rem;
}

.bl-20__arrows button:hover:not(:disabled) {
  border-color: var(--acc);
  color: var(--acc);
  scale: 1.06;
}

.bl-20__arrows button:disabled {
  opacity: .35;
  cursor: not-allowed;
}

.bl-20__rail {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: minmax(min(82vw,18rem),24rem);
  gap: clamp(1rem,2vw,1.5rem);
  margin: 0;
  padding: .5rem clamp(1.25rem,5vw,4rem) 1rem;
  list-style: none;
  overflow-x: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
  scroll-padding-inline: clamp(1.25rem,5vw,4rem);
  scroll-behavior: smooth;
  scrollbar-width: thin;
}

.bl-20__card {
  scroll-snap-align: center;
  min-width: 0;
}

.bl-20__card > a {
  position: relative;
  display: grid;
  gap: .5rem;
  height: 100%;
  padding: 1rem 1rem 1.25rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  overflow: hidden;
  transition: border-color .3s ease, translate .35s cubic-bezier(.16,1,.3,1), box-shadow .35s cubic-bezier(.16,1,.3,1);
}

.bl-20__card > a:hover {
  border-color: color-mix(in oklab,var(--acc) 45%,var(--line));
  translate: 0 -.3rem;
  box-shadow: 0 1.5rem 3rem -1.5rem color-mix(in oklab,var(--acc) 40%,transparent);
}

.bl-20__media {
  display: block;
  aspect-ratio: 16/10;
  border-radius: .75rem;
  overflow: hidden;
  background: var(--line);
}

.bl-20__media img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: scale .6s cubic-bezier(.16,1,.3,1);
}

.bl-20__card > a:hover .bl-20__media img {
  scale: 1.06;
}

.bl-20__num {
  position: absolute;
  inset-block-start: 1.4rem;
  inset-inline-end: 1.4rem;
  z-index: 2;
  font-size: .75rem;
  font-weight: 800;
  letter-spacing: .06em;
  color: #fff;
  padding: .25rem .5rem;
  border-radius: .4rem;
  background: rgba(10,10,14,.7);
  font-variant-numeric: tabular-nums;
}

.bl-20__cat {
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc-2);
  margin-top: .25rem;
}

.bl-20__card strong {
  font-size: clamp(1.0625rem,2vw,1.3125rem);
  font-weight: 700;
  line-height: 1.18;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.bl-20__ex {
  font-family: var(--serif);
  font-size: .9375rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-20__meta {
  margin-top: auto;
  padding-top: .6rem;
  border-top: 1px solid var(--line);
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-20__track {
  height: 3px;
  margin-inline: clamp(1.25rem,5vw,4rem);
  border-radius: 999px;
  background: var(--line);
  overflow: hidden;
}

.bl-20__progress {
  height: 100%;
  width: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg,var(--acc),var(--acc-2));
  transform-origin: left;
  scale: .2 1;
}

@supports (animation-timeline: scroll()) {
  .bl-20__progress {
    animation: bl-20-progress linear both;
    animation-timeline: scroll(nearest inline);
  }

  @keyframes bl-20-progress {
    from {
      scale: .14 1;
    }

    to {
      scale: 1 1;
    }
  }
}

@supports not (animation-timeline: scroll()) {
  .bl-20__track {
    display: none;
  }
}

.bl-20__hint {
  margin: 0;
  padding-inline: clamp(1.25rem,5vw,4rem);
  font-size: .8125rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 62ch;
  text-wrap: pretty;
}

@media (hover: none) {
  .bl-20__arrows {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-20__rail {
    scroll-behavior: auto;
  }

  .bl-20 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .bl-20__card > a {
    border: 1px solid CanvasText;
  }

  .bl-20__progress {
    background: Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.bl-20');
  if (!root) return;
  const rail = root.querySelector('[data-rail]');
  const btns = [...root.querySelectorAll('.bl-20__arrows button')];
  const step = () => Math.max(240, rail.clientWidth * 0.8);
  btns.forEach((b) => b.addEventListener('click', () => rail.scrollBy({ left: Number(b.dataset.dir) * step(), behavior: 'smooth' })));
  const sync = () => {
    const max = rail.scrollWidth - rail.clientWidth - 2;
    btns[0].disabled = rail.scrollLeft <= 2;
    btns[1].disabled = rail.scrollLeft >= max;
  };
  rail.addEventListener('scroll', sync, { passive: true });
  new ResizeObserver(sync).observe(rail);
  sync();
})();
```
