---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-accordion-sidebar-with-details-and-summary/"
title: "Pure Tailwind Accordion Sidebar with Details and Summary"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "One group open at a time, with no script and no state variable: the name attribute on <details> makes the browser enforce exclusivity, exactly like radio…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Accordion Sidebar with Details and Summary
Source: https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-accordion-sidebar-with-details-and-summary/

One group open at a time, with no script and no state variable: the name attribute on <details> makes the browser enforce exclusivity, exactly like radio buttons. The port keeps every visual decision in utilities &mdash; chevron rotation through group-open:, the containing-group highlight through group-has-[…] &mdash; and the stylesheet holds nothing but tokens.
## HTML
```html
<section class="tsb-16 block relative w-full min-h-svh bg-tsb16-bg text-tsb16-ink font-tsb16-sans leading-[1.55]" aria-label="Quill mail">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-16-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-16-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[0.6rem] border border-tsb16-line bg-tsb16-surf text-tsb16-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb16-acc peer-focus-visible:outline-offset-2" for="tsb-16-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] min-h-svh bg-tsb16-bg r46:grid-cols-[minmax(0,16.5rem)_minmax(0,1fr)]">
    <nav class="min-w-0 content-start px-2.5 py-3 bg-tsb16-surf2 r46:border-r r46:border-tsb16-line" aria-label="Quill mailboxes">
      <div class="px-2.5 pt-2 pb-3">
        <p class="m-0 font-tsb16-display text-[1.2rem] font-bold tracking-[-0.02em] text-tsb16-acc">Quill</p>
        <p class="m-0 text-[0.78rem] text-tsb16-mut">Sam Rivera</p>
      </div>

      <details class="group mb-1.5 rounded-[0.6rem] overflow-hidden bg-tsb16-surf" name="tsb-16-accordion" open>
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 text-[0.92rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden group-has-[a[aria-current=page]]:text-tsb16-acc hover:bg-tsb16-surf3 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2">
          <svg class="w-4 h-4 flex-none text-tsb16-mut transition-transform duration-150 ease-out group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Mail
        </summary>
        <ul class="list-none m-0 px-1.5 pt-0 pb-1.5">
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb16-accsoft aria-[current=page]:text-tsb16-acc aria-[current=page]:font-semibold aria-[current=page]:[&>span]:text-tsb16-acc" href="#tsb-16-main" aria-current="page">Inbox <span class="ml-auto text-[0.74rem] tabular-nums text-tsb16-mut">12 unread</span></a></li>
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Starred</a></li>
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Sent</a></li>
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Drafts <span class="ml-auto text-[0.74rem] tabular-nums text-tsb16-mut">3</span></a></li>
        </ul>
      </details>

      <details class="group mb-1.5 rounded-[0.6rem] overflow-hidden bg-tsb16-surf" name="tsb-16-accordion">
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 text-[0.92rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden group-has-[a[aria-current=page]]:text-tsb16-acc hover:bg-tsb16-surf3 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2">
          <svg class="w-4 h-4 flex-none text-tsb16-mut transition-transform duration-150 ease-out group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Shared inboxes
        </summary>
        <ul class="list-none m-0 px-1.5 pt-0 pb-1.5">
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Support <span class="ml-auto text-[0.74rem] tabular-nums text-tsb16-mut">41 unread</span></a></li>
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Billing</a></li>
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Security reports</a></li>
        </ul>
      </details>

      <details class="group mb-1.5 rounded-[0.6rem] overflow-hidden bg-tsb16-surf" name="tsb-16-accordion">
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 text-[0.92rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden group-has-[a[aria-current=page]]:text-tsb16-acc hover:bg-tsb16-surf3 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2">
          <svg class="w-4 h-4 flex-none text-tsb16-mut transition-transform duration-150 ease-out group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Settings
        </summary>
        <ul class="list-none m-0 px-1.5 pt-0 pb-1.5">
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Filters</a></li>
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Signatures</a></li>
          <li><a class="flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.45rem] text-[0.89rem] text-tsb16-ink no-underline hover:bg-tsb16-surf2 focus-visible:outline-2 focus-visible:outline-tsb16-acc focus-visible:-outline-offset-2" href="#tsb-16-main">Forwarding</a></li>
        </ul>
      </details>
    </nav>

    <main class="min-w-0 content-start px-5 pt-5.5 pb-10 bg-tsb16-surf r46:px-8 r46:pt-9 r46:pb-12" id="tsb-16-main">
      <h2 class="m-0 mb-4 text-[clamp(1.3rem,3.2vw,1.7rem)] tracking-[-0.015em]">Inbox</h2>
      <ul class="list-none m-0 p-0 grid gap-2 max-w-[46rem] [&>li]:min-w-0 [&>li]:px-3.5 [&>li]:py-3 [&>li]:rounded-[0.6rem] [&>li]:bg-tsb16-surf2">
        <li><p class="m-0 text-[0.78rem] font-semibold text-tsb16-acc">Priya Sharma</p><p class="my-0.5 text-[0.94rem] font-semibold min-w-0">Rollback runbook &mdash; review before Thursday</p><p class="m-0 overflow-hidden text-ellipsis whitespace-nowrap text-[0.82rem] text-tsb16-mut">I have added the verification step we discussed&hellip;</p></li>
        <li><p class="m-0 text-[0.78rem] font-semibold text-tsb16-acc">Vale Operations</p><p class="my-0.5 text-[0.94rem] font-semibold min-w-0">Access request: audit log export</p><p class="m-0 overflow-hidden text-ellipsis whitespace-nowrap text-[0.82rem] text-tsb16-mut">Jordan needs read access for the quarter&hellip;</p></li>
        <li><p class="m-0 text-[0.78rem] font-semibold text-tsb16-acc">Basalt Hosting</p><p class="my-0.5 text-[0.94rem] font-semibold min-w-0">Certificate renewal completed</p><p class="m-0 overflow-hidden text-ellipsis whitespace-nowrap text-[0.82rem] text-tsb16-mut">No action needed. The new certificate&hellip;</p></li>
        <li><p class="m-0 text-[0.78rem] font-semibold text-tsb16-acc">Ada Okafor</p><p class="my-0.5 text-[0.94rem] font-semibold min-w-0">Region failover drill, Friday 14:00</p><p class="m-0 overflow-hidden text-ellipsis whitespace-nowrap text-[0.82rem] text-tsb16-mut">Adding you as the observer for eu-west&hellip;</p></li>
        <li><p class="m-0 text-[0.78rem] font-semibold text-tsb16-acc">Fern Studio</p><p class="my-0.5 text-[0.94rem] font-semibold min-w-0">Invoice 4471 attached</p><p class="m-0 overflow-hidden text-ellipsis whitespace-nowrap text-[0.82rem] text-tsb16-mut">Net 30, payable on the usual account&hellip;</p></li>
      </ul>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb16-bg: #f1f3f5;
  --color-tsb16-bg: oklch(95.5% 0.004 250);
  --color-tsb16-surf: #ffffff;
  --color-tsb16-surf: oklch(100% 0 0);
  --color-tsb16-surf2: #e7eaee;
  --color-tsb16-surf2: oklch(92.5% 0.008 250);
  --color-tsb16-surf3: #dde1e7;
  --color-tsb16-surf3: oklch(89% 0.01 250);
  --color-tsb16-line: #cfd5dc;
  --color-tsb16-line: oklch(85.5% 0.012 250);
  --color-tsb16-ink: #131720;
  --color-tsb16-ink: oklch(19% 0.02 260);
  --color-tsb16-mut: #59616e;
  --color-tsb16-mut: oklch(47% 0.02 260);
  --color-tsb16-acc: #2b4a8f;
  --color-tsb16-acc: oklch(42% 0.13 264);
  --color-tsb16-accsoft: #e0e7f6;
  --color-tsb16-accsoft: oklch(93% 0.025 264);
  --font-tsb16-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb16-display: 'Figtree', system-ui, 'Segoe UI', sans-serif;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. */

.tsb-16 {
  width: 100%;
  min-height: 100svh;
}

.tsb-16 *,
.tsb-16 *::before,
.tsb-16 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-16:has(.tsb-16-theme-input:checked) {
  --color-tsb16-bg: #0b0e14;
  --color-tsb16-surf: #12161f;
  --color-tsb16-surf2: #191e29;
  --color-tsb16-surf3: #202634;
  --color-tsb16-line: #262d3b;
  --color-tsb16-ink: #e8ecf3;
  --color-tsb16-mut: #909aab;
  --color-tsb16-acc: #8fabf0;
  --color-tsb16-acc: oklch(78% 0.11 264);
  --color-tsb16-accsoft: #1a2238;
}

@media (prefers-color-scheme: dark) {
  .tsb-16 {
    --color-tsb16-bg: #0b0e14;
    --color-tsb16-surf: #12161f;
    --color-tsb16-surf2: #191e29;
    --color-tsb16-surf3: #202634;
    --color-tsb16-line: #262d3b;
    --color-tsb16-ink: #e8ecf3;
    --color-tsb16-mut: #909aab;
    --color-tsb16-acc: #8fabf0;
    --color-tsb16-acc: oklch(78% 0.11 264);
    --color-tsb16-accsoft: #1a2238;
  }

  .tsb-16:has(.tsb-16-theme-input:checked) {
    --color-tsb16-bg: #f1f3f5;
    --color-tsb16-surf: #ffffff;
    --color-tsb16-surf2: #e7eaee;
    --color-tsb16-surf3: #dde1e7;
    --color-tsb16-line: #cfd5dc;
    --color-tsb16-ink: #131720;
    --color-tsb16-mut: #59616e;
    --color-tsb16-acc: #2b4a8f;
    --color-tsb16-acc: oklch(42% 0.13 264);
    --color-tsb16-accsoft: #e0e7f6;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-16:has(.tsb-16-theme-input:checked) {
    --color-tsb16-bg: #0b0e14;
    --color-tsb16-surf: #12161f;
    --color-tsb16-surf2: #191e29;
    --color-tsb16-surf3: #202634;
    --color-tsb16-line: #262d3b;
    --color-tsb16-ink: #e8ecf3;
    --color-tsb16-mut: #909aab;
    --color-tsb16-acc: #8fabf0;
    --color-tsb16-acc: oklch(78% 0.11 264);
    --color-tsb16-accsoft: #1a2238;
  }
}
```
