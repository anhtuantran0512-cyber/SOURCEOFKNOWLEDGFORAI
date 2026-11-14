---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-multi-level-accordion-sidebar-menu/"
title: "Tailwind CSS Multi-Level Accordion Sidebar Menu"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A documentation-site sidebar with nested, animated sections."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Multi-Level Accordion Sidebar Menu
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-multi-level-accordion-sidebar-menu/

A documentation-site sidebar with nested, animated sections. The checkbox hack is gone: every section is a native <details>, so it announces expanded/collapsed, works with Enter and Space, and opens for find-in-page. Height animates to auto through ::details-content with interpolate-size; chevrons turn with group-open/l1:. Zero JavaScript.
## HTML
```html
<div class="tnv-12 flex min-h-svh w-full flex-col bg-tnv12-bg font-tnv12-sans text-tnv12-ink antialiased selection:bg-tnv12-acc selection:text-white md:flex-row">
  <aside class="flex w-full flex-none flex-col border-b border-tnv12-line bg-white md:sticky md:top-0 md:h-svh md:w-[17rem] md:border-r md:border-b-0">
    <div class="flex items-center gap-2.5 border-b border-tnv12-line px-4 py-4">
      <span class="grid size-8 place-items-center rounded-lg bg-tnv12-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" aria-hidden="true"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2zM22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg></span>
      <span class="font-semibold"><span class="text-tnv12-acc-ink">Dev</span>Docs</span>
      <span class="ml-auto rounded-md bg-tnv12-soft px-1.5 py-0.5 font-tnv12-mono text-[11px] font-medium text-tnv12-acc-ink">v4.2</span>
    </div>
    <div class="border-b border-tnv12-line p-3">
      <button type="button" class="flex h-10 w-full items-center gap-2 rounded-lg border border-tnv12-line bg-tnv12-bg px-3 text-left text-[13px] text-tnv12-mut transition-colors hover:border-slate-300"><svg class="size-4 flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>Search docs<kbd class="ml-auto rounded border border-tnv12-line bg-white px-1.5 font-tnv12-mono text-[10px]">⌘K</kbd></button>
    </div>
    <nav aria-label="Documentation" class="flex-1 overflow-y-auto p-2 text-sm font-medium text-tnv12-mut [&_summary]:flex [&_summary]:min-h-10 [&_summary]:cursor-pointer [&_summary]:list-none [&_summary]:items-center [&_summary]:gap-2.5 [&_summary]:rounded-lg [&_summary]:px-2.5 [&_summary]:transition-colors [&_summary]:select-none [&_summary:hover]:bg-tnv12-bg [&_summary:hover]:text-tnv12-ink [&_summary:focus-visible]:outline-2 [&_summary:focus-visible]:outline-tnv12-acc [&_summary::-webkit-details-marker]:hidden [&_a]:flex [&_a]:min-h-10 [&_a]:items-center [&_a]:gap-2.5 [&_a]:rounded-lg [&_a]:px-2.5 [&_a]:transition-colors [&_a:hover]:bg-tnv12-bg [&_a:hover]:text-tnv12-ink [&_a:focus-visible]:outline-2 [&_a:focus-visible]:outline-tnv12-acc [&_svg]:size-4 [&_svg]:flex-none">
      <ul class="space-y-0.5">
        <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg>Introduction</a></li>
        <li><details open class="group/l1">
          <summary><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/></svg>Getting Started<svg class="ml-auto size-3.5! opacity-60 transition-transform duration-200 group-open/l1:rotate-90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></summary>
          <ul class="my-0.5 ml-[19px] border-l border-tnv12-line pl-2 text-[13px] [&>li>a]:-ml-[9px] [&>li>a]:rounded-l-none [&>li>a]:border-l-2 [&>li>a]:border-transparent [&>li>a]:pl-3.5 [&>li>a[aria-current]]:border-tnv12-acc [&>li>a[aria-current]]:bg-tnv12-soft [&>li>a[aria-current]]:font-semibold [&>li>a[aria-current]]:text-tnv12-acc-ink">
            <li><a href="#">Installation</a></li>
            <li><a href="#" aria-current="page">Quick start guide</a></li>
            <li><a href="#">Project structure</a></li>
            <li><details class="group/l2">
              <summary class="text-[13px]">Configuration<svg class="ml-auto size-3.5! opacity-60 transition-transform duration-200 group-open/l2:rotate-90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></summary>
              <ul class="ml-3 border-l border-tnv12-line pl-2"><li><a href="#">Environment variables</a></li><li><a href="#">TypeScript config</a></li><li><a href="#">ESLint setup</a></li></ul>
            </details></li>
          </ul>
        </details></li>
        <li><details class="group/l1">
          <summary><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>Components<span class="ml-auto rounded-full bg-tnv12-soft px-1.5 text-[10px] font-semibold text-tnv12-acc-ink">5</span><svg class="size-3.5! opacity-60 transition-transform duration-200 group-open/l1:rotate-90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></summary>
          <ul class="my-0.5 ml-[19px] border-l border-tnv12-line pl-2 text-[13px]"><li><a href="#">Button</a></li><li><a href="#">Input</a></li><li><a href="#">Modal</a></li><li><a href="#">Navigation</a></li><li><a href="#">Table</a></li></ul>
        </details></li>
        <li><details class="group/l1">
          <summary><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg>API Reference<svg class="ml-auto size-3.5! opacity-60 transition-transform duration-200 group-open/l1:rotate-90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></summary>
          <ul class="my-0.5 ml-[19px] border-l border-tnv12-line pl-2 text-[13px]"><li><a href="#">Authentication</a></li><li><a href="#">Endpoints</a></li><li><a href="#">Webhooks</a></li></ul>
        </details></li>
        <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>FAQ</a></li>
      </ul>
    </nav>
  </aside>
  <main class="min-w-0 flex-1 px-6 py-10 sm:px-12 [&_code]:rounded [&_code]:bg-tnv12-soft [&_code]:px-1.5 [&_code]:font-tnv12-mono [&_code]:text-[0.85em] [&_code]:text-tnv12-acc-ink">
    <p class="text-[13px] font-semibold text-tnv12-acc-ink">Getting Started</p>
    <h1 class="mt-1 text-3xl font-semibold tracking-[-0.02em]">Quick start guide</h1>
    <p class="mt-4 max-w-2xl text-[15px]/[1.75] text-tnv12-mut">Every section in the sidebar is a native <code>&lt;details&gt;</code>. It announces its state, opens with Enter or Space, and animates its height to <code>auto</code> with <code>::details-content</code>. Chevrons rotate with <code>group-open/l1:</code>.</p>
    <pre class="mt-6 max-w-2xl overflow-x-auto rounded-xl bg-slate-900 p-5 font-tnv12-mono text-[13px]/[1.7] text-slate-300"><span class="text-slate-500">/* the only CSS left */</span>
.tnv-12 { <span class="text-sky-300">interpolate-size</span>: allow-keywords; }
.tnv-12 details::details-content {
  <span class="text-sky-300">block-size</span>: <span class="text-emerald-300">0</span>; overflow: hidden;
  transition: block-size .3s, content-visibility .3s allow-discrete;
}
.tnv-12 details[open]::details-content { <span class="text-sky-300">block-size</span>: <span class="text-emerald-300">auto</span>; }</pre>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv12-bg: #f8fafc;
  --color-tnv12-bg: oklch(0.984 0.003 248);
  --color-tnv12-soft: #ecfeff;
  --color-tnv12-soft: oklch(0.984 0.019 201);
  --color-tnv12-line: #e2e8f0;
  --color-tnv12-line: oklch(0.929 0.013 256);
  --color-tnv12-ink: #1e293b;
  --color-tnv12-ink: oklch(0.279 0.041 260);
  --color-tnv12-mut: #475569;
  --color-tnv12-mut: oklch(0.446 0.043 257);
  --color-tnv12-acc: #0891b2;
  --color-tnv12-acc: oklch(0.609 0.126 222);
  --color-tnv12-acc-ink: #0e7490;
  --color-tnv12-acc-ink: oklch(0.52 0.105 223);
  --font-tnv12-sans: 'Rubik', system-ui, sans-serif;
  --font-tnv12-mono: 'IBM Plex Mono', ui-monospace, monospace;
}

.tnv-12 {
  width: 100%;
  min-height: 100svh;
  interpolate-size: allow-keywords;
}
/* ::details-content has no Tailwind variant, so the height animation stays CSS. */

.tnv-12 details::details-content {
  block-size: 0;
  overflow: hidden;
  transition: block-size 0.3s ease, content-visibility 0.3s allow-discrete;
}

.tnv-12 details[open]::details-content {
  block-size: auto;
}

@media (prefers-reduced-motion: reduce) {
  .tnv-12 details::details-content {
    transition: none;
  }
}
```
