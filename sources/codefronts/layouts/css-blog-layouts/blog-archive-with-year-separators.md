---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/blog-archive-with-year-separators/"
title: "Blog Archive with Year Separators"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "The archive page a writer actually wants: every post since 2021 in one scannable column, grouped by year, with year labels that stick to the side of the…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blog Archive with Year Separators
Source: https://codefronts.com/layouts/css-blog-layouts/blog-archive-with-year-separators/

The archive page a writer actually wants: every post since 2021 in one scannable column, grouped by year, with year labels that stick to the side of the viewport as you scroll past them. Pure CSS position:sticky — no scroll listeners, no IntersectionObserver, no library.
## HTML
```html
<div class="bl-03">
  <header class="bl-03__head">
    <p class="bl-03__eyebrow">Archive</p>
    <h1 class="bl-03__title">Everything I've written, oldest habit first</h1>
    <p class="bl-03__lede">128 posts since 2021. No categories, no tags to click through — just the whole run, in order, so you can see how the thinking changed.</p>
    <dl class="bl-03__stats">
      <div><dt>Posts</dt><dd>128</dd></div>
      <div><dt>Words</dt><dd>241k</dd></div>
      <div><dt>Longest gap</dt><dd>94 days</dd></div>
    </dl>
  </header>

  <main class="bl-03__main">
    <section class="bl-03__year" aria-labelledby="bl-03-y2026">
      <h2 class="bl-03__yearLabel" id="bl-03-y2026">2026<span>14 posts</span></h2>
      <ol class="bl-03__rows">
        <li class="bl-03__row"><time datetime="2026-08-02">02 Aug</time><a href="#" data-pinned>Writing less, on purpose</a><span>9 min</span></li>
        <li class="bl-03__row"><time datetime="2026-07-19">19 Jul</time><a href="#">The note-taking system I finally deleted</a><span>6 min</span></li>
        <li class="bl-03__row"><time datetime="2026-06-28">28 Jun</time><a href="#">Six months of building in the open</a><span>12 min</span></li>
        <li class="bl-03__row"><time datetime="2026-05-11">11 May</time><a href="#">What I got wrong about design systems</a><span>15 min</span></li>
        <li class="bl-03__row"><time datetime="2026-03-04">04 Mar</time><a href="#">A slower reading list</a><span>4 min</span></li>
      </ol>
    </section>

    <section class="bl-03__year" aria-labelledby="bl-03-y2025">
      <h2 class="bl-03__yearLabel" id="bl-03-y2025">2025<span>31 posts</span></h2>
      <ol class="bl-03__rows">
        <li class="bl-03__row"><time datetime="2025-12-21">21 Dec</time><a href="#">Year notes: the quiet year</a><span>18 min</span></li>
        <li class="bl-03__row"><time datetime="2025-11-02">02 Nov</time><a href="#">Against the second monitor</a><span>5 min</span></li>
        <li class="bl-03__row"><time datetime="2025-09-14">14 Sep</time><a href="#">How I actually use a wiki</a><span>11 min</span></li>
        <li class="bl-03__row"><time datetime="2025-07-30">30 Jul</time><a href="#">The interview question I stole</a><span>7 min</span></li>
        <li class="bl-03__row"><time datetime="2025-04-08">08 Apr</time><a href="#">Notes from a month without feeds</a><span>10 min</span></li>
        <li class="bl-03__row"><time datetime="2025-01-19">19 Jan</time><a href="#">Starting over on the personal site, again</a><span>8 min</span></li>
      </ol>
    </section>

    <section class="bl-03__year" aria-labelledby="bl-03-y2024">
      <h2 class="bl-03__yearLabel" id="bl-03-y2024">2024<span>27 posts</span></h2>
      <ol class="bl-03__rows">
        <li class="bl-03__row"><time datetime="2024-11-11">11 Nov</time><a href="#">Everything is a queue</a><span>6 min</span></li>
        <li class="bl-03__row"><time datetime="2024-08-23">23 Aug</time><a href="#">On keeping a work journal for five years</a><span>13 min</span></li>
        <li class="bl-03__row"><time datetime="2024-06-01">01 Jun</time><a href="#">The cost of a good default</a><span>9 min</span></li>
        <li class="bl-03__row"><time datetime="2024-02-17">17 Feb</time><a href="#">Learning CSS a third time</a><span>14 min</span></li>
      </ol>
    </section>

    <section class="bl-03__year" aria-labelledby="bl-03-y2023">
      <h2 class="bl-03__yearLabel" id="bl-03-y2023">2023<span>22 posts</span></h2>
      <ol class="bl-03__rows">
        <li class="bl-03__row"><time datetime="2023-10-05">05 Oct</time><a href="#">Small tools, sharp edges</a><span>7 min</span></li>
        <li class="bl-03__row"><time datetime="2023-07-12">12 Jul</time><a href="#">Why my blog has no comments</a><span>5 min</span></li>
        <li class="bl-03__row"><time datetime="2023-03-29">29 Mar</time><a href="#">Reading papers as a practitioner</a><span>16 min</span></li>
      </ol>
    </section>
  </main>

  <footer class="bl-03__footer">
    <p>Want the older stuff? <a href="#">2021—2022 lives here</a>, unedited.</p>
  </footer>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,400&family=DM+Mono:wght@400;500&display=swap');

.bl-03 {
  --bg: #f6f5f2;
  --text: #1a1a17;
  --muted: #77746c;
  --line: #dedbd3;
  --acc: #3f6212;
  --row-pad: .9rem;
  --serif: "Newsreader",ui-serif,Georgia,serif;
  --mono: "DM Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}

@supports (color: oklch(50% 0 0)) {
  .bl-03 {
    --bg: oklch(97% .006 95);
    --text: oklch(20% .008 80);
    --muted: oklch(55% .012 85);
    --line: oklch(89% .01 92);
    --acc: oklch(48% .13 130);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-03:not([data-theme="light"]) {
    --bg: #121210;
    --text: #efeee9;
    --muted: #a09d95;
    --line: #2a2a26;
    --acc: #a3e635;
  }
}

.bl-03[data-theme="dark"] {
  --bg: #121210;
  --text: #efeee9;
  --muted: #a09d95;
  --line: #2a2a26;
  --acc: #a3e635;
}

.bl-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
}

.bl-03,
.bl-03 *,
.bl-03 *::before,
.bl-03 *::after {
  box-sizing: border-box;
}

.bl-03 a {
  color: inherit;
  text-decoration: none;
}

.bl-03 a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.bl-03 ::selection {
  background: color-mix(in oklab,var(--acc) 25%,transparent);
}

.bl-03__head {
  max-width: 72rem;
  margin-inline: auto;
  padding: clamp(3rem,9vw,7rem) clamp(1.25rem,5vw,3rem) clamp(2rem,4vw,3rem);
  display: grid;
  gap: 1.25rem;
}

.bl-03__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-03__title {
  margin: 0;
  font-weight: 400;
  font-size: clamp(2rem,5.5vw,3.75rem);
  line-height: 1.04;
  letter-spacing: -.025em;
  max-width: 26ch;
  text-wrap: balance;
}

.bl-03__lede {
  margin: 0;
  font-size: clamp(1rem,1.4vw,1.1875rem);
  line-height: 1.7;
  color: var(--muted);
  max-width: 58ch;
  text-wrap: pretty;
}

.bl-03__stats {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 2.5rem;
  margin: .5rem 0 0;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
}

.bl-03__stats div {
  display: grid;
  gap: .2rem;
}

.bl-03__stats dt {
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-03__stats dd {
  margin: 0;
  font-size: 1.5rem;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.bl-03__main {
  max-width: 72rem;
  margin-inline: auto;
  padding: 0 clamp(1.25rem,5vw,3rem) clamp(3rem,6vw,5rem);
}

.bl-03__year {
  display: grid;
  grid-template-columns: 8rem minmax(0,1fr);
  gap: clamp(1rem,3vw,2.5rem);
  padding-block: clamp(1.5rem,3vw,2.5rem);
  border-top: 1px solid var(--line);
}

.bl-03__yearLabel {
  position: sticky;
  top: 2rem;
  align-self: start;
  margin: 0;
  font-family: var(--mono);
  font-weight: 500;
  font-size: 1.125rem;
  letter-spacing: .02em;
  display: grid;
  gap: .35rem;
  font-variant-numeric: tabular-nums;
}

.bl-03__yearLabel span {
  font-size: .6875rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-03__rows {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
}

.bl-03__row {
  display: grid;
  grid-template-columns: 5.5rem minmax(0,1fr) auto;
  gap: .5rem 1.25rem;
  align-items: baseline;
  padding-block: var(--row-pad);
  border-bottom: 1px solid color-mix(in oklab,var(--line) 65%,transparent);
  position: relative;
}

.bl-03__row:last-child {
  border-bottom: 0;
}

.bl-03__row time {
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  letter-spacing: .02em;
}

.bl-03__row a {
  font-size: clamp(1.0625rem,1.8vw,1.375rem);
  line-height: 1.25;
  letter-spacing: -.012em;
  text-wrap: pretty;
  background: linear-gradient(var(--acc),var(--acc)) 0 100%/0 1px no-repeat;
  transition: background-size .35s cubic-bezier(.16,1,.3,1), color .2s ease;
}

.bl-03__row a:hover {
  background-size: 100% 1px;
  color: var(--acc);
}

.bl-03__row span {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-03__row:has([data-pinned]) a::after {
  content: "Pinned";
  margin-inline-start: .6rem;
  padding: .15rem .4rem;
  border: 1px solid var(--acc);
  border-radius: .25rem;
  font-family: var(--mono);
  font-size: .5625rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--acc);
  vertical-align: .15em;
}

.bl-03__footer {
  max-width: 72rem;
  margin-inline: auto;
  padding: 0 clamp(1.25rem,5vw,3rem) clamp(3rem,8vw,6rem);
  font-size: .9375rem;
  color: var(--muted);
}

.bl-03__footer p {
  margin: 0;
}

.bl-03__footer a {
  color: var(--text);
  text-decoration: underline;
  text-underline-offset: .25em;
  text-decoration-color: var(--acc);
}

@media (max-width: 44rem) {
  .bl-03__year {
    grid-template-columns: minmax(0,1fr);
    gap: 1rem;
  }

  .bl-03__yearLabel {
    position: sticky;
    top: 0;
    z-index: 2;
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    padding: .6rem .75rem;
    border-radius: .375rem;
    background: color-mix(in oklab,var(--bg) 92%,var(--text));
  }

  @supports (backdrop-filter: blur(6px)) {
    .bl-03__yearLabel {
      background: color-mix(in oklab,var(--bg) 80%,transparent);
      backdrop-filter: blur(10px);
    }
  }

  .bl-03__row {
    grid-template-columns: minmax(0,1fr) auto;
  }

  .bl-03__row time {
    grid-column: 1/-1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-03 * {
    transition: none !important;
    animation: none !important;
  }
}
```
