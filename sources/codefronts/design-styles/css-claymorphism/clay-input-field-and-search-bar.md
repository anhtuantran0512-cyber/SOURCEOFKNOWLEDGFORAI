---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-input-field-and-search-bar/"
title: "Clay Input Field and Search Bar"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Inputs are the one place clay inverts: a field you type into must be a well, not a lifted object."
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Input Field and Search Bar
Source: https://codefronts.com/design-styles/css-claymorphism/clay-input-field-and-search-bar/

Inputs are the one place clay inverts: a field you type into must be a well, not a lifted object. This set gets it right — an inset search bar with a suggestion tray on focus, a floating-label field, a textarea that grows with field-sizing:content, and validation styled with :user-invalid so errors appear only after the user finishes.
## HTML
```html
<section class="cl-11" aria-label="Clay input field and search bar demo">
  <div class="cl-11__stage">
    <div class="cl-11__panel">
      <div class="cl-11__searchWrap">
        <label class="cl-11__lab" for="cl-11-search">Search lessons</label>
        <div class="cl-11__shell cl-11__shell--search">
          <svg class="cl-11__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M10.5 3a7.5 7.5 0 015.9 12.1l4.3 4.3-1.4 1.4-4.3-4.3A7.5 7.5 0 1110.5 3zm0 2a5.5 5.5 0 100 11 5.5 5.5 0 000-11z" fill="currentColor"/></svg>
          <input class="cl-11__input" type="search" id="cl-11-search" placeholder="Try &quot;inset shadows&quot;" autocomplete="off">
          <kbd class="cl-11__kbd">/</kbd>
        </div>
        <ul class="cl-11__tray" role="listbox" aria-label="Suggestions">
          <li role="option" aria-selected="false"><b>inset box-shadow</b> · technique</li>
          <li role="option" aria-selected="false"><b>clay vs neumorphism</b> · comparison</li>
          <li role="option" aria-selected="false"><b>puffy radius scale</b> · reference</li>
        </ul>
      </div>
      <div class="cl-11__grid">
        <div class="cl-11__floatWrap">
          <div class="cl-11__shell">
            <input class="cl-11__input cl-11__input--float" type="text" id="cl-11-name" placeholder=" ">
            <label class="cl-11__float" for="cl-11-name">Display name</label>
          </div>
        </div>
        <div class="cl-11__floatWrap">
          <div class="cl-11__shell">
            <input class="cl-11__input cl-11__input--float" type="email" id="cl-11-mail" placeholder=" " required>
            <label class="cl-11__float" for="cl-11-mail">Email address</label>
          </div>
          <p class="cl-11__hint">We only email your weekly streak.</p>
        </div>
      </div>
      <div>
        <label class="cl-11__lab" for="cl-11-note">Practice note</label>
        <div class="cl-11__shell cl-11__shell--area">
          <textarea class="cl-11__area" id="cl-11-note" rows="2" placeholder="What did you learn today?"></textarea>
        </div>
      </div>
    </div>
    <p class="cl-11__chip" aria-hidden="true">field = well · :focus-within ring · :user-invalid · @starting-style tray · field-sizing</p>
  </div>
</section>
```
## CSS
```css
.cl-11,
.cl-11 *,
.cl-11 *::before,
.cl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-11-bg);
  --cl-11-bg: oklch(0.94 0.025 230);
  --cl-11-clay: oklch(0.89 0.045 235);
  --cl-11-accent: oklch(0.72 0.14 240);
  --cl-11-error: oklch(0.62 0.19 25);
  --cl-11-shade: oklch(0.55 0.08 235/.6);
  --cl-11-light: oklch(1 0.01 235/.95);
  --cl-11-ink: oklch(0.28 0.045 235);
  --cl-11-mut: oklch(0.5 0.035 235);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-11-ink);
}

.cl-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(20px,5vw,56px);
}

.cl-11__panel {
  width: min(100%,600px);
  display: grid;
  gap: clamp(18px,3vw,24px);
  padding: clamp(22px,3.4vw,34px);
  border-radius: 42px;
  background: color-mix(in oklch,var(--cl-11-bg) 92%,white);
  box-shadow: 0 30px 60px -24px var(--cl-11-shade),inset 0 -16px 28px -16px var(--cl-11-shade),inset 0 18px 28px -12px var(--cl-11-light);
}

.cl-11__lab {
  display: block;
  margin-bottom: 9px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--cl-11-mut);
}

.cl-11__searchWrap {
  position: relative;
}

.cl-11__shell {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 18px;
  border-radius: 24px;
  background: color-mix(in oklch,var(--cl-11-bg) 93%,oklch(0.6 0.06 235));
  box-shadow: inset 0 10px 18px -6px var(--cl-11-shade),inset 0 -8px 14px -10px var(--cl-11-light);
  transition: box-shadow .28s;
}

.cl-11__shell:focus-within {
  box-shadow: inset 0 8px 14px -8px var(--cl-11-shade),inset 0 -6px 12px -10px var(--cl-11-light),0 0 0 4px color-mix(in oklch,var(--cl-11-accent) 42%,transparent);
}

.cl-11__shell--search {
  border-radius: 99px;
}

.cl-11__shell--area {
  border-radius: 24px;
  padding: 14px 18px;
}

.cl-11__icon {
  flex: none;
  color: var(--cl-11-mut);
}

.cl-11__input {
  flex: 1;
  min-width: 0;
  min-height: 56px;
  border: 0;
  background: none;
  font: inherit;
  font-size: 15px;
  color: var(--cl-11-ink);
  outline: none;
}

.cl-11__input::placeholder {
  color: color-mix(in oklch,var(--cl-11-mut) 88%,transparent);
}

.cl-11__input::-webkit-search-cancel-button {
  filter: grayscale(1) opacity(.6);
}

.cl-11__kbd {
  flex: none;
  display: grid;
  place-items: center;
  width: 26px;
  height: 26px;
  border-radius: 9px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--cl-11-mut);
  background: color-mix(in oklch,var(--cl-11-bg) 82%,white);
  box-shadow: 0 4px 8px -5px var(--cl-11-shade),inset 0 5px 7px -5px var(--cl-11-light);
}

.cl-11__tray {
  position: absolute;
  left: 0;
  right: 0;
  top: calc(100% + 10px);
  z-index: 2;
  list-style: none;
  display: none;
  opacity: 0;
  translate: 0 -8px;
  padding: 10px;
  border-radius: 26px;
  background: color-mix(in oklch,var(--cl-11-bg) 96%,white);
  box-shadow: 0 26px 50px -20px var(--cl-11-shade),inset 0 -12px 22px -16px var(--cl-11-shade),inset 0 14px 22px -12px var(--cl-11-light);
  transition: opacity .26s,translate .26s,display .26s allow-discrete;
}

.cl-11__searchWrap:focus-within .cl-11__tray {
  display: grid;
  opacity: 1;
  translate: 0;
}

@starting-style {
  .cl-11__searchWrap:focus-within .cl-11__tray {
    opacity: 0;
    translate: 0 -8px;
  }
}

.cl-11__tray li {
  padding: 12px 16px;
  border-radius: 18px;
  font-size: 13.5px;
  color: var(--cl-11-mut);
  cursor: pointer;
  transition: background .2s;
}

.cl-11__tray li b {
  color: var(--cl-11-ink);
  font-weight: 660;
}

.cl-11__tray li:hover {
  background: color-mix(in oklch,var(--cl-11-accent) 16%,transparent);
}

.cl-11__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
  gap: 16px;
}

.cl-11__floatWrap .cl-11__shell {
  position: relative;
  padding-top: 6px;
}

.cl-11__input--float {
  min-height: 60px;
  padding-top: 14px;
}

.cl-11__float {
  position: absolute;
  left: 19px;
  top: 19px;
  font-size: 15px;
  color: var(--cl-11-mut);
  pointer-events: none;
  transition: translate .22s cubic-bezier(.2,.8,.3,1),font-size .22s,color .22s;
}

.cl-11__input--float:focus+.cl-11__float,
.cl-11__input--float:not(:placeholder-shown)+.cl-11__float {
  translate: 0 -13px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--cl-11-accent);
}

.cl-11__hint {
  margin-top: 8px;
  padding-left: 6px;
  font-size: 12.5px;
  color: var(--cl-11-mut);
  transition: color .25s;
}

.cl-11__floatWrap:has(:user-invalid) .cl-11__shell {
  box-shadow: inset 0 10px 18px -6px color-mix(in oklch,var(--cl-11-error) 55%,transparent),inset 0 -8px 14px -10px var(--cl-11-light),0 0 0 3px color-mix(in oklch,var(--cl-11-error) 55%,transparent);
}

.cl-11__floatWrap:has(:user-invalid) .cl-11__hint {
  color: var(--cl-11-error);
}

.cl-11__floatWrap:has(:user-invalid) .cl-11__hint::before {
  content: 'Check this address — ';
  font-weight: 680;
}

.cl-11__area {
  width: 100%;
  border: 0;
  background: none;
  font: inherit;
  font-size: 15px;
  line-height: 1.6;
  color: var(--cl-11-ink);
  outline: none;
  resize: none;
  field-sizing: content;
  min-height: 64px;
  max-height: 180px;
}

.cl-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-11-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-11-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-11 * {
    transition-duration: .01ms !important;
  }
}
```
