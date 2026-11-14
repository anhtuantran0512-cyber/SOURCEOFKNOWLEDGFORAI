---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-neo-brutalist-login-form-hard-shadow/"
title: "Tailwind Neo-Brutalist Login Form with Hard Offset Shadow"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "Raw neo-brutalism for agencies and portfolios: thick black borders, zero-blur offset shadows, monospace type and a press that slams the button flush onto its…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neo-Brutalist Login Form with Hard Offset Shadow
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-neo-brutalist-login-form-hard-shadow/

Raw neo-brutalism for agencies and portfolios: thick black borders, zero-blur offset shadows, monospace type and a press that slams the button flush onto its own shadow. The port is a good reminder that arbitrary values are not always the answer &mdash; shadow-[9px_9px_0_#0a0a0a] is the design, and it deserves to be a @theme shadow token used by four elements.
## HTML
```html
<section class="tlf-23 w-full min-h-svh grid place-items-center bg-tlf23-stage font-tlf23-mono p-6">
  <form novalidate class="relative w-[min(380px,100%)] flex flex-col gap-4 p-8 bg-white rounded-none border-[3px] border-tlf23-ink shadow-tlf23-hard">
    <span aria-hidden="true" class="absolute -top-3.5 right-4 px-3 py-1 rotate-[4deg] bg-tlf23-acc border-[3px] border-tlf23-ink text-xs font-bold tracking-[0.12em] text-tlf23-ink">MEMBERS</span>
    <h1 class="text-[32px] font-tlf23-display tracking-tight text-tlf23-ink">LOG&nbsp;IN</h1>
    <label class="flex flex-col gap-1.5"><span class="text-xs font-bold tracking-[0.1em] text-tlf23-ink">EMAIL</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-13 px-3.5 rounded-none font-tlf23-mono text-[15px] text-tlf23-ink bg-white border-[3px] border-tlf23-ink transition-shadow duration-100 placeholder:text-tlf23-ph focus-visible:outline-none focus-visible:shadow-[5px_5px_0_var(--color-tlf23-acc),0_0_0_3px_var(--color-tlf23-ink)]"></label>
    <label class="flex flex-col gap-1.5"><span class="text-xs font-bold tracking-[0.1em] text-tlf23-ink">PASSWORD</span>
      <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-13 px-3.5 rounded-none font-tlf23-mono text-[15px] text-tlf23-ink bg-white border-[3px] border-tlf23-ink transition-shadow duration-100 placeholder:text-tlf23-ph focus-visible:outline-none focus-visible:shadow-[5px_5px_0_var(--color-tlf23-acc),0_0_0_3px_var(--color-tlf23-ink)]"></label>
    <button type="submit" class="h-13 mt-1 rounded-none cursor-pointer bg-tlf23-acc border-[3px] border-tlf23-ink text-tlf23-ink font-tlf23-display text-base tracking-[0.04em] shadow-tlf23-press transition-[translate,box-shadow] duration-100 hover:-translate-x-px hover:-translate-y-px hover:shadow-[6px_6px_0_var(--color-tlf23-ink)] active:translate-x-[5px] active:translate-y-[5px] active:shadow-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tlf23-ink motion-reduce:transition-none motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0">ENTER &rarr;</button>
    <p class="text-center text-xs text-tlf23-ink">NO ACCOUNT? <a href="#" class="font-bold underline decoration-[3px] underline-offset-2 decoration-tlf23-acc hover:bg-tlf23-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf23-ink">GET ONE</a></p>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf23-stage: #f0efe9;
  --color-tlf23-stage: oklch(0.95 0.008 95);
  --color-tlf23-ink: #0a0a0a;
  --color-tlf23-ink: oklch(0.14 0 0);
  --color-tlf23-acc: #ffe600;
  --color-tlf23-acc: oklch(0.92 0.2 105);
  --color-tlf23-ph: #8a8a80;
  --color-tlf23-ph: oklch(0.6 0.01 95);
  --shadow-tlf23-hard: 9px 9px 0 oklch(0.14 0 0);
  --shadow-tlf23-press: 5px 5px 0 oklch(0.14 0 0);
  --font-tlf23-display: 'Archivo Black', system-ui, sans-serif;
  --font-tlf23-mono: 'Space Mono', ui-monospace, Menlo, monospace;
}

.tlf-23 {
  width: 100%;
  min-height: 100svh;
}
```
