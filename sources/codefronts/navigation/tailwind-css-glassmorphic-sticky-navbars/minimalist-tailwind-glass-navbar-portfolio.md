---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/minimalist-tailwind-glass-navbar-portfolio/"
title: "Minimalist Tailwind Glass Navbar for Portfolios"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "Near-clear glass for work that should be the star: a 12% white fill, an 8px blur, a hairline bottom edge and links whose underline grows from the centre."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Tailwind Glass Navbar for Portfolios
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/minimalist-tailwind-glass-navbar-portfolio/

Near-clear glass for work that should be the star: a 12% white fill, an 8px blur, a hairline bottom edge and links whose underline grows from the centre. No CTA, no box &mdash; just the name and four links over a full-bleed project grid whose captions reveal on hover, focus, or always on touch.
## HTML
```html
<div class="tgn-11 w-full min-h-svh bg-tgn11-c bg-linear-200 from-tgn11-a via-tgn11-b via-40% to-tgn11-c font-tgn11-sans">
  <div class="relative h-svh overflow-y-auto scroll-smooth">
    <header class="sticky top-0 z-10 flex h-15 items-center gap-8 border-b border-white/18 bg-white/12 px-6 backdrop-blur-sm backdrop-saturate-[1.3] not-supports-[backdrop-filter:blur(1px)]:bg-tgn11-c/85 max-sm:h-14 max-sm:gap-4 max-sm:px-4">
      <a class="rounded-sm font-tgn11-serif text-[22px] leading-none text-white italic [text-shadow:0_1px_8px_rgb(0_0_0/0.35)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white max-sm:text-xl" href="#">Ava Reyes</a>
      <nav class="ml-auto" aria-label="Primary">
        <ul class="flex gap-7 max-sm:gap-4">
          <li><a href="#" aria-current="page" class="relative inline-flex h-15 items-center text-sm font-medium tracking-[0.01em] text-white/85 [text-shadow:0_1px_6px_rgb(0_0_0/0.3)] transition-colors duration-200 after:absolute after:inset-x-0 after:bottom-4 after:h-[1.5px] after:scale-x-0 after:bg-white after:transition-transform after:duration-250 after:ease-out hover:text-white hover:after:scale-x-100 aria-[current=page]:text-white aria-[current=page]:after:scale-x-100 aria-[current=page]:after:opacity-70 focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:transition-none motion-reduce:after:transition-none max-sm:h-14 max-sm:text-[13px] max-sm:after:bottom-3.5">Work</a></li>
          <li><a href="#" class="relative inline-flex h-15 items-center text-sm font-medium tracking-[0.01em] text-white/85 [text-shadow:0_1px_6px_rgb(0_0_0/0.3)] transition-colors duration-200 after:absolute after:inset-x-0 after:bottom-4 after:h-[1.5px] after:scale-x-0 after:bg-white after:transition-transform after:duration-250 after:ease-out hover:text-white hover:after:scale-x-100 aria-[current=page]:text-white aria-[current=page]:after:scale-x-100 aria-[current=page]:after:opacity-70 focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:transition-none motion-reduce:after:transition-none max-sm:h-14 max-sm:text-[13px] max-sm:after:bottom-3.5">Studio</a></li>
          <li class="max-[380px]:hidden"><a href="#" class="relative inline-flex h-15 items-center text-sm font-medium tracking-[0.01em] text-white/85 [text-shadow:0_1px_6px_rgb(0_0_0/0.3)] transition-colors duration-200 after:absolute after:inset-x-0 after:bottom-4 after:h-[1.5px] after:scale-x-0 after:bg-white after:transition-transform after:duration-250 after:ease-out hover:text-white hover:after:scale-x-100 aria-[current=page]:text-white aria-[current=page]:after:scale-x-100 aria-[current=page]:after:opacity-70 focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:transition-none motion-reduce:after:transition-none max-sm:h-14 max-sm:text-[13px] max-sm:after:bottom-3.5">Journal</a></li>
          <li><a href="#" class="relative inline-flex h-15 items-center text-sm font-medium tracking-[0.01em] text-white/85 [text-shadow:0_1px_6px_rgb(0_0_0/0.3)] transition-colors duration-200 after:absolute after:inset-x-0 after:bottom-4 after:h-[1.5px] after:scale-x-0 after:bg-white after:transition-transform after:duration-250 after:ease-out hover:text-white hover:after:scale-x-100 aria-[current=page]:text-white aria-[current=page]:after:scale-x-100 aria-[current=page]:after:opacity-70 focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:transition-none motion-reduce:after:transition-none max-sm:h-14 max-sm:text-[13px] max-sm:after:bottom-3.5">Contact</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,220px),1fr))] gap-1.5 p-1.5">
        <a href="#" class="group relative block aspect-[4/5] overflow-hidden rounded-md bg-[radial-gradient(120%_100%_at_30%_20%,oklch(0.72_0.14_45),oklch(0.4_0.09_25))] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
          <span class="absolute inset-0 bg-[radial-gradient(120%_100%_at_30%_20%,oklch(0.72_0.14_45),oklch(0.4_0.09_25))] transition-transform duration-500 ease-out group-hover:scale-105 motion-reduce:transition-none"></span>
          <span class="absolute inset-x-0 bottom-0 flex items-baseline justify-between bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 pointer-coarse:opacity-100"><span class="font-tgn11-serif text-xl italic">Saltwater</span><span class="font-tgn11-mono text-[11px] tracking-[0.08em]">2026</span></span>
        </a>
        <a href="#" class="group relative block aspect-[4/5] overflow-hidden rounded-md bg-[radial-gradient(120%_100%_at_70%_30%,oklch(0.55_0.15_320),oklch(0.28_0.08_285))] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
          <span class="absolute inset-0 bg-[radial-gradient(120%_100%_at_70%_30%,oklch(0.55_0.15_320),oklch(0.28_0.08_285))] transition-transform duration-500 ease-out group-hover:scale-105 motion-reduce:transition-none"></span>
          <span class="absolute inset-x-0 bottom-0 flex items-baseline justify-between bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 pointer-coarse:opacity-100"><span class="font-tgn11-serif text-xl italic">Night Garden</span><span class="font-tgn11-mono text-[11px] tracking-[0.08em]">2026</span></span>
        </a>
        <a href="#" class="group relative block aspect-[4/5] overflow-hidden rounded-md bg-[radial-gradient(120%_100%_at_40%_60%,oklch(0.6_0.13_200),oklch(0.32_0.08_240))] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
          <span class="absolute inset-0 bg-[radial-gradient(120%_100%_at_40%_60%,oklch(0.6_0.13_200),oklch(0.32_0.08_240))] transition-transform duration-500 ease-out group-hover:scale-105 motion-reduce:transition-none"></span>
          <span class="absolute inset-x-0 bottom-0 flex items-baseline justify-between bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 pointer-coarse:opacity-100"><span class="font-tgn11-serif text-xl italic">Tidal</span><span class="font-tgn11-mono text-[11px] tracking-[0.08em]">2025</span></span>
        </a>
        <a href="#" class="group relative block aspect-[4/5] overflow-hidden rounded-md bg-[radial-gradient(120%_100%_at_60%_40%,oklch(0.65_0.12_90),oklch(0.35_0.08_55))] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
          <span class="absolute inset-0 bg-[radial-gradient(120%_100%_at_60%_40%,oklch(0.65_0.12_90),oklch(0.35_0.08_55))] transition-transform duration-500 ease-out group-hover:scale-105 motion-reduce:transition-none"></span>
          <span class="absolute inset-x-0 bottom-0 flex items-baseline justify-between bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 pointer-coarse:opacity-100"><span class="font-tgn11-serif text-xl italic">Field Notes</span><span class="font-tgn11-mono text-[11px] tracking-[0.08em]">2025</span></span>
        </a>
        <a href="#" class="group relative block aspect-[4/5] overflow-hidden rounded-md bg-[radial-gradient(120%_100%_at_50%_70%,oklch(0.7_0.13_30),oklch(0.3_0.09_350))] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
          <span class="absolute inset-0 bg-[radial-gradient(120%_100%_at_50%_70%,oklch(0.7_0.13_30),oklch(0.3_0.09_350))] transition-transform duration-500 ease-out group-hover:scale-105 motion-reduce:transition-none"></span>
          <span class="absolute inset-x-0 bottom-0 flex items-baseline justify-between bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 pointer-coarse:opacity-100"><span class="font-tgn11-serif text-xl italic">Ember</span><span class="font-tgn11-mono text-[11px] tracking-[0.08em]">2024</span></span>
        </a>
        <a href="#" class="group relative block aspect-[4/5] overflow-hidden rounded-md bg-[radial-gradient(120%_100%_at_30%_30%,oklch(0.58_0.14_270),oklch(0.24_0.07_260))] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
          <span class="absolute inset-0 bg-[radial-gradient(120%_100%_at_30%_30%,oklch(0.58_0.14_270),oklch(0.24_0.07_260))] transition-transform duration-500 ease-out group-hover:scale-105 motion-reduce:transition-none"></span>
          <span class="absolute inset-x-0 bottom-0 flex items-baseline justify-between bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 pointer-coarse:opacity-100"><span class="font-tgn11-serif text-xl italic">Blue Hour</span><span class="font-tgn11-mono text-[11px] tracking-[0.08em]">2024</span></span>
        </a>
      </div>
      <div class="mx-auto max-w-2xl px-7 pt-10 pb-20 text-white/88 [&_:is(p,h2,h3)]:[text-shadow:0_1px_8px_rgb(0_0_0/0.35)] [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:text-white [&_h2]:font-tgn11-serif [&_h2]:text-[32px] [&_h2]:font-normal [&_h3]:font-tgn11-serif [&_h3]:text-2xl [&_h3]:font-normal [&_h3]:italic [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn11-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:border [&_code]:border-white/22 [&_code]:bg-white/14 [&_code]:text-white [&_code]:[text-shadow:none]">
      <h2>Ultra-clean glass over full-bleed portfolio work</h2>
      <p>The sticky bar barely tints the imagery underneath. A near-clear <code>rgba(255,255,255,.14)</code> fill lets the work read straight through — the navigation is present, quiet, readable.</p>
      <p>A light <code>backdrop-filter:blur(8px)</code> is just enough to lift the letterforms off busy photography without frosting the work into obscurity.</p>
      <p>No border box, no shadow, no CTA — only a hairline bottom rule to separate nav from canvas. Type does the work: tight letter-spacing, small logo, generous <code>gap</code>, low-key underline that grows from the centre on hover.</p>
      <p>Because the fill is so light, legibility rides on the <code>text-shadow</code> plus the blur softening high-frequency detail directly under the strip.</p>
      <p>The active link is marked by a small persistent underline, not a filled pill — anything heavier would break the minimalist contract.</p>
      <h3>Minimalism as constraint, not decoration</h3>
      <p>Every element removed makes the imagery louder. No border box means no visible frame competing with the composition. No shadow means no fake elevation implying the header sits above the work.</p>
      <p>No CTA means no commercial intrusion into the reading experience. Portfolio sites are trust-builders, not conversion funnels — the visitor decides to reach out, not the button.</p>
      <p>Every restraint has a payoff. The imagery reads first. The navigation reads only when the visitor looks for it. The header stops being chrome and becomes a service.</p>
      <h3>The centre-grow underline in detail</h3>
      <p>The underline pseudo-element sits below each link at <code>transform: scaleX(0)</code> with <code>transform-origin: center</code>. On hover, it transitions to <code>scaleX(1)</code> — growing from the centre outward instead of unfurling from the left.</p>
      <p>Setting <code>transform-origin: center</code> is the key. Forgetting it makes the underline grow from the left, which reads as directional and pushy. From the centre, it reads as balanced and confident.</p>
      <p>Duration around 250ms with an ease-out curve. Faster reads as accidental; slower reads as ceremonial. 250ms is the sweet spot for “yes, I noticed you”.</p>
      <h3>When the near-clear fill works</h3>
      <p>Over dark photography with strong tonal range. The white glass tints subtly without competing with the imagery's own light-dark story.</p>
      <p>Over hero video with limited palette range. The light tint reads as unified with the video's atmospheric colour.</p>
      <p>Over animated backgrounds where an opaque bar would break the ambient motion. The near-clear fill keeps the motion continuous.</p>
      <h3>When it fails</h3>
      <p>Over predominantly white imagery. The nearly-clear glass over a light background makes text almost invisible. Test with your lightest hero image, not your darkest.</p>
      <p>Over very busy imagery with high-frequency detail. The light blur can't hide it, and the text ends up sitting on visual noise.</p>
      <p>For products that require a visible CTA. Portfolio pattern doesn't include one; if you need one, use Demo 01 or Demo 04 instead.</p>
      <h3>Real portfolio sites shipping this pattern</h3>
      <p>Awwwards site-of-the-day winners frequently use it. It signals that the designer understands restraint, which is what awards judges respond to.</p>
      <p>Photography portfolio sites (Bruce Munro, David LaChapelle, high-end wedding photographers). The imagery must lead; the chrome must serve.</p>
      <p>Design agency landing pages that want to signal seniority. Junior agencies show off their design system in the chrome; senior agencies let the client work show it.</p>
      <p>Editorial magazines and long-form journalism. The Read.cv variant is exactly this pattern with a hairline separator and no CTA.</p>
      <p>Keep scrolling — the sticky bar stays present, stays quiet, stays out of the way of the imagery below.</p>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgn11-a: #9e5f48;
  --color-tgn11-a: oklch(0.55 0.09 40);
  --color-tgn11-b: #5a2a2b;
  --color-tgn11-b: oklch(0.35 0.07 20);
  --color-tgn11-c: #0f1932;
  --color-tgn11-c: oklch(0.22 0.05 265);
  --font-tgn11-serif: 'Instrument Serif', Georgia, serif;
  --font-tgn11-sans: 'Hanken Grotesk', system-ui, sans-serif;
  --font-tgn11-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-11 {
  width: 100%;
  min-height: 100svh;
}
```
