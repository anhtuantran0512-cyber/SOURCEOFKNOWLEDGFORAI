---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/css-gradient-search-bar-input/"
title: "CSS Gradient Search Bar & Input"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A command-palette-style search bar whose gradient border ignites on :focus-within, plus a settings form where each field grows an animated gradient underline…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Search Bar & Input
Source: https://codefronts.com/design-styles/css-gradient-ui/css-gradient-search-bar-input/

A command-palette-style search bar whose gradient border ignites on :focus-within, plus a settings form where each field grows an animated gradient underline as you focus it — the modern replacement for the default blue outline.
## HTML
```html
<div class="cgu-05-group">
<section class="cgu-05" aria-label="CSS gradient search bar and input demos">
  <div class="cgu-05__inner">
    <header class="cgu-05__head">
      <p class="cgu-05__eyebrow">05 · Search &amp; inputs</p>
      <h2 class="cgu-05__title">Focus states worth focusing on</h2>
      <p class="cgu-05__sub">Click into the search bar, then Tab through the form — gradient borders and self-drawing underlines, all <code>:focus-within</code>.</p>
    </header>
    <div class="cgu-05__search">
      <span class="cgu-05__icon" aria-hidden="true">⌕</span>
      <input class="cgu-05__input" type="search" placeholder="Search docs, components, tokens…" aria-label="Search documentation">
      <kbd class="cgu-05__kbd">⌘K</kbd>
    </div>
    <div class="cgu-05__chips" aria-label="Popular searches">
      <button class="cgu-05__chip" type="button">gradient border</button>
      <button class="cgu-05__chip" type="button">mask-composite</button>
      <button class="cgu-05__chip" type="button">oklch palette</button>
      <button class="cgu-05__chip" type="button">focus ring</button>
    </div>
    <form class="cgu-05__form" aria-label="Profile settings">
      <div class="cgu-05__field">
        <label class="cgu-05__label" for="cgu-05-name">Display name</label>
        <input class="cgu-05__text" id="cgu-05-name" type="text" placeholder="Ada Lovelace" autocomplete="name">
      </div>
      <div class="cgu-05__field">
        <label class="cgu-05__label" for="cgu-05-mail">Work email</label>
        <input class="cgu-05__text" id="cgu-05-mail" type="email" placeholder="[email protected]" autocomplete="email">
      </div>
      <div class="cgu-05__field cgu-05__field--wide">
        <label class="cgu-05__label" for="cgu-05-bio">Bio</label>
        <input class="cgu-05__text" id="cgu-05-bio" type="text" placeholder="First programmer. Gradient enthusiast.">
      </div>
    </form>
    <p class="cgu-05__foot">The gradient border doubles as the focus indicator — never remove an outline without replacing it.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-05-group {
  display: block;
  width: 100%;
}

.cgu-05,
.cgu-05 *,
.cgu-05 *::before,
.cgu-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-05 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: radial-gradient(90% 70% at 50% 110%,#141b33 0%,#0b0d16 60%);
}

.cgu-05__inner {
  width: min(720px,100%);
  display: grid;
  gap: 26px;
  justify-items: center;
}

.cgu-05__head {
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
  margin-bottom: 8px;
}

.cgu-05__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #818cf8;
}

.cgu-05__title {
  font-size: clamp(27px,4vw,44px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  text-wrap: balance;
}

.cgu-05__sub {
  max-width: 54ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
}

.cgu-05__sub code,
.cgu-05__foot {
  font-size: 13px;
}

.cgu-05__sub code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12.5px;
  color: #c7d2fe;
  background: rgba(129,140,248,.1);
  padding: 1px 5px;
  border-radius: 5px;
}

.cgu-05__search {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 6px 14px 6px 18px;
  border-radius: 16px;
  border: 2px solid transparent;
  background: linear-gradient(#0e1020,#0e1020) padding-box,linear-gradient(120deg,#2b2f45,#2b2f45) border-box;
  transition: box-shadow .3s,background .3s;
}

.cgu-05__search:hover {
  background: linear-gradient(#0e1020,#0e1020) padding-box,linear-gradient(120deg,#3b415e,#3b415e) border-box;
}

.cgu-05__search:focus-within {
  background: linear-gradient(#0e1020,#0e1020) padding-box,linear-gradient(120deg,#22d3ee,#818cf8,#e879f9) border-box;
  box-shadow: 0 0 0 4px rgba(129,140,248,.16),0 20px 44px -20px rgba(129,140,248,.45);
}

.cgu-05__icon {
  font-size: 20px;
  color: #8b90b0;
}

.cgu-05__input {
  flex: 1;
  font: inherit;
  font-size: 16px;
  color: #eef0ff;
  background: transparent;
  border: none;
  padding: 14px 0;
  outline: none;
}

.cgu-05__input::placeholder {
  color: #8b90b0;
}

.cgu-05__kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: #a7abc8;
  padding: 4px 9px;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,.12);
  background: rgba(255,255,255,.05);
}

.cgu-05__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
}

.cgu-05__chip {
  font: inherit;
  font-size: 12.5px;
  font-weight: 650;
  color: #a7abc8;
  padding: 7px 15px;
  border-radius: 9999px;
  cursor: pointer;
  border: 1px solid transparent;
  background: linear-gradient(#10121f,#10121f) padding-box,linear-gradient(135deg,#2b2f45,#2b2f45) border-box;
  transition: color .25s,background .25s;
}

.cgu-05__chip:hover,
.cgu-05__chip:focus-visible {
  color: #fff;
  background: linear-gradient(#10121f,#10121f) padding-box,linear-gradient(135deg,#22d3ee,#e879f9) border-box;
}

.cgu-05__chip:focus-visible {
  outline: 2px solid #c7d2fe;
  outline-offset: 2px;
}

.cgu-05__form {
  width: 100%;
  margin-top: 14px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 22px;
  padding: 28px;
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,.07);
  background: rgba(255,255,255,.028);
}

.cgu-05__field {
  display: grid;
  gap: 8px;
}

.cgu-05__field--wide {
  grid-column: 1/-1;
}

.cgu-05__label {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #8b90b0;
}

.cgu-05__text {
  font: inherit;
  font-size: 15px;
  color: #eef0ff;
  background-color: transparent;
  border: none;
  border-bottom: 1.5px solid #2b2f45;
  padding: 9px 2px;
  outline: none;
  background-image: linear-gradient(90deg,#22d3ee,#818cf8,#e879f9);
  background-repeat: no-repeat;
  background-size: 0% 2px;
  background-position: 0 100%;
  transition: background-size .45s cubic-bezier(.2,.8,.3,1);
}

.cgu-05__text::placeholder {
  color: #6f7495;
}

.cgu-05__text:focus {
  background-size: 100% 2px;
}

.cgu-05__foot {
  text-align: center;
  color: #7c81a3;
}

@media (max-width: 560px) {
  .cgu-05__form {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-05__search,
    .cgu-05__text,
    .cgu-05__chip {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — :focus-within lights the wrapper's double-background gradient border; underlines draw via animatable background-size. */
```
