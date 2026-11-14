---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-bakelite-radio-dial-toggle-button/"
title: "Tailwind Bakelite Radio Dial Toggle Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A bakelite rotary switch that turns 132° from OFF to ON, with a knurled grip, a chamfered pointer, engraved ticks around the bezel, and a warm indicator lamp…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bakelite Radio Dial Toggle Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-bakelite-radio-dial-toggle-button/

A bakelite rotary switch that turns 132° from OFF to ON, with a knurled grip, a chamfered pointer, engraved ticks around the bezel, and a warm indicator lamp that fades up as the contact closes. A checkbox with role="switch" holds the state.
## HTML
```html
<div class="tb-44 w-full min-h-svh grid place-items-center font-tb44-sans p-[clamp(1.5rem,6vw,4rem)]">
  <label class="group relative block cursor-pointer [-webkit-tap-highlight-color:transparent]">
    <input type="checkbox" role="switch" aria-label="Power" class="sr-only">
    <span aria-hidden="true" class="tb-44__plate relative grid place-items-center size-38 rounded-full shadow-[inset_0_2px_4px_#ffffff1a,inset_0_-3px_8px_#000000b3,0_16px_26px_-12px_#000000d9] group-has-focus-visible:outline-2 group-has-focus-visible:outline-offset-[5px] group-has-focus-visible:outline-tb44-lamp">
      <span class="absolute inset-0 rounded-full opacity-65 bg-[repeating-conic-gradient(from_-66deg,var(--color-tb44-tick)_0_0.9deg,transparent_0.9deg_11deg)] [mask-image:radial-gradient(farthest-side,transparent_76%,#000_78%)]"></span>
      <span class="absolute left-1.5 bottom-6 text-[0.6875rem] tracking-[0.16em] uppercase text-tb44-ink opacity-100 -rotate-[24deg] transition-opacity duration-300 group-has-checked:opacity-60 motion-reduce:transition-none">Off</span>
      <span class="absolute right-1.5 bottom-6 text-[0.6875rem] tracking-[0.16em] uppercase text-tb44-ink opacity-60 rotate-[24deg] transition-[opacity,color] duration-300 group-has-checked:opacity-100 group-has-checked:text-tb44-lamp motion-reduce:transition-none">On</span>
      <span class="absolute top-3.5 size-2 rounded-full bg-tb44-lamp opacity-[0.18] shadow-[0_0_6px_var(--color-tb44-lamp),0_0_14px_var(--color-tb44-lamp-55)] transition-opacity duration-[350ms] group-has-checked:opacity-100 motion-reduce:transition-none"></span>
      <span class="tb-44__knob relative w-[62%] h-[62%] rounded-full -rotate-[66deg] shadow-[inset_0_2px_3px_#ffffff38,inset_0_-3px_6px_#00000099,0_6px_12px_-4px_#000000cc] transition-[rotate,filter] duration-700 ease-tb44-spring group-hover:brightness-110 group-active:scale-[0.97] group-has-checked:rotate-[66deg] motion-reduce:transition-none">
        <span class="absolute inset-0 rounded-full bg-[repeating-conic-gradient(from_0deg,#ffffff24_0_1.6deg,#00000038_1.6deg_3.4deg)] [mask-image:radial-gradient(farthest-side,transparent_78%,#000_80%)]"></span>
        <span class="absolute top-[9%] left-1/2 w-[0.28rem] h-[34%] -ml-[0.14rem] rounded-full bg-[linear-gradient(180deg,var(--color-tb44-tick),var(--color-tb44-tick-lo))] shadow-[0_0_4px_#00000099]"></span>
      </span>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb44-bg: #1b1512;
  --color-tb44-bg: oklch(0.2 0.02 50);
  --color-tb44-plate: #241c17;
  --color-tb44-plate: oklch(0.24 0.025 50);
  --color-tb44-bake: #3a2418;
  --color-tb44-bake: oklch(0.3 0.05 50);
  --color-tb44-bake-hi: #5a3a26;
  --color-tb44-bake-hi: oklch(0.4 0.06 52);
  --color-tb44-bake-lo: #1d120b;
  --color-tb44-bake-lo: oklch(0.18 0.03 48);
  --color-tb44-tick: #c9b48d;
  --color-tb44-tick: oklch(0.78 0.04 82);
  --color-tb44-tick-lo: #8a7a59;
  --color-tb44-tick-lo: oklch(0.56 0.04 82);
  --color-tb44-ink: #e6d7b8;
  --color-tb44-ink: oklch(0.88 0.04 85);
  --color-tb44-lamp: #ff9f43;
  --color-tb44-lamp: oklch(0.78 0.16 62);
  --color-tb44-lamp-55: #ff9f438c;
  --color-tb44-lamp-55: oklch(0.78 0.16 62 / 0.55);
  --font-tb44-sans: "Oswald", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb44-spring: cubic-bezier(0.16, 1, 0.3, 1);
}

@supports (transition-timing-function: linear(0, 1)) {
  @theme {
    --ease-tb44-spring: linear(0, 0.36 7%, 0.8 15%, 1.05 23%, 1.09 29%, 1.02 39%, 1 54%, 1);
  }
}

.tb-44 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(30rem 20rem at 50% 44%, #2b211a, transparent 74%), var(--color-tb44-bg);
}

.tb-44__plate {
  background: radial-gradient(circle at 40% 30%, rgba(255,255,255,.08), transparent 60%), linear-gradient(160deg, #2e241d, var(--color-tb44-plate));
}
/* BAKELITE: mottled two-blotch overlay + specular, which is what separates it
   from plain dark plastic. */

.tb-44__knob {
  background: radial-gradient(circle at 36% 28%, var(--color-tb44-bake-hi), transparent 58%), radial-gradient(1.4rem 1rem at 70% 74%, rgba(0,0,0,.4), transparent 70%), linear-gradient(155deg, var(--color-tb44-bake), var(--color-tb44-bake-lo));
}
/* Safari ≤15.3 shims for the two annulus masks. */

.tb-44__plate > span:first-child {
  -webkit-mask-image: radial-gradient(farthest-side, transparent 76%, #000 78%);
}

.tb-44__knob > span:first-child {
  -webkit-mask-image: radial-gradient(farthest-side, transparent 78%, #000 80%);
}

@media (prefers-color-scheme: light) {
  .tb-44:not([data-theme="dark"]) {
    --color-tb44-bg: oklch(0.25 0.022 50);
  }
}

.tb-44[data-theme="light"] {
  --color-tb44-bg: oklch(0.25 0.022 50);
}

@media (forced-colors: active) {
  .tb-44__plate,
    .tb-44__knob {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-44__plate > span:first-child,
    .tb-44__knob > span:first-child {
    display: none;
  }

  .tb-44__knob > span:last-child {
    background: ButtonText;
  }
}
```
