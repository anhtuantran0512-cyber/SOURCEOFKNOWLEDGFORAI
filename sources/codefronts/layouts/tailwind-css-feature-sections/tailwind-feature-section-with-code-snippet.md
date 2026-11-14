---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-with-code-snippet/"
title: "Tailwind Feature Section with Code Snippet"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "An editor-window feature block: file tabs (radio state), CSS-counter line numbers, a highlighted diff line and a copy button — beside three developer benefits."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Section with Code Snippet
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-with-code-snippet/

An editor-window feature block: file tabs (radio state), CSS-counter line numbers, a highlighted diff line and a copy button — beside three developer benefits. Line numbers are before:content-[counter(line)] on each line span, so copying the code never copies the numbers.
## HTML
```html
<section class="tfs-17 relative w-full min-h-svh overflow-hidden bg-tfs17-bg px-5 py-20 font-tfs17-sans text-white antialiased sm:py-28" aria-labelledby="tfs-17-h">
  <div aria-hidden="true" class="absolute inset-0 bg-[radial-gradient(50%_40%_at_75%_40%,color-mix(in_oklab,var(--color-tfs17-acc)_25%,transparent),transparent)]"></div>
  <div class="relative mx-auto grid w-full max-w-6xl gap-12 lg:grid-cols-[1fr_1.3fr] lg:items-center lg:gap-16">
    <div class="grid gap-8">
      <div class="grid gap-4">
        <p class="font-tfs17-mono text-xs uppercase tracking-[0.18em] text-tfs17-acc">Quill SDK</p>
        <h2 id="tfs-17-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">Add realtime docs in eleven lines</h2>
        <p class="text-pretty text-lg text-tfs17-mut">Drop in the provider, point it at a room, and every editor is multiplayer.</p>
      </div>
      <ul class="grid gap-4">
        <li class="flex gap-3"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mt-1 size-5 flex-none text-tfs17-acc"><path d="M20 6 9 17l-5-5"/></svg><span><strong class="font-semibold">CRDT under the hood.</strong> <span class="text-tfs17-mut">Conflict-free merges, offline first.</span></span></li>
        <li class="flex gap-3"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mt-1 size-5 flex-none text-tfs17-acc"><path d="M20 6 9 17l-5-5"/></svg><span><strong class="font-semibold">Typed end to end.</strong> <span class="text-tfs17-mut">Your schema, inferred in the editor.</span></span></li>
        <li class="flex gap-3"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mt-1 size-5 flex-none text-tfs17-acc"><path d="M20 6 9 17l-5-5"/></svg><span><strong class="font-semibold">3 kB gzipped.</strong> <span class="text-tfs17-mut">Tree-shakes to what you use.</span></span></li>
      </ul>
      <div class="flex flex-wrap gap-3"><a href="#tfs-17-h" class="inline-flex min-h-11 items-center rounded-full bg-white px-5 text-sm font-semibold text-tfs17-bg transition hover:bg-tfs17-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs17-acc">Read the docs</a><code class="inline-flex min-h-11 items-center rounded-full bg-white/5 px-5 font-tfs17-mono text-sm text-tfs17-mut ring-1 ring-white/10">npm i @quill/react</code></div>
    </div>
    <div class="group/ed overflow-hidden rounded-2xl bg-tfs17-code shadow-[0_40px_100px_-30px_rgb(0_0_0/0.8)] ring-1 ring-white/10" data-tfs17>
      <div class="flex items-center gap-3 border-b border-white/10 bg-white/[0.02] px-4">
        <span aria-hidden="true" class="flex gap-1.5"><i class="size-3 rounded-full bg-white/15"></i><i class="size-3 rounded-full bg-white/15"></i><i class="size-3 rounded-full bg-white/15"></i></span>
        <fieldset class="flex"><legend class="sr-only">File</legend>
          <label class="inline-flex min-h-11 cursor-pointer items-center border-b-2 border-transparent px-3 font-tfs17-mono text-xs text-tfs17-mut transition hover:text-white has-checked:border-tfs17-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tfs17-acc"><input type="radio" name="tfs-17-f" id="tfs-17-f1" class="sr-only" checked>Editor.tsx</label>
          <label class="inline-flex min-h-11 cursor-pointer items-center border-b-2 border-transparent px-3 font-tfs17-mono text-xs text-tfs17-mut transition hover:text-white has-checked:border-tfs17-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tfs17-acc"><input type="radio" name="tfs-17-f" id="tfs-17-f2" class="sr-only">schema.ts</label>
        </fieldset>
        <button type="button" data-copy class="group/btn ml-auto inline-flex min-h-9 items-center gap-1.5 rounded-lg px-3 text-xs text-tfs17-mut ring-1 ring-white/10 transition hover:bg-white/10 hover:text-white focus-visible:outline-2 focus-visible:outline-tfs17-acc data-copied:text-tfs17-acc"><span class="group-data-copied/btn:hidden"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M8 8h12v12H8zM16 8V4H4v12h4"/></svg></span><span class="hidden group-data-copied/btn:block"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="group-data-copied/btn:hidden">Copy</span><span class="hidden group-data-copied/btn:inline">Copied</span></button>
        <span role="status" class="sr-only"></span>
      </div>
      <pre tabindex="0" data-file="f1" class="hidden overflow-x-auto py-5 pr-5 font-tfs17-mono text-[13px] leading-6 text-slate-200 group-has-[#tfs-17-f1:checked]/ed:block focus-visible:outline-2 focus-visible:outline-tfs17-acc"><code class="block [counter-reset:line] [&>span]:block [&>span]:pl-4 [&>span]:before:mr-5 [&>span]:before:inline-block [&>span]:before:w-5 [&>span]:before:text-right [&>span]:before:text-white/25 [&>span]:before:select-none [&>span]:before:[counter-increment:line] [&>span]:before:content-[counter(line)]"><span><span class="text-tfs17-key">import</span> { QuillProvider, useRoom } <span class="text-tfs17-key">from</span> <span class="text-tfs17-str">'@quill/react'</span>;</span><span>&nbsp;</span><span><span class="text-tfs17-key">export function</span> <span class="text-tfs17-fn">Editor</span>({ docId }) {</span><span>  <span class="text-tfs17-key">return</span> (</span><span class="bg-tfs17-acc/10 shadow-[inset_2px_0_0_var(--color-tfs17-acc)]">    &lt;<span class="text-tfs17-fn">QuillProvider</span> room={docId} presence&gt;</span><span>      &lt;<span class="text-tfs17-fn">Canvas</span> /&gt;</span><span>      &lt;<span class="text-tfs17-fn">Cursors</span> /&gt;</span><span>    &lt;/<span class="text-tfs17-fn">QuillProvider</span>&gt;</span><span>  );</span><span>}</span></code></pre>
      <pre tabindex="0" data-file="f2" class="hidden overflow-x-auto py-5 pr-5 font-tfs17-mono text-[13px] leading-6 text-slate-200 group-has-[#tfs-17-f2:checked]/ed:block focus-visible:outline-2 focus-visible:outline-tfs17-acc"><code class="block [counter-reset:line] [&>span]:block [&>span]:pl-4 [&>span]:before:mr-5 [&>span]:before:inline-block [&>span]:before:w-5 [&>span]:before:text-right [&>span]:before:text-white/25 [&>span]:before:select-none [&>span]:before:[counter-increment:line] [&>span]:before:content-[counter(line)]"><span><span class="text-tfs17-key">import</span> { defineSchema } <span class="text-tfs17-key">from</span> <span class="text-tfs17-str">'@quill/core'</span>;</span><span>&nbsp;</span><span><span class="text-tfs17-key">export const</span> schema = <span class="text-tfs17-fn">defineSchema</span>({</span><span>  title: <span class="text-tfs17-str">'text'</span>,</span><span class="bg-tfs17-acc/10 shadow-[inset_2px_0_0_var(--color-tfs17-acc)]">  body: <span class="text-tfs17-str">'richtext'</span>,</span><span>  tags: <span class="text-tfs17-str">'list&lt;string&gt;'</span>,</span><span>});</span></code></pre>
      <div class="flex items-center gap-4 border-t border-white/10 px-4 py-2 font-tfs17-mono text-[11px] text-tfs17-mut"><span class="flex items-center gap-1.5"><span class="size-1.5 rounded-full bg-tfs17-acc"></span>3 collaborators</span><span>TypeScript</span><span class="ml-auto">UTF-8</span></div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs17-bg: #0a0b10;
  --color-tfs17-bg: oklch(0.151 0.011 276);
  --color-tfs17-code: #10121a;
  --color-tfs17-code: oklch(0.184 0.017 274);
  --color-tfs17-mut: #a1a7b8;
  --color-tfs17-mut: oklch(0.729 0.025 270);
  --color-tfs17-acc: #facc15;
  --color-tfs17-acc: oklch(0.861 0.173 92);
  --color-tfs17-key: #c084fc;
  --color-tfs17-key: oklch(0.722 0.177 306);
  --color-tfs17-str: #86efac;
  --color-tfs17-str: oklch(0.871 0.136 154);
  --color-tfs17-fn: #7dd3fc;
  --color-tfs17-fn: oklch(0.828 0.101 230);
  --font-tfs17-sans: 'Geist', system-ui, sans-serif;
  --font-tfs17-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const copyText = async (text) => {
    try { await navigator.clipboard.writeText(text); return true; }
    catch {
      const ta = Object.assign(document.createElement('textarea'), { value: text });
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;opacity:0';
      document.body.append(ta); ta.select();
      const ok = document.execCommand('copy'); ta.remove(); return ok;
    }
  };
  document.querySelectorAll('[data-tfs17]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const btn = root.querySelector('[data-copy]');
    const status = root.querySelector('[role="status"]');
    let t = 0;
    btn.addEventListener('click', async () => {
      const f = root.querySelector('input[name="tfs-17-f"]:checked').id.replace('tfs-17-', '');
      const lines = [...root.querySelectorAll('pre[data-file="' + f + '"] code > span')].map((s) => s.textContent.replace(/\u00a0/g, ''));
      const ok = await copyText(lines.join('\n'));
      clearTimeout(t);
      if (ok) { btn.setAttribute('data-copied', ''); status.textContent = 'Code copied'; }
      else status.textContent = 'Copy failed';
      t = setTimeout(() => { btn.removeAttribute('data-copied'); status.textContent = ''; }, 1800);
    });
  });
})();
```
