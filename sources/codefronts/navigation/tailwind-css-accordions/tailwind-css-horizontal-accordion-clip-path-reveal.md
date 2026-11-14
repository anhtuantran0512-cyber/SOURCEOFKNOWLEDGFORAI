---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-horizontal-accordion-clip-path-reveal/"
title: "Tailwind CSS Horizontal Accordion with clip-path Reveal"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "An architecture studio's selected-works switcher where every project panel is always full size, stacked in one grid cell, and the chosen one is uncovered by…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Horizontal Accordion with clip-path Reveal
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-horizontal-accordion-clip-path-reveal/

An architecture studio's selected-works switcher where every project panel is always full size, stacked in one grid cell, and the chosen one is uncovered by a [clip-path:inset(0)] curtain wipe instead of a resize. Radios live inside the rail's labels; the shell reads them with group-has-[#tac29-a:checked]/shell:, so the rail and the stage need no shared parent selector and no JavaScript. Content never reflows mid-animation — it is revealed, not stretched.
## HTML
```html
<section class="tac-29 w-full min-h-svh grid place-items-center bg-tac29-bg bg-[radial-gradient(90%_60%_at_50%_0%,var(--color-tac29-glow),transparent_70%)] px-5 py-14 font-tac29-sans text-tac29-ink" aria-label="clip-path curtain reveal horizontal accordion demo">
  <div class="grid w-full max-w-5xl justify-items-center gap-8">
    <header class="flex w-full flex-wrap items-end justify-between gap-x-8 gap-y-3">
      <div>
        <p class="flex items-center gap-2.5 font-tac29-mono text-[11.5px] font-medium tracking-[0.16em] uppercase text-tac29-mut"><span aria-hidden="true" class="h-px w-8 bg-tac29-acc"></span>Atelier Nord · Selected works</p>
        <h2 class="mt-3 font-tac29-serif text-[clamp(36px,5vw,54px)] leading-[0.95] tracking-[-0.015em]">Buildings that <em class="text-tac29-acc-ink">hold still.</em></h2>
      </div>
      <p class="max-w-xs text-[14.5px] leading-[1.6] text-tac29-mut text-pretty">Four recent commissions in brick, timber, concrete and steel — each one designed around a single, patient material.</p>
    </header>

    <div class="group/shell grid w-full overflow-hidden rounded-[22px] bg-tac29-card shadow-[0_1px_2px_oklch(0.3_0.02_60/0.06),0_30px_70px_-30px_oklch(0.3_0.04_50/0.35)] ring-1 ring-tac29-ink/8 md:grid-cols-[15rem_minmax(0,1fr)]" role="group" aria-label="Selected works">
      <div class="flex flex-col gap-1 border-tac29-line bg-tac29-rail p-3 md:border-r md:p-4 max-md:grid max-md:grid-cols-2 max-md:border-b" role="radiogroup" aria-label="Choose a project">
        <p aria-hidden="true" class="mb-2 px-3 pt-1 font-tac29-mono text-[10.5px] tracking-[0.18em] uppercase text-tac29-mut max-md:hidden">Index — 04</p>
        <label class="group/tab relative flex min-h-14 cursor-pointer items-center gap-3 rounded-xl py-2 pr-3 pl-5 transition-colors duration-200 select-none before:absolute before:top-1/2 before:left-2 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tac29-acc before:transition-[height] before:duration-300 hover:bg-tac29-wash has-checked:bg-tac29-wash has-checked:before:h-7 has-focus-visible:ring-2 has-focus-visible:ring-tac29-acc has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac29-rail motion-reduce:transition-none motion-reduce:before:transition-none">
          <input type="radio" name="tac29-work" id="tac29-a" class="sr-only" checked>
          <span class="font-tac29-mono text-[11px] text-tac29-mut group-has-checked/tab:text-tac29-acc-ink">01</span>
          <span class="grid min-w-0"><span class="truncate text-[15px] font-semibold tracking-[-0.01em]">Kiln Pavilion</span><span class="text-[12.5px] text-tac29-mut max-md:hidden">Aarhus · 2024</span></span>
        </label>
        <label class="group/tab relative flex min-h-14 cursor-pointer items-center gap-3 rounded-xl py-2 pr-3 pl-5 transition-colors duration-200 select-none before:absolute before:top-1/2 before:left-2 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tac29-acc before:transition-[height] before:duration-300 hover:bg-tac29-wash has-checked:bg-tac29-wash has-checked:before:h-7 has-focus-visible:ring-2 has-focus-visible:ring-tac29-acc has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac29-rail motion-reduce:transition-none motion-reduce:before:transition-none">
          <input type="radio" name="tac29-work" id="tac29-b" class="sr-only">
          <span class="font-tac29-mono text-[11px] text-tac29-mut group-has-checked/tab:text-tac29-acc-ink">02</span>
          <span class="grid min-w-0"><span class="truncate text-[15px] font-semibold tracking-[-0.01em]">Fjord House</span><span class="text-[12.5px] text-tac29-mut max-md:hidden">Hardanger · 2023</span></span>
        </label>
        <label class="group/tab relative flex min-h-14 cursor-pointer items-center gap-3 rounded-xl py-2 pr-3 pl-5 transition-colors duration-200 select-none before:absolute before:top-1/2 before:left-2 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tac29-acc before:transition-[height] before:duration-300 hover:bg-tac29-wash has-checked:bg-tac29-wash has-checked:before:h-7 has-focus-visible:ring-2 has-focus-visible:ring-tac29-acc has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac29-rail motion-reduce:transition-none motion-reduce:before:transition-none">
          <input type="radio" name="tac29-work" id="tac29-c" class="sr-only">
          <span class="font-tac29-mono text-[11px] text-tac29-mut group-has-checked/tab:text-tac29-acc-ink">03</span>
          <span class="grid min-w-0"><span class="truncate text-[15px] font-semibold tracking-[-0.01em]">Atrium Library</span><span class="text-[12.5px] text-tac29-mut max-md:hidden">Ghent · 2022</span></span>
        </label>
        <label class="group/tab relative flex min-h-14 cursor-pointer items-center gap-3 rounded-xl py-2 pr-3 pl-5 transition-colors duration-200 select-none before:absolute before:top-1/2 before:left-2 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tac29-acc before:transition-[height] before:duration-300 hover:bg-tac29-wash has-checked:bg-tac29-wash has-checked:before:h-7 has-focus-visible:ring-2 has-focus-visible:ring-tac29-acc has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac29-rail motion-reduce:transition-none motion-reduce:before:transition-none">
          <input type="radio" name="tac29-work" id="tac29-d" class="sr-only">
          <span class="font-tac29-mono text-[11px] text-tac29-mut group-has-checked/tab:text-tac29-acc-ink">04</span>
          <span class="grid min-w-0"><span class="truncate text-[15px] font-semibold tracking-[-0.01em]">Marsh Bridge</span><span class="text-[12.5px] text-tac29-mut max-md:hidden">Essex · 2021</span></span>
        </label>
        <p aria-hidden="true" class="mt-auto px-3 pt-6 text-[12.5px] leading-[1.5] text-tac29-mut max-md:hidden">Drawings shown as south elevations, not to scale.</p>
      </div>

      <div class="grid">
        <article class="invisible z-0 grid gap-6 p-4 [grid-area:1/1] [clip-path:inset(0_100%_0_0)] [transition:clip-path_.8s_cubic-bezier(.65,0,.2,1),visibility_0s_.8s] sm:p-6 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)] lg:gap-8 lg:p-7 group-has-[#tac29-a:checked]/shell:visible group-has-[#tac29-a:checked]/shell:z-10 group-has-[#tac29-a:checked]/shell:[clip-path:inset(0)] group-has-[#tac29-a:checked]/shell:[transition:clip-path_.8s_cubic-bezier(.65,0,.2,1),visibility_0s] motion-reduce:[transition:none]!" aria-label="Kiln Pavilion">
          <figure class="relative aspect-[4/3] overflow-hidden rounded-2xl bg-linear-to-b from-[#f2c39b] to-[#f8e9d9]">
            <svg class="absolute inset-0 size-full scale-[1.08] transition-transform duration-[1400ms] ease-[cubic-bezier(.2,.7,.2,1)] group-has-[#tac29-a:checked]/shell:scale-100 motion-reduce:transition-none" viewBox="0 0 400 300" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
              <circle cx="304" cy="86" r="34" fill="#fff6ea" opacity="0.85"/>
              <path d="M0 214 Q70 186 150 204 T300 196 T400 206 V300 H0Z" fill="#dfae86" opacity="0.6"/>
              <rect x="0" y="232" width="400" height="68" fill="#d8bf9f"/>
              <rect x="74" y="120" width="246" height="112" fill="#b85f3a"/>
              <path d="M74 138H320M74 156H320M74 174H320M74 192H320M74 210H320" stroke="#9e4d2c" stroke-width="1.2" opacity="0.55"/>
              <rect x="58" y="108" width="278" height="13" fill="#7f3c22"/>
              <path d="M98 232V178a16 16 0 0 1 32 0V232Z" fill="#3b1d12"/>
              <path d="M152 232V178a16 16 0 0 1 32 0V232Z" fill="#3b1d12"/>
              <path d="M206 232V178a16 16 0 0 1 32 0V232Z" fill="#3b1d12"/>
              <path d="M260 232V178a16 16 0 0 1 32 0V232Z" fill="#3b1d12"/>
              <path d="M156 232V182a12 12 0 0 1 24 0V232Z" fill="#f2b56e" opacity="0.6"/>
              <path d="M210 232V182a12 12 0 0 1 24 0V232Z" fill="#f2b56e" opacity="0.45"/>
              <rect x="44" y="246" width="306" height="9" rx="4.5" fill="#f6dfc6" opacity="0.8"/>
              <rect x="349" y="196" width="5" height="38" fill="#4c3a2a"/>
              <circle cx="351" cy="188" r="24" fill="#6e7c4e"/>
              <circle cx="338" cy="198" r="15" fill="#7e8c5c"/>
              <rect x="138" y="216" width="4" height="16" rx="2" fill="#2a1a12"/>
              <circle cx="140" cy="212" r="3" fill="#2a1a12"/>
            </svg>
            <figcaption class="absolute bottom-3 left-3 rounded-full bg-white/85 px-3 py-1.5 font-tac29-mono text-[11px] text-tac29-ink shadow-sm ring-1 ring-black/5 backdrop-blur">Fig. 01 — South elevation, dusk</figcaption>
          </figure>
          <div class="flex flex-col justify-center">
            <p class="font-tac29-mono text-[11.5px] tracking-[0.14em] uppercase text-tac29-acc-ink">Cultural · 1,240 m²</p>
            <h3 class="mt-2 font-tac29-serif text-[clamp(34px,4vw,46px)] leading-none tracking-[-0.01em]">Kiln Pavilion</h3>
            <p class="mt-4 max-w-[46ch] text-[15px] leading-[1.65] text-tac29-quiet text-pretty">A ceramics hall built from 180,000 hand-pressed bricks fired on site. Four deep arches hold the kilns; the roof slab floats on a hidden steel ring so the walls carry nothing but light.</p>
            <dl class="mt-6 grid grid-cols-3 gap-4 border-t border-tac29-line pt-4">
              <div><dt class="text-[12px] text-tac29-mut">Material</dt><dd class="mt-1 text-[15px] font-semibold">Clay brick</dd></div>
              <div><dt class="text-[12px] text-tac29-mut">Completed</dt><dd class="mt-1 text-[15px] font-semibold">May 2024</dd></div>
              <div><dt class="text-[12px] text-tac29-mut">Team</dt><dd class="mt-1 text-[15px] font-semibold">7 people</dd></div>
            </dl>
          </div>
        </article>

        <article class="invisible z-0 grid gap-6 p-4 [grid-area:1/1] [clip-path:inset(0_100%_0_0)] [transition:clip-path_.8s_cubic-bezier(.65,0,.2,1),visibility_0s_.8s] sm:p-6 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)] lg:gap-8 lg:p-7 group-has-[#tac29-b:checked]/shell:visible group-has-[#tac29-b:checked]/shell:z-10 group-has-[#tac29-b:checked]/shell:[clip-path:inset(0)] group-has-[#tac29-b:checked]/shell:[transition:clip-path_.8s_cubic-bezier(.65,0,.2,1),visibility_0s] motion-reduce:[transition:none]!" aria-label="Fjord House">
          <figure class="relative aspect-[4/3] overflow-hidden rounded-2xl bg-linear-to-b from-[#c4d6e4] to-[#eef2f4]">
            <svg class="absolute inset-0 size-full scale-[1.08] transition-transform duration-[1400ms] ease-[cubic-bezier(.2,.7,.2,1)] group-has-[#tac29-b:checked]/shell:scale-100 motion-reduce:transition-none" viewBox="0 0 400 300" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
              <path d="M0 196 L68 118 L120 160 L196 78 L268 148 L326 112 L400 172 V300 H0Z" fill="#8fa3b3"/>
              <path d="M196 78 L216 98 L204 96 L194 106 L184 94 L176 98Z" fill="#f4f7f9"/>
              <path d="M68 118 L82 134 L72 132 L62 140 L58 130Z" fill="#f4f7f9"/>
              <path d="M0 214 L60 176 L118 200 L176 168 L240 198 L300 180 L400 210 V300 H0Z" fill="#6f8798"/>
              <rect x="0" y="226" width="400" height="74" fill="#557589"/>
              <path d="M210 244H300M240 256H370M190 270H260M300 282H380" stroke="#a9c1d1" stroke-width="2" stroke-linecap="round" opacity="0.55"/>
              <path d="M0 300 L0 176 Q50 166 104 178 L170 204 L198 232 L210 300Z" fill="#33403a"/>
              <rect x="64" y="142" width="2" height="40" fill="#2b2420"/>
              <rect x="150" y="142" width="2" height="54" fill="#2b2420"/>
              <rect x="40" y="128" width="144" height="7" fill="#2b2420"/>
              <rect x="44" y="135" width="136" height="40" fill="#6a4a33"/>
              <rect x="56" y="143" width="112" height="22" fill="#f4d8a3"/>
              <path d="M84 143V165M112 143V165M140 143V165" stroke="#6a4a33" stroke-width="2"/>
              <path d="M278 252 L314 252 L308 260 L284 260Z" fill="#ece6dc"/>
              <path d="M296 234 V252 M296 236 L310 248 H296" stroke="#ece6dc" stroke-width="2" fill="none"/>
            </svg>
            <figcaption class="absolute bottom-3 left-3 rounded-full bg-white/85 px-3 py-1.5 font-tac29-mono text-[11px] text-tac29-ink shadow-sm ring-1 ring-black/5 backdrop-blur">Fig. 02 — West elevation, morning</figcaption>
          </figure>
          <div class="flex flex-col justify-center">
            <p class="font-tac29-mono text-[11.5px] tracking-[0.14em] uppercase text-tac29-acc-ink">Residential · 186 m²</p>
            <h3 class="mt-2 font-tac29-serif text-[clamp(34px,4vw,46px)] leading-none tracking-[-0.01em]">Fjord House</h3>
            <p class="mt-4 max-w-[46ch] text-[15px] leading-[1.65] text-tac29-quiet text-pretty">A larch box cantilevered eleven metres off a granite shelf. One continuous window frames the water; everything else — kitchen, stair, bath — hides in a thickened rear wall.</p>
            <dl class="mt-6 grid grid-cols-3 gap-4 border-t border-tac29-line pt-4">
              <div><dt class="text-[12px] text-tac29-mut">Material</dt><dd class="mt-1 text-[15px] font-semibold">Larch, CLT</dd></div>
              <div><dt class="text-[12px] text-tac29-mut">Completed</dt><dd class="mt-1 text-[15px] font-semibold">Sep 2023</dd></div>
              <div><dt class="text-[12px] text-tac29-mut">Cantilever</dt><dd class="mt-1 text-[15px] font-semibold">11 m</dd></div>
            </dl>
          </div>
        </article>

        <article class="invisible z-0 grid gap-6 p-4 [grid-area:1/1] [clip-path:inset(0_100%_0_0)] [transition:clip-path_.8s_cubic-bezier(.65,0,.2,1),visibility_0s_.8s] sm:p-6 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)] lg:gap-8 lg:p-7 group-has-[#tac29-c:checked]/shell:visible group-has-[#tac29-c:checked]/shell:z-10 group-has-[#tac29-c:checked]/shell:[clip-path:inset(0)] group-has-[#tac29-c:checked]/shell:[transition:clip-path_.8s_cubic-bezier(.65,0,.2,1),visibility_0s] motion-reduce:[transition:none]!" aria-label="Atrium Library">
          <figure class="relative aspect-[4/3] overflow-hidden rounded-2xl bg-linear-to-b from-[#d9dcda] to-[#f3f2ee]">
            <svg class="absolute inset-0 size-full scale-[1.08] transition-transform duration-[1400ms] ease-[cubic-bezier(.2,.7,.2,1)] group-has-[#tac29-c:checked]/shell:scale-100 motion-reduce:transition-none" viewBox="0 0 400 300" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
              <rect x="0" y="236" width="400" height="64" fill="#d3cec4"/>
              <rect x="40" y="150" width="96" height="86" fill="#c2bdb4"/>
              <rect x="120" y="104" width="176" height="132" fill="#b5afa5"/>
              <rect x="280" y="132" width="86" height="104" fill="#c8c3ba"/>
              <rect x="136" y="122" width="144" height="34" fill="#93adb9"/>
              <path d="M160 122V156M184 122V156M208 122V156M232 122V156M256 122V156" stroke="#b5afa5" stroke-width="3"/>
              <rect x="136" y="172" width="144" height="64" fill="#2f3a3e"/>
              <rect x="146" y="182" width="124" height="54" fill="#f1d9a2" opacity="0.75"/>
              <path d="M146 196H270M146 212H270M146 226H270" stroke="#a58a5c" stroke-width="2" opacity="0.6"/>
              <path d="M52 166H124M52 184H124M52 202H124M292 150H354M292 170H354M292 190H354" stroke="#aba59b" stroke-width="2"/>
              <rect x="112" y="98" width="192" height="8" fill="#8f897f"/>
              <circle cx="24" cy="214" r="22" fill="#7b8d68"/>
              <circle cx="384" cy="210" r="24" fill="#7b8d68"/>
              <rect x="22" y="222" width="4" height="16" fill="#4a3d2f"/>
              <rect x="382" y="222" width="4" height="16" fill="#4a3d2f"/>
              <path d="M120 250H296" stroke="#bdb6aa" stroke-width="4" stroke-linecap="round"/>
              <rect x="200" y="221" width="4" height="15" rx="2" fill="#1f2326"/>
              <circle cx="202" cy="217" r="3" fill="#1f2326"/>
            </svg>
            <figcaption class="absolute bottom-3 left-3 rounded-full bg-white/85 px-3 py-1.5 font-tac29-mono text-[11px] text-tac29-ink shadow-sm ring-1 ring-black/5 backdrop-blur">Fig. 03 — Street elevation, overcast</figcaption>
          </figure>
          <div class="flex flex-col justify-center">
            <p class="font-tac29-mono text-[11.5px] tracking-[0.14em] uppercase text-tac29-acc-ink">Civic · 4,900 m²</p>
            <h3 class="mt-2 font-tac29-serif text-[clamp(34px,4vw,46px)] leading-none tracking-[-0.01em]">Atrium Library</h3>
            <p class="mt-4 max-w-[46ch] text-[15px] leading-[1.65] text-tac29-quiet text-pretty">Three board-marked concrete volumes stepped around a five-storey reading atrium. A clerestory of 214 fixed fins keeps the stacks in north light from opening to close.</p>
            <dl class="mt-6 grid grid-cols-3 gap-4 border-t border-tac29-line pt-4">
              <div><dt class="text-[12px] text-tac29-mut">Material</dt><dd class="mt-1 text-[15px] font-semibold">Concrete</dd></div>
              <div><dt class="text-[12px] text-tac29-mut">Completed</dt><dd class="mt-1 text-[15px] font-semibold">Mar 2022</dd></div>
              <div><dt class="text-[12px] text-tac29-mut">Seats</dt><dd class="mt-1 text-[15px] font-semibold">620</dd></div>
            </dl>
          </div>
        </article>

        <article class="invisible z-0 grid gap-6 p-4 [grid-area:1/1] [clip-path:inset(0_100%_0_0)] [transition:clip-path_.8s_cubic-bezier(.65,0,.2,1),visibility_0s_.8s] sm:p-6 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)] lg:gap-8 lg:p-7 group-has-[#tac29-d:checked]/shell:visible group-has-[#tac29-d:checked]/shell:z-10 group-has-[#tac29-d:checked]/shell:[clip-path:inset(0)] group-has-[#tac29-d:checked]/shell:[transition:clip-path_.8s_cubic-bezier(.65,0,.2,1),visibility_0s] motion-reduce:[transition:none]!" aria-label="Marsh Bridge">
          <figure class="relative aspect-[4/3] overflow-hidden rounded-2xl bg-linear-to-b from-[#e4bcc4] to-[#f5e4d8]">
            <svg class="absolute inset-0 size-full scale-[1.08] transition-transform duration-[1400ms] ease-[cubic-bezier(.2,.7,.2,1)] group-has-[#tac29-d:checked]/shell:scale-100 motion-reduce:transition-none" viewBox="0 0 400 300" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
              <circle cx="92" cy="80" r="22" fill="#fff4ee" opacity="0.9"/>
              <path d="M0 196 Q100 182 200 192 T400 188 V300 H0Z" fill="#b59cae" opacity="0.7"/>
              <rect x="0" y="208" width="400" height="92" fill="#8e7f9e"/>
              <path d="M30 236H120M180 248H300M60 268H200M260 280H380" stroke="#c8b7cf" stroke-width="2" stroke-linecap="round" opacity="0.6"/>
              <path d="M16 206 Q200 96 384 206" fill="none" stroke="#2c2434" stroke-width="6" stroke-linecap="round"/>
              <path d="M8 206H392" stroke="#2c2434" stroke-width="7"/>
              <path d="M60 206V183M100 206V168M140 206V157M180 206V152M220 206V152M260 206V157M300 206V168M340 206V183" stroke="#2c2434" stroke-width="1.6"/>
              <path d="M10 236 Q200 290 390 236" fill="none" stroke="#2c2434" stroke-width="3" opacity="0.25"/>
              <path d="M12 300V250M18 300V258M24 300V246M370 300V252M378 300V244M386 300V256M392 300V248" stroke="#4d4258" stroke-width="2" stroke-linecap="round"/>
              <rect x="246" y="190" width="4" height="15" rx="2" fill="#2c2434"/>
              <circle cx="248" cy="186" r="3" fill="#2c2434"/>
            </svg>
            <figcaption class="absolute bottom-3 left-3 rounded-full bg-white/85 px-3 py-1.5 font-tac29-mono text-[11px] text-tac29-ink shadow-sm ring-1 ring-black/5 backdrop-blur">Fig. 04 — Long section, low tide</figcaption>
          </figure>
          <div class="flex flex-col justify-center">
            <p class="font-tac29-mono text-[11.5px] tracking-[0.14em] uppercase text-tac29-acc-ink">Infrastructure · 92 m span</p>
            <h3 class="mt-2 font-tac29-serif text-[clamp(34px,4vw,46px)] leading-none tracking-[-0.01em]">Marsh Bridge</h3>
            <p class="mt-4 max-w-[46ch] text-[15px] leading-[1.65] text-tac29-quiet text-pretty">A weathering-steel arch that lands only twice, so the marsh keeps its tidal channels. The deck is 1.8 m wide on purpose: walkers slow down, cyclists dismount, everyone looks at the water.</p>
            <dl class="mt-6 grid grid-cols-3 gap-4 border-t border-tac29-line pt-4">
              <div><dt class="text-[12px] text-tac29-mut">Material</dt><dd class="mt-1 text-[15px] font-semibold">Corten steel</dd></div>
              <div><dt class="text-[12px] text-tac29-mut">Completed</dt><dd class="mt-1 text-[15px] font-semibold">Oct 2021</dd></div>
              <div><dt class="text-[12px] text-tac29-mut">Footings</dt><dd class="mt-1 text-[15px] font-semibold">2</dd></div>
            </dl>
          </div>
        </article>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tac29-ink/10 bg-white/70 px-3.5 py-2 font-tac29-mono text-[11.5px] text-tac29-mut">[grid-area:1/1] · [clip-path:inset(0)] · group-has-[#id:checked]/shell:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac29-bg: #ebe7e0;
  --color-tac29-bg: oklch(0.93 0.009 80);
  --color-tac29-glow: #f7f5f1;
  --color-tac29-glow: oklch(0.975 0.005 80);
  --color-tac29-card: #fdfcfa;
  --color-tac29-card: oklch(0.993 0.003 80);
  --color-tac29-rail: #f8f6f2;
  --color-tac29-rail: oklch(0.975 0.005 80);
  --color-tac29-wash: #f0ebe4;
  --color-tac29-wash: oklch(0.945 0.011 70);
  --color-tac29-line: #e5e0d8;
  --color-tac29-line: oklch(0.91 0.01 80);
  --color-tac29-ink: #1f1c19;
  --color-tac29-ink: oklch(0.22 0.008 70);
  --color-tac29-quiet: #48423c;
  --color-tac29-quiet: oklch(0.39 0.012 70);
  --color-tac29-mut: #686159;
  --color-tac29-mut: oklch(0.5 0.013 70);
  --color-tac29-acc: #bb5a30;
  --color-tac29-acc: oklch(0.58 0.14 45);
  --color-tac29-acc-ink: #9a4321;
  --color-tac29-acc-ink: oklch(0.49 0.13 42);
  --font-tac29-serif: 'Instrument Serif', 'Iowan Old Style', Georgia, serif;
  --font-tac29-sans: 'Geist', system-ui, sans-serif;
  --font-tac29-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-29 {
  width: 100%;
  min-height: 100svh;
}
```
