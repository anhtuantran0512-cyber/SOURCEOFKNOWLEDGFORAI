---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/typewriter-retype/"
title: "Typewriter Retype"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A retro-terminal CTA where, on hover, the label retypes character by character with a blinking cursor — nostalgic and techy for dev tools and docs."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Typewriter Retype
Source: https://codefronts.com/motion/css-button-hover-effects/typewriter-retype/

A retro-terminal CTA where, on hover, the label retypes character by character with a blinking cursor — nostalgic and techy for dev tools and docs.
## HTML
```html
<div class="bhe-26-group">
<section class="bhe-26a" aria-label="Typewriter retype button">
  <button class="bhe-26a__btn" type="button"><span class="bhe-26a__type">$ deploy_now</span></button>
</section>
<section class="bhe-26b" aria-label="Prompt caret button">
  <button class="bhe-26b__btn" type="button"><span class="bhe-26b__label">run build</span><span class="bhe-26b__caret" aria-hidden="true"></span></button>
</section>
</div>
```
## CSS
```css
.bhe-26-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-26-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-26a,
.bhe-26a *,
.bhe-26a *::before,
.bhe-26a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-26a {
  --term: oklch(0.82 0.19 145);
  font-family: ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #06120b;
}

.bhe-26a__btn {
  font-size: 16px;
  font-weight: 700;
  color: var(--term);
  padding: 16px 28px;
  border: 1px solid var(--term);
  border-radius: 6px;
  cursor: pointer;
  background: #0a1c12;
  box-shadow: 0 0 20px -8px var(--term);
}

.bhe-26a__type {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  vertical-align: bottom;
  width: 12ch;
  border-right: 2px solid var(--term);
  animation: bhe-26a-blink 1s steps(1) infinite;
}

.bhe-26a__btn:hover .bhe-26a__type,
.bhe-26a__btn:focus-visible .bhe-26a__type {
  width: 0;
  animation: bhe-26a-type 1s steps(12) forwards,bhe-26a-blink 1s steps(1) infinite;
}

.bhe-26a__btn:focus-visible {
  outline: 3px solid var(--term);
  outline-offset: 4px;
}

@keyframes bhe-26a-type {
  from {
    width: 0;
  }

  to {
    width: 12ch;
  }
}

@keyframes bhe-26a-blink {
  50% {
    border-color: transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-26a__type {
    animation: none;
    width: 12ch;
  }

  .bhe-26a__btn:hover .bhe-26a__type,
    .bhe-26a__btn:focus-visible .bhe-26a__type {
    animation: none;
    width: 12ch;
  }
}

.bhe-26b,
.bhe-26b *,
.bhe-26b *::before,
.bhe-26b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-26b {
  --term: oklch(0.8 0.16 90);
  font-family: ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #12100a;
}

.bhe-26b__btn {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  font-size: 16px;
  font-weight: 700;
  color: var(--term);
  padding: 16px 30px;
  border: 1px solid var(--term);
  border-radius: 6px;
  cursor: pointer;
  background: #1c180c;
}

.bhe-26b__label {
  overflow: hidden;
  white-space: nowrap;
  max-width: 9ch;
  transition: max-width .7s steps(9);
}

.bhe-26b__caret {
  width: 9px;
  height: 1.1em;
  background: var(--term);
  animation: bhe-26b-blink 1s steps(1) infinite;
}

.bhe-26b__btn:hover .bhe-26b__label,
.bhe-26b__btn:focus-visible .bhe-26b__label {
  max-width: 0;
}

.bhe-26b__btn:hover .bhe-26b__caret,
.bhe-26b__btn:focus-visible .bhe-26b__caret {
  animation: bhe-26b-blink .4s steps(1) infinite;
}

.bhe-26b__btn:focus-visible {
  outline: 3px solid var(--term);
  outline-offset: 4px;
}

@keyframes bhe-26b-blink {
  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-26b__label {
    transition: none;
  }

  .bhe-26b__caret {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
