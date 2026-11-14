---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/animated-details-accordion-height-auto/"
title: "Smoothly Animated <details> Accordion — Transition height: auto in Pure CSS"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "THE most-searched accordion trick, solved: a native <details> element that slides open AND closed with a real height transition — no fixed max-height hack,…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Smoothly Animated <details> Accordion — Transition height: auto in Pure CSS
Source: https://codefronts.com/navigation/css-accordions/animated-details-accordion-height-auto/

THE most-searched accordion trick, solved: a native <details> element that slides open AND closed with a real height transition — no fixed max-height hack, no JavaScript measuring. Uses the new ::details-content pseudo-element with interpolate-size: allow-keywords, degrading gracefully to instant toggle in older browsers.
## HTML
```html
<section class="acc-05" aria-label="Animated details accordion demo">
  <div class="acc-05__wrap">
    <p class="acc-05__kicker">Changelog</p>
    <h3 class="acc-05__title">What shipped this quarter</h3>
    <details class="acc-05__item" open>
      <summary class="acc-05__sum"><span class="acc-05__ver">3.4</span>Realtime collaboration<span class="acc-05__chev"></span></summary>
      <div class="acc-05__body"><p>Multiplayer cursors, presence avatars and conflict-free co-editing landed across every document type. Sessions reconnect automatically and offline edits merge on return.</p></div>
    </details>
    <details class="acc-05__item">
      <summary class="acc-05__sum"><span class="acc-05__ver">3.3</span>Command palette<span class="acc-05__chev"></span></summary>
      <div class="acc-05__body"><p>Press ⌘K anywhere to search actions, files and people. Fuzzy matching, recent-first ranking and full keyboard operability out of the box.</p></div>
    </details>
    <details class="acc-05__item">
      <summary class="acc-05__sum"><span class="acc-05__ver">3.2</span>Audit log export<span class="acc-05__chev"></span></summary>
      <div class="acc-05__body"><p>Admins can stream audit events to S3 or download signed CSV exports. Retention is configurable per workspace, with SOC 2 evidence bundles one click away.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-05,
.acc-05 *,
.acc-05 *::before,
.acc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-05 {
  --accent: oklch(0.58 0.2 300);
  interpolate-size: allow-keywords;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f6f3fa;
  padding: 40px 20px;
}

.acc-05__wrap {
  width: min(600px,100%);
  background: #fff;
  border-radius: 18px;
  padding: 36px 34px;
  box-shadow: 0 24px 60px -34px rgba(60,30,90,.35);
}

.acc-05__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.acc-05__title {
  font-size: 25px;
  font-weight: 800;
  color: #251b30;
  letter-spacing: -.02em;
  margin: 6px 0 16px;
}

.acc-05__item {
  border: 1.5px solid #ece5f4;
  border-radius: 14px;
  margin-bottom: 10px;
  transition: border-color .25s,background .25s;
}

.acc-05__item[open] {
  border-color: oklch(0.58 0.2 300 / .45);
  background: #fdfbff;
}

.acc-05__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 58px;
  padding: 0 18px;
  font-size: 16px;
  font-weight: 650;
  color: #251b30;
  cursor: pointer;
}

.acc-05__sum::-webkit-details-marker {
  display: none;
}

.acc-05__sum::marker {
  content: "";
}

.acc-05__ver {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--accent);
  background: oklch(0.58 0.2 300 / .1);
  padding: 4px 9px;
  border-radius: 8px;
}

.acc-05__chev {
  margin-left: auto;
  width: 9px;
  height: 9px;
  border-right: 2.5px solid #a394b8;
  border-bottom: 2.5px solid #a394b8;
  transform: rotate(45deg) translateY(-2px);
  transition: transform .3s;
}

.acc-05__item[open] .acc-05__chev {
  transform: rotate(225deg) translateY(-2px);
}

.acc-05__item::details-content {
  height: 0;
  overflow: clip;
  opacity: 0;
  transition: height .38s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .38s allow-discrete;
}

.acc-05__item[open]::details-content {
  height: auto;
  opacity: 1;
}

.acc-05__body {
  padding: 2px 18px 20px 18px;
  font-size: 15px;
  line-height: 1.65;
  color: #584a68;
}

.acc-05__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-05__item::details-content,
    .acc-05__chev,
    .acc-05__item {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — interpolate-size: allow-keywords lets height transition to auto, and ::details-content + transition-behavior: allow-discrete animates the native details element open AND closed. Older browsers toggle instantly. */
```
