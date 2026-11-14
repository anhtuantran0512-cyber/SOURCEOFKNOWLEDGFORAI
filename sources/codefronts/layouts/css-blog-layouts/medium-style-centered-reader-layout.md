---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/medium-style-centered-reader-layout/"
title: "Medium Style Centered Reader Layout"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "The reading layout that quietly beats every clever one: a single centered column measured in ch, line-height that scales with the measure, spacing set by the…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Medium Style Centered Reader Layout
Source: https://codefronts.com/layouts/css-blog-layouts/medium-style-centered-reader-layout/

The reading layout that quietly beats every clever one: a single centered column measured in ch, line-height that scales with the measure, spacing set by the flow rather than per-element margins, and breakout media that escapes the column without a single negative margin. This is the baseline every article page should start from.
## HTML
```html
<div class="bl-09">
  <header class="bl-09__bar">
    <a class="bl-09__home" href="#">Ledger</a>
    <p class="bl-09__crumb">Engineering culture</p>
    <div class="bl-09__actions">
      <button type="button" aria-pressed="false"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M6 3h8v14l-4-3.2L6 17z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg><span>Save</span></button>
      <button type="button"><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 13V3m0 0L6.5 6.5M10 3l3.5 3.5M4 13v3h12v-3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Share</span></button>
    </div>
  </header>

  <article class="bl-09__prose">
    <p class="bl-09__tag">Essay</p>
    <h1>What I learned reviewing 4,000 pull requests</h1>
    <div class="bl-09__author">
      <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="120" height="120" loading="lazy" decoding="async">
      <p><a href="#">Tomás Ferreira</a><span><time datetime="2026-08-01">1 Aug 2026</time> · 9 min read · <a href="#">Engineering</a></span></p>
    </div>

    <p class="bl-09__lede">Four years, two companies, roughly four thousand reviews. The single biggest thing I got wrong was thinking the review was about the code.</p>

    <p>A review is a conversation with a deadline attached. Most of the friction I caused early on came from treating it as an inspection: I read the diff, I found the defects, I listed them. Technically correct, socially expensive, and slow — because the author then had to reverse-engineer which comments were blocking and which were taste.</p>

    <h2>Say what kind of comment it is</h2>
    <p>The highest-leverage change I made was labelling every comment with its intent. Four prefixes covered ninety percent of everything I ever wrote: <strong>blocking</strong>, <strong>question</strong>, <strong>suggestion</strong>, <strong>nit</strong>. Nothing else about my reviews changed and cycle time dropped by roughly a third, because authors stopped guessing.</p>
    <p>This is not a process innovation. It is just being explicit about something reviewers have always kept in their heads and assumed was obvious from tone. It never is, especially in writing, especially across time zones.</p>

    <figure>
      <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1400&amp;q=70&amp;auto=format&amp;fit=crop" alt="Two developers reviewing code together at a laptop" width="1400" height="800" loading="lazy" decoding="async">
      <figcaption>The best reviews I gave were the ones I gave in person, and then wrote down.</figcaption>
    </figure>

    <h2>Review the change, not the file</h2>
    <p>A diff invites you to evaluate lines. What actually matters is whether the change achieves what the description says, whether it can be reverted safely, and whether the next person reading this code in eight months will be able to tell why it exists. None of those questions are answerable line by line.</p>
    <blockquote>
      <p>If I can't tell what the change is for from the title and the tests, that's the review comment. Everything else is premature.</p>
    </blockquote>
    <p>The corollary is uncomfortable: a lot of my careful line-level feedback was noise. Useful noise, occasionally. But it competed for attention with the two or three comments that actually mattered, and attention is the scarce resource in a review, not correctness.</p>

    <h2>The rule I'd keep</h2>
    <p>Approve with comments more often than you think you should. A blocked pull request costs a context switch on both sides; a trusted colleague with three suggestions and an approval will address the good ones and ignore the bad ones, which is the correct outcome anyway.</p>
    <p>Four thousand reviews later, the checklist I actually use has three items: does the description explain the why, can this be reverted, and would I be able to debug it at 3am. The rest is negotiable.</p>

    <hr>
    <p class="bl-09__coda">Tomás writes about engineering practice at <a href="#">ledger.dev</a>. Reply by email — there are no comments here on purpose.</p>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,[email protected],400;8..60,600;8..60,700&family=Schibsted+Grotesk:wght@400;500;600&display=swap');

.bl-09 {
  --bg: #ffffff;
  --text: #18181b;
  --muted: #6b7280;
  --line: #e5e7eb;
  --acc: #166534;
  --measure: 65ch;
  --serif: "Source Serif 4",ui-serif,Georgia,serif;
  --sans: "Schibsted Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-09 {
    --bg: oklch(100% 0 0);
    --text: oklch(20% .006 275);
    --muted: oklch(53% .015 265);
    --line: oklch(92% .005 265);
    --acc: oklch(45% .12 150);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-09:not([data-theme="light"]) {
    --bg: #0c0d0f;
    --text: #eceef1;
    --muted: #9aa1ab;
    --line: #23262b;
    --acc: #6ee7a8;
  }
}

.bl-09[data-theme="dark"] {
  --bg: #0c0d0f;
  --text: #eceef1;
  --muted: #9aa1ab;
  --line: #23262b;
  --acc: #6ee7a8;
}

.bl-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
}

.bl-09,
.bl-09 *,
.bl-09 *::before,
.bl-09 *::after {
  box-sizing: border-box;
}

.bl-09 a {
  color: inherit;
}

.bl-09 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.bl-09 ::selection {
  background: color-mix(in oklab,var(--acc) 22%,transparent);
}

.bl-09__bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: .6rem clamp(1rem,4vw,2rem);
  border-bottom: 1px solid var(--line);
  background: color-mix(in oklab,var(--bg) 88%,transparent);
  font-family: var(--sans);
}

@supports (backdrop-filter: blur(6px)) {
  .bl-09__bar {
    backdrop-filter: blur(12px);
  }
}

.bl-09__home {
  font-weight: 600;
  font-size: 1.0625rem;
  letter-spacing: -.02em;
  text-decoration: none;
}

.bl-09__crumb {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  padding-inline-start: 1rem;
  border-inline-start: 1px solid var(--line);
}

.bl-09__actions {
  margin-inline-start: auto;
  display: flex;
  gap: .4rem;
}

.bl-09__actions button {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  padding: 0 .75rem;
  border: 1px solid transparent;
  border-radius: 999px;
  background: transparent;
  color: var(--muted);
  font-family: inherit;
  font-size: .8125rem;
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.bl-09__actions button svg {
  width: 1.05rem;
  height: 1.05rem;
}

.bl-09__actions button:hover {
  background: color-mix(in oklab,var(--text) 6%,transparent);
  color: var(--text);
}

.bl-09__actions button[aria-pressed="true"] {
  color: var(--acc);
}

@media (max-width: 34rem) {
  .bl-09__actions button span {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip-path: inset(50%);
  }

  .bl-09__crumb {
    display: none;
  }
}

.bl-09__prose {
  display: grid;
  grid-template-columns: [wide-start] minmax(1.25rem,1fr) [narrow-start] min(var(--measure),100% - 2.5rem) [narrow-end] minmax(1.25rem,1fr) [wide-end];
  padding-block: clamp(2.5rem,6vw,4.5rem) clamp(4rem,10vw,7rem);
  font-size: clamp(1.125rem,1.35vw,1.25rem);
  line-height: 1.75;
}

.bl-09__prose > * {
  grid-column: narrow;
  margin: 0;
}

.bl-09__prose > * + * {
  margin-block-start: var(--flow,1.5em);
}

.bl-09__tag {
  --flow: 0;
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-09__prose h1 {
  --flow: .5em;
  font-size: clamp(2rem,5vw,3.25rem);
  font-weight: 700;
  line-height: 1.06;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.bl-09__author {
  --flow: 1.4em;
  display: flex;
  align-items: center;
  gap: .75rem;
  font-family: var(--sans);
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--line);
}

.bl-09__author img {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  object-fit: cover;
  background: var(--line);
}

.bl-09__author p {
  margin: 0;
  display: grid;
  gap: .1rem;
  font-size: .875rem;
}

.bl-09__author a {
  font-weight: 600;
  text-decoration: none;
}

.bl-09__author span {
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-09__author span a {
  color: var(--acc);
  font-weight: 500;
}

.bl-09__lede {
  font-size: 1.25em;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-09__prose h2 {
  --flow: 2.4em;
  font-family: var(--sans);
  font-size: clamp(1.25rem,2.4vw,1.625rem);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-09__prose h2 + p {
  --flow: .9em;
}

.bl-09__prose p {
  text-wrap: pretty;
}

.bl-09__prose strong {
  font-weight: 600;
}

.bl-09__prose figure {
  --flow: 2.6em;
  grid-column: wide;
  display: grid;
  gap: .65rem;
  justify-items: center;
}

.bl-09__prose figure img {
  display: block;
  width: 100%;
  max-width: 74rem;
  height: auto;
  aspect-ratio: 7/4;
  object-fit: cover;
  border-radius: .5rem;
  background: var(--line);
}

.bl-09__prose figcaption {
  max-width: 52ch;
  font-family: var(--sans);
  font-size: .8125rem;
  line-height: 1.5;
  color: var(--muted);
  text-align: center;
}

.bl-09__prose blockquote {
  --flow: 2.2em;
  margin: 0;
  padding-inline-start: 1.25rem;
  border-inline-start: 3px solid var(--acc);
}

.bl-09__prose blockquote p {
  font-size: 1.15em;
  line-height: 1.5;
  font-style: italic;
  letter-spacing: -.01em;
  text-wrap: pretty;
}

.bl-09__prose hr {
  --flow: 3em;
  width: 4rem;
  height: 1px;
  border: 0;
  background: var(--line);
  justify-self: center;
}

.bl-09__coda {
  --flow: 1.5em;
  font-family: var(--sans);
  font-size: .875rem;
  line-height: 1.65;
  color: var(--muted);
}

.bl-09__coda a {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: .2em;
}

@media (prefers-reduced-motion: reduce) {
  .bl-09 * {
    transition: none !important;
    animation: none !important;
  }
}
```
