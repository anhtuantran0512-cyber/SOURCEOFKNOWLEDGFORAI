---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/vs-code-style-file-tabs-tailwind-css/"
title: "VS Code Style File Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "IDE file tabs with language dots, an accent stripe on the active tab and an editor body that merges with it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: VS Code Style File Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/vs-code-style-file-tabs-tailwind-css/

IDE file tabs with language dots, an accent stripe on the active tab and an editor body that merges with it. The port adds what a real editor shows: a breadcrumb, CSS-counter line numbers that don't copy, a close glyph on the active tab and a status bar — all from utilities.
## HTML
```html
<section class="ttb-05 group/tabs grid min-h-svh w-full place-items-center bg-ttb05-bg px-5 py-14 font-ttb05-mono text-ttb05-ink" aria-label="VS Code style file tabs demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-xl overflow-hidden rounded-xl bg-ttb05-editor shadow-[0_24px_60px_-20px_rgb(0_0_0/0.7)] ring-1 ring-white/8">
      <div role="radiogroup" aria-label="Open files" class="flex overflow-x-auto border-b border-ttb05-line bg-ttb05-chrome [scrollbar-width:none]">
        <label class="group/tab relative -mb-px flex min-h-11 flex-none cursor-pointer items-center gap-2 border-r border-b border-r-ttb05-line border-b-transparent px-4 text-[12.5px] text-ttb05-mut transition-colors before:absolute before:inset-x-0 before:top-0 before:h-0.5 hover:bg-white/4 hover:text-ttb05-ink has-checked:border-b-ttb05-editor has-checked:bg-ttb05-editor has-checked:text-ttb05-ink has-checked:before:bg-ttb05-acc has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb05-acc"><input class="sr-only" type="radio" name="ttb05" id="ttb05-r1" checked><span aria-hidden="true" class="size-2 rounded-full bg-ttb05-ts"></span>app.tsx<span aria-hidden="true" class="ml-1 text-ttb05-mut opacity-0 group-has-checked/tab:opacity-100">×</span></label>
        <label class="group/tab relative -mb-px flex min-h-11 flex-none cursor-pointer items-center gap-2 border-r border-b border-r-ttb05-line border-b-transparent px-4 text-[12.5px] text-ttb05-mut transition-colors before:absolute before:inset-x-0 before:top-0 before:h-0.5 hover:bg-white/4 hover:text-ttb05-ink has-checked:border-b-ttb05-editor has-checked:bg-ttb05-editor has-checked:text-ttb05-ink has-checked:before:bg-ttb05-acc has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb05-acc"><input class="sr-only" type="radio" name="ttb05" id="ttb05-r2"><span aria-hidden="true" class="size-2 rounded-full bg-ttb05-js"></span>config.js<span aria-hidden="true" class="ml-1 text-ttb05-mut opacity-0 group-has-checked/tab:opacity-100">×</span></label>
        <label class="group/tab relative -mb-px flex min-h-11 flex-none cursor-pointer items-center gap-2 border-r border-b border-r-ttb05-line border-b-transparent px-4 text-[12.5px] text-ttb05-mut transition-colors before:absolute before:inset-x-0 before:top-0 before:h-0.5 hover:bg-white/4 hover:text-ttb05-ink has-checked:border-b-ttb05-editor has-checked:bg-ttb05-editor has-checked:text-ttb05-ink has-checked:before:bg-ttb05-acc has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb05-acc"><input class="sr-only" type="radio" name="ttb05" id="ttb05-r3"><span aria-hidden="true" class="size-2 rounded-full bg-ttb05-css"></span>styles.css<span aria-hidden="true" class="ml-1 text-ttb05-mut opacity-0 group-has-checked/tab:opacity-100">×</span></label>
      </div>
      <div class="min-h-40 py-3 text-[12.5px] leading-[1.75]">
        <div class="hidden group-has-[#ttb05-r1:checked]/tabs:block"><p class="px-4 pb-2 text-[11px] text-ttb05-mut">src › app.tsx</p><code class="block [counter-reset:ttb05] [&>span]:block [&>span]:pr-4 [&>span]:whitespace-pre [&>span]:[counter-increment:ttb05] [&>span]:before:mr-4 [&>span]:before:inline-block [&>span]:before:w-8 [&>span]:before:text-right [&>span]:before:text-ttb05-lineno [&>span]:before:select-none [&>span]:before:content-[counter(ttb05)]"><span><span class="text-ttb05-kw">import</span> { Shell } <span class="text-ttb05-kw">from</span> <span class="text-ttb05-str">'./shell'</span>;</span><span> </span><span><span class="text-ttb05-kw">export default function</span> <span class="text-ttb05-fn">App</span>() {</span><span>  <span class="text-ttb05-kw">return</span> &lt;<span class="text-ttb05-tag">Shell</span> /&gt;;</span><span>}</span></code></div>
        <div class="hidden group-has-[#ttb05-r2:checked]/tabs:block"><p class="px-4 pb-2 text-[11px] text-ttb05-mut">config.js</p><code class="block [counter-reset:ttb05] [&>span]:block [&>span]:pr-4 [&>span]:whitespace-pre [&>span]:[counter-increment:ttb05] [&>span]:before:mr-4 [&>span]:before:inline-block [&>span]:before:w-8 [&>span]:before:text-right [&>span]:before:text-ttb05-lineno [&>span]:before:select-none [&>span]:before:content-[counter(ttb05)]"><span>module.exports = {</span><span>  <span class="text-ttb05-fn">port</span>: <span class="text-ttb05-num">3000</span>,</span><span>  <span class="text-ttb05-fn">strict</span>: <span class="text-ttb05-kw">true</span>,</span><span>};</span></code></div>
        <div class="hidden group-has-[#ttb05-r3:checked]/tabs:block"><p class="px-4 pb-2 text-[11px] text-ttb05-mut">src › styles.css</p><code class="block [counter-reset:ttb05] [&>span]:block [&>span]:pr-4 [&>span]:whitespace-pre [&>span]:[counter-increment:ttb05] [&>span]:before:mr-4 [&>span]:before:inline-block [&>span]:before:w-8 [&>span]:before:text-right [&>span]:before:text-ttb05-lineno [&>span]:before:select-none [&>span]:before:content-[counter(ttb05)]"><span><span class="text-ttb05-tag">:root</span> {</span><span>  <span class="text-ttb05-fn">color-scheme</span>: dark;</span><span>  <span class="text-ttb05-fn">--radius</span>: <span class="text-ttb05-num">12px</span>;</span><span>}</span></code></div>
      </div>
      <div class="flex justify-between bg-ttb05-acc-deep px-3.5 py-1 font-ttb05-sans text-[11px] text-white"><span>main</span><span>UTF-8 · Spaces: 2</span></div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 text-[11.5px] text-ttb05-mut">-mb-px merge · has-checked:before:bg-acc · counter() gutter</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb05-bg: #111114;
  --color-ttb05-bg: oklch(0.179 0.006 285.8);
  --color-ttb05-editor: #1e1e1e;
  --color-ttb05-editor: oklch(0.235 0 0);
  --color-ttb05-chrome: #2a2a2a;
  --color-ttb05-chrome: oklch(0.285 0 0);
  --color-ttb05-line: #161616;
  --color-ttb05-line: oklch(0.200 0 0);
  --color-ttb05-ink: #ececec;
  --color-ttb05-ink: oklch(0.943 0 0);
  --color-ttb05-mut: #a3a3a3;
  --color-ttb05-mut: oklch(0.715 0 0);
  --color-ttb05-lineno: #858585;
  --color-ttb05-lineno: oklch(0.617 0 0);
  --color-ttb05-acc: #4fc1ff;
  --color-ttb05-acc: oklch(0.772 0.135 236.2);
  --color-ttb05-acc-deep: #0a6cbd;
  --color-ttb05-acc-deep: oklch(0.526 0.150 251.3);
  --color-ttb05-ts: #3178c6;
  --color-ttb05-ts: oklch(0.567 0.140 253.3);
  --color-ttb05-js: #f0db4f;
  --color-ttb05-js: oklch(0.884 0.156 100.7);
  --color-ttb05-css: #2965f1;
  --color-ttb05-css: oklch(0.556 0.220 263.4);
  --color-ttb05-kw: #c586c0;
  --color-ttb05-kw: oklch(0.702 0.109 329.4);
  --color-ttb05-str: #ce9178;
  --color-ttb05-str: oklch(0.710 0.083 43.2);
  --color-ttb05-fn: #9cdcfe;
  --color-ttb05-fn: oklch(0.863 0.080 232.1);
  --color-ttb05-tag: #4ec9b0;
  --color-ttb05-tag: oklch(0.760 0.115 177.2);
  --color-ttb05-num: #b5cea8;
  --color-ttb05-num: oklch(0.823 0.059 134.9);
  --font-ttb05-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttb05-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-05 {
  width: 100%;
  min-height: 100svh;
}
```
