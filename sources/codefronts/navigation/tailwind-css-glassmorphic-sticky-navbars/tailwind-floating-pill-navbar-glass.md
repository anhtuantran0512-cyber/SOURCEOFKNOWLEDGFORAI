---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-floating-pill-navbar-glass/"
title: "Tailwind Floating Pill Navbar with Glass Effect"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "The floating-island capsule: a glass pill detached from the edges, a filled sub-pill for the active page and a doubled contact + float shadow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Pill Navbar with Glass Effect
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-floating-pill-navbar-glass/

The floating-island capsule: a glass pill detached from the edges, a filled sub-pill for the active page and a doubled contact + float shadow. On phones the same markup docks to the bottom as a thumb-zone tab bar with max-sm:fixed max-sm:bottom-3 &mdash; no second component.
## HTML
```html
<div class="tgn-04 w-full min-h-svh bg-tgn04-a bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-tgn04-a),var(--color-tgn04-b),var(--color-tgn04-c),var(--color-tgn04-d),var(--color-tgn04-a))] font-tgn04-sans">
  <div class="relative h-svh overflow-y-auto scroll-smooth">
    <header class="sticky top-4 z-10 mx-auto mt-4 flex max-w-lg items-center gap-4 rounded-full border border-white/65 bg-white/50 p-1.5 pl-5 shadow-[0_2px_8px_oklch(0.25_0.08_300/0.14),0_16px_40px_-8px_oklch(0.25_0.08_300/0.22)] backdrop-blur-lg backdrop-saturate-[1.8] not-supports-[backdrop-filter:blur(1px)]:bg-white/90 max-sm:fixed max-sm:inset-x-3 max-sm:top-auto max-sm:bottom-3 max-sm:mt-0 max-sm:max-w-none max-sm:p-1.5">
      <a class="flex items-center gap-2 rounded-full text-base font-extrabold tracking-[-0.02em] whitespace-nowrap text-tgn04-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn04-acc max-sm:hidden" href="#"><span aria-hidden="true" class="size-3 rounded-full bg-tgn04-acc ring-4 ring-tgn04-acc/25"></span>Halo</a>
      <nav class="ml-auto max-sm:ml-0 max-sm:w-full" aria-label="Primary">
        <ul class="flex gap-1 max-sm:gap-0.5">
          <li class="max-sm:flex max-sm:flex-1"><a href="#" aria-current="page" class="flex h-11 items-center justify-center rounded-full px-4 text-sm font-semibold text-tgn04-ink transition-colors hover:bg-white/60 aria-[current=page]:bg-tgn04-acc aria-[current=page]:text-white aria-[current=page]:shadow-[0_4px_12px_-2px_var(--color-tgn04-acc)] focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn04-acc focus-visible:ring-offset-2 focus-visible:ring-offset-white max-sm:flex-1 max-sm:px-2 max-sm:text-[13px]">Home</a></li>
          <li class="max-sm:flex max-sm:flex-1"><a href="#" class="flex h-11 items-center justify-center rounded-full px-4 text-sm font-semibold text-tgn04-ink transition-colors hover:bg-white/60 aria-[current=page]:bg-tgn04-acc aria-[current=page]:text-white aria-[current=page]:shadow-[0_4px_12px_-2px_var(--color-tgn04-acc)] focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn04-acc focus-visible:ring-offset-2 focus-visible:ring-offset-white max-sm:flex-1 max-sm:px-2 max-sm:text-[13px]">Features</a></li>
          <li class="max-sm:flex max-sm:flex-1"><a href="#" class="flex h-11 items-center justify-center rounded-full px-4 text-sm font-semibold text-tgn04-ink transition-colors hover:bg-white/60 aria-[current=page]:bg-tgn04-acc aria-[current=page]:text-white aria-[current=page]:shadow-[0_4px_12px_-2px_var(--color-tgn04-acc)] focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn04-acc focus-visible:ring-offset-2 focus-visible:ring-offset-white max-sm:flex-1 max-sm:px-2 max-sm:text-[13px]">Team</a></li>
          <li class="max-sm:flex max-sm:flex-1"><a href="#" class="flex h-11 items-center justify-center rounded-full px-4 text-sm font-semibold text-tgn04-ink transition-colors hover:bg-white/60 aria-[current=page]:bg-tgn04-acc aria-[current=page]:text-white aria-[current=page]:shadow-[0_4px_12px_-2px_var(--color-tgn04-acc)] focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn04-acc focus-visible:ring-offset-2 focus-visible:ring-offset-white max-sm:flex-1 max-sm:px-2 max-sm:text-[13px]">Contact</a></li>
        </ul>
      </nav>
    </header>
    <div class="mx-auto max-w-2xl px-7 pt-24 pb-16 text-tgn04-text max-sm:pt-12 max-sm:pb-28 [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_strong]:font-extrabold [&_strong]:text-tgn04-ink [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:font-extrabold [&_:is(h2,h3)]:text-tgn04-ink [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn04-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:bg-white/45 [&_code]:text-tgn04-ink">
      <p><strong>Watch the island float.</strong></p>
      <p>The pill sits above the content as you scroll — a detached, capsule-shaped bar anchored top-centre with visible gaps on either side, so the page reads through underneath.</p>
      <p>This is the "floating island" pattern popularised by modern app landing pages. It feels like a physical lozenge hovering above the imagery, connected to nothing.</p>
      <p>The max-width plus <code>margin-inline:auto</code> is what sells it — the pill never spans the full width, so there is a visible slice of content flowing past on both sides.</p>
      <p>Under the pill the shadow is doubled: a tight dark shadow for the contact plane, a wide soft shadow for the float. Read together, the lozenge sits above the page rather than stuck to it.</p>
      <h3>Anatomy of the doubled shadow</h3>
      <p>The tight contact shadow (small blur radius, dark, close to the pill) reads as ambient occlusion — the pill is casting a shadow on the surface directly beneath it.</p>
      <p>The wide float shadow (large blur radius, faint, offset further) reads as elevation — the pill is well above the surface, so its shadow spreads and softens.</p>
      <p>Together they read as physically correct. Ship only one and the effect collapses: a single tight shadow makes the pill look stuck to the page; a single wide shadow makes it look weightless.</p>
      <p>Keep the contact shadow blur under 12px and the float shadow opacity under 0.2. Above those thresholds the shadow starts to compete with the pill itself.</p>
      <h3>Sub-pill active state</h3>
      <p>Inside the pill, the active link is a filled sub-pill — a smaller capsule with its own solid background — so navigation carries a visible selected state that echoes the outer shape.</p>
      <p>Hover states are also pill-shaped, giving the whole thing a cohesive rounded language across every interactive element. Nothing rectangular appears anywhere inside the pill.</p>
      <p>Because it is <code>sticky</code>, the island rides down with the scroll while the content flows underneath the transparent gaps at its sides — exactly what you are seeing now.</p>
      <p>Try anchoring the same markup to <code>bottom-centre</code> with <code>top:auto;bottom:16px</code> for a floating mobile-style tab bar. Same technique, opposite anchor.</p>
      <h3>When the floating island beats the full-width bar</h3>
      <p>Portfolio sites where the imagery is the star. The gap on either side lets full-bleed hero images breathe without being framed by a nav strip.</p>
      <p>Editorial magazines and long-form reading experiences. The pill reads as a small, ignorable UI affordance rather than a persistent frame around the content.</p>
      <p>Landing pages that shift between light and dark sections. A full-width bar has to commit to one theme and fight the sections that don't match; a floating pill can stay glass-neutral and read against everything.</p>
      <p>Mobile-first apps that mimic native tab-bar conventions. Anchor the pill to the bottom instead of the top and it reads as iOS-native tab navigation.</p>
      <h3>When it fails</h3>
      <p>Enterprise dashboards with dense information architecture. A pill can only carry 4-5 primary links; anything more forces a dropdown that breaks the minimalist promise.</p>
      <p>SaaS marketing sites with a Sign in + Get started + Book demo + Docs + Pricing lineup. Five items plus two CTAs is too much for a pill; use a full-width bar with the doubled shadow removed.</p>
      <p>Any product where accessibility auditors will Lighthouse the page. A pill with heavy shadow can fail contrast against certain background patches; use the full-width variant for compliance-critical products.</p>
      <p>Keep scrolling — the island demonstrates its floating behaviour by staying pinned as the content moves past it.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgn04-a: #e1b942;
  --color-tgn04-a: oklch(0.8 0.14 90);
  --color-tgn04-b: #f87966;
  --color-tgn04-b: oklch(0.72 0.16 30);
  --color-tgn04-c: #de65bb;
  --color-tgn04-c: oklch(0.68 0.18 340);
  --color-tgn04-d: #4ba3f7;
  --color-tgn04-d: oklch(0.7 0.15 250);
  --color-tgn04-ink: #2b1844;
  --color-tgn04-ink: oklch(0.26 0.08 300);
  --color-tgn04-text: #2b1531;
  --color-tgn04-text: oklch(0.24 0.06 320);
  --color-tgn04-acc: #b70385;
  --color-tgn04-acc: oklch(0.52 0.22 345);
  --font-tgn04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tgn04-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-04 {
  width: 100%;
  min-height: 100svh;
}
```
