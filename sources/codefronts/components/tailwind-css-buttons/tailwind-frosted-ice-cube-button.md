---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-frosted-ice-cube-button/"
title: "Tailwind Frosted Ice Cube Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Real frosted glass over a photograph: backdrop-blur and backdrop-saturate handle the refraction, a bright inner rim catches the light on two edges only,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Frosted Ice Cube Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-frosted-ice-cube-button/

Real frosted glass over a photograph: backdrop-blur and backdrop-saturate handle the refraction, a bright inner rim catches the light on two edges only, frost collects in the corners, and pressing sends a hairline crack across the face.
## HTML
```html
<div class="tb-23 w-full min-h-svh bg-tb23-fallback font-tb23-sans antialiased">
  <div class="relative min-h-svh grid place-items-center overflow-hidden p-[clamp(1.5rem,6vw,4rem)]">
    <img src="https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=1600&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="1600" height="1000" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover bg-tb23-fallback saturate-105 brightness-90">
    <button type="button" class="group relative overflow-hidden z-10 cursor-pointer min-h-15 px-8 border-0 rounded-[1.1rem] text-base font-semibold tracking-[-0.005em] text-tb23-ink bg-[linear-gradient(150deg,rgba(255,255,255,0.30),rgba(255,255,255,0.08))] [text-shadow:0_1px_12px_rgba(4,20,32,0.65)] backdrop-blur-[16px] backdrop-saturate-150 backdrop-brightness-105 shadow-[inset_1px_1px_0_rgba(255,255,255,0.7),inset_-1px_-1px_0_rgba(255,255,255,0.18),inset_0_0_24px_rgba(255,255,255,0.14),0_20px_44px_-20px_rgba(4,16,26,0.75)] transition-[translate,box-shadow,scale] duration-300 ease-tb23-out hover:-translate-y-0.5 hover:shadow-[inset_1px_1px_0_rgba(255,255,255,0.85),inset_-1px_-1px_0_rgba(255,255,255,0.22),inset_0_0_30px_rgba(255,255,255,0.2),0_26px_50px_-20px_rgba(4,16,26,0.8)] active:scale-[0.985] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white/90 supports-[not_(backdrop-filter:blur(4px))]:bg-tb23-solid supports-[not_(backdrop-filter:blur(4px))]:text-tb23-ink-solid supports-[not_(backdrop-filter:blur(4px))]:[text-shadow:none] motion-reduce:transition-none">
      <span aria-hidden="true" class="tb-23__frost absolute inset-0 z-10 pointer-events-none opacity-85 transition-opacity duration-[350ms] group-hover:opacity-100 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="absolute inset-0 z-20 pointer-events-none opacity-0 bg-white/95 [clip-path:polygon(0_52%,18%_44%,26%_58%,44%_40%,58%_56%,72%_38%,86%_52%,100%_44%,100%_46%,86%_54%,72%_41%,58%_59%,44%_43%,26%_61%,18%_47%,0_54%)] group-active:animate-tb23-crack motion-reduce:hidden"></span>
      <span class="relative z-30 grid grid-flow-col items-center gap-2">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" class="size-[1.15rem]"><path d="M12 3v18M4 7.5l16 9M20 7.5l-16 9"/></svg>
        <span>Chill mode</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb23-fallback: #123044;
  --color-tb23-fallback: oklch(0.32 0.05 235);
  --color-tb23-ink: #f2fbff;
  --color-tb23-ink-solid: #0b2434;
  --color-tb23-ink-solid: oklch(0.25 0.04 235);
  --color-tb23-solid: #d9ecf7b3;
  --color-tb23-solid: oklch(0.92 0.02 225 / 0.7);
  --font-tb23-sans: "Outfit", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb23-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb23-crack: tb-23-crack 0.5s ease-out;
}

@keyframes tb-23-crack {
  0% {
    opacity: 0;
    scale: 0.4 1;
  }

  30% {
    opacity: 0.9;
  }

  100% {
    opacity: 0;
    scale: 1 1;
  }
}

.tb-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
/* FROST BLOOM: two large soft corner gradients + a fine speckle. Ice reads as
   uneven — a uniform white overlay always looks like plastic. */

.tb-23__frost {
  background: radial-gradient(4rem 3rem at 8% 4%, rgba(255,255,255,.42), transparent 70%), radial-gradient(5rem 3.5rem at 96% 100%, rgba(255,255,255,.34), transparent 72%), radial-gradient(.06rem .06rem at 22% 62%, rgba(255,255,255,.9) 99%, transparent), radial-gradient(.05rem .05rem at 71% 28%, rgba(255,255,255,.8) 99%, transparent);
  background-size: 100% 100%, 100% 100%, 9px 9px, 14px 14px;
}

@media (forced-colors: active) {
  .tb-23 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
    box-shadow: none;
    text-shadow: none;
  }

  .tb-23 button span[aria-hidden] {
    display: none;
  }
}
```
