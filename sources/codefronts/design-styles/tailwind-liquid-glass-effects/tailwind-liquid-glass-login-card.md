---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-login-card/"
title: "Tailwind Liquid Glass Login Card"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "An auth screen where the glass has something worth refracting: a mesh of radial-gradient blobs drifting slowly behind the card, so the blur visibly shifts…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Login Card
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-login-card/

An auth screen where the glass has something worth refracting: a mesh of radial-gradient blobs drifting slowly behind the card, so the blur visibly shifts colour in real time. Utilities only &mdash; the whole 'wow' is a keyframe on a background layer and four glass utilities on a form.
## HTML
```html
<section class="lgt-17 relative grid w-full min-h-svh place-items-center overflow-hidden bg-lgt17-bg p-15 font-lgt17-sans" aria-label="Tailwind liquid glass login card">
  <div aria-hidden="true" class="pointer-events-none absolute -inset-[20%] animate-lgt17-drift saturate-140 [background:radial-gradient(40%_40%_at_20%_30%,oklch(0.6_0.22_300),transparent_70%),radial-gradient(40%_40%_at_80%_20%,oklch(0.62_0.2_210),transparent_70%),radial-gradient(45%_45%_at_70%_80%,oklch(0.64_0.2_340),transparent_70%),radial-gradient(40%_40%_at_25%_85%,oklch(0.6_0.2_40),transparent_70%)] motion-reduce:animate-none"></div>

  <form novalidate class="relative z-2 w-[min(380px,92vw)] rounded-[26px] border border-white/32 bg-white/12 p-8.5 text-white backdrop-blur-[22px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_40px_80px_-34px_rgba(0,0,0,.7)]">
    <h3 class="text-[26px] font-extrabold tracking-[-0.02em]">Welcome back</h3>
    <p class="mt-1.5 mb-6 text-sm text-white/75">Sign in to your Lumen workspace</p>

    <div class="mb-4 focus-within:[&amp;_input]:border-lgt17-accent focus-within:[&amp;_input]:bg-white/14 focus-within:[&amp;_input]:shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_0_0_3px_color-mix(in_oklab,var(--color-lgt17-accent)_40%,transparent)]">
      <label for="lgt-17-email" class="mb-1.75 block text-xs font-semibold uppercase tracking-[0.05em] text-white/70">Email</label>
      <input id="lgt-17-email" type="email" autocomplete="email" placeholder="[email protected]" class="w-full rounded-[13px] border border-white/25 bg-white/8 px-3.75 py-3.25 text-[15px] text-white outline-none backdrop-blur-[6px] shadow-[inset_0_1px_0_rgba(255,255,255,.3)] transition-[border-color,box-shadow,background-color] duration-200 placeholder:text-white/50">
    </div>

    <div class="mb-4 focus-within:[&amp;_input]:border-lgt17-accent focus-within:[&amp;_input]:bg-white/14 focus-within:[&amp;_input]:shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_0_0_3px_color-mix(in_oklab,var(--color-lgt17-accent)_40%,transparent)]">
      <label for="lgt-17-pass" class="mb-1.75 block text-xs font-semibold uppercase tracking-[0.05em] text-white/70">Password</label>
      <input id="lgt-17-pass" type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" class="w-full rounded-[13px] border border-white/25 bg-white/8 px-3.75 py-3.25 text-[15px] text-white outline-none backdrop-blur-[6px] shadow-[inset_0_1px_0_rgba(255,255,255,.3)] transition-[border-color,box-shadow,background-color] duration-200 placeholder:text-white/50">
    </div>

    <div class="mt-1 mb-5 flex items-center justify-between text-[13px]">
      <label class="flex cursor-pointer items-center gap-1.75 text-white/80"><input type="checkbox" class="accent-lgt17-accent"> Remember me</label>
      <a href="#lgt-17" class="font-semibold text-lgt17-link no-underline hover:underline focus-visible:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Forgot?</a>
    </div>

    <button type="submit" class="group relative w-full cursor-pointer overflow-hidden rounded-[13px] border border-lgt17-accent/60 bg-linear-to-b from-lgt17-accent-top to-lgt17-accent py-3.5 text-base font-bold text-white shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_14px_30px_-16px_rgba(0,0,0,.6)] transition-transform duration-150 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white after:pointer-events-none after:absolute after:inset-y-0 after:left-0 after:w-1/2 after:[background:linear-gradient(105deg,transparent,rgba(255,255,255,.5),transparent)] after:[transform:translateX(-200%)_skewX(-14deg)] after:transition-transform after:duration-700 group-hover:after:[transform:translateX(320%)_skewX(-14deg)] group-focus-visible:after:[transform:translateX(320%)_skewX(-14deg)] motion-reduce:transition-none motion-reduce:after:hidden">Sign in</button>

    <p class="mt-4.5 text-center text-[13px] text-white/75">New here? <a href="#lgt-17" class="font-semibold text-lgt17-link no-underline hover:underline focus-visible:underline">Create an account</a></p>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt17-bg: #0c0a18;
  --color-lgt17-accent: #7c5cf0;
  --color-lgt17-accent: oklch(0.66 0.19 285);
  --color-lgt17-accent-top: #9b83f6;
  --color-lgt17-accent-top: oklch(0.72 0.16 285);
  --color-lgt17-link: #c4b5fd;
  --color-lgt17-link: oklch(0.82 0.12 285);
  --font-lgt17-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt17-drift: lgt-17-drift 20s ease-in-out infinite alternate;
}

@keyframes lgt-17-drift {
  from {
    transform: translate(-4%, -3%) scale(1.05);
  }

  to {
    transform: translate(4%, 4%) scale(1.15);
  }
}
```
