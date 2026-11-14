---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-biometric-face-id-prompt-pulse-ripples/"
title: "Tailwind Biometric Face ID Prompt with Pulse Ripples"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A PWA-style face / touch-ID prompt: a large biometric glyph in a circular target with concentric ripples signalling that the app is listening."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Biometric Face ID Prompt with Pulse Ripples
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-biometric-face-id-prompt-pulse-ripples/

A PWA-style face / touch-ID prompt: a large biometric glyph in a circular target with concentric ripples signalling that the app is listening. The port's substantive point is not the animation &mdash; it is that the fallback link is mandatory, and the markup says so.
## HTML
```html
<section class="tlf-30 w-full min-h-svh grid place-items-center bg-tlf30-stage font-tlf30-sans p-6">
  <div class="w-[min(360px,100%)] p-9 text-center bg-tlf30-card border border-tlf30-edge rounded-[22px] text-tlf30-ink shadow-[0_30px_70px_-44px_black]">
    <h1 class="text-[22px] font-bold">Confirm it&rsquo;s you</h1>
    <p class="mt-1.5 mb-7 text-[13.5px]/[1.5] text-tlf30-mut">Use Face ID or your fingerprint to sign in.</p>
    <button type="button" aria-label="Authenticate with biometrics" class="relative grid place-items-center size-26 mx-auto mb-6 rounded-full border-0 cursor-pointer bg-tlf30-wash text-tlf30-acc transition-[background-color,scale] duration-150 hover:bg-tlf30-washhover active:scale-95 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tlf30-ring motion-reduce:transition-colors motion-reduce:active:scale-100">
      <span aria-hidden="true" class="absolute inset-0 rounded-full border-2 border-tlf30-acc opacity-0 animate-tlf30-pulse motion-reduce:animate-none motion-reduce:opacity-40 motion-reduce:-inset-1.5"></span>
      <span aria-hidden="true" class="absolute inset-0 rounded-full border-2 border-tlf30-acc opacity-0 animate-tlf30-pulse [animation-delay:1.2s] motion-reduce:hidden"></span>
      <svg viewBox="0 0 24 24" aria-hidden="true" class="relative size-13"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" d="M5 11a7 7 0 0 1 14 0M7.5 12.5a4.5 4.5 0 0 1 9 0v1.5M12 12v4M9.5 15v1.5M14.5 14.5V17M4.5 14v1"></path></svg>
    </button>
    <p role="status" aria-live="polite" class="mb-5 text-[12.5px] text-tlf30-mut">Waiting for authentication&hellip;</p>
    <a href="#" class="inline-grid place-items-center min-h-11 px-3 text-[13.5px] font-semibold text-tlf30-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf30-acc">Use passcode instead</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf30-stage: #0f1220;
  --color-tlf30-stage: oklch(0.17 0.025 275);
  --color-tlf30-card: #171a2b;
  --color-tlf30-card: oklch(0.22 0.025 275);
  --color-tlf30-edge: #2b3048;
  --color-tlf30-edge: oklch(0.29 0.028 275);
  --color-tlf30-ink: #e9ecf7;
  --color-tlf30-ink: oklch(0.94 0.01 275);
  --color-tlf30-mut: #a6adc6;
  --color-tlf30-mut: oklch(0.75 0.022 275);
  --color-tlf30-acc: #8ba4f5;
  --color-tlf30-acc: oklch(0.72 0.14 265);
  --color-tlf30-wash: #232a4a;
  --color-tlf30-wash: oklch(0.72 0.14 265 / 0.16);
  --color-tlf30-washhover: #2c3660;
  --color-tlf30-washhover: oklch(0.72 0.14 265 / 0.24);
  --color-tlf30-ring: #adbef8;
  --color-tlf30-ring: oklch(0.72 0.14 265 / 0.6);
  --font-tlf30-sans: 'Sora', system-ui, sans-serif;
  --animate-tlf30-pulse: tlf-30-pulse 2.4s ease-out infinite;
}

@keyframes tlf-30-pulse {
  0% {
    transform: scale(0.7);
    opacity: 0.7;
  }

  80%,
    100% {
    transform: scale(1.5);
    opacity: 0;
  }
}

.tlf-30 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
```
