---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-css-faq-accordion-template-free/"
title: "Tailwind CSS FAQ Accordion Template (Free, Copy-Paste)"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The house-style SaaS FAQ, and the demo where the port stops being a port: in the CSS collection this entry shipped a hand-compiled stylesheet imitating…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS FAQ Accordion Template (Free, Copy-Paste)
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-css-faq-accordion-template-free/

The house-style SaaS FAQ, and the demo where the port stops being a port: in the CSS collection this entry shipped a hand-compiled stylesheet imitating Tailwind, and here it is simply real Tailwind. Indigo on white, native <details class="group">, divide-y for the rules between rows, a full dark: track, and no plugin, no config extension, no JavaScript.
## HTML
```html
<section class="tfa-05 w-full min-h-svh grid place-items-center bg-slate-50 font-tfa05-sans px-5 py-12 dark:bg-slate-950">
  <div class="mx-auto w-full max-w-2xl">
    <p class="text-center font-tfa05-mono text-[12px] font-semibold uppercase tracking-[0.18em] text-indigo-600 dark:text-indigo-400">Support</p>
    <h1 class="mt-3 text-center text-[clamp(28px,5vw,38px)] font-extrabold tracking-[-0.025em] text-slate-900 dark:text-slate-50">Frequently asked questions</h1>
    <p class="mx-auto mt-3 max-w-[48ch] text-center text-[14.5px] leading-7 text-slate-600 dark:text-slate-400">Native <code class="rounded bg-indigo-50 px-1.5 py-0.5 font-tfa05-mono text-[0.85em] text-indigo-700 dark:bg-indigo-950 dark:text-indigo-300">&lt;details class="group"&gt;</code> + <code class="rounded bg-indigo-50 px-1.5 py-0.5 font-tfa05-mono text-[0.85em] text-indigo-700 dark:bg-indigo-950 dark:text-indigo-300">group-open:</code> — no plugin, no JavaScript.</p>

    <div data-panel class="mt-9 divide-y divide-slate-200 overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-[0_1px_2px_oklch(0.4_0.02_250/0.06),0_12px_28px_-20px_oklch(0.4_0.02_250/0.25)] dark:divide-slate-800 dark:border-slate-800 dark:bg-slate-900">
      <details class="group" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 text-[15.5px] font-semibold text-slate-900 transition-colors duration-200 hover:text-indigo-700 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-indigo-600 dark:text-slate-100 dark:hover:text-indigo-300 [&::-webkit-details-marker]:hidden">How does billing work?
          <svg class="size-5 shrink-0 text-indigo-600 transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none dark:text-indigo-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
        </summary>
        <p class="px-6 pb-5 text-[14px] leading-7 text-slate-600 dark:text-slate-400">Plans are billed per seat, monthly or annually. You can add or remove seats at any time and the next invoice prorates automatically — no support ticket needed.</p>
      </details>

      <details class="group">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 text-[15.5px] font-semibold text-slate-900 transition-colors duration-200 hover:text-indigo-700 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-indigo-600 dark:text-slate-100 dark:hover:text-indigo-300 [&::-webkit-details-marker]:hidden">Can I invite external collaborators?
          <svg class="size-5 shrink-0 text-indigo-600 transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none dark:text-indigo-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
        </summary>
        <p class="px-6 pb-5 text-[14px] leading-7 text-slate-600 dark:text-slate-400">Guests can be invited to single projects free of charge. They see only what you share, and you can convert a guest to a full seat with one click when the collaboration grows.</p>
      </details>

      <details class="group">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 text-[15.5px] font-semibold text-slate-900 transition-colors duration-200 hover:text-indigo-700 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-indigo-600 dark:text-slate-100 dark:hover:text-indigo-300 [&::-webkit-details-marker]:hidden">Is there an API?
          <svg class="size-5 shrink-0 text-indigo-600 transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none dark:text-indigo-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
        </summary>
        <p class="px-6 pb-5 text-[14px] leading-7 text-slate-600 dark:text-slate-400">A REST API with typed SDKs for TypeScript and Python ships on every plan, rate-limited by tier. Webhooks cover every event you can see in the activity feed.</p>
      </details>

      <details class="group">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 text-[15.5px] font-semibold text-slate-900 transition-colors duration-200 hover:text-indigo-700 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-indigo-600 dark:text-slate-100 dark:hover:text-indigo-300 [&::-webkit-details-marker]:hidden">How do I cancel?
          <svg class="size-5 shrink-0 text-indigo-600 transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none dark:text-indigo-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
        </summary>
        <p class="px-6 pb-5 text-[14px] leading-7 text-slate-600 dark:text-slate-400">Self-serve, from Settings → Billing, effective at period end — no call, no retention script. Your data stays exportable for 90 days after cancellation.</p>
      </details>
    </div>

    <p class="mt-6 text-center text-[12px] text-slate-500 dark:text-slate-500">Real utilities, not a compiled imitation — paste straight into any Tailwind 3/4 project.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-tfa05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa05-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-05 {
  width: 100%;
  min-height: 100svh;
}
/* Optional enhancement, identical to demo 02 and worth pasting into your globals.css once:
   it animates every group accordion on the site and degrades to instant open where unsupported. */

.tfa-05 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-05 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .3s cubic-bezier(.4,0,.2,1), opacity .25s, content-visibility .3s allow-discrete;
  }

  .tfa-05 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-05 details::details-content {
    transition-duration: 1ms;
  }
}
```
