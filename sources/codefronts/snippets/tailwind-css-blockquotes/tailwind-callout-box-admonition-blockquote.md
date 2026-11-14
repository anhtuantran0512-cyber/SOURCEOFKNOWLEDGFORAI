---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/tailwind-callout-box-admonition-blockquote/"
title: "Tailwind Callout Box / Admonition Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Docs-style Note / Tip / Warning admonitions."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Callout Box / Admonition Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/tailwind-callout-box-admonition-blockquote/

Docs-style Note / Tip / Warning admonitions. The CSS original drove all three from one --tone token and [data-kind] selectors; the Tailwind port makes each variant an explicit class list (border-l-tbq03-tip bg-tbq03-tip/8) &mdash; more characters, but every variant is greppable and a reviewer can see exactly what "warning" looks like without reading a stylesheet.
## HTML
```html
<section class="tbq-03 w-full min-h-svh grid place-items-center bg-tbq03-bg px-5 py-14 font-tbq03-sans text-tbq03-ink" aria-label="Callout box admonition blockquote demo">
  <div class="grid w-full justify-items-center gap-6">
    <div class="flex w-full max-w-[600px] flex-col gap-3.5">
      <p aria-hidden="true" class="mb-0.5 font-tbq03-mono text-xs text-tbq03-mut">docs / deploying / <b class="font-semibold text-tbq03-ink">zero-downtime.md</b></p>
      <blockquote class="rounded-r-xl border border-l-4 border-tbq03-note/25 border-l-tbq03-note bg-tbq03-note/8 px-4.5 py-4 shadow-[0_1px_2px_oklch(0_0_0/0.04)]">
        <p class="mb-1.5 flex items-center gap-2 text-[13px] font-bold tracking-[0.02em] text-tbq03-note-ink"><span aria-hidden="true" class="grid size-6 place-items-center rounded-md bg-tbq03-note/15"><svg viewBox="0 0 16 16" width="15" height="15"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 7.2v4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="8" cy="4.9" r=".9" fill="currentColor"/></svg></span>Note</p>
        <p class="text-[14.5px] leading-[1.62] text-tbq03-ink/90 text-pretty">Deploys are atomic. The new release only receives traffic after every health check passes — a failed boot never reaches users.</p>
      </blockquote>
      <blockquote class="rounded-r-xl border border-l-4 border-tbq03-tip/25 border-l-tbq03-tip bg-tbq03-tip/8 px-4.5 py-4 shadow-[0_1px_2px_oklch(0_0_0/0.04)]">
        <p class="mb-1.5 flex items-center gap-2 text-[13px] font-bold tracking-[0.02em] text-tbq03-tip-ink"><span aria-hidden="true" class="grid size-6 place-items-center rounded-md bg-tbq03-tip/15"><svg viewBox="0 0 16 16" width="15" height="15"><path d="M8 1.6a4.6 4.6 0 0 0-2.6 8.4c.5.4.8.9.8 1.5h3.6c0-.6.3-1.1.8-1.5A4.6 4.6 0 0 0 8 1.6z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M6.4 13.6h3.2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></span>Tip</p>
        <p class="text-[14.5px] leading-[1.62] text-tbq03-ink/90 text-pretty">Set <code class="rounded-md bg-tbq03-tip/14 px-1.5 py-px font-tbq03-mono text-[0.86em]">--grace-period=30s</code> so in-flight requests drain before the old release is retired. Your p99 will thank you.</p>
      </blockquote>
      <blockquote class="rounded-r-xl border border-l-4 border-tbq03-warn/35 border-l-tbq03-warn bg-tbq03-warn/10 px-4.5 py-4 shadow-[0_1px_2px_oklch(0_0_0/0.04)]">
        <p class="mb-1.5 flex items-center gap-2 text-[13px] font-bold tracking-[0.02em] text-tbq03-warn-ink"><span aria-hidden="true" class="grid size-6 place-items-center rounded-md bg-tbq03-warn/20"><svg viewBox="0 0 16 16" width="15" height="15"><path d="M8 2 14.6 13.4H1.4z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M8 6.4v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="8" cy="11.4" r=".85" fill="currentColor"/></svg></span>Warning</p>
        <p class="text-[14.5px] leading-[1.62] text-tbq03-ink/90 text-pretty">Skipping migrations with <code class="rounded-md bg-tbq03-warn/18 px-1.5 py-px font-tbq03-mono text-[0.86em]">--no-migrate</code> leaves the schema behind the code. Only do this when the release is verified backwards-compatible.</p>
      </blockquote>
    </div>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq03-mono text-[11.5px] text-tbq03-mut">border-l-4 · bg-tone/8 wash · -ink label tokens</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq03-bg: #f5f7f9;
  --color-tbq03-bg: oklch(0.975 0.004 250);
  --color-tbq03-card: #ffffff;
  --color-tbq03-card: oklch(1 0 0);
  --color-tbq03-ink: #22272e;
  --color-tbq03-ink: oklch(0.27 0.015 260);
  --color-tbq03-mut: #5e646c;
  --color-tbq03-mut: oklch(0.5 0.015 260);
  --color-tbq03-note: #398ad6;
  --color-tbq03-note: oklch(0.62 0.14 250);
  --color-tbq03-note-ink: #155aa7;
  --color-tbq03-note-ink: oklch(0.47 0.14 255);
  --color-tbq03-tip: #2fa465;
  --color-tbq03-tip: oklch(0.64 0.14 155);
  --color-tbq03-tip-ink: #036639;
  --color-tbq03-tip-ink: oklch(0.45 0.11 155);
  --color-tbq03-warn: #e8a127;
  --color-tbq03-warn: oklch(0.76 0.15 75);
  --color-tbq03-warn-ink: #915200;
  --color-tbq03-warn-ink: oklch(0.5 0.12 65);
  --font-tbq03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq03-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-03 {
  width: 100%;
  min-height: 100svh;
}
```
