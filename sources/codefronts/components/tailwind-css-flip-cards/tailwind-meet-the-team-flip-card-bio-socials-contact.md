---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-meet-the-team-flip-card-bio-socials-contact/"
title: "Tailwind Meet the Team Flip Card with Bio, Socials & Contact Reveal"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A staff profile whose back holds the bio, social links and a mailto action."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Meet the Team Flip Card with Bio, Socials & Contact Reveal
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-meet-the-team-flip-card-bio-socials-contact/

A staff profile whose back holds the bio, social links and a mailto action. The flip is a keyframed scale-and-turn rather than a plain spin &mdash; the card shrinks slightly at 90&deg; and settles a hair oversized, so it reads as stepping forward to introduce itself. Crucially, the port makes those back-face links reachable: on the CSS original they lived behind a hover state a touch device can never hold.
## HTML
```html
<section class="tfc-04 w-full min-h-svh grid place-items-center bg-tfc04-bg font-tfc04-sans px-5 py-10 text-tfc04-ink">
  <div class="group relative w-[300px] h-[410px] [perspective:1200px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc04-blue has-[:focus-visible]:outline-offset-4">
    <input id="tfc-04-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-04-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show Aria Chen's biography and contact links</span></label>

    <div class="relative w-full h-full [transform-style:preserve-3d] group-hover:animate-tfc04-turn group-has-checked:animate-tfc04-turn group-has-[:focus-visible]:animate-tfc04-turn motion-reduce:animate-none motion-reduce:group-has-checked:[transform:rotateY(180deg)]">

      <div class="absolute inset-0 flex flex-col items-center rounded-2xl overflow-hidden px-6 py-9 bg-linear-160 from-tfc04-panel to-tfc04-panel2 border border-tfc04-blue/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.4_0.15_260/0.55)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div class="mb-4 grid size-25 place-items-center overflow-hidden rounded-full border-[3px] border-tfc04-blue/40 bg-linear-135 from-tfc04-deep to-tfc04-deep2 shadow-[0_0_30px_oklch(0.6_0.18_260/0.25)]">
          <svg width="60" height="60" viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="22" r="14" fill="oklch(0.6 0.18 260 / 0.6)"/><ellipse cx="30" cy="54" rx="22" ry="16" fill="oklch(0.6 0.18 260 / 0.4)"/></svg>
        </div>
        <p class="mb-1.5 max-w-full truncate text-[10px] font-bold uppercase tracking-[0.15em] text-tfc04-cyan">Lead Designer</p>
        <h3 class="text-center text-[22px] font-extrabold tracking-[-0.02em] text-white">Aria Chen</h3>
        <p class="mt-1.5 rounded-full border border-tfc04-blue/20 bg-tfc04-blue/10 px-3 py-0.5 text-xs text-tfc04-muted">Product &amp; UX</p>
        <dl class="mt-6 flex gap-6 text-center">
          <div><dd class="bg-linear-135 from-tfc04-blue to-tfc04-cyan bg-clip-text text-[22px] font-extrabold tracking-[-0.02em] text-transparent">120+</dd><dt class="mt-0.5 text-[10px] uppercase tracking-[0.1em] text-tfc04-dim">Projects</dt></div>
          <div><dd class="bg-linear-135 from-tfc04-blue to-tfc04-cyan bg-clip-text text-[22px] font-extrabold tracking-[-0.02em] text-transparent">6 yrs</dd><dt class="mt-0.5 text-[10px] uppercase tracking-[0.1em] text-tfc04-dim">Experience</dt></div>
          <div><dd class="bg-linear-135 from-tfc04-blue to-tfc04-cyan bg-clip-text text-[22px] font-extrabold tracking-[-0.02em] text-transparent">98%</dd><dt class="mt-0.5 text-[10px] uppercase tracking-[0.1em] text-tfc04-dim">Rating</dt></div>
        </dl>
        <p class="mt-auto text-[10px] tracking-[0.08em] text-tfc04-dim">Hover, tap or press Space to connect &rarr;</p>
      </div>

      <div class="absolute inset-0 flex flex-col gap-4 rounded-2xl overflow-hidden p-7 bg-linear-160 from-tfc04-back to-tfc04-back2 border border-tfc04-cyan/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.4_0.1_210/0.5)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <h3 class="text-[11px] font-bold uppercase tracking-[0.15em] text-tfc04-cyan">About Aria</h3>
        <p class="text-[13px] leading-[1.7] text-tfc04-ink/65 text-pretty">Aria leads design systems and cross-platform UX at NovaTech. She specialises in accessible, data-dense interfaces that scale from mobile to enterprise dashboards.</p>
        <div class="relative z-30 flex gap-2.5">
          <a href="#" class="flex min-h-11 flex-1 items-center justify-center rounded-xl border border-white/10 bg-white/4 text-[11px] font-bold tracking-[0.06em] text-tfc04-ink/70 no-underline transition-colors duration-200 hover:border-tfc04-blue/30 hover:bg-tfc04-blue/15 hover:text-tfc04-blue focus-visible:outline-2 focus-visible:outline-tfc04-cyan focus-visible:outline-offset-2">Twitter</a>
          <a href="#" class="flex min-h-11 flex-1 items-center justify-center rounded-xl border border-white/10 bg-white/4 text-[11px] font-bold tracking-[0.06em] text-tfc04-ink/70 no-underline transition-colors duration-200 hover:border-tfc04-blue/30 hover:bg-tfc04-blue/15 hover:text-tfc04-blue focus-visible:outline-2 focus-visible:outline-tfc04-cyan focus-visible:outline-offset-2">LinkedIn</a>
          <a href="#" class="flex min-h-11 flex-1 items-center justify-center rounded-xl border border-white/10 bg-white/4 text-[11px] font-bold tracking-[0.06em] text-tfc04-ink/70 no-underline transition-colors duration-200 hover:border-tfc04-blue/30 hover:bg-tfc04-blue/15 hover:text-tfc04-blue focus-visible:outline-2 focus-visible:outline-tfc04-cyan focus-visible:outline-offset-2">Dribbble</a>
        </div>
        <a href="mailto:[email protected]" class="relative z-30 mt-auto flex min-h-11 items-center gap-2 rounded-xl border border-tfc04-blue/20 bg-linear-135 from-tfc04-blue/15 to-tfc04-cyan/8 px-4 text-xs text-tfc04-ink/75 no-underline transition-colors duration-200 hover:bg-tfc04-blue/25 focus-visible:outline-2 focus-visible:outline-tfc04-cyan focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-tfc04-blue" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/></svg>
          [email protected]
        </a>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc04-bg: #08090f;
  --color-tfc04-bg: oklch(0.14 0.015 265);
  --color-tfc04-panel: #0d1b3e;
  --color-tfc04-panel: oklch(0.22 0.07 265);
  --color-tfc04-panel2: #0a1220;
  --color-tfc04-panel2: oklch(0.17 0.03 260);
  --color-tfc04-back: #0d1117;
  --color-tfc04-back: oklch(0.17 0.01 255);
  --color-tfc04-back2: #111827;
  --color-tfc04-back2: oklch(0.2 0.025 260);
  --color-tfc04-deep: #1e3a8a;
  --color-tfc04-deep: oklch(0.35 0.14 265);
  --color-tfc04-deep2: #1e40af;
  --color-tfc04-deep2: oklch(0.4 0.17 265);
  --color-tfc04-blue: #3b82f6;
  --color-tfc04-blue: oklch(0.6 0.18 260);
  --color-tfc04-cyan: #22d3ee;
  --color-tfc04-cyan: oklch(0.78 0.13 200);
  --color-tfc04-ink: #f8fafc;
  --color-tfc04-ink: oklch(0.98 0.003 250);
  --color-tfc04-muted: #a7b4c8;
  --color-tfc04-muted: oklch(0.77 0.03 255);
  --color-tfc04-dim: #7d8899;
  --color-tfc04-dim: oklch(0.63 0.02 255);
  --font-tfc04-sans: 'Sora', system-ui, sans-serif;
  --animate-tfc04-turn: tfc04-turn 0.85s cubic-bezier(.34,1.4,.5,1) forwards;
}

@keyframes tfc04-turn {
  0% {
    transform: rotateY(0deg) scale(1);
  }

  40% {
    transform: rotateY(90deg) scale(0.85);
  }

  70% {
    transform: rotateY(160deg) scale(0.92);
  }

  100% {
    transform: rotateY(180deg) scale(1.03);
  }
}

.tfc-04 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-04 * {
    animation: none !important;
    transition-duration: 1ms !important;
  }
}
```
