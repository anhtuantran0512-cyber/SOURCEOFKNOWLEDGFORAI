---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-sidebar-navigation-is-not-a-tab-list/"
title: "Tailwind Sidebar Navigation Is Not a Tab List"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "The boundary marker."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Navigation Is Not a Tab List
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-sidebar-navigation-is-not-a-tab-list/

The boundary marker. A sidebar is a list of links that navigate; a tab list is a set of controls that swap a panel in place, and the two have different roles, different attributes and different keyboard contracts. This is the correct build &mdash; <nav>, <ul>, <a>, aria-current="page" &mdash; with every visual decision in utilities and not one line of script.
## HTML
```html
<section class="tsb-04 block relative w-full min-h-svh bg-tsb04-bg text-tsb04-ink font-tsb04-sans leading-[1.55]" aria-label="Quill learning centre">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-04-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-04-theme">
    <label class="grid place-items-center w-11 h-11 border-0 bg-tsb04-surf2 text-tsb04-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb04-acc peer-focus-visible:outline-offset-2" for="tsb-04-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] min-h-svh r46:grid-cols-[15rem_minmax(0,1fr)]">
    <nav class="min-w-0 px-2 py-4 bg-tsb04-surf border-b border-tsb04-line r46:border-b-0 r46:border-r r46:border-tsb04-line" aria-label="Quill learning centre">
      <p class="m-0 mb-3.5 px-3 font-tsb04-display text-[1.05rem] font-bold tracking-[0.18em] uppercase">Quill</p>
      <ul class="list-none m-0 p-0 grid gap-[2px]">
        <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 bg-tsb04-surf text-[0.92rem] text-tsb04-ink no-underline hover:bg-tsb04-accsoft focus-visible:outline-2 focus-visible:outline-tsb04-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb04-accsoft aria-[current=page]:text-tsb04-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb04-acc)]" href="#tsb-04-main" aria-current="page">Getting started</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 bg-tsb04-surf text-[0.92rem] text-tsb04-ink no-underline hover:bg-tsb04-accsoft focus-visible:outline-2 focus-visible:outline-tsb04-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb04-accsoft aria-[current=page]:text-tsb04-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb04-acc)]" href="#tsb-04-main">Deployments</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 bg-tsb04-surf text-[0.92rem] text-tsb04-ink no-underline hover:bg-tsb04-accsoft focus-visible:outline-2 focus-visible:outline-tsb04-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb04-accsoft aria-[current=page]:text-tsb04-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb04-acc)]" href="#tsb-04-main">Billing</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 bg-tsb04-surf text-[0.92rem] text-tsb04-ink no-underline hover:bg-tsb04-accsoft focus-visible:outline-2 focus-visible:outline-tsb04-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb04-accsoft aria-[current=page]:text-tsb04-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb04-acc)]" href="#tsb-04-main">Audit log</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 bg-tsb04-surf text-[0.92rem] text-tsb04-ink no-underline hover:bg-tsb04-accsoft focus-visible:outline-2 focus-visible:outline-tsb04-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb04-accsoft aria-[current=page]:text-tsb04-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb04-acc)]" href="#tsb-04-main">Integrations</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 bg-tsb04-surf text-[0.92rem] text-tsb04-ink no-underline hover:bg-tsb04-accsoft focus-visible:outline-2 focus-visible:outline-tsb04-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb04-accsoft aria-[current=page]:text-tsb04-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb04-acc)]" href="#tsb-04-main">Certification</a></li>
      </ul>
    </nav>

    <main class="min-w-0 content-start px-5 pt-6 pb-10 r46:px-9 r46:pt-10 r46:pb-12" id="tsb-04-main">
      <p class="m-0 mb-1.5 font-tsb04-display text-[0.8rem] tracking-[0.14em] uppercase text-tsb04-mut">Course &middot; 6 lessons</p>
      <h2 class="m-0 mb-5.5 font-tsb04-display text-[clamp(1.6rem,4.4vw,2.4rem)] leading-[1.05] uppercase">Getting started</h2>
      <div class="grid grid-cols-[minmax(0,1fr)] gap-[2px] bg-tsb04-line border border-tsb04-line r52:grid-cols-2">
        <article class="min-w-0 p-4 bg-tsb04-surf">
          <p class="m-0 mb-1.5 font-tsb04-display text-[0.8rem] tracking-[0.12em] text-tsb04-acc">01</p>
          <h3 class="m-0 mb-1 text-base leading-[1.25]">Create your first workspace</h3>
          <p class="m-0 text-[0.83rem] text-tsb04-mut">8 min &middot; video</p>
        </article>
        <article class="min-w-0 p-4 bg-tsb04-surf">
          <p class="m-0 mb-1.5 font-tsb04-display text-[0.8rem] tracking-[0.12em] text-tsb04-acc">02</p>
          <h3 class="m-0 mb-1 text-base leading-[1.25]">Invite a teammate and set roles</h3>
          <p class="m-0 text-[0.83rem] text-tsb04-mut">5 min &middot; reading</p>
        </article>
        <article class="min-w-0 p-4 bg-tsb04-surf">
          <p class="m-0 mb-1.5 font-tsb04-display text-[0.8rem] tracking-[0.12em] text-tsb04-acc">03</p>
          <h3 class="m-0 mb-1 text-base leading-[1.25]">Connect a repository</h3>
          <p class="m-0 text-[0.83rem] text-tsb04-mut">11 min &middot; walkthrough</p>
        </article>
        <article class="min-w-0 p-4 bg-tsb04-surf">
          <p class="m-0 mb-1.5 font-tsb04-display text-[0.8rem] tracking-[0.12em] text-tsb04-acc">04</p>
          <h3 class="m-0 mb-1 text-base leading-[1.25]">Ship a preview environment</h3>
          <p class="m-0 text-[0.83rem] text-tsb04-mut">14 min &middot; walkthrough</p>
        </article>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb04-bg: #f4f4f5;
  --color-tsb04-bg: oklch(96% 0.002 285);
  --color-tsb04-surf: #ffffff;
  --color-tsb04-surf: oklch(100% 0 0);
  --color-tsb04-surf2: #ebebed;
  --color-tsb04-surf2: oklch(93% 0.003 285);
  --color-tsb04-line: #d4d4d8;
  --color-tsb04-line: oklch(87% 0.005 285);
  --color-tsb04-ink: #18181b;
  --color-tsb04-ink: oklch(21% 0.005 285);
  --color-tsb04-mut: #5f5f68;
  --color-tsb04-mut: oklch(48% 0.01 285);
  --color-tsb04-acc: #6d3ce0;
  --color-tsb04-acc: oklch(52% 0.22 291);
  --color-tsb04-accsoft: #ece4fd;
  --color-tsb04-accsoft: oklch(94% 0.035 291);
  --font-tsb04-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb04-display: 'Archivo Narrow', 'Roboto Condensed', ui-sans-serif, system-ui, sans-serif;
  /* Custom breakpoints, so the port keeps the CSS version's own numbers rather than
       being re-tuned to Tailwind's md/lg scale. */
  --breakpoint-r46: 46rem;
  --breakpoint-r52: 52rem;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.tsb-04 {
  width: 100%;
  min-height: 100svh;
}

.tsb-04 *,
.tsb-04 *::before,
.tsb-04 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-04:has(.tsb-04-theme-input:checked) {
  --color-tsb04-bg: #0e0e11;
  --color-tsb04-surf: #17171b;
  --color-tsb04-surf2: #1f1f25;
  --color-tsb04-line: #2c2c33;
  --color-tsb04-ink: #f2f2f5;
  --color-tsb04-mut: #9d9da8;
  --color-tsb04-acc: #b79bff;
  --color-tsb04-acc: oklch(80% 0.13 292);
  --color-tsb04-accsoft: #241a3d;
}

@media (prefers-color-scheme: dark) {
  .tsb-04 {
    --color-tsb04-bg: #0e0e11;
    --color-tsb04-surf: #17171b;
    --color-tsb04-surf2: #1f1f25;
    --color-tsb04-line: #2c2c33;
    --color-tsb04-ink: #f2f2f5;
    --color-tsb04-mut: #9d9da8;
    --color-tsb04-acc: #b79bff;
    --color-tsb04-acc: oklch(80% 0.13 292);
    --color-tsb04-accsoft: #241a3d;
  }

  .tsb-04:has(.tsb-04-theme-input:checked) {
    --color-tsb04-bg: #f4f4f5;
    --color-tsb04-surf: #ffffff;
    --color-tsb04-surf2: #ebebed;
    --color-tsb04-line: #d4d4d8;
    --color-tsb04-ink: #18181b;
    --color-tsb04-mut: #5f5f68;
    --color-tsb04-acc: #6d3ce0;
    --color-tsb04-acc: oklch(52% 0.22 291);
    --color-tsb04-accsoft: #ece4fd;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-04:has(.tsb-04-theme-input:checked) {
    --color-tsb04-bg: #0e0e11;
    --color-tsb04-surf: #17171b;
    --color-tsb04-surf2: #1f1f25;
    --color-tsb04-line: #2c2c33;
    --color-tsb04-ink: #f2f2f5;
    --color-tsb04-mut: #9d9da8;
    --color-tsb04-acc: #b79bff;
    --color-tsb04-acc: oklch(80% 0.13 292);
    --color-tsb04-accsoft: #241a3d;
  }
}
```
