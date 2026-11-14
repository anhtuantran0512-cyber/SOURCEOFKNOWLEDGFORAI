---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/minimal-tailwind-css-admin-dashboard-template-no-javascript/"
title: "Minimal Tailwind CSS Admin Dashboard Template (No JavaScript)"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "A complete shell where the server template stays plain: <header>, <nav>, <main>, <footer>, lists and links &mdash; almost no classes inside."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Tailwind CSS Admin Dashboard Template (No JavaScript)
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/minimal-tailwind-css-admin-dashboard-template-no-javascript/

A complete shell where the server template stays plain: <header>, <nav>, <main>, <footer>, lists and links &mdash; almost no classes inside. All styling hangs off one root element via child and descendant variants ([&>nav]:, [&_main_section]:, [&_a]:), so Django, Laravel, Rails or PHP partials render clean HTML and still get a modern Tailwind look.
## HTML
```html
<section class="tdl-12 @container/s w-full min-h-svh bg-tdl12-bg font-tdl12-sans text-tdl12-ink antialiased" aria-label="Minimal zero-JS dashboard shell demo">
  <div class="relative grid h-svh min-h-[32rem] grid-cols-[13.75rem_minmax(0,1fr)] grid-rows-[auto_minmax(0,1fr)_auto] overflow-hidden bg-tdl12-paper [grid-template-areas:'header_header'_'nav_main'_'footer_footer'] @max-[39rem]/s:grid-cols-1 @max-[39rem]/s:grid-rows-[auto_auto_minmax(0,1fr)_auto] @max-[39rem]/s:[grid-template-areas:'header'_'nav'_'main'_'footer'] [&_a]:rounded-md [&_a]:text-[13.5px] [&_a]:font-semibold [&_a]:text-tdl12-acc [&_a]:no-underline [&_a]:underline-offset-3 [&_a:hover]:underline [&_a:focus-visible]:outline-2 [&_a:focus-visible]:outline-offset-2 [&_a:focus-visible]:outline-tdl12-acc [&>header]:flex [&>header]:items-center [&>header]:gap-5 [&>header]:border-b [&>header]:border-tdl12-edge [&>header]:bg-white [&>header]:px-4 [&>header]:py-3.5 [&>header]:[grid-area:header] [&>header_strong]:mr-auto [&>header_strong]:flex [&>header_strong]:items-center [&>header_strong]:gap-2 [&>header_strong]:text-base [&>header_strong]:font-extrabold [&>header_strong]:tracking-tight [&>nav]:flex [&>nav]:flex-col [&>nav]:gap-0.5 [&>nav]:border-r [&>nav]:border-tdl12-edge [&>nav]:bg-white [&>nav]:p-3 [&>nav]:[grid-area:nav] @max-[39rem]/s:[&>nav]:flex-row @max-[39rem]/s:[&>nav]:overflow-x-auto @max-[39rem]/s:[&>nav]:border-r-0 @max-[39rem]/s:[&>nav]:border-b [&>nav_a]:flex [&>nav_a]:h-10 [&>nav_a]:flex-none [&>nav_a]:items-center [&>nav_a]:rounded-lg [&>nav_a]:px-3 [&>nav_a]:text-tdl12-mut [&>nav_a:hover]:bg-tdl12-acc/6 [&>nav_a:hover]:text-tdl12-ink [&>nav_a:hover]:no-underline [&>nav_a[aria-current=page]]:bg-tdl12-acc/12 [&>nav_a[aria-current=page]]:text-tdl12-accink [&>main]:grid [&>main]:content-start [&>main]:gap-4 [&>main]:overflow-y-auto [&>main]:overscroll-contain [&>main]:p-5 [&>main]:[grid-area:main] [&_h1]:text-xl [&_h1]:font-extrabold [&_h1]:tracking-tight [&_main_section]:rounded-xl [&_main_section]:border [&_main_section]:border-tdl12-edge [&_main_section]:bg-white [&_main_section]:p-4 [&_h2]:mb-1.5 [&_h2]:text-[11px] [&_h2]:font-bold [&_h2]:tracking-[0.09em] [&_h2]:text-tdl12-mut [&_h2]:uppercase [&_ul]:grid [&_li]:flex [&_li]:items-baseline [&_li]:gap-1.5 [&_li]:border-b [&_li]:border-tdl12-edge/55 [&_li]:px-0.5 [&_li]:py-2.5 [&_li]:text-[13.5px] [&_li:last-child]:border-b-0 [&_li_b]:font-semibold [&_time]:ml-auto [&_time]:text-[11.5px] [&_time]:text-tdl12-mut [&_time]:tabular-nums [&>footer]:border-t [&>footer]:border-tdl12-edge [&>footer]:bg-white [&>footer]:px-4 [&>footer]:py-2.5 [&>footer]:text-xs [&>footer]:text-tdl12-mut [&>footer]:[grid-area:footer]">
    <a href="#tdl12-main" class="sr-only z-20 bg-white px-3 py-2 focus:not-sr-only focus:absolute focus:top-2 focus:left-2">Skip to content</a>
    <header><strong><span aria-hidden="true" class="size-3 rounded-full bg-tdl12-acc"></span>Plainboard</strong><a href="#docs">Docs</a><a href="#account">Account</a></header>
    <nav aria-label="Primary">
      <a href="#home" aria-current="page">Home</a>
      <a href="#projects">Projects</a>
      <a href="#tasks">Tasks</a>
      <a href="#invoices">Invoices</a>
      <a href="#team">Team</a>
    </nav>
    <main id="tdl12-main" tabindex="-1">
      <h1>Good morning, Jordan</h1>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(min(9.5rem,100%),1fr))] gap-4 [&_p]:text-[26px] [&_p]:font-extrabold [&_p]:tracking-tight [&_p]:tabular-nums">
        <section><h2>Open tasks</h2><p>23</p></section>
        <section><h2>Due this week</h2><p>7</p></section>
        <section><h2>Hours logged</h2><p>31.5</p></section>
      </div>
      <section>
        <h2>Recent activity</h2>
        <ul>
          <li>Invoice <b>#204</b> sent to Harper &amp; Co <time>10:41</time></li>
          <li>Task <b>“Migrate DNS”</b> completed <time>09:12</time></li>
          <li>New project <b>Riverside</b> created <time>Yesterday</time></li>
          <li>Task <b>“QA pass”</b> assigned to Sam <time>Yesterday</time></li>
        </ul>
      </section>
    </main>
    <footer>Rendered server-side · no client framework · <a href="#src">view source</a></footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl12-bg: #f4f6f9;
  --color-tdl12-bg: oklch(0.97 0.005 250);
  --color-tdl12-paper: #f9fafc;
  --color-tdl12-paper: oklch(0.985 0.003 250);
  --color-tdl12-edge: #e1e4ea;
  --color-tdl12-edge: oklch(0.91 0.008 250);
  --color-tdl12-ink: #262b33;
  --color-tdl12-ink: oklch(0.27 0.012 250);
  --color-tdl12-mut: #5a616d;
  --color-tdl12-mut: oklch(0.48 0.015 250);
  --color-tdl12-acc: #2864c7;
  --color-tdl12-acc: oklch(0.53 0.16 255);
  --color-tdl12-accink: #1d4c9c;
  --color-tdl12-accink: oklch(0.44 0.14 255);
  --font-tdl12-sans: 'Hanken Grotesk', system-ui, sans-serif;
}

.tdl-12 {
  width: 100%;
  min-height: 100svh;
}
```
