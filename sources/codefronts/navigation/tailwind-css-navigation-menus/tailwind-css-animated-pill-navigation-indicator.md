---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-animated-pill-navigation-indicator/"
title: "Tailwind CSS Animated Pill Navigation Indicator"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A floating pill nav whose indicator slides between five tabs with a spring, squashes and stretches mid-flight, and recolours to each section's accent with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Animated Pill Navigation Indicator
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-animated-pill-navigation-indicator/

A floating pill nav whose indicator slides between five tabs with a spring, squashes and stretches mid-flight, and recolours to each section's accent with a matching glow. Panels below swap with a starting: fade: metrics, traffic bars and quotas. The morph re-triggers on every switch by giving each state its own keyframe utility. Zero JavaScript.
## HTML
```html
<div class="tnv-15 group/root grid min-h-svh w-full content-start justify-items-center bg-tnv15-bg bg-[radial-gradient(60%_40%_at_50%_0%,rgb(99_102_241/0.12),transparent)] px-5 py-12 font-tnv15-sans text-tnv15-ink antialiased selection:bg-tnv15-p1 selection:text-white sm:py-16">
  <input type="radio" name="tnv15" id="tnv15-1" class="sr-only" checked><input type="radio" name="tnv15" id="tnv15-2" class="sr-only"><input type="radio" name="tnv15" id="tnv15-3" class="sr-only"><input type="radio" name="tnv15" id="tnv15-4" class="sr-only"><input type="radio" name="tnv15" id="tnv15-5" class="sr-only">
  <nav aria-label="Workspace" class="relative grid w-full max-w-[40rem] grid-cols-5 gap-0.5 rounded-full border border-white/[0.08] bg-white/[0.04] p-[5px] shadow-[0_12px_40px_-12px_rgb(0_0_0/0.6)] group-has-[input:focus-visible]/root:ring-2 group-has-[input:focus-visible]/root:ring-white/40 [&_label]:relative [&_label]:z-10 [&_label]:flex [&_label]:h-11 [&_label]:cursor-pointer [&_label]:items-center [&_label]:justify-center [&_label]:gap-1.5 [&_label]:rounded-full [&_label]:text-[13px] [&_label]:font-semibold [&_label]:text-tnv15-mut [&_label]:transition-colors [&_label]:duration-300 [&_label]:select-none [&_label:hover]:text-white [&_svg]:size-4 [&_svg]:flex-none [&_label>span]:max-sm:sr-only">
    <span aria-hidden="true" class="absolute inset-y-[5px] left-[5px] z-0 w-[calc((100%-18px)/5)] transition-transform duration-[450ms] ease-[cubic-bezier(.34,1.4,.64,1)] [--pill:var(--color-tnv15-p1)] before:absolute before:inset-0 before:rounded-full before:bg-(--pill) before:shadow-[0_0_24px_-4px_var(--pill)] before:transition-[background-color,box-shadow] before:duration-300 before:content-[''] group-has-[#tnv15-1:checked]/root:before:animate-tnv15-m1 group-has-[#tnv15-2:checked]/root:translate-x-[calc(100%+2px)] group-has-[#tnv15-2:checked]/root:[--pill:var(--color-tnv15-p2)] group-has-[#tnv15-2:checked]/root:before:animate-tnv15-m2 group-has-[#tnv15-3:checked]/root:translate-x-[calc(200%+4px)] group-has-[#tnv15-3:checked]/root:[--pill:var(--color-tnv15-p3)] group-has-[#tnv15-3:checked]/root:before:animate-tnv15-m3 group-has-[#tnv15-4:checked]/root:translate-x-[calc(300%+6px)] group-has-[#tnv15-4:checked]/root:[--pill:var(--color-tnv15-p4)] group-has-[#tnv15-4:checked]/root:before:animate-tnv15-m4 group-has-[#tnv15-5:checked]/root:translate-x-[calc(400%+8px)] group-has-[#tnv15-5:checked]/root:[--pill:var(--color-tnv15-p5)] group-has-[#tnv15-5:checked]/root:before:animate-tnv15-m5 motion-reduce:transition-none motion-reduce:before:animate-none!"></span>
    <label for="tnv15-1" class="group-has-[#tnv15-1:checked]/root:text-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg><span>Overview</span></label>
    <label for="tnv15-2" class="group-has-[#tnv15-2:checked]/root:text-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg><span>Analytics</span></label>
    <label for="tnv15-3" class="group-has-[#tnv15-3:checked]/root:text-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg><span>Customers</span></label>
    <label for="tnv15-4" class="group-has-[#tnv15-4:checked]/root:text-black"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18"/></svg><span>Orders</span></label>
    <label for="tnv15-5" class="group-has-[#tnv15-5:checked]/root:text-black"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 1v3M12 20v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M1 12h3M20 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/></svg><span>Settings</span></label>
  </nav>
  <div class="mt-10 w-full max-w-3xl [&>section]:hidden [&>section]:overflow-hidden [&>section]:rounded-[20px] [&>section]:border [&>section]:border-white/[0.07] [&>section]:bg-tnv15-surface [&>section]:transition-[opacity,translate] [&>section]:duration-300 [&>section]:starting:translate-y-2 [&>section]:starting:opacity-0 [&_header]:flex [&_header]:items-start [&_header]:gap-5 [&_header]:px-7 [&_header]:pt-8 sm:[&_header]:px-9 [&_h2]:text-xl [&_h2]:font-bold [&_h2]:tracking-[-0.02em] [&_header_p]:mt-1.5 [&_header_p]:text-[15px]/[1.6] [&_header_p]:text-tnv15-mut [&_[data-ic]]:grid [&_[data-ic]]:size-[52px] [&_[data-ic]]:flex-none [&_[data-ic]]:place-items-center [&_[data-ic]]:rounded-2xl [&_[data-ic]_svg]:size-6 [&_dl]:grid [&_dl]:gap-3.5 [&_dl]:px-7 [&_dl]:pt-7 [&_dl]:pb-8 sm:[&_dl]:grid-cols-3 sm:[&_dl]:px-9 [&_dl>div]:rounded-xl [&_dl>div]:bg-tnv15-surface2 [&_dl>div]:px-5 [&_dl>div]:py-4 [&_dd]:text-2xl [&_dd]:font-bold [&_dd]:tracking-[-0.03em] [&_dt]:order-last [&_dt]:mt-1 [&_dt]:text-[13px] [&_dt]:text-tnv15-mut [&_dl>div]:flex [&_dl>div]:flex-col">
    <section class="group-has-[#tnv15-1:checked]/root:block"><header><span data-ic class="bg-tnv15-p1"><svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.75" aria-hidden="true"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg></span><div><h2>Overview</h2><p>The pill slides on a spring, squashes mid-flight and takes on each tab's colour.</p></div></header><dl><div><dt>Total revenue</dt><dd>$128k</dd></div><div><dt>Active users</dt><dd>8,412</dd></div><div><dt>Uptime</dt><dd>99.98%</dd></div></dl></section>
    <section class="group-has-[#tnv15-2:checked]/root:block"><header><span data-ic class="bg-tnv15-p2"><svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.75" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></span><div><h2>Analytics</h2><p>Where this month's traffic came from.</p></div></header>
      <ul class="grid gap-4 px-7 pt-7 pb-8 text-[13px] font-medium text-tnv15-mut sm:px-9 [&_i]:mt-2 [&_i]:block [&_i]:h-1.5 [&_i]:overflow-hidden [&_i]:rounded-full [&_i]:bg-white/[0.06] [&_b]:block [&_b]:h-full [&_b]:rounded-full [&_b]:transition-[width] [&_b]:duration-700 [&_b]:starting:w-0! [&_li>span]:flex [&_li>span]:justify-between">
        <li><span><span>Organic search</span><span class="text-tnv15-ink">48%</span></span><i><b class="w-[48%] bg-tnv15-p2"></b></i></li>
        <li><span><span>Direct</span><span class="text-tnv15-ink">31%</span></span><i><b class="w-[31%] bg-violet-400"></b></i></li>
        <li><span><span>Social</span><span class="text-tnv15-ink">14%</span></span><i><b class="w-[14%] bg-violet-300"></b></i></li>
      </ul></section>
    <section class="group-has-[#tnv15-3:checked]/root:block"><header><span data-ic class="bg-tnv15-p3"><svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.75" aria-hidden="true"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></span><div><h2>Customers</h2><p>Each panel enters with <code class="font-tnv15-mono text-[0.85em]">starting:</code>, no keyframes needed.</p></div></header><dl><div><dt>Total customers</dt><dd>3,241</dd></div><div><dt>New this week</dt><dd>128</dd></div><div><dt>Avg rating</dt><dd>4.8 / 5</dd></div></dl></section>
    <section class="group-has-[#tnv15-4:checked]/root:block"><header><span data-ic class="bg-tnv15-p4"><svg viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.75" aria-hidden="true"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18"/></svg></span><div><h2>Orders</h2><p>On light accents like amber the label flips to black to keep 4.5:1 contrast.</p></div></header><dl><div><dt>Total orders</dt><dd>1,093</dd></div><div><dt>Pending</dt><dd>47</dd></div><div><dt>Avg order value</dt><dd>$68</dd></div></dl></section>
    <section class="group-has-[#tnv15-5:checked]/root:block"><header><span data-ic class="bg-tnv15-p5"><svg viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.75" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 1v3M12 20v3M1 12h3M20 12h3"/></svg></span><div><h2>Settings</h2><p>Zero JavaScript: radios, <code class="font-tnv15-mono text-[0.85em]">:has()</code> and five keyframe names.</p></div></header>
      <ul class="grid gap-4 px-7 pt-7 pb-8 text-[13px] font-medium text-tnv15-mut sm:px-9 [&_i]:mt-2 [&_i]:block [&_i]:h-1.5 [&_i]:overflow-hidden [&_i]:rounded-full [&_i]:bg-white/[0.06] [&_b]:block [&_b]:h-full [&_b]:rounded-full [&_b]:transition-[width] [&_b]:duration-700 [&_b]:starting:w-0! [&_li>span]:flex [&_li>span]:justify-between">
        <li><span><span>Storage used</span><span class="text-tnv15-ink">62%</span></span><i><b class="w-[62%] bg-tnv15-p5"></b></i></li>
        <li><span><span>API quota</span><span class="text-tnv15-ink">28%</span></span><i><b class="w-[28%] bg-emerald-300"></b></i></li>
      </ul></section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv15-bg: #030712;
  --color-tnv15-bg: oklch(0.13 0.028 262);
  --color-tnv15-surface: #0d1117;
  --color-tnv15-surface: oklch(0.18 0.015 260);
  --color-tnv15-surface2: #161b26;
  --color-tnv15-surface2: oklch(0.22 0.02 265);
  --color-tnv15-ink: #f9fafb;
  --color-tnv15-ink: oklch(0.985 0.002 248);
  --color-tnv15-mut: #9ca3af;
  --color-tnv15-mut: oklch(0.707 0.022 261);
  --color-tnv15-p1: #6366f1;
  --color-tnv15-p1: oklch(0.585 0.233 277);
  --color-tnv15-p2: #8b5cf6;
  --color-tnv15-p2: oklch(0.606 0.25 293);
  --color-tnv15-p3: #ec4899;
  --color-tnv15-p3: oklch(0.656 0.241 354);
  --color-tnv15-p4: #f59e0b;
  --color-tnv15-p4: oklch(0.769 0.188 70);
  --color-tnv15-p5: #10b981;
  --color-tnv15-p5: oklch(0.696 0.17 162);
  --font-tnv15-sans: 'Hanken Grotesk', system-ui, sans-serif;
  --font-tnv15-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tnv15-m1: tnv15-m1 0.45s ease-out;
  --animate-tnv15-m2: tnv15-m2 0.45s ease-out;
  --animate-tnv15-m3: tnv15-m3 0.45s ease-out;
  --animate-tnv15-m4: tnv15-m4 0.45s ease-out;
  --animate-tnv15-m5: tnv15-m5 0.45s ease-out;

  @keyframes tnv15-m1 {
    0%,
        100% {
      scale: 1 1;
    }

    45% {
      scale: 1.12 0.72;
    }
  }

  @keyframes tnv15-m2 {
    0%,
        100% {
      scale: 1 1;
    }

    45% {
      scale: 1.12 0.72;
    }
  }

  @keyframes tnv15-m3 {
    0%,
        100% {
      scale: 1 1;
    }

    45% {
      scale: 1.12 0.72;
    }
  }

  @keyframes tnv15-m4 {
    0%,
        100% {
      scale: 1 1;
    }

    45% {
      scale: 1.12 0.72;
    }
  }

  @keyframes tnv15-m5 {
    0%,
        100% {
      scale: 1 1;
    }

    45% {
      scale: 1.12 0.72;
    }
  }
}

.tnv-15 {
  width: 100%;
  min-height: 100svh;
}
```
