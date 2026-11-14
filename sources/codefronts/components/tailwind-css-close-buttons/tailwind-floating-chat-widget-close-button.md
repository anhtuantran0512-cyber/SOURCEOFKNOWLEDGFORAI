---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/tailwind-floating-chat-widget-close-button/"
title: "Tailwind Floating Chat Widget Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "The support-widget launcher: a gradient FAB whose chat bubble spins out as the × spins in, driven entirely by group-aria-expanded: — the script flips one…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Chat Widget Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/tailwind-floating-chat-widget-close-button/

The support-widget launcher: a gradient FAB whose chat bubble spins out as the × spins in, driven entirely by group-aria-expanded: — the script flips one ARIA attribute and never touches a class. The panel enters and exits on data-open: with a visibility transition, so the original's setTimeout/hidden juggling is gone, and Esc now closes it.
## HTML
```html
<section class="tcb-04 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb04-bg),var(--color-tcb04-bg2))] px-6 py-12 font-tcb04-sans text-tcb04-ink" aria-label="Floating chat close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="relative flex h-72 w-full max-w-[20rem] items-end justify-end">
      <div id="tcb-04-panel" role="dialog" aria-label="Support chat" class="invisible absolute end-0 bottom-20 w-64 translate-y-2 rounded-2xl rounded-ee-sm bg-white opacity-0 shadow-[0_20px_46px_-22px_var(--color-tcb04-shadow)] ring-1 ring-tcb04-ink/5 transition-[translate,opacity,visibility] duration-250 data-open:visible data-open:translate-y-0 data-open:opacity-100 motion-reduce:transition-none">
        <div class="flex items-center gap-3 border-b border-tcb04-ink/8 px-4 py-3">
          <span aria-hidden="true" class="relative size-8 rounded-full bg-linear-to-br from-tcb04-a to-tcb04-b after:absolute after:-end-0.5 after:-bottom-0.5 after:size-2.5 after:rounded-full after:bg-emerald-500 after:ring-2 after:ring-white"></span>
          <div><div class="text-sm font-semibold">Support</div><div class="text-xs text-tcb04-mut">Typically replies in 2 min</div></div>
        </div>
        <p class="px-4 py-4 text-sm/[1.55]">Hi there — how can we help today?</p>
      </div>
      <button id="tcb-04-fab" type="button" aria-expanded="false" aria-controls="tcb-04-panel" aria-label="Open chat" class="group grid size-15 cursor-pointer place-items-center rounded-full bg-linear-140 from-tcb04-a to-tcb04-b shadow-[0_14px_30px_-12px_var(--color-tcb04-glow)] transition duration-200 hover:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb04-a active:scale-93 motion-reduce:transition-none">
        <span aria-hidden="true" class="relative col-start-1 row-start-1 size-6 transition duration-250 before:absolute before:inset-x-0 before:top-0.5 before:bottom-1.5 before:rounded-lg before:bg-white after:absolute after:bottom-px after:left-1.5 after:size-2 after:bg-white after:[clip-path:polygon(0_0,100%_0,0_100%)] group-aria-expanded:rotate-90 group-aria-expanded:scale-40 group-aria-expanded:opacity-0 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="relative col-start-1 row-start-1 size-6 -rotate-90 scale-40 opacity-0 transition duration-250 before:absolute before:top-1/2 before:left-1/2 before:h-[2.5px] before:w-[18px] before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-[2.5px] after:w-[18px] after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white group-aria-expanded:rotate-0 group-aria-expanded:scale-100 group-aria-expanded:opacity-100 motion-reduce:transition-none"></span>
      </button>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb04-mono text-[11.5px] text-tcb04-mut ring-1 ring-tcb04-ink/10">group-aria-expanded: · data-open: · Esc closes</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb04-bg: #f6f4fb;
  --color-tcb04-bg: oklch(0.97 0.008 280);
  --color-tcb04-bg2: #e9e4f6;
  --color-tcb04-bg2: oklch(0.93 0.02 290);
  --color-tcb04-ink: #36304a;
  --color-tcb04-ink: oklch(0.32 0.03 290);
  --color-tcb04-mut: #686279;
  --color-tcb04-mut: oklch(0.5 0.03 290);
  --color-tcb04-a: #7359e8;
  --color-tcb04-a: oklch(0.58 0.19 280);
  --color-tcb04-b: #7a3fc4;
  --color-tcb04-b: oklch(0.5 0.2 300);
  --color-tcb04-glow: #6d36b8b3;
  --color-tcb04-glow: oklch(0.5 0.2 290 / 0.7);
  --color-tcb04-shadow: #5d3d9a8c;
  --color-tcb04-shadow: oklch(0.4 0.12 290 / 0.55);
  --font-tcb04-sans: 'Geist', system-ui, sans-serif;
  --font-tcb04-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-04 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const fab = document.getElementById('tcb-04-fab');
  if (!fab || fab.dataset.wired) return;
  fab.dataset.wired = '1';
  const panel = document.getElementById('tcb-04-panel');
  const set = (open) => {
    fab.setAttribute('aria-expanded', String(open));
    fab.setAttribute('aria-label', open ? 'Close chat' : 'Open chat');
    panel.toggleAttribute('data-open', open);
    panel.inert = !open;
  };
  set(false);
  fab.addEventListener('click', () => set(fab.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && fab.getAttribute('aria-expanded') === 'true') { set(false); fab.focus(); }
  });
})();
```
