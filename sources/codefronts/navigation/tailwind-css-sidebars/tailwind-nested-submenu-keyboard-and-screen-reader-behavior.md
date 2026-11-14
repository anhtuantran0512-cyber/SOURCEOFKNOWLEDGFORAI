---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-nested-submenu-keyboard-and-screen-reader-behavior/"
title: "Tailwind Nested Submenu Keyboard and Screen Reader Behavior"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "Two-level navigation done natively: each group is a <details>, so a collapsed submenu is genuinely removed from the tab order and the expanded state is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Nested Submenu Keyboard and Screen Reader Behavior
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-nested-submenu-keyboard-and-screen-reader-behavior/

Two-level navigation done natively: each group is a <details>, so a collapsed submenu is genuinely removed from the tab order and the expanded state is exposed by the browser. The port's real find is group-has-[a[aria-current=page]]: &mdash; a group that contains the current page marks itself, both with a dot and with a visually hidden phrase, entirely from the class list.
## HTML
```html
<section class="tsb-09 block relative w-full min-h-svh bg-tsb09-bg text-tsb09-ink font-tsb09-sans leading-[1.55]" aria-label="Fern CMS">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-09-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-09-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[0.5rem] border border-tsb09-line bg-tsb09-surf text-tsb09-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb09-acc peer-focus-visible:outline-offset-2" for="tsb-09-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] min-h-svh bg-tsb09-surf r46:grid-cols-[minmax(0,18.5rem)_minmax(0,1fr)]">
    <nav class="min-w-0 px-2.5 pt-4 pb-5 bg-tsb09-surf2 border-b border-tsb09-line r46:border-b-0 r46:border-r r46:border-tsb09-line" aria-label="Fern workspace">
      <p class="m-0 mb-3 px-2.5 text-[0.74rem] tracking-[0.08em] uppercase text-tsb09-mut">Fern &mdash; Meridian site</p>
      <ul class="list-none m-0 p-0">
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.92rem] text-tsb09-ink no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2" href="#tsb-09-main">Dashboard</a></li>
      </ul>

      <details class="group my-0.5" open>
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.92rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2">
          <svg class="w-4 h-4 flex-none text-tsb09-mut transition-transform duration-150 ease-out group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Content
          <span class="hidden group-has-[a[aria-current=page]]:block absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">contains the current page</span>
          <span class="hidden group-has-[a[aria-current=page]]:block flex-none ml-auto w-1.5 h-1.5 rounded-full bg-tsb09-acc" aria-hidden="true"></span>
        </summary>
        <ul class="list-none m-0 p-0">
          <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-8.5 rounded-[0.4rem] text-[0.89rem] text-tsb09-mut no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb09-accsoft aria-[current=page]:text-tsb09-acc aria-[current=page]:font-semibold" href="#tsb-09-main">Pages</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-8.5 rounded-[0.4rem] text-[0.89rem] text-tsb09-mut no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb09-accsoft aria-[current=page]:text-tsb09-acc aria-[current=page]:font-semibold" href="#tsb-09-main" aria-current="page">Articles</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-8.5 rounded-[0.4rem] text-[0.89rem] text-tsb09-mut no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb09-accsoft aria-[current=page]:text-tsb09-acc aria-[current=page]:font-semibold" href="#tsb-09-main">Media library</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-8.5 rounded-[0.4rem] text-[0.89rem] text-tsb09-mut no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb09-accsoft aria-[current=page]:text-tsb09-acc aria-[current=page]:font-semibold" href="#tsb-09-main">Redirects</a></li>
        </ul>
      </details>

      <details class="group my-0.5">
        <summary class="flex items-center gap-2 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.92rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2">
          <svg class="w-4 h-4 flex-none text-tsb09-mut transition-transform duration-150 ease-out group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Team settings
          <span class="hidden group-has-[a[aria-current=page]]:block absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">contains the current page</span>
          <span class="hidden group-has-[a[aria-current=page]]:block flex-none ml-auto w-1.5 h-1.5 rounded-full bg-tsb09-acc" aria-hidden="true"></span>
        </summary>
        <ul class="list-none m-0 p-0">
          <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-8.5 rounded-[0.4rem] text-[0.89rem] text-tsb09-mut no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2" href="#tsb-09-main">Members</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-8.5 rounded-[0.4rem] text-[0.89rem] text-tsb09-mut no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2" href="#tsb-09-main">Roles</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-8.5 rounded-[0.4rem] text-[0.89rem] text-tsb09-mut no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2" href="#tsb-09-main">Audit log</a></li>
        </ul>
      </details>

      <ul class="list-none m-0 p-0">
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.92rem] text-tsb09-ink no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2" href="#tsb-09-main">API keys</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.92rem] text-tsb09-ink no-underline hover:bg-tsb09-surf focus-visible:outline-2 focus-visible:outline-tsb09-acc focus-visible:-outline-offset-2" href="#tsb-09-main">Billing</a></li>
      </ul>
    </nav>

    <main class="min-w-0 content-start px-5 pt-6 pb-10 r46:px-9 r46:pt-10 r46:pb-12" id="tsb-09-main">
      <p class="m-0 mb-1 text-[0.78rem] text-tsb09-mut">Content / Articles</p>
      <h2 class="m-0 mb-5 font-tsb09-display text-[clamp(1.35rem,3.4vw,1.9rem)] leading-[1.15] tracking-[-0.015em]">Articles</h2>
      <table class="w-full max-w-[48rem] border-collapse text-[0.9rem]">
        <caption class="text-start pb-2 text-[0.74rem] tracking-[0.08em] uppercase text-tsb09-mut">Recently edited</caption>
        <thead><tr class="[&>th]:p-2.5 [&>th]:text-start [&>th]:border-b [&>th]:border-tsb09-line [&>th]:text-[0.74rem] [&>th]:tracking-[0.06em] [&>th]:uppercase [&>th]:font-semibold [&>th]:text-tsb09-mut"><th scope="col">Title</th><th scope="col">Editor</th><th scope="col">State</th></tr></thead>
        <tbody class="[&>tr>td]:p-2.5 [&>tr>td]:border-b [&>tr>td]:border-tsb09-line [&>tr>td]:min-w-0">
          <tr><td>Deployment regions</td><td>Alex Chen</td><td>Published</td></tr>
          <tr><td>Token rotation policy</td><td>Priya Sharma</td><td>In review</td></tr>
          <tr><td>Audit log retention</td><td>Sam Rivera</td><td>Draft</td></tr>
          <tr><td>Media naming rules</td><td>Ada Okafor</td><td>Published</td></tr>
        </tbody>
      </table>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb09-bg: #f4f7fc;
  --color-tsb09-bg: oklch(96.5% 0.01 258);
  --color-tsb09-surf: #ffffff;
  --color-tsb09-surf: oklch(100% 0 0);
  --color-tsb09-surf2: #eaf0f9;
  --color-tsb09-surf2: oklch(94% 0.015 258);
  --color-tsb09-line: #d2dcec;
  --color-tsb09-line: oklch(87% 0.02 258);
  --color-tsb09-ink: #101a2b;
  --color-tsb09-ink: oklch(19% 0.03 258);
  --color-tsb09-mut: #56658a;
  --color-tsb09-mut: oklch(47% 0.04 258);
  --color-tsb09-acc: #1554c8;
  --color-tsb09-acc: oklch(48% 0.17 258);
  --color-tsb09-accsoft: #dfe9fc;
  --color-tsb09-accsoft: oklch(93% 0.03 258);
  --font-tsb09-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb09-display: 'Manrope', 'Segoe UI', system-ui, sans-serif;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. */

.tsb-09 {
  width: 100%;
  min-height: 100svh;
}

.tsb-09 *,
.tsb-09 *::before,
.tsb-09 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-09:has(.tsb-09-theme-input:checked) {
  --color-tsb09-bg: #080d16;
  --color-tsb09-surf: #0f1725;
  --color-tsb09-surf2: #16202f;
  --color-tsb09-line: #24303f;
  --color-tsb09-ink: #e9eef8;
  --color-tsb09-mut: #92a1bd;
  --color-tsb09-acc: #7fa6ff;
  --color-tsb09-acc: oklch(78% 0.13 260);
  --color-tsb09-accsoft: #172441;
}

@media (prefers-color-scheme: dark) {
  .tsb-09 {
    --color-tsb09-bg: #080d16;
    --color-tsb09-surf: #0f1725;
    --color-tsb09-surf2: #16202f;
    --color-tsb09-line: #24303f;
    --color-tsb09-ink: #e9eef8;
    --color-tsb09-mut: #92a1bd;
    --color-tsb09-acc: #7fa6ff;
    --color-tsb09-acc: oklch(78% 0.13 260);
    --color-tsb09-accsoft: #172441;
  }

  .tsb-09:has(.tsb-09-theme-input:checked) {
    --color-tsb09-bg: #f4f7fc;
    --color-tsb09-surf: #ffffff;
    --color-tsb09-surf2: #eaf0f9;
    --color-tsb09-line: #d2dcec;
    --color-tsb09-ink: #101a2b;
    --color-tsb09-mut: #56658a;
    --color-tsb09-acc: #1554c8;
    --color-tsb09-acc: oklch(48% 0.17 258);
    --color-tsb09-accsoft: #dfe9fc;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-09:has(.tsb-09-theme-input:checked) {
    --color-tsb09-bg: #080d16;
    --color-tsb09-surf: #0f1725;
    --color-tsb09-surf2: #16202f;
    --color-tsb09-line: #24303f;
    --color-tsb09-ink: #e9eef8;
    --color-tsb09-mut: #92a1bd;
    --color-tsb09-acc: #7fa6ff;
    --color-tsb09-acc: oklch(78% 0.13 260);
    --color-tsb09-accsoft: #172441;
  }
}
```
