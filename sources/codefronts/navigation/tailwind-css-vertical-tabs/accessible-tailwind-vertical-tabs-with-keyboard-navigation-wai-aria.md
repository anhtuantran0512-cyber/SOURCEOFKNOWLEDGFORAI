---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/accessible-tailwind-vertical-tabs-with-keyboard-navigation-wai-aria/"
title: "Accessible Tailwind Vertical Tabs with Keyboard Navigation (WAI-ARIA)"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "The WAI-ARIA Authoring Practices tablist, done properly in Tailwind: role=\"tablist\" with aria-orientation=\"vertical\", a roving tabindex, Up/Down/Home/End…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Vertical Tabs with Keyboard Navigation (WAI-ARIA)
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/accessible-tailwind-vertical-tabs-with-keyboard-navigation-wai-aria/

The WAI-ARIA Authoring Practices tablist, done properly in Tailwind: role="tablist" with aria-orientation="vertical", a roving tabindex, Up/Down/Home/End with wrap-around, and a live switch between automatic and manual activation. Every visual state is an ARIA or data attribute read by a variant &mdash; aria-selected:, aria-pressed:, group-data-[key=ArrowDown]/root: lights the keycap you just pressed &mdash; and focus rings meet WCAG 2.2 Focus Appearance in both themes.
## HTML
```html
<section id="tvt-18-root" class="tvt-18 group/root w-full min-h-svh grid place-items-center bg-tvt18-bg bg-[radial-gradient(60%_50%_at_15%_0%,var(--color-tvt18-glow),transparent_70%)] px-4 py-14 font-tvt18-sans text-tvt18-ink antialiased sm:px-6" data-mode="auto" aria-label="Accessible Tailwind vertical tabs with keyboard navigation demo">
  <div class="grid w-full max-w-[72rem] gap-7">
    <header class="flex flex-wrap items-end justify-between gap-x-8 gap-y-4">
      <div>
        <p class="inline-flex items-center gap-2 rounded-full bg-tvt18-card px-3 py-1.5 font-tvt18-mono text-[12px] font-semibold text-tvt18-acc-ink ring-1 ring-tvt18-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="10" cy="4" r="1.8" fill="currentColor"/><path d="M4 7.2h12M10 7.2v5M7.2 17.5 10 12.2l2.8 5.3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>WAI-ARIA APG · WCAG 2.2 AA</p>
        <h2 class="mt-3 text-[clamp(28px,4.4vw,44px)] leading-[1.04] font-extrabold tracking-[-0.03em] text-balance">The reference tablist,<br class="max-sm:hidden"> <span class="text-tvt18-acc-ink">built for the keyboard</span></h2>
      </div>
      <p class="max-w-[38ch] text-[15px] leading-relaxed text-tvt18-mut text-pretty">Press <kbd class="rounded border border-tvt18-line bg-tvt18-kbd px-1.5 font-tvt18-mono text-[12.5px] text-tvt18-ink">Tab</kbd> to enter the rail, then use the arrow keys. One tab stop, four tabs, every key announced.</p>
    </header>

    <div class="grid items-start gap-5 lg:grid-cols-[minmax(0,1fr)_18rem]">
      <article class="overflow-hidden rounded-[22px] bg-tvt18-card shadow-tvt18-card ring-1 ring-tvt18-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-600 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
        <div class="grid md:grid-cols-[20rem_minmax(0,1fr)]">
          <div role="tablist" aria-orientation="vertical" aria-label="Accessible tabs guide" class="grid content-start gap-1 border-tvt18-line bg-tvt18-rail p-3 max-md:border-b md:border-e">

          <button type="button" role="tab" id="tvt-18-t1" aria-controls="tvt-18-p1" aria-selected="true" class="group/tab relative flex min-h-14 w-full items-center gap-3 rounded-xl ps-4 pe-3 text-start text-tvt18-mut transition-colors duration-150 hover:bg-tvt18-sel/60 hover:text-tvt18-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tvt18-focus aria-selected:bg-tvt18-sel aria-selected:text-tvt18-ink before:absolute before:inset-y-2.5 before:start-1 before:w-1 before:rounded-full before:bg-tvt18-acc before:opacity-0 before:transition-opacity aria-selected:before:opacity-100 motion-reduce:transition-none motion-reduce:before:transition-none">
            <kbd aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-md border border-tvt18-line bg-tvt18-kbd font-tvt18-mono text-[12.5px] font-semibold text-tvt18-ink shadow-[0_2px_0_var(--color-tvt18-line)] group-aria-selected/tab:border-transparent group-aria-selected/tab:bg-tvt18-acc group-aria-selected/tab:text-tvt18-on group-aria-selected/tab:shadow-none">1</kbd>
            <span class="grid min-w-0 flex-1 leading-tight"><span data-label class="text-[15px] font-bold">Roving tabindex</span><span class="mt-0.5 truncate text-[12.5px] text-tvt18-mut">One stop for the whole rail</span></span>
            <code aria-hidden="true" class="shrink-0 rounded-md px-1.5 py-0.5 font-tvt18-mono text-[11px] text-tvt18-mut ring-1 ring-tvt18-line group-aria-selected/tab:text-tvt18-acc-ink group-aria-selected/tab:ring-tvt18-acc/50 max-[430px]:hidden"><span class="group-aria-selected/tab:hidden">tabindex −1</span><span class="hidden group-aria-selected/tab:inline">tabindex 0</span></code>
          </button>

          <button type="button" role="tab" id="tvt-18-t2" aria-controls="tvt-18-p2" aria-selected="false" tabindex="-1" class="group/tab relative flex min-h-14 w-full items-center gap-3 rounded-xl ps-4 pe-3 text-start text-tvt18-mut transition-colors duration-150 hover:bg-tvt18-sel/60 hover:text-tvt18-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tvt18-focus aria-selected:bg-tvt18-sel aria-selected:text-tvt18-ink before:absolute before:inset-y-2.5 before:start-1 before:w-1 before:rounded-full before:bg-tvt18-acc before:opacity-0 before:transition-opacity aria-selected:before:opacity-100 motion-reduce:transition-none motion-reduce:before:transition-none">
            <kbd aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-md border border-tvt18-line bg-tvt18-kbd font-tvt18-mono text-[12.5px] font-semibold text-tvt18-ink shadow-[0_2px_0_var(--color-tvt18-line)] group-aria-selected/tab:border-transparent group-aria-selected/tab:bg-tvt18-acc group-aria-selected/tab:text-tvt18-on group-aria-selected/tab:shadow-none">2</kbd>
            <span class="grid min-w-0 flex-1 leading-tight"><span data-label class="text-[15px] font-bold">Key bindings</span><span class="mt-0.5 truncate text-[12.5px] text-tvt18-mut">Up · Down · Home · End</span></span>
            <code aria-hidden="true" class="shrink-0 rounded-md px-1.5 py-0.5 font-tvt18-mono text-[11px] text-tvt18-mut ring-1 ring-tvt18-line group-aria-selected/tab:text-tvt18-acc-ink group-aria-selected/tab:ring-tvt18-acc/50 max-[430px]:hidden"><span class="group-aria-selected/tab:hidden">tabindex −1</span><span class="hidden group-aria-selected/tab:inline">tabindex 0</span></code>
          </button>

          <button type="button" role="tab" id="tvt-18-t3" aria-controls="tvt-18-p3" aria-selected="false" tabindex="-1" class="group/tab relative flex min-h-14 w-full items-center gap-3 rounded-xl ps-4 pe-3 text-start text-tvt18-mut transition-colors duration-150 hover:bg-tvt18-sel/60 hover:text-tvt18-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tvt18-focus aria-selected:bg-tvt18-sel aria-selected:text-tvt18-ink before:absolute before:inset-y-2.5 before:start-1 before:w-1 before:rounded-full before:bg-tvt18-acc before:opacity-0 before:transition-opacity aria-selected:before:opacity-100 motion-reduce:transition-none motion-reduce:before:transition-none">
            <kbd aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-md border border-tvt18-line bg-tvt18-kbd font-tvt18-mono text-[12.5px] font-semibold text-tvt18-ink shadow-[0_2px_0_var(--color-tvt18-line)] group-aria-selected/tab:border-transparent group-aria-selected/tab:bg-tvt18-acc group-aria-selected/tab:text-tvt18-on group-aria-selected/tab:shadow-none">3</kbd>
            <span class="grid min-w-0 flex-1 leading-tight"><span data-label class="text-[15px] font-bold">Activation modes</span><span class="mt-0.5 truncate text-[12.5px] text-tvt18-mut">Automatic or manual</span></span>
            <code aria-hidden="true" class="shrink-0 rounded-md px-1.5 py-0.5 font-tvt18-mono text-[11px] text-tvt18-mut ring-1 ring-tvt18-line group-aria-selected/tab:text-tvt18-acc-ink group-aria-selected/tab:ring-tvt18-acc/50 max-[430px]:hidden"><span class="group-aria-selected/tab:hidden">tabindex −1</span><span class="hidden group-aria-selected/tab:inline">tabindex 0</span></code>
          </button>

          <button type="button" role="tab" id="tvt-18-t4" aria-controls="tvt-18-p4" aria-selected="false" tabindex="-1" class="group/tab relative flex min-h-14 w-full items-center gap-3 rounded-xl ps-4 pe-3 text-start text-tvt18-mut transition-colors duration-150 hover:bg-tvt18-sel/60 hover:text-tvt18-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tvt18-focus aria-selected:bg-tvt18-sel aria-selected:text-tvt18-ink before:absolute before:inset-y-2.5 before:start-1 before:w-1 before:rounded-full before:bg-tvt18-acc before:opacity-0 before:transition-opacity aria-selected:before:opacity-100 motion-reduce:transition-none motion-reduce:before:transition-none">
            <kbd aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-md border border-tvt18-line bg-tvt18-kbd font-tvt18-mono text-[12.5px] font-semibold text-tvt18-ink shadow-[0_2px_0_var(--color-tvt18-line)] group-aria-selected/tab:border-transparent group-aria-selected/tab:bg-tvt18-acc group-aria-selected/tab:text-tvt18-on group-aria-selected/tab:shadow-none">4</kbd>
            <span class="grid min-w-0 flex-1 leading-tight"><span data-label class="text-[15px] font-bold">Panel semantics</span><span class="mt-0.5 truncate text-[12.5px] text-tvt18-mut">Focusable, labelled, hidden</span></span>
            <code aria-hidden="true" class="shrink-0 rounded-md px-1.5 py-0.5 font-tvt18-mono text-[11px] text-tvt18-mut ring-1 ring-tvt18-line group-aria-selected/tab:text-tvt18-acc-ink group-aria-selected/tab:ring-tvt18-acc/50 max-[430px]:hidden"><span class="group-aria-selected/tab:hidden">tabindex −1</span><span class="hidden group-aria-selected/tab:inline">tabindex 0</span></code>
          </button>
          </div>
          <div class="grid min-h-[22rem] content-start">

          <div role="tabpanel" id="tvt-18-p1" aria-labelledby="tvt-18-t1" tabindex="0" class="rounded-2xl p-6 animate-tvt18-in focus-visible:outline-3 focus-visible:outline-offset-[-3px] focus-visible:outline-tvt18-focus motion-reduce:animate-none sm:p-7">
            <h3 class="font-tvt18-sans text-[clamp(21px,2.6vw,26px)] leading-tight font-extrabold tracking-[-0.02em] text-balance">One tab stop, not four</h3>
            <p class="mt-2.5 max-w-[52ch] text-[15px] leading-relaxed text-tvt18-mut text-pretty">Exactly one tab carries <code class="font-tvt18-mono text-[13px] text-tvt18-ink">tabindex="0"</code>; the rest are <code class="font-tvt18-mono text-[13px] text-tvt18-ink">-1</code>. <kbd class="font-tvt18-mono text-[13px] text-tvt18-ink">Tab</kbd> moves past the widget, the arrows move inside it.</p>
            <ol aria-label="Tab order of the rail" class="mt-6 grid grid-cols-4 gap-2.5">
              <li class="grid gap-1 rounded-xl bg-tvt18-acc p-3 text-center text-tvt18-on"><span class="font-tvt18-mono text-[20px] font-bold">0</span><span class="text-[11.5px] font-semibold">tab 1</span></li>
              <li class="grid gap-1 rounded-xl p-3 text-center ring-1 ring-tvt18-line"><span class="font-tvt18-mono text-[20px] font-bold">−1</span><span class="text-[11.5px] text-tvt18-mut">tab 2</span></li>
              <li class="grid gap-1 rounded-xl p-3 text-center ring-1 ring-tvt18-line"><span class="font-tvt18-mono text-[20px] font-bold">−1</span><span class="text-[11.5px] text-tvt18-mut">tab 3</span></li>
              <li class="grid gap-1 rounded-xl p-3 text-center ring-1 ring-tvt18-line"><span class="font-tvt18-mono text-[20px] font-bold">−1</span><span class="text-[11.5px] text-tvt18-mut">tab 4</span></li>
            </ol>
            <pre class="mt-4 overflow-x-auto rounded-xl bg-tvt18-code p-4 font-tvt18-mono text-[12.5px] leading-relaxed text-tvt18-code-ink"><code>t.tabIndex = t === active ? 0 : -1;</code></pre>
          </div>

          <div role="tabpanel" id="tvt-18-p2" aria-labelledby="tvt-18-t2" tabindex="0" class="rounded-2xl p-6 animate-tvt18-in focus-visible:outline-3 focus-visible:outline-offset-[-3px] focus-visible:outline-tvt18-focus motion-reduce:animate-none sm:p-7">
            <h3 class="font-tvt18-sans text-[clamp(21px,2.6vw,26px)] leading-tight font-extrabold tracking-[-0.02em] text-balance">Up, Down, Home, End</h3>
            <p class="mt-2.5 max-w-[52ch] text-[15px] leading-relaxed text-tvt18-mut text-pretty">Movement wraps at both ends, and every handler calls <code class="font-tvt18-mono text-[13px] text-tvt18-ink">preventDefault()</code> so the page never scrolls out from under the focus ring.</p>
            <table class="mt-5 w-full overflow-hidden rounded-xl text-start text-[14px] ring-1 ring-tvt18-line">
              <thead class="bg-tvt18-rail text-[12px] text-tvt18-mut"><tr><th scope="col" class="px-4 py-2.5 text-start font-semibold">Key</th><th scope="col" class="px-4 py-2.5 text-start font-semibold">Action</th></tr></thead>
              <tbody class="divide-y divide-tvt18-line">
                <tr><td class="px-4 py-2.5 font-tvt18-mono font-semibold">↓ / →</td><td class="px-4 py-2.5">Next tab, wraps to first</td></tr>
                <tr><td class="px-4 py-2.5 font-tvt18-mono font-semibold">↑ / ←</td><td class="px-4 py-2.5">Previous tab, wraps to last</td></tr>
                <tr><td class="px-4 py-2.5 font-tvt18-mono font-semibold">Home · End</td><td class="px-4 py-2.5">First · last tab</td></tr>
                <tr><td class="px-4 py-2.5 font-tvt18-mono font-semibold">Enter · Space</td><td class="px-4 py-2.5">Select the focused tab (manual mode)</td></tr>
              </tbody>
            </table>
          </div>

          <div role="tabpanel" id="tvt-18-p3" aria-labelledby="tvt-18-t3" tabindex="0" class="rounded-2xl p-6 animate-tvt18-in focus-visible:outline-3 focus-visible:outline-offset-[-3px] focus-visible:outline-tvt18-focus motion-reduce:animate-none sm:p-7">
            <h3 class="font-tvt18-sans text-[clamp(21px,2.6vw,26px)] leading-tight font-extrabold tracking-[-0.02em] text-balance">Automatic or manual</h3>
            <p class="mt-2.5 max-w-[52ch] text-[15px] leading-relaxed text-tvt18-mut text-pretty">Automatic selects on focus. Manual moves focus and waits for Enter or Space — mandatory when a panel fetches data, or five arrow presses fire five requests.</p>
            <div class="mt-5 grid gap-3 sm:grid-cols-2">
              <div class="rounded-xl p-4 ring-1 ring-tvt18-line group-data-[mode=auto]/root:bg-tvt18-sel group-data-[mode=auto]/root:ring-2 group-data-[mode=auto]/root:ring-tvt18-acc"><p class="flex items-center justify-between text-[14.5px] font-bold">Automatic <span class="hidden rounded-full bg-tvt18-acc px-2 py-0.5 text-[11px] text-tvt18-on group-data-[mode=auto]/root:inline">Active</span></p><p class="mt-1 text-[13.5px] text-tvt18-mut">Arrow = focus + select. Best for cheap, local panels.</p></div>
              <div class="rounded-xl p-4 ring-1 ring-tvt18-line group-data-[mode=manual]/root:bg-tvt18-sel group-data-[mode=manual]/root:ring-2 group-data-[mode=manual]/root:ring-tvt18-acc"><p class="flex items-center justify-between text-[14.5px] font-bold">Manual <span class="hidden rounded-full bg-tvt18-acc px-2 py-0.5 text-[11px] text-tvt18-on group-data-[mode=manual]/root:inline">Active</span></p><p class="mt-1 text-[13.5px] text-tvt18-mut">Arrow = focus only; Enter or Space selects.</p></div>
            </div>
          </div>

          <div role="tabpanel" id="tvt-18-p4" aria-labelledby="tvt-18-t4" tabindex="0" class="rounded-2xl p-6 animate-tvt18-in focus-visible:outline-3 focus-visible:outline-offset-[-3px] focus-visible:outline-tvt18-focus motion-reduce:animate-none sm:p-7">
            <h3 class="font-tvt18-sans text-[clamp(21px,2.6vw,26px)] leading-tight font-extrabold tracking-[-0.02em] text-balance">Panels are focusable</h3>
            <p class="mt-2.5 max-w-[52ch] text-[15px] leading-relaxed text-tvt18-mut text-pretty">Each panel is <code class="font-tvt18-mono text-[13px] text-tvt18-ink">tabindex="0"</code> with <code class="font-tvt18-mono text-[13px] text-tvt18-ink">aria-labelledby</code> pointing at its tab, so content is reachable and announced by name. Inactive panels use the <code class="font-tvt18-mono text-[13px] text-tvt18-ink">hidden</code> attribute — never <code class="font-tvt18-mono text-[13px] text-tvt18-ink">opacity-0</code>.</p>
            <ul class="mt-5 grid gap-2">
              <li class="flex gap-3 rounded-xl px-3.5 py-3 ring-1 ring-tvt18-line"><span class="shrink-0 font-tvt18-mono text-[12px] font-semibold text-tvt18-acc-ink tabular-nums">2.1.1</span><span class="text-[14px] leading-snug"><b class="font-bold">Keyboard</b> <span class="text-tvt18-mut">— every action works without a pointer</span></span></li>
              <li class="flex gap-3 rounded-xl px-3.5 py-3 ring-1 ring-tvt18-line"><span class="shrink-0 font-tvt18-mono text-[12px] font-semibold text-tvt18-acc-ink tabular-nums">2.4.7</span><span class="text-[14px] leading-snug"><b class="font-bold">Focus Visible</b> <span class="text-tvt18-mut">— 3px outline, offset from the control</span></span></li>
              <li class="flex gap-3 rounded-xl px-3.5 py-3 ring-1 ring-tvt18-line"><span class="shrink-0 font-tvt18-mono text-[12px] font-semibold text-tvt18-acc-ink tabular-nums">2.4.13</span><span class="text-[14px] leading-snug"><b class="font-bold">Focus Appearance</b> <span class="text-tvt18-mut">— ≥ 3:1 against both neighbours, both themes</span></span></li>
              <li class="flex gap-3 rounded-xl px-3.5 py-3 ring-1 ring-tvt18-line"><span class="shrink-0 font-tvt18-mono text-[12px] font-semibold text-tvt18-acc-ink tabular-nums">2.5.8</span><span class="text-[14px] leading-snug"><b class="font-bold">Target Size</b> <span class="text-tvt18-mut">— tabs are 56px tall, keys 44px</span></span></li>
            </ul>
          </div>
          </div>
        </div>
      </article>

      <aside aria-label="Keyboard inspector" class="hidden gap-4 rounded-[22px] bg-tvt18-card p-5 shadow-tvt18-card ring-1 ring-tvt18-line group-data-ready/root:grid">
        <div>
          <p id="tvt-18-modelabel" class="text-[13px] font-bold">Activation</p>
          <div role="group" aria-labelledby="tvt-18-modelabel" class="mt-2 grid grid-cols-2 gap-1 rounded-xl bg-tvt18-rail p-1 ring-1 ring-tvt18-line">
            <button type="button" data-mode-btn="auto" aria-pressed="true" class="min-h-11 rounded-lg text-[14px] font-bold text-tvt18-mut transition-colors hover:text-tvt18-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tvt18-focus aria-pressed:bg-tvt18-card aria-pressed:text-tvt18-ink aria-pressed:shadow-tvt18-seg motion-reduce:transition-none">Automatic</button>
            <button type="button" data-mode-btn="manual" aria-pressed="false" class="min-h-11 rounded-lg text-[14px] font-bold text-tvt18-mut transition-colors hover:text-tvt18-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tvt18-focus aria-pressed:bg-tvt18-card aria-pressed:text-tvt18-ink aria-pressed:shadow-tvt18-seg motion-reduce:transition-none">Manual</button>
          </div>
        </div>
        <div>
          <p class="text-[13px] font-bold">Keys <span class="font-normal text-tvt18-mut">— last press lights up</span></p>
          <div aria-hidden="true" class="mt-2.5 grid gap-1.5">
            <div class="flex justify-center"><kbd data-k="ArrowUp" class="grid min-h-11 min-w-11 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=ArrowUp]/root:translate-y-[3px] group-data-[key=ArrowUp]/root:border-transparent group-data-[key=ArrowUp]/root:bg-tvt18-acc group-data-[key=ArrowUp]/root:text-tvt18-on group-data-[key=ArrowUp]/root:shadow-none motion-reduce:transition-none">↑</kbd></div>
            <div class="flex justify-center gap-1.5"><kbd data-k="ArrowLeft" class="grid min-h-11 min-w-11 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=ArrowLeft]/root:translate-y-[3px] group-data-[key=ArrowLeft]/root:border-transparent group-data-[key=ArrowLeft]/root:bg-tvt18-acc group-data-[key=ArrowLeft]/root:text-tvt18-on group-data-[key=ArrowLeft]/root:shadow-none motion-reduce:transition-none">←</kbd><kbd data-k="ArrowDown" class="grid min-h-11 min-w-11 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=ArrowDown]/root:translate-y-[3px] group-data-[key=ArrowDown]/root:border-transparent group-data-[key=ArrowDown]/root:bg-tvt18-acc group-data-[key=ArrowDown]/root:text-tvt18-on group-data-[key=ArrowDown]/root:shadow-none motion-reduce:transition-none">↓</kbd><kbd data-k="ArrowRight" class="grid min-h-11 min-w-11 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=ArrowRight]/root:translate-y-[3px] group-data-[key=ArrowRight]/root:border-transparent group-data-[key=ArrowRight]/root:bg-tvt18-acc group-data-[key=ArrowRight]/root:text-tvt18-on group-data-[key=ArrowRight]/root:shadow-none motion-reduce:transition-none">→</kbd></div>
            <div class="mt-1.5 grid grid-cols-3 gap-1.5"><kbd data-k="Home" class="grid min-h-11 min-w-0 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=Home]/root:translate-y-[3px] group-data-[key=Home]/root:border-transparent group-data-[key=Home]/root:bg-tvt18-acc group-data-[key=Home]/root:text-tvt18-on group-data-[key=Home]/root:shadow-none motion-reduce:transition-none">Home</kbd><kbd data-k="End" class="grid min-h-11 min-w-0 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=End]/root:translate-y-[3px] group-data-[key=End]/root:border-transparent group-data-[key=End]/root:bg-tvt18-acc group-data-[key=End]/root:text-tvt18-on group-data-[key=End]/root:shadow-none motion-reduce:transition-none">End</kbd><kbd data-k="Tab" class="grid min-h-11 min-w-0 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=Tab]/root:translate-y-[3px] group-data-[key=Tab]/root:border-transparent group-data-[key=Tab]/root:bg-tvt18-acc group-data-[key=Tab]/root:text-tvt18-on group-data-[key=Tab]/root:shadow-none motion-reduce:transition-none">Tab</kbd></div>
            <div class="grid grid-cols-[1fr_2fr] gap-1.5"><kbd data-k="Enter" class="grid min-h-11 min-w-0 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=Enter]/root:translate-y-[3px] group-data-[key=Enter]/root:border-transparent group-data-[key=Enter]/root:bg-tvt18-acc group-data-[key=Enter]/root:text-tvt18-on group-data-[key=Enter]/root:shadow-none motion-reduce:transition-none">Enter</kbd><kbd data-k="Space" class="grid min-h-11 min-w-0 place-items-center rounded-lg border border-tvt18-line bg-tvt18-kbd px-2 font-tvt18-mono text-[13px] font-semibold text-tvt18-ink shadow-[0_3px_0_var(--color-tvt18-line)] transition-[background-color,color,translate,box-shadow] duration-150 group-data-[key=Space]/root:translate-y-[3px] group-data-[key=Space]/root:border-transparent group-data-[key=Space]/root:bg-tvt18-acc group-data-[key=Space]/root:text-tvt18-on group-data-[key=Space]/root:shadow-none motion-reduce:transition-none">Space</kbd></div>
          </div>
        </div>
        <dl class="grid gap-2 text-[12.5px]">
          <div class="flex items-center justify-between gap-3 rounded-xl bg-tvt18-rail px-3 py-2.5 ring-1 ring-tvt18-line"><dt class="text-tvt18-mut">Focused</dt><dd id="tvt-18-focus" class="truncate font-bold">—</dd></div>
          <div class="flex items-center justify-between gap-3 rounded-xl bg-tvt18-rail px-3 py-2.5 ring-1 ring-tvt18-line"><dt class="text-tvt18-mut">Selected</dt><dd id="tvt-18-sel" class="truncate font-bold">Roving tabindex</dd></div>
        </dl>
        <p id="tvt-18-log" role="status" aria-live="polite" class="min-h-11 rounded-xl bg-tvt18-code px-3.5 py-3 font-tvt18-mono text-[12.5px] leading-snug text-tvt18-code-ink">Focus a tab, then press ↑ ↓ Home End</p>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt18-bg: #eff7fe;
  --color-tvt18-bg: oklch(0.972 0.012 245);
  --color-tvt18-glow: #bee4ffb3;
  --color-tvt18-glow: oklch(0.9 0.06 240 / 0.7);
  --color-tvt18-card: #ffffff;
  --color-tvt18-card: oklch(1 0 0);
  --color-tvt18-rail: #f1f8fd;
  --color-tvt18-rail: oklch(0.975 0.01 245);
  --color-tvt18-ink: #091628;
  --color-tvt18-ink: oklch(0.2 0.04 255);
  --color-tvt18-mut: #415166;
  --color-tvt18-mut: oklch(0.43 0.04 255);
  --color-tvt18-line: #c3d3e4;
  --color-tvt18-line: oklch(0.86 0.03 250);
  --color-tvt18-acc: #005dca;
  --color-tvt18-acc: oklch(0.5 0.19 258);
  --color-tvt18-acc-ink: #0049b3;
  --color-tvt18-acc-ink: oklch(0.44 0.19 260);
  --color-tvt18-on: #ffffff;
  --color-tvt18-on: oklch(1 0 0);
  --color-tvt18-sel: #e2f0ff;
  --color-tvt18-sel: oklch(0.95 0.03 250);
  --color-tvt18-kbd: #f7fafe;
  --color-tvt18-kbd: oklch(0.985 0.006 250);
  --color-tvt18-focus: #0045c6;
  --color-tvt18-focus: oklch(0.45 0.23 262);
  --color-tvt18-code: #0e1b2d;
  --color-tvt18-code: oklch(0.22 0.04 258);
  --color-tvt18-code-ink: #bde5f9;
  --color-tvt18-code-ink: oklch(0.9 0.05 230);
  --font-tvt18-sans: 'Atkinson Hyperlegible Next', system-ui, sans-serif;
  --font-tvt18-mono: 'Atkinson Hyperlegible Mono', ui-monospace, monospace;
  --shadow-tvt18-card: 0 1px 2px oklch(0.25 0.05 255 / 0.06), 0 26px 60px -28px oklch(0.35 0.12 255 / 0.32);
  --shadow-tvt18-seg: 0 1px 2px oklch(0.25 0.05 255 / 0.14), 0 4px 10px -4px oklch(0.35 0.12 255 / 0.25);
  --animate-tvt18-in: tvt18-in 0.32s cubic-bezier(0.16, 1, 0.3, 1);

  @keyframes tvt18-in {
    from {
      opacity: 0;
      translate: 0 6px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-18 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-18:not([data-theme="light"]) {
    --color-tvt18-bg: #040b18;
    --color-tvt18-bg: oklch(0.15 0.03 255);
    --color-tvt18-glow: #002f5680;
    --color-tvt18-glow: oklch(0.3 0.09 250 / 0.5);
    --color-tvt18-card: #0a1524;
    --color-tvt18-card: oklch(0.195 0.035 255);
    --color-tvt18-rail: #07111e;
    --color-tvt18-rail: oklch(0.175 0.032 255);
    --color-tvt18-ink: #f0f6fc;
    --color-tvt18-ink: oklch(0.97 0.01 250);
    --color-tvt18-mut: #b0c0d1;
    --color-tvt18-mut: oklch(0.8 0.03 250);
    --color-tvt18-line: #263951;
    --color-tvt18-line: oklch(0.34 0.05 255);
    --color-tvt18-acc: #4dacf6;
    --color-tvt18-acc: oklch(0.72 0.14 245);
    --color-tvt18-acc-ink: #95d3ff;
    --color-tvt18-acc-ink: oklch(0.84 0.1 240);
    --color-tvt18-on: #041020;
    --color-tvt18-on: oklch(0.17 0.04 255);
    --color-tvt18-sel: #102743;
    --color-tvt18-sel: oklch(0.27 0.06 255);
    --color-tvt18-kbd: #0f1d2f;
    --color-tvt18-kbd: oklch(0.23 0.04 255);
    --color-tvt18-focus: #6ee4ff;
    --color-tvt18-focus: oklch(0.86 0.14 215);
    --color-tvt18-code: #020713;
    --color-tvt18-code: oklch(0.13 0.03 255);
    --color-tvt18-code-ink: #9be4fc;
    --color-tvt18-code-ink: oklch(0.88 0.08 220);
  }
}

.tvt-18[data-theme="dark"] {
  --color-tvt18-bg: #040b18;
  --color-tvt18-bg: oklch(0.15 0.03 255);
  --color-tvt18-glow: #002f5680;
  --color-tvt18-glow: oklch(0.3 0.09 250 / 0.5);
  --color-tvt18-card: #0a1524;
  --color-tvt18-card: oklch(0.195 0.035 255);
  --color-tvt18-rail: #07111e;
  --color-tvt18-rail: oklch(0.175 0.032 255);
  --color-tvt18-ink: #f0f6fc;
  --color-tvt18-ink: oklch(0.97 0.01 250);
  --color-tvt18-mut: #b0c0d1;
  --color-tvt18-mut: oklch(0.8 0.03 250);
  --color-tvt18-line: #263951;
  --color-tvt18-line: oklch(0.34 0.05 255);
  --color-tvt18-acc: #4dacf6;
  --color-tvt18-acc: oklch(0.72 0.14 245);
  --color-tvt18-acc-ink: #95d3ff;
  --color-tvt18-acc-ink: oklch(0.84 0.1 240);
  --color-tvt18-on: #041020;
  --color-tvt18-on: oklch(0.17 0.04 255);
  --color-tvt18-sel: #102743;
  --color-tvt18-sel: oklch(0.27 0.06 255);
  --color-tvt18-kbd: #0f1d2f;
  --color-tvt18-kbd: oklch(0.23 0.04 255);
  --color-tvt18-focus: #6ee4ff;
  --color-tvt18-focus: oklch(0.86 0.14 215);
  --color-tvt18-code: #020713;
  --color-tvt18-code: oklch(0.13 0.03 255);
  --color-tvt18-code-ink: #9be4fc;
  --color-tvt18-code-ink: oklch(0.88 0.08 220);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tvt-18-root');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const list = root.querySelector('[role="tablist"]');
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const log = document.getElementById('tvt-18-log');
  const focusOut = document.getElementById('tvt-18-focus');
  const selOut = document.getElementById('tvt-18-sel');
  const modes = [...root.querySelectorAll('[data-mode-btn]')];
  const name = (t) => t.querySelector('[data-label]').textContent;
  let automatic = true, timer;
  const activate = (tab) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    selOut.textContent = name(tab);
  };
  // Panels ship visible so the page reads top-to-bottom without JS; the script hides all but one.
  activate(tabs.find((t) => t.getAttribute('aria-selected') === 'true') || tabs[0]);
  root.dataset.ready = '';
  root.addEventListener('keydown', (e) => {
    root.dataset.key = e.key === ' ' ? 'Space' : e.key;
    clearTimeout(timer);
    timer = setTimeout(() => delete root.dataset.key, 900);
  });
  list.addEventListener('focusin', (e) => { const t = e.target.closest('[role="tab"]'); if (t) focusOut.textContent = name(t); });
  list.addEventListener('click', (e) => {
    const tab = e.target.closest('[role="tab"]');
    if (tab) { activate(tab); log.textContent = 'Click → selected “' + name(tab) + '”'; }
  });
  list.addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    const last = tabs.length - 1;
    const to = { ArrowDown: i + 1, ArrowRight: i + 1, ArrowUp: i - 1, ArrowLeft: i - 1, Home: 0, End: last }[e.key];
    if (i < 0) return;
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault(); activate(tabs[i]);
      log.textContent = (e.key === ' ' ? 'Space' : 'Enter') + ' → selected “' + name(tabs[i]) + '”';
      return;
    }
    if (to === undefined) return;
    e.preventDefault();
    const next = tabs[(to + tabs.length) % tabs.length];
    next.focus();
    if (automatic) activate(next);
    log.textContent = e.key + ' → ' + (automatic ? 'focus + select' : 'focus only') + ' “' + name(next) + '”';
  });
  modes.forEach((btn) => btn.addEventListener('click', () => {
    automatic = btn.dataset.modeBtn === 'auto';
    root.dataset.mode = btn.dataset.modeBtn;
    modes.forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
    log.textContent = 'Mode → ' + (automatic ? 'automatic activation' : 'manual activation');
  }));
})();
```
