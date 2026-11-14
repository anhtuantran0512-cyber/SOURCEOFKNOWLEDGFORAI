---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/editorial-dividers/"
title: "Editorial Article Serif Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "How print handles a scene break: not a line, but breathing room and a mark."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Article Serif Divider CSS
Source: https://codefronts.com/snippets/css-dividers/editorial-dividers/

How print handles a scene break: not a line, but breathing room and a mark. This demo pairs a true asterism break with a real drop cap set by initial-letter — the property that sinks a letter by a number of lines instead of the fragile float-plus-magic-numbers hack — and a first-line small-caps lead-in. Everything you need for long-form reading layouts that feel typeset rather than styled.
## HTML
```html
<section class="div-09" aria-label="Editorial serif divider and drop cap demo">
  <article class="div-09__stage">
    <p class="div-09__kicker">Essay · Typography</p>
    <h2 class="div-09__title">The Quiet Rules of the Page</h2>
    <p class="div-09__lead">Typographers spend their lives on decisions readers are never meant to notice. A scene break is one of them: the reader feels a pause, closes one thought, opens another, and never once thinks about the mark that did it.</p>
    <hr class="div-09__break" aria-label="Section break">
    <p class="div-09__body">Print solved this centuries before the browser existed. A rule across the column reads as an ending; a small centred ornament with air above and below reads as a breath. The difference is not decoration, it is grammar — and it is why editorial CSS should reach for whitespace before it reaches for a border.</p>
    <hr class="div-09__break div-09__break--dots" aria-label="Section break">
    <p class="div-09__body">Set the measure at sixty-five characters, give the break two-and-a-half ems of air, and let the mark be small. The page will feel typeset rather than styled, which is the entire ambition.</p>
    <p class="div-09__chip">initial-letter · ⁂ asterism · text-indent cancels letter-spacing</p>
  </article>
</section>
```
## CSS
```css
.div-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-09-bg);
  --div-09-bg: oklch(0.972 0.011 88);
  --div-09-ink: oklch(0.24 0.018 55);
  --div-09-mut: oklch(0.53 0.02 55);
  --div-09-line: oklch(0.24 0.018 55/.22);
  --div-09-acc: oklch(0.5 0.13 32);
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  color: var(--div-09-ink);
}

.div-09 *,
.div-09 *::before,
.div-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-09__stage {
  min-height: 100svh;
  width: min(92vw,64ch);
  margin-inline: auto;
  display: grid;
  align-content: center;
  gap: 2px;
  padding: clamp(32px,6vw,72px) 0;
}

.div-09__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--div-09-acc);
  margin-bottom: 10px;
}

.div-09__title {
  font-size: clamp(30px,5.4vw,54px);
  line-height: 1.07;
  letter-spacing: -.022em;
  font-weight: 400;
  margin-bottom: 22px;
  text-wrap: balance;
}

.div-09__lead,
.div-09__body {
  font-size: clamp(16px,2vw,19px);
  line-height: 1.66;
  text-wrap: pretty;
}

.div-09__lead::first-letter {
  -webkit-initial-letter: 3;
  initial-letter: 3;
  color: var(--div-09-acc);
  font-weight: 700;
  margin-right: .09em;
}

@supports not (initial-letter: 3) {
  .div-09__lead::first-letter {
    float: left;
    font-size: 3.35em;
    line-height: .86;
    padding: .06em .09em 0 0;
  }
}

.div-09__break {
  border: 0;
  height: auto;
  text-align: center;
  color: var(--div-09-acc);
  margin: clamp(26px,4vw,42px) 0;
  letter-spacing: .62em;
  text-indent: .62em;
  font-size: 15px;
  line-height: 1;
}

.div-09__break::before {
  content: '\2042';
}

.div-09__break--dots::before {
  content: '\2022 \2022 \2022';
  font-size: 9px;
  letter-spacing: .9em;
  text-indent: .9em;
}

.div-09__chip {
  margin-top: 26px;
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-09-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-09-line);
  border-radius: 99px;
}
```
