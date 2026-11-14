---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-dashboard-sidebar-with-current-page-state/"
title: "Tailwind Dashboard Sidebar with Current Page State"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "Where the user is has to be answered three times in an admin shell &mdash; in the rail, in the group that contains the page, and in the breadcrumb &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dashboard Sidebar with Current Page State
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-dashboard-sidebar-with-current-page-state/

Where the user is has to be answered three times in an admin shell &mdash; in the rail, in the group that contains the page, and in the breadcrumb &mdash; and all three have to agree. This build derives every one of them from aria-current="page" on a single link: the item marker through aria-[current=page]:, the group badge through group-has-[…]:, and the breadcrumb from the same word in the copy.
## HTML
```html
<section class="tsb-14 block relative w-full min-h-svh bg-tsb14-bg text-tsb14-ink font-tsb14-sans leading-[1.55]" aria-label="Meridian admin">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-14-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-14-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[0.35rem] border border-tsb14-line bg-tsb14-surf text-tsb14-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb14-acc peer-focus-visible:outline-offset-2" for="tsb-14-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] min-h-svh bg-tsb14-surf r46:grid-cols-[minmax(0,15rem)_minmax(0,1fr)]">
    <nav class="min-w-0 px-2 pt-4 pb-5 bg-tsb14-surf2 border-b border-tsb14-line r46:border-b-0 r46:border-r r46:border-tsb14-line" aria-label="Meridian admin">
      <p class="m-0 mb-3 px-2.5 font-tsb14-display text-[1.15rem]">Meridian</p>
      <ul class="list-none m-0 p-0">
        <li><a class="relative flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.91rem] text-tsb14-ink no-underline hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2" href="#tsb-14-main"><span class="flex-none text-[0.7rem] text-tsb14-mut" aria-hidden="true">&#9633;</span>Overview</a></li>
      </ul>

      <details class="group my-0.5" open>
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.91rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2">
          <span class="flex-none text-[0.7rem] text-tsb14-mut -rotate-90 transition-transform duration-150 ease-out group-open:rotate-0 motion-reduce:transition-none" aria-hidden="true">&#9660;</span>Infrastructure
          <span class="hidden group-has-[a[aria-current=page]]:block absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">contains the current page</span>
          <span class="hidden group-has-[a[aria-current=page]]:block flex-none ml-auto w-1.5 h-1.5 rounded-full bg-tsb14-acc" aria-hidden="true"></span>
        </summary>
        <ul class="list-none m-0 p-0">
          <li><a class="relative flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 rounded-[0.3rem] text-[0.88rem] text-tsb14-mut no-underline hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb14-accsoft aria-[current=page]:text-tsb14-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb14-acc)]" href="#tsb-14-main">Regions</a></li>
          <li><a class="relative flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 rounded-[0.3rem] text-[0.88rem] text-tsb14-mut no-underline hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb14-accsoft aria-[current=page]:text-tsb14-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb14-acc)]" href="#tsb-14-main" aria-current="page">Deployments</a></li>
          <li><a class="relative flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 rounded-[0.3rem] text-[0.88rem] text-tsb14-mut no-underline hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb14-accsoft aria-[current=page]:text-tsb14-acc aria-[current=page]:font-semibold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb14-acc)]" href="#tsb-14-main">Certificates</a></li>
        </ul>
      </details>

      <details class="group my-0.5">
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.91rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2">
          <span class="flex-none text-[0.7rem] text-tsb14-mut -rotate-90 transition-transform duration-150 ease-out group-open:rotate-0 motion-reduce:transition-none" aria-hidden="true">&#9660;</span>Access
          <span class="hidden group-has-[a[aria-current=page]]:block absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">contains the current page</span>
          <span class="hidden group-has-[a[aria-current=page]]:block flex-none ml-auto w-1.5 h-1.5 rounded-full bg-tsb14-acc" aria-hidden="true"></span>
        </summary>
        <ul class="list-none m-0 p-0">
          <li><a class="relative flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 rounded-[0.3rem] text-[0.88rem] text-tsb14-mut no-underline hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2" href="#tsb-14-main">Members</a></li>
          <li><a class="relative flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 rounded-[0.3rem] text-[0.88rem] text-tsb14-mut no-underline hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2" href="#tsb-14-main">API keys</a></li>
          <li><a class="relative flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-7.5 rounded-[0.3rem] text-[0.88rem] text-tsb14-mut no-underline hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2" href="#tsb-14-main">Audit log</a></li>
        </ul>
      </details>

      <ul class="list-none m-0 p-0">
        <li><a class="relative flex items-center gap-2 min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.91rem] text-tsb14-ink no-underline hover:bg-tsb14-surf3 focus-visible:outline-2 focus-visible:outline-tsb14-acc focus-visible:-outline-offset-2" href="#tsb-14-main"><span class="flex-none text-[0.7rem] text-tsb14-mut" aria-hidden="true">&#9633;</span>Billing</a></li>
      </ul>
    </nav>

    <main class="min-w-0 content-start px-5 pt-6 pb-10 r46:px-9 r46:pt-10 r46:pb-12" id="tsb-14-main">
      <p class="m-0 mb-1 text-[0.82rem] text-tsb14-mut">Infrastructure &rarr; <span class="font-semibold text-tsb14-acc">Deployments</span></p>
      <h2 class="m-0 mb-5 font-tsb14-display text-[clamp(1.45rem,3.6vw,2.1rem)] leading-[1.1]">Deployments</h2>
      <ul class="list-none m-0 p-0 grid gap-px max-w-[48rem] bg-tsb14-line border border-tsb14-line [&>li]:flex [&>li]:flex-wrap [&>li]:items-baseline [&>li]:gap-2.5 [&>li]:min-w-0 [&>li]:px-3.5 [&>li]:py-2.5 [&>li]:bg-tsb14-surf [&>li]:text-[0.88rem] [&>li>em]:ml-auto [&>li>em]:not-italic [&>li>em]:text-[0.8rem] [&>li>em]:text-tsb14-mut">
        <li><span class="font-tsb14-mono text-[0.82rem] text-tsb14-acc">4c19f2a</span><span>eu-west-1</span><em>Promoted 09:14 &middot; Alex Chen</em></li>
        <li><span class="font-tsb14-mono text-[0.82rem] text-tsb14-acc">9ab7d10</span><span>eu-west-1</span><em>Building &middot; Priya Sharma</em></li>
        <li><span class="font-tsb14-mono text-[0.82rem] text-tsb14-acc">17c40be</span><span>us-east-1</span><em>Rolled back &middot; Jordan Lee</em></li>
        <li><span class="font-tsb14-mono text-[0.82rem] text-tsb14-acc">08e5cc1</span><span>ap-south-1</span><em>Promoted 07:41 &middot; Ada Okafor</em></li>
        <li><span class="font-tsb14-mono text-[0.82rem] text-tsb14-acc">b7712fd</span><span>eu-west-1</span><em>Superseded &middot; Sam Rivera</em></li>
      </ul>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb14-bg: #f2f3f2;
  --color-tsb14-bg: oklch(95.5% 0.004 160);
  --color-tsb14-surf: #fbfbfa;
  --color-tsb14-surf: oklch(98.5% 0.003 160);
  --color-tsb14-surf2: #e7e9e7;
  --color-tsb14-surf2: oklch(92.5% 0.006 160);
  --color-tsb14-surf3: #dcdfdc;
  --color-tsb14-surf3: oklch(89% 0.008 160);
  --color-tsb14-line: #cdd1cd;
  --color-tsb14-line: oklch(84.5% 0.008 160);
  --color-tsb14-ink: #161a18;
  --color-tsb14-ink: oklch(21% 0.008 170);
  --color-tsb14-mut: #5c625f;
  --color-tsb14-mut: oklch(47% 0.01 170);
  --color-tsb14-acc: #0d6b62;
  --color-tsb14-acc: oklch(46% 0.09 190);
  --color-tsb14-accsoft: #d5e8e5;
  --color-tsb14-accsoft: oklch(91% 0.025 190);
  --font-tsb14-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb14-display: 'Lora', 'Iowan Old Style', Palatino, Georgia, serif;
  --font-tsb14-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. */

.tsb-14 {
  width: 100%;
  min-height: 100svh;
}

.tsb-14 *,
.tsb-14 *::before,
.tsb-14 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-14:has(.tsb-14-theme-input:checked) {
  --color-tsb14-bg: #0c100e;
  --color-tsb14-surf: #141917;
  --color-tsb14-surf2: #1b211f;
  --color-tsb14-surf3: #232b28;
  --color-tsb14-line: #2b3532;
  --color-tsb14-ink: #e9efec;
  --color-tsb14-mut: #94a09c;
  --color-tsb14-acc: #6fd2c6;
  --color-tsb14-acc: oklch(82% 0.1 190);
  --color-tsb14-accsoft: #14302c;
}

@media (prefers-color-scheme: dark) {
  .tsb-14 {
    --color-tsb14-bg: #0c100e;
    --color-tsb14-surf: #141917;
    --color-tsb14-surf2: #1b211f;
    --color-tsb14-surf3: #232b28;
    --color-tsb14-line: #2b3532;
    --color-tsb14-ink: #e9efec;
    --color-tsb14-mut: #94a09c;
    --color-tsb14-acc: #6fd2c6;
    --color-tsb14-acc: oklch(82% 0.1 190);
    --color-tsb14-accsoft: #14302c;
  }

  .tsb-14:has(.tsb-14-theme-input:checked) {
    --color-tsb14-bg: #f2f3f2;
    --color-tsb14-surf: #fbfbfa;
    --color-tsb14-surf2: #e7e9e7;
    --color-tsb14-surf3: #dcdfdc;
    --color-tsb14-line: #cdd1cd;
    --color-tsb14-ink: #161a18;
    --color-tsb14-mut: #5c625f;
    --color-tsb14-acc: #0d6b62;
    --color-tsb14-acc: oklch(46% 0.09 190);
    --color-tsb14-accsoft: #d5e8e5;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-14:has(.tsb-14-theme-input:checked) {
    --color-tsb14-bg: #0c100e;
    --color-tsb14-surf: #141917;
    --color-tsb14-surf2: #1b211f;
    --color-tsb14-surf3: #232b28;
    --color-tsb14-line: #2b3532;
    --color-tsb14-ink: #e9efec;
    --color-tsb14-mut: #94a09c;
    --color-tsb14-acc: #6fd2c6;
    --color-tsb14-acc: oklch(82% 0.1 190);
    --color-tsb14-accsoft: #14302c;
  }
}
```
