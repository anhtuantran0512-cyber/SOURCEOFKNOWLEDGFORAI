---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/copy-quote/"
title: "CSS Blockquote with One-Click Copy Button"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "A share-ready quote card with the interaction every docs site trained users to expect: a copy button that grabs the quote plus its attribution via…"
has_js: "true"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Blockquote with One-Click Copy Button
Source: https://codefronts.com/snippets/css-blockquotes/copy-quote/

A share-ready quote card with the interaction every docs site trained users to expect: a copy button that grabs the quote plus its attribution via navigator.clipboard.writeText, then proves it worked — icon swaps to a check, label flips to 'Copied', a green tint washes the button, and the state announces itself to screen readers through an aria-live region (the visual swap alone is silent to assistive tech). The button reveals on card hover but stays permanently visible on keyboard focus and on touch devices, where hover doesn't exist.
## HTML
```html
<section class="bq-25" aria-label="Blockquote with one-click copy button demo">
  <div class="bq-25__stage">
    <figure class="bq-25__card">
      <button class="bq-25__copy" type="button" aria-label="Copy quote to clipboard">
        <svg class="bq-25__ic-copy" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><rect x="5.2" y="5.2" width="8.2" height="8.2" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10.8 5.2V4a1.6 1.6 0 0 0-1.6-1.6H4A1.6 1.6 0 0 0 2.4 4v5.2A1.6 1.6 0 0 0 4 10.8h1.2" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        <svg class="bq-25__ic-check" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2.8 8.6l3.4 3.4 7-7.6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="bq-25__lbl-copy">Copy</span>
        <span class="bq-25__lbl-done">Copied</span>
      </button>
      <blockquote class="bq-25__quote">
        <p>Programs must be written for people to read, and only incidentally for machines to execute.</p>
      </blockquote>
      <figcaption class="bq-25__by">Harold Abelson, <cite>Structure and Interpretation of Computer Programs</cite></figcaption>
      <span class="bq-25__status" role="status" aria-live="polite"></span>
    </figure>
    <p class="bq-25__chip" aria-hidden="true">navigator.clipboard · aria-live confirmation · hover:none override</p>
  </div>
</section>
```
## CSS
```css
.bq-25,
.bq-25 *,
.bq-25 *::before,
.bq-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.2 0.02 250);
  --card: oklch(0.25 0.022 252);
  --ink: oklch(0.95 0.008 250);
  --quiet: oklch(0.82 0.015 250);
  --mut: oklch(0.62 0.02 250);
  --acc: oklch(0.72 0.13 210);
  --ok: oklch(0.72 0.15 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-25__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(75% 60% at 50% 0%,oklch(0.26 0.04 235/.7),transparent),var(--bg);
  overflow-y: auto;
}

.bq-25__card {
  position: relative;
  width: min(100%,540px);
  background: var(--card);
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 18px;
  padding: clamp(26px,4vw,36px);
  box-shadow: 0 22px 54px oklch(0 0 0/.4);
}

.bq-25__quote p {
  font-family: Georgia,serif;
  font-size: clamp(19px,2.6vw,24px);
  line-height: 1.55;
  font-style: italic;
  color: var(--ink);
  text-wrap: pretty;
}

.bq-25__quote p::before {
  content: '\201C';
}

.bq-25__quote p::after {
  content: '\201D';
}

.bq-25__by {
  margin-top: 16px;
  font-size: 13px;
  color: var(--mut);
}

.bq-25__by cite {
  font-style: italic;
  color: var(--quiet);
}

.bq-25__copy {
  position: absolute;
  top: 14px;
  right: 14px;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 36px;
  padding: 0 13px;
  border-radius: 9px;
  border: 1px solid oklch(1 0 0/.16);
  background: oklch(1 0 0/.06);
  color: var(--quiet);
  font-size: 12px;
  font-weight: 650;
  cursor: pointer;
  opacity: 0;
  transition: opacity .25s,background .2s,border-color .2s,color .2s;
}

.bq-25__card:hover .bq-25__copy,
.bq-25__card:focus-within .bq-25__copy {
  opacity: 1;
}

.bq-25__copy:hover {
  background: oklch(1 0 0/.12);
  color: var(--ink);
}

.bq-25__copy:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  opacity: 1;
}

@media (hover: none) {
  .bq-25__copy {
    opacity: 1;
  }
}

.bq-25__ic-check,
.bq-25__lbl-done {
  display: none;
}

.bq-25__copy.is-copied {
  border-color: color-mix(in oklch,var(--ok) 55%,transparent);
  background: color-mix(in oklch,var(--ok) 16%,transparent);
  color: var(--ok);
}

.bq-25__copy.is-copied .bq-25__ic-copy,
.bq-25__copy.is-copied .bq-25__lbl-copy {
  display: none;
}

.bq-25__copy.is-copied .bq-25__ic-check,
.bq-25__copy.is-copied .bq-25__lbl-done {
  display: inline;
}

.bq-25__status {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.bq-25__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .bq-25 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.bq-25__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const btn = card.querySelector('.bq-25__copy');
    const status = card.querySelector('.bq-25__status');
    let t = 0;
    btn.addEventListener('click', async () => {
      const text = card.querySelector('.bq-25__quote').textContent.trim() +
        ' \u2014 ' + card.querySelector('.bq-25__by').textContent.trim();
      try {
        await navigator.clipboard.writeText(text);
        btn.classList.add('is-copied');
        status.textContent = 'Quote copied to clipboard';
        clearTimeout(t);
        t = setTimeout(() => { btn.classList.remove('is-copied'); status.textContent = ''; }, 1800);
      } catch { status.textContent = 'Copy failed \u2014 select the text instead'; }
    });
  });
})();
```
