---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-ios-26-floating-tab-bar/"
title: "Tailwind iOS 26 Floating Tab Bar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The iOS 26 bottom tab bar as a floating glass capsule, ported so the collapse is a state rather than a class."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind iOS 26 Floating Tab Bar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-ios-26-floating-tab-bar/

The iOS 26 bottom tab bar as a floating glass capsule, ported so the collapse is a state rather than a class. The scroll handler writes data-compact on the bar and nothing else; data-[compact=true]: retunes the bar's own padding while group-data-[compact=true]: reaches the labels two levels down. The frost recipe — translucent fill, hairline rim, inset specular, backdrop-blur-[24px] — is one class list you can read end to end.
## HTML
```html
<section class="nbtw-01 relative block w-full min-h-svh overflow-hidden font-nb01-sans bg-[conic-gradient(from_210deg_at_30%_20%,#5b8cff,#b06bff,#ff7ab0,#5b8cff)] bg-[length:200%_200%] animate-nb01-bg motion-reduce:animate-none" aria-label="iOS 26 floating tab bar demo">
  <div class="absolute inset-0 overflow-y-auto px-6 pt-8 pb-35 text-white" id="nbtw-01-scroll">
    <h2 class="text-[26px] font-extrabold tracking-[-0.02em] mb-3.5 [text-shadow:0_2px_12px_rgba(0,0,0,.3)]">Scroll me &darr;</h2>
    <p class="max-w-[44ch] mb-16 text-[15px] leading-[1.7] text-white/90 [text-shadow:0_1px_8px_rgba(0,0,0,.28)]">The floating tab bar shrinks to icons as you scroll down and springs back on scroll-up, idle or hover — the whole collapse is one <code>data-compact</code> attribute.</p>
    <p class="max-w-[44ch] mb-16 text-[15px] leading-[1.7] text-white/90 [text-shadow:0_1px_8px_rgba(0,0,0,.28)]">Keep scrolling to watch the glass capsule frost the content passing beneath it. The bar collapses on scroll-down, expands on scroll-up, and always expands after 600ms of idle so it stays reachable.</p>
    <p class="max-w-[44ch] mb-16 text-[15px] leading-[1.7] text-white/90 [text-shadow:0_1px_8px_rgba(0,0,0,.28)]">Every tab is a real link with a 44px hit target and an <code>aria-current</code> active state, and the active pill is styled from that attribute with <code>aria-[current=page]:</code>.</p>
    <p class="max-w-[44ch] mb-16 text-[15px] leading-[1.7] text-white/90 [text-shadow:0_1px_8px_rgba(0,0,0,.28)]">Labels stay in the DOM when collapsed — <code>group-data-[compact=true]:max-w-0</code> only clamps their width — so screen readers still announce them.</p>
    <p class="max-w-[44ch] mb-16 text-[15px] leading-[1.7] text-white/90 [text-shadow:0_1px_8px_rgba(0,0,0,.28)]">Hovering the bar or focusing any tab forces the expanded state, which is what keeps a keyboard user from being stranded in the icon-only bar.</p>
    <p class="max-w-[44ch] mb-16 text-[15px] leading-[1.7] text-white/90 [text-shadow:0_1px_8px_rgba(0,0,0,.28)]">All motion is padding, max-width, opacity and backdrop-filter — no layout thrashing on the page itself, INP-friendly, WCAG 2.2 compliant.</p>
    <p class="max-w-[44ch] mb-16 text-[15px] leading-[1.7] text-white/90 [text-shadow:0_1px_8px_rgba(0,0,0,.28)]">Keep going to see the bar frost this line…</p>
    <p class="max-w-[44ch] mb-16 text-[15px] leading-[1.7] text-white/90 [text-shadow:0_1px_8px_rgba(0,0,0,.28)]">…and this one too. That's it — scroll up to reset, or hover the bar to force it open.</p>
  </div>
  <nav class="group absolute left-1/2 bottom-[22px] -translate-x-1/2 flex gap-1.5 px-3.5 py-2.5 rounded-full isolate bg-[color-mix(in_oklab,white_16%,transparent)] border border-white/40 shadow-[inset_0_1px_0_rgba(255,255,255,.55),0_20px_44px_-20px_rgba(0,0,0,.6)] backdrop-blur-[24px] backdrop-saturate-[1.8] transition-[padding,gap] duration-[450ms] ease-nb01 data-[compact=true]:gap-0.5 data-[compact=true]:p-2 motion-reduce:transition-none" id="nbtw-01-bar" data-compact="false" aria-label="Primary">
    <a class="flex items-center gap-2 min-h-11 px-4 rounded-full no-underline text-white text-sm font-semibold transition-[background-color,transform] duration-200 hover:bg-white/15 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-nb01-accent aria-[current=page]:shadow-[0_6px_16px_-6px_color-mix(in_oklab,var(--color-nb01-accent)_70%,transparent)] aria-[current=page]:hover:bg-nb01-accent group-data-[compact=true]:px-3" href="#nbtw-01" aria-current="page" aria-label="Home">
      <span class="text-[19px] leading-none" aria-hidden="true">⌂</span>
      <span class="max-w-20 overflow-hidden whitespace-nowrap transition-[max-width,opacity] duration-[450ms] ease-nb01 group-data-[compact=true]:max-w-0 group-data-[compact=true]:opacity-0 motion-reduce:transition-none">Home</span>
    </a>
    <a class="flex items-center gap-2 min-h-11 px-4 rounded-full no-underline text-white text-sm font-semibold transition-[background-color,transform] duration-200 hover:bg-white/15 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 group-data-[compact=true]:px-3" href="#nbtw-01" aria-label="Search">
      <span class="text-[19px] leading-none" aria-hidden="true">⌕</span>
      <span class="max-w-20 overflow-hidden whitespace-nowrap transition-[max-width,opacity] duration-[450ms] ease-nb01 group-data-[compact=true]:max-w-0 group-data-[compact=true]:opacity-0 motion-reduce:transition-none">Search</span>
    </a>
    <a class="flex items-center gap-2 min-h-11 px-4 rounded-full no-underline text-white text-sm font-semibold transition-[background-color,transform] duration-200 hover:bg-white/15 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 group-data-[compact=true]:px-3" href="#nbtw-01" aria-label="Saved">
      <span class="text-[19px] leading-none" aria-hidden="true">♥</span>
      <span class="max-w-20 overflow-hidden whitespace-nowrap transition-[max-width,opacity] duration-[450ms] ease-nb01 group-data-[compact=true]:max-w-0 group-data-[compact=true]:opacity-0 motion-reduce:transition-none">Saved</span>
    </a>
    <a class="flex items-center gap-2 min-h-11 px-4 rounded-full no-underline text-white text-sm font-semibold transition-[background-color,transform] duration-200 hover:bg-white/15 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 group-data-[compact=true]:px-3" href="#nbtw-01" aria-label="Profile">
      <span class="text-[19px] leading-none" aria-hidden="true">◉</span>
      <span class="max-w-20 overflow-hidden whitespace-nowrap transition-[max-width,opacity] duration-[450ms] ease-nb01 group-data-[compact=true]:max-w-0 group-data-[compact=true]:opacity-0 motion-reduce:transition-none">Profile</span>
    </a>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-nb01-accent: #6b73f5;
  --color-nb01-accent: oklch(0.64 0.2 265);
  --font-nb01-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --ease-nb01: cubic-bezier(0.34, 1.4, 0.5, 1);
  --animate-nb01-bg: nb01-bg 18s ease-in-out infinite;
}
/* Keyframes cannot be a theme entry on their own — the @theme --animate-* token
   names the animation, this declares what it does. */

@keyframes nb01-bg {
  50% {
    background-position: 100% 100%;
  }
}
```

## JavaScript
```js
(() => {
  const scroll = document.querySelector('#nbtw-01-scroll');
  const bar = document.querySelector('#nbtw-01-bar');
  if (!scroll || !bar) return;
  const THRESHOLD = 10;
  let last = 0, idle;
  const set = (v) => { bar.dataset.compact = String(v); };
  scroll.addEventListener('scroll', () => {
    const y = scroll.scrollTop;
    if (y > last + THRESHOLD && y > 40) set(true);
    else if (y < last - THRESHOLD) set(false);
    last = y;
    clearTimeout(idle);
    idle = setTimeout(() => set(false), 600);
  }, { passive: true });
  bar.addEventListener('pointerenter', () => set(false));
  bar.addEventListener('focusin', () => set(false));
})();
```
