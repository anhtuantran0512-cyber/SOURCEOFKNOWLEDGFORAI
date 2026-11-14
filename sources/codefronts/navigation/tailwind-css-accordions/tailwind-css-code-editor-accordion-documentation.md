---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-code-editor-accordion-documentation/"
title: "Tailwind CSS Code Editor Accordion for Documentation"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "Documentation that looks like the editor your readers live in: each <summary> is a // comment line with a fold chevron in a line-numbered gutter, and opening…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Code Editor Accordion for Documentation
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-code-editor-accordion-documentation/

Documentation that looks like the editor your readers live in: each <summary> is a // comment line with a fold chevron in a line-numbered gutter, and opening it unfolds a syntax-highlighted <pre> beneath, Tokyo Night palette included. Line numbers are a CSS counter written entirely in utilities ([counter-reset:tac19-ln], before:content-[counter(tac19-ln)]), so they re-number as folds open and close, just as VS Code does.
## HTML
```html
<section class="tac-19 w-full min-h-svh grid place-items-center bg-tac19-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tac19-glow),transparent_70%)] px-5 py-14 font-tac19-sans text-tac19-fg [interpolate-size:allow-keywords]" aria-label="Code editor documentation accordion demo">
  <div class="grid w-full grid-cols-[minmax(0,1fr)] justify-items-center gap-7">
    <div class="w-full min-w-0 max-w-[720px]">
      <header class="mb-5">
        <p class="font-tac19-mono text-xs text-tac19-mut">Docs <span aria-hidden="true">/</span> Node SDK <span aria-hidden="true">/</span> <span class="text-tac19-fg">Quickstart</span></p>
        <h2 class="mt-2 text-[clamp(22px,3.4vw,28px)] font-semibold tracking-[-0.02em] text-white">Ship your first request in four folds</h2>
        <p class="mt-1.5 max-w-[56ch] text-[15px] leading-relaxed text-tac19-mut text-pretty">Each comment is a question. Unfold it for the answer; line numbers keep counting like your editor does.</p>
      </header>

      <div class="overflow-hidden rounded-2xl bg-tac19-editor shadow-[0_1px_0_oklch(1_0_0/0.05)_inset,0_40px_90px_-35px_oklch(0_0_0/0.85)] ring-1 ring-white/8">
        <div class="flex items-center gap-4 bg-tac19-chrome px-4 pt-3" aria-hidden="true">
          <span class="flex gap-2 pb-3"><i class="size-3 rounded-full bg-[#f7768e]"></i><i class="size-3 rounded-full bg-[#e0af68]"></i><i class="size-3 rounded-full bg-[#9ece6a]"></i></span>
          <span class="flex min-w-0 items-end gap-1 overflow-hidden font-tac19-mono text-xs">
            <span class="flex items-center gap-2 rounded-t-lg border-t-2 border-tac19-fn bg-tac19-editor px-3.5 py-2 text-tac19-fg"><b class="font-semibold text-tac19-type">TS</b>quickstart.ts</span>
            <span class="flex items-center gap-2 px-3.5 py-2 text-tac19-mut max-sm:hidden"><b class="font-semibold text-tac19-num">{}</b>package.json</span>
            <span class="flex items-center gap-2 px-3.5 py-2 text-tac19-mut max-sm:hidden"><b class="font-semibold text-tac19-fn">M↓</b>README.md</span>
          </span>
        </div>
        <p class="border-b border-white/6 px-4 py-1.5 font-tac19-mono text-[11.5px] text-tac19-mut" aria-hidden="true">acme-sdk › examples › <span class="text-tac19-fg">quickstart.ts</span></p>
        <div class="py-3 font-tac19-mono text-[12.5px] sm:text-[13.5px] [counter-reset:tac19-ln]">
        <details class="group [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-400 [&::details-content]:ease-[cubic-bezier(.2,.8,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none" open>
          <summary class="relative flex min-h-11 cursor-pointer list-none items-center gap-2.5 py-2 pr-4 pl-[4.5rem] text-tac19-cm italic transition-colors [counter-increment:tac19-ln] before:absolute before:left-0 before:w-10 before:text-right before:text-[12px] before:not-italic before:text-tac19-gut before:content-[counter(tac19-ln)] hover:bg-white/[0.03] hover:text-tac19-cmh group-open:bg-tac19-line group-open:text-tac19-cmh group-open:before:text-tac19-fg focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac19-fn [&::-webkit-details-marker]:hidden"><svg class="absolute left-[2.85rem] size-3.5 -rotate-90 text-tac19-gut transition-transform duration-200 group-hover:text-tac19-fg group-open:rotate-0 group-open:text-tac19-fg motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6 8 10l4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span>// 1 · Install the SDK and authenticate</span><span class="shrink-0 whitespace-nowrap rounded-md bg-tac19-fn/10 px-1.5 py-px text-[11px] not-italic text-tac19-fn ring-1 ring-tac19-fn/25 group-open:hidden max-sm:hidden" aria-hidden="true">{…} 6 lines</span></summary>
<pre class="relative overflow-x-auto pr-4 pb-2 pl-[4.5rem] leading-[1.8] text-tac19-fg before:absolute before:top-0 before:bottom-2 before:left-[3.3rem] before:w-px before:bg-tac19-guide [&>code>span]:relative [&>code>span]:[counter-increment:tac19-ln] [&>code>span]:before:absolute [&>code>span]:before:-left-[4.5rem] [&>code>span]:before:w-10 [&>code>span]:before:text-right [&>code>span]:before:text-[12px] [&>code>span]:before:text-tac19-gut [&>code>span]:before:content-[counter(tac19-ln)]"><code><span><b class="font-normal text-tac19-kw">import</b> { <em class="not-italic text-tac19-type">Acme</em> } <b class="font-normal text-tac19-kw">from</b> <i class="not-italic text-tac19-str">'@acme/sdk'</i>;</span>
<span></span>
<span><b class="font-normal text-tac19-kw">const</b> acme <em class="not-italic text-tac19-op">=</em> <b class="font-normal text-tac19-kw">new</b> <em class="not-italic text-tac19-fn">Acme</em>({</span>
<span>  <em class="not-italic text-tac19-prop">apiKey</em>: process.env.<em class="not-italic text-tac19-prop">ACME_KEY</em>, <em class="text-tac19-cm">// server-side only</em></span>
<span>  <em class="not-italic text-tac19-prop">region</em>: <i class="not-italic text-tac19-str">'eu-west-1'</i>,</span>
<span>});</span></code></pre>
        </details>
        <details class="group [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-400 [&::details-content]:ease-[cubic-bezier(.2,.8,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none">
          <summary class="relative flex min-h-11 cursor-pointer list-none items-center gap-2.5 py-2 pr-4 pl-[4.5rem] text-tac19-cm italic transition-colors [counter-increment:tac19-ln] before:absolute before:left-0 before:w-10 before:text-right before:text-[12px] before:not-italic before:text-tac19-gut before:content-[counter(tac19-ln)] hover:bg-white/[0.03] hover:text-tac19-cmh group-open:bg-tac19-line group-open:text-tac19-cmh group-open:before:text-tac19-fg focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac19-fn [&::-webkit-details-marker]:hidden"><svg class="absolute left-[2.85rem] size-3.5 -rotate-90 text-tac19-gut transition-transform duration-200 group-hover:text-tac19-fg group-open:rotate-0 group-open:text-tac19-fg motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6 8 10l4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span>// 2 · Fetch a single record</span><span class="shrink-0 whitespace-nowrap rounded-md bg-tac19-fn/10 px-1.5 py-px text-[11px] not-italic text-tac19-fn ring-1 ring-tac19-fn/25 group-open:hidden max-sm:hidden" aria-hidden="true">{…} 2 lines</span></summary>
<pre class="relative overflow-x-auto pr-4 pb-2 pl-[4.5rem] leading-[1.8] text-tac19-fg before:absolute before:top-0 before:bottom-2 before:left-[3.3rem] before:w-px before:bg-tac19-guide [&>code>span]:relative [&>code>span]:[counter-increment:tac19-ln] [&>code>span]:before:absolute [&>code>span]:before:-left-[4.5rem] [&>code>span]:before:w-10 [&>code>span]:before:text-right [&>code>span]:before:text-[12px] [&>code>span]:before:text-tac19-gut [&>code>span]:before:content-[counter(tac19-ln)]"><code><span><b class="font-normal text-tac19-kw">const</b> order <em class="not-italic text-tac19-op">=</em> <b class="font-normal text-tac19-kw">await</b> acme.orders.<em class="not-italic text-tac19-fn">get</em>(<i class="not-italic text-tac19-str">'ord_8h2k'</i>);</span>
<span>console.<em class="not-italic text-tac19-fn">log</em>(order.<em class="not-italic text-tac19-prop">status</em>); <em class="text-tac19-cm">// "shipped"</em></span></code></pre>
        </details>
        <details class="group [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-400 [&::details-content]:ease-[cubic-bezier(.2,.8,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none">
          <summary class="relative flex min-h-11 cursor-pointer list-none items-center gap-2.5 py-2 pr-4 pl-[4.5rem] text-tac19-cm italic transition-colors [counter-increment:tac19-ln] before:absolute before:left-0 before:w-10 before:text-right before:text-[12px] before:not-italic before:text-tac19-gut before:content-[counter(tac19-ln)] hover:bg-white/[0.03] hover:text-tac19-cmh group-open:bg-tac19-line group-open:text-tac19-cmh group-open:before:text-tac19-fg focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac19-fn [&::-webkit-details-marker]:hidden"><svg class="absolute left-[2.85rem] size-3.5 -rotate-90 text-tac19-gut transition-transform duration-200 group-hover:text-tac19-fg group-open:rotate-0 group-open:text-tac19-fg motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6 8 10l4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span>// 3 · Paginate without the bookkeeping</span><span class="shrink-0 whitespace-nowrap rounded-md bg-tac19-fn/10 px-1.5 py-px text-[11px] not-italic text-tac19-fn ring-1 ring-tac19-fn/25 group-open:hidden max-sm:hidden" aria-hidden="true">{…} 4 lines</span></summary>
<pre class="relative overflow-x-auto pr-4 pb-2 pl-[4.5rem] leading-[1.8] text-tac19-fg before:absolute before:top-0 before:bottom-2 before:left-[3.3rem] before:w-px before:bg-tac19-guide [&>code>span]:relative [&>code>span]:[counter-increment:tac19-ln] [&>code>span]:before:absolute [&>code>span]:before:-left-[4.5rem] [&>code>span]:before:w-10 [&>code>span]:before:text-right [&>code>span]:before:text-[12px] [&>code>span]:before:text-tac19-gut [&>code>span]:before:content-[counter(tac19-ln)]"><code><span><b class="font-normal text-tac19-kw">let</b> total <em class="not-italic text-tac19-op">=</em> <em class="not-italic text-tac19-num">0</em>;</span>
<span><b class="font-normal text-tac19-kw">for await</b> (<b class="font-normal text-tac19-kw">const</b> invoice <b class="font-normal text-tac19-kw">of</b> acme.invoices.<em class="not-italic text-tac19-fn">list</em>({ <em class="not-italic text-tac19-prop">limit</em>: <em class="not-italic text-tac19-num">50</em> })) {</span>
<span>  total <em class="not-italic text-tac19-op">+=</em> invoice.<em class="not-italic text-tac19-prop">amount</em>;</span>
<span>}</span></code></pre>
        </details>
        <details class="group [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-400 [&::details-content]:ease-[cubic-bezier(.2,.8,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none">
          <summary class="relative flex min-h-11 cursor-pointer list-none items-center gap-2.5 py-2 pr-4 pl-[4.5rem] text-tac19-cm italic transition-colors [counter-increment:tac19-ln] before:absolute before:left-0 before:w-10 before:text-right before:text-[12px] before:not-italic before:text-tac19-gut before:content-[counter(tac19-ln)] hover:bg-white/[0.03] hover:text-tac19-cmh group-open:bg-tac19-line group-open:text-tac19-cmh group-open:before:text-tac19-fg focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac19-fn [&::-webkit-details-marker]:hidden"><svg class="absolute left-[2.85rem] size-3.5 -rotate-90 text-tac19-gut transition-transform duration-200 group-hover:text-tac19-fg group-open:rotate-0 group-open:text-tac19-fg motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6 8 10l4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span>// 4 · Handle rate limits and errors</span><span class="shrink-0 whitespace-nowrap rounded-md bg-tac19-fn/10 px-1.5 py-px text-[11px] not-italic text-tac19-fn ring-1 ring-tac19-fn/25 group-open:hidden max-sm:hidden" aria-hidden="true">{…} 6 lines</span></summary>
<pre class="relative overflow-x-auto pr-4 pb-2 pl-[4.5rem] leading-[1.8] text-tac19-fg before:absolute before:top-0 before:bottom-2 before:left-[3.3rem] before:w-px before:bg-tac19-guide [&>code>span]:relative [&>code>span]:[counter-increment:tac19-ln] [&>code>span]:before:absolute [&>code>span]:before:-left-[4.5rem] [&>code>span]:before:w-10 [&>code>span]:before:text-right [&>code>span]:before:text-[12px] [&>code>span]:before:text-tac19-gut [&>code>span]:before:content-[counter(tac19-ln)]"><code><span><b class="font-normal text-tac19-kw">try</b> {</span>
<span>  <b class="font-normal text-tac19-kw">await</b> acme.orders.<em class="not-italic text-tac19-fn">create</em>(payload);</span>
<span>} <b class="font-normal text-tac19-kw">catch</b> (err) {</span>
<span>  <b class="font-normal text-tac19-kw">if</b> (err <b class="font-normal text-tac19-kw">instanceof</b> <em class="not-italic text-tac19-type">RateLimitError</em>) <b class="font-normal text-tac19-kw">return</b> <em class="not-italic text-tac19-fn">retry</em>(err.<em class="not-italic text-tac19-prop">retryAfter</em>);</span>
<span>  <b class="font-normal text-tac19-kw">throw</b> err; <em class="text-tac19-cm">// everything else is yours</em></span>
<span>}</span></code></pre>
        </details>
        </div>
        <div class="flex flex-wrap items-center gap-x-4 gap-y-1 bg-tac19-chrome px-4 py-1.5 font-tac19-mono text-[11px] text-tac19-mut" aria-hidden="true">
          <span class="flex items-center gap-1.5 text-tac19-fn"><svg class="size-3" viewBox="0 0 16 16"><circle cx="4.5" cy="3.5" r="1.8" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="4.5" cy="12.5" r="1.8" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="11.5" cy="5.5" r="1.8" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M4.5 5.3v5.4M11.5 7.3c0 2.5-3 2.5-6.2 3.6" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>main</span>
          <span class="text-tac19-str">✓ 0 problems</span>
          <span class="ml-auto">Ln 4, Col 38</span>
          <span class="max-sm:hidden">UTF-8</span>
          <span>TypeScript</span>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tac19-mono text-[11.5px] text-tac19-mut ring-1 ring-white/10">[counter-reset:tac19-ln] · before:content-[counter(tac19-ln)] · group-open:rotate-0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac19-bg: #0f1017;
  --color-tac19-bg: oklch(0.17 0.015 280);
  --color-tac19-glow: #23264880;
  --color-tac19-glow: oklch(0.29 0.06 275 / 0.5);
  --color-tac19-editor: #1a1b26;
  --color-tac19-editor: oklch(0.22 0.025 278);
  --color-tac19-chrome: #16161e;
  --color-tac19-chrome: oklch(0.2 0.015 280);
  --color-tac19-line: #1f2335;
  --color-tac19-line: oklch(0.25 0.035 275);
  --color-tac19-guide: #2b2f45;
  --color-tac19-guide: oklch(0.31 0.035 275);
  --color-tac19-fg: #c0caf5;
  --color-tac19-fg: oklch(0.85 0.06 270);
  --color-tac19-mut: #9aa3c7;
  --color-tac19-mut: oklch(0.73 0.05 272);
  --color-tac19-gut: #737aa2;
  --color-tac19-gut: oklch(0.6 0.05 275);
  --color-tac19-cm: #8b93bf;
  --color-tac19-cm: oklch(0.68 0.06 275);
  --color-tac19-cmh: #b4bce6;
  --color-tac19-cmh: oklch(0.8 0.06 275);
  --color-tac19-kw: #bb9af7;
  --color-tac19-kw: oklch(0.74 0.15 300);
  --color-tac19-str: #9ece6a;
  --color-tac19-str: oklch(0.8 0.15 130);
  --color-tac19-fn: #7aa2f7;
  --color-tac19-fn: oklch(0.72 0.13 262);
  --color-tac19-prop: #73daca;
  --color-tac19-prop: oklch(0.82 0.1 180);
  --color-tac19-type: #2ac3de;
  --color-tac19-type: oklch(0.76 0.12 214);
  --color-tac19-num: #ff9e64;
  --color-tac19-num: oklch(0.79 0.14 52);
  --color-tac19-op: #89ddff;
  --color-tac19-op: oklch(0.86 0.1 222);
  --font-tac19-sans: 'Geist', system-ui, sans-serif;
  --font-tac19-mono: 'JetBrains Mono', ui-monospace, 'Cascadia Code', Menlo, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-19 {
  width: 100%;
  min-height: 100svh;
}
```
