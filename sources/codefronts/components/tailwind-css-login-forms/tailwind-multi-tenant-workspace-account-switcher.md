---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-multi-tenant-workspace-account-switcher/"
title: "Tailwind Multi-Tenant Workspace Account Switcher"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The B2B enterprise front door (think Slack or AWS): a returning user picks which workspace to enter from a stack of profile rows, each with a tinted avatar…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Tenant Workspace Account Switcher
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-multi-tenant-workspace-account-switcher/

The B2B enterprise front door (think Slack or AWS): a returning user picks which workspace to enter from a stack of profile rows, each with a tinted avatar and a role badge. The port keeps the original's best idea &mdash; one --tint hue per row drives avatar, badge, hover and ring &mdash; because a per-row hue is data, not a design-scale value, and belongs in a style attribute rather than four utilities.
## HTML
```html
<section class="tlf-02 w-full min-h-svh grid place-items-center bg-tlf02-stage font-tlf02-sans px-5 py-8">
  <div class="w-[min(420px,100%)] p-6 bg-white border border-tlf02-edge rounded-[20px] shadow-[0_24px_56px_-38px_oklch(0.25_0.06_265/0.55)]">
    <header class="mb-4">
      <h1 class="text-xl font-bold tracking-tight text-tlf02-ink">Choose a workspace</h1>
      <p class="mt-1 text-[13px] text-tlf02-mut">You&rsquo;re signed in as [email protected]</p>
    </header>
    <ul class="flex flex-col gap-2 list-none m-0 p-0">
      <li style="--tint:264">
        <a href="#" class="flex items-center gap-3 min-h-11 p-3 rounded-xl no-underline border border-transparent transition-[background-color,border-color,translate] duration-150 hover:translate-x-0.5 hover:bg-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_8%,white)] hover:border-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_30%,white)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.58_0.19_var(--tint)/0.55)] motion-reduce:transition-colors motion-reduce:hover:translate-x-0">
          <span aria-hidden="true" class="grid place-items-center flex-none size-11 rounded-full text-sm font-bold text-white bg-[oklch(0.58_0.16_var(--tint))]">LM</span>
          <span class="flex-1 min-w-0 flex flex-col gap-0.5">
            <span class="text-[15px] font-semibold text-tlf02-ink truncate">Lumen Design</span>
            <span class="text-[12.5px] text-tlf02-mut">lumen.slack.com</span>
          </span>
          <span class="flex-none text-[11px] font-bold tracking-wide px-2.5 py-1 rounded-full text-[oklch(0.42_0.16_var(--tint))] bg-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_16%,white)]">Owner</span>
        </a>
      </li>
      <li style="--tint:160">
        <a href="#" class="flex items-center gap-3 min-h-11 p-3 rounded-xl no-underline border border-transparent transition-[background-color,border-color,translate] duration-150 hover:translate-x-0.5 hover:bg-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_8%,white)] hover:border-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_30%,white)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.58_0.19_var(--tint)/0.55)] motion-reduce:transition-colors motion-reduce:hover:translate-x-0">
          <span aria-hidden="true" class="grid place-items-center flex-none size-11 rounded-full text-sm font-bold text-white bg-[oklch(0.58_0.16_var(--tint))]">AC</span>
          <span class="flex-1 min-w-0 flex flex-col gap-0.5">
            <span class="text-[15px] font-semibold text-tlf02-ink truncate">Acme Corp</span>
            <span class="text-[12.5px] text-tlf02-mut">acme.slack.com</span>
          </span>
          <span class="flex-none text-[11px] font-bold tracking-wide px-2.5 py-1 rounded-full text-[oklch(0.42_0.16_var(--tint))] bg-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_16%,white)]">Admin</span>
        </a>
      </li>
      <li style="--tint:30">
        <a href="#" class="flex items-center gap-3 min-h-11 p-3 rounded-xl no-underline border border-transparent transition-[background-color,border-color,translate] duration-150 hover:translate-x-0.5 hover:bg-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_8%,white)] hover:border-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_30%,white)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.58_0.19_var(--tint)/0.55)] motion-reduce:transition-colors motion-reduce:hover:translate-x-0">
          <span aria-hidden="true" class="grid place-items-center flex-none size-11 rounded-full text-sm font-bold text-white bg-[oklch(0.58_0.16_var(--tint))]">NW</span>
          <span class="flex-1 min-w-0 flex flex-col gap-0.5">
            <span class="text-[15px] font-semibold text-tlf02-ink truncate">Northwind</span>
            <span class="text-[12.5px] text-tlf02-mut">northwind.slack.com</span>
          </span>
          <span class="flex-none text-[11px] font-bold tracking-wide px-2.5 py-1 rounded-full text-[oklch(0.42_0.16_var(--tint))] bg-[color-mix(in_oklch,oklch(0.58_0.16_var(--tint))_16%,white)]">Member</span>
        </a>
      </li>
    </ul>
    <a href="#" class="flex items-center justify-center gap-2 min-h-11 mt-4 p-3 rounded-xl border-[1.5px] border-dashed border-tlf02-dash text-sm font-semibold text-tlf02-mut no-underline transition-colors duration-150 hover:border-tlf02-acc hover:text-tlf02-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf02-ring"><span aria-hidden="true" class="text-[17px] leading-none">+</span> Add another account</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf02-stage: #f4f5f9;
  --color-tlf02-stage: oklch(0.96 0.005 270);
  --color-tlf02-edge: #e7e9f0;
  --color-tlf02-edge: oklch(0.92 0.006 270);
  --color-tlf02-dash: #cfd4e2;
  --color-tlf02-dash: oklch(0.85 0.012 270);
  --color-tlf02-ink: #161c2e;
  --color-tlf02-ink: oklch(0.23 0.04 270);
  --color-tlf02-mut: #656c86;
  --color-tlf02-mut: oklch(0.51 0.03 270);
  --color-tlf02-acc: #5a63d8;
  --color-tlf02-acc: oklch(0.58 0.19 264);
  --color-tlf02-ring: #c9cdf4;
  --color-tlf02-ring: oklch(0.58 0.19 264 / 0.5);
  --color-tlf02-wash: #f0f1f6;
  --color-tlf02-wash: oklch(0.94 0.005 270);
  --font-tlf02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tlf-02 {
  width: 100%;
  min-height: 100svh;
}
/* color-mix() fallback: browsers without it get a neutral wash rather than no hover at all. */

@supports not (background: color-mix(in oklch, red 8%, white)) {
  .tlf-02 a:hover {
    background: var(--color-tlf02-wash);
    border-color: var(--color-tlf02-dash);
  }
}
```
