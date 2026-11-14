---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-dark-vcard-iridescent-sheen/"
title: "Tailwind Dark vCard with Iridescent Sheen"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A dark link-in-bio vCard: two gradient grounds, a rotated iridescent sheen, a blurred corner bloom, gradient-clipped name, skill chips and a light-on-dark…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark vCard with Iridescent Sheen
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-dark-vcard-iridescent-sheen/

A dark link-in-bio vCard: two gradient grounds, a rotated iridescent sheen, a blurred corner bloom, gradient-clipped name, skill chips and a light-on-dark Connect pill. The port's win is that the sheen and the bloom &mdash; the two effects that make the card &mdash; are readable as one class list each rather than two opaque modifier names.
## HTML
```html
<section class="twc-13 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc13-bg [background-image:radial-gradient(ellipse_at_30%_20%,oklch(0.78_0.1_275/0.09),transparent_50%),radial-gradient(ellipse_at_80%_80%,oklch(0.68_0.2_350/0.07),transparent_50%)] font-twc13-sans">

  <article class="relative isolate w-full max-w-[360px] min-h-55 overflow-hidden rounded-[20px] px-5.5 pt-5.5 pb-4.5 border border-white/6 [background:linear-gradient(180deg,oklch(1_0_0/0.02)_0%,transparent_40%),linear-gradient(160deg,#14152a_0%,#0d0e1c_100%)] shadow-[0_30px_60px_-30px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.05)] transition-[transform,box-shadow] duration-300 hover:-translate-y-0.5 hover:shadow-[0_40px_70px_-30px_oklch(0_0_0/0.9),inset_0_0_0_1px_oklch(0.78_0.1_275/0.14)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">

    <div aria-hidden="true" class="absolute -top-1/2 -left-[20%] w-3/5 h-[200%] z-0 rotate-15 pointer-events-none [background:linear-gradient(115deg,transparent_30%,oklch(0.78_0.1_275/0.06)_45%,oklch(0.75_0.16_350/0.05)_50%,oklch(0.8_0.13_200/0.06)_55%,transparent_70%)]"></div>
    <div aria-hidden="true" class="absolute -top-15 -right-15 size-55 z-0 pointer-events-none blur-[24px] [background:radial-gradient(circle_at_30%_30%,oklch(0.78_0.1_275/0.32)_0%,transparent_55%),radial-gradient(circle_at_60%_70%,oklch(0.75_0.16_350/0.18)_0%,transparent_55%)]"></div>

    <header class="relative z-1 flex items-center justify-between gap-3 mb-4">
      <div class="flex items-center gap-2">
        <span aria-hidden="true" class="relative size-5.5 rounded-[7px] [background:linear-gradient(135deg,#a5b4fc_0%,#6366f1_50%,#4338ca_100%)] shadow-[0_0_0_1px_oklch(0.78_0.1_275/0.35),0_4px_12px_oklch(0.55_0.2_275/0.35)] after:absolute after:inset-1 after:rounded after:content-[''] after:[background:linear-gradient(135deg,transparent_40%,oklch(1_0_0/0.4)_55%,transparent_65%)]"></span>
        <span class="font-twc13-mono text-[10.5px] font-bold tracking-[0.14em] text-white/85">SASHA LIN</span>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-full bg-twc13-green/10 border border-twc13-green/22 text-[10px] font-medium text-twc13-dim">
        <span aria-hidden="true" class="size-[5px] rounded-full bg-twc13-green shadow-[0_0_8px_oklch(0.78_0.14_165)] animate-twc13-pulse motion-reduce:animate-none"></span>
        Open to opportunities
      </span>
    </header>

    <div class="relative z-1 mb-4.5">
      <h3 class="inline-flex items-center gap-1.5 m-0 mb-1 text-2xl/[1.1] font-bold tracking-[-0.02em] text-twc13-white [background-image:linear-gradient(180deg,#ffffff_0%,#d4d4de_130%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">
        Sasha Lin
        <svg role="img" aria-label="Verified" width="16" height="16" viewBox="0 0 24 24" fill="none" class="flex-none"><path d="M12 2L14 4L17 3L18 6L21 7L20 10L22 12L20 14L21 17L18 18L17 21L14 20L12 22L10 20L7 21L6 18L3 17L4 14L2 12L4 10L3 7L6 6L7 3L10 4Z" fill="#a5b4fc"/><path d="M9 12L11 14L15 10" stroke="#0a0b12" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </h3>
      <p class="m-0 mb-2 text-[12.5px] font-medium text-twc13-ink2">Head of Partnerships &middot; Stripe</p>
      <p class="m-0 mb-3 text-xs/[1.5] text-twc13-dim">Helping fintechs ship revenue infrastructure. Previously YC, Notion.</p>
      <ul aria-label="Focus areas" class="flex flex-wrap gap-1.5 list-none m-0 p-0">
        <li class="px-2.5 py-[3px] rounded-full bg-twc13-acc/10 border border-twc13-acc/18 text-[10.5px] font-semibold tracking-[0.01em] text-twc13-chipink">Fintech</li>
        <li class="px-2.5 py-[3px] rounded-full bg-twc13-acc/10 border border-twc13-acc/18 text-[10.5px] font-semibold tracking-[0.01em] text-twc13-chipink">Product</li>
        <li class="px-2.5 py-[3px] rounded-full bg-twc13-acc/10 border border-twc13-acc/18 text-[10.5px] font-semibold tracking-[0.01em] text-twc13-chipink">Growth</li>
      </ul>
    </div>

    <footer class="relative z-1 flex items-center justify-between gap-3 pt-3.5 border-t border-white/6">
      <div class="flex items-center gap-1.5">
        <a href="#connect" class="inline-flex items-center gap-1.5 min-h-11 px-4 rounded-full no-underline text-xs font-bold tracking-[-0.005em] text-twc13-btnink [background:linear-gradient(180deg,#ecfdf5_0%,#a5b4fc_100%)] shadow-[0_4px_12px_oklch(0.78_0.1_275/0.28),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_6px_16px_oklch(0.78_0.1_275/0.4),inset_0_0_0_1px_oklch(1_0_0/0.2)] focus-visible:outline-2 focus-visible:outline-twc13-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 12h8M12 8v8"/></svg>
          Connect
        </a>
        <a href="#vcard" aria-label="Save contact card" class="inline-flex items-center justify-center size-11 rounded-full no-underline bg-white/5 border border-white/8 text-twc13-ink2 transition-[background,color,border-color] duration-200 hover:bg-twc13-acc/12 hover:text-twc13-acc hover:border-twc13-acc/32 focus-visible:outline-2 focus-visible:outline-twc13-acc focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        </a>
      </div>
      <div aria-label="Social links" class="flex items-center gap-0.5">
        <a href="mailto:[email protected]" aria-label="Email Sasha" class="inline-flex items-center justify-center size-11 rounded-lg no-underline text-twc13-faint transition-[color,background] duration-200 hover:text-twc13-acc hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-twc13-acc focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3,7 12,13 21,7"/></svg>
        </a>
        <a href="#linkedin" aria-label="LinkedIn" class="inline-flex items-center justify-center size-11 rounded-lg no-underline text-twc13-faint transition-[color,background] duration-200 hover:text-twc13-acc hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-twc13-acc focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.03-1.85-3.03-1.85 0-2.13 1.44-2.13 2.94v5.66H9.37V9h3.4v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.46zM5.34 7.43c-1.14 0-2.06-.93-2.06-2.06 0-1.14.93-2.06 2.06-2.06 1.14 0 2.06.93 2.06 2.06.01 1.14-.92 2.06-2.06 2.06zm1.78 13.02H3.56V9h3.55v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.22.79 24 1.77 24h20.45c.99 0 1.78-.78 1.78-1.73V1.73C24 .77 23.21 0 22.22 0z"/></svg>
        </a>
        <a href="#x" aria-label="X" class="inline-flex items-center justify-center size-11 rounded-lg no-underline text-twc13-faint transition-[color,background] duration-200 hover:text-twc13-acc hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-twc13-acc focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </a>
      </div>
    </footer>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc13-bg: #05060d;
  --color-twc13-bg: oklch(0.1 0.015 270);
  --color-twc13-white: #fafafa;
  --color-twc13-white: oklch(0.98 0 0);
  --color-twc13-ink2: #d4d4d8;
  --color-twc13-ink2: oklch(0.87 0.005 285);
  --color-twc13-dim: #a1a1aa;
  --color-twc13-dim: oklch(0.7 0.01 285);
  --color-twc13-faint: #71717a;
  --color-twc13-faint: oklch(0.54 0.015 285);
  --color-twc13-acc: #a5b4fc;
  --color-twc13-acc: oklch(0.78 0.1 275);
  --color-twc13-chipink: #c7d2fe;
  --color-twc13-chipink: oklch(0.86 0.07 275);
  --color-twc13-green: #34d399;
  --color-twc13-green: oklch(0.78 0.14 165);
  --color-twc13-btnink: #06070c;
  --color-twc13-btnink: oklch(0.11 0.01 270);
  --font-twc13-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc13-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc13-pulse: twc13-pulse 2.4s ease-in-out infinite;
}

@keyframes twc13-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

.twc-13 {
  width: 100%;
  min-height: 100svh;
}
```
