---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-code-editor-ui-syntax-highlighting/"
title: "Tailwind Dark Mode Code Editor UI with Syntax Highlighting"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "An editor chrome — file tree, tab bar with an unsaved dot, gutter, code panel and status bar — where the syntax palette is a token set rather than a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Code Editor UI with Syntax Highlighting
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-code-editor-ui-syntax-highlighting/

An editor chrome — file tree, tab bar with an unsaved dot, gutter, code panel and status bar — where the syntax palette is a token set rather than a stylesheet per theme. Keyword, string, comment, function, number and property colours are light-dark() pairs, so the same highlighted markup reads correctly on a near-black editor and a paper-white one.
## HTML
```html
<div class="tdm-10 scheme-light-dark has-[#tdm-10-toggle:checked]:scheme-dark dark:has-[#tdm-10-toggle:checked]:scheme-light grid w-full min-h-svh place-items-center bg-tdm10-bg px-3 py-10 font-tdm10-sans text-tdm10-ink antialiased transition-colors duration-300 sm:px-6">
  <div class="@container w-full max-w-6xl overflow-hidden rounded-[22px] border border-tdm10-line bg-tdm10-panel shadow-tdm10-win">
    <div class="flex items-center gap-2 border-b border-tdm10-line bg-tdm10-chrome px-4 py-3">
      <span class="flex gap-1.5" aria-hidden="true"><i class="size-3 rounded-full bg-[#ff5f57]"></i><i class="size-3 rounded-full bg-[#febc2e]"></i><i class="size-3 rounded-full bg-[#28c840]"></i></span>
      <p class="flex-1 text-center font-tdm10-mono text-xs text-tdm10-mut">meridian-web — theme.css</p>
    </div>
    <div class="grid min-h-[30rem] grid-cols-[14rem_minmax(0,1fr)] @max-[44rem]:grid-cols-1">
      <aside aria-label="Files" class="grid content-start gap-1 border-r border-tdm10-line bg-tdm10-tree p-3 @max-[44rem]:hidden">
        <p class="px-2 pb-2 font-tdm10-mono text-[11px] uppercase tracking-[0.12em] text-tdm10-mut">Explorer</p>
        <button type="button" class="flex min-h-9 items-center gap-2 rounded-lg px-2 text-left font-tdm10-mono text-[13px] text-tdm10-mut transition hover:bg-tdm10-ink/5 hover:text-tdm10-ink focus-visible:outline-2 focus-visible:outline-tdm10-focus aria-[current=true]:bg-tdm10-acc/12 aria-[current=true]:text-tdm10-ink"><svg class="size-4 text-tdm10-num" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7.5A2.5 2.5 0 0 1 5.5 5h4l2 2.5h7A2.5 2.5 0 0 1 21 10v7.5a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 17.5Z"/></svg>app</button>
        <button type="button" aria-current="true" class="flex min-h-9 items-center gap-2 rounded-lg px-2 text-left font-tdm10-mono text-[13px] text-tdm10-mut transition hover:bg-tdm10-ink/5 hover:text-tdm10-ink focus-visible:outline-2 focus-visible:outline-tdm10-focus aria-[current=true]:bg-tdm10-acc/12 aria-[current=true]:text-tdm10-ink"><svg class="size-4 text-tdm10-fn" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg>theme.css</button>
        <button type="button" class="flex min-h-9 items-center gap-2 rounded-lg px-2 text-left font-tdm10-mono text-[13px] text-tdm10-mut transition hover:bg-tdm10-ink/5 hover:text-tdm10-ink focus-visible:outline-2 focus-visible:outline-tdm10-focus aria-[current=true]:bg-tdm10-acc/12 aria-[current=true]:text-tdm10-ink"><svg class="size-4 text-tdm10-fn" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg>App.tsx</button>
        <button type="button" class="flex min-h-9 items-center gap-2 rounded-lg px-2 text-left font-tdm10-mono text-[13px] text-tdm10-mut transition hover:bg-tdm10-ink/5 hover:text-tdm10-ink focus-visible:outline-2 focus-visible:outline-tdm10-focus aria-[current=true]:bg-tdm10-acc/12 aria-[current=true]:text-tdm10-ink"><svg class="size-4 text-tdm10-fn" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg>next.config.mjs</button>
        <button type="button" class="flex min-h-9 items-center gap-2 rounded-lg px-2 text-left font-tdm10-mono text-[13px] text-tdm10-mut transition hover:bg-tdm10-ink/5 hover:text-tdm10-ink focus-visible:outline-2 focus-visible:outline-tdm10-focus aria-[current=true]:bg-tdm10-acc/12 aria-[current=true]:text-tdm10-ink"><svg class="size-4 text-tdm10-fn" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg>package.json</button>
      </aside>
      <div class="flex min-w-0 flex-col">
        <div role="tablist" aria-label="Open files" class="flex overflow-x-auto border-b border-tdm10-line bg-tdm10-chrome">
          <button type="button" role="tab" aria-selected="true" class="relative flex min-h-11 flex-none items-center gap-2 border-r border-tdm10-line px-4 font-tdm10-mono text-[12.5px] text-tdm10-mut transition hover:text-tdm10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdm10-focus aria-selected:bg-tdm10-panel aria-selected:text-tdm10-ink aria-selected:before:absolute aria-selected:before:inset-x-0 aria-selected:before:top-0 aria-selected:before:h-0.5 aria-selected:before:bg-tdm10-acc aria-selected:before:content-['']">theme.css<span class="size-2 rounded-full bg-tdm10-num" title="Unsaved changes"></span><span class="sr-only">(unsaved)</span></button>
          <button type="button" role="tab" aria-selected="false" class="relative flex min-h-11 flex-none items-center gap-2 border-r border-tdm10-line px-4 font-tdm10-mono text-[12.5px] text-tdm10-mut transition hover:text-tdm10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdm10-focus aria-selected:bg-tdm10-panel aria-selected:text-tdm10-ink aria-selected:before:absolute aria-selected:before:inset-x-0 aria-selected:before:top-0 aria-selected:before:h-0.5 aria-selected:before:bg-tdm10-acc aria-selected:before:content-['']">App.tsx</button>
          <button type="button" role="tab" aria-selected="false" class="relative flex min-h-11 flex-none items-center gap-2 border-r border-tdm10-line px-4 font-tdm10-mono text-[12.5px] text-tdm10-mut transition hover:text-tdm10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdm10-focus aria-selected:bg-tdm10-panel aria-selected:text-tdm10-ink aria-selected:before:absolute aria-selected:before:inset-x-0 aria-selected:before:top-0 aria-selected:before:h-0.5 aria-selected:before:bg-tdm10-acc aria-selected:before:content-['']">next.config.mjs</button>
        </div>
        <div class="flex flex-1 overflow-auto font-tdm10-mono text-[13.5px]/[1.75rem]">
          <div aria-hidden="true" class="flex-none select-none py-4 pr-3 pl-5 text-right text-tdm10-gutter"><span class="block ">1</span><span class="block ">2</span><span class="block ">3</span><span class="block ">4</span><span class="block ">5</span><span class="block ">6</span><span class="block ">7</span><span class="block text-tdm10-ink">8</span><span class="block ">9</span><span class="block ">10</span><span class="block ">11</span><span class="block ">12</span><span class="block ">13</span><span class="block ">14</span></div>
<pre class="m-0 min-w-0 flex-1 py-4 pr-6 text-tdm10-punct"><code><span class="block"><span class="text-tdm10-cmt italic">/* semantic tokens — one source of truth */</span></span><span class="block"><span class="text-tdm10-kw">@theme</span> {</span><span class="block">  <span class="text-tdm10-prop">--color-surface</span>: <span class="text-tdm10-fn">light-dark</span>(<span class="text-tdm10-num">#ffffff</span>, <span class="text-tdm10-num">#0d1017</span>);</span><span class="block">  <span class="text-tdm10-prop">--color-ink</span>:     <span class="text-tdm10-fn">light-dark</span>(<span class="text-tdm10-num">#0d1017</span>, <span class="text-tdm10-num">#e8ecf4</span>);</span><span class="block">  <span class="text-tdm10-prop">--color-accent</span>:  <span class="text-tdm10-fn">light-dark</span>(<span class="text-tdm10-num">#1d4ed8</span>, <span class="text-tdm10-num">#82aaff</span>);</span><span class="block">}</span><span class="block"> </span><span class="-mr-6 -ml-3 block bg-tdm10-hl pr-6 pl-3"><span class="text-tdm10-kw">@custom-variant</span> <span class="text-tdm10-fn">theme-dark</span> (<span class="text-tdm10-str">&amp;:where(.dark *)</span>);<span class="ml-px inline-block h-[1.1em] w-0.5 translate-y-[3px] bg-tdm10-caret animate-tdm10-caret motion-reduce:animate-none" aria-hidden="true"></span></span><span class="block"> </span><span class="block"><span class="text-tdm10-cmt italic">/* the markup only ever names the token */</span></span><span class="block">&lt;<span class="text-tdm10-kw">div</span> <span class="text-tdm10-prop">class</span>=<span class="text-tdm10-str">"bg-surface text-ink scheme-light-dark"</span>&gt;</span><span class="block">  &lt;<span class="text-tdm10-kw">button</span> <span class="text-tdm10-prop">class</span>=<span class="text-tdm10-str">"bg-accent/90 hover:bg-accent"</span>&gt;</span><span class="block">    Deploy <span class="text-tdm10-num">4.2</span></span><span class="block">  &lt;/<span class="text-tdm10-kw">button</span>&gt;&lt;/<span class="text-tdm10-kw">div</span>&gt;</span></code></pre>
        </div>
        <div class="flex flex-wrap items-center gap-x-4 gap-y-1 border-t border-tdm10-line bg-tdm10-status px-3 py-1 font-tdm10-mono text-[11.5px] text-tdm10-mut">
          <span class="flex items-center gap-1.5 text-tdm10-acc"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="6" cy="5.5" r="2.5"/><circle cx="6" cy="18.5" r="2.5"/><circle cx="18" cy="8" r="2.5"/><path d="M6 8v8M18 10.5c0 4-6 3.5-11 6.5"/></svg>main</span>
          <span>Ln 8, Col 41</span><span>Spaces: 2</span><span>CSS</span>
          <span class="ml-auto flex items-center gap-2"><span class="flex items-center gap-1.5"><svg class="size-3.5 text-tdm10-str" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Prettier</span><label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm10-line bg-tdm10-surface transition duration-200 hover:-translate-y-px hover:border-tdm10-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm10-focus motion-reduce:transition-none ">
        <input id="tdm-10-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm10-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm10-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label></span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm10-bg: light-dark(#e8ebf0, #050608);
  --color-tdm10-chrome: light-dark(#f3f4f7, #0d1017);
  --color-tdm10-panel: light-dark(#ffffff, #0a0c12);
  --color-tdm10-tree: light-dark(#f8f9fb, #0b0e14);
  --color-tdm10-status: light-dark(#f3f4f7, #0b0e14);
  --color-tdm10-surface: light-dark(#ffffff, #121621);
  --color-tdm10-ink: light-dark(#0d1017, #e8ecf4);
  --color-tdm10-mut: light-dark(#5b6476, #8f99ad);
  --color-tdm10-gutter: light-dark(#9aa1ae, #4b5568);
  --color-tdm10-line: light-dark(#e3e6ec, #1c212c);
  --color-tdm10-hl: light-dark(rgb(29 78 216 / .06), rgb(130 170 255 / .07));
  --color-tdm10-acc: light-dark(#1d4ed8, #82aaff);
  --color-tdm10-caret: light-dark(#1d4ed8, #82aaff);
  --color-tdm10-focus: light-dark(#1d4ed8, #b4cbff);
  --color-tdm10-kw: light-dark(#7c3aed, #c792ea);
  --color-tdm10-str: light-dark(#15803d, #a5e075);
  --color-tdm10-cmt: light-dark(#6b7280, #7a879d);
  --color-tdm10-fn: light-dark(#1d4ed8, #82aaff);
  --color-tdm10-num: light-dark(#c2410c, #f78c6c);
  --color-tdm10-prop: light-dark(#0e7490, #7fdbca);
  --color-tdm10-punct: light-dark(#475569, #a0a9bb);
  --color-tdm10-sun: light-dark(#b45309, transparent);
  --color-tdm10-moon: light-dark(transparent, #b4cbff);
  --shadow-tdm10-win: 0 50px 100px -50px light-dark(rgb(13 16 23 / .35), rgb(0 0 0 / .9));
  --font-tdm10-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tdm10-caret: tdm10-caret 1.1s steps(1) infinite;

  @keyframes tdm10-caret {
    50% {
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
