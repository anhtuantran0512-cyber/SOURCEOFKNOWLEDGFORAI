---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-animate-height-auto-faq-grid-rows/"
title: "Tailwind Animate Height Auto FAQ with grid-rows 0fr to 1fr"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The technique demo: how grid-template-rows: 0fr → 1fr finally solved CSS's oldest animation problem — transitioning to height:auto — written entirely in…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animate Height Auto FAQ with grid-rows 0fr to 1fr
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-animate-height-auto-faq-grid-rows/

The technique demo: how grid-template-rows: 0fr → 1fr finally solved CSS's oldest animation problem — transitioning to height:auto — written entirely in utilities. This FAQ dissects its own animation: every open panel carries a live annotation of what the track is doing, and the answers explain why max-height hacks break and why the one overflow-hidden wrapper is mandatory.
## HTML
```html
<section class="tfa-10 w-full min-h-svh grid place-items-center bg-tfa10-bg font-tfa10-sans text-tfa10-ink px-5 py-12 bg-[radial-gradient(1000px_520px_at_100%_100%,var(--color-tfa10-glow),transparent_58%)]">
  <div class="w-[min(700px,100%)]">
    <header>
      <span class="inline-block rounded-full bg-tfa10-tint px-3.5 py-1.5 font-tfa10-mono text-[12px] font-semibold text-tfa10-acc">grid-rows-[0fr] → grid-rows-[1fr]</span>
      <h1 class="mt-4 text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Animating to height: auto</h1>
      <p class="mt-3 max-w-[54ch] text-[15px] leading-relaxed text-tfa10-mut">The accordion that explains its own animation. Watch the track annotation as panels open.</p>
    </header>

    <div class="mt-8 flex flex-col gap-2.5">
      <div class="relative overflow-hidden rounded-2xl border border-tfa10-edge bg-tfa10-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa10-accedge has-checked:shadow-[0_18px_40px_-26px_oklch(0.75_0.14_190/0.5)]">
        <input id="tfa10-q1" type="checkbox" class="peer absolute opacity-0 pointer-events-none" checked>
        <label for="tfa10-q1" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa10-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa10-acc">Why doesn't height: auto animate?
          <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa10-acc before:transition-transform before:duration-500 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa10-acc after:rotate-90 after:transition-transform after:duration-500 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden">
            <p class="max-w-[62ch] px-5 text-[14px] leading-[1.7] text-tfa10-mut">Because <code class="rounded bg-tfa10-tint px-1.5 py-0.5 font-tfa10-mono text-[0.88em] text-tfa10-acc">auto</code> is a keyword, not a number — the engine has nothing to interpolate between 0px and “whatever it turns out to be”. Fraction units sidestep this: <code class="rounded bg-tfa10-tint px-1.5 py-0.5 font-tfa10-mono text-[0.88em] text-tfa10-acc">0fr → 1fr</code> is a numeric share of the content's size, resolved to real pixels every frame.</p>
            <span aria-hidden="true" class="mx-5 mb-4 mt-3 block rounded-r-lg border-l-[3px] border-tfa10-acc bg-tfa10-tint px-3 py-2 font-tfa10-mono text-[11.5px] text-tfa10-acc">grid-template-rows: <b class='font-bold'>1fr</b> · height resolved per frame</span>
          </div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-2xl border border-tfa10-edge bg-tfa10-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa10-accedge has-checked:shadow-[0_18px_40px_-26px_oklch(0.75_0.14_190/0.5)]">
        <input id="tfa10-q2" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa10-q2" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa10-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa10-acc">What's wrong with max-height: 500px?
          <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa10-acc before:transition-transform before:duration-500 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa10-acc after:rotate-90 after:transition-transform after:duration-500 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden">
            <p class="max-w-[62ch] px-5 text-[14px] leading-[1.7] text-tfa10-mut">It animates to 500px, not to your content. Short answers finish early then “wait” invisibly; long answers get clipped. Every max-height accordion has a magic number that is wrong for someone's content, font size, or translation.</p>
            <span aria-hidden="true" class="mx-5 mb-4 mt-3 block rounded-r-lg border-l-[3px] border-tfa10-acc bg-tfa10-tint px-3 py-2 font-tfa10-mono text-[11.5px] text-tfa10-acc">this panel needed no magic number</span>
          </div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-2xl border border-tfa10-edge bg-tfa10-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa10-accedge has-checked:shadow-[0_18px_40px_-26px_oklch(0.75_0.14_190/0.5)]">
        <input id="tfa10-q3" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa10-q3" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa10-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa10-acc">Why the extra inner wrapper?
          <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa10-acc before:transition-transform before:duration-500 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa10-acc after:rotate-90 after:transition-transform after:duration-500 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden">
            <p class="max-w-[62ch] px-5 text-[14px] leading-[1.7] text-tfa10-mut">Grid items refuse to shrink below <code class="rounded bg-tfa10-tint px-1.5 py-0.5 font-tfa10-mono text-[0.88em] text-tfa10-acc">min-content</code> by default — a 0fr track with an unclippable child still renders tall. <code class="rounded bg-tfa10-tint px-1.5 py-0.5 font-tfa10-mono text-[0.88em] text-tfa10-acc">overflow-hidden</code> plus <code class="rounded bg-tfa10-tint px-1.5 py-0.5 font-tfa10-mono text-[0.88em] text-tfa10-acc">min-h-0</code> on the direct child releases that constraint. Forget it and the accordion “never closes”.</p>
            <span aria-hidden="true" class="mx-5 mb-4 mt-3 block rounded-r-lg border-l-[3px] border-tfa10-acc bg-tfa10-tint px-3 py-2 font-tfa10-mono text-[11.5px] text-tfa10-acc">class=&quot;min-h-0 overflow-hidden&quot;</span>
          </div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-2xl border border-tfa10-edge bg-tfa10-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa10-accedge has-checked:shadow-[0_18px_40px_-26px_oklch(0.75_0.14_190/0.5)]">
        <input id="tfa10-q4" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa10-q4" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa10-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa10-acc">Does this work with really long content?
          <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa10-acc before:transition-transform before:duration-500 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa10-acc after:rotate-90 after:transition-transform after:duration-500 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden">
            <p class="max-w-[62ch] px-5 text-[14px] leading-[1.7] text-tfa10-mut">Yes — that is the whole point. This answer is deliberately longer to prove it: the track interpolates shares, not pixels, so a two-line answer and a twelve-line answer both animate over the same 500 milliseconds with the same easing, and the browser resolves the actual height continuously during the transition. Resize the pane mid-animation; it self-corrects. Add another paragraph tomorrow; there is nothing to update. That is what “no magic numbers” buys you in maintenance terms.</p>
            <span aria-hidden="true" class="mx-5 mb-4 mt-3 block rounded-r-lg border-l-[3px] border-tfa10-acc bg-tfa10-tint px-3 py-2 font-tfa10-mono text-[11.5px] text-tfa10-acc">same duration-500 regardless of content length</span>
          </div>
        </div>
      </div>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa10-mut">The same pattern rotated 90° is demo 15's horizontal accordion (<code class="rounded bg-tfa10-tint px-1.5 py-0.5 font-tfa10-mono text-[0.88em] text-tfa10-acc">grid-cols-[0fr]</code>).</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa10-bg: #1a1f24;
  --color-tfa10-bg: oklch(0.2 0.015 220);
  --color-tfa10-panel: #212a30;
  --color-tfa10-panel: oklch(0.24 0.02 220);
  --color-tfa10-glow: #1c3b41;
  --color-tfa10-glow: oklch(0.28 0.06 190 / 0.5);
  --color-tfa10-ink: #f1f5f6;
  --color-tfa10-ink: oklch(0.96 0.008 210);
  --color-tfa10-mut: #b4bfc3;
  --color-tfa10-mut: oklch(0.79 0.014 215);
  --color-tfa10-edge: #38434a;
  --color-tfa10-edge: oklch(0.34 0.022 218);
  --color-tfa10-accedge: #4e8f96;
  --color-tfa10-accedge: oklch(0.6 0.08 190);
  --color-tfa10-tint: #24383c;
  --color-tfa10-tint: oklch(0.29 0.04 190);
  --color-tfa10-acc: #7fdbe4;
  --color-tfa10-acc: oklch(0.85 0.12 190);
  --font-tfa10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa10-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-10 {
  width: 100%;
  min-height: 100svh;
}
```
