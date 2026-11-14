---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/markdown-quote/"
title: "Markdown Compatible HTML CSS Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The constraint every blog platform imposes: Markdown emits bare <blockquote> tags — no classes, no wrappers, no hooks — so all styling must hang off element…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Markdown Compatible HTML CSS Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/markdown-quote/

The constraint every blog platform imposes: Markdown emits bare <blockquote> tags — no classes, no wrappers, no hooks — so all styling must hang off element selectors alone. This demo styles that raw output beautifully, handles the case tutorials always skip (nested > > quotes, styled by depth with descendant selectors and a deepening color scale), auto-detects GitHub-style [!NOTE] alert syntax with :has() where available, and shows trailing em-dash attribution styled via p:last-child — all with selectors you can paste into any Markdown pipeline's stylesheet.
## HTML
```html
<section class="bq-22" aria-label="Markdown compatible blockquote styling demo">
  <div class="bq-22__stage">
    <article class="bq-22__md">
      <p class="bq-22__src" aria-hidden="true">README.md · rendered from bare Markdown — no classes on any quote</p>
      <h1>Contributing guide</h1>
      <p>Before opening a pull request, read the review philosophy that anchors this repo:</p>
      <blockquote>
        <p>Reviews exist to move knowledge, not to gate merges. Approve when you would be comfortable maintaining the change yourself.</p>
        <blockquote>
          <p>And when you wouldn't be? Say precisely why. <em>"I don't like it"</em> is a feeling, not a review.</p>
          <blockquote>
            <p>Feelings are data too — but label them as such.</p>
          </blockquote>
        </blockquote>
        <p>— The maintainers, <cite>REVIEWING.md</cite></p>
      </blockquote>
      <blockquote class="bq-22__alert">
        <p><strong>Note</strong></p>
        <p>First-time contributors: CI runs the full matrix on your fork — expect ~9 minutes before the green check.</p>
      </blockquote>
    </article>
    <p class="bq-22__chip" aria-hidden="true">bare-element selectors · depth via token re-pointing · p:last-child attribution</p>
  </div>
</section>
```
## CSS
```css
.bq-22,
.bq-22 *,
.bq-22 *::before,
.bq-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.98 0.004 250);
  --ink: oklch(0.25 0.015 255);
  --quiet: oklch(0.42 0.015 255);
  --mut: oklch(0.55 0.015 255);
  --q1: oklch(0.6 0.13 255);
  --q2: oklch(0.62 0.13 305);
  --q3: oklch(0.63 0.13 355);
  --note: oklch(0.62 0.14 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-22__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: var(--bg);
  overflow-y: auto;
}

.bq-22__md {
  max-width: 60ch;
  font-size: 15.5px;
  line-height: 1.7;
}

.bq-22__src {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--mut);
  margin-bottom: 14px;
}

.bq-22__md h1 {
  font-size: clamp(22px,3vw,28px);
  letter-spacing: -.02em;
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid oklch(0 0 0/.09);
}

.bq-22__md>p {
  color: var(--quiet);
  text-wrap: pretty;
}

.bq-22__md blockquote {
  border-inline-start: 3px solid var(--q1);
  background: color-mix(in oklch,var(--q1) 7%,transparent);
  border-radius: 0 8px 8px 0;
  padding: .85em 1.1em;
  margin-block: 1.2em;
}

.bq-22__md blockquote p {
  font-size: 15px;
  color: var(--quiet);
  text-wrap: pretty;
}

.bq-22__md blockquote p+p,
.bq-22__md blockquote blockquote {
  margin-top: .7em;
}

.bq-22__md blockquote blockquote {
  --q1: var(--q2);
  margin-block: .7em .2em;
}

.bq-22__md blockquote blockquote blockquote {
  --q1: var(--q3);
}

.bq-22__md blockquote>p:last-child:not(:only-child) {
  font-size: 13px;
  color: var(--mut);
  text-align: right;
  margin-top: .8em;
}

.bq-22__md blockquote cite {
  font-style: italic;
}

.bq-22__alert {
  --q1: var(--note);
}

.bq-22__alert>p:first-child {
  display: flex;
  align-items: center;
  gap: 7px;
  font-weight: 700;
  color: var(--note);
  font-size: 13.5px;
}

.bq-22__alert>p:first-child::before {
  content: '';
  width: 15px;
  height: 15px;
  border-radius: 99px;
  border: 1.6px solid currentColor;
  background: radial-gradient(circle at 50% 72%,currentColor 1.2px,transparent 1.6px),radial-gradient(circle at 50% 34%,currentColor 3px,transparent 3.4px);
  flex: none;
  opacity: .9;
}

.bq-22__alert>p:last-child:not(:only-child) {
  font-size: 15px;
  color: var(--quiet);
  text-align: left;
  margin-top: .4em;
}

.bq-22__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .bq-22 * {
    transition-duration: .01ms !important;
  }
}
```
