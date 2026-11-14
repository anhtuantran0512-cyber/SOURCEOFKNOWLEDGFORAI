---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-animated-gradient-border-glass-navbar/"
title: "Tailwind Animated Gradient Border Glass Navbar"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "An iridescent conic-gradient border chasing around a dark glass bar, with a soft blurred glow of the same gradient underneath."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Gradient Border Glass Navbar
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-animated-gradient-border-glass-navbar/

An iridescent conic-gradient border chasing around a dark glass bar, with a soft blurred glow of the same gradient underneath. The angle is a registered @property (the one thing that must stay CSS), the spin is an @theme animation token, and the ring itself is a masked before: layer.
## HTML
```html
<div class="tgn-08 w-full min-h-svh bg-tgn08-night bg-[radial-gradient(90%_120%_at_15%_0%,var(--color-tgn08-dusk),var(--color-tgn08-night)_70%)] font-tgn08-sans">
  <div class="relative h-svh overflow-y-auto scroll-smooth px-4 py-5 sm:px-6 sm:py-7">
    <header class="group/frame sticky top-0 z-10 rounded-2xl p-0.5 before:pointer-events-none before:absolute before:inset-0 before:rounded-[inherit] before:p-0.5 before:bg-[conic-gradient(from_var(--tgn08-angle),var(--color-tgn08-a),var(--color-tgn08-b),var(--color-tgn08-c),var(--color-tgn08-d),var(--color-tgn08-a))] before:[mask:linear-gradient(#000_0_0)_content-box_exclude,linear-gradient(#000_0_0)] before:animate-tgn08-spin after:pointer-events-none after:absolute after:inset-0 after:-z-10 after:rounded-[inherit] after:bg-[conic-gradient(from_var(--tgn08-angle),var(--color-tgn08-a),var(--color-tgn08-b),var(--color-tgn08-c),var(--color-tgn08-d),var(--color-tgn08-a))] after:opacity-40 after:blur-xl after:animate-tgn08-spin after:transition-opacity after:duration-300 hover:after:opacity-75 focus-within:after:opacity-75 motion-reduce:before:animate-none motion-reduce:after:animate-none">
      <div class="relative flex h-15 items-center gap-5 rounded-[14px] bg-tgn08-glass/60 px-5 backdrop-blur-lg backdrop-saturate-[1.6] not-supports-[backdrop-filter:blur(1px)]:bg-tgn08-glass max-sm:h-14 max-sm:gap-2 max-sm:px-3">
        <a class="flex items-center gap-2 rounded-md text-lg font-bold tracking-[-0.02em] text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn08-c" href="#"><span aria-hidden="true" class="size-4 rotate-45 rounded-[3px] bg-[conic-gradient(from_45deg,var(--color-tgn08-a),var(--color-tgn08-b),var(--color-tgn08-c),var(--color-tgn08-d),var(--color-tgn08-a))]"></span>Prism</a>
        <nav class="ml-auto" aria-label="Primary">
          <ul class="flex gap-1 max-sm:gap-0">
            <li><a href="#" aria-current="page" class="flex h-11 items-center rounded-[10px] px-3.5 text-sm font-medium text-tgn08-ink/80 transition-colors hover:bg-white/10 hover:text-white aria-[current=page]:bg-white/14 aria-[current=page]:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn08-c max-sm:px-2.5 max-sm:text-[13px]">Studio</a></li>
            <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3.5 text-sm font-medium text-tgn08-ink/80 transition-colors hover:bg-white/10 hover:text-white aria-[current=page]:bg-white/14 aria-[current=page]:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn08-c max-sm:px-2.5 max-sm:text-[13px]">Gallery</a></li>
            <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3.5 text-sm font-medium text-tgn08-ink/80 transition-colors hover:bg-white/10 hover:text-white aria-[current=page]:bg-white/14 aria-[current=page]:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn08-c max-sm:px-2.5 max-sm:text-[13px]">Shop</a></li>
            <li class="max-[400px]:hidden"><a href="#" class="flex h-11 items-center rounded-[10px] px-3.5 text-sm font-medium text-tgn08-ink/80 transition-colors hover:bg-white/10 hover:text-white aria-[current=page]:bg-white/14 aria-[current=page]:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn08-c max-sm:px-2.5 max-sm:text-[13px]">Info</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <div class="mx-auto max-w-2xl px-2 pt-12 pb-20 text-tgn08-ink/88 [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:text-white [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn08-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:border [&_code]:border-white/18 [&_code]:bg-white/10 [&_code]:text-white">
      <h2>Watch the border chase § the frame stays lit while you scroll</h2>
      <p>The sticky frame keeps its rotating gradient border visible the whole way down the page. Because <code>@property --angle</code> is registered as a typed <code>&lt;angle&gt;</code>, CSS can actually interpolate it — untyped custom properties snap between values.</p>
      <p>A pseudo-element sits behind the bar, one <code>--border-width</code> larger on every side, filled with a <code>conic-gradient(from var(--angle), …)</code>. The gradient rotates through 360deg; the only visible slice is the thin frame peeking around the glass bar in front.</p>
      <p>The gradient stops ARE the palette. Two or three saturated hues at a few positions read as a chasing highlight; a full oklch hue wheel reads as an iridescent ring.</p>
      <h3>The @property gate</h3>
      <p>Registered custom properties are the entire reason this animation works. Without <code>@property</code>, the browser treats <code>--angle</code> as a plain string and cannot interpolate it — the keyframe animation would snap from 0deg to 360deg with no intermediate frames.</p>
      <p>The registration tells the browser: this variable is an <code>&lt;angle&gt;</code> type, has an initial value of 0deg, and does not inherit. Now CSS can smoothly tween it, and the conic-gradient re-renders continuously.</p>
      <p>This is CSS Houdini territory — the ability to define new typed primitives. Baseline support arrived in 2024 (Firefox 128 was the last major engine). For older browsers, the border shows a static gradient at the initial angle — a graceful fallback that still looks intentional.</p>
      <h3>Mask-composite is the second half of the trick</h3>
      <p>The gradient pseudo-element fills the entire frame area, not just the border. To reveal only the border, use <code>mask-composite:exclude</code> with two masks: one for the outer edge, one for the inner content area. The subtraction leaves only the ring.</p>
      <p>This is the same technique CSS Tricks documented for gradient borders. Combined with the rotating <code>--angle</code>, it creates the lit-edge illusion without any actual border property.</p>
      <p>The alternative — a real <code>border-image</code> with an animated gradient — doesn't work because <code>border-image</code> cannot animate its gradient angle directly. The conic + mask + <code>@property</code> route is the only way in current CSS.</p>
      <h3>Polish moves</h3>
      <p>Add a <code>filter:blur(6px)</code> on the gradient pseudo-element to convert the crisp border into a soft glow halo. Or a matching <code>box-shadow</code> to bleed the colour outward for a bigger lit-edge feel.</p>
      <p>Speed via the animation duration: 6s is an elegant drift, 2s is an energetic gamer-RGB spin. Freeze one segment as an accent by dropping the animation entirely for a static gradient border.</p>
      <p>Animate <code>--angle</code> on hover only rather than continuously. The border comes alive when the user engages the nav and stays quiet otherwise — better for battery on mobile and less visually noisy on long-form content pages.</p>
      <p>A constantly-spinning border repaints every frame — respect <code>prefers-reduced-motion</code> and consider pausing it when off-screen for battery.</p>
      <h3>Where iridescent borders belong</h3>
      <p>NFT marketplaces and Web3 wallet-connect flows. The rotating rainbow reads as blockchain / crypto premium and matches audience expectation.</p>
      <p>Dev-tool marketing pages (Cursor, Warp, Zed, Raycast). The iridescent border reads as “this is a crafted product” without needing prose to say it.</p>
      <p>AI/LLM product landing pages. The gradient signals novelty and generative aesthetics without leaning on the tired holographic-mesh cliché.</p>
      <p>Gaming portals. Full RGB spin at 2s duration reads as gamer aesthetic instantly — the audience welcomes the energy.</p>
      <h3>Where it doesn't belong</h3>
      <p>Fintech dashboards for regulated audiences (banking, insurance). The animation reads as gimmicky and undermines the trust signal these products need.</p>
      <p>Healthcare and public-sector sites. Same reasoning — the accessibility-first audience needs quiet chrome, not chasing lights.</p>
      <p>Legal firm websites. ABA Model Rule 7.1 requires substantiated claims; a spinning iridescent border sends the wrong signal about seriousness.</p>
      <p>Enterprise dashboards where the user spends 8 hours a day. The animation would be genuinely irritating over that duration. Reserve for marketing surfaces, not the product itself.</p>
      <p>Keep scrolling — the sticky frame stays lit, stays glass, and demonstrates its behaviour across the full page height.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";
/* @property is an at-rule with no utility equivalent — the one piece of real CSS here. */

@property --tgn08-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tgn08-a: #ff725c;
  --color-tgn08-a: oklch(0.75 0.2 30);
  --color-tgn08-b: #e181f7;
  --color-tgn08-b: oklch(0.75 0.19 320);
  --color-tgn08-c: #5ebdff;
  --color-tgn08-c: oklch(0.78 0.16 250);
  --color-tgn08-d: #21e79b;
  --color-tgn08-d: oklch(0.82 0.18 160);
  --color-tgn08-dusk: #2b1e66;
  --color-tgn08-dusk: oklch(0.3 0.12 285);
  --color-tgn08-night: #030a26;
  --color-tgn08-night: oklch(0.16 0.06 265);
  --color-tgn08-glass: #100d26;
  --color-tgn08-glass: oklch(0.18 0.05 285);
  --color-tgn08-ink: #f1f1f8;
  --color-tgn08-ink: oklch(0.96 0.01 285);
  --font-tgn08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgn08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tgn08-spin: tgn08spin 6s linear infinite;

  @keyframes tgn08spin {
    to {
      --tgn08-angle: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-08 {
  width: 100%;
  min-height: 100svh;
}
```
