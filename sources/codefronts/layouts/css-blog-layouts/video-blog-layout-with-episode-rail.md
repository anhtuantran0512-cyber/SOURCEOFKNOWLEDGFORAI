---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/video-blog-layout-with-episode-rail/"
title: "Video Blog Layout with Episode Rail"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "The two-pane video page: a 16:9 player that never letterboxes, a description block with a real expand/collapse using <details>, and an up-next rail whose…"
has_js: "true"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Blog Layout with Episode Rail
Source: https://codefronts.com/layouts/css-blog-layouts/video-blog-layout-with-episode-rail/

The two-pane video page: a 16:9 player that never letterboxes, a description block with a real expand/collapse using <details>, and an up-next rail whose active row is driven by one data attribute. Selecting an episode swaps the poster, title and metadata in place — twelve lines of JavaScript, no framework, and the rail becomes a horizontal scroll-snap strip on mobile.
## HTML
```html
<div class="bl-13">
  <header class="bl-13__top">
    <a class="bl-13__brand" href="#">Build Log<span aria-hidden="true">▸</span></a>
    <nav class="bl-13__topNav" aria-label="Sections"><a href="#" aria-current="page">Episodes</a><a href="#">Series</a><a href="#">Notes</a></nav>
    <a class="bl-13__sub" href="#">Subscribe · 24.8k</a>
  </header>

  <main class="bl-13__main">
    <div class="bl-13__player">
      <div class="bl-13__stage" data-state="paused">
        <img data-poster src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1600&amp;q=70&amp;auto=format&amp;fit=crop" alt="Code editor open on a laptop beside a notebook" width="1600" height="900" loading="eager" fetchpriority="high" decoding="async">
        <button class="bl-13__playBig" type="button" data-play aria-pressed="false">
          <svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path class="bl-13__tri" d="M12 9.5 23 16l-11 6.5z" fill="currentColor"/><g class="bl-13__pause"><rect x="11" y="9.5" width="3.4" height="13" rx="1.2" fill="currentColor"/><rect x="17.6" y="9.5" width="3.4" height="13" rx="1.2" fill="currentColor"/></g></svg>
          <span class="bl-13__srOnly" data-play-label>Play episode</span>
        </button>
        <div class="bl-13__scrub" aria-hidden="true"><i></i></div>
        <p class="bl-13__stamp" data-dur>18:24</p>
      </div>

      <div class="bl-13__meta">
        <p class="bl-13__series" data-series>Series 3 · Episode 07</p>
        <h1 data-title>Rebuilding our design system without a rewrite</h1>
        <div class="bl-13__statsRow">
          <p><strong data-views>41,208</strong> views · <time datetime="2026-08-03">3 Aug 2026</time></p>
          <div class="bl-13__buttons">
            <button type="button" aria-pressed="false"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M6 9.5 9.5 4h.8a1.7 1.7 0 0 1 1.6 2.2L11.4 8h3.1A1.5 1.5 0 0 1 16 9.8l-.9 4.4A2 2 0 0 1 13.1 16H6z" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><rect x="3" y="9" width="3" height="7" rx="1" fill="none" stroke="currentColor" stroke-width="1.4"/></svg><span>1.2k</span></button>
            <button type="button"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 13V3m0 0L6.5 6.5M10 3l3.5 3.5M4 13v3h12v-3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Share</span></button>
            <button type="button" aria-pressed="false"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M6 3h8v14l-4-3.2L6 17z" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg><span>Save</span></button>
          </div>
        </div>

        <details class="bl-13__desc">
          <summary><span>Episode notes</span><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5 8l5 4.5L15 8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></summary>
          <div class="bl-13__descBody">
            <p>We had eleven button variants, four of them undocumented, and a token file nobody trusted. This episode walks through the audit that came before any code: how we counted real usage in production, which components we deliberately left alone, and the two-week window where both systems ran side by side.</p>
            <p>Timestamps and the full component inventory are in the written companion post. The migration script shown at 11:40 is open source.</p>
            <ul>
              <li><a href="#">Companion article — the audit spreadsheet</a></li>
              <li><a href="#">Repository — codemod and token diff</a></li>
              <li><a href="#">Previous episode — measuring component usage</a></li>
            </ul>
          </div>
        </details>
      </div>
    </div>

    <aside class="bl-13__up" aria-labelledby="bl-13-up-h">
      <h2 class="bl-13__upHead" id="bl-13-up-h">Up next in Series 3</h2>
      <ol class="bl-13__rail">
        <li><a class="bl-13__row" href="#" data-active="true" data-ep="Series 3 · Episode 07" data-t="Rebuilding our design system without a rewrite" data-d="18:24" data-v="41,208" data-src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1600&amp;q=70&amp;auto=format&amp;fit=crop">
          <span class="bl-13__thumb"><img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400&amp;q=60&amp;auto=format&amp;fit=crop" alt="" width="400" height="225" loading="lazy" decoding="async"><i>18:24</i></span>
          <span class="bl-13__rowText"><strong>Rebuilding our design system without a rewrite</strong><span>Ep 07 · 41,208 views</span></span>
        </a></li>
        <li><a class="bl-13__row" href="#" data-ep="Series 3 · Episode 08" data-t="The codemod that migrated 1,400 components" data-d="22:09" data-v="12,940" data-src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1600&amp;q=70&amp;auto=format&amp;fit=crop">
          <span class="bl-13__thumb"><img src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=400&amp;q=60&amp;auto=format&amp;fit=crop" alt="" width="400" height="225" loading="lazy" decoding="async"><i>22:09</i></span>
          <span class="bl-13__rowText"><strong>The codemod that migrated 1,400 components</strong><span>Ep 08 · 12,940 views</span></span>
        </a></li>
        <li><a class="bl-13__row" href="#" data-ep="Series 3 · Episode 09" data-t="Deleting a component in a 60-person company" data-d="14:51" data-v="9,105" data-src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1600&amp;q=70&amp;auto=format&amp;fit=crop">
          <span class="bl-13__thumb"><img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400&amp;q=60&amp;auto=format&amp;fit=crop" alt="" width="400" height="225" loading="lazy" decoding="async"><i>14:51</i></span>
          <span class="bl-13__rowText"><strong>Deleting a component in a 60-person company</strong><span>Ep 09 · 9,105 views</span></span>
        </a></li>
        <li><a class="bl-13__row" href="#" data-ep="Series 3 · Episode 10" data-t="Design tokens: what we stopped naming" data-d="26:37" data-v="7,412" data-src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&amp;q=70&amp;auto=format&amp;fit=crop">
          <span class="bl-13__thumb"><img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&amp;q=60&amp;auto=format&amp;fit=crop" alt="" width="400" height="225" loading="lazy" decoding="async"><i>26:37</i></span>
          <span class="bl-13__rowText"><strong>Design tokens: what we stopped naming</strong><span>Ep 10 · 7,412 views</span></span>
        </a></li>
        <li><a class="bl-13__row" href="#" data-ep="Series 3 · Episode 11" data-t="Six months later: what broke anyway" data-d="19:02" data-v="5,880" data-src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1600&amp;q=70&amp;auto=format&amp;fit=crop">
          <span class="bl-13__thumb"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&amp;q=60&amp;auto=format&amp;fit=crop" alt="" width="400" height="225" loading="lazy" decoding="async"><i>19:02</i></span>
          <span class="bl-13__rowText"><strong>Six months later: what broke anyway</strong><span>Ep 11 · 5,880 views</span></span>
        </a></li>
      </ol>
    </aside>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

.bl-13 {
  --bg: #0b0b0d;
  --surface: #15161a;
  --text: #f2f3f5;
  --muted: #9497a1;
  --line: #24262c;
  --acc: #ef4444;
  --acc-fg: #ffffff;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-13 {
    --bg: oklch(14% .006 270);
    --surface: oklch(20% .008 270);
    --text: oklch(96% .004 270);
    --muted: oklch(66% .012 270);
    --line: oklch(27% .01 270);
    --acc: oklch(60% .22 25);
  }
}

@media (prefers-color-scheme: light) {
  .bl-13:not([data-theme="dark"]) {
    --bg: #ffffff;
    --surface: #f4f5f7;
    --text: #101114;
    --muted: #5f636d;
    --line: #e3e5ea;
  }
}

.bl-13[data-theme="light"] {
  --bg: #ffffff;
  --surface: #f4f5f7;
  --text: #101114;
  --muted: #5f636d;
  --line: #e3e5ea;
}

.bl-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-13,
.bl-13 *,
.bl-13 *::before,
.bl-13 *::after {
  box-sizing: border-box;
}

.bl-13 a {
  color: inherit;
  text-decoration: none;
}

.bl-13 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.bl-13 img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--line);
}

.bl-13__srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bl-13__top {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem 1.5rem;
  padding: .85rem clamp(1rem,3vw,2rem);
  border-bottom: 1px solid var(--line);
}

.bl-13__brand {
  font-size: 1.125rem;
  font-weight: 800;
  letter-spacing: -.03em;
}

.bl-13__brand span {
  color: var(--acc);
  margin-inline-start: .25em;
}

.bl-13__topNav {
  display: flex;
  gap: .25rem;
  margin-inline-end: auto;
}

.bl-13__topNav a {
  display: grid;
  place-items: center;
  min-height: 2.5rem;
  padding: 0 .8rem;
  border-radius: 999px;
  font-size: .8125rem;
  font-weight: 600;
  color: var(--muted);
}

.bl-13__topNav a:hover {
  color: var(--text);
  background: var(--surface);
}

.bl-13__topNav a[aria-current="page"] {
  color: var(--text);
  background: var(--surface);
}

.bl-13__sub {
  display: grid;
  place-items: center;
  min-height: 2.5rem;
  padding: 0 1rem;
  border-radius: 999px;
  background: var(--acc);
  color: var(--acc-fg);
  font-size: .8125rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.bl-13__main {
  display: grid;
  gap: clamp(1.25rem,2.5vw,2rem);
  align-items: start;
  grid-template-columns: minmax(0,1fr) clamp(18rem,26vw,24rem);
  max-width: 96rem;
  margin-inline: auto;
  padding: clamp(1rem,2.5vw,2rem) clamp(1rem,3vw,2rem) clamp(3rem,6vw,5rem);
}

.bl-13__player {
  display: grid;
  gap: 1.25rem;
  min-width: 0;
}

.bl-13__stage {
  position: relative;
  aspect-ratio: 16/9;
  max-height: calc(100svh - 13rem);
  width: 100%;
  margin-inline: auto;
  border-radius: 1rem;
  overflow: hidden;
  background: #000;
  isolation: isolate;
}

.bl-13__stage img {
  position: absolute;
  inset: 0;
  transition: opacity .3s ease, scale .6s cubic-bezier(.16,1,.3,1);
}

.bl-13__stage[data-state="playing"] img {
  opacity: .55;
  scale: 1.02;
}

.bl-13__playBig {
  position: absolute;
  inset: 0;
  margin: auto;
  width: 5rem;
  height: 5rem;
  border-radius: 50%;
  cursor: pointer;
  display: grid;
  place-items: center;
  border: 0;
  color: #fff;
  background: color-mix(in oklab,#000 45%,transparent);
  transition: scale .25s cubic-bezier(.16,1,.3,1), background .25s ease;
}

@supports (backdrop-filter: blur(4px)) {
  .bl-13__playBig {
    backdrop-filter: blur(10px) saturate(1.4);
  }
}

.bl-13__playBig:hover {
  scale: 1.07;
  background: var(--acc);
}

.bl-13__playBig svg {
  width: 2.25rem;
  height: 2.25rem;
}

.bl-13__pause {
  opacity: 0;
}

.bl-13__stage[data-state="playing"] .bl-13__tri {
  opacity: 0;
}

.bl-13__stage[data-state="playing"] .bl-13__pause {
  opacity: 1;
}

.bl-13__scrub {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  height: 3px;
  background: rgba(255,255,255,.22);
}

.bl-13__scrub i {
  display: block;
  height: 100%;
  width: 100%;
  background: var(--acc);
  transform-origin: left;
  scale: .18 1;
}

.bl-13__stage[data-state="playing"] .bl-13__scrub i {
  animation: bl-13-scrub 40s linear forwards;
}

@keyframes bl-13-scrub {
  from {
    scale: .18 1;
  }

  to {
    scale: 1 1;
  }
}

.bl-13__stamp {
  position: absolute;
  inset-block-end: .85rem;
  inset-inline-end: .85rem;
  margin: 0;
  padding: .2rem .45rem;
  border-radius: .25rem;
  background: rgba(0,0,0,.75);
  color: #fff;
  font-size: .75rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.bl-13__meta {
  display: grid;
  gap: .85rem;
}

.bl-13__series {
  margin: 0;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-13__meta h1 {
  margin: 0;
  font-size: clamp(1.375rem,3vw,2.125rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -.032em;
  text-wrap: balance;
}

.bl-13__statsRow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: .75rem 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--line);
}

.bl-13__statsRow p {
  margin: 0;
  font-size: .875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-13__statsRow strong {
  color: var(--text);
  font-weight: 700;
}

.bl-13__buttons {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}

.bl-13__buttons button {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  padding: 0 .85rem;
  cursor: pointer;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--surface);
  color: var(--text);
  font-family: inherit;
  font-size: .8125rem;
  font-weight: 600;
  transition: border-color .18s ease, color .18s ease;
}

.bl-13__buttons button svg {
  width: 1.05rem;
  height: 1.05rem;
}

.bl-13__buttons button:hover {
  border-color: color-mix(in oklab,var(--text) 30%,var(--line));
}

.bl-13__buttons button[aria-pressed="true"] {
  color: var(--acc);
  border-color: var(--acc);
}

.bl-13__desc {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: .875rem;
  overflow: hidden;
}

.bl-13__desc summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  cursor: pointer;
  min-height: 3rem;
  padding: 0 1.1rem;
  font-size: .875rem;
  font-weight: 700;
  list-style: none;
}

.bl-13__desc summary::-webkit-details-marker {
  display: none;
}

.bl-13__desc summary svg {
  width: 1.15rem;
  height: 1.15rem;
  color: var(--muted);
  transition: rotate .25s cubic-bezier(.16,1,.3,1);
}

.bl-13__desc[open] summary svg {
  rotate: 180deg;
}

.bl-13__descBody {
  padding: 0 1.1rem 1.25rem;
  display: grid;
  gap: .85rem;
}

.bl-13__descBody p {
  margin: 0;
  font-size: .9375rem;
  line-height: 1.7;
  color: var(--muted);
  max-width: 70ch;
  text-wrap: pretty;
}

.bl-13__descBody ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .35rem;
}

.bl-13__descBody li a {
  font-size: .875rem;
  font-weight: 600;
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: .2em;
}

@supports (interpolate-size: allow-keywords) {
  @media (prefers-reduced-motion: no-preference) {
    .bl-13 {
      interpolate-size: allow-keywords;
    }

    .bl-13__desc::details-content {
      block-size: 0;
      overflow: hidden;
      opacity: 0;
      transition: block-size .35s cubic-bezier(.16,1,.3,1), opacity .3s ease, content-visibility .35s allow-discrete;
    }

    .bl-13__desc[open]::details-content {
      block-size: auto;
      opacity: 1;
    }
  }
}

.bl-13__up {
  display: grid;
  gap: .75rem;
  min-width: 0;
}

.bl-13__upHead {
  margin: 0;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-13__rail {
  display: grid;
  gap: .5rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.bl-13__row {
  display: grid;
  grid-template-columns: 9rem minmax(0,1fr);
  gap: .75rem;
  align-items: start;
  padding: .5rem;
  border-radius: .75rem;
  border: 1px solid transparent;
  transition: background .2s ease, border-color .2s ease;
}

.bl-13__row:hover {
  background: var(--surface);
  border-color: var(--line);
}

.bl-13__row[data-active="true"] {
  background: var(--surface);
  border-color: color-mix(in oklab,var(--acc) 45%,var(--line));
}

.bl-13__thumb {
  position: relative;
  display: block;
  aspect-ratio: 16/9;
  border-radius: .5rem;
  overflow: hidden;
}

.bl-13__thumb i {
  position: absolute;
  inset-block-end: .25rem;
  inset-inline-end: .25rem;
  padding: .1rem .3rem;
  border-radius: .2rem;
  background: rgba(0,0,0,.78);
  color: #fff;
  font-size: .625rem;
  font-style: normal;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.bl-13__rowText {
  display: grid;
  gap: .25rem;
  min-width: 0;
}

.bl-13__rowText strong {
  font-size: .875rem;
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.bl-13__rowText span {
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-13__row[data-active="true"] .bl-13__rowText strong {
  color: var(--acc);
}

@media (max-width: 62rem) {
  .bl-13__main {
    grid-template-columns: minmax(0,1fr);
  }

  .bl-13__rail {
    grid-auto-flow: column;
    grid-auto-columns: min(80vw,20rem);
    overflow-x: auto;
    scroll-snap-type: x proximity;
    padding-bottom: .5rem;
    scrollbar-width: thin;
  }

  .bl-13__rail li {
    scroll-snap-align: start;
  }

  .bl-13__row {
    grid-template-columns: minmax(0,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-13 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .bl-13__row[data-active="true"] {
    forced-color-adjust: none;
    outline: 2px solid Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.bl-13');
  if (!root) return;
  const stage = root.querySelector('.bl-13__stage');
  const poster = root.querySelector('[data-poster]');
  const play = root.querySelector('[data-play]');
  const playLabel = root.querySelector('[data-play-label]');
  const set = (sel, val) => { const el = root.querySelector(sel); if (el) el.textContent = val; };
  play.addEventListener('click', () => {
    const on = stage.dataset.state !== 'playing';
    stage.dataset.state = on ? 'playing' : 'paused';
    play.setAttribute('aria-pressed', String(on));
    playLabel.textContent = on ? 'Pause episode' : 'Play episode';
  });
  root.querySelectorAll('.bl-13__row').forEach((row) => {
    row.addEventListener('click', (e) => {
      e.preventDefault();
      root.querySelectorAll('.bl-13__row').forEach((r) => r.removeAttribute('data-active'));
      row.dataset.active = 'true';
      poster.src = row.dataset.src;
      set('[data-title]', row.dataset.t); set('[data-series]', row.dataset.ep);
      set('[data-dur]', row.dataset.d); set('[data-views]', row.dataset.v);
      stage.dataset.state = 'paused'; play.setAttribute('aria-pressed', 'false');
      playLabel.textContent = 'Play episode';
    });
  });
})();
```
