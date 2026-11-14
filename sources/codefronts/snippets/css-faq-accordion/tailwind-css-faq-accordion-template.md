---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/tailwind-css-faq-accordion-template/"
title: "Tailwind CSS FAQ Accordion Template"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "A production Tailwind FAQ built the idiomatic way: native <details> for behavior, the group / group-open variant pair for state styling, and zero plugins or JS."
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS FAQ Accordion Template
Source: https://codefronts.com/snippets/css-faq-accordion/tailwind-css-faq-accordion-template/

A production Tailwind FAQ built the idiomatic way: native <details> for behavior, the group / group-open variant pair for state styling, and zero plugins or JS. The markup is 1:1 real Tailwind utility classes you can paste into any Tailwind 3/4 project; the demo ships with a scoped stylesheet compiling exactly those utilities, so it renders standalone here and drops into your build unchanged. Indigo-on-white, the house style of half the SaaS industry — intentionally.
## HTML
```html
<section class="cfa-05" aria-label="Tailwind CSS FAQ accordion template">
  <div class="cfa-05__stage">
    <div class="mx-auto w-full max-w-2xl">
      <p class="text-center text-sm font-semibold uppercase tracking-widest text-indigo-600">Support</p>
      <h1 class="mt-3 text-center text-3xl font-bold tracking-tight text-slate-900">Frequently asked questions</h1>
      <p class="mt-3 text-center text-sm leading-6 text-slate-500">Native <code class="cfa-05__code">&lt;details class="group"&gt;</code> + <code class="cfa-05__code">group-open:</code> — no plugin, no JS.</p>
      <div class="mt-10 divide-y divide-slate-200 rounded-2xl border border-slate-200 bg-white shadow-sm">
        <details class="group" open>
          <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 font-semibold text-slate-900 marker-hidden focus-ring">How does billing work?
            <svg class="size-5 shrink-0 text-indigo-600 transition-transform duration-300 group-open-rotate" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
          </summary>
          <p class="px-6 pb-5 text-sm leading-7 text-slate-600">Plans are billed per seat, monthly or annually. You can add or remove seats at any time and the next invoice prorates automatically — no support ticket needed.</p>
        </details>
        <details class="group">
          <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 font-semibold text-slate-900 marker-hidden focus-ring">Can I invite external collaborators?
            <svg class="size-5 shrink-0 text-indigo-600 transition-transform duration-300 group-open-rotate" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
          </summary>
          <p class="px-6 pb-5 text-sm leading-7 text-slate-600">Guests can be invited to single projects free of charge. They see only what you share, and you can convert a guest to a full seat with one click when the collaboration grows.</p>
        </details>
        <details class="group">
          <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 font-semibold text-slate-900 marker-hidden focus-ring">Is there an API?
            <svg class="size-5 shrink-0 text-indigo-600 transition-transform duration-300 group-open-rotate" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
          </summary>
          <p class="px-6 pb-5 text-sm leading-7 text-slate-600">A REST API with typed SDKs for TypeScript and Python ships on every plan, rate-limited by tier. Webhooks cover every event you can see in the activity feed.</p>
        </details>
        <details class="group">
          <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 font-semibold text-slate-900 marker-hidden focus-ring">How do I cancel?
            <svg class="size-5 shrink-0 text-indigo-600 transition-transform duration-300 group-open-rotate" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
          </summary>
          <p class="px-6 pb-5 text-sm leading-7 text-slate-600">Self-serve, from Settings → Billing, effective at period end — no call, no chat with a retention script. Your data stays exportable for 90 days after cancellation.</p>
        </details>
      </div>
      <p class="mt-6 text-center text-xs text-slate-400">Markup is 1:1 Tailwind utilities — paste into any Tailwind 3/4 project. CodeFronts collection.</p>
    </div>
  </div>
</section>
```
## CSS
```css
/* Scoped "compiled Tailwind" so the template previews standalone.
   In a real Tailwind project DELETE this block — the markup's utilities compile natively.
   Two shorthands used in the markup for portability outside JIT arbitrary variants:
   .marker-hidden = list-none + [&::-webkit-details-marker]:hidden
   .group-open-rotate = group-open:rotate-180 · .focus-ring = focus-visible ring utilities */

.cfa-05,
.cfa-05 *,
.cfa-05 *::before,
.cfa-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  border: 0 solid rgb(226 232 240);
}

.cfa-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: rgb(248 250 252);
  font-family: ui-sans-serif,'Segoe UI',system-ui,sans-serif;
  color: rgb(15 23 42);
}

.cfa-05__stage {
  width: 100%;
  padding: clamp(20px,4vw,56px);
}

.cfa-05__code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .85em;
  background: rgb(238 242 255);
  color: rgb(79 70 229);
  padding: 2px 6px;
  border-radius: 5px;
}

.cfa-05 .mx-auto {
  margin-inline: auto;
}

.cfa-05 .w-full {
  width: 100%;
}

.cfa-05 .max-w-2xl {
  max-width: 42rem;
}

.cfa-05 .text-center {
  text-align: center;
}

.cfa-05 .text-sm {
  font-size: .875rem;
}

.cfa-05 .text-xs {
  font-size: .75rem;
}

.cfa-05 .text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.cfa-05 .font-semibold {
  font-weight: 600;
}

.cfa-05 .font-bold {
  font-weight: 700;
}

.cfa-05 .uppercase {
  text-transform: uppercase;
}

.cfa-05 .tracking-widest {
  letter-spacing: .1em;
}

.cfa-05 .tracking-tight {
  letter-spacing: -.025em;
}

.cfa-05 .text-indigo-600 {
  color: rgb(79 70 229);
}

.cfa-05 .text-slate-900 {
  color: rgb(15 23 42);
}

.cfa-05 .text-slate-600 {
  color: rgb(71 85 105);
}

.cfa-05 .text-slate-500 {
  color: rgb(100 116 139);
}

.cfa-05 .text-slate-400 {
  color: rgb(148 163 184);
}

.cfa-05 .mt-3 {
  margin-top: .75rem;
}

.cfa-05 .mt-6 {
  margin-top: 1.5rem;
}

.cfa-05 .mt-10 {
  margin-top: 2.5rem;
}

.cfa-05 .leading-6 {
  line-height: 1.5rem;
}

.cfa-05 .leading-7 {
  line-height: 1.75rem;
}

.cfa-05 .divide-y>*+* {
  border-top-width: 1px;
}

.cfa-05 .divide-slate-200>*+* {
  border-color: rgb(226 232 240);
}

.cfa-05 .rounded-2xl {
  border-radius: 1rem;
  overflow: hidden;
}

.cfa-05 .border {
  border-width: 1px;
}

.cfa-05 .border-slate-200 {
  border-color: rgb(226 232 240);
}

.cfa-05 .bg-white {
  background: rgb(255 255 255);
}

.cfa-05 .shadow-sm {
  box-shadow: 0 1px 3px rgb(15 23 42/.08),0 1px 2px rgb(15 23 42/.04);
}

.cfa-05 .flex {
  display: flex;
}

.cfa-05 .cursor-pointer {
  cursor: pointer;
}

.cfa-05 .items-center {
  align-items: center;
}

.cfa-05 .justify-between {
  justify-content: space-between;
}

.cfa-05 .gap-4 {
  gap: 1rem;
}

.cfa-05 .px-6 {
  padding-inline: 1.5rem;
}

.cfa-05 .py-5 {
  padding-block: 1.25rem;
}

.cfa-05 .pb-5 {
  padding-bottom: 1.25rem;
}

.cfa-05 .list-none {
  list-style: none;
}

.cfa-05 .marker-hidden {
  list-style: none;
}

.cfa-05 .marker-hidden::-webkit-details-marker {
  display: none;
}

.cfa-05 .size-5 {
  width: 1.25rem;
  height: 1.25rem;
}

.cfa-05 .shrink-0 {
  flex-shrink: 0;
}

.cfa-05 .transition-transform {
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.cfa-05 .duration-300 {
  transition-duration: .3s;
}

.cfa-05 .group[open]>summary .group-open-rotate {
  transform: rotate(180deg);
}

.cfa-05 summary {
  min-height: 44px;
}

.cfa-05 .focus-ring:focus-visible {
  outline: 2px solid rgb(99 102 241);
  outline-offset: -2px;
  border-radius: .5rem;
}

.cfa-05 summary:hover {
  color: rgb(79 70 229);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-05 * {
    transition-duration: .01ms !important;
  }
}
```
