---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/chevron-rotate/"
title: "Chevron Rotate Card Accordion — The Production Default, Perfected"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The accordion you actually ship: separated card items, an SVG-quality chevron drawn in CSS that rotates a clean 180°, hover elevation, an open-state border…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Chevron Rotate Card Accordion — The Production Default, Perfected
Source: https://codefronts.com/navigation/css-accordions/chevron-rotate/

The accordion you actually ship: separated card items, an SVG-quality chevron drawn in CSS that rotates a clean 180°, hover elevation, an open-state border tint and dividing rule between question and answer. Deliberately unflashy — every detail tuned so it drops into any SaaS product unchanged.
## HTML
```html
<section class="acc-10" aria-label="Chevron rotate card accordion demo">
  <div class="acc-10__wrap">
    <h3 class="acc-10__title">Help center</h3>
    <details class="acc-10__item" open>
      <summary class="acc-10__sum">How do I reset a teammate's password?<span class="acc-10__chip"><span class="acc-10__chev"></span></span></summary>
      <div class="acc-10__body"><p>Admins can send a reset link from <b>Members → ⋯ → Reset password</b>. The link expires in 30 minutes and signs out all of that user's sessions.</p></div>
    </details>
    <details class="acc-10__item">
      <summary class="acc-10__sum">Where do I find my API keys?<span class="acc-10__chip"><span class="acc-10__chev"></span></span></summary>
      <div class="acc-10__body"><p>Under <b>Settings → Developers</b>. Keys are shown once at creation — store them in a secret manager, and rotate them from the same screen.</p></div>
    </details>
    <details class="acc-10__item">
      <summary class="acc-10__sum">Can I export my data?<span class="acc-10__chip"><span class="acc-10__chev"></span></span></summary>
      <div class="acc-10__body"><p>Yes — full workspace exports (JSON + attachments) run from <b>Settings → Export</b> and email you a download link within minutes.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-10,
.acc-10 *,
.acc-10 *::before,
.acc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-10 {
  --accent: oklch(0.52 0.17 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f2f3f8;
  padding: 40px 20px;
}

.acc-10__wrap {
  width: min(580px,100%);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.acc-10__title {
  font-size: 24px;
  font-weight: 800;
  color: #191d33;
  letter-spacing: -.02em;
  margin-bottom: 6px;
}

.acc-10__item {
  background: #fff;
  border: 1.5px solid #e4e6f0;
  border-radius: 14px;
  box-shadow: 0 6px 20px -16px rgba(25,29,70,.35);
  transition: border-color .2s,box-shadow .2s,translate .2s;
}

.acc-10__item:hover {
  translate: 0 -1px;
  box-shadow: 0 12px 28px -18px rgba(25,29,70,.45);
}

.acc-10__item[open] {
  border-color: oklch(0.52 0.17 265 / .5);
}

.acc-10__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 60px;
  padding: 8px 16px 8px 20px;
  font-size: 15.5px;
  font-weight: 650;
  color: #232948;
  cursor: pointer;
}

.acc-10__sum::-webkit-details-marker {
  display: none;
}

.acc-10__sum::marker {
  content: "";
}

.acc-10__chip {
  margin-left: auto;
  width: 28px;
  height: 28px;
  flex: none;
  display: grid;
  place-content: center;
  background: #eef0f7;
  border-radius: 50%;
  transition: background .2s;
}

.acc-10__item[open] .acc-10__chip {
  background: var(--accent);
}

.acc-10__chev {
  width: 8px;
  height: 8px;
  border-right: 2px solid #5d6488;
  border-bottom: 2px solid #5d6488;
  rotate: 45deg;
  translate: 0 -1.5px;
  transition: rotate .3s cubic-bezier(.4,0,.2,1),border-color .2s;
}

.acc-10__item[open] .acc-10__chev {
  rotate: 225deg;
  translate: 0 1.5px;
  border-color: #fff;
}

.acc-10__body {
  margin: 0 20px;
  padding: 14px 24px 18px 0;
  border-top: 1px solid #edeff5;
  font-size: 14.5px;
  line-height: 1.65;
  color: #4a5170;
}

.acc-10__item[open] .acc-10__body {
  animation: acc-10-in .3s ease-out;
}

@keyframes acc-10-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.acc-10__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-10__item,
    .acc-10__chev {
    transition: none;
  }

  .acc-10__item[open] .acc-10__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — details[open] rotates the chevron with the individual rotate: property inside a fixed chip so text never reflows; everything else is hover/focus/open CSS states. */
```
