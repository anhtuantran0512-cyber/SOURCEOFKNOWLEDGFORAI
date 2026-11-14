---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/article-with-pull-quotes-and-drop-caps/"
title: "Article with Pull Quotes and Drop Caps"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "Print typography, done properly on the web: a three-line drop cap using initial-letter with a hand-tuned ::first-letter fallback, pull quotes that float into…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Article with Pull Quotes and Drop Caps
Source: https://codefronts.com/layouts/css-blog-layouts/article-with-pull-quotes-and-drop-caps/

Print typography, done properly on the web: a three-line drop cap using initial-letter with a hand-tuned ::first-letter fallback, pull quotes that float into the measure and let text wrap around them, small caps for the opening line, and hanging punctuation. Every effect is one CSS rule — no spans, no wrapper divs, no JS.
## HTML
```html
<article class="bl-08">
  <header class="bl-08__head">
    <p class="bl-08__rubric">Essay · Typography</p>
    <h1 class="bl-08__title">The paragraph is a technology, and we keep forgetting how it works</h1>
    <p class="bl-08__standfirst">Drop caps, pull quotes and hanging punctuation were invented to solve problems that have not gone away. They were solved on paper five centuries ago; the web spent twenty years relearning them badly.</p>
    <div class="bl-08__meta">
      <img class="bl-08__avatar" src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=120&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="120" height="120" loading="lazy" decoding="async">
      <p>By <a href="#">Rosalind Achebe</a><span><time datetime="2026-07-28">28 July 2026</time> · 12 min read</span></p>
    </div>
  </header>

  <div class="bl-08__body">
    <p>Manuscript scribes did not invent the initial capital for decoration. They invented it because an unbroken column of text has no entry point, and a reader returning to a page needs to be told, unmistakably, where to begin again. The device is navigational before it is beautiful.</p>

    <aside class="bl-08__pull">
      <p>A drop cap is not ornament. It is the oldest wayfinding element in the history of reading.</p>
    </aside>

    <p>That distinction matters because it changes how you judge the result. If the cap is decoration, any size will do. If it is wayfinding, it has to sit on the baseline grid, it has to be optically aligned with the left edge of the measure, and it has to be large enough to read as a landmark from arm's length — three lines, traditionally, because two reads as an accident and four starts to compete with the headline.</p>

    <p>Pull quotes carry a different job. They are not there to repeat the best sentence; they exist to give a scanning reader a second, shorter version of the argument. A good one is a summary with attitude. A bad one is a sentence you already read, set larger, forty words later.</p>

    <p>The web made both of these harder than they needed to be. For years the only way to sink a capital was a float with a hand-tuned line-height per typeface, and the only way to float a quote was to hope the paragraph was long enough. Both problems now have real answers in the specification, and almost nobody uses them.</p>

    <blockquote class="bl-08__quote">
      <p>“Typography is what language looks like. Get the paragraph wrong and no amount of art direction will save the page.”</p>
      <cite>— Ellen Lupton, <i>Thinking with Type</i></cite>
    </blockquote>

    <p>What changed is small and specific. <code>initial-letter</code> sinks a glyph by a stated number of lines and aligns it to the baseline for you, which is the entire manual tuning problem solved in one declaration. <code>shape-outside</code> lets a floated quote define the shape the text wraps around, rather than the browser assuming a rectangle. <code>hanging-punctuation</code> pushes opening quote marks into the margin so the measure stays visually flush — the detail that separates a set page from a styled one.</p>

    <p>None of this is nostalgia for print. It is the recognition that reading is a physical act with five hundred years of accumulated ergonomics behind it, and that most of those findings were written down. The web's job is not to reinvent the paragraph. It is to stop breaking it.</p>

    <p class="bl-08__coda">Rosalind Achebe teaches typography at the Royal College of Art and writes about reading interfaces.</p>
  </div>
</article>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Archivo:wght@400;500;600;700&display=swap');

.bl-08 {
  --bg: #fcfbf7;
  --text: #191713;
  --muted: #6f6a5f;
  --line: #e3ded1;
  --acc: #7c2d12;
  --measure: 34rem;
  --serif: "EB Garamond",ui-serif,Garamond,Georgia,serif;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-08 {
    --bg: oklch(98.5% .01 90);
    --text: oklch(18% .012 60);
    --muted: oklch(50% .015 70);
    --line: oklch(90% .015 88);
    --acc: oklch(42% .13 42);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-08:not([data-theme="light"]) {
    --bg: #12100d;
    --text: #f3efe6;
    --muted: #a29b8c;
    --line: #2b2721;
    --acc: #fdba74;
  }
}

.bl-08[data-theme="dark"] {
  --bg: #12100d;
  --text: #f3efe6;
  --muted: #a29b8c;
  --line: #2b2721;
  --acc: #fdba74;
}

.bl-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  hanging-punctuation: first last;
}

.bl-08,
.bl-08 *,
.bl-08 *::before,
.bl-08 *::after {
  box-sizing: border-box;
}

.bl-08 a {
  color: inherit;
}

.bl-08 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.bl-08 ::selection {
  background: color-mix(in oklab,var(--acc) 22%,transparent);
}

.bl-08__head {
  max-width: 44rem;
  margin-inline: auto;
  padding: clamp(3rem,8vw,6rem) clamp(1.25rem,5vw,2rem) clamp(1.5rem,3vw,2.5rem);
  display: grid;
  gap: 1.15rem;
}

.bl-08__rubric {
  margin: 0;
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-08__title {
  margin: 0;
  font-weight: 500;
  font-size: clamp(2.125rem,6vw,4rem);
  line-height: 1.02;
  letter-spacing: -.022em;
  text-wrap: balance;
}

.bl-08__standfirst {
  margin: 0;
  font-size: clamp(1.125rem,2.1vw,1.4375rem);
  line-height: 1.55;
  color: var(--muted);
  max-width: 52ch;
  text-wrap: pretty;
}

.bl-08__meta {
  display: flex;
  align-items: center;
  gap: .875rem;
  margin-top: .5rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--line);
}

.bl-08__avatar {
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  object-fit: cover;
  background: var(--line);
}

.bl-08__meta p {
  margin: 0;
  display: grid;
  gap: .1rem;
  font-family: var(--sans);
  font-size: .875rem;
}

.bl-08__meta a {
  font-weight: 600;
  text-decoration: none;
}

.bl-08__meta a:hover {
  color: var(--acc);
}

.bl-08__meta span {
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-08__body {
  max-width: 44rem;
  margin-inline: auto;
  padding: 0 clamp(1.25rem,5vw,2rem) clamp(4rem,10vw,8rem);
  display: flow-root;
  font-size: clamp(1.125rem,1.5vw,1.3125rem);
  line-height: 1.68;
}

.bl-08__body p {
  margin: 0 0 1.15em;
  text-wrap: pretty;
}

.bl-08__body p:first-of-type::first-letter {
  float: inline-start;
  font-family: var(--sans);
  font-weight: 600;
  font-size: 3.4em;
  line-height: .82;
  padding-inline-end: .09em;
  padding-block-start: .02em;
  color: var(--acc);
}

@supports (initial-letter: 3) or (-webkit-initial-letter: 3) {
  .bl-08__body p:first-of-type::first-letter {
    float: none;
    -webkit-initial-letter: 3;
    initial-letter: 3;
    font-size: inherit;
    line-height: normal;
    padding-inline-end: .08em;
  }
}

.bl-08__body p:first-of-type::first-line {
  font-variant-caps: small-caps;
  letter-spacing: .02em;
}

.bl-08__body code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .82em;
  padding: .1em .3em;
  border-radius: .25rem;
  background: color-mix(in oklab,var(--acc) 10%,transparent);
}

.bl-08__pull {
  float: inline-end;
  width: min(48%,20rem);
  margin: .35rem 0 1.1rem 1.75rem;
  shape-outside: inset(0 0 0 1.5rem);
  shape-margin: .6rem;
  padding-inline-start: 1.25rem;
  border-inline-start: 3px solid var(--acc);
}

.bl-08__pull p {
  margin: 0;
  font-size: clamp(1.375rem,2.6vw,1.75rem);
  line-height: 1.24;
  font-weight: 500;
  letter-spacing: -.02em;
  text-wrap: balance;
  color: var(--text);
}

.bl-08__pull:nth-of-type(even) {
  float: inline-start;
  margin: .35rem 1.75rem 1.1rem 0;
  shape-outside: inset(0 1.5rem 0 0);
  border-inline: 0;
  border-inline-end: 3px solid var(--acc);
  padding-inline: 0 1.25rem;
  text-align: end;
}

.bl-08__quote {
  clear: both;
  margin: clamp(1.75rem,4vw,3rem) 0;
  padding: clamp(1.25rem,3vw,2rem) 0;
  border-block: 1px solid var(--line);
  display: grid;
  gap: .75rem;
  text-align: center;
}

.bl-08__quote p {
  margin: 0;
  font-size: clamp(1.25rem,2.4vw,1.625rem);
  line-height: 1.4;
  font-style: italic;
  text-wrap: balance;
}

.bl-08__quote cite {
  font-family: var(--sans);
  font-style: normal;
  font-size: .75rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-08__quote cite i {
  font-style: italic;
  text-transform: none;
  letter-spacing: 0;
}

.bl-08__coda {
  clear: both;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
  font-family: var(--sans);
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
}

@media (max-width: 38rem) {
  .bl-08__pull {
    float: none;
    width: 100%;
    margin: 1.5rem 0;
    shape-outside: none;
  }

  .bl-08__pull:nth-of-type(even) {
    float: none;
    width: 100%;
    margin: 1.5rem 0;
    text-align: start;
    border-inline-end: 0;
    border-inline-start: 3px solid var(--acc);
    padding-inline: 1.25rem 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-08 * {
    transition: none !important;
    animation: none !important;
  }
}
```
