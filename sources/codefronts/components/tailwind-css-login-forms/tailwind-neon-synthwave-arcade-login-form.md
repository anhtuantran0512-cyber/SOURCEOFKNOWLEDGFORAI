---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-neon-synthwave-arcade-login-form/"
title: "Tailwind Neon Synthwave Arcade Login Form"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A dark-mode-first retro-arcade login glowing with disciplined neon: layered text shadows, a tight box glow, and a perspective grid receding into the floor."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Synthwave Arcade Login Form
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-neon-synthwave-arcade-login-form/

A dark-mode-first retro-arcade login glowing with disciplined neon: layered text shadows, a tight box glow, and a perspective grid receding into the floor. The discipline is the point &mdash; the glow lives on borders, headings and labels, never on the characters a user has to read.
## HTML
```html
<section class="tlf-09 relative w-full min-h-svh grid place-items-center overflow-hidden bg-tlf09-stage font-tlf09-body p-6">
  <div aria-hidden="true" class="absolute -left-1/2 -right-1/2 -bottom-[10%] h-[70%] bg-[linear-gradient(oklch(0.72_0.16_330/0.35)_1px,transparent_1px),linear-gradient(90deg,oklch(0.72_0.16_330/0.35)_1px,transparent_1px)] bg-[length:44px_44px] [transform:perspective(300px)_rotateX(62deg)] [mask-image:linear-gradient(black,transparent)]"></div>
  <form novalidate class="relative z-1 w-[min(380px,100%)] flex flex-col gap-4 p-8 rounded-2xl bg-tlf09-card border-[1.5px] border-tlf09-neon text-tlf09-ink shadow-[0_0_18px_oklch(0.72_0.2_330/0.5),inset_0_0_22px_oklch(0.72_0.2_330/0.12)]">
    <h1 class="text-center text-2xl font-extrabold tracking-[0.08em] text-white font-tlf09-display [text-shadow:0_0_5px_var(--color-tlf09-neon),0_0_16px_var(--color-tlf09-neon)]">PLAYER LOGIN</h1>
    <label class="flex flex-col gap-1.5"><span class="text-[11px] font-bold tracking-[0.12em] uppercase text-tlf09-neon2 [text-shadow:0_0_8px_oklch(0.8_0.14_200/0.6)]">Username</span>
      <input type="text" autocomplete="username" placeholder="neo_runner" required class="h-12 px-3.5 rounded-md text-[15px] text-white bg-tlf09-field border-[1.5px] border-tlf09-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf09-ph focus-visible:outline-none focus-visible:border-tlf09-neon focus-visible:shadow-[0_0_0_3px_oklch(0.72_0.2_330/0.35),0_0_14px_oklch(0.72_0.2_330/0.5)]"></label>
    <label class="flex flex-col gap-1.5"><span class="text-[11px] font-bold tracking-[0.12em] uppercase text-tlf09-neon2 [text-shadow:0_0_8px_oklch(0.8_0.14_200/0.6)]">Password</span>
      <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-md text-[15px] text-white bg-tlf09-field border-[1.5px] border-tlf09-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf09-ph focus-visible:outline-none focus-visible:border-tlf09-neon focus-visible:shadow-[0_0_0_3px_oklch(0.72_0.2_330/0.35),0_0_14px_oklch(0.72_0.2_330/0.5)]"></label>
    <button type="submit" class="mt-1 h-12 rounded-md cursor-pointer bg-transparent border-[1.5px] border-tlf09-neon text-white text-[15px] font-extrabold tracking-[0.1em] font-tlf09-display [text-shadow:0_0_8px_var(--color-tlf09-neon)] shadow-[0_0_12px_oklch(0.72_0.2_330/0.4)] transition-[background-color,box-shadow,scale] duration-150 hover:bg-tlf09-neonwash hover:shadow-[0_0_22px_oklch(0.72_0.2_330/0.6)] active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tlf09-ring motion-reduce:transition-[background-color,box-shadow] motion-reduce:active:scale-100">ENTER</button>
    <p class="text-center text-[12.5px]"><a href="#" class="text-tlf09-neon2 no-underline [text-shadow:0_0_8px_oklch(0.8_0.14_200/0.5)] hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf09-neon2">Insert coin &mdash; sign up</a></p>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf09-stage: #0a0713;
  --color-tlf09-stage: oklch(0.12 0.03 300);
  --color-tlf09-card: #120b22;
  --color-tlf09-card: oklch(0.17 0.05 300);
  --color-tlf09-field: #0c0718;
  --color-tlf09-field: oklch(0.13 0.035 300);
  --color-tlf09-fieldedge: #6b4f8a;
  --color-tlf09-fieldedge: oklch(0.5 0.08 320);
  --color-tlf09-ink: #eeeaf5;
  --color-tlf09-ink: oklch(0.94 0.01 300);
  --color-tlf09-ph: #8a7ba8;
  --color-tlf09-ph: oklch(0.63 0.05 300);
  --color-tlf09-neon: #e964c4;
  --color-tlf09-neon: oklch(0.72 0.2 330);
  --color-tlf09-neon2: #5fd4e8;
  --color-tlf09-neon2: oklch(0.8 0.14 200);
  --color-tlf09-neonwash: #e964c4;
  --color-tlf09-neonwash: oklch(0.72 0.2 330 / 0.16);
  --color-tlf09-ring: #f09ad9;
  --color-tlf09-ring: oklch(0.72 0.2 330 / 0.6);
  --font-tlf09-display: 'Orbitron', system-ui, sans-serif;
  --font-tlf09-body: 'Rajdhani', system-ui, sans-serif;
}

.tlf-09 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
/* Safari mask prefix for the receding grid. */

.tlf-09 > div[aria-hidden] {
  -webkit-mask-image: linear-gradient(black, transparent);
}
```
