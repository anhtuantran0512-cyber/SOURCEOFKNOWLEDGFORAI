---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/tailwind-checkbox-table-has-row-states-progress-bar/"
title: "Tailwind Checkbox Table with :has() Row States & Progress Bar"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A sprint task board where ticking a box restyles its whole row — tint, accent rail, strikethrough, faded priority and a spring-in Done badge — all from…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Checkbox Table with :has() Row States & Progress Bar
Source: https://codefronts.com/snippets/tailwind-css-tables/tailwind-checkbox-table-has-row-states-progress-bar/

A sprint task board where ticking a box restyles its whole row — tint, accent rail, strikethrough, faded priority and a spring-in Done badge — all from has-checked: and group-has-checked/row:. New: a pure-CSS Hide completed switch (group-has-[#ttb09-hide:checked]/board:has-checked:hidden) and a celebration state when the sprint hits 100%.
## HTML
```html
<section class="ttb-09 grid-cols-1 w-full min-h-svh grid place-items-center bg-ttb09-bg px-5 py-14 font-ttb09-sans text-ttb09-ink" aria-label="Checkbox task table demo">
  <div id="ttb09-board" class="group/board w-full max-w-4xl rounded-3xl bg-white p-6 shadow-[0_1px_2px_oklch(0_0_0/0.04),0_24px_48px_-24px_oklch(0.45_0.15_280/0.3)] ring-1 ring-ttb09-line sm:p-8">
    <header class="mb-6 grid gap-5 sm:grid-cols-[1fr_auto] sm:items-end">
      <div>
        <div class="flex items-center gap-2.5">
          <h2 class="text-xl font-bold tracking-tight">Sprint 24 · Launch prep</h2>
          <span class="hidden items-center gap-1 rounded-full bg-ttb09-ok/12 px-2.5 py-0.5 text-xs font-bold text-ttb09-ok-ink group-data-complete/board:inline-flex animate-ttb09-pop">Sprint complete</span>
        </div>
        <div class="mt-3 flex items-center gap-3">
          <div class="h-2 w-full max-w-72 overflow-hidden rounded-full bg-ttb09-line"><div data-bar class="h-full w-1/5 rounded-full bg-linear-to-r from-ttb09-acc to-ttb09-ok transition-[width] duration-500 motion-reduce:transition-none"></div></div>
          <span data-pct class="text-sm font-bold tabular-nums">20%</span>
        </div>
        <p data-progress role="status" class="mt-1.5 text-xs font-medium text-ttb09-mut">1 of 5 completed</p>
      </div>
      <label class="flex min-h-11 cursor-pointer items-center gap-3 text-sm font-medium text-ttb09-mut">
        <input id="ttb09-hide" type="checkbox" class="peer sr-only">
        <span aria-hidden="true" class="relative h-6 w-10 rounded-full bg-ttb09-line transition peer-checked:bg-ttb09-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-ttb09-acc after:absolute after:top-0.5 after:left-0.5 after:size-5 after:rounded-full after:bg-white after:shadow after:transition peer-checked:after:translate-x-4 motion-reduce:after:transition-none"></span>
        Hide completed
      </label>
    </header>
    <div class="relative overflow-x-auto">
      <table class="w-full min-w-[680px] border-collapse text-left text-sm">
        <caption class="sr-only">Sprint tasks with priority, assignee, due date and status</caption>
        <thead class="[&_th]:border-b-2 [&_th]:border-ttb09-line [&_th]:px-3 [&_th]:py-3 [&_th]:text-[10.5px] [&_th]:font-bold [&_th]:tracking-[0.16em] [&_th]:text-ttb09-mut [&_th]:uppercase">
          <tr><th scope="col" class="w-14"><span class="sr-only">Done</span></th><th scope="col">Task</th><th scope="col">Priority</th><th scope="col">Owner</th><th scope="col">Due</th><th scope="col">Status</th></tr>
        </thead>
        <tbody class="[&_td]:px-3 [&_td]:py-3 [&_td]:align-middle">
          <tr class="group/row border-b border-ttb09-line transition-colors hover:bg-ttb09-acc/4 has-checked:bg-ttb09-done has-checked:shadow-[inset_3px_0_0_var(--color-ttb09-ok)] group-has-[#ttb09-hide:checked]/board:has-checked:hidden">
            <td><label class="relative grid size-11 cursor-pointer place-items-center"><input id="ttb09-t1" type="checkbox" class="peer size-5 cursor-pointer appearance-none rounded-md border-2 border-ttb09-line bg-white transition checked:border-ttb09-acc checked:bg-ttb09-acc hover:border-ttb09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb09-acc"><svg class="pointer-events-none absolute size-3.5 text-white opacity-0 peer-checked:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Mark done: Redesign onboarding flow</span></label></td>
            <td><label for="ttb09-t1" class="cursor-pointer font-semibold decoration-ttb09-ok decoration-2 transition-colors group-has-checked/row:text-ttb09-mut group-has-checked/row:line-through">Redesign onboarding flow</label><div class="mt-0.5 text-xs text-ttb09-mut">Design → engineering handoff</div></td>
            <td><span class="rounded-full bg-red-50 px-2.5 py-1 text-[11px] font-bold text-red-700 transition-opacity group-has-checked/row:opacity-40">High</span></td>
            <td><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-indigo-500 to-cyan-500 text-[11px] font-bold text-white">AK</span><span class="sr-only">Arya Kapoor</span></td>
            <td class="text-xs font-semibold text-red-700 group-has-checked/row:font-normal group-has-checked/row:text-ttb09-mut">Jun 18 · overdue</td>
            <td><span class="inline-flex rounded-full bg-ttb09-acc/8 px-2.5 py-1 text-[11px] font-semibold text-ttb09-acc-ink ring-1 ring-ttb09-acc/20 group-has-checked/row:hidden">In progress</span><span class="hidden items-center gap-1 rounded-full bg-ttb09-ok/12 px-2.5 py-1 text-[11px] font-bold text-ttb09-ok-ink ring-1 ring-ttb09-ok/30 group-has-checked/row:inline-flex animate-ttb09-pop motion-reduce:animate-none">✓ Done</span></td>
          </tr>
          <tr class="group/row border-b border-ttb09-line transition-colors hover:bg-ttb09-acc/4 has-checked:bg-ttb09-done has-checked:shadow-[inset_3px_0_0_var(--color-ttb09-ok)] group-has-[#ttb09-hide:checked]/board:has-checked:hidden">
            <td><label class="relative grid size-11 cursor-pointer place-items-center"><input id="ttb09-t2" type="checkbox" checked class="peer size-5 cursor-pointer appearance-none rounded-md border-2 border-ttb09-line bg-white transition checked:border-ttb09-acc checked:bg-ttb09-acc hover:border-ttb09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb09-acc"><svg class="pointer-events-none absolute size-3.5 text-white opacity-0 peer-checked:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Mark done: Set up CI/CD for staging</span></label></td>
            <td><label for="ttb09-t2" class="cursor-pointer font-semibold decoration-ttb09-ok decoration-2 transition-colors group-has-checked/row:text-ttb09-mut group-has-checked/row:line-through">Set up CI/CD for staging</label><div class="mt-0.5 text-xs text-ttb09-mut">DevOps → GitHub Actions</div></td>
            <td><span class="rounded-full bg-red-50 px-2.5 py-1 text-[11px] font-bold text-red-700 transition-opacity group-has-checked/row:opacity-40">High</span></td>
            <td><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-amber-400 to-red-500 text-[11px] font-bold text-white">MR</span><span class="sr-only">Marcus Reid</span></td>
            <td class="text-xs text-ttb09-mut">Jun 22</td>
            <td><span class="inline-flex rounded-full bg-ttb09-acc/8 px-2.5 py-1 text-[11px] font-semibold text-ttb09-acc-ink ring-1 ring-ttb09-acc/20 group-has-checked/row:hidden">Review</span><span class="hidden items-center gap-1 rounded-full bg-ttb09-ok/12 px-2.5 py-1 text-[11px] font-bold text-ttb09-ok-ink ring-1 ring-ttb09-ok/30 group-has-checked/row:inline-flex animate-ttb09-pop motion-reduce:animate-none">✓ Done</span></td>
          </tr>
          <tr class="group/row border-b border-ttb09-line transition-colors hover:bg-ttb09-acc/4 has-checked:bg-ttb09-done has-checked:shadow-[inset_3px_0_0_var(--color-ttb09-ok)] group-has-[#ttb09-hide:checked]/board:has-checked:hidden">
            <td><label class="relative grid size-11 cursor-pointer place-items-center"><input id="ttb09-t3" type="checkbox" class="peer size-5 cursor-pointer appearance-none rounded-md border-2 border-ttb09-line bg-white transition checked:border-ttb09-acc checked:bg-ttb09-acc hover:border-ttb09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb09-acc"><svg class="pointer-events-none absolute size-3.5 text-white opacity-0 peer-checked:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Mark done: Unit tests for auth module</span></label></td>
            <td><label for="ttb09-t3" class="cursor-pointer font-semibold decoration-ttb09-ok decoration-2 transition-colors group-has-checked/row:text-ttb09-mut group-has-checked/row:line-through">Unit tests for auth module</label><div class="mt-0.5 text-xs text-ttb09-mut">Backend coverage ≥ 80%</div></td>
            <td><span class="rounded-full bg-amber-50 px-2.5 py-1 text-[11px] font-bold text-amber-800 transition-opacity group-has-checked/row:opacity-40">Medium</span></td>
            <td><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-emerald-500 to-sky-500 text-[11px] font-bold text-white">SN</span><span class="sr-only">Selin Novak</span></td>
            <td class="text-xs text-ttb09-mut">Jun 25</td>
            <td><span class="inline-flex rounded-full bg-ttb09-acc/8 px-2.5 py-1 text-[11px] font-semibold text-ttb09-acc-ink ring-1 ring-ttb09-acc/20 group-has-checked/row:hidden">To do</span><span class="hidden items-center gap-1 rounded-full bg-ttb09-ok/12 px-2.5 py-1 text-[11px] font-bold text-ttb09-ok-ink ring-1 ring-ttb09-ok/30 group-has-checked/row:inline-flex animate-ttb09-pop motion-reduce:animate-none">✓ Done</span></td>
          </tr>
          <tr class="group/row border-b border-ttb09-line transition-colors hover:bg-ttb09-acc/4 has-checked:bg-ttb09-done has-checked:shadow-[inset_3px_0_0_var(--color-ttb09-ok)] group-has-[#ttb09-hide:checked]/board:has-checked:hidden">
            <td><label class="relative grid size-11 cursor-pointer place-items-center"><input id="ttb09-t4" type="checkbox" class="peer size-5 cursor-pointer appearance-none rounded-md border-2 border-ttb09-line bg-white transition checked:border-ttb09-acc checked:bg-ttb09-acc hover:border-ttb09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb09-acc"><svg class="pointer-events-none absolute size-3.5 text-white opacity-0 peer-checked:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Mark done: Update API documentation</span></label></td>
            <td><label for="ttb09-t4" class="cursor-pointer font-semibold decoration-ttb09-ok decoration-2 transition-colors group-has-checked/row:text-ttb09-mut group-has-checked/row:line-through">Update API documentation</label><div class="mt-0.5 text-xs text-ttb09-mut">OpenAPI 3.1 spec + Postman</div></td>
            <td><span class="rounded-full bg-ttb09-acc/8 px-2.5 py-1 text-[11px] font-bold text-ttb09-acc-ink transition-opacity group-has-checked/row:opacity-40">Low</span></td>
            <td><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-violet-500 to-pink-500 text-[11px] font-bold text-white">TW</span><span class="sr-only">Theo Walsh</span></td>
            <td class="text-xs text-ttb09-mut">Jun 28</td>
            <td><span class="inline-flex rounded-full bg-ttb09-acc/8 px-2.5 py-1 text-[11px] font-semibold text-ttb09-acc-ink ring-1 ring-ttb09-acc/20 group-has-checked/row:hidden">To do</span><span class="hidden items-center gap-1 rounded-full bg-ttb09-ok/12 px-2.5 py-1 text-[11px] font-bold text-ttb09-ok-ink ring-1 ring-ttb09-ok/30 group-has-checked/row:inline-flex animate-ttb09-pop motion-reduce:animate-none">✓ Done</span></td>
          </tr>
          <tr class="group/row transition-colors hover:bg-ttb09-acc/4 has-checked:bg-ttb09-done has-checked:shadow-[inset_3px_0_0_var(--color-ttb09-ok)] group-has-[#ttb09-hide:checked]/board:has-checked:hidden">
            <td><label class="relative grid size-11 cursor-pointer place-items-center"><input id="ttb09-t5" type="checkbox" class="peer size-5 cursor-pointer appearance-none rounded-md border-2 border-ttb09-line bg-white transition checked:border-ttb09-acc checked:bg-ttb09-acc hover:border-ttb09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb09-acc"><svg class="pointer-events-none absolute size-3.5 text-white opacity-0 peer-checked:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Mark done: Lighthouse performance audit</span></label></td>
            <td><label for="ttb09-t5" class="cursor-pointer font-semibold decoration-ttb09-ok decoration-2 transition-colors group-has-checked/row:text-ttb09-mut group-has-checked/row:line-through">Lighthouse performance audit</label><div class="mt-0.5 text-xs text-ttb09-mut">Target 95+ on all metrics</div></td>
            <td><span class="rounded-full bg-amber-50 px-2.5 py-1 text-[11px] font-bold text-amber-800 transition-opacity group-has-checked/row:opacity-40">Medium</span></td>
            <td><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-rose-500 to-orange-400 text-[11px] font-bold text-white">JP</span><span class="sr-only">James Park</span></td>
            <td class="text-xs text-ttb09-mut">Jul 1</td>
            <td><span class="inline-flex rounded-full bg-ttb09-acc/8 px-2.5 py-1 text-[11px] font-semibold text-ttb09-acc-ink ring-1 ring-ttb09-acc/20 group-has-checked/row:hidden">To do</span><span class="hidden items-center gap-1 rounded-full bg-ttb09-ok/12 px-2.5 py-1 text-[11px] font-bold text-ttb09-ok-ink ring-1 ring-ttb09-ok/30 group-has-checked/row:inline-flex animate-ttb09-pop motion-reduce:animate-none">✓ Done</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb09-bg: #f6f5ff;
  --color-ttb09-bg: oklch(0.97 0.012 285);
  --color-ttb09-line: #e3e1f7;
  --color-ttb09-line: oklch(0.92 0.025 285);
  --color-ttb09-ink: #1e1b4b;
  --color-ttb09-ink: oklch(0.26 0.09 280);
  --color-ttb09-mut: #6a6791;
  --color-ttb09-mut: oklch(0.52 0.06 285);
  --color-ttb09-acc: #6366f1;
  --color-ttb09-acc: oklch(0.59 0.2 277);
  --color-ttb09-acc-ink: #4338ca;
  --color-ttb09-acc-ink: oklch(0.46 0.21 277);
  --color-ttb09-ok: #22c55e;
  --color-ttb09-ok: oklch(0.72 0.19 150);
  --color-ttb09-ok-ink: #15803d;
  --color-ttb09-ok-ink: oklch(0.53 0.14 150);
  --color-ttb09-done: #f0fdf4;
  --color-ttb09-done: oklch(0.98 0.02 155);
  --font-ttb09-sans: 'Outfit', system-ui, sans-serif;
  --animate-ttb09-pop: ttb09-pop 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);

  @keyframes ttb09-pop {
    from {
      transform: scale(0.7);
      opacity: 0;
    }

    to {
      transform: scale(1);
      opacity: 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-09 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('ttb09-board');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const boxes = Array.from(root.querySelectorAll('tbody input[type="checkbox"]'));
  const bar = root.querySelector('[data-bar]');
  const label = root.querySelector('[data-progress]');
  const pct = root.querySelector('[data-pct]');
  const update = () => {
    const done = boxes.filter((b) => b.checked).length;
    const p = Math.round(done / boxes.length * 100);
    bar.style.width = p + '%';
    pct.textContent = p + '%';
    label.textContent = done + ' of ' + boxes.length + ' completed';
    root.toggleAttribute('data-complete', done === boxes.length);
  };
  boxes.forEach((b) => b.addEventListener('change', update));
  update();
})();
```
