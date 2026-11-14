---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-grain-opacity-mix-blend-mode-matrix/"
title: "Tailwind Grain Opacity and mix-blend-mode Composite Matrix"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Grain has two dials after generation: how strong it is and how it composites."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Grain Opacity and mix-blend-mode Composite Matrix
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-grain-opacity-mix-blend-mode-matrix/

Grain has two dials after generation: how strong it is and how it composites. This is the full matrix — eight mix-blend-mode values against one identical noise layer, plus a five-stop opacity scale with the production band marked. The port deletes every inline style attribute the CSS version needed: each mode is a real utility, and isolate sits on the surface that owns the blend.
## HTML
```html
<section class="gtw-04 relative block w-full min-h-svh bg-gtw04-bg text-gtw04-ink" aria-labelledby="gtw-04-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-04-theme" class="gtw-04-theme peer sr-only">
    <label for="gtw-04-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw04-line bg-gtw04-surf text-gtw04-ink cursor-pointer transition-colors duration-200 hover:border-gtw04-acc peer-focus-visible:outline-2 peer-focus-visible:outline-gtw04-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(76rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2.2rem,5vw,3.4rem)]">
    <header class="max-w-[46rem] grid gap-3">
      <p class="m-0 font-gtw04-mono text-[0.72rem] font-medium tracking-[0.18em] uppercase text-gtw04-acc">Composite reference · 04</p>
      <h1 id="gtw-04-title" class="m-0 font-gtw04-display text-[clamp(2rem,5.4vw,3.5rem)] font-semibold leading-[1.03] tracking-[-0.035em] text-balance">Same noise. Eight composites. Only three ship.</h1>
      <p class="m-0 max-w-[40rem] text-gtw04-mut text-[clamp(0.95rem,1.9vw,1.09rem)] text-pretty">One grain layer, one opacity, eight <code class="font-gtw04-mono text-[0.9em]">mix-blend-mode</code> values — each one a real utility now. Then the opacity scale, with the band that survives design review marked on it.</p>
    </header>

    <section class="grid gap-4" aria-labelledby="gtw-04-h-op">
      <div class="flex flex-wrap items-baseline gap-x-4 gap-y-[0.35rem] pb-[0.6rem] border-b border-gtw04-line">
        <h2 id="gtw-04-h-op" class="m-0 font-gtw04-display text-[clamp(1.1rem,2.6vw,1.4rem)] font-semibold leading-tight tracking-[-0.015em]">Opacity scale</h2>
        <p class="m-0 max-w-[44rem] text-gtw04-mut text-[0.88rem] text-pretty">Blend held at <code class="font-gtw04-mono text-[0.9em]">overlay</code>. The marked band is where production lives.</p>
      </div>
      <ol class="list-none m-0 p-0 grid gap-[clamp(0.5rem,1.4vw,0.9rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,8.5rem),1fr))]">
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(5.5rem,12vw,7.5rem)] rounded-xl overflow-hidden bg-[linear-gradient(150deg,var(--color-gtw04-acc),var(--color-gtw04-acc2)_70%,var(--color-gtw04-surf))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:mix-blend-overlay after:opacity-[0.02]"></span>
          <span class="font-gtw04-mono text-[0.88rem] font-medium leading-none">0.02</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">invisible</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(5.5rem,12vw,7.5rem)] rounded-xl overflow-hidden shadow-[0_0_0_2px_var(--color-gtw04-acc)] bg-[linear-gradient(150deg,var(--color-gtw04-acc),var(--color-gtw04-acc2)_70%,var(--color-gtw04-surf))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:mix-blend-overlay after:opacity-[0.05]"></span>
          <span class="font-gtw04-mono text-[0.88rem] font-medium leading-none">0.05</span>
          <span class="text-[0.72rem] font-semibold tracking-[0.06em] uppercase text-gtw04-acc">light UI</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(5.5rem,12vw,7.5rem)] rounded-xl overflow-hidden shadow-[0_0_0_2px_var(--color-gtw04-acc)] bg-[linear-gradient(150deg,var(--color-gtw04-acc),var(--color-gtw04-acc2)_70%,var(--color-gtw04-surf))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:mix-blend-overlay after:opacity-[0.09]"></span>
          <span class="font-gtw04-mono text-[0.88rem] font-medium leading-none">0.09</span>
          <span class="text-[0.72rem] font-semibold tracking-[0.06em] uppercase text-gtw04-acc">dark UI</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(5.5rem,12vw,7.5rem)] rounded-xl overflow-hidden bg-[linear-gradient(150deg,var(--color-gtw04-acc),var(--color-gtw04-acc2)_70%,var(--color-gtw04-surf))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:mix-blend-overlay after:opacity-[0.18]"></span>
          <span class="font-gtw04-mono text-[0.88rem] font-medium leading-none">0.18</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">editorial</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(5.5rem,12vw,7.5rem)] rounded-xl overflow-hidden bg-[linear-gradient(150deg,var(--color-gtw04-acc),var(--color-gtw04-acc2)_70%,var(--color-gtw04-surf))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:mix-blend-overlay after:opacity-[0.4]"></span>
          <span class="font-gtw04-mono text-[0.88rem] font-medium leading-none">0.40</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">effect, not texture</span>
        </li>
      </ol>
    </section>

    <section class="grid gap-4" aria-labelledby="gtw-04-h-blend">
      <div class="flex flex-wrap items-baseline gap-x-4 gap-y-[0.35rem] pb-[0.6rem] border-b border-gtw04-line">
        <h2 id="gtw-04-h-blend" class="m-0 font-gtw04-display text-[clamp(1.1rem,2.6vw,1.4rem)] font-semibold leading-tight tracking-[-0.015em]">Blend mode matrix</h2>
        <p class="m-0 max-w-[44rem] text-gtw04-mut text-[0.88rem] text-pretty">Opacity held at <code class="font-gtw04-mono text-[0.9em]">0.32</code> so the differences are legible at tile size.</p>
      </div>
      <ul class="list-none m-0 p-0 grid gap-[clamp(0.55rem,1.5vw,0.95rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,9.5rem),1fr))]">
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] rounded-xl overflow-hidden shadow-[0_0_0_2px_var(--color-gtw04-acc)] bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-gtw04-acc),var(--color-gtw04-acc2)_40%,var(--color-gtw04-surf)_78%,var(--color-gtw04-acc))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[var(--gtw04-op)] after:mix-blend-overlay"></span>
          <span class="font-gtw04-mono text-[0.85rem] font-medium leading-tight text-gtw04-acc">overlay</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">embedded · default</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] rounded-xl overflow-hidden shadow-[0_0_0_2px_var(--color-gtw04-acc)] bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-gtw04-acc),var(--color-gtw04-acc2)_40%,var(--color-gtw04-surf)_78%,var(--color-gtw04-acc))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[var(--gtw04-op)] after:mix-blend-soft-light"></span>
          <span class="font-gtw04-mono text-[0.85rem] font-medium leading-tight text-gtw04-acc">soft-light</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">gentle · large fields</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] rounded-xl overflow-hidden shadow-[0_0_0_2px_var(--color-gtw04-acc)] bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-gtw04-acc),var(--color-gtw04-acc2)_40%,var(--color-gtw04-surf)_78%,var(--color-gtw04-acc))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[var(--gtw04-op)] after:mix-blend-multiply"></span>
          <span class="font-gtw04-mono text-[0.85rem] font-medium leading-tight text-gtw04-acc">multiply</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">darkens only · paper</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] rounded-xl overflow-hidden bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-gtw04-acc),var(--color-gtw04-acc2)_40%,var(--color-gtw04-surf)_78%,var(--color-gtw04-acc))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[var(--gtw04-op)] after:mix-blend-screen"></span>
          <span class="font-gtw04-mono text-[0.85rem] font-medium leading-tight">screen</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">lightens only · dust</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] rounded-xl overflow-hidden bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-gtw04-acc),var(--color-gtw04-acc2)_40%,var(--color-gtw04-surf)_78%,var(--color-gtw04-acc))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[var(--gtw04-op)] after:mix-blend-luminosity"></span>
          <span class="font-gtw04-mono text-[0.85rem] font-medium leading-tight">luminosity</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">hue-safe · photos</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] rounded-xl overflow-hidden bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-gtw04-acc),var(--color-gtw04-acc2)_40%,var(--color-gtw04-surf)_78%,var(--color-gtw04-acc))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[var(--gtw04-op)] after:mix-blend-color-burn"></span>
          <span class="font-gtw04-mono text-[0.85rem] font-medium leading-tight">color-burn</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">clips hard</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] rounded-xl overflow-hidden bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-gtw04-acc),var(--color-gtw04-acc2)_40%,var(--color-gtw04-surf)_78%,var(--color-gtw04-acc))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[var(--gtw04-op)] after:mix-blend-hard-light"></span>
          <span class="font-gtw04-mono text-[0.85rem] font-medium leading-tight">hard-light</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">too contrasty</span>
        </li>
        <li class="group grid gap-[0.3rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] rounded-xl overflow-hidden bg-[conic-gradient(from_210deg_at_30%_20%,var(--color-gtw04-acc),var(--color-gtw04-acc2)_40%,var(--color-gtw04-surf)_78%,var(--color-gtw04-acc))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[var(--gtw04-op)] after:mix-blend-normal"></span>
          <span class="font-gtw04-mono text-[0.85rem] font-medium leading-tight">normal</span>
          <span class="text-[0.72rem] tracking-[0.06em] uppercase text-gtw04-mut">grey veil · avoid</span>
        </li>
      </ul>
    </section>

    <section class="relative isolate overflow-hidden rounded-[20px] bg-[radial-gradient(130%_130%_at_78%_8%,var(--color-gtw04-acc2)_0%,var(--color-gtw04-acc)_38%,var(--color-gtw04-surf)_82%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw04-noise)] after:opacity-[0.07] after:mix-blend-soft-light" aria-labelledby="gtw-04-h-live">
      <div class="relative z-[1] grid gap-[0.7rem] max-w-[40rem] p-[clamp(1.8rem,5vw,3.2rem)]">
        <h2 id="gtw-04-h-live" class="m-0 font-gtw04-display text-[clamp(1.1rem,2.6vw,1.4rem)] font-semibold leading-tight tracking-[-0.015em] text-white">The same rule at hero scale</h2>
        <p class="m-0 max-w-[44rem] text-white text-[0.88rem] text-pretty">Modes that look identical on a 140px tile diverge across a full-bleed field. This panel runs <code class="font-gtw04-mono text-[0.9em]">after:mix-blend-soft-light after:opacity-[0.07]</code> — the setting that survives the most design reviews.</p>
        <p class="m-0 justify-self-start px-[0.85rem] py-[0.6rem] rounded-[10px] bg-[oklch(0.15_0.04_300/0.55)] backdrop-blur-[3px] text-white font-gtw04-mono text-[0.84rem] leading-[1.5]"><code>isolate</code> is on this panel. Remove it and the grain blends against the page instead.</p>
      </div>
    </section>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw04-bg: #0f0b16;
  --color-gtw04-bg: oklch(0.17 0.03 300);
  --color-gtw04-surf: #191128;
  --color-gtw04-surf: oklch(0.23 0.05 300);
  --color-gtw04-line: #2f2145;
  --color-gtw04-line: oklch(0.32 0.06 300);
  --color-gtw04-ink: #f0eaff;
  --color-gtw04-ink: oklch(0.95 0.02 300);
  --color-gtw04-mut: #a394c4;
  --color-gtw04-mut: oklch(0.72 0.05 300);
  --color-gtw04-acc: #a78bfa;
  --color-gtw04-acc: oklch(0.75 0.16 296);
  --color-gtw04-acc2: #f472b6;
  --color-gtw04-acc2: oklch(0.72 0.19 350);
  --font-gtw04-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw04-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-04 {
  width: 100%;
  min-height: 100svh;
  --gtw04-op: 0.32;
  --gtw04-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='gtw04n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23gtw04n)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-04:has(.gtw-04-theme:checked) {
  --color-gtw04-bg: #f6f3fc;
  --color-gtw04-bg: oklch(0.97 0.01 300);
  --color-gtw04-surf: #ffffff;
  --color-gtw04-surf: oklch(1 0 0);
  --color-gtw04-line: #e0d7f2;
  --color-gtw04-line: oklch(0.89 0.03 300);
  --color-gtw04-ink: #140f1f;
  --color-gtw04-ink: oklch(0.2 0.03 300);
  --color-gtw04-mut: #63558a;
  --color-gtw04-mut: oklch(0.49 0.07 295);
  --color-gtw04-acc: #7c3aed;
  --color-gtw04-acc: oklch(0.54 0.23 295);
  --color-gtw04-acc2: #db2777;
  --color-gtw04-acc2: oklch(0.56 0.21 355);
  --gtw04-op: 0.26;
}

@media (prefers-color-scheme: light) {
  .gtw-04 {
    --color-gtw04-bg: #f6f3fc;
    --color-gtw04-bg: oklch(0.97 0.01 300);
    --color-gtw04-surf: #ffffff;
    --color-gtw04-surf: oklch(1 0 0);
    --color-gtw04-line: #e0d7f2;
    --color-gtw04-line: oklch(0.89 0.03 300);
    --color-gtw04-ink: #140f1f;
    --color-gtw04-ink: oklch(0.2 0.03 300);
    --color-gtw04-mut: #63558a;
    --color-gtw04-mut: oklch(0.49 0.07 295);
    --color-gtw04-acc: #7c3aed;
    --color-gtw04-acc: oklch(0.54 0.23 295);
    --color-gtw04-acc2: #db2777;
    --color-gtw04-acc2: oklch(0.56 0.21 355);
    --gtw04-op: 0.26;
  }

  .gtw-04:has(.gtw-04-theme:checked) {
    --color-gtw04-bg: #0f0b16;
    --color-gtw04-bg: oklch(0.17 0.03 300);
    --color-gtw04-surf: #191128;
    --color-gtw04-surf: oklch(0.23 0.05 300);
    --color-gtw04-line: #2f2145;
    --color-gtw04-line: oklch(0.32 0.06 300);
    --color-gtw04-ink: #f0eaff;
    --color-gtw04-ink: oklch(0.95 0.02 300);
    --color-gtw04-mut: #a394c4;
    --color-gtw04-mut: oklch(0.72 0.05 300);
    --color-gtw04-acc: #a78bfa;
    --color-gtw04-acc: oklch(0.75 0.16 296);
    --color-gtw04-acc2: #f472b6;
    --color-gtw04-acc2: oklch(0.72 0.19 350);
    --gtw04-op: 0.32;
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-04:has(.gtw-04-theme:checked) {
    --color-gtw04-bg: #f6f3fc;
    --color-gtw04-bg: oklch(0.97 0.01 300);
    --color-gtw04-surf: #ffffff;
    --color-gtw04-surf: oklch(1 0 0);
    --color-gtw04-line: #e0d7f2;
    --color-gtw04-line: oklch(0.89 0.03 300);
    --color-gtw04-ink: #140f1f;
    --color-gtw04-ink: oklch(0.2 0.03 300);
    --color-gtw04-mut: #63558a;
    --color-gtw04-mut: oklch(0.49 0.07 295);
    --color-gtw04-acc: #7c3aed;
    --color-gtw04-acc: oklch(0.54 0.23 295);
    --color-gtw04-acc2: #db2777;
    --color-gtw04-acc2: oklch(0.56 0.21 355);
    --gtw04-op: 0.26;
  }
}
```
