---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-glassmorphism-card-aurora-stage/"
title: "Tailwind Glassmorphism Card on Animated Aurora Stage"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "The most layered demo in the set: three drifting aurora blobs, a film-grain overlay and a rotating caustic sweep behind a double-tinted glass panel with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Card on Animated Aurora Stage
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-glassmorphism-card-aurora-stage/

The most layered demo in the set: three drifting aurora blobs, a film-grain overlay and a rotating caustic sweep behind a double-tinted glass panel with a chromatic edge and a champagne CTA. The port's win is that eleven decorative layers each state their own blur, blend mode and animation instead of hiding behind eleven class names.
## HTML
```html
<section class="twc-17 relative w-full min-h-svh flex items-center justify-center overflow-hidden px-5 py-9 bg-twc17-bg font-twc17-sans">

  <div aria-hidden="true" class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
    <div class="absolute -top-[15%] -left-[10%] size-120 rounded-full opacity-50 blur-[60px] animate-twc17-drift motion-reduce:animate-none [background:radial-gradient(circle,#f5d97b,transparent_60%)]"></div>
    <div class="absolute top-[30%] -right-[20%] size-135 rounded-full opacity-50 blur-[60px] animate-twc17-drift [animation-delay:-8s] motion-reduce:animate-none [background:radial-gradient(circle,#d4718b,transparent_60%)]"></div>
    <div class="absolute -bottom-[25%] left-1/4 size-125 rounded-full opacity-50 blur-[60px] animate-twc17-drift [animation-delay:-16s] motion-reduce:animate-none [background:radial-gradient(circle,#a78bfa,transparent_60%)]"></div>
    <div class="absolute inset-0 opacity-60 [mix-blend-mode:overlay] [background-image:radial-gradient(circle_at_15%_25%,oklch(0.87_0.11_90/0.06)_0.5px,transparent_1px),radial-gradient(circle_at_65%_45%,oklch(0.68_0.12_0/0.05)_0.5px,transparent_1px),radial-gradient(circle_at_35%_75%,oklch(0.72_0.15_290/0.05)_0.5px,transparent_1px),radial-gradient(circle_at_85%_85%,oklch(1_0_0/0.04)_0.5px,transparent_1px)] [background-size:4px_4px,5px_5px,3px_3px,6px_6px]"></div>
    <div class="absolute -top-1/2 -left-1/2 w-[200%] h-[200%] pointer-events-none [mix-blend-mode:screen] animate-twc17-caustic motion-reduce:animate-none [background:linear-gradient(115deg,transparent_40%,oklch(0.87_0.11_90/0.05)_47%,oklch(1_0_0/0.08)_50%,oklch(0.68_0.12_0/0.05)_53%,transparent_60%)]"></div>
  </div>

  <article class="group/card relative z-1 isolate w-full max-w-[380px] rounded-[28px] [transform:perspective(1200px)_rotateX(2deg)_rotateY(-2deg)] transition-transform duration-600 ease-[cubic-bezier(0.34,1.2,0.64,1)] hover:[transform:perspective(1200px)_rotateX(0deg)_rotateY(0deg)_translateY(-4px)] motion-reduce:transition-none motion-reduce:hover:[transform:perspective(1200px)_rotateX(2deg)_rotateY(-2deg)] before:absolute before:-inset-[3px] before:-z-1 before:rounded-[30px] before:blur-[1px] before:opacity-50 before:transition-opacity before:duration-400 before:content-[''] before:[background:linear-gradient(135deg,oklch(0.87_0.11_90/0.55)_0%,oklch(0.68_0.12_0/0.4)_30%,oklch(0.72_0.15_290/0.4)_60%,oklch(0.87_0.11_90/0.55)_100%)] hover:before:opacity-85 after:absolute after:-inset-[30px] after:-z-2 after:rounded-[55px] after:blur-[30px] after:pointer-events-none after:content-[''] after:[background:radial-gradient(ellipse,oklch(0.87_0.11_90/0.14)_0%,transparent_65%)]">

    <div aria-hidden="true" class="absolute inset-0 z-1 rounded-[28px] pointer-events-none border border-white/15 [background:linear-gradient(160deg,oklch(1_0_0/0.1)_0%,oklch(1_0_0/0.02)_40%,oklch(1_0_0/0.06)_100%)] [backdrop-filter:blur(24px)_saturate(1.5)_brightness(1.05)] [-webkit-backdrop-filter:blur(24px)_saturate(1.5)_brightness(1.05)] shadow-[inset_0_1px_0_oklch(1_0_0/0.22),inset_0_-1px_0_oklch(0_0_0/0.14),0_30px_60px_-20px_oklch(0_0_0/0.55)]"></div>
    <div aria-hidden="true" class="absolute inset-0 z-2 rounded-[28px] pointer-events-none [background:radial-gradient(ellipse_at_30%_15%,oklch(0.87_0.11_90/0.14)_0%,transparent_55%),radial-gradient(ellipse_at_80%_90%,oklch(0.68_0.12_0/0.1)_0%,transparent_55%)]"></div>

    <div class="relative z-3 px-5.5 pt-5.5 pb-5 text-white/95">

      <header class="flex items-center justify-between mb-4">
        <div class="flex items-center gap-2">
          <span aria-hidden="true" class="relative size-5.5 rounded-[7px] [background:linear-gradient(135deg,#f5d97b_0%,#d4a574_50%,#7c4a3e_100%)] shadow-[inset_0_1px_0_oklch(1_0_0/0.4),inset_0_-1px_0_oklch(0_0_0/0.3),0_3px_8px_oklch(0.78_0.08_70/0.4)] after:absolute after:inset-1 after:rounded-[3px] after:content-[''] after:[background:linear-gradient(135deg,transparent_40%,oklch(1_0_0/0.5)_55%,transparent_65%)]"></span>
          <span class="inline-flex items-baseline gap-1.5 font-twc17-mono text-[10.5px] font-extrabold tracking-[0.16em] text-white/90">
            LUMEN OS
            <span class="text-[8.5px] font-bold tracking-[0.1em] text-twc17-gilt/75">v2.6</span>
          </span>
        </div>
        <button type="button" aria-label="Dismiss" class="inline-flex items-center justify-center size-11 rounded-lg bg-white/6 border border-white/10 text-white/55 cursor-pointer transition-[color,background] duration-200 hover:text-white hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-twc17-gilt focus-visible:outline-offset-2">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><line x1="6" y1="6" x2="18" y2="18"/><line x1="6" y1="18" x2="18" y2="6"/></svg>
        </button>
      </header>

      <div aria-hidden="true" class="relative size-14 mb-3.5">
        <span class="absolute -inset-1.5 rounded-full blur-[8px] animate-twc17-pulse motion-reduce:animate-none [background:radial-gradient(circle,oklch(0.87_0.11_90/0.4)_0%,transparent_65%)]"></span>
        <span class="relative flex items-center justify-center size-14 rounded-2xl [background:radial-gradient(circle_at_30%_25%,oklch(1_0_0/0.35)_0%,transparent_50%),linear-gradient(135deg,#f5d97b_0%,#d4a574_60%,#8b5a3c_100%)] shadow-[inset_0_2px_0_oklch(1_0_0/0.5),inset_0_-2px_0_oklch(0.35_0.06_50/0.4),0_8px_20px_-4px_oklch(0.78_0.08_70/0.5),0_0_0_1px_oklch(1_0_0/0.12)]">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fef3c7" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v6M12 22v-6M4.93 4.93l4.24 4.24M19.07 19.07l-4.24-4.24M2 12h6M22 12h-6M4.93 19.07l4.24-4.24M19.07 4.93l-4.24 4.24"/></svg>
        </span>
      </div>

      <div class="flex flex-wrap items-center gap-1.5 mb-3">
        <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-full font-twc17-mono text-[9px] font-extrabold tracking-[0.16em] uppercase text-twc17-gilt bg-white/10 border border-white/15">
          <span aria-hidden="true" class="size-[5px] rounded-full bg-twc17-gilt shadow-[0_0_6px_oklch(0.87_0.11_90)] animate-twc17-blink motion-reduce:animate-none"></span>
          LIVE
        </span>
        <span class="inline-flex items-center px-2 py-[3px] rounded-full font-twc17-mono text-[9px] font-extrabold tracking-[0.16em] uppercase text-twc17-gilt/90 bg-twc17-gilt/10 border border-twc17-gilt/25">PREMIUM &middot; v2.6</span>
      </div>

      <h3 class="m-0 mb-2 text-[22px]/[1.2] font-bold tracking-[-0.03em] text-white [background-image:linear-gradient(180deg,#ffffff_0%,oklch(0.87_0.11_90/0.85)_130%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">Realtime intelligence, everywhere.</h3>
      <p class="m-0 mb-4.5 text-[13px]/[1.55] tracking-[-0.005em] text-white/70">Custom dashboards, predictive alerts, and voice-driven exports. Deploy across your entire stack in under a minute.</p>

      <dl class="grid grid-cols-3 gap-1 m-0 mb-4.5 px-1 py-3 rounded-2xl bg-white/4 border border-white/8">
        <div class="flex flex-col items-center gap-0.5">
          <dt class="m-0 font-twc17-mono text-[8.5px] font-bold tracking-[0.14em] uppercase text-white/50">Latency</dt>
          <dd class="m-0 text-sm font-extrabold tracking-[-0.02em] text-twc17-gilt/95 [font-variant-numeric:tabular-nums]">&lt;12ms</dd>
        </div>
        <div class="flex flex-col items-center gap-0.5 border-l border-white/10">
          <dt class="m-0 font-twc17-mono text-[8.5px] font-bold tracking-[0.14em] uppercase text-white/50">Signals</dt>
          <dd class="m-0 text-sm font-extrabold tracking-[-0.02em] text-twc17-gilt/95 [font-variant-numeric:tabular-nums]">2.4M/s</dd>
        </div>
        <div class="flex flex-col items-center gap-0.5 border-l border-white/10">
          <dt class="m-0 font-twc17-mono text-[8.5px] font-bold tracking-[0.14em] uppercase text-white/50">Uptime</dt>
          <dd class="m-0 text-sm font-extrabold tracking-[-0.02em] text-twc17-gilt/95 [font-variant-numeric:tabular-nums]">99.99</dd>
        </div>
      </dl>

      <div class="grid grid-cols-[1fr_auto] gap-1.5 mb-4">
        <a href="#upgrade" class="group/cta inline-flex items-center justify-center gap-1.5 min-h-11 px-4 rounded-2xl no-underline text-[13px] font-bold tracking-[-0.01em] text-twc17-ctaink [background:linear-gradient(180deg,#fef3c7_0%,#f5d97b_50%,#d4a574_100%)] shadow-[inset_0_1px_0_oklch(1_0_0/0.6),inset_0_-1px_0_oklch(0.35_0.06_50/0.4),0_4px_12px_oklch(0.87_0.11_90/0.4),0_0_0_1px_oklch(0.87_0.11_90/0.3)] transition-[transform,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[inset_0_1px_0_oklch(1_0_0/0.7),inset_0_-1px_0_oklch(0.35_0.06_50/0.4),0_6px_18px_oklch(0.87_0.11_90/0.6),0_0_0_1px_oklch(0.87_0.11_90/0.5)] focus-visible:outline-2 focus-visible:outline-twc17-gilt focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <span>Upgrade to Pro</span>
          <span aria-hidden="true" class="inline-flex items-center transition-transform duration-200 group-hover/cta:translate-x-[3px] motion-reduce:transition-none motion-reduce:group-hover/cta:translate-x-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </span>
        </a>
        <a href="#learn" class="inline-flex items-center justify-center min-h-11 px-3.5 rounded-2xl no-underline text-[13px] font-semibold tracking-[-0.01em] text-white bg-white/8 border border-white/15 transition-[background] duration-200 hover:bg-white/15 focus-visible:outline-2 focus-visible:outline-twc17-gilt focus-visible:outline-offset-2">Watch demo</a>
      </div>

      <footer class="flex items-center gap-2 pt-3.5 border-t border-white/8">
        <div aria-hidden="true" class="flex">
          <span class="inline-flex items-center justify-center size-[22px] rounded-full border-[1.5px] border-twc17-bg/60 text-twc17-ctaink text-[8.5px] font-extrabold [background:linear-gradient(135deg,#f5d97b,#d4a574)]">AR</span>
          <span class="inline-flex items-center justify-center size-[22px] -ml-1.5 rounded-full border-[1.5px] border-twc17-bg/60 text-twc17-ctaink text-[8.5px] font-extrabold [background:linear-gradient(135deg,#f4a2b8,#d4718b)]">JL</span>
          <span class="inline-flex items-center justify-center size-[22px] -ml-1.5 rounded-full border-[1.5px] border-twc17-bg/60 text-twc17-ctaink text-[8.5px] font-extrabold [background:linear-gradient(135deg,#c1a3f5,#a78bfa)]">MK</span>
        </div>
        <span class="text-[11px] tracking-[-0.005em] text-white/65">Trusted by <strong class="font-bold text-twc17-gilt/90">4,832</strong> teams</span>
      </footer>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc17-bg: #0a0710;
  --color-twc17-bg: oklch(0.13 0.02 315);
  --color-twc17-gilt: #f5d97b;
  --color-twc17-gilt: oklch(0.87 0.11 90);
  --color-twc17-ctaink: #3a1f15;
  --color-twc17-ctaink: oklch(0.28 0.05 40);
  --font-twc17-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc17-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc17-drift: twc17-drift 24s ease-in-out infinite;
  --animate-twc17-caustic: twc17-caustic 12s linear infinite;
  --animate-twc17-blink: twc17-blink 1.6s ease-in-out infinite;
  --animate-twc17-pulse: twc17-pulse 3.5s ease-in-out infinite;
}

@keyframes twc17-drift {
  0%,
    100% {
    transform: translate(0, 0) scale(1);
  }

  33% {
    transform: translate(30px, -20px) scale(1.05);
  }

  66% {
    transform: translate(-20px, 30px) scale(0.95);
  }
}

@keyframes twc17-caustic {
  from {
    transform: translate(-30%, -30%) rotate(0deg);
  }

  to {
    transform: translate(-30%, -30%) rotate(360deg);
  }
}

@keyframes twc17-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.4;
    transform: scale(0.8);
  }
}

@keyframes twc17-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 0.8;
  }

  50% {
    transform: scale(1.2);
    opacity: 1;
  }
}

.twc-17 {
  width: 100%;
  min-height: 100svh;
}
```
