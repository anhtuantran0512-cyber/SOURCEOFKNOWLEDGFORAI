---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/editorial-footnote/"
title: "Editorial Footnote"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A sidenote for longform reading."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Footnote
Source: https://codefronts.com/snippets/css-tooltips/editorial-footnote/

A sidenote for longform reading. The source word grows an underline on hover; a paper-card with a deckle clip-path drops down on a hairline tether, holds the body of the note in italic Garamond, and closes with a small all-caps citation. Made for essays, not interfaces.
## HTML
```html
<div class="tp-04">
  <article class="tp-04__essay">
    <div class="tp-04__byline">
      <span>An essay · No. XII</span>
      <span>14 May 2026</span>
    </div>
    <p>
      <span class="tp-04__dropcap">T</span>he interface is a place where reading becomes touch. We rarely talk about the cursor as a finger, but it is — it brushes against language, and language flinches back. A tooltip is what happens when a word
      <span class="tp-04__anchor">decides to answer<span class="tp-04__sup">1</span><span class="tp-04__tip">
        <span class="tp-04__tip-num">1.</span>
        <span class="tp-04__tip-body">The phrase belongs to Robin Sloan, who described hover states as "the part of the web that whispers back." Most of us, of course, have settled for the part that mumbles.</span>
        <span class="tp-04__tip-cite">— Sloan, 2019, p. 84</span>
      </span></span>. Once it could only do so in gray boxes, a meek municipal voice; now it can do almost anything, and so the question is no longer whether it speaks but what register it speaks in.
    </p>
    <p>
      Consider the
      <span class="tp-04__anchor">marginalia of medieval readers<span class="tp-04__sup">2</span><span class="tp-04__tip">
        <span class="tp-04__tip-num">2.</span>
        <span class="tp-04__tip-body">In the manuscript tradition, glosses were often longer than the texts they served. The Vulgate, the Talmud, the Glossa Ordinaria — these are pages where the footnote ate the page and called it home.</span>
        <span class="tp-04__tip-cite">— de Hamel, 2016, ch. 4</span>
      </span></span>, who wrote louder than the books they read. Their pages were tooltips made of ink, hovering forever — annotations that became canon because the original was lonely without them.
    </p>
  </article>
</div>
```
## CSS
```css
.tp-04 {
  width: 100%;
  min-height: 100vh;
  background: #f3eee3;
  /* Generous bottom room — footnote tips drop down from each anchor. */
  padding: 40px 40px 220px;
  position: relative;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.tp-04::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2'/><feColorMatrix values='0 0 0 0 0.16  0 0 0 0 0.12  0 0 0 0 0.09  0 0 0 0.05 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
  pointer-events: none;
  opacity: 0.5;
}

.tp-04__essay {
  max-width: 560px;
  font-family: Georgia, serif;
  font-size: 18px;
  line-height: 1.65;
  color: #2a1f17;
  position: relative;
  z-index: 1;
}

.tp-04__byline {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9.5px;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: #8a2c1c;
  margin-bottom: 22px;
  border-bottom: 1px solid rgba(138, 44, 28, 0.3);
  padding-bottom: 12px;
  display: flex;
  justify-content: space-between;
}

.tp-04__essay p {
  margin-bottom: 18px;
  text-align: justify;
  hyphens: auto;
}

.tp-04__dropcap {
  float: left;
  font-family: Georgia, serif;
  font-weight: 500;
  font-size: 76px;
  line-height: 0.85;
  margin: 4px 10px 0 0;
  color: #8a2c1c;
}

.tp-04__anchor {
  position: relative;
  display: inline;
  color: #8a2c1c;
  cursor: help;
  font-family: Georgia, serif;
  font-style: italic;
  font-weight: 500;
  background-image: linear-gradient(to right, #8a2c1c 0%, #8a2c1c 100%);
  background-size: 0 1px;
  background-repeat: no-repeat;
  background-position: 0 100%;
  transition: background-size 0.5s cubic-bezier(0.65, 0, 0.35, 1);
  padding-bottom: 2px;
}

.tp-04__anchor:hover {
  background-size: 100% 1px;
}

.tp-04__sup {
  font-size: 0.65em;
  vertical-align: super;
  color: #8a2c1c;
  font-weight: 600;
  margin-left: 1px;
}

.tp-04__tip {
  position: absolute;
  top: calc(100% + 14px);
  left: 50%;
  transform: translate(-50%, -8px) rotate(-0.4deg);
  width: 300px;
  background: #faf5ea;
  color: #2a1f17;
  padding: 16px 20px 18px;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.05), 0 10px 26px -6px rgba(75, 40, 20, 0.25), 0 2px 5px -1px rgba(75, 40, 20, 0.15);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s, transform 0.4s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear 0.3s;
  z-index: 20;
  font-family: Georgia, serif;
  font-size: 14px;
  line-height: 1.55;
  pointer-events: none;
  text-align: left;
  display: block;
  clip-path: polygon(
      0% 4%, 2% 1%, 6% 3%, 12% 0%, 22% 2%, 35% 0%, 48% 2%, 62% 0%,
      78% 2%, 90% 0%, 96% 3%, 100% 1%,
      100% 96%, 98% 99%, 90% 97%, 78% 100%, 60% 98%, 42% 100%, 24% 98%,
      10% 100%, 4% 97%, 0% 99%
    );
}

.tp-04__anchor:hover .tp-04__tip {
  opacity: 1;
  visibility: visible;
  transform: translate(-50%, 0) rotate(-0.4deg);
  transition-delay: 0s;
}

.tp-04__tip::before {
  content: '';
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  width: 1px;
  height: 14px;
  background: #8a2c1c;
  opacity: 0.4;
}

.tp-04__tip-num {
  display: inline-block;
  font-family: Georgia, serif;
  font-style: italic;
  font-weight: 500;
  color: #8a2c1c;
  font-size: 20px;
  line-height: 1;
  margin-right: 6px;
  vertical-align: -2px;
}

.tp-04__tip-body {
  font-style: italic;
  display: inline;
}

.tp-04__tip-cite {
  display: block;
  margin-top: 10px;
  padding-top: 8px;
  border-top: 1px dotted rgba(138, 44, 28, 0.4);
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #8a2c1c;
  font-style: normal;
}
```
