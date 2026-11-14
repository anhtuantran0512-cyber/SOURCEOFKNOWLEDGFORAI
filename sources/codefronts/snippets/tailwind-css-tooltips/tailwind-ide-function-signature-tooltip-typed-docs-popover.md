---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-ide-function-signature-tooltip-typed-docs-popover/"
title: "Tailwind IDE Function Signature Tooltip with Typed Docs Popover"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "The typed-signature popover a code editor shows on hover: badge, namespace path, multi-line signature, prose, a parameter table and a footer shortcut."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind IDE Function Signature Tooltip with Typed Docs Popover
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-ide-function-signature-tooltip-typed-docs-popover/

The typed-signature popover a code editor shows on hover: badge, namespace path, multi-line signature, prose, a parameter table and a footer shortcut. The port's interesting cost is whitespace-pre &mdash; the CSS version fights inheritance with two resets, and Tailwind makes both of them visible on the elements that need them.
## HTML
```html
<section class="ttp-03 w-full min-h-svh flex items-start justify-center bg-ttp03-bg font-ttp03-mono px-7 pt-[300px] pb-12">
  <div class="w-full max-w-[560px] bg-ttp03-panel border border-ttp03-edge rounded-lg shadow-[0_18px_50px_-16px_rgba(0,0,0,0.7)]">
    <div class="flex items-center gap-1 h-8 px-3.5 bg-ttp03-bg border-b border-ttp03-edge rounded-t-lg">
      <span class="w-[9px] h-[9px] rounded-full bg-[#ff5f57]"></span>
      <span class="w-[9px] h-[9px] rounded-full bg-[#febc2e]"></span>
      <span class="w-[9px] h-[9px] rounded-full bg-[#28c840]"></span>
      <span class="ml-4.5 inline-flex items-center gap-[7px] px-3 py-[5px] rounded-t-md bg-ttp03-panel text-[11px] text-ttp03-ink before:content-[''] before:w-1 before:h-1 before:rounded-full before:bg-ttp03-blue">orchestrator.ts</span>
    </div>

    <div class="flex py-4.5 text-[13px] leading-[22px] text-ttp03-ink">
      <div class="w-11 pr-3 text-right select-none border-r border-ttp03-rule text-ttp03-gutter text-[13px]">
        <div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div><div>7</div><div>8</div>
      </div>
      <div class="flex-1 min-w-0 px-4">
        <div><span class="italic text-ttp03-cmt">// pipeline assembled at boot</span></div>
        <div><span class="text-ttp03-kw">import</span> { <span class="text-ttp03-fn">createScheduler</span> } <span class="text-ttp03-kw">from</span> <span class="text-ttp03-str">"./scheduler"</span>;</div>
        <div>&nbsp;</div>
        <div><span class="text-ttp03-kw">const</span> <span class="text-ttp03-var">queue</span> = <button type="button" aria-describedby="ttp03-tip" class="group relative inline cursor-help border-0 bg-transparent p-0 px-0.5 rounded-[2px] font-ttp03-mono text-[13px] [border-bottom:1px_dashed_rgba(88,166,255,0.55)] transition-colors duration-200 hover:bg-ttp03-blue/10 hover:[border-bottom-color:#58a6ff] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp03-blue after:content-['ⓘ'] after:inline-block after:align-middle after:ml-[3px] after:text-[9px] after:text-ttp03-blue/60 hover:after:text-ttp03-blue"><span class="text-ttp03-fn">createScheduler</span><span id="ttp03-tip" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+14px)] left-[-20px] z-10 block w-[380px] max-w-[calc(100vw-56px)] text-left whitespace-normal leading-normal translate-y-2 opacity-0 rounded-md border border-ttp03-edge bg-linear-to-b from-ttp03-card1 to-ttp03-card2 shadow-[0_18px_50px_-8px_rgba(0,0,0,0.75),0_0_0_1px_rgba(88,166,255,0.06),inset_0_1px_0_rgba(255,255,255,0.04)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-opacity after:content-[''] after:absolute after:top-full after:left-8 after:w-2.5 after:h-2.5 after:-translate-y-1/2 after:rotate-45 after:bg-ttp03-panel after:border-r after:border-b after:border-ttp03-edge">
          <span class="flex items-center gap-2.5 px-3.5 pt-2.5 pb-2.25 border-b border-ttp03-rule text-[11px]">
            <span class="rounded-[10px] bg-ttp03-blue/15 px-1.75 py-0.5 text-[10px] font-semibold tracking-[0.05em] text-ttp03-blue">FUNCTION</span>
            <span class="text-ttp03-dim">core<span class="mx-1 text-ttp03-gutter">›</span>scheduler<span class="mx-1 text-ttp03-gutter">›</span>createScheduler</span>
          </span>
          <span class="block whitespace-pre border-b border-ttp03-rule px-3.5 py-3 text-xs leading-[1.6]"><span class="text-ttp03-kw">function</span> <span class="text-ttp03-fn">createScheduler</span>&lt;<span class="text-ttp03-var">T</span>&gt;(
  <span class="text-ttp03-param">opts</span>: <span class="text-ttp03-var">SchedulerOptions</span>&lt;<span class="text-ttp03-var">T</span>&gt;
): <span class="text-ttp03-var">Queue</span>&lt;<span class="text-ttp03-var">T</span>&gt;</span>
          <span class="block border-b border-ttp03-rule px-3.5 py-3 font-ttp03-sans text-xs leading-[1.65] text-ttp03-ink">Creates a back-pressured task queue with concurrency control. Items are processed in <code class="rounded-[3px] bg-ttp03-chip px-1.25 py-px font-ttp03-mono text-[11px] text-ttp03-param">FIFO</code> order; failing jobs surface to the dead-letter sink.</span>
          <span class="block border-b border-ttp03-rule px-3.5 py-2.5">
            <span class="grid grid-cols-[90px_1fr] gap-2.5 py-0.75 text-[11.5px] leading-[1.5]"><span class="text-ttp03-param">concurrency</span><span class="font-ttp03-sans text-ttp03-dim">Max parallel jobs. Default <code class="rounded-[3px] bg-ttp03-chip px-1.25 py-px font-ttp03-mono text-[11px] text-ttp03-param">4</code>.</span></span>
            <span class="grid grid-cols-[90px_1fr] gap-2.5 py-0.75 text-[11.5px] leading-[1.5]"><span class="text-ttp03-param">retries</span><span class="font-ttp03-sans text-ttp03-dim">Per-task retry budget. Default <code class="rounded-[3px] bg-ttp03-chip px-1.25 py-px font-ttp03-mono text-[11px] text-ttp03-param">3</code>.</span></span>
            <span class="grid grid-cols-[90px_1fr] gap-2.5 py-0.75 text-[11.5px] leading-[1.5]"><span class="text-ttp03-param">onDrain</span><span class="font-ttp03-sans text-ttp03-dim">Fires once when the queue empties.</span></span>
          </span>
          <span class="flex items-center justify-between px-3.5 py-2.25 text-[10.5px] text-ttp03-dim">
            <span>scheduler.ts · L42</span>
            <span><kbd class="not-italic"><span class="mx-0.5 inline-block rounded-[4px] border border-ttp03-edge border-b-2 bg-ttp03-chipdark px-1.5 py-px text-[10px] text-ttp03-ink">⌘</span><span class="mx-0.5 inline-block rounded-[4px] border border-ttp03-edge border-b-2 bg-ttp03-chipdark px-1.5 py-px text-[10px] text-ttp03-ink">K</span></kbd> for docs</span>
          </span>
        </span></button>({</div>
        <div>&nbsp;&nbsp;<span class="text-ttp03-param">concurrency</span>: <span class="text-ttp03-num">8</span>,</div>
        <div>&nbsp;&nbsp;<span class="text-ttp03-param">retries</span>: <span class="text-ttp03-num">3</span>,</div>
        <div>});</div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp03-bg: #0d1117;
  --color-ttp03-bg: oklch(0.18 0.02 265);
  --color-ttp03-panel: #161b22;
  --color-ttp03-panel: oklch(0.22 0.02 265);
  --color-ttp03-card1: #1c2128;
  --color-ttp03-card1: oklch(0.25 0.02 265);
  --color-ttp03-card2: #161b22;
  --color-ttp03-card2: oklch(0.22 0.02 265);
  --color-ttp03-edge: #30363d;
  --color-ttp03-edge: oklch(0.35 0.01 265);
  --color-ttp03-rule: #21262d;
  --color-ttp03-chip: #3a4049;
  --color-ttp03-chip: oklch(0.38 0.01 265);
  --color-ttp03-chipdark: #21262d;
  --color-ttp03-ink: #c9d1d9;
  --color-ttp03-ink: oklch(0.85 0.01 265);
  --color-ttp03-dim: #9aa4b0;
  --color-ttp03-dim: oklch(0.72 0.014 265);
  --color-ttp03-gutter: #6e7681;
  --color-ttp03-gutter: oklch(0.56 0.01 265);
  --color-ttp03-blue: #58a6ff;
  --color-ttp03-blue: oklch(0.71 0.14 255);
  --color-ttp03-kw: #ff7b72;
  --color-ttp03-fn: #d2a8ff;
  --color-ttp03-str: #a5d6ff;
  --color-ttp03-num: #79c0ff;
  --color-ttp03-var: #79c0ff;
  --color-ttp03-cmt: #9aa4b0;
  --color-ttp03-param: #ffa657;
  --font-ttp03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttp03-sans: 'Inter', system-ui, sans-serif;
}

.ttp-03 {
  width: 100%;
  min-height: 100svh;
}
```
