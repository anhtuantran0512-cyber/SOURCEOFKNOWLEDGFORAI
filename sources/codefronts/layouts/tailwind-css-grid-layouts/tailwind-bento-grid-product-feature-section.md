---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-bento-grid-product-feature-section/"
title: "Tailwind Bento Grid for a Product Feature Section"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "The feature section every modern product page ships: a 2×2 hero tile with real numbers, a photo tile, a metric tile and satellites — each with its own accent…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bento Grid for a Product Feature Section
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-bento-grid-product-feature-section/

The feature section every modern product page ships: a 2×2 hero tile with real numbers, a photo tile, a metric tile and satellites — each with its own accent driven by a single inline custom property.
## HTML
```html
<section class="tgx-09 w-full min-h-svh bg-tgx09-bg font-tgx09-sans p-6">
  <header class="flex flex-col gap-1.5 mb-5">
    <p class="font-tgx09-mono text-[0.66rem] tracking-[0.18em] uppercase text-tgx09-dim">Lumen 3.0</p>
    <h2 class="text-[1.5rem] font-semibold tracking-[-0.015em] text-white">Everything your team watches, on one board</h2>
  </header>
  <div class="grid grid-cols-4 max-sm:grid-cols-2 auto-rows-[minmax(104px,auto)] gap-3">
    <article style="--glow:oklch(0.78 0.16 300)" class="col-span-2 row-span-2 max-sm:col-span-2 flex flex-col justify-between gap-4 rounded-2xl p-5 bg-tgx09-tile bg-[image:radial-gradient(140%_120%_at_15%_0%,color-mix(in_oklab,var(--glow)_18%,transparent),transparent_58%)] border border-[color-mix(in_oklab,var(--glow)_30%,oklch(0.32_0.02_290))] transition duration-200 hover:-translate-y-1 hover:shadow-[0_18px_36px_-18px_color-mix(in_oklab,var(--glow)_45%,transparent)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="flex flex-col gap-2">
        <h3 class="text-[clamp(1.2rem,2.6vw,1.6rem)] leading-[1.15] font-semibold text-[var(--glow)]">Real-time pipeline health</h3>
        <p class="text-[0.85rem] leading-[1.55] text-tgx09-dim max-w-[36ch]">Every deploy, queue and worker in one view, updated as events land — no refresh, no polling loop of your own.</p>
      </div>
      <dl class="grid grid-cols-3 gap-3 pt-3 border-t border-white/10">
        <div><dt class="text-[0.6rem] uppercase tracking-[0.1em] text-tgx09-dim">Events/s</dt><dd class="text-[1.1rem] font-semibold tabular-nums text-white">48k</dd></div>
        <div><dt class="text-[0.6rem] uppercase tracking-[0.1em] text-tgx09-dim">p99</dt><dd class="text-[1.1rem] font-semibold tabular-nums text-white">62ms</dd></div>
        <div><dt class="text-[0.6rem] uppercase tracking-[0.1em] text-tgx09-dim">Uptime</dt><dd class="text-[1.1rem] font-semibold tabular-nums text-white">99.99%</dd></div>
      </dl>
    </article>
    <article style="--glow:oklch(0.85 0.16 140)" class="flex flex-col justify-end gap-1.5 rounded-2xl p-4 bg-tgx09-tile bg-[image:radial-gradient(140%_120%_at_15%_0%,color-mix(in_oklab,var(--glow)_18%,transparent),transparent_58%)] border border-[color-mix(in_oklab,var(--glow)_30%,oklch(0.32_0.02_290))] transition duration-200 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <p class="text-[1.6rem] font-semibold tabular-nums leading-none text-[var(--glow)]">−41%</p>
      <h4 class="text-[0.86rem] font-medium text-white">Mean time to detect</h4>
      <p class="text-[0.74rem] leading-[1.45] text-tgx09-dim">After switching alerts to streams.</p>
    </article>
    <article style="--glow:oklch(0.82 0.14 200)" class="row-span-2 overflow-hidden flex flex-col rounded-2xl bg-tgx09-tile border border-[color-mix(in_oklab,var(--glow)_30%,oklch(0.32_0.02_290))] transition duration-200 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="aspect-[4/3] overflow-hidden"><img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600&h=450&q=80&auto=format&fit=crop" alt="Developer workstation with a code editor open on screen" loading="lazy" class="w-full h-full object-cover"></div>
      <div class="flex flex-col gap-1.5 p-4">
        <h4 class="text-[0.9rem] font-semibold text-[var(--glow)]">Built for the terminal crowd</h4>
        <p class="text-[0.76rem] leading-[1.5] text-tgx09-dim">Every board has a CLI equivalent and a stable JSON export.</p>
      </div>
    </article>
    <article style="--glow:oklch(0.8 0.15 60)" class="col-span-2 flex items-center justify-between gap-4 rounded-2xl p-4 bg-tgx09-tile bg-[image:radial-gradient(140%_120%_at_15%_0%,color-mix(in_oklab,var(--glow)_18%,transparent),transparent_58%)] border border-[color-mix(in_oklab,var(--glow)_30%,oklch(0.32_0.02_290))] transition duration-200 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="flex flex-col gap-1">
        <h4 class="text-[0.9rem] font-semibold text-[var(--glow)]">Traffic, last 12 hours</h4>
        <p class="text-[0.74rem] text-tgx09-dim">Steady climb after the 14:00 release.</p>
      </div>
      <div role="img" aria-label="Bar chart rising across 10 intervals" class="grid grid-cols-10 items-end gap-[3px] h-12 w-[45%] min-w-[120px]">
        <i style="--v:32%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/70"></i><i style="--v:44%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/70"></i><i style="--v:38%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/70"></i><i style="--v:56%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/70"></i><i style="--v:62%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/70"></i><i style="--v:58%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/70"></i><i style="--v:74%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/70"></i><i style="--v:80%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/70"></i><i style="--v:88%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]/85"></i><i style="--v:96%" class="h-[var(--v)] rounded-t-[2px] bg-[var(--glow)]"></i>
      </div>
    </article>
    <article style="--glow:oklch(0.78 0.13 250)" class="flex flex-col justify-end gap-1.5 rounded-2xl p-4 bg-tgx09-tile bg-[image:radial-gradient(140%_120%_at_15%_0%,color-mix(in_oklab,var(--glow)_18%,transparent),transparent_58%)] border border-[color-mix(in_oklab,var(--glow)_30%,oklch(0.32_0.02_290))] transition duration-200 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <h4 class="text-[0.9rem] font-semibold text-[var(--glow)]">SOC 2 Type II</h4>
      <p class="text-[0.74rem] leading-[1.45] text-tgx09-dim">Audited annually. Logs stay in your region.</p>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx09-bg: #17141f;
  --color-tgx09-bg: oklch(0.16 0.015 290);
  --color-tgx09-tile: #241f31;
  --color-tgx09-tile: oklch(0.22 0.02 290);
  --color-tgx09-dim: #b3aec2;
  --color-tgx09-dim: oklch(0.76 0.02 290);
  --font-tgx09-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx09-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-09 {
  width: 100%;
  min-height: 100svh;
}
```
