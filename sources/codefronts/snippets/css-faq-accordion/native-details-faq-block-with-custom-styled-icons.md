---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/native-details-faq-block-with-custom-styled-icons/"
title: "Native <details> FAQ Block with Custom Styled Icons"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The most semantic FAQ possible: native <details>/<summary>, which browsers give you free keyboard support, screen-reader disclosure semantics, and even…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Native <details> FAQ Block with Custom Styled Icons
Source: https://codefronts.com/snippets/css-faq-accordion/native-details-faq-block-with-custom-styled-icons/

The most semantic FAQ possible: native <details>/<summary>, which browsers give you free keyboard support, screen-reader disclosure semantics, and even in-page find-and-expand for. This demo removes the default triangle marker, draws a custom animated chevron ring, and — the 2026 part — animates open/close to height:auto using ::details-content + interpolate-size: allow-keywords, with a graceful instant-open fallback wrapped in @supports. Styled as a warm editorial help page.
## HTML
```html
<section class="cfa-02" aria-label="Native details FAQ with custom icons">
  <div class="cfa-02__wrap">
    <header class="cfa-02__head">
      <h1>Help &amp; support</h1>
      <p>Built on native <code>&lt;details&gt;</code> — keyboard support, screen-reader semantics and find-in-page expansion are free. Try <kbd>Ctrl</kbd>+<kbd>F</kbd> for “passport”.</p>
    </header>
    <div class="cfa-02__list">
      <details class="cfa-02__item" open>
        <summary class="cfa-02__q">How long does delivery take?
          <span class="cfa-02__ic" aria-hidden="true"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="cfa-02__a"><p>Standard delivery is 3–5 business days across the US, UK, Canada and Australia. Express (1–2 days) is available at checkout, and every order gets a tracked link the moment it leaves the warehouse.</p></div>
      </details>
      <details class="cfa-02__item">
        <summary class="cfa-02__q">Do I need a passport copy to book?
          <span class="cfa-02__ic" aria-hidden="true"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="cfa-02__a"><p>Only for international itineraries. Upload a photo of the ID page once and we auto-fill every future booking — the file is encrypted at rest and deleted 30 days after your trip ends.</p></div>
      </details>
      <details class="cfa-02__item">
        <summary class="cfa-02__q">Can I change my order after placing it?
          <span class="cfa-02__ic" aria-hidden="true"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="cfa-02__a"><p>Yes — orders can be edited for 60 minutes after checkout from your account page. After that the warehouse has it, but you can always refuse delivery or start a free return.</p></div>
      </details>
      <details class="cfa-02__item">
        <summary class="cfa-02__q">Which payment methods do you accept?
          <span class="cfa-02__ic" aria-hidden="true"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="cfa-02__a"><p>All major cards, Apple Pay, Google Pay and PayPal. Business customers can request invoicing with NET-30 terms once approved.</p></div>
      </details>
    </div>
    <p class="cfa-02__foot">Open/close animates to <code>height:auto</code> via <code>::details-content</code> — no JavaScript, no wrappers. A demo from the CodeFronts FAQ collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-02,
.cfa-02 *,
.cfa-02 *::before,
.cfa-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-02 {
  --bg: oklch(0.97 0.012 85);
  --panel: oklch(0.995 0.004 90);
  --ink: oklch(0.25 0.02 60);
  --mut: oklch(0.5 0.025 60);
  --line: oklch(0.88 0.02 80);
  --acc: oklch(0.55 0.14 45);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: var(--bg);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.cfa-02__wrap {
  width: min(100%,640px);
}

.cfa-02__head h1 {
  font-size: clamp(30px,5cqi,42px);
  font-weight: 700;
  letter-spacing: -.02em;
}

.cfa-02__head p {
  margin-top: 10px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 14px;
  line-height: 1.65;
  color: var(--mut);
}

.cfa-02__head code,
.cfa-02__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .85em;
  background: oklch(0.93 0.015 85);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.cfa-02__head kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .82em;
  padding: 1px 6px;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  background: var(--panel);
}

.cfa-02__list {
  margin-top: 26px;
  border-top: 1px solid var(--line);
  interpolate-size: allow-keywords;
}

.cfa-02__item {
  border-bottom: 1px solid var(--line);
}

.cfa-02__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 19px 4px;
  cursor: pointer;
  font-size: 18px;
  font-weight: 600;
  letter-spacing: -.01em;
  list-style: none;
  transition: color .2s;
}

.cfa-02__q::-webkit-details-marker {
  display: none;
}

.cfa-02__q:hover {
  color: var(--acc);
}

.cfa-02__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.cfa-02__ic {
  display: grid;
  place-items: center;
  flex: none;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: 1.5px solid var(--line);
  color: var(--acc);
  transition: rotate .4s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s;
}

.cfa-02__item[open] .cfa-02__ic {
  rotate: -180deg;
  background: color-mix(in oklch,var(--acc) 12%,transparent);
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-02__a p {
  padding: 2px 4px 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 14.5px;
  line-height: 1.75;
  color: var(--mut);
  max-width: 58ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-02__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .4s cubic-bezier(.4,0,.2,1),opacity .35s,content-visibility .4s allow-discrete;
  }

  .cfa-02__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-02__foot {
  margin-top: 22px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-02 *,
    .cfa-02 .cfa-02__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
