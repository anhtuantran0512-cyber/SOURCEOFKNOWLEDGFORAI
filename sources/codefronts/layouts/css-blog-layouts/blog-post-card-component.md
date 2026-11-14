---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/blog-post-card-component/"
title: "Blog Post Card Component"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "One card, engineered properly — because the card is the component you will paste into forty templates."
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blog Post Card Component
Source: https://codefronts.com/layouts/css-blog-layouts/blog-post-card-component/

One card, engineered properly — because the card is the component you will paste into forty templates. Author row, reading time, tag chips, a bookmark toggle that works with zero JavaScript (a hidden checkbox), and a container query that re-lays the whole thing out based on the slot it lands in rather than the viewport. Drop it in a sidebar and it stacks; drop it in a main column and it goes horizontal.
## HTML
```html
<div class="bl-17">
  <div class="bl-17__stage">
    <p class="bl-17__hint">One card component. Resize the frame — it re-lays out from its <em>container</em>, not the viewport.</p>

    <div class="bl-17__slot">
      <article class="bl-17__card">
        <div class="bl-17__media">
          <img src="https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="A notebook, laptop and coffee on a wooden desk" width="800" height="600" loading="lazy" decoding="async">
          <p class="bl-17__kicker">Craft</p>
        </div>

        <div class="bl-17__body">
          <div class="bl-17__tags">
            <a href="#">CSS</a><a href="#">Architecture</a><a href="#">Components</a>
          </div>
          <h2 class="bl-17__title"><a href="#">Stop writing breakpoints: the component-owned layout pattern</a></h2>
          <p class="bl-17__excerpt">Container queries move the decision from the page to the piece. Here is the refactor, the two gotchas, and what it does to your CSS budget.</p>

          <footer class="bl-17__foot">
            <div class="bl-17__author">
              <img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="100" height="100" loading="lazy" decoding="async">
              <p><strong>Lena Ostrowski</strong><span><time datetime="2026-08-07">7 Aug 2026</time> · 9 min read</span></p>
            </div>
            <label class="bl-17__save">
              <input type="checkbox">
              <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M6 3.5h8v13l-4-3.3-4 3.3z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
              <span class="bl-17__srOnly">Save this article for later</span>
            </label>
          </footer>
        </div>
      </article>
    </div>

    <p class="bl-17__note">Whole card is one link (stretched pseudo-element), so there is exactly one entry in the accessibility tree — plus a real checkbox for save, and real links for tags.</p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400;12..96,500;12..96,600;12..96,700&family=Newsreader:opsz,[email protected],400&display=swap');

.bl-17 {
  --bg: #f4f4f2;
  --surface: #ffffff;
  --text: #131313;
  --muted: #6d6d68;
  --line: #e3e3de;
  --acc: #4338ca;
  --save: #ea580c;
  --sans: "Bricolage Grotesque",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-17 {
    --bg: oklch(96.5% .003 100);
    --surface: oklch(100% 0 0);
    --text: oklch(16% .004 100);
    --muted: oklch(51% .008 100);
    --line: oklch(90% .004 100);
    --acc: oklch(45% .2 285);
    --save: oklch(58% .18 45);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-17:not([data-theme="light"]) {
    --bg: #0d0d0e;
    --surface: #161618;
    --text: #f1f1f0;
    --muted: #9c9c98;
    --line: #262629;
    --acc: #a5b4fc;
    --save: #fdba74;
  }
}

.bl-17[data-theme="dark"] {
  --bg: #0d0d0e;
  --surface: #161618;
  --text: #f1f1f0;
  --muted: #9c9c98;
  --line: #262629;
  --acc: #a5b4fc;
  --save: #fdba74;
}

.bl-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-17,
.bl-17 *,
.bl-17 *::before,
.bl-17 *::after {
  box-sizing: border-box;
}

.bl-17 a {
  color: inherit;
  text-decoration: none;
}

.bl-17 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.bl-17__srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bl-17__stage {
  min-height: 100svh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 1.25rem;
  padding: clamp(1.5rem,5vw,4rem);
  max-width: 56rem;
  margin-inline: auto;
}

.bl-17__hint,
.bl-17__note {
  margin: 0;
  max-width: 44ch;
  text-align: center;
  font-size: .8125rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-17__hint em {
  font-family: var(--serif);
  font-style: italic;
  color: var(--text);
}

.bl-17__slot {
  container: card / inline-size;
  width: 100%;
  max-width: 44rem;
}

.bl-17__card {
  position: relative;
  display: grid;
  gap: 0;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  overflow: hidden;
  transition: box-shadow .35s cubic-bezier(.16,1,.3,1), translate .35s cubic-bezier(.16,1,.3,1), border-color .3s ease;
}

.bl-17__card:has(a:hover),
.bl-17__card:has(a:focus-visible) {
  translate: 0 -.3rem;
  box-shadow: 0 1.75rem 3rem -1.5rem color-mix(in oklab,var(--text) 30%,transparent);
  border-color: color-mix(in oklab,var(--acc) 35%,var(--line));
}

.bl-17__card:has(:checked) {
  border-color: color-mix(in oklab,var(--save) 55%,var(--line));
}

.bl-17__media {
  position: relative;
  aspect-ratio: 4/3;
  overflow: hidden;
  background: var(--line);
}

.bl-17__media img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: scale .6s cubic-bezier(.16,1,.3,1);
}

.bl-17__card:has(a:hover) .bl-17__media img {
  scale: 1.05;
}

.bl-17__kicker {
  position: absolute;
  inset-block-start: .75rem;
  inset-inline-start: .75rem;
  z-index: 2;
  margin: 0;
  padding: .3rem .6rem;
  border-radius: 999px;
  background: var(--surface);
  color: var(--acc);
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
}

.bl-17__body {
  display: grid;
  gap: .75rem;
  align-content: start;
  padding: clamp(1.1rem,3cqi,1.6rem);
}

.bl-17__tags {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
}

.bl-17__tags a {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  min-height: 1.75rem;
  padding: 0 .55rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  font-size: .6875rem;
  font-weight: 500;
  color: var(--muted);
  transition: border-color .18s ease, color .18s ease;
}

.bl-17__tags a:hover {
  border-color: var(--acc);
  color: var(--acc);
}

.bl-17__title {
  margin: 0;
  font-size: clamp(1.1875rem,4cqi,1.625rem);
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -.028em;
  text-wrap: balance;
}

.bl-17__title a::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
}

.bl-17__excerpt {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(.9375rem,2.6cqi,1.0625rem);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-17__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-top: .35rem;
  padding-top: .9rem;
  border-top: 1px solid var(--line);
}

.bl-17__author {
  display: flex;
  align-items: center;
  gap: .6rem;
  min-width: 0;
}

.bl-17__author img {
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 50%;
  object-fit: cover;
  flex: 0 0 auto;
  background: var(--line);
}

.bl-17__author p {
  margin: 0;
  display: grid;
  gap: .05rem;
  min-width: 0;
}

.bl-17__author strong {
  font-size: .8125rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.bl-17__author span {
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-17__save {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  width: 2.75rem;
  height: 2.75rem;
  flex: 0 0 auto;
  border-radius: 50%;
  cursor: pointer;
  color: var(--muted);
  transition: background .2s ease, color .2s ease, scale .2s cubic-bezier(.16,1,.3,1);
}

.bl-17__save input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.bl-17__save svg {
  width: 1.25rem;
  height: 1.25rem;
}

.bl-17__save:hover {
  background: color-mix(in oklab,var(--save) 12%,transparent);
  color: var(--save);
  scale: 1.06;
}

.bl-17__save:has(:checked) {
  color: var(--save);
}

.bl-17__save:has(:checked) svg path {
  fill: currentColor;
}

.bl-17__save:has(:focus-visible) {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@container card (min-width: 30rem) {
  .bl-17__card {
    grid-template-columns: 15rem minmax(0,1fr);
    align-items: stretch;
  }

  .bl-17__media {
    aspect-ratio: auto;
    height: 100%;
  }

  .bl-17__body {
    padding: clamp(1.25rem,3cqi,1.75rem);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-17 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .bl-17__card {
    border: 1px solid CanvasText;
  }

  .bl-17__save:has(:checked) {
    forced-color-adjust: none;
    color: Highlight;
  }
}
```
