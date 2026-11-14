---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/recipe-blog-card-grid/"
title: "Recipe Blog Card Grid"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "An image-first recipe index where nothing ever jumps: every photo is aspect-ratio-locked so the grid reserves its space before a single byte of image downloads."
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Recipe Blog Card Grid
Source: https://codefronts.com/layouts/css-blog-layouts/recipe-blog-card-grid/

An image-first recipe index where nothing ever jumps: every photo is aspect-ratio-locked so the grid reserves its space before a single byte of image downloads. Prep-time and difficulty badges float over the image, the metadata strip aligns across all cards, and each card is a real link region — the whole card is clickable without nesting anchors or faking it with JavaScript.
## HTML
```html
<div class="bl-05">
  <header class="bl-05__head">
    <p class="bl-05__eyebrow">Weeknights · 34 recipes</p>
    <h1>Dinner in under an hour, mostly one pan</h1>
    <p class="bl-05__lede">Tested three times each, with the timings you'd actually get on a Tuesday — no mise en place fantasy, no ten-ingredient garnish.</p>
    <div class="bl-05__filters" role="group" aria-label="Filter recipes">
      <button type="button" aria-pressed="true">All</button>
      <button type="button" aria-pressed="false">Under 30 min</button>
      <button type="button" aria-pressed="false">Vegetarian</button>
      <button type="button" aria-pressed="false">One pan</button>
      <button type="button" aria-pressed="false">Batch cook</button>
    </div>
  </header>

  <main class="bl-05__grid">
    <article class="bl-05__card" data-diff="easy">
      <div class="bl-05__media">
        <img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="Bowl of charred broccoli, grains and yoghurt" width="700" height="525" loading="eager" decoding="async">
        <p class="bl-05__badge"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 6v4.2l2.8 1.7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span><span class="bl-05__srOnly">Total time </span>25 min</span></p>
        <p class="bl-05__diff">Easy</p>
      </div>
      <div class="bl-05__body">
        <p class="bl-05__cat">Vegetarian</p>
        <h2 class="bl-05__title"><a href="#">Charred broccoli bowl with lemon yoghurt</a></h2>
        <p class="bl-05__note">The trick is a dry pan and no stirring for four full minutes.</p>
        <dl class="bl-05__stats">
          <div><dt>Prep</dt><dd>10 min</dd></div>
          <div><dt>Cook</dt><dd>15 min</dd></div>
          <div><dt>Serves</dt><dd>2</dd></div>
        </dl>
      </div>
    </article>

    <article class="bl-05__card" data-diff="medium">
      <div class="bl-05__media">
        <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="Seared steak resting on a wooden board" width="700" height="525" loading="eager" decoding="async">
        <p class="bl-05__badge"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 6v4.2l2.8 1.7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span><span class="bl-05__srOnly">Total time </span>40 min</span></p>
        <p class="bl-05__diff">Medium</p>
      </div>
      <div class="bl-05__body">
        <p class="bl-05__cat">One pan</p>
        <h2 class="bl-05__title"><a href="#">Butter-basted sirloin with charred shallots</a></h2>
        <p class="bl-05__note">Rest it longer than you think. Nine minutes, not three.</p>
        <dl class="bl-05__stats">
          <div><dt>Prep</dt><dd>12 min</dd></div>
          <div><dt>Cook</dt><dd>18 min</dd></div>
          <div><dt>Serves</dt><dd>2</dd></div>
        </dl>
      </div>
    </article>

    <article class="bl-05__card" data-diff="easy">
      <div class="bl-05__media">
        <img src="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="Colourful grain salad in a shallow bowl" width="700" height="525" loading="lazy" decoding="async">
        <p class="bl-05__badge"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 6v4.2l2.8 1.7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span><span class="bl-05__srOnly">Total time </span>18 min</span></p>
        <p class="bl-05__diff">Easy</p>
      </div>
      <div class="bl-05__body">
        <p class="bl-05__cat">Batch cook</p>
        <h2 class="bl-05__title"><a href="#">Cold farro salad that survives three lunches</a></h2>
        <p class="bl-05__note">Dress it warm; it drinks the vinaigrette instead of sitting in it.</p>
        <dl class="bl-05__stats">
          <div><dt>Prep</dt><dd>8 min</dd></div>
          <div><dt>Cook</dt><dd>10 min</dd></div>
          <div><dt>Serves</dt><dd>4</dd></div>
        </dl>
      </div>
    </article>

    <article class="bl-05__card" data-diff="hard">
      <div class="bl-05__media">
        <img src="https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="Overhead flat lay of a plated dinner" width="700" height="525" loading="lazy" decoding="async">
        <p class="bl-05__badge"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 6v4.2l2.8 1.7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span><span class="bl-05__srOnly">Total time </span>55 min</span></p>
        <p class="bl-05__diff">Ambitious</p>
      </div>
      <div class="bl-05__body">
        <p class="bl-05__cat">Sunday</p>
        <h2 class="bl-05__title"><a href="#">Braised fennel with orange and fried breadcrumbs</a></h2>
        <p class="bl-05__note">Worth the extra pan for the breadcrumbs. Genuinely.</p>
        <dl class="bl-05__stats">
          <div><dt>Prep</dt><dd>15 min</dd></div>
          <div><dt>Cook</dt><dd>40 min</dd></div>
          <div><dt>Serves</dt><dd>4</dd></div>
        </dl>
      </div>
    </article>

    <article class="bl-05__card" data-diff="easy">
      <div class="bl-05__media">
        <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="Flat white coffee in a ceramic cup" width="700" height="525" loading="lazy" decoding="async">
        <p class="bl-05__badge"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 6v4.2l2.8 1.7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span><span class="bl-05__srOnly">Total time </span>6 min</span></p>
        <p class="bl-05__diff">Easy</p>
      </div>
      <div class="bl-05__body">
        <p class="bl-05__cat">Basics</p>
        <h2 class="bl-05__title"><a href="#">The only cold brew ratio worth memorising</a></h2>
        <p class="bl-05__note">1:8 overnight, then cut it. Everything else is preference.</p>
        <dl class="bl-05__stats">
          <div><dt>Prep</dt><dd>6 min</dd></div>
          <div><dt>Steep</dt><dd>14 hr</dd></div>
          <div><dt>Makes</dt><dd>1 L</dd></div>
        </dl>
      </div>
    </article>

    <article class="bl-05__card" data-diff="medium">
      <div class="bl-05__media">
        <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="Table set for a shared meal with several dishes" width="700" height="525" loading="lazy" decoding="async">
        <p class="bl-05__badge"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 6v4.2l2.8 1.7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span><span class="bl-05__srOnly">Total time </span>35 min</span></p>
        <p class="bl-05__diff">Medium</p>
      </div>
      <div class="bl-05__body">
        <p class="bl-05__cat">For friends</p>
        <h2 class="bl-05__title"><a href="#">Six small plates from one shopping list</a></h2>
        <p class="bl-05__note">Built around one bunch of herbs and a tin of beans.</p>
        <dl class="bl-05__stats">
          <div><dt>Prep</dt><dd>20 min</dd></div>
          <div><dt>Cook</dt><dd>15 min</dd></div>
          <div><dt>Serves</dt><dd>6</dd></div>
        </dl>
      </div>
    </article>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Gabarito:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@1,6..72,400&display=swap');

.bl-05 {
  --bg: #fdf8f3;
  --surface: #ffffff;
  --text: #1d1611;
  --muted: #7b6d60;
  --line: #ecdfd2;
  --acc: #b45309;
  --chip: #111827;
  --chip-fg: #ffffff;
  --ratio: 4/3;
  --easy: #15803d;
  --medium: #b45309;
  --hard: #b91c1c;
  --sans: "Gabarito",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-05 {
    --bg: oklch(97.5% .015 70);
    --surface: oklch(100% 0 0);
    --text: oklch(19% .02 50);
    --muted: oklch(52% .025 55);
    --line: oklch(90% .025 70);
    --acc: oklch(52% .13 60);
    --easy: oklch(50% .14 145);
    --medium: oklch(55% .14 65);
    --hard: oklch(50% .18 25);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-05:not([data-theme="light"]) {
    --bg: #14100d;
    --surface: #1d1815;
    --text: #f7f1ea;
    --muted: #a8998a;
    --line: #2f2822;
    --acc: #fbbf24;
    --chip: #fafaf9;
    --chip-fg: #14100d;
    --easy: #4ade80;
    --medium: #fbbf24;
    --hard: #f87171;
  }
}

.bl-05[data-theme="dark"] {
  --bg: #14100d;
  --surface: #1d1815;
  --text: #f7f1ea;
  --muted: #a8998a;
  --line: #2f2822;
  --acc: #fbbf24;
  --chip: #fafaf9;
  --chip-fg: #14100d;
  --easy: #4ade80;
  --medium: #fbbf24;
  --hard: #f87171;
}

.bl-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-05,
.bl-05 *,
.bl-05 *::before,
.bl-05 *::after {
  box-sizing: border-box;
}

.bl-05 a {
  color: inherit;
  text-decoration: none;
}

.bl-05 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 3px;
}

.bl-05__srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bl-05__head {
  max-width: 78rem;
  margin-inline: auto;
  padding: clamp(2.5rem,7vw,5rem) clamp(1.25rem,4vw,3rem) clamp(1.5rem,3vw,2.5rem);
  display: grid;
  gap: 1rem;
}

.bl-05__eyebrow {
  margin: 0;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
}

.bl-05__head h1 {
  margin: 0;
  font-size: clamp(2rem,5vw,3.5rem);
  font-weight: 600;
  line-height: 1.02;
  letter-spacing: -.03em;
  max-width: 24ch;
  text-wrap: balance;
}

.bl-05__lede {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(1.0625rem,1.6vw,1.25rem);
  line-height: 1.6;
  color: var(--muted);
  max-width: 56ch;
  text-wrap: pretty;
}

.bl-05__filters {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin-top: .5rem;
}

.bl-05__filters button {
  min-height: 2.75rem;
  padding: 0 1rem;
  border-radius: 999px;
  cursor: pointer;
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--text);
  font-family: inherit;
  font-size: .875rem;
  font-weight: 500;
  transition: background .18s ease, border-color .18s ease, color .18s ease;
}

.bl-05__filters button:hover {
  border-color: var(--acc);
  color: var(--acc);
}

.bl-05__filters button[aria-pressed="true"] {
  background: var(--chip);
  border-color: var(--chip);
  color: var(--chip-fg);
}

.bl-05__grid {
  display: grid;
  gap: clamp(1.25rem,2.5vw,2rem);
  grid-template-columns: repeat(auto-fill,minmax(min(100%,17rem),1fr));
  max-width: 78rem;
  margin-inline: auto;
  padding: 0 clamp(1.25rem,4vw,3rem) clamp(3rem,7vw,6rem);
}

.bl-05__card {
  container-type: inline-size;
  position: relative;
  display: grid;
  gap: 0;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
  overflow: hidden;
  transition: translate .3s cubic-bezier(.16,1,.3,1), box-shadow .3s cubic-bezier(.16,1,.3,1), border-color .3s ease;
}

.bl-05__card:has(a:hover),
.bl-05__card:has(a:focus-visible) {
  translate: 0 -.35rem;
  border-color: color-mix(in oklab,var(--acc) 40%,var(--line));
  box-shadow: 0 1.5rem 2.5rem -1rem color-mix(in oklab,var(--text) 22%,transparent);
}

.bl-05__media {
  position: relative;
  aspect-ratio: var(--ratio);
  overflow: hidden;
  background: var(--line);
}

.bl-05__media img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: scale .6s cubic-bezier(.16,1,.3,1);
}

.bl-05__card:has(a:hover) .bl-05__media img {
  scale: 1.06;
}

.bl-05__badge,
.bl-05__diff {
  position: absolute;
  z-index: 2;
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  padding: .4rem .6rem;
  border-radius: 999px;
  font-size: .75rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.bl-05__badge {
  inset-block-start: .75rem;
  inset-inline-start: .75rem;
  background: color-mix(in oklab,var(--chip) 88%,transparent);
  color: var(--chip-fg);
}

@supports (backdrop-filter: blur(4px)) {
  .bl-05__badge {
    background: color-mix(in oklab,var(--chip) 72%,transparent);
    backdrop-filter: blur(8px) saturate(1.3);
  }
}

.bl-05__badge svg {
  width: .9rem;
  height: .9rem;
}

.bl-05__diff {
  inset-block-start: .75rem;
  inset-inline-end: .75rem;
  background: var(--surface);
  color: var(--easy);
  font-size: .6875rem;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.bl-05__card[data-diff="medium"] .bl-05__diff {
  color: var(--medium);
}

.bl-05__card[data-diff="hard"] .bl-05__diff {
  color: var(--hard);
}

.bl-05__body {
  display: grid;
  gap: .5rem;
  padding: clamp(1rem,2vw,1.25rem);
}

.bl-05__cat {
  margin: 0;
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-05__title {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-05__title a::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  border-radius: inherit;
}

.bl-05__note {
  margin: 0;
  font-family: var(--serif);
  font-style: italic;
  font-size: .9375rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-05__stats {
  display: flex;
  gap: 1.25rem;
  margin: .5rem 0 0;
  padding-top: .75rem;
  border-top: 1px solid var(--line);
}

.bl-05__stats div {
  display: grid;
  gap: .1rem;
}

.bl-05__stats dt {
  font-size: .625rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-05__stats dd {
  margin: 0;
  font-size: .875rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

@container (max-width: 20rem) {
  .bl-05__title {
    font-size: 1.125rem;
  }

  .bl-05__stats {
    flex-wrap: wrap;
    gap: .5rem 1rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-05 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .bl-05__card {
    border: 1px solid CanvasText;
  }

  .bl-05__filters button[aria-pressed="true"] {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}
```
