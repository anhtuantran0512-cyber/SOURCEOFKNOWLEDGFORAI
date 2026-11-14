---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/markdown-compatible-html-blockquote-tailwind/"
title: "Markdown Compatible HTML Blockquote in Tailwind"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Styles bare Markdown output — nested blockquotes, attribution and a GitHub-style Note alert — with zero classes inside the rendered content."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Markdown Compatible HTML Blockquote in Tailwind
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/markdown-compatible-html-blockquote-tailwind/

Styles bare Markdown output — nested blockquotes, attribution and a GitHub-style Note alert — with zero classes inside the rendered content. Every rule lives on the article wrapper as an arbitrary descendant variant ([&_blockquote]:border-s-3), and nesting depth re-points one custom property: [&_blockquote_blockquote]:[--q:var(--color-tbq22-q2)].
## HTML
```html
<section class="tbq-22 w-full min-h-svh grid place-items-center bg-tbq22-bg px-5 py-14 font-tbq22-sans text-tbq22-ink" aria-label="Markdown compatible blockquote styling demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-[62ch]">
      <p aria-hidden="true" class="mb-3.5 inline-flex items-center gap-2 rounded-md border border-black/8 bg-white px-2.5 py-1 font-tbq22-mono text-[11px] text-tbq22-mut">README.md · rendered Markdown — no classes below this line</p>
      <article class="text-[15.5px] leading-[1.7] [&>h1]:mb-3 [&>h1]:border-b [&>h1]:border-black/9 [&>h1]:pb-2 [&>h1]:text-[clamp(22px,3vw,28px)] [&>h1]:font-bold [&>h1]:tracking-[-0.02em] [&>p]:text-tbq22-quiet [&>p]:text-pretty [&_blockquote]:my-[1.2em] [&_blockquote]:rounded-r-lg [&_blockquote]:border-s-3 [&_blockquote]:px-[1.1em] [&_blockquote]:py-[0.85em] [&_blockquote]:[--q:var(--color-tbq22-q1)] [&_blockquote]:[border-color:var(--q)] [&_blockquote]:bg-[color-mix(in_oklch,var(--q)_7%,transparent)] [&_blockquote_blockquote]:mt-[0.7em] [&_blockquote_blockquote]:mb-[0.2em] [&_blockquote_blockquote]:[--q:var(--color-tbq22-q2)] [&_blockquote_blockquote_blockquote]:[--q:var(--color-tbq22-q3)] [&_blockquote_p]:text-[15px] [&_blockquote_p]:text-tbq22-quiet [&_blockquote_p]:text-pretty [&_blockquote_p+p]:mt-[0.7em] [&_blockquote>p:has(cite)]:text-right [&_blockquote>p:has(cite)]:text-[13px] [&_blockquote>p:has(cite)]:text-tbq22-mut [&_cite]:italic [&_[data-alert]]:[--q:var(--color-tbq22-note)] [&_[data-alert]>p:first-child]:flex [&_[data-alert]>p:first-child]:items-center [&_[data-alert]>p:first-child]:gap-2 [&_[data-alert]>p:first-child]:text-[13.5px] [&_[data-alert]>p:first-child]:font-bold [&_[data-alert]>p:first-child]:text-tbq22-note-ink [&_[data-alert]>p+p]:mt-[0.35em]">
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
        <blockquote data-alert="note">
          <p><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 7.2v4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="8" cy="4.9" r=".9" fill="currentColor"/></svg>Note</p>
          <p>First-time contributors: CI runs the full matrix on your fork — expect ~9 minutes before the green check.</p>
        </blockquote>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq22-mono text-[11.5px] text-tbq22-mut">[&amp;_blockquote]: variants · --q per depth · p:has(cite) attribution</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq22-bg: #f6f9fb;
  --color-tbq22-bg: oklch(0.98 0.004 250);
  --color-tbq22-ink: #1b2026;
  --color-tbq22-ink: oklch(0.24 0.015 255);
  --color-tbq22-quiet: #424850;
  --color-tbq22-quiet: oklch(0.4 0.015 255);
  --color-tbq22-mut: #5e646c;
  --color-tbq22-mut: oklch(0.5 0.015 255);
  --color-tbq22-q1: #407bc5;
  --color-tbq22-q1: oklch(0.58 0.13 255);
  --color-tbq22-q2: #8e62bc;
  --color-tbq22-q2: oklch(0.58 0.14 305);
  --color-tbq22-q3: #c25485;
  --color-tbq22-q3: oklch(0.6 0.15 355);
  --color-tbq22-note: #3284d0;
  --color-tbq22-note: oklch(0.6 0.14 250);
  --color-tbq22-note-ink: #155aa7;
  --color-tbq22-note-ink: oklch(0.47 0.14 255);
  --font-tbq22-sans: 'Geist', system-ui, sans-serif;
  --font-tbq22-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-22 {
  width: 100%;
  min-height: 100svh;
}
```
