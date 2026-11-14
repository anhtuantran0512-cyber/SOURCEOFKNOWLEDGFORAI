---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tri-state-checkbox-tailwind-javascript/"
title: "Tri-State Checkbox in Tailwind CSS + JavaScript — Done / N/A / Unset"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A review checklist whose boxes cycle Unset → Done → N/A."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tri-State Checkbox in Tailwind CSS + JavaScript — Done / N/A / Unset
Source: https://codefronts.com/components/tailwind-css-checkboxes/tri-state-checkbox-tailwind-javascript/

A review checklist whose boxes cycle Unset → Done → N/A. The script only writes aria-checked; every visual — fill colour, glyph, status chip — is an ARIA variant: group-aria-checked/btn: and group-aria-[checked=mixed]/btn:. Now the whole row is clickable and every target is 44px.
## HTML
```html
<section class="tcb-25 w-full min-h-svh grid place-items-center bg-tcb25-bg px-5 py-14 font-tcb25-sans text-tcb25-ink selection:bg-tcb25-ring selection:text-white" data-tcb25 aria-label="Multi-state review checklist">
  <div class="w-full max-w-[27rem] divide-y divide-tcb25-line rounded-2xl border border-tcb25-line bg-white px-3 py-1">
    <div class="flex min-h-15 cursor-pointer items-center gap-2 pr-2" data-row><button type="button" role="checkbox" aria-checked="true" aria-labelledby="tcb25-a11y" data-cycle class="group/btn peer grid size-11 flex-none cursor-pointer place-items-center rounded-lg focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tcb25-ring"><span aria-hidden="true" class="grid size-6 place-items-center rounded-[7px] border-2 border-tcb25-box bg-white text-white transition-colors duration-200 group-aria-checked/btn:border-tcb25-yes group-aria-checked/btn:bg-tcb25-yes group-aria-[checked=mixed]/btn:border-tcb25-na group-aria-[checked=mixed]/btn:bg-tcb25-na motion-reduce:transition-none"><span class="col-start-1 row-start-1 opacity-0 transition-opacity group-aria-checked/btn:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="col-start-1 row-start-1 opacity-0 transition-opacity group-aria-[checked=mixed]/btn:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" class="size-3.5"><path d="M6 12h12"/></svg></span></span></button><span id="tcb25-a11y" class="flex-1 text-[15px]">Accessibility audit</span><span aria-hidden="true" class="rounded-md bg-tcb25-chip px-2 py-1 font-tcb25-mono text-[11px] font-semibold uppercase tracking-[0.08em] text-tcb25-mut after:content-['Unset'] peer-aria-checked:bg-tcb25-yes/12 peer-aria-checked:text-tcb25-yesink peer-aria-checked:after:content-['Done'] peer-aria-[checked=mixed]:bg-tcb25-na/15 peer-aria-[checked=mixed]:text-tcb25-naink peer-aria-[checked=mixed]:after:content-['N/A']"></span></div>
    <div class="flex min-h-15 cursor-pointer items-center gap-2 pr-2" data-row><button type="button" role="checkbox" aria-checked="mixed" aria-labelledby="tcb25-perf" data-cycle class="group/btn peer grid size-11 flex-none cursor-pointer place-items-center rounded-lg focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tcb25-ring"><span aria-hidden="true" class="grid size-6 place-items-center rounded-[7px] border-2 border-tcb25-box bg-white text-white transition-colors duration-200 group-aria-checked/btn:border-tcb25-yes group-aria-checked/btn:bg-tcb25-yes group-aria-[checked=mixed]/btn:border-tcb25-na group-aria-[checked=mixed]/btn:bg-tcb25-na motion-reduce:transition-none"><span class="col-start-1 row-start-1 opacity-0 transition-opacity group-aria-checked/btn:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="col-start-1 row-start-1 opacity-0 transition-opacity group-aria-[checked=mixed]/btn:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" class="size-3.5"><path d="M6 12h12"/></svg></span></span></button><span id="tcb25-perf" class="flex-1 text-[15px]">Performance budget</span><span aria-hidden="true" class="rounded-md bg-tcb25-chip px-2 py-1 font-tcb25-mono text-[11px] font-semibold uppercase tracking-[0.08em] text-tcb25-mut after:content-['Unset'] peer-aria-checked:bg-tcb25-yes/12 peer-aria-checked:text-tcb25-yesink peer-aria-checked:after:content-['Done'] peer-aria-[checked=mixed]:bg-tcb25-na/15 peer-aria-[checked=mixed]:text-tcb25-naink peer-aria-[checked=mixed]:after:content-['N/A']"></span></div>
    <div class="flex min-h-15 cursor-pointer items-center gap-2 pr-2" data-row><button type="button" role="checkbox" aria-checked="false" aria-labelledby="tcb25-legal" data-cycle class="group/btn peer grid size-11 flex-none cursor-pointer place-items-center rounded-lg focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tcb25-ring"><span aria-hidden="true" class="grid size-6 place-items-center rounded-[7px] border-2 border-tcb25-box bg-white text-white transition-colors duration-200 group-aria-checked/btn:border-tcb25-yes group-aria-checked/btn:bg-tcb25-yes group-aria-[checked=mixed]/btn:border-tcb25-na group-aria-[checked=mixed]/btn:bg-tcb25-na motion-reduce:transition-none"><span class="col-start-1 row-start-1 opacity-0 transition-opacity group-aria-checked/btn:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="col-start-1 row-start-1 opacity-0 transition-opacity group-aria-[checked=mixed]/btn:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" class="size-3.5"><path d="M6 12h12"/></svg></span></span></button><span id="tcb25-legal" class="flex-1 text-[15px]">Legal review</span><span aria-hidden="true" class="rounded-md bg-tcb25-chip px-2 py-1 font-tcb25-mono text-[11px] font-semibold uppercase tracking-[0.08em] text-tcb25-mut after:content-['Unset'] peer-aria-checked:bg-tcb25-yes/12 peer-aria-checked:text-tcb25-yesink peer-aria-checked:after:content-['Done'] peer-aria-[checked=mixed]:bg-tcb25-na/15 peer-aria-[checked=mixed]:text-tcb25-naink peer-aria-[checked=mixed]:after:content-['N/A']"></span></div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb25-bg: #f4f5f7;
  --color-tcb25-bg: oklch(0.97 0.004 260);
  --color-tcb25-ink: #2a2f3a;
  --color-tcb25-ink: oklch(0.3 0.02 265);
  --color-tcb25-mut: #5d6472;
  --color-tcb25-mut: oklch(0.49 0.02 265);
  --color-tcb25-line: #eef0f3;
  --color-tcb25-line: oklch(0.953 0.005 265);
  --color-tcb25-chip: #f1f2f5;
  --color-tcb25-chip: oklch(0.96 0.005 265);
  --color-tcb25-box: #9aa1ad;
  --color-tcb25-box: oklch(0.71 0.02 265);
  --color-tcb25-yes: #1f8a4c;
  --color-tcb25-yes: oklch(0.55 0.14 152);
  --color-tcb25-yesink: #146b39;
  --color-tcb25-yesink: oklch(0.46 0.12 152);
  --color-tcb25-na: #d4952b;
  --color-tcb25-na: oklch(0.7 0.14 70);
  --color-tcb25-naink: #8a5a0c;
  --color-tcb25-naink: oklch(0.5 0.11 65);
  --color-tcb25-ring: #2f7de1;
  --color-tcb25-ring: oklch(0.6 0.17 255);
  --font-tcb25-sans: 'Geist', system-ui, sans-serif;
  --font-tcb25-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-25 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const CYCLE = ['false', 'true', 'mixed'];
  document.querySelectorAll('[data-tcb25]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    root.querySelectorAll('[data-row]').forEach((row) => {
      const btn = row.querySelector('[data-cycle]');
      btn.addEventListener('click', () => {
        const cur = btn.getAttribute('aria-checked') || 'false';
        btn.setAttribute('aria-checked', CYCLE[(CYCLE.indexOf(cur) + 1) % CYCLE.length]);
      });
      row.addEventListener('click', (e) => { if (!e.target.closest('[data-cycle]')) btn.click(); });
    });
  });
})();
```
