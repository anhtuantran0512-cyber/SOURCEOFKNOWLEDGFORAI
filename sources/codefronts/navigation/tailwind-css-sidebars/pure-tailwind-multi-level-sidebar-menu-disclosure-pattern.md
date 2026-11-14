---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-multi-level-sidebar-menu-disclosure-pattern/"
title: "Pure Tailwind Multi Level Sidebar Menu Disclosure Pattern"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "Three levels deep, and the demo exists to document the one Tailwind trap that bites here: group-open: matches through EVERY open ancestor, so a nested tree…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Multi Level Sidebar Menu Disclosure Pattern
Source: https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-multi-level-sidebar-menu-disclosure-pattern/

Three levels deep, and the demo exists to document the one Tailwind trap that bites here: group-open: matches through EVERY open ancestor, so a nested tree rotates chevrons that are still closed. The fix is named groups &mdash; group/l1 and group/l2 with group-open/l1: and group-open/l2: &mdash; and once they are named, three levels cost no more than one.
## HTML
```html
<section class="tsb-15 block relative w-full min-h-svh bg-tsb15-bg text-tsb15-ink font-tsb15-sans leading-[1.55]" aria-label="Basalt knowledge base">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-15-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-15-theme">
    <label class="grid place-items-center w-11 h-11 border border-tsb15-line bg-tsb15-surf text-tsb15-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb15-acc peer-focus-visible:outline-offset-2" for="tsb-15-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] min-h-svh bg-tsb15-surf r48:grid-cols-[minmax(0,17.5rem)_minmax(0,1fr)]">
    <nav class="min-w-0 px-2.5 pt-4 pb-5 border-b border-tsb15-line r48:border-b-0 r48:border-r r48:border-tsb15-line" aria-label="Basalt knowledge base">
      <p class="m-0 mb-3 px-2 font-tsb15-display text-[1.05rem] tracking-[0.02em]">Handbook</p>
      <ul class="list-none m-0 p-0">
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 text-[0.91rem] text-tsb15-ink no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Start here</a></li>
      </ul>

      <details class="group/l1" open>
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 text-[0.91rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden before:content-[''] before:flex-none before:w-1.5 before:h-1.5 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tsb15-mut before:-rotate-45 before:transition-transform before:duration-150 group-open/l1:before:rotate-45 group-has-[a[aria-current=page]]/l1:text-tsb15-acc hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 motion-reduce:before:transition-none">Operations</summary>
        <div class="ml-2.5 border-l border-tsb15-line">
          <details class="group/l2" open>
            <summary class="flex items-center gap-2 min-h-11 py-2 pr-2.5 pl-4.5 text-[0.89rem] font-medium cursor-pointer list-none [&::-webkit-details-marker]:hidden before:content-[''] before:flex-none before:w-1.5 before:h-1.5 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tsb15-mut before:-rotate-45 before:transition-transform before:duration-150 group-open/l2:before:rotate-45 group-has-[a[aria-current=page]]/l2:text-tsb15-acc hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 motion-reduce:before:transition-none">Deployments</summary>
            <ul class="list-none m-0 p-0">
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb15-accsoft aria-[current=page]:text-tsb15-acc aria-[current=page]:font-semibold" href="#tsb-15-main">Promotion policy</a></li>
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb15-accsoft aria-[current=page]:text-tsb15-acc aria-[current=page]:font-semibold" href="#tsb-15-main" aria-current="page">Rollback runbook</a></li>
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb15-accsoft aria-[current=page]:text-tsb15-acc aria-[current=page]:font-semibold" href="#tsb-15-main">Region failover</a></li>
            </ul>
          </details>
          <details class="group/l2">
            <summary class="flex items-center gap-2 min-h-11 py-2 pr-2.5 pl-4.5 text-[0.89rem] font-medium cursor-pointer list-none [&::-webkit-details-marker]:hidden before:content-[''] before:flex-none before:w-1.5 before:h-1.5 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tsb15-mut before:-rotate-45 before:transition-transform before:duration-150 group-open/l2:before:rotate-45 group-has-[a[aria-current=page]]/l2:text-tsb15-acc hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 motion-reduce:before:transition-none">On call</summary>
            <ul class="list-none m-0 p-0">
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Escalation ladder</a></li>
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Incident review</a></li>
            </ul>
          </details>
        </div>
      </details>

      <details class="group/l1">
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 text-[0.91rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden before:content-[''] before:flex-none before:w-1.5 before:h-1.5 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tsb15-mut before:-rotate-45 before:transition-transform before:duration-150 group-open/l1:before:rotate-45 group-has-[a[aria-current=page]]/l1:text-tsb15-acc hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 motion-reduce:before:transition-none">People</summary>
        <div class="ml-2.5 border-l border-tsb15-line">
          <details class="group/l2">
            <summary class="flex items-center gap-2 min-h-11 py-2 pr-2.5 pl-4.5 text-[0.89rem] font-medium cursor-pointer list-none [&::-webkit-details-marker]:hidden before:content-[''] before:flex-none before:w-1.5 before:h-1.5 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tsb15-mut before:-rotate-45 before:transition-transform before:duration-150 group-open/l2:before:rotate-45 group-has-[a[aria-current=page]]/l2:text-tsb15-acc hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 motion-reduce:before:transition-none">Onboarding</summary>
            <ul class="list-none m-0 p-0">
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">First week</a></li>
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Access requests</a></li>
            </ul>
          </details>
          <details class="group/l2">
            <summary class="flex items-center gap-2 min-h-11 py-2 pr-2.5 pl-4.5 text-[0.89rem] font-medium cursor-pointer list-none [&::-webkit-details-marker]:hidden before:content-[''] before:flex-none before:w-1.5 before:h-1.5 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tsb15-mut before:-rotate-45 before:transition-transform before:duration-150 group-open/l2:before:rotate-45 group-has-[a[aria-current=page]]/l2:text-tsb15-acc hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 motion-reduce:before:transition-none">Reviews</summary>
            <ul class="list-none m-0 p-0">
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Cycle calendar</a></li>
              <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 text-[0.88rem] text-tsb15-mut no-underline hover:bg-tsb15-surf2 focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Writing feedback</a></li>
            </ul>
          </details>
        </div>
      </details>
    </nav>

    <main class="min-w-0 content-start px-5 pt-6 pb-10 r48:px-9 r48:pt-10 r48:pb-12" id="tsb-15-main">
      <p class="m-0 mb-1 text-[0.82rem] text-tsb15-mut">Operations / Deployments</p>
      <h2 class="m-0 mb-4.5 font-tsb15-display text-[clamp(1.45rem,3.6vw,2rem)] leading-[1.1]">Rollback runbook</h2>
      <nav class="mb-5 px-3.5 py-3 max-w-[44rem] bg-tsb15-surf2" aria-label="On this page">
        <p class="m-0 mb-2 text-[0.7rem] tracking-[0.1em] uppercase text-tsb15-mut">On this page</p>
        <ul class="list-none m-0 p-0 flex flex-wrap gap-1.5">
          <li><a class="inline-flex items-center min-h-11 px-3.5 bg-tsb15-surf border border-tsb15-line text-[0.87rem] text-tsb15-ink no-underline hover:bg-tsb15-bg focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb15-acc aria-[current=page]:border-tsb15-acc aria-[current=page]:text-tsb15-onacc aria-[current=page]:font-semibold" href="#tsb-15-main" aria-current="page">Before you start</a></li>
          <li><a class="inline-flex items-center min-h-11 px-3.5 bg-tsb15-surf border border-tsb15-line text-[0.87rem] text-tsb15-ink no-underline hover:bg-tsb15-bg focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Pointer move</a></li>
          <li><a class="inline-flex items-center min-h-11 px-3.5 bg-tsb15-surf border border-tsb15-line text-[0.87rem] text-tsb15-ink no-underline hover:bg-tsb15-bg focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Verifying</a></li>
          <li><a class="inline-flex items-center min-h-11 px-3.5 bg-tsb15-surf border border-tsb15-line text-[0.87rem] text-tsb15-ink no-underline hover:bg-tsb15-bg focus-visible:outline-2 focus-visible:outline-tsb15-acc focus-visible:-outline-offset-2" href="#tsb-15-main">Post-mortem</a></li>
        </ul>
      </nav>
      <p class="m-0 mb-3 max-w-[40rem] text-[0.94rem] text-tsb15-mut text-pretty">Promotion is a pointer move, so a rollback is the same operation in reverse and completes in under a second. The slow part is verification &mdash; confirm the health checks on the previous build before you announce it.</p>
      <p class="m-0 mb-3 max-w-[40rem] text-[0.94rem] text-tsb15-mut text-pretty">Announce in the incident channel first, then update the status page. If the previous build is more than seven days old, check the migration log before promoting it.</p>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb15-bg: #f7f4ee;
  --color-tsb15-bg: oklch(96% 0.012 90);
  --color-tsb15-surf: #fffdf8;
  --color-tsb15-surf: oklch(99% 0.008 90);
  --color-tsb15-surf2: #efeade;
  --color-tsb15-surf2: oklch(93% 0.018 90);
  --color-tsb15-line: #ddd6c6;
  --color-tsb15-line: oklch(87% 0.024 90);
  --color-tsb15-ink: #201d16;
  --color-tsb15-ink: oklch(23% 0.014 80);
  --color-tsb15-mut: #6a6252;
  --color-tsb15-mut: oklch(47% 0.02 85);
  --color-tsb15-acc: #4c5f2a;
  --color-tsb15-acc: oklch(45% 0.1 122);
  --color-tsb15-accsoft: #e4ead2;
  --color-tsb15-accsoft: oklch(92% 0.03 122);
  --color-tsb15-onacc: #fffdf8;
  --color-tsb15-onacc: oklch(99% 0.008 90);
  --font-tsb15-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb15-display: 'Karla', Optima, Candara, 'Gill Sans', system-ui, sans-serif;
  --breakpoint-r48: 48rem;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. */

.tsb-15 {
  width: 100%;
  min-height: 100svh;
}

.tsb-15 *,
.tsb-15 *::before,
.tsb-15 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-15:has(.tsb-15-theme-input:checked) {
  --color-tsb15-bg: #14130f;
  --color-tsb15-surf: #1b1a14;
  --color-tsb15-surf2: #23211a;
  --color-tsb15-line: #332f25;
  --color-tsb15-ink: #f0ece1;
  --color-tsb15-mut: #a49b87;
  --color-tsb15-acc: #b6cf80;
  --color-tsb15-acc: oklch(82% 0.12 122);
  --color-tsb15-accsoft: #262d17;
  --color-tsb15-onacc: #1b1a14;
}

@media (prefers-color-scheme: dark) {
  .tsb-15 {
    --color-tsb15-bg: #14130f;
    --color-tsb15-surf: #1b1a14;
    --color-tsb15-surf2: #23211a;
    --color-tsb15-line: #332f25;
    --color-tsb15-ink: #f0ece1;
    --color-tsb15-mut: #a49b87;
    --color-tsb15-acc: #b6cf80;
    --color-tsb15-acc: oklch(82% 0.12 122);
    --color-tsb15-accsoft: #262d17;
    --color-tsb15-onacc: #1b1a14;
  }

  .tsb-15:has(.tsb-15-theme-input:checked) {
    --color-tsb15-bg: #f7f4ee;
    --color-tsb15-surf: #fffdf8;
    --color-tsb15-surf2: #efeade;
    --color-tsb15-line: #ddd6c6;
    --color-tsb15-ink: #201d16;
    --color-tsb15-mut: #6a6252;
    --color-tsb15-acc: #4c5f2a;
    --color-tsb15-acc: oklch(45% 0.1 122);
    --color-tsb15-accsoft: #e4ead2;
    --color-tsb15-onacc: #fffdf8;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-15:has(.tsb-15-theme-input:checked) {
    --color-tsb15-bg: #14130f;
    --color-tsb15-surf: #1b1a14;
    --color-tsb15-surf2: #23211a;
    --color-tsb15-line: #332f25;
    --color-tsb15-ink: #f0ece1;
    --color-tsb15-mut: #a49b87;
    --color-tsb15-acc: #b6cf80;
    --color-tsb15-acc: oklch(82% 0.12 122);
    --color-tsb15-accsoft: #262d17;
    --color-tsb15-onacc: #1b1a14;
  }
}
```
