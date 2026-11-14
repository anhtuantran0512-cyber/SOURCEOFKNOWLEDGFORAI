---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/accessible-tailwind-glassmorphism-navbar-wcag/"
title: "Accessible Tailwind Glassmorphism Navbar (WCAG AA)"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "Glass engineered to pass a real audit: a 72% fill that holds AA over the lightest part of the image, an opaque not-supports-[backdrop-filter:blur(1px)]:…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Glassmorphism Navbar (WCAG AA)
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/accessible-tailwind-glassmorphism-navbar-wcag/

Glass engineered to pass a real audit: a 72% fill that holds AA over the lightest part of the image, an opaque not-supports-[backdrop-filter:blur(1px)]: fallback, a solid bar under prefers-reduced-transparency and contrast-more:, a two-tone focus ring, a skip link, and Atkinson Hyperlegible for the type.
## HTML
```html
<div class="tgn-09 w-full min-h-svh bg-tgn09-a bg-[conic-gradient(from_45deg_at_60%_30%,var(--color-tgn09-a),var(--color-tgn09-b),var(--color-tgn09-c),var(--color-tgn09-d),var(--color-tgn09-a))] font-tgn09-sans">
  <div class="relative h-svh overflow-y-auto scroll-smooth p-3 sm:p-4.5">
    <a href="#tgn09-main" class="sr-only rounded-xl bg-tgn09-ink px-4 py-3 font-bold text-white focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-20 focus:outline-none focus:ring-[2.5px] focus:ring-white">Skip to content</a>
    <header class="sticky top-0 z-10 flex min-h-15 flex-wrap items-center gap-x-5 gap-y-1 rounded-2xl border border-white/85 bg-white/72 py-2 pr-2 pl-5 shadow-[0_6px_22px_-4px_oklch(0.25_0.03_255/0.25)] backdrop-blur-[14px] backdrop-saturate-150 not-supports-[backdrop-filter:blur(1px)]:bg-tgn09-solid [@media(prefers-reduced-transparency:reduce)]:bg-white contrast-more:border-2 contrast-more:border-tgn09-ink contrast-more:bg-white sm:flex-nowrap">
      <a class="rounded-md text-lg font-bold text-tgn09-ink focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn09-ring focus-visible:ring-offset-[2.5px] focus-visible:ring-offset-white" href="#">Civicline</a>
      <nav class="max-sm:order-last max-sm:-ml-3 max-sm:w-full max-sm:overflow-x-auto max-sm:[scrollbar-width:none] sm:mx-auto" aria-label="Primary">
        <ul class="flex gap-0.5">
          <li><a href="#" aria-current="page" class="flex h-11 items-center rounded-[10px] px-3.5 text-[15px] font-bold whitespace-nowrap text-tgn09-ink transition-colors hover:bg-tgn09-ink/8 hover:underline hover:underline-offset-4 aria-[current=page]:bg-tgn09-acc aria-[current=page]:text-white focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn09-ring focus-visible:ring-offset-[2.5px] focus-visible:ring-offset-white motion-reduce:transition-none">Services</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3.5 text-[15px] font-bold whitespace-nowrap text-tgn09-ink transition-colors hover:bg-tgn09-ink/8 hover:underline hover:underline-offset-4 aria-[current=page]:bg-tgn09-acc aria-[current=page]:text-white focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn09-ring focus-visible:ring-offset-[2.5px] focus-visible:ring-offset-white motion-reduce:transition-none">Payments</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3.5 text-[15px] font-bold whitespace-nowrap text-tgn09-ink transition-colors hover:bg-tgn09-ink/8 hover:underline hover:underline-offset-4 aria-[current=page]:bg-tgn09-acc aria-[current=page]:text-white focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn09-ring focus-visible:ring-offset-[2.5px] focus-visible:ring-offset-white motion-reduce:transition-none">Support</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3.5 text-[15px] font-bold whitespace-nowrap text-tgn09-ink transition-colors hover:bg-tgn09-ink/8 hover:underline hover:underline-offset-4 aria-[current=page]:bg-tgn09-acc aria-[current=page]:text-white focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn09-ring focus-visible:ring-offset-[2.5px] focus-visible:ring-offset-white motion-reduce:transition-none">Contact</a></li>
        </ul>
      </nav>
      <a href="#" class="flex h-11 items-center rounded-[10px] bg-tgn09-acc px-4.5 text-[15px] font-bold text-white transition-colors hover:bg-tgn09-ring focus-visible:outline-none focus-visible:ring-[2.5px] focus-visible:ring-tgn09-ring focus-visible:ring-offset-[2.5px] focus-visible:ring-offset-white motion-reduce:transition-none max-sm:ml-auto">Sign in</a>
    </header>
    <main id="tgn09-main" tabindex="-1" class="mx-auto max-w-2xl px-1 pt-5 pb-20 text-tgn09-ink outline-none [&_:is(p,h2,h3)]:[text-shadow:0_1px_2px_rgb(255_255_255/0.55)] [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_p]:text-base/[1.7] [&_p]:font-normal [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:text-tgn09-ink [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn09-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:border [&_code]:border-white/90 [&_code]:bg-white/80 [&_code]:text-tgn09-acc">
      <p class="mb-5! inline-block rounded-xl bg-white/70 px-3.5 py-2 text-sm/[1.5]! font-bold!">Legible over the busiest, lightest part of the image — and solid where backdrop-filter isn’t supported.</p>
      <h2>Accessible glass, engineered to pass a real audit</h2>
      <p>Glassmorphism's dirty secret is that translucent text over a random photo routinely fails contrast. This demo fixes it three ways — and stays sticky the whole way down.</p>
      <p>First, the fill is opaque enough to guarantee a contrast floor. The frosted pane never drops below the fill's own contrast with the text, no matter what colour scrolls behind it.</p>
      <p>Second, a whisper-thin <code>text-shadow</code> gives every glyph a subtle halo so edges stay crisp against light patches of the image.</p>
      <p>Third — the critical part — an <code>@supports not (backdrop-filter:blur(1px))</code> block replaces the translucent fill with a fully opaque bar, so browsers without <code>backdrop-filter</code> and users who'd otherwise get unreadable transparent text get a solid, legible header instead.</p>
      <p>Focus is handled for the blur too: the <code>:focus-visible</code> ring is a high-contrast double outline (dark inside, light outside) so it reads on any background the glass might sample.</p>
      <p>Every colour pairing clears WCAG AA (4.5:1) against the fill's effective luminance. The demo is intentionally conservative — it passes an audit rather than merely looking modern.</p>
      <p>For AAA (7:1) contexts, darken the text and thicken the fill; keep the text-shadow subtle so it aids edges without smudging.</p>
      <h3>prefers-reduced-transparency</h3>
      <p>Apple introduced this media query alongside iOS 17. When the user opts out of translucency in system settings, <code>@media (prefers-reduced-transparency: reduce)</code> matches, and the responsible move is to swap the glass fill for a solid tint.</p>
      <p>This is not the same as <code>prefers-reduced-motion</code>. Motion-reduction guards animation; transparency-reduction guards translucency. A user might want reduced motion but full transparency, or vice versa.</p>
      <p>Ship both media queries. Most users never trigger them; the ones who do are a critical audience who will notice when you don't respect their settings.</p>
      <h3>The @supports fallback in detail</h3>
      <p>Ship the <code>@supports</code> fallback or a meaningful slice of users get white-on-random-photo text; this single declaration is the most-skipped and most-important line in accessible glass.</p>
      <p>The fallback fill can be your brand solid colour, not just a neutral. Treat the “no-glass” skin as intentional, not an afterthought. Users who see it should think “this is the alternate mode”, not “this looks broken”.</p>
      <p>For belt-and-braces coverage, also negate the webkit-prefixed version: <code>@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px)))</code>. This catches every browser that supports neither the standard nor the prefix.</p>
      <h3>Regulated verticals that demand this build</h3>
      <p>Healthcare and HIPAA-adjacent products (Zocdoc, Doximity, EHR frontends). HIPAA does not directly mandate accessibility, but any US healthcare product that touches federal payment (Medicare, Medicaid) inherits Section 508.</p>
      <p>Government and public-sector sites. Section 508 (US federal), EN 301 549 (EU / German public sector), AODA (Ontario), DDA (Australia), and the European Accessibility Act (June 2025) all require WCAG 2.2 AA.</p>
      <p>Insurance quote comparators. Regulated in most tier-1 markets; state insurance commissioners require the site to be usable by consumers with disabilities.</p>
      <p>Legal firm websites. ABA Model Rule 7.1 requires accurate advertising; a site that fails accessibility discriminates against clients with disabilities. Malpractice risk.</p>
      <h3>Focus rings that survive glass</h3>
      <p>Single-colour focus rings can vanish against particular background patches. The double outline pattern (light on dark or dark on light, doubled) guarantees at least one edge is visible against any backdrop.</p>
      <p>Ship <code>outline: 2px solid Highlight</code> as a fallback in <code>@media (forced-colors: active)</code> for Windows High Contrast mode. The system palette handles the ratio; you just have to opt in.</p>
      <p>Never rely on the blur for contrast. A light patch of the background photo can scroll behind the bar and tank your ratio at any moment; the opaque-enough fill is the real guarantee.</p>
      <p>Keep scrolling — the sticky bar demonstrates its legibility over the full range of gradient hues.</p>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgn09-a: #fce39f;
  --color-tgn09-a: oklch(0.92 0.09 90);
  --color-tgn09-b: #f47c6b;
  --color-tgn09-b: oklch(0.72 0.15 30);
  --color-tgn09-c: #6ee8e1;
  --color-tgn09-c: oklch(0.86 0.11 190);
  --color-tgn09-d: #a780e6;
  --color-tgn09-d: oklch(0.68 0.15 300);
  --color-tgn09-ink: #142234;
  --color-tgn09-ink: oklch(0.25 0.04 255);
  --color-tgn09-acc: #006852;
  --color-tgn09-acc: oklch(0.45 0.11 175);
  --color-tgn09-ring: #004d3a;
  --color-tgn09-ring: oklch(0.36 0.1 175);
  --color-tgn09-solid: #fafcfe;
  --color-tgn09-solid: oklch(0.99 0.004 250);
  --font-tgn09-sans: 'Atkinson Hyperlegible', system-ui, sans-serif;
  --font-tgn09-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-09 {
  width: 100%;
  min-height: 100svh;
}
```
