---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-conic-border-beam-floating-label/"
title: "Tailwind Conic Border-Beam Floating Label (@property Animation)"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "A comet of light orbits the field's border while the label floats into a glowing chip."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Conic Border-Beam Floating Label (@property Animation)
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-conic-border-beam-floating-label/

A comet of light orbits the field's border while the label floats into a glowing chip. The beam is a before: layer painting bg-[conic-gradient(from_var(--tfl03-a),…)]; the @property registration that makes the angle animatable is the one rule that stays CSS. The orbit runs only under focus-within: — zero idle cost.
## HTML
```html
<section class="tfl-03 w-full min-h-svh grid place-items-center bg-tfl03-bg bg-[radial-gradient(60%_50%_at_50%_0%,var(--color-tfl03-glow),transparent_70%)] px-5 py-12 font-tfl03-sans" aria-label="Conic border beam floating label demo">
  <form class="flex w-full max-w-[380px] flex-col gap-6 rounded-3xl border border-tfl03-edge bg-tfl03-card p-8 shadow-[0_30px_80px_-40px_oklch(0_0_0/0.9)]" novalidate>
    <div class="grid gap-1.5">
      <h3 class="text-2xl font-extrabold tracking-[-0.02em] text-tfl03-ink">Access the beta</h3>
      <p class="text-sm text-tfl03-mut">Invite codes are case-insensitive.</p>
    </div>
    <div class="relative rounded-[13px] before:pointer-events-none before:absolute before:-inset-[1.5px] before:rounded-[14px] before:bg-[conic-gradient(from_var(--tfl03-a),transparent_0deg_300deg,var(--color-tfl03-acc)_330deg,transparent_360deg)] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] focus-within:before:opacity-100 focus-within:before:animate-tfl03-orbit motion-reduce:before:bg-tfl03-acc motion-reduce:focus-within:before:animate-none">
      <input class="peer relative z-[1] h-14 w-full rounded-xl border-[1.5px] border-tfl03-line bg-tfl03-field px-4 pt-[22px] pb-1.5 text-base text-tfl03-ink outline-hidden transition-[border-color] duration-200 hover:border-tfl03-line-hover focus:border-transparent" type="email" id="tfl-03-mail" name="email" placeholder=" " autocomplete="email">
      <label class="pointer-events-none absolute left-4 top-1/2 z-[2] -ml-[9px] origin-left -translate-y-1/2 rounded-md px-[9px] py-0.5 text-base text-tfl03-mut transition-[translate,scale,color,background-color,box-shadow] duration-[280ms] ease-[cubic-bezier(.3,1.3,.4,1)] peer-focus:translate-y-[calc(-50%_-_14px)] peer-focus:scale-74 peer-focus:bg-tfl03-bg peer-focus:text-tfl03-acc peer-focus:shadow-[0_0_16px_-2px_oklch(0.78_0.14_190/0.45)] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_14px)] peer-[:not(:placeholder-shown)]:scale-74 peer-[:not(:placeholder-shown)]:bg-tfl03-bg motion-reduce:transition-none" for="tfl-03-mail">Work email</label>
    </div>
    <div class="relative rounded-[13px] before:pointer-events-none before:absolute before:-inset-[1.5px] before:rounded-[14px] before:bg-[conic-gradient(from_var(--tfl03-a),transparent_0deg_300deg,var(--color-tfl03-acc)_330deg,transparent_360deg)] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] focus-within:before:opacity-100 focus-within:before:animate-tfl03-orbit motion-reduce:before:bg-tfl03-acc motion-reduce:focus-within:before:animate-none">
      <input class="peer relative z-[1] h-14 w-full rounded-xl border-[1.5px] border-tfl03-line bg-tfl03-field px-4 pt-[22px] pb-1.5 font-tfl03-mono text-base uppercase tracking-[0.18em] text-tfl03-ink outline-hidden transition-[border-color] duration-200 hover:border-tfl03-line-hover focus:border-transparent" type="text" id="tfl-03-key" name="invite" placeholder=" " autocomplete="off" autocapitalize="characters" spellcheck="false">
      <label class="pointer-events-none absolute left-4 top-1/2 z-[2] -ml-[9px] origin-left -translate-y-1/2 rounded-md px-[9px] py-0.5 text-base text-tfl03-mut transition-[translate,scale,color,background-color,box-shadow] duration-[280ms] ease-[cubic-bezier(.3,1.3,.4,1)] peer-focus:translate-y-[calc(-50%_-_14px)] peer-focus:scale-74 peer-focus:bg-tfl03-bg peer-focus:text-tfl03-acc peer-focus:shadow-[0_0_16px_-2px_oklch(0.78_0.14_190/0.45)] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_14px)] peer-[:not(:placeholder-shown)]:scale-74 peer-[:not(:placeholder-shown)]:bg-tfl03-bg motion-reduce:transition-none" for="tfl-03-key">Invite code</label>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-tfl03-acc text-[15px] font-extrabold text-tfl03-on-acc transition-[filter,box-shadow,scale] duration-200 hover:brightness-110 hover:shadow-[0_0_28px_-6px_var(--color-tfl03-acc)] active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl03-acc/60" type="button">Unlock access</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";
/* The one rule utilities cannot express: register the angle so the conic gradient interpolates. */

@property --tfl03-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tfl03-bg: #0a0d12;
  --color-tfl03-bg: oklch(0.15 0.01 250);
  --color-tfl03-glow: #0f2a30;
  --color-tfl03-glow: oklch(0.26 0.04 200);
  --color-tfl03-card: #11151d;
  --color-tfl03-card: oklch(0.19 0.014 255);
  --color-tfl03-edge: #1f2633;
  --color-tfl03-edge: oklch(0.26 0.02 255);
  --color-tfl03-field: #0d1117;
  --color-tfl03-field: oklch(0.17 0.012 255);
  --color-tfl03-line: #273042;
  --color-tfl03-line: oklch(0.3 0.03 260);
  --color-tfl03-line-hover: #36425a;
  --color-tfl03-line-hover: oklch(0.37 0.04 260);
  --color-tfl03-ink: #e8eef5;
  --color-tfl03-ink: oklch(0.94 0.01 250);
  --color-tfl03-mut: #909bb3;
  --color-tfl03-mut: oklch(0.69 0.03 260);
  --color-tfl03-acc: #36d0d6;
  --color-tfl03-acc: oklch(0.78 0.14 195);
  --color-tfl03-on-acc: #04252a;
  --color-tfl03-on-acc: oklch(0.24 0.04 200);
  --font-tfl03-sans: 'Geist', system-ui, sans-serif;
  --font-tfl03-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tfl03-orbit: tfl03-orbit 2.6s linear infinite;

  @keyframes tfl03-orbit {
    to {
      --tfl03-a: 360deg;
    }
  }
}

.tfl-03 {
  width: 100%;
  min-height: 100svh;
}
```
