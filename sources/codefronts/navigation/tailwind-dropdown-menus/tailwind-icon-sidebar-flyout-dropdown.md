---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-icon-sidebar-flyout-dropdown/"
title: "Tailwind Icon Sidebar Flyout Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "The collapsed-sidebar pattern: a 60px icon rail where each icon reveals a labelled flyout to its right."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon Sidebar Flyout Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-icon-sidebar-flyout-dropdown/

The collapsed-sidebar pattern: a 60px icon rail where each icon reveals a labelled flyout to its right. The port is mostly positional, and the one thing worth stating out loud is that the rail must not clip — overflow-visible is load-bearing, and in utilities it sits right next to the width that makes it necessary.
## HTML
```html
<section class="tdd-12 w-full min-h-svh grid place-items-center bg-linear-[135deg,var(--color-tdd12-bg1),var(--color-tdd12-bg2)] font-tdd12-sans text-tdd12-ink px-5 py-10" aria-label="Icon sidebar flyout dropdown demo">
  <div class="flex h-75 w-[min(560px,100%)] overflow-visible rounded-2xl border border-tdd12-edge bg-white shadow-[0_8px_32px_oklch(0.5_0.2_300/0.12)]">
    <aside class="relative z-10 flex w-15 shrink-0 flex-col items-center gap-1 overflow-visible rounded-l-2xl border-r border-tdd12-edge bg-tdd12-rail py-3.5" aria-label="Sidebar">
      <div class="mb-4 text-lg font-bold text-tdd12-acc" aria-hidden="true">&#9670;</div>
      <div class="group relative flex w-full justify-center after:absolute after:inset-y-0 after:left-full after:w-2 after:content-['']">
        <a href="#dashboard" aria-label="Dashboard" class="flex size-10 items-center justify-center rounded-[10px] text-lg transition-colors duration-150 group-hover:bg-tdd12-tint focus-visible:bg-tdd12-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd12-acc">&#127968;</a>
        <div class="pointer-events-none absolute -top-1 left-[calc(100%+8px)] z-20 flex min-w-42 -translate-x-2 flex-col gap-0.5 rounded-xl border border-tdd12-edge bg-white p-3 opacity-0 shadow-[0_8px_28px_oklch(0.5_0.2_300/0.15)] transition-[opacity,translate] duration-250 ease-tdd12 group-hover:pointer-events-auto group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-x-0 group-focus-within:opacity-100 motion-reduce:duration-150">
          <p class="px-1 pb-1 text-[11px] font-semibold uppercase tracking-[0.08em] text-tdd12-acc">Dashboard</p>
          <div class="my-1 h-px bg-tdd12-edge" aria-hidden="true"></div>
          <a href="#overview" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Overview</a>
          <a href="#analytics" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Analytics</a>
          <a href="#reports" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Reports</a>
        </div>
      </div>
      <div class="group relative flex w-full justify-center after:absolute after:inset-y-0 after:left-full after:w-2 after:content-['']">
        <a href="#projects" aria-label="Projects" class="flex size-10 items-center justify-center rounded-[10px] text-lg transition-colors duration-150 group-hover:bg-tdd12-tint focus-visible:bg-tdd12-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd12-acc">&#128203;</a>
        <div class="pointer-events-none absolute -top-1 left-[calc(100%+8px)] z-20 flex min-w-42 -translate-x-2 flex-col gap-0.5 rounded-xl border border-tdd12-edge bg-white p-3 opacity-0 shadow-[0_8px_28px_oklch(0.5_0.2_300/0.15)] transition-[opacity,translate] duration-250 ease-tdd12 group-hover:pointer-events-auto group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-x-0 group-focus-within:opacity-100 motion-reduce:duration-150">
          <p class="px-1 pb-1 text-[11px] font-semibold uppercase tracking-[0.08em] text-tdd12-acc">Projects</p>
          <div class="my-1 h-px bg-tdd12-edge" aria-hidden="true"></div>
          <a href="#all" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">All Projects</a>
          <a href="#active" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Active</a>
          <a href="#archived" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Archived</a>
        </div>
      </div>
      <div class="group relative flex w-full justify-center after:absolute after:inset-y-0 after:left-full after:w-2 after:content-['']">
        <a href="#messages" aria-label="Messages" class="flex size-10 items-center justify-center rounded-[10px] text-lg transition-colors duration-150 group-hover:bg-tdd12-tint focus-visible:bg-tdd12-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd12-acc">&#128172;</a>
        <div class="pointer-events-none absolute -top-1 left-[calc(100%+8px)] z-20 flex min-w-42 -translate-x-2 flex-col gap-0.5 rounded-xl border border-tdd12-edge bg-white p-3 opacity-0 shadow-[0_8px_28px_oklch(0.5_0.2_300/0.15)] transition-[opacity,translate] duration-250 ease-tdd12 group-hover:pointer-events-auto group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-x-0 group-focus-within:opacity-100 motion-reduce:duration-150">
          <p class="px-1 pb-1 text-[11px] font-semibold uppercase tracking-[0.08em] text-tdd12-acc">Messages</p>
          <div class="my-1 h-px bg-tdd12-edge" aria-hidden="true"></div>
          <a href="#inbox" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Inbox</a>
          <a href="#sent" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Sent</a>
          <a href="#drafts" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Drafts</a>
        </div>
      </div>
      <div class="group relative flex w-full justify-center after:absolute after:inset-y-0 after:left-full after:w-2 after:content-['']">
        <a href="#settings" aria-label="Settings" class="flex size-10 items-center justify-center rounded-[10px] text-lg transition-colors duration-150 group-hover:bg-tdd12-tint focus-visible:bg-tdd12-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd12-acc">&#9881;</a>
        <div class="pointer-events-none absolute -top-1 left-[calc(100%+8px)] z-20 flex min-w-42 -translate-x-2 flex-col gap-0.5 rounded-xl border border-tdd12-edge bg-white p-3 opacity-0 shadow-[0_8px_28px_oklch(0.5_0.2_300/0.15)] transition-[opacity,translate] duration-250 ease-tdd12 group-hover:pointer-events-auto group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-x-0 group-focus-within:opacity-100 motion-reduce:duration-150">
          <p class="px-1 pb-1 text-[11px] font-semibold uppercase tracking-[0.08em] text-tdd12-acc">Settings</p>
          <div class="my-1 h-px bg-tdd12-edge" aria-hidden="true"></div>
          <a href="#profile" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Profile</a>
          <a href="#security" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Security</a>
          <a href="#billing" class="block rounded-[7px] px-2.5 py-1.5 text-[13px] font-medium text-tdd12-ink no-underline transition-colors duration-150 hover:bg-tdd12-tint hover:text-tdd12-acc focus-visible:bg-tdd12-tint focus-visible:outline-none">Billing</a>
        </div>
      </div>
    </aside>
    <main class="flex flex-1 items-center justify-center">
      <p class="text-[13px] italic text-tdd12-mut">Hover or tab the icons &#8592;</p>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd12-bg1: #f5f3ff;
  --color-tdd12-bg1: oklch(0.97 0.02 295);
  --color-tdd12-bg2: #ede9fe;
  --color-tdd12-bg2: oklch(0.94 0.03 295);
  --color-tdd12-ink: #1e1b4b;
  --color-tdd12-ink: oklch(0.26 0.08 285);
  --color-tdd12-mut: #6b7280;
  --color-tdd12-mut: oklch(0.55 0.02 265);
  --color-tdd12-edge: #ede9fe;
  --color-tdd12-edge: oklch(0.94 0.03 295);
  --color-tdd12-rail: #fafafa;
  --color-tdd12-rail: oklch(0.98 0 0);
  --color-tdd12-tint: #f5f3ff;
  --color-tdd12-tint: oklch(0.97 0.02 295);
  --color-tdd12-acc: #7c3aed;
  --color-tdd12-acc: oklch(0.54 0.24 295);
  --font-tdd12-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --ease-tdd12: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-12 {
  width: 100%;
  min-height: 100svh;
}

.tdd-12 ::selection {
  background: var(--color-tdd12-acc);
  color: #ede9fe;
}
```
