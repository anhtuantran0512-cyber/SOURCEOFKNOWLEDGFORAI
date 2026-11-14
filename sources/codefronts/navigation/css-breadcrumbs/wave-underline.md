---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/wave-underline/"
title: "Editorial Blog Breadcrumb with Animated Wave Underline Hover"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "Editorial publishing breadcrumb in the spirit of Medium, Substack, and NYT — warm cream paper, muted ink serif type, and a signature hover flourish where an…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Blog Breadcrumb with Animated Wave Underline Hover
Source: https://codefronts.com/navigation/css-breadcrumbs/wave-underline/

Editorial publishing breadcrumb in the spirit of Medium, Substack, and NYT — warm cream paper, muted ink serif type, and a signature hover flourish where an inline SVG wave underline draws itself beneath each crumb like a printer's flourish finishing on the page.
## HTML
```html
<section class="bc-21" aria-label="Editorial blog breadcrumb with wave underline demo">
      <article class="bc-21__frame">
        <nav aria-label="Breadcrumb" class="bc-21__nav">
          <ol class="bc-21__list">
            <li class="bc-21__item">
              <a class="bc-21__link" href="#">
                <span class="bc-21__label">Home</span>
                <svg class="bc-21__wave" aria-hidden="true" viewBox="0 0 60 6" preserveAspectRatio="none">
                  <path d="M0 3 Q 15 0, 30 3 T 60 3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" pathLength="100" vector-effect="non-scaling-stroke"/>
                </svg>
              </a>
            </li>
            <li class="bc-21__item">
              <a class="bc-21__link" href="#">
                <span class="bc-21__label">Style</span>
                <svg class="bc-21__wave" aria-hidden="true" viewBox="0 0 60 6" preserveAspectRatio="none">
                  <path d="M0 3 Q 15 0, 30 3 T 60 3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" pathLength="100" vector-effect="non-scaling-stroke"/>
                </svg>
              </a>
            </li>
            <li class="bc-21__item">
              <a class="bc-21__link" href="#">
                <span class="bc-21__label">Fashion</span>
                <svg class="bc-21__wave" aria-hidden="true" viewBox="0 0 60 6" preserveAspectRatio="none">
                  <path d="M0 3 Q 15 0, 30 3 T 60 3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" pathLength="100" vector-effect="non-scaling-stroke"/>
                </svg>
              </a>
            </li>
            <li class="bc-21__item" aria-current="page">
              <span class="bc-21__link bc-21__link--current">
                <span class="bc-21__label">The Return of Tailored Denim</span>
              </span>
            </li>
          </ol>
        </nav>
        <h1 class="bc-21__headline">The Return of Tailored Denim</h1>
        <p class="bc-21__dek">A quiet revival of pressed seams and structured silhouettes, filed under Style / Fashion.</p>
      </article>
    </section>
```
## CSS
```css
.bc-21 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(2rem, 6vw, 4rem) clamp(1rem, 4vw, 2.5rem);
  background: oklch(0.97 0.01 85);
  font-family: Charter, 'Iowan Old Style', 'Palatino Linotype', Georgia, 'Times New Roman', serif;
  color: oklch(0.28 0.02 60);
  -webkit-font-smoothing: antialiased;
  --bc-21-ink: oklch(0.42 0.02 60);
  --bc-21-ink-strong: oklch(0.22 0.02 60);
  --bc-21-accent: oklch(0.55 0.14 30);
  --bc-21-draw: 420ms;
  --bc-21-ease: cubic-bezier(0.22, 0.61, 0.36, 1);
}

.bc-21 *,
.bc-21 *::before,
.bc-21 *::after {
  box-sizing: border-box;
}

.bc-21__frame {
  width: 100%;
  max-width: 62ch;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.bc-21__nav {
  font-size: 0.9375rem;
  line-height: 1.4;
}

.bc-21__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.15rem 0.35rem;
}

.bc-21__item {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  color: var(--bc-21-ink);
}

.bc-21__item + .bc-21__item::before {
  content: "·";
  margin: 0 0.55rem 0 0.2rem;
  color: oklch(0.62 0.02 60);
  font-size: 1.05em;
  line-height: 1;
  transform: translateY(-0.05em);
}

.bc-21__link {
  position: relative;
  display: inline-flex;
  align-items: center;
  padding: 0.6rem 0.15rem;
  min-height: 44px;
  color: var(--bc-21-ink);
  text-decoration: none;
  font-style: italic;
  letter-spacing: 0.005em;
  transition: color 220ms var(--bc-21-ease);
  border-radius: 2px;
}

.bc-21__label {
  position: relative;
  display: inline-block;
}

.bc-21__wave {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0.35rem;
  width: 100%;
  height: 6px;
  color: var(--bc-21-accent);
  overflow: visible;
  pointer-events: none;
}

.bc-21__wave path {
  stroke-dasharray: 100;
  stroke-dashoffset: 100;
  opacity: 0;
  transition: stroke-dashoffset var(--bc-21-draw) var(--bc-21-ease), opacity 180ms var(--bc-21-ease);
}

.bc-21__link:hover,
.bc-21__link:focus-visible {
  color: var(--bc-21-ink-strong);
}

.bc-21__link:hover .bc-21__wave path,
.bc-21__link:focus-visible .bc-21__wave path {
  stroke-dashoffset: 0;
  opacity: 1;
}

.bc-21__link:focus-visible {
  outline: 2px solid var(--bc-21-accent);
  outline-offset: 3px;
}

.bc-21__link--current {
  color: var(--bc-21-ink-strong);
  font-style: normal;
  font-weight: 600;
  cursor: default;
}

.bc-21__link--current .bc-21__wave {
  display: none;
}

.bc-21__headline {
  margin: 0.5rem 0 0;
  font-size: clamp(1.75rem, 4vw, 2.4rem);
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -0.01em;
  color: var(--bc-21-ink-strong);
}

.bc-21__dek {
  margin: 0;
  font-size: 1rem;
  font-style: italic;
  color: var(--bc-21-ink);
  line-height: 1.55;
  max-width: 48ch;
}

@media (prefers-reduced-motion: reduce) {
  .bc-21__wave path {
    transition: opacity 160ms linear;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
  }

  .bc-21__link {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .bc-21 {
    background: oklch(0.19 0.01 70);
    color: oklch(0.82 0.02 80);
    --bc-21-ink: oklch(0.74 0.02 80);
    --bc-21-ink-strong: oklch(0.93 0.02 85);
    --bc-21-accent: oklch(0.78 0.14 60);
  }

  .bc-21__item + .bc-21__item::before {
    color: oklch(0.55 0.02 70);
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS transitions stroke-dashoffset from 100 to 0 on :hover and :focus-visible, drawing the wave underline in beneath each crumb. */
```
