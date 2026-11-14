---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-collapsible-sidebar-with-checkbox-state/"
title: "Pure Tailwind Collapsible Sidebar with Checkbox State"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "The zero-JS collapse."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Collapsible Sidebar with Checkbox State
Source: https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-collapsible-sidebar-with-checkbox-state/

The zero-JS collapse. A visually hidden checkbox holds the state, a <label> is the control, and every responding element reads the state through group-has-checked: &mdash; which is precisely what the :has() era gave utility CSS. Compare demo 05, the scripted version: same product, and the honest trade is that a checkbox cannot carry aria-expanded.
## HTML
```html
<section class="tsb-11 block relative w-full min-h-svh bg-tsb11-bg text-tsb11-ink font-tsb11-sans leading-[1.55]" aria-label="Vale account settings">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-11-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-11-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[1.4rem] border-0 bg-tsb11-surf2 text-tsb11-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb11-acc peer-focus-visible:outline-offset-2" for="tsb-11-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="group flex min-w-0 min-h-svh bg-tsb11-surf max-r30:flex-col">
    <input class="absolute w-px h-px m-0 overflow-hidden whitespace-nowrap [clip-path:inset(50%)]" type="checkbox" id="tsb-11-collapse">
    <aside class="flex-none flex flex-col min-w-0 w-[var(--tsb11-w-open)] bg-tsb11-surf2 transition-[width] duration-200 ease-out group-has-checked:w-[var(--tsb11-w-rail)] motion-reduce:transition-none max-r30:w-full max-r30:group-has-checked:w-full">
      <div class="p-2.5 pr-14 r30:pr-2.5">
        <label class="flex items-center gap-2.5 min-w-11 min-h-11 px-2.5 rounded-[1.4rem] bg-tsb11-surf text-[0.86rem] font-semibold whitespace-nowrap cursor-pointer [&>svg]:w-4.5 [&>svg]:h-4.5 [&>svg]:flex-none group-has-checked:justify-center group-has-checked:px-0 group-has-[input:focus-visible]:outline-2 group-has-[input:focus-visible]:outline-tsb11-acc group-has-[input:focus-visible]:outline-offset-2" for="tsb-11-collapse">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="group-has-checked:absolute group-has-checked:w-px group-has-checked:h-px group-has-checked:overflow-hidden group-has-checked:whitespace-nowrap group-has-checked:[clip-path:inset(50%)]">Collapse</span>
          <span class="hidden group-has-checked:block group-has-checked:absolute group-has-checked:w-px group-has-checked:h-px group-has-checked:overflow-hidden group-has-checked:whitespace-nowrap group-has-checked:[clip-path:inset(50%)]">Expand</span>
        </label>
      </div>
      <nav class="flex-1 min-h-0 px-2.5 py-1" aria-label="Vale account settings">
        <ul class="list-none m-0 p-0 grid gap-0.5">
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.92rem] text-tsb11-ink no-underline whitespace-nowrap hover:bg-tsb11-surf focus-visible:outline-2 focus-visible:outline-tsb11-acc focus-visible:outline-offset-2 aria-[current=page]:bg-tsb11-acc aria-[current=page]:text-tsb11-onacc aria-[current=page]:font-semibold aria-[current=page]:[&>span:first-child]:text-current group-has-checked:justify-center group-has-checked:gap-0" href="#tsb-11-main" aria-current="page"><span class="flex-none text-[0.6rem] text-tsb11-mut" aria-hidden="true">&#9679;</span><span class="min-w-0 overflow-hidden text-ellipsis group-has-checked:absolute group-has-checked:w-px group-has-checked:h-px group-has-checked:whitespace-nowrap group-has-checked:[clip-path:inset(50%)]">Profile</span></a></li>
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.92rem] text-tsb11-ink no-underline whitespace-nowrap hover:bg-tsb11-surf focus-visible:outline-2 focus-visible:outline-tsb11-acc focus-visible:outline-offset-2 group-has-checked:justify-center group-has-checked:gap-0" href="#tsb-11-main"><span class="flex-none text-[0.6rem] text-tsb11-mut" aria-hidden="true">&#9679;</span><span class="min-w-0 overflow-hidden text-ellipsis group-has-checked:absolute group-has-checked:w-px group-has-checked:h-px group-has-checked:whitespace-nowrap group-has-checked:[clip-path:inset(50%)]">Notifications</span></a></li>
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.92rem] text-tsb11-ink no-underline whitespace-nowrap hover:bg-tsb11-surf focus-visible:outline-2 focus-visible:outline-tsb11-acc focus-visible:outline-offset-2 group-has-checked:justify-center group-has-checked:gap-0" href="#tsb-11-main"><span class="flex-none text-[0.6rem] text-tsb11-mut" aria-hidden="true">&#9679;</span><span class="min-w-0 overflow-hidden text-ellipsis group-has-checked:absolute group-has-checked:w-px group-has-checked:h-px group-has-checked:whitespace-nowrap group-has-checked:[clip-path:inset(50%)]">Security</span></a></li>
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.92rem] text-tsb11-ink no-underline whitespace-nowrap hover:bg-tsb11-surf focus-visible:outline-2 focus-visible:outline-tsb11-acc focus-visible:outline-offset-2 group-has-checked:justify-center group-has-checked:gap-0" href="#tsb-11-main"><span class="flex-none text-[0.6rem] text-tsb11-mut" aria-hidden="true">&#9679;</span><span class="min-w-0 overflow-hidden text-ellipsis group-has-checked:absolute group-has-checked:w-px group-has-checked:h-px group-has-checked:whitespace-nowrap group-has-checked:[clip-path:inset(50%)]">Billing</span></a></li>
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.92rem] text-tsb11-ink no-underline whitespace-nowrap hover:bg-tsb11-surf focus-visible:outline-2 focus-visible:outline-tsb11-acc focus-visible:outline-offset-2 group-has-checked:justify-center group-has-checked:gap-0" href="#tsb-11-main"><span class="flex-none text-[0.6rem] text-tsb11-mut" aria-hidden="true">&#9679;</span><span class="min-w-0 overflow-hidden text-ellipsis group-has-checked:absolute group-has-checked:w-px group-has-checked:h-px group-has-checked:whitespace-nowrap group-has-checked:[clip-path:inset(50%)]">API keys</span></a></li>
        </ul>
      </nav>
      <p class="m-0 px-4 pt-2.5 pb-3.5 overflow-hidden whitespace-nowrap text-[0.78rem] text-tsb11-mut"><span class="min-w-0 overflow-hidden text-ellipsis group-has-checked:absolute group-has-checked:w-px group-has-checked:h-px group-has-checked:whitespace-nowrap group-has-checked:[clip-path:inset(50%)]">Signed in as Priya Sharma</span></p>
    </aside>

    <main class="flex-1 min-w-0 px-5 pt-6 pb-10 r46:px-9 r46:pt-10 r46:pb-12" id="tsb-11-main">
      <h2 class="m-0 mb-5 font-tsb11-display text-[clamp(1.35rem,3.4vw,1.9rem)] leading-[1.15]">Profile</h2>
      <dl class="m-0 grid grid-cols-[minmax(0,1fr)] gap-2.5 max-w-[44rem] r34:grid-cols-2 [&>div]:min-w-0 [&>div]:px-3.5 [&>div]:py-3 [&>div]:rounded-[0.9rem] [&>div]:bg-tsb11-surf2 [&_dt]:text-[0.72rem] [&_dt]:tracking-[0.08em] [&_dt]:uppercase [&_dt]:text-tsb11-mut [&_dd]:mt-0.5 [&_dd]:ml-0 [&_dd]:text-[0.92rem]">
        <div><dt>Display name</dt><dd>Priya Sharma</dd></div>
        <div><dt>Workspace</dt><dd>Vale &middot; Operations</dd></div>
        <div><dt>Time zone</dt><dd>Europe/Lisbon (UTC+1)</dd></div>
        <div><dt>Two-factor</dt><dd>Authenticator app</dd></div>
        <div><dt>Recovery email</dt><dd>[email protected]</dd></div>
        <div><dt>Member since</dt><dd>March 2024</dd></div>
      </dl>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb11-bg: #f5f1ee;
  --color-tsb11-bg: oklch(95.5% 0.008 45);
  --color-tsb11-surf: #fffcfa;
  --color-tsb11-surf: oklch(99% 0.004 45);
  --color-tsb11-surf2: #ebe3dd;
  --color-tsb11-surf2: oklch(92% 0.014 45);
  --color-tsb11-line: #d9cdc4;
  --color-tsb11-line: oklch(85% 0.02 45);
  --color-tsb11-ink: #241c17;
  --color-tsb11-ink: oklch(24% 0.018 45);
  --color-tsb11-mut: #6d5c52;
  --color-tsb11-mut: oklch(48% 0.025 45);
  --color-tsb11-acc: #7d4a35;
  --color-tsb11-acc: oklch(46% 0.09 40);
  --color-tsb11-accsoft: #eee0d8;
  --color-tsb11-accsoft: oklch(92% 0.02 45);
  --color-tsb11-onacc: #fffcfa;
  --color-tsb11-onacc: oklch(99% 0.004 45);
  --font-tsb11-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb11-display: 'Quicksand', Nunito, ui-rounded, system-ui, sans-serif;
  --breakpoint-r30: 30rem;
  --breakpoint-r34: 34rem;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract plus the two rail widths. */

.tsb-11 {
  width: 100%;
  min-height: 100svh;
  --tsb11-w-open: 15rem;
  --tsb11-w-rail: 4.5rem;
}

.tsb-11 *,
.tsb-11 *::before,
.tsb-11 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks.
   Note this is a SECOND checkbox in the demo, independent of the collapse one — which is
   why the collapse group is scoped to the app shell, not to the section root. */

.tsb-11:has(.tsb-11-theme-input:checked) {
  --color-tsb11-bg: #14100e;
  --color-tsb11-surf: #1c1714;
  --color-tsb11-surf2: #251e1a;
  --color-tsb11-line: #362c26;
  --color-tsb11-ink: #f1e9e3;
  --color-tsb11-mut: #a89689;
  --color-tsb11-acc: #dda183;
  --color-tsb11-acc: oklch(78% 0.09 45);
  --color-tsb11-accsoft: #32241d;
  --color-tsb11-onacc: #1c1714;
}

@media (prefers-color-scheme: dark) {
  .tsb-11 {
    --color-tsb11-bg: #14100e;
    --color-tsb11-surf: #1c1714;
    --color-tsb11-surf2: #251e1a;
    --color-tsb11-line: #362c26;
    --color-tsb11-ink: #f1e9e3;
    --color-tsb11-mut: #a89689;
    --color-tsb11-acc: #dda183;
    --color-tsb11-acc: oklch(78% 0.09 45);
    --color-tsb11-accsoft: #32241d;
    --color-tsb11-onacc: #1c1714;
  }

  .tsb-11:has(.tsb-11-theme-input:checked) {
    --color-tsb11-bg: #f5f1ee;
    --color-tsb11-surf: #fffcfa;
    --color-tsb11-surf2: #ebe3dd;
    --color-tsb11-line: #d9cdc4;
    --color-tsb11-ink: #241c17;
    --color-tsb11-mut: #6d5c52;
    --color-tsb11-acc: #7d4a35;
    --color-tsb11-acc: oklch(46% 0.09 40);
    --color-tsb11-accsoft: #eee0d8;
    --color-tsb11-onacc: #fffcfa;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-11:has(.tsb-11-theme-input:checked) {
    --color-tsb11-bg: #14100e;
    --color-tsb11-surf: #1c1714;
    --color-tsb11-surf2: #251e1a;
    --color-tsb11-line: #362c26;
    --color-tsb11-ink: #f1e9e3;
    --color-tsb11-mut: #a89689;
    --color-tsb11-acc: #dda183;
    --color-tsb11-acc: oklch(78% 0.09 45);
    --color-tsb11-accsoft: #32241d;
    --color-tsb11-onacc: #1c1714;
  }
}
```
