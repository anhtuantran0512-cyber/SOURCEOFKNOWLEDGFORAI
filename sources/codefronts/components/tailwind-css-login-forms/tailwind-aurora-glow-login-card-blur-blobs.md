---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-aurora-glow-login-card-blur-blobs/"
title: "Tailwind Aurora Glow Login Card with Drifting Blur Blobs"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The indie-startup landing look: two big blurred colour fields drift behind a translucent login card like a slow aurora."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Aurora Glow Login Card with Drifting Blur Blobs
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-aurora-glow-login-card-blur-blobs/

The indie-startup landing look: two big blurred colour fields drift behind a translucent login card like a slow aurora. High aesthetic impact, engineered to stay smooth on mobile &mdash; only transform animates, so the expensive blur is rasterised once and cheaply moved.
## HTML
```html
<section class="tlf-08 relative w-full min-h-svh grid place-items-center overflow-hidden bg-tlf08-stage font-tlf08-sans p-6">
  <div aria-hidden="true" class="absolute -inset-[20%] z-0">
    <div class="absolute left-[2%] top-[5%] w-3/5 h-3/5 rounded-full opacity-85 blur-[90px] will-change-transform animate-tlf08-a bg-[radial-gradient(circle,oklch(0.7_0.2_300),transparent_70%)] motion-reduce:animate-none"></div>
    <div class="absolute right-0 bottom-0 w-3/5 h-3/5 rounded-full opacity-85 blur-[90px] will-change-transform animate-tlf08-b bg-[radial-gradient(circle,oklch(0.72_0.19_210),transparent_70%)] motion-reduce:animate-none"></div>
  </div>
  <form novalidate class="relative z-1 w-[min(380px,100%)] flex flex-col gap-4 p-8 rounded-[20px] bg-tlf08-card backdrop-blur-[6px] border border-white/10 text-tlf08-ink shadow-[0_30px_80px_-40px_black]">
    <h1 class="text-[26px] font-bold tracking-tight">Welcome back</h1>
    <p class="-mt-2.5 mb-1 text-sm text-tlf08-mut">Sign in to keep building.</p>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf08-label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-[14px] text-[15px] text-tlf08-ink bg-white/5 border-[1.5px] border-white/15 transition-[border-color,box-shadow] duration-150 placeholder:text-tlf08-ph focus-visible:outline-none focus-visible:border-tlf08-acc focus-visible:ring-4 focus-visible:ring-tlf08-halo"></label>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf08-label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-[14px] text-[15px] text-tlf08-ink bg-white/5 border-[1.5px] border-white/15 transition-[border-color,box-shadow] duration-150 placeholder:text-tlf08-ph focus-visible:outline-none focus-visible:border-tlf08-acc focus-visible:ring-4 focus-visible:ring-tlf08-halo"></label>
    <button type="submit" class="mt-1 h-12 rounded-[14px] border-0 cursor-pointer text-white text-[15px] font-semibold bg-[linear-gradient(90deg,oklch(0.6_0.2_300),oklch(0.6_0.19_250))] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tlf08-ring motion-reduce:transition-none motion-reduce:active:scale-100">Sign in</button>
    <p class="text-center text-[13px]"><a href="#" class="text-tlf08-link no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf08-link">Forgot password?</a></p>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf08-stage: #0a0a14;
  --color-tlf08-stage: oklch(0.13 0.02 280);
  --color-tlf08-card: #121222;
  --color-tlf08-card: oklch(0.19 0.025 285 / 0.78);
  --color-tlf08-ink: #eef0fa;
  --color-tlf08-ink: oklch(0.96 0.008 280);
  --color-tlf08-label: #cfd2e6;
  --color-tlf08-label: oklch(0.87 0.014 280);
  --color-tlf08-mut: #b3b7cc;
  --color-tlf08-mut: oklch(0.78 0.018 280);
  --color-tlf08-ph: #8d92ab;
  --color-tlf08-ph: oklch(0.65 0.02 280);
  --color-tlf08-acc: #b37cf0;
  --color-tlf08-acc: oklch(0.7 0.19 300);
  --color-tlf08-halo: #d7bcf7;
  --color-tlf08-halo: oklch(0.7 0.19 300 / 0.28);
  --color-tlf08-ring: #cba6f5;
  --color-tlf08-ring: oklch(0.7 0.19 300 / 0.6);
  --color-tlf08-link: #d3c6fb;
  --color-tlf08-link: oklch(0.85 0.09 295);
  --font-tlf08-sans: 'Sora', system-ui, sans-serif;
  --animate-tlf08-a: tlf-08-a 16s ease-in-out infinite;
  --animate-tlf08-b: tlf-08-b 20s ease-in-out infinite;
}

@keyframes tlf-08-a {
  0%,
    100% {
    transform: translate(0, 0) rotate(0deg);
  }

  50% {
    transform: translate(30%, 20%) rotate(40deg);
  }
}

@keyframes tlf-08-b {
  0%,
    100% {
    transform: translate(0, 0) rotate(0deg);
  }

  50% {
    transform: translate(-25%, -15%) rotate(-30deg);
  }
}

.tlf-08 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
/* Safari < 16.4 backdrop-filter prefix. */

.tlf-08 form {
  -webkit-backdrop-filter: blur(6px);
}
```
