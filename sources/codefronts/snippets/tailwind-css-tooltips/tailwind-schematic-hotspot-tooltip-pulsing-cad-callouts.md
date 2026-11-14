---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-schematic-hotspot-tooltip-pulsing-cad-callouts/"
title: "Tailwind Schematic Hotspot Tooltip with Pulsing CAD Callouts"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "For product diagrams and exploded views: four pulsing red discs pin a wireframe drawing, and hovering or focusing one reveals a numbered callout with part…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Schematic Hotspot Tooltip with Pulsing CAD Callouts
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-schematic-hotspot-tooltip-pulsing-cad-callouts/

For product diagrams and exploded views: four pulsing red discs pin a wireframe drawing, and hovering or focusing one reveals a numbered callout with part name, prose and a monospaced spec grid. The port's win is peer — the CSS original's .hot:hover + .leader + .note chain broke the moment anything was inserted between the two elements; peer-hover: compiles to a general sibling combinator and does not.
## HTML
```html
<section class="ttp-01 w-full min-h-svh flex items-center justify-center px-6 py-8 bg-ttp01-stage font-ttp01-sans text-ttp01-ink bg-[linear-gradient(var(--color-ttp01-grid)_1px,transparent_1px),linear-gradient(90deg,var(--color-ttp01-grid)_1px,transparent_1px)] bg-[size:24px_24px]">
  <div class="relative w-full max-w-[760px] aspect-[16/10] bg-ttp01-paper border border-ttp01-edge before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:bg-[linear-gradient(var(--color-ttp01-grid2)_1px,transparent_1px),linear-gradient(90deg,var(--color-ttp01-grid2)_1px,transparent_1px)] before:bg-[size:18px_18px]">
    <span class="absolute top-1.5 left-1.5 w-3 h-3 border border-ttp01-tick border-r-0 border-b-0"></span>
    <span class="absolute top-1.5 right-1.5 w-3 h-3 border border-ttp01-tick border-l-0 border-b-0"></span>
    <span class="absolute bottom-1.5 left-1.5 w-3 h-3 border border-ttp01-tick border-r-0 border-t-0"></span>
    <span class="absolute bottom-1.5 right-1.5 w-3 h-3 border border-ttp01-tick border-l-0 border-t-0"></span>

    <div class="absolute top-3 left-4 right-4 z-2 flex justify-between font-ttp01-mono text-[10px] tracking-[0.15em] uppercase text-ttp01-meta">
      <span>DWG-0142-A · Camera / Exploded View</span>
      <span class="text-right leading-[1.6]">Scale 1:1 · Rev 04<br>14.MAY.2026</span>
    </div>

    <div class="absolute inset-y-[50px] inset-x-[60px] flex items-center justify-center">
      <svg class="w-full h-full overflow-visible" viewBox="0 0 800 460" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
        <rect x="200" y="160" width="400" height="200" stroke="#1c2330" stroke-width="1.5" fill="none"/>
        <rect x="340" y="130" width="80" height="30" stroke="#1c2330" stroke-width="1.5" fill="none"/>
        <rect x="355" y="120" width="50" height="10" stroke="#1c2330" stroke-width="1" fill="none"/>
        <path d="M200 160 L160 180 L160 340 L200 360 Z" stroke="#1c2330" stroke-width="1.5" fill="none"/>
        <circle cx="450" cy="260" r="90" stroke="#1c2330" stroke-width="1.5" fill="none"/>
        <circle cx="450" cy="260" r="68" stroke="#1c2330" stroke-width="1" fill="none"/>
        <circle cx="450" cy="260" r="46" stroke="#1c2330" stroke-width="0.8" fill="none"/>
        <circle cx="450" cy="260" r="24" stroke="#1c2330" stroke-width="0.6" fill="none"/>
        <circle cx="260" cy="200" r="22" stroke="#1c2330" stroke-width="1" fill="none"/>
        <circle cx="260" cy="200" r="3" fill="#1c2330"/>
        <circle cx="540" cy="200" r="18" stroke="#1c2330" stroke-width="1" fill="none"/>
        <rect x="320" y="190" width="40" height="28" stroke="#1c2330" stroke-width="0.8" fill="none"/>
        <line x1="200" y1="380" x2="600" y2="380" stroke="#1c2330" stroke-width="0.5" stroke-dasharray="4,4"/>
        <text x="400" y="398" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#1c2330">142mm</text>
      </svg>

      <button type="button" aria-describedby="ttp01-note-1" aria-label="Callout 01, optical assembly" class="peer/h1 group absolute top-[56%] left-[56.25%] -m-5.5 w-11 h-11 grid place-items-center rounded-full bg-transparent border-0 p-0 cursor-help focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp01-red">
        <span class="relative block w-4 h-4"><span class="absolute inset-[5px] rounded-full bg-ttp01-red"></span><span class="absolute inset-0 rounded-full border border-ttp01-red animate-ttp01-pulse motion-reduce:animate-none"></span></span>
      </button>
      <div id="ttp01-note-1" role="tooltip" class="absolute top-[4%] right-0 w-[190px] z-10 invisible opacity-0 pointer-events-none bg-ttp01-paper border border-ttp01-ink px-3.5 py-3 font-ttp01-mono text-[11px] leading-[1.6] shadow-[4px_4px_0_rgba(28,35,48,0.08)] transition-[opacity,visibility] duration-300 peer-hover/h1:visible peer-hover/h1:opacity-100 peer-hover/h1:delay-120 peer-focus-visible/h1:visible peer-focus-visible/h1:opacity-100 max-[560px]:static max-[560px]:w-full">
        <div class="font-ttp01-serif italic font-medium text-xl leading-none text-ttp01-red mb-[3px]">01</div>
        <div class="text-[10px] tracking-[0.15em] uppercase text-ttp01-label mb-1.5">— Optical Assembly</div>
        <div class="font-ttp01-serif text-[15px] font-medium leading-tight mb-1.5">35mm <em class="italic text-ttp01-red">f/1.4</em> prime</div>
        <div class="font-ttp01-sans text-[11px] leading-[1.5] text-ttp01-body">Twelve-element design across nine groups. Aspherical front and rear, two ED elements mid-stack.</div>
        <dl class="mt-2 pt-1.5 border-t border-dashed border-ttp01-dash grid grid-cols-[54px_1fr] gap-x-2 gap-y-[3px] text-[10px]">
          <dt class="text-ttp01-key">Glass</dt><dd class="m-0 text-ttp01-red">12 / 9</dd>
          <dt class="text-ttp01-key">Coating</dt><dd class="m-0 text-ttp01-red">Nano-V</dd>
          <dt class="text-ttp01-key">Weight</dt><dd class="m-0 text-ttp01-red">410g</dd>
        </dl>
      </div>

      <button type="button" aria-describedby="ttp01-note-2" aria-label="Callout 02, shutter dial" class="peer/h2 absolute top-[25%] left-[32.5%] -m-5.5 w-11 h-11 grid place-items-center rounded-full bg-transparent border-0 p-0 cursor-help focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp01-red">
        <span class="relative block w-4 h-4"><span class="absolute inset-[5px] rounded-full bg-ttp01-red"></span><span class="absolute inset-0 rounded-full border border-ttp01-red animate-ttp01-pulse motion-reduce:animate-none"></span></span>
      </button>
      <div id="ttp01-note-2" role="tooltip" class="absolute top-[4%] left-0 w-[190px] z-10 invisible opacity-0 pointer-events-none bg-ttp01-paper border border-ttp01-ink px-3.5 py-3 font-ttp01-mono text-[11px] leading-[1.6] shadow-[4px_4px_0_rgba(28,35,48,0.08)] transition-[opacity,visibility] duration-300 peer-hover/h2:visible peer-hover/h2:opacity-100 peer-hover/h2:delay-120 peer-focus-visible/h2:visible peer-focus-visible/h2:opacity-100 max-[560px]:static max-[560px]:w-full">
        <div class="font-ttp01-serif italic font-medium text-xl leading-none text-ttp01-red mb-[3px]">02</div>
        <div class="text-[10px] tracking-[0.15em] uppercase text-ttp01-label mb-1.5">— Shutter Dial</div>
        <div class="font-ttp01-serif text-[15px] font-medium leading-tight mb-1.5">Mechanical <em class="italic text-ttp01-red">command</em> dial</div>
        <div class="font-ttp01-sans text-[11px] leading-[1.5] text-ttp01-body">Detented brass with knurled edge. Range 1/8000s to 30s plus bulb. Locks with a quarter-press.</div>
        <dl class="mt-2 pt-1.5 border-t border-dashed border-ttp01-dash grid grid-cols-[54px_1fr] gap-x-2 gap-y-[3px] text-[10px]">
          <dt class="text-ttp01-key">Steps</dt><dd class="m-0 text-ttp01-red">1/3 EV</dd>
          <dt class="text-ttp01-key">Travel</dt><dd class="m-0 text-ttp01-red">300°</dd>
          <dt class="text-ttp01-key">Cycles</dt><dd class="m-0 text-ttp01-red">500k</dd>
        </dl>
      </div>

      <button type="button" aria-describedby="ttp01-note-3" aria-label="Callout 03, accessory port" class="peer/h3 absolute top-[30%] left-[47.5%] -m-5.5 w-11 h-11 grid place-items-center rounded-full bg-transparent border-0 p-0 cursor-help focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp01-red">
        <span class="relative block w-4 h-4"><span class="absolute inset-[5px] rounded-full bg-ttp01-red"></span><span class="absolute inset-0 rounded-full border border-ttp01-red animate-ttp01-pulse motion-reduce:animate-none"></span></span>
      </button>
      <div id="ttp01-note-3" role="tooltip" class="absolute top-[4%] left-1/2 w-[190px] z-10 invisible opacity-0 pointer-events-none bg-ttp01-paper border border-ttp01-ink px-3.5 py-3 font-ttp01-mono text-[11px] leading-[1.6] shadow-[4px_4px_0_rgba(28,35,48,0.08)] transition-[opacity,visibility] duration-300 peer-hover/h3:visible peer-hover/h3:opacity-100 peer-hover/h3:delay-120 peer-focus-visible/h3:visible peer-focus-visible/h3:opacity-100 max-[560px]:static max-[560px]:w-full">
        <div class="font-ttp01-serif italic font-medium text-xl leading-none text-ttp01-red mb-[3px]">03</div>
        <div class="text-[10px] tracking-[0.15em] uppercase text-ttp01-label mb-1.5">— Accessory Port</div>
        <div class="font-ttp01-serif text-[15px] font-medium leading-tight mb-1.5">ISO 518 <em class="italic text-ttp01-red">hot shoe</em></div>
        <div class="font-ttp01-sans text-[11px] leading-[1.5] text-ttp01-body">Standard mount with X-sync at 1/250s. Center pin plus four data contacts for TTL flash control.</div>
        <dl class="mt-2 pt-1.5 border-t border-dashed border-ttp01-dash grid grid-cols-[54px_1fr] gap-x-2 gap-y-[3px] text-[10px]">
          <dt class="text-ttp01-key">Sync</dt><dd class="m-0 text-ttp01-red">1/250s</dd>
          <dt class="text-ttp01-key">Pins</dt><dd class="m-0 text-ttp01-red">1+4</dd>
          <dt class="text-ttp01-key">Hot</dt><dd class="m-0 text-ttp01-red">12V</dd>
        </dl>
      </div>

      <button type="button" aria-describedby="ttp01-note-4" aria-label="Callout 04, hand grip" class="peer/h4 absolute top-[56%] left-[22.5%] -m-5.5 w-11 h-11 grid place-items-center rounded-full bg-transparent border-0 p-0 cursor-help focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp01-red">
        <span class="relative block w-4 h-4"><span class="absolute inset-[5px] rounded-full bg-ttp01-red"></span><span class="absolute inset-0 rounded-full border border-ttp01-red animate-ttp01-pulse motion-reduce:animate-none"></span></span>
      </button>
      <div id="ttp01-note-4" role="tooltip" class="absolute bottom-[4%] left-0 w-[190px] z-10 invisible opacity-0 pointer-events-none bg-ttp01-paper border border-ttp01-ink px-3.5 py-3 font-ttp01-mono text-[11px] leading-[1.6] shadow-[4px_4px_0_rgba(28,35,48,0.08)] transition-[opacity,visibility] duration-300 peer-hover/h4:visible peer-hover/h4:opacity-100 peer-hover/h4:delay-120 peer-focus-visible/h4:visible peer-focus-visible/h4:opacity-100 max-[560px]:static max-[560px]:w-full">
        <div class="font-ttp01-serif italic font-medium text-xl leading-none text-ttp01-red mb-[3px]">04</div>
        <div class="text-[10px] tracking-[0.15em] uppercase text-ttp01-label mb-1.5">— Hand Grip</div>
        <div class="font-ttp01-serif text-[15px] font-medium leading-tight mb-1.5">Magnesium <em class="italic text-ttp01-red">undergrip</em></div>
        <div class="font-ttp01-sans text-[11px] leading-[1.5] text-ttp01-body">Cast magnesium core wrapped in pressed cowhide. Conceals battery, card slot and focus-recall trigger.</div>
        <dl class="mt-2 pt-1.5 border-t border-dashed border-ttp01-dash grid grid-cols-[54px_1fr] gap-x-2 gap-y-[3px] text-[10px]">
          <dt class="text-ttp01-key">Wrap</dt><dd class="m-0 text-ttp01-red">Cowhide</dd>
          <dt class="text-ttp01-key">Core</dt><dd class="m-0 text-ttp01-red">MgAl</dd>
          <dt class="text-ttp01-key">Battery</dt><dd class="m-0 text-ttp01-red">7.4 Wh</dd>
        </dl>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp01-stage: #f4f3ee;
  --color-ttp01-stage: oklch(0.96 0.005 95);
  --color-ttp01-paper: #fbfaf6;
  --color-ttp01-paper: oklch(0.98 0.006 95);
  --color-ttp01-ink: #1c2330;
  --color-ttp01-ink: oklch(0.26 0.03 265);
  --color-ttp01-body: #4a505c;
  --color-ttp01-body: oklch(0.44 0.02 265);
  --color-ttp01-label: #585e6b;
  --color-ttp01-label: oklch(0.48 0.02 265);
  --color-ttp01-meta: #5b616e;
  --color-ttp01-meta: oklch(0.49 0.02 265);
  --color-ttp01-key: #5f6472;
  --color-ttp01-key: oklch(0.51 0.02 265);
  --color-ttp01-edge: #c7cad1;
  --color-ttp01-edge: oklch(0.83 0.008 265);
  --color-ttp01-tick: #9aa0ab;
  --color-ttp01-tick: oklch(0.69 0.012 265);
  --color-ttp01-dash: #b0b5be;
  --color-ttp01-dash: oklch(0.76 0.01 265);
  --color-ttp01-grid: rgba(28, 35, 48, 0.06);
  --color-ttp01-grid2: rgba(28, 35, 48, 0.05);
  --color-ttp01-red: #c1422c;
  --color-ttp01-red: oklch(0.52 0.16 32);
  --font-ttp01-sans: 'Inter', system-ui, sans-serif;
  --font-ttp01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttp01-serif: Georgia, 'Times New Roman', serif;
  --animate-ttp01-pulse: ttp01-pulse 2.4s ease-out infinite;
}

@keyframes ttp01-pulse {
  0% {
    transform: scale(0.6);
    opacity: 0.8;
  }

  100% {
    transform: scale(2);
    opacity: 0;
  }
}

.ttp-01 {
  width: 100%;
  min-height: 100svh;
}
/* Under 560px the percentage-pinned notes are stacked by max-[560px]:static;
   the flow container needs to allow that, and the ticks go. */

@media (max-width: 560px) {
  .ttp-01 [role="tooltip"] {
    margin-top: 8px;
  }
}
```
