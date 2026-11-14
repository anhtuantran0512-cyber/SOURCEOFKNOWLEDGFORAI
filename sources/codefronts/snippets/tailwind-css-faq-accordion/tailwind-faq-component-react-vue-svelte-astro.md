---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-component-react-vue-svelte-astro/"
title: "Tailwind FAQ Component in React, Vue, Svelte and Astro (One Port Recipe)"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "One accordion, five codebases: a working native-<details> FAQ up top, and beneath it a pure-CSS tab viewer showing the same component in React, Vue 3, Svelte…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind FAQ Component in React, Vue, Svelte and Astro (One Port Recipe)
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-component-react-vue-svelte-astro/

One accordion, five codebases: a working native-<details> FAQ up top, and beneath it a pure-CSS tab viewer showing the same component in React, Vue 3, Svelte 5 and Astro. The thesis is stronger in Tailwind than it was in CSS — because the class list travels with the markup, the port really is just a data-mapping shell, with no stylesheet to move at all.
## HTML
```html
<section class="tfa-24 w-full min-h-svh grid place-items-center bg-tfa24-bg font-tfa24-sans text-tfa24-ink px-5 py-12 bg-[radial-gradient(900px_500px_at_85%_0%,var(--color-tfa24-glow),transparent_60%)]">
  <div class="w-[min(700px,100%)]">
    <header>
      <h1 class="text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">One accordion, five codebases</h1>
      <p class="mt-3 max-w-[56ch] text-[15px] leading-relaxed text-tfa24-mut">The living component, then the same 15-line shell per framework. Behaviour stays in <code class="rounded bg-tfa24-tint px-1.5 py-0.5 font-tfa24-mono text-[0.87em] text-tfa24-acc">&lt;details&gt;</code>, styling stays in the class list, frameworks only map data.</p>
    </header>

    <div data-panel class="mt-6 flex flex-col gap-2.5">
        <details class="group rounded-[13px] border border-tfa24-edge bg-tfa24-panel transition-[border-color] duration-300 open:border-tfa24-accedge" open>
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa24-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa24-acc [&::-webkit-details-marker]:hidden">Why no accordion library?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa24-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa24-mut">Because the platform ships one. The details element gives you state, keyboard support and semantics; a library would re-implement all three in 40kB and still need this class list.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa24-edge bg-tfa24-panel transition-[border-color] duration-300 open:border-tfa24-accedge">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa24-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa24-acc [&::-webkit-details-marker]:hidden">Where does state live?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa24-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa24-mut">In the DOM open attribute — so SSR, static builds and server components render working accordions with zero hydration. Lift state into the framework only when a feature actually demands it.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa24-edge bg-tfa24-panel transition-[border-color] duration-300 open:border-tfa24-accedge">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa24-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa24-acc [&::-webkit-details-marker]:hidden">Does the styling need porting?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa24-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa24-mut">No, and that is new: utilities travel inside the markup. The CSS version still had to get a stylesheet into four different scoping systems.</p>
        </details>
    </div>

    <div class="mt-5 overflow-hidden rounded-2xl border border-tfa24-edge bg-tfa24-viewer">
      <div class="flex flex-wrap px-2.5 pt-2.5">
        <input type="radio" name="tfa24-tab" id="tfa24-react" class="peer/tfa24-react absolute opacity-0 pointer-events-none" checked>
        <label for="tfa24-react" class="grid min-h-11 cursor-pointer place-items-center rounded-t-[10px] px-4 text-[13px] font-bold text-tfa24-mut transition-colors duration-200 hover:text-tfa24-ink peer-focus-visible/tfa24-react:outline-2 peer-focus-visible/tfa24-react:-outline-offset-2 peer-focus-visible/tfa24-react:outline-tfa24-acc peer-checked/tfa24-react:bg-tfa24-panel peer-checked/tfa24-react:text-tfa24-acc">React</label>
        <div class="hidden w-full border-t border-tfa24-edge bg-tfa24-panel peer-checked/tfa24-react:block">
          <pre class="overflow-x-auto px-5 py-4"><code class="font-tfa24-mono text-[12px] leading-[1.65] text-tfa24-code">function Faq({ items }) {
  return (
    &lt;div className="flex flex-col gap-2.5"&gt;
      {items.map(it =&gt; (
        &lt;details key={it.q} className="group rounded-2xl border"
                 {...(it.open ? { open: true } : {})}&gt;
          &lt;summary className="flex min-h-11 cursor-pointer list-none
                              items-center justify-between px-5 py-4
                              [&amp;::-webkit-details-marker]:hidden"&gt;
            {it.q}
            &lt;i className="size-2 rotate-45 border-b-2 border-r-2
                         group-open:rotate-[225deg]" /&gt;
          &lt;/summary&gt;
          &lt;p className="px-5 pb-4 text-sm"&gt;{it.a}&lt;/p&gt;
        &lt;/details&gt;
      ))}
    &lt;/div&gt;
  );
}  // no useState — the DOM holds the state</code></pre>
        </div>
        <input type="radio" name="tfa24-tab" id="tfa24-vue" class="peer/tfa24-vue absolute opacity-0 pointer-events-none">
        <label for="tfa24-vue" class="grid min-h-11 cursor-pointer place-items-center rounded-t-[10px] px-4 text-[13px] font-bold text-tfa24-mut transition-colors duration-200 hover:text-tfa24-ink peer-focus-visible/tfa24-vue:outline-2 peer-focus-visible/tfa24-vue:-outline-offset-2 peer-focus-visible/tfa24-vue:outline-tfa24-acc peer-checked/tfa24-vue:bg-tfa24-panel peer-checked/tfa24-vue:text-tfa24-acc">Vue 3</label>
        <div class="hidden w-full border-t border-tfa24-edge bg-tfa24-panel peer-checked/tfa24-vue:block">
          <pre class="overflow-x-auto px-5 py-4"><code class="font-tfa24-mono text-[12px] leading-[1.65] text-tfa24-code">&lt;script setup&gt;
defineProps({ items: Array })
&lt;/script&gt;

&lt;template&gt;
  &lt;div class="flex flex-col gap-2.5"&gt;
    &lt;details v-for="it in items" :key="it.q" :open="it.open"
             class="group rounded-2xl border"&gt;
      &lt;summary class="flex min-h-11 cursor-pointer list-none
                      items-center justify-between px-5 py-4
                      [&amp;::-webkit-details-marker]:hidden"&gt;
        {{ it.q }}
        &lt;i class="size-2 rotate-45 border-b-2 border-r-2
                  group-open:rotate-[225deg]" /&gt;
      &lt;/summary&gt;
      &lt;p class="px-5 pb-4 text-sm"&gt;{{ it.a }}&lt;/p&gt;
    &lt;/details&gt;
  &lt;/div&gt;
&lt;/template&gt;</code></pre>
        </div>
        <input type="radio" name="tfa24-tab" id="tfa24-svelte" class="peer/tfa24-svelte absolute opacity-0 pointer-events-none">
        <label for="tfa24-svelte" class="grid min-h-11 cursor-pointer place-items-center rounded-t-[10px] px-4 text-[13px] font-bold text-tfa24-mut transition-colors duration-200 hover:text-tfa24-ink peer-focus-visible/tfa24-svelte:outline-2 peer-focus-visible/tfa24-svelte:-outline-offset-2 peer-focus-visible/tfa24-svelte:outline-tfa24-acc peer-checked/tfa24-svelte:bg-tfa24-panel peer-checked/tfa24-svelte:text-tfa24-acc">Svelte 5</label>
        <div class="hidden w-full border-t border-tfa24-edge bg-tfa24-panel peer-checked/tfa24-svelte:block">
          <pre class="overflow-x-auto px-5 py-4"><code class="font-tfa24-mono text-[12px] leading-[1.65] text-tfa24-code">&lt;script&gt;
  let { items } = $props();
&lt;/script&gt;

&lt;div class="flex flex-col gap-2.5"&gt;
  {#each items as it (it.q)}
    &lt;details open={it.open} class="group rounded-2xl border"&gt;
      &lt;summary class="flex min-h-11 cursor-pointer list-none
                      items-center justify-between px-5 py-4
                      [&amp;::-webkit-details-marker]:hidden"&gt;
        {it.q}
        &lt;i class="size-2 rotate-45 border-b-2 border-r-2
                  group-open:rotate-[225deg]"&gt;&lt;/i&gt;
      &lt;/summary&gt;
      &lt;p class="px-5 pb-4 text-sm"&gt;{it.a}&lt;/p&gt;
    &lt;/details&gt;
  {/each}
&lt;/div&gt;</code></pre>
        </div>
        <input type="radio" name="tfa24-tab" id="tfa24-astro" class="peer/tfa24-astro absolute opacity-0 pointer-events-none">
        <label for="tfa24-astro" class="grid min-h-11 cursor-pointer place-items-center rounded-t-[10px] px-4 text-[13px] font-bold text-tfa24-mut transition-colors duration-200 hover:text-tfa24-ink peer-focus-visible/tfa24-astro:outline-2 peer-focus-visible/tfa24-astro:-outline-offset-2 peer-focus-visible/tfa24-astro:outline-tfa24-acc peer-checked/tfa24-astro:bg-tfa24-panel peer-checked/tfa24-astro:text-tfa24-acc">Astro</label>
        <div class="hidden w-full border-t border-tfa24-edge bg-tfa24-panel peer-checked/tfa24-astro:block">
          <pre class="overflow-x-auto px-5 py-4"><code class="font-tfa24-mono text-[12px] leading-[1.65] text-tfa24-code">---
// Faq.astro — renders to plain HTML, ships zero JS
const { items } = Astro.props;
---
&lt;div class="flex flex-col gap-2.5"&gt;
  {items.map(it =&gt; (
    &lt;details open={it.open} class="group rounded-2xl border"&gt;
      &lt;summary class="flex min-h-11 cursor-pointer list-none
                      items-center justify-between px-5 py-4
                      [&amp;::-webkit-details-marker]:hidden"&gt;
        {it.q}
        &lt;i class="size-2 rotate-45 border-b-2 border-r-2
                  group-open:rotate-[225deg]"&gt;&lt;/i&gt;
      &lt;/summary&gt;
      &lt;p class="px-5 pb-4 text-sm"&gt;{it.a}&lt;/p&gt;
    &lt;/details&gt;
  ))}
&lt;/div&gt;
&lt;!-- no client: directive — none needed --&gt;</code></pre>
        </div>
      </div>
    </div>

    <p class="mt-5 text-[12.5px] text-tfa24-mut">The tab viewer above is the radio hack from demo 01, with named peers. Patterns compound.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa24-bg: #1e1a26;
  --color-tfa24-bg: oklch(0.21 0.022 285);
  --color-tfa24-panel: #262030;
  --color-tfa24-panel: oklch(0.25 0.026 285);
  --color-tfa24-viewer: #191521;
  --color-tfa24-viewer: oklch(0.18 0.02 285);
  --color-tfa24-glow: #3a2444;
  --color-tfa24-glow: oklch(0.3 0.06 310 / 0.5);
  --color-tfa24-ink: #f3f0f7;
  --color-tfa24-ink: oklch(0.96 0.006 280);
  --color-tfa24-mut: #bab2c6;
  --color-tfa24-mut: oklch(0.79 0.018 282);
  --color-tfa24-edge: #3a3348;
  --color-tfa24-edge: oklch(0.35 0.028 284);
  --color-tfa24-accedge: #9a6cc0;
  --color-tfa24-accedge: oklch(0.62 0.11 310);
  --color-tfa24-tint: #33244a;
  --color-tfa24-tint: oklch(0.29 0.055 310);
  --color-tfa24-acc: #dda8f0;
  --color-tfa24-acc: oklch(0.82 0.13 310);
  --color-tfa24-code: #ded2ec;
  --color-tfa24-code: oklch(0.88 0.03 300);
  --font-tfa24-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa24-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-24 {
  width: 100%;
  min-height: 100svh;
}

.tfa-24 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-24 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .tfa-24 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-24 details::details-content {
    transition-duration: 1ms;
  }
}
```
