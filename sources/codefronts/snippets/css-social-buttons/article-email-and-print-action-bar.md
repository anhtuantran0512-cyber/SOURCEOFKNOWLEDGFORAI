---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/article-email-and-print-action-bar/"
title: "Article Email and Print Action Bar"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "The quiet pair of controls every long-form page needs: an email link with subject and body already filled in, and a print button that calls window.print(). A…"
has_js: "true"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Article Email and Print Action Bar
Source: https://codefronts.com/snippets/css-social-buttons/article-email-and-print-action-bar/

The quiet pair of controls every long-form page needs: an email link with subject and body already filled in, and a print button that calls window.print(). A small print stylesheet removes the bar itself from the printed page, which is the detail almost every implementation forgets — readers should not get a row of dead buttons on paper.
## HTML
```html
<div class="soc-10">
  <div class="soc-10__stage">
    <article class="soc-10__card">
      <p class="soc-10__eyebrow">Long read</p>
      <h2 class="soc-10__title">A field guide to accessible motion</h2>
      <p class="soc-10__meta">Jordan Lee · 14 min · Updated August 2026</p>
      <p class="soc-10__body">Motion should explain a change of state, not decorate it. This guide covers the four transitions worth animating, the ones that always hurt comprehension, and how to test both with a real reduced-motion setting.</p>
      <div class="soc-10__bar">
        <a class="soc-10__btn" href="mailto:?subject=A%20field%20guide%20to%20accessible%20motion&amp;body=Thought%20you%27d%20find%20this%20useful%3A%0D%0Ahttps%3A%2F%2Fexample.com%2Faccessible-motion">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.2" width="18" height="13.6" rx="3.4"/><path d="m4.4 8 6.7 4.7a1.6 1.6 0 0 0 1.8 0L19.6 8"/></svg>
          <span>Email this article</span>
        </a>
        <button class="soc-10__btn soc-10__btn--ghost" type="button">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7.5 8.5V4h9v4.5"/><rect x="3.5" y="8.5" width="17" height="7.2" rx="2.6"/><path d="M7.5 13.5h9V20h-9z"/></svg>
          <span>Print</span>
        </button>
      </div>
      <p class="soc-10__live" role="status" aria-live="polite"></p>
    </article>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-10 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-10 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-10:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
  }
}

.soc-10[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
}

.soc-10,
.soc-10 *,
.soc-10 *::before,
.soc-10 *::after {
  box-sizing: border-box;
}

.soc-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-10__card {
  inline-size: min(36rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-10__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-10__title {
  margin: 0 0 .4rem;
  font-size: clamp(1.15rem,1rem + 1vw,1.5rem);
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.soc-10__meta {
  margin: 0 0 1rem;
  font-size: .82rem;
  color: var(--muted);
}

.soc-10__body {
  margin: 0 0 1.6rem;
  font-size: .95rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.soc-10__bar {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  padding-block-start: 1.3rem;
  border-block-start: 1px solid var(--line);
}

.soc-10__btn {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-block-size: 2.875rem;
  padding: 0 1.1rem;
  border: 1px solid var(--fg);
  border-radius: .85rem;
  background: var(--fg);
  color: var(--surface);
  font: inherit;
  font-size: .9rem;
  font-weight: 550;
  text-decoration: none;
  cursor: pointer;
  min-inline-size: 0;
  transition: translate .2s cubic-bezier(.16,1,.3,1), background-color .2s ease, color .2s ease, border-color .2s ease;
}

.soc-10__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.soc-10__btn span {
  min-inline-size: 0;
}

.soc-10__btn:hover {
  translate: 0 -2px;
}

.soc-10__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-10__btn--ghost {
  background: var(--surface);
  color: var(--fg);
  border-color: var(--line);
}

.soc-10__btn--ghost:hover {
  border-color: var(--fg);
  background: color-mix(in oklab,var(--fg) 5%,var(--surface));
}

.soc-10__live {
  margin: .9rem 0 0;
  min-block-size: 1.1rem;
  font-size: .8rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .soc-10__btn {
    transition-duration: 1ms;
  }

  .soc-10__btn:hover {
    translate: none;
  }
}

@media print {
  .soc-10 {
    background: #fff;
    min-height: 0;
  }

  .soc-10__stage {
    min-height: 0;
    padding: 0;
    display: block;
  }

  .soc-10__card {
    inline-size: auto;
    border: 0;
    box-shadow: none;
    padding: 0;
  }

  .soc-10__bar,
    .soc-10__live {
    display: none;
  }

  .soc-10__body,
    .soc-10__meta {
    color: #222;
  }
}

@media (forced-colors: active) {
  .soc-10__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.soc-10');
  if (!root) return;
  const btn = root.querySelector('.soc-10__btn--ghost');
  const live = root.querySelector('.soc-10__live');
  btn.addEventListener('click', () => {
    live.textContent = 'Opening your print dialog. The action bar is hidden on paper.';
    window.print();
    setTimeout(() => { live.textContent = ''; }, 4000);
  });
})();
```
