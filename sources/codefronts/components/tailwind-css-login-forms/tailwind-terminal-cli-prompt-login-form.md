---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-terminal-cli-prompt-login-form/"
title: "Tailwind Terminal CLI Prompt Login Form"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "An authentic CLI login for dev-tools, DevOps panels and security apps: monospaced type, a traffic-light window bar, a blinking block cursor and raw…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Terminal CLI Prompt Login Form
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-terminal-cli-prompt-login-form/

An authentic CLI login for dev-tools, DevOps panels and security apps: monospaced type, a traffic-light window bar, a blinking block cursor and raw prompt-style inputs with no chrome. The port keeps every affordance the original argued for &mdash; including a visible focus treatment on borderless fields, which is the easy thing to lose in a terminal aesthetic.
## HTML
```html
<section class="tlf-12 w-full min-h-svh grid place-items-center bg-tlf12-stage font-tlf12-mono p-6">
  <form novalidate class="w-[min(460px,100%)] rounded-xl overflow-hidden bg-tlf12-card border border-tlf12-edge shadow-[0_30px_70px_-44px_black]">
    <div class="flex items-center gap-2 px-4 py-3 bg-tlf12-bar border-b border-tlf12-edge">
      <span aria-hidden="true" class="size-3 rounded-full bg-tlf12-dot1"></span>
      <span aria-hidden="true" class="size-3 rounded-full bg-tlf12-dot2"></span>
      <span aria-hidden="true" class="size-3 rounded-full bg-tlf12-dot3"></span>
      <span class="ml-2 text-xs text-tlf12-mut">auth@northwind &mdash; ssh</span>
    </div>
    <div class="flex flex-col gap-4 p-6">
      <p class="text-[13px]/[1.6] text-tlf12-mut">Authentication required. Provide credentials to continue.</p>
      <label class="flex items-center gap-2 pb-2 border-b border-transparent transition-colors duration-150 focus-within:border-tlf12-caret before:content-['$'] before:font-bold before:text-tlf12-prompt">
        <span class="text-[13px] text-tlf12-label select-none">username</span>
        <input type="text" autocomplete="username" placeholder="ana.reyes" required class="flex-1 min-w-0 h-8 bg-transparent border-0 text-[14.5px] text-tlf12-ink placeholder:text-tlf12-ph focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tlf12-caret">
      </label>
      <label class="flex items-center gap-2 pb-2 border-b border-transparent transition-colors duration-150 focus-within:border-tlf12-caret before:content-['$'] before:font-bold before:text-tlf12-prompt">
        <span class="text-[13px] text-tlf12-label select-none">password</span>
        <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="flex-1 min-w-0 h-8 bg-transparent border-0 text-[14.5px] text-tlf12-ink placeholder:text-tlf12-ph focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tlf12-caret">
        <span aria-hidden="true" class="w-2 h-[17px] bg-tlf12-caret animate-tlf12-blink motion-reduce:animate-none"></span>
      </label>
      <button type="submit" class="flex items-center justify-center gap-2 min-h-11 mt-1 rounded-md cursor-pointer bg-tlf12-btn border border-tlf12-prompt text-tlf12-prompt text-[14px] font-bold tracking-wide transition-colors duration-150 hover:bg-tlf12-btnhover focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf12-prompt"><span aria-hidden="true">&rarr;</span> ./authenticate</button>
      <p class="text-[12px] text-tlf12-mut">Need access? <a href="#" class="text-tlf12-caret no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf12-caret">request an account</a></p>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf12-stage: #07090c;
  --color-tlf12-stage: oklch(0.13 0.008 250);
  --color-tlf12-card: #0d1117;
  --color-tlf12-card: oklch(0.17 0.01 250);
  --color-tlf12-bar: #151a21;
  --color-tlf12-bar: oklch(0.21 0.01 250);
  --color-tlf12-edge: #232a34;
  --color-tlf12-edge: oklch(0.27 0.012 250);
  --color-tlf12-btn: #101820;
  --color-tlf12-btn: oklch(0.19 0.015 160 / 0.6);
  --color-tlf12-btnhover: #16251d;
  --color-tlf12-btnhover: oklch(0.24 0.04 150 / 0.7);
  --color-tlf12-ink: #e8edf5;
  --color-tlf12-ink: oklch(0.94 0.008 250);
  --color-tlf12-label: #b8c1cf;
  --color-tlf12-label: oklch(0.81 0.015 250);
  --color-tlf12-mut: #9aa4b4;
  --color-tlf12-mut: oklch(0.71 0.018 250);
  --color-tlf12-ph: #6f7a8b;
  --color-tlf12-ph: oklch(0.57 0.02 250);
  --color-tlf12-prompt: #5fd98f;
  --color-tlf12-prompt: oklch(0.78 0.16 145);
  --color-tlf12-caret: #f0b74d;
  --color-tlf12-caret: oklch(0.8 0.15 80);
  --color-tlf12-dot1: #ef6a5e;
  --color-tlf12-dot1: oklch(0.68 0.18 25);
  --color-tlf12-dot2: #f0b74d;
  --color-tlf12-dot2: oklch(0.8 0.15 80);
  --color-tlf12-dot3: #5fd98f;
  --color-tlf12-dot3: oklch(0.78 0.16 145);
  --font-tlf12-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  --animate-tlf12-blink: tlf-12-blink 1s steps(1, end) infinite;
}

@keyframes tlf-12-blink {
  0%,
    50% {
    opacity: 1;
  }

  50.01%,
    100% {
    opacity: 0;
  }
}

.tlf-12 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
```
