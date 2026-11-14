---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-multi-open-faq-accordion-css-counter/"
title: "Tailwind Multi-Open FAQ Accordion with a Live CSS Counter"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The comparison-friendly FAQ: every panel opens independently, so users can read three answers side by side — the pattern research keeps showing beats…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Open FAQ Accordion with a Live CSS Counter
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-multi-open-faq-accordion-css-counter/

The comparison-friendly FAQ: every panel opens independently, so users can read three answers side by side — the pattern research keeps showing beats only-one-open for comprehension tasks. On top sits a live "N of 6 open" chip driven entirely by CSS counters and has-checked: — genuinely JS-free UI state, and the one demo where Tailwind's arbitrary-property escape hatch is the whole technique.
## HTML
```html
<section class="tfa-04 w-full min-h-svh grid place-items-center bg-tfa04-bg font-tfa04-sans text-tfa04-ink px-5 py-12 bg-[radial-gradient(900px_520px_at_12%_0%,var(--color-tfa04-glow),transparent_62%)]">
  <div class="w-[min(700px,100%)]">
    <header>
      <h1 class="text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Compare answers freely</h1>
      <p class="mt-3 max-w-[54ch] text-[15px] leading-relaxed text-tfa04-mut">Every panel stays open independently — read across, not one at a time. The counter below the heading is pure CSS.</p>
    </header>

    <div class="mt-7 flex flex-col">
      <div class="flex flex-col gap-2.5 [counter-reset:tfa04open]">
        <div class="relative overflow-hidden rounded-2xl border border-tfa04-edge bg-tfa04-panel transition-[border-color,box-shadow] duration-300 has-checked:[counter-increment:tfa04open] has-checked:border-tfa04-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.7_0.16_330/0.5)]">
          <input id="tfa04-q1" type="checkbox" class="peer absolute opacity-0 pointer-events-none" checked>
          <label for="tfa04-q1" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa04-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa04-acc">What is the difference between Starter and Pro?
            <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa04-acc before:transition-transform before:duration-400 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa04-acc after:rotate-90 after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:-rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
          </label>
          <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none"><div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa04-mut">Starter covers one workspace with core analytics. Pro adds unlimited workspaces, funnels, cohort reports and priority support — most teams upgrade when they hit three projects.</p></div></div>
        </div>

        <div class="relative overflow-hidden rounded-2xl border border-tfa04-edge bg-tfa04-panel transition-[border-color,box-shadow] duration-300 has-checked:[counter-increment:tfa04open] has-checked:border-tfa04-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.7_0.16_330/0.5)]">
          <input id="tfa04-q2" type="checkbox" class="peer absolute opacity-0 pointer-events-none" checked>
          <label for="tfa04-q2" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa04-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa04-acc">Which plan do agencies usually pick?
            <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa04-acc before:transition-transform before:duration-400 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa04-acc after:rotate-90 after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:-rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
          </label>
          <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none"><div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa04-mut">Agencies almost always run Pro with the client-billing add-on: each client becomes a workspace with its own invoice line, and you can hand off ownership when an engagement ends.</p></div></div>
        </div>

        <div class="relative overflow-hidden rounded-2xl border border-tfa04-edge bg-tfa04-panel transition-[border-color,box-shadow] duration-300 has-checked:[counter-increment:tfa04open] has-checked:border-tfa04-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.7_0.16_330/0.5)]">
          <input id="tfa04-q3" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
          <label for="tfa04-q3" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa04-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa04-acc">Can I mix plans across one team?
            <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa04-acc before:transition-transform before:duration-400 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa04-acc after:rotate-90 after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:-rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
          </label>
          <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none"><div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa04-mut">No — a workspace has one plan for everyone in it. You can run different plans on different workspaces under the same organisation and consolidate the billing.</p></div></div>
        </div>

        <div class="relative overflow-hidden rounded-2xl border border-tfa04-edge bg-tfa04-panel transition-[border-color,box-shadow] duration-300 has-checked:[counter-increment:tfa04open] has-checked:border-tfa04-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.7_0.16_330/0.5)]">
          <input id="tfa04-q4" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
          <label for="tfa04-q4" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa04-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa04-acc">Is there a nonprofit or education discount?
            <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa04-acc before:transition-transform before:duration-400 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa04-acc after:rotate-90 after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:-rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
          </label>
          <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none"><div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa04-mut">Registered nonprofits and accredited educators get 50% off Pro, verified once a year. Student projects are free on Starter with a .edu / .ac address.</p></div></div>
        </div>

        <div class="relative overflow-hidden rounded-2xl border border-tfa04-edge bg-tfa04-panel transition-[border-color,box-shadow] duration-300 has-checked:[counter-increment:tfa04open] has-checked:border-tfa04-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.7_0.16_330/0.5)]">
          <input id="tfa04-q5" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
          <label for="tfa04-q5" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa04-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa04-acc">What happens to my data if I downgrade?
            <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa04-acc before:transition-transform before:duration-400 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa04-acc after:rotate-90 after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:-rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
          </label>
          <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none"><div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa04-mut">Nothing is deleted. Reports beyond the Starter limits freeze read-only, and re-upgrading unfreezes them instantly with full history intact.</p></div></div>
        </div>

        <div class="relative overflow-hidden rounded-2xl border border-tfa04-edge bg-tfa04-panel transition-[border-color,box-shadow] duration-300 has-checked:[counter-increment:tfa04open] has-checked:border-tfa04-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.7_0.16_330/0.5)]">
          <input id="tfa04-q6" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
          <label for="tfa04-q6" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa04-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa04-acc">Do you have a public roadmap?
            <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa04-acc before:transition-transform before:duration-400 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa04-acc after:rotate-90 after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:-rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
          </label>
          <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none"><div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa04-mut">Yes — roadmap.example.com shows what is planned, building and shipped. Every feature request you upvote notifies you on release.</p></div></div>
        </div>
      </div>

      <div class="order-first mb-3 flex items-baseline gap-2.5">
        <span aria-hidden="true" class="rounded-full bg-tfa04-tint px-3 py-1.5 font-tfa04-mono text-[12px] font-bold text-tfa04-acc after:content-[counter(tfa04open)_'_of_6_open']"></span>
        <span class="text-[11.5px] tracking-[0.04em] text-tfa04-mut">counted by CSS, not JavaScript</span>
      </div>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa04-mut">Pattern note: multi-open beats only-one-open when users compare answers.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa04-bg: #201c2b;
  --color-tfa04-bg: oklch(0.22 0.025 300);
  --color-tfa04-panel: #292335;
  --color-tfa04-panel: oklch(0.26 0.028 300);
  --color-tfa04-glow: #3d2440;
  --color-tfa04-glow: oklch(0.32 0.07 330 / 0.5);
  --color-tfa04-ink: #f5f2f7;
  --color-tfa04-ink: oklch(0.97 0.006 300);
  --color-tfa04-mut: #bdb4c6;
  --color-tfa04-mut: oklch(0.8 0.016 300);
  --color-tfa04-edge: #3e3650;
  --color-tfa04-edge: oklch(0.36 0.03 300);
  --color-tfa04-accedge: #a4649b;
  --color-tfa04-accedge: oklch(0.62 0.1 330);
  --color-tfa04-tint: #3a2739;
  --color-tfa04-tint: oklch(0.3 0.05 330);
  --color-tfa04-acc: #f0a8d8;
  --color-tfa04-acc: oklch(0.83 0.13 330);
  --font-tfa04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa04-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-04 {
  width: 100%;
  min-height: 100svh;
}
```
