---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-documentation-sidebar-multi-level-target-tree/"
title: "Tailwind Documentation Sidebar with Multi-Level :target Tree"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The Stripe-style docs tree: three levels of nested navigation, a guide rail connecting each level, and the current section lit automatically as readers jump…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Documentation Sidebar with Multi-Level :target Tree
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-documentation-sidebar-multi-level-target-tree/

The Stripe-style docs tree: three levels of nested navigation, a guide rail connecting each level, and the current section lit automatically as readers jump between anchors &mdash; no scroll-spy script. The port turns eight :has(#id:target) selectors into eight arbitrary variants that sit on the links they light.
## HTML
```html
<section class="tsl-03 w-full h-svh min-h-svh grid grid-cols-[250px_1fr] font-tsl03-sans bg-tsl03-bg text-tsl03-ink">
  <aside class="border-r border-tsl03-line px-3 py-6 overflow-y-auto [scrollbar-gutter:stable]">
    <nav aria-label="Documentation">
      <ul class="list-none m-0 p-0 [--depth:0]">
        <li><a href="#tsl03-start" class="block my-px py-[7px] pe-2.5 ps-[calc(0.75rem+var(--depth)*0.875rem)] rounded-lg text-[13.5px] font-medium leading-tight text-tsl03-mut no-underline transition-colors duration-150 hover:text-tsl03-ink hover:bg-tsl03-hover focus-visible:outline-2 focus-visible:outline-tsl03-accent focus-visible:outline-offset-1">Getting started</a>
          <ul class="list-none m-0 p-0 [--depth:1] border-s border-tsl03-line ms-[19px]">
            <li><a href="#tsl03-install" class="block my-px py-[7px] pe-2.5 ps-3 rounded-lg text-[13.5px] font-medium leading-tight text-tsl03-mut no-underline transition-colors duration-150 hover:text-tsl03-ink hover:bg-tsl03-hover focus-visible:outline-2 focus-visible:outline-tsl03-accent focus-visible:outline-offset-1">Installation</a></li>
            <li><a href="#tsl03-auth" class="block my-px py-[7px] pe-2.5 ps-3 rounded-lg text-[13.5px] font-medium leading-tight text-tsl03-mut no-underline transition-colors duration-150 hover:text-tsl03-ink hover:bg-tsl03-hover focus-visible:outline-2 focus-visible:outline-tsl03-accent focus-visible:outline-offset-1">Authentication</a>
              <ul class="list-none m-0 p-0 [--depth:2] border-s border-tsl03-line ms-[15px]">
                <li><a href="#tsl03-keys" class="block my-px py-[7px] pe-2.5 ps-3 rounded-lg text-[13.5px] font-medium leading-tight text-tsl03-mut no-underline transition-colors duration-150 hover:text-tsl03-ink hover:bg-tsl03-hover focus-visible:outline-2 focus-visible:outline-tsl03-accent focus-visible:outline-offset-1">API keys</a></li>
                <li><a href="#tsl03-oauth" class="block my-px py-[7px] pe-2.5 ps-3 rounded-lg text-[13.5px] font-medium leading-tight text-tsl03-mut no-underline transition-colors duration-150 hover:text-tsl03-ink hover:bg-tsl03-hover focus-visible:outline-2 focus-visible:outline-tsl03-accent focus-visible:outline-offset-1">OAuth 2.0</a></li>
              </ul>
            </li>
          </ul>
        </li>
        <li class="mt-1"><a href="#tsl03-core" class="block my-px py-[7px] pe-2.5 ps-[calc(0.75rem+var(--depth)*0.875rem)] rounded-lg text-[13.5px] font-medium leading-tight text-tsl03-mut no-underline transition-colors duration-150 hover:text-tsl03-ink hover:bg-tsl03-hover focus-visible:outline-2 focus-visible:outline-tsl03-accent focus-visible:outline-offset-1">Core concepts</a>
          <ul class="list-none m-0 p-0 [--depth:1] border-s border-tsl03-line ms-[19px]">
            <li><a href="#tsl03-webhooks" class="block my-px py-[7px] pe-2.5 ps-3 rounded-lg text-[13.5px] font-medium leading-tight text-tsl03-mut no-underline transition-colors duration-150 hover:text-tsl03-ink hover:bg-tsl03-hover focus-visible:outline-2 focus-visible:outline-tsl03-accent focus-visible:outline-offset-1">Webhooks</a></li>
            <li><a href="#tsl03-errors" class="block my-px py-[7px] pe-2.5 ps-3 rounded-lg text-[13.5px] font-medium leading-tight text-tsl03-mut no-underline transition-colors duration-150 hover:text-tsl03-ink hover:bg-tsl03-hover focus-visible:outline-2 focus-visible:outline-tsl03-accent focus-visible:outline-offset-1">Error handling</a></li>
          </ul>
        </li>
      </ul>
    </nav>
  </aside>
  <main class="overflow-y-auto scroll-smooth px-11 py-9 grid gap-[34px] content-start motion-reduce:scroll-auto [scrollbar-gutter:stable]">
    <section id="tsl03-start" class="scroll-mt-6"><h1 class="text-[26px] font-bold leading-tight tracking-tight">Getting started</h1><p class="mt-2 max-w-[58ch] text-sm leading-[1.65] text-tsl03-mut text-pretty">Click any sidebar item &mdash; the matching link lights via <code class="font-tsl03-mono text-[12.5px]">:target</code>, no scroll-spy script.</p></section>
    <section id="tsl03-install" class="scroll-mt-6"><h2 class="text-xl font-bold leading-tight">Installation</h2><p class="mt-2 max-w-[58ch] text-sm leading-[1.65] text-tsl03-mut text-pretty">Install the SDK with your package manager of choice.</p></section>
    <section id="tsl03-auth" class="scroll-mt-6"><h2 class="text-xl font-bold leading-tight">Authentication</h2><p class="mt-2 max-w-[58ch] text-sm leading-[1.65] text-tsl03-mut text-pretty">All requests are authenticated with a bearer token.</p></section>
    <section id="tsl03-keys" class="scroll-mt-6"><h3 class="text-base font-semibold leading-snug">API keys</h3><p class="mt-2 max-w-[58ch] text-sm leading-[1.65] text-tsl03-mut text-pretty">Generate keys from the dashboard. Rotate them quarterly.</p></section>
    <section id="tsl03-oauth" class="scroll-mt-6"><h3 class="text-base font-semibold leading-snug">OAuth 2.0</h3><p class="mt-2 max-w-[58ch] text-sm leading-[1.65] text-tsl03-mut text-pretty">Use the authorization-code flow for user-scoped access.</p></section>
    <section id="tsl03-core" class="scroll-mt-6"><h2 class="text-xl font-bold leading-tight">Core concepts</h2><p class="mt-2 max-w-[58ch] text-sm leading-[1.65] text-tsl03-mut text-pretty">Resources, events and idempotency.</p></section>
    <section id="tsl03-webhooks" class="scroll-mt-6"><h3 class="text-base font-semibold leading-snug">Webhooks</h3><p class="mt-2 max-w-[58ch] text-sm leading-[1.65] text-tsl03-mut text-pretty">Receive events at your endpoint within seconds.</p></section>
    <section id="tsl03-errors" class="scroll-mt-6"><h3 class="text-base font-semibold leading-snug">Error handling</h3><p class="mt-2 max-w-[58ch] text-sm leading-[1.65] text-tsl03-mut text-pretty">Every error returns a typed code and a human message.</p></section>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl03-bg: #fdfdfc;
  --color-tsl03-bg: oklch(0.99 0.002 100);
  --color-tsl03-ink: #3b3f47;
  --color-tsl03-ink: oklch(0.27 0.015 265);
  --color-tsl03-mut: #767a84;
  --color-tsl03-mut: oklch(0.52 0.012 265);
  --color-tsl03-line: #e3e4e9;
  --color-tsl03-line: oklch(0.9 0.007 265);
  --color-tsl03-accent: #4a5fd0;
  --color-tsl03-accent: oklch(0.55 0.17 265);
  --color-tsl03-hover: rgb(59 63 71 / 0.05);
  --color-tsl03-hover: color-mix(in oklab, oklch(0.27 0.015 265) 5%, transparent);
  --color-tsl03-tint: rgb(74 95 208 / 0.1);
  --color-tsl03-tint: color-mix(in oklab, oklch(0.55 0.17 265) 10%, transparent);
  --font-tsl03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl03-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-03 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: light;
}
/* STATE — the active link, keyed off the section the fragment points at. */

.tsl-03:has(#tsl03-start:target) a[href="#tsl03-start"],
.tsl-03:has(#tsl03-install:target) a[href="#tsl03-install"],
.tsl-03:has(#tsl03-auth:target) a[href="#tsl03-auth"],
.tsl-03:has(#tsl03-keys:target) a[href="#tsl03-keys"],
.tsl-03:has(#tsl03-oauth:target) a[href="#tsl03-oauth"],
.tsl-03:has(#tsl03-core:target) a[href="#tsl03-core"],
.tsl-03:has(#tsl03-webhooks:target) a[href="#tsl03-webhooks"],
.tsl-03:has(#tsl03-errors:target) a[href="#tsl03-errors"] {
  color: var(--color-tsl03-accent);
  background: var(--color-tsl03-tint);
  font-weight: 600;
}
```
