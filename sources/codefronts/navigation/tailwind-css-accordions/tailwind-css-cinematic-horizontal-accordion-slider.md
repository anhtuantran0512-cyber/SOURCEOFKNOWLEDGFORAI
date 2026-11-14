---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-cinematic-horizontal-accordion-slider/"
title: "Tailwind CSS Cinematic Horizontal Accordion Slider"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A film-festival lineup on a strip of 35mm: perforated rails run along the edges, collapsed frames show a Roman numeral and the title running down the spine,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Cinematic Horizontal Accordion Slider
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-cinematic-horizontal-accordion-slider/

A film-festival lineup on a strip of 35mm: perforated rails run along the edges, collapsed frames show a Roman numeral and the title running down the spine, and the chosen film grows (lg:has-checked:grow-[7]) into a letterboxed still. The black bars drop in with scale-y-0 → scale-y-100, the still settles from scale-110, and the title tracks in like opening credits with tracking-[0.5em] → group-has-checked:tracking-[0.04em]. Below lg the strip turns vertical, rails and all.
## HTML
```html
<section class="tac-31 w-full min-h-svh grid place-items-center bg-tac31-bg bg-[radial-gradient(70%_45%_at_50%_100%,var(--color-tac31-glow),transparent_75%)] px-5 py-14 font-tac31-sans text-tac31-ivory" aria-label="Cinematic horizontal accordion slider demo">
  <div class="grid w-full max-w-5xl justify-items-center gap-8">
    <header class="flex w-full flex-wrap items-end justify-between gap-x-8 gap-y-3">
      <div>
        <p class="flex items-center gap-2.5 font-tac31-mono text-[11.5px] tracking-[0.2em] uppercase text-tac31-gold"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac31-gold"></span>Nordlicht Film Festival · Competition</p>
        <h2 class="mt-3 font-tac31-display text-[clamp(30px,4.6vw,48px)] leading-[0.98] font-extrabold tracking-[-0.02em] uppercase">Four films.<span class="font-tac31-serif font-normal tracking-normal normal-case italic text-tac31-ivory/80"> One night each.</span></h2>
      </div>
      <p class="max-w-[17rem] font-tac31-mono text-[12px] leading-[1.7] text-tac31-mut">Screenings 12–15 Feb · Verdensteatret, Tromsø · Original language, English subtitles</p>
    </header>
    <div class="relative flex w-full flex-col gap-2 rounded-xl bg-tac31-film px-7 py-3 shadow-[0_40px_80px_-30px_rgb(0_0_0/.9)] ring-1 ring-white/6 lg:h-[29rem] lg:flex-row lg:px-3 lg:py-7" role="radiogroup" aria-label="Festival lineup">
      <span aria-hidden="true" class="absolute top-4 bottom-4 left-1.5 w-3 [background:radial-gradient(closest-side,var(--color-tac31-hole)_62%,transparent_72%)_0_0/100%_22px_repeat-y] lg:top-1.5 lg:right-4 lg:bottom-auto lg:left-4 lg:h-3 lg:w-auto lg:[background-size:22px_100%] lg:[background-repeat:repeat-x]"></span>
      <span aria-hidden="true" class="absolute top-4 right-1.5 bottom-4 w-3 [background:radial-gradient(closest-side,var(--color-tac31-hole)_62%,transparent_72%)_0_0/100%_22px_repeat-y] lg:top-auto lg:right-4 lg:bottom-1.5 lg:left-4 lg:h-3 lg:w-auto lg:[background-size:22px_100%] lg:[background-repeat:repeat-x]"></span>
      <div class="group relative h-[4.5rem] shrink-0 overflow-hidden rounded-[5px] transition-[height,flex-grow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] has-checked:h-[30rem] has-focus-visible:ring-2 has-focus-visible:ring-tac31-ivory has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac31-film sm:has-checked:h-[25rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[7] motion-reduce:transition-none" style="--tac31-t:#3d6a9e">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-4 px-5 text-tac31-ivory/90 ring-1 ring-white/7 ring-inset transition-[opacity,box-shadow] duration-300 [background:radial-gradient(90%_60%_at_50%_40%,color-mix(in_oklab,var(--tac31-t)_28%,transparent),transparent_75%),var(--color-tac31-frame)] hover:ring-white/20 group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-6 motion-reduce:transition-none">
          <input type="radio" name="tac31-lineup" id="tac31-a" class="sr-only" checked>
          <span class="w-9 font-tac31-serif text-[26px] leading-none text-tac31-ivory/70 italic lg:w-auto">I</span>
          <span class="min-w-0 flex-1 truncate font-tac31-display text-[13px] font-bold tracking-[0.28em] uppercase lg:flex-none lg:[writing-mode:vertical-rl]">Still Water</span>
          <span class="font-tac31-mono text-[11px] text-tac31-mut">96′</span>
        </label>
        <div class="invisible absolute inset-0 z-10 overflow-hidden bg-linear-to-b from-[#2b3d58] via-[#7a6a72] to-[#d9a77a] opacity-0 transition-[opacity,visibility] duration-200 group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-150 group-has-checked:duration-500 lg:right-auto lg:w-[max(100%,40rem)] motion-reduce:transition-none">
          <svg class="absolute inset-0 size-full scale-110 transition-transform duration-[2400ms] ease-out group-has-checked:scale-100 motion-reduce:transition-none" viewBox="0 0 640 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <circle cx="300" cy="104" r="26" fill="#f6dfb4" opacity="0.9"/>
              <path d="M0 210 L90 150 L170 190 L260 120 L350 186 L440 140 L540 196 L640 160 V260 H0Z" fill="#33405a"/>
              <path d="M0 236 L120 190 L220 222 L330 180 L460 228 L560 196 L640 220 V260 H0Z" fill="#1d2738"/>
              <rect x="0" y="246" width="640" height="114" fill="#141d2b"/>
              <path d="M270 262H330M240 276H360M280 290H320M210 306H390M260 322H340" stroke="#f0cf96" stroke-width="2.4" stroke-linecap="round" opacity="0.45"/>
              <path d="M380 252 L560 252 L544 270 L396 270Z" fill="#0b0f17"/>
              <rect x="416" y="230" width="112" height="22" fill="#0b0f17"/>
              <rect x="444" y="214" width="56" height="16" fill="#0b0f17"/>
              <rect x="482" y="198" width="7" height="16" fill="#0b0f17"/>
              <path d="M426 240H436M444 240H454M462 240H472M480 240H490M498 240H508M454 222H462M474 222H482" stroke="#f4d38a" stroke-width="5"/>
              <path d="M410 284H540M430 296H520" stroke="#f4d38a" stroke-width="2" opacity="0.3" stroke-linecap="round"/>
          </svg>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-t from-black/85 via-black/25 via-45% to-transparent"></span>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-r from-black/55 via-black/10 via-55% to-transparent"></span>
          <span aria-hidden="true" class="absolute inset-x-0 top-0 h-[10%] origin-top scale-y-0 bg-black transition-transform duration-700 ease-[cubic-bezier(.65,0,.2,1)] group-has-checked:scale-y-100 group-has-checked:delay-200 motion-reduce:scale-y-100 motion-reduce:transition-none"></span>
          <span aria-hidden="true" class="absolute inset-x-0 bottom-0 h-[10%] origin-bottom scale-y-0 bg-black transition-transform duration-700 ease-[cubic-bezier(.65,0,.2,1)] group-has-checked:scale-y-100 group-has-checked:delay-200 motion-reduce:scale-y-100 motion-reduce:transition-none"></span>
          <div class="absolute inset-x-5 top-[calc(10%+14px)] flex items-start justify-between gap-3 sm:inset-x-7">
            <p class="rounded-full bg-black/45 px-3 py-1.5 font-tac31-mono text-[10.5px] tracking-[0.16em] text-tac31-ivory/90 uppercase ring-1 ring-white/15 backdrop-blur-sm">Competition · I</p>
            <p class="flex items-center gap-1.5 rounded-full bg-tac31-ivory px-2.5 py-1 text-[12.5px] font-bold text-tac31-ink"><svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M8 1.5l1.9 4.1 4.5.5-3.4 3 1 4.4L8 11.3l-4 2.2 1-4.4-3.4-3 4.5-.5z" fill="currentColor"/></svg><span><span class="sr-only">Critics rating </span>8.4</span></p>
          </div>
          <div class="absolute inset-x-5 bottom-[calc(10%+18px)] sm:inset-x-7">
            <p class="font-tac31-mono text-[11px] tracking-[0.18em] text-tac31-mut uppercase">dir. E. Almqvist · 96 min · Sweden</p>
            <h3 class="mt-2 font-tac31-display text-[clamp(26px,3.6vw,40px)] leading-none font-extrabold tracking-[0.5em] whitespace-nowrap text-tac31-ivory uppercase transition-[letter-spacing,opacity] duration-1000 ease-[cubic-bezier(.2,.7,.2,1)] group-has-checked:tracking-[0.04em] group-has-checked:delay-200 motion-reduce:tracking-[0.04em] motion-reduce:transition-none">Still Water</h3>
            <p class="mt-2.5 max-w-[42ch] font-tac31-serif text-[17px] leading-[1.45] text-tac31-ivory/85 italic text-pretty">A ferry pilot on her final crossing discovers a passenger who never boarded.</p>
            <div class="mt-4 flex items-center gap-3">
              <span aria-hidden="true" class="grid size-11 place-items-center rounded-full bg-tac31-ivory text-tac31-ink shadow-[0_0_0_6px_rgb(255_255_255/.12)]"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M5 3.2v9.6L12.8 8z" fill="currentColor"/></svg></span>
              <span class="text-[13px] font-semibold text-tac31-ivory">Trailer <span class="font-tac31-mono font-normal text-tac31-mut">2:14</span></span>
            </div>
          </div>
        </div>
      </div>
      <div class="group relative h-[4.5rem] shrink-0 overflow-hidden rounded-[5px] transition-[height,flex-grow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] has-checked:h-[30rem] has-focus-visible:ring-2 has-focus-visible:ring-tac31-ivory has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac31-film sm:has-checked:h-[25rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[7] motion-reduce:transition-none" style="--tac31-t:#b8402a">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-4 px-5 text-tac31-ivory/90 ring-1 ring-white/7 ring-inset transition-[opacity,box-shadow] duration-300 [background:radial-gradient(90%_60%_at_50%_40%,color-mix(in_oklab,var(--tac31-t)_28%,transparent),transparent_75%),var(--color-tac31-frame)] hover:ring-white/20 group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-6 motion-reduce:transition-none">
          <input type="radio" name="tac31-lineup" id="tac31-b" class="sr-only">
          <span class="w-9 font-tac31-serif text-[26px] leading-none text-tac31-ivory/70 italic lg:w-auto">II</span>
          <span class="min-w-0 flex-1 truncate font-tac31-display text-[13px] font-bold tracking-[0.28em] uppercase lg:flex-none lg:[writing-mode:vertical-rl]">Red Harvest</span>
          <span class="font-tac31-mono text-[11px] text-tac31-mut">121′</span>
        </label>
        <div class="invisible absolute inset-0 z-10 overflow-hidden bg-linear-to-b from-[#5a120d] via-[#b3401f] to-[#efa057] opacity-0 transition-[opacity,visibility] duration-200 group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-150 group-has-checked:duration-500 lg:right-auto lg:w-[max(100%,40rem)] motion-reduce:transition-none">
          <svg class="absolute inset-0 size-full scale-110 transition-transform duration-[2400ms] ease-out group-has-checked:scale-100 motion-reduce:transition-none" viewBox="0 0 640 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <circle cx="470" cy="226" r="92" fill="#f8c36e" opacity="0.85"/>
              <path d="M0 250 Q160 214 320 236 T640 230 V360 H0Z" fill="#6e1b10"/>
              <path d="M0 286 Q200 252 400 276 T640 270 V360 H0Z" fill="#3a0c07"/>
              <circle cx="70" cy="222" r="30" fill="#4a1009"/><rect x="66" y="238" width="8" height="30" fill="#4a1009"/>
              <circle cx="150" cy="214" r="24" fill="#4a1009"/><rect x="147" y="228" width="6" height="28" fill="#4a1009"/>
              <circle cx="300" cy="214" r="28" fill="#4a1009"/><rect x="296" y="230" width="8" height="30" fill="#4a1009"/>
              <circle cx="590" cy="222" r="22" fill="#4a1009"/><rect x="587" y="234" width="6" height="26" fill="#4a1009"/>
              <circle cx="40" cy="268" r="40" fill="#2a0805"/><circle cx="610" cy="262" r="44" fill="#2a0805"/>
              <rect x="450" y="226" width="12" height="52" rx="5" fill="#1c0503"/><circle cx="456" cy="218" r="8" fill="#1c0503"/>
              <rect x="484" y="220" width="13" height="58" rx="5" fill="#1c0503"/><circle cx="490.5" cy="211" r="8.5" fill="#1c0503"/>
              <rect x="520" y="230" width="11" height="48" rx="5" fill="#1c0503"/><circle cx="525.5" cy="222" r="7.5" fill="#1c0503"/>
          </svg>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-t from-black/85 via-black/25 via-45% to-transparent"></span>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-r from-black/55 via-black/10 via-55% to-transparent"></span>
          <span aria-hidden="true" class="absolute inset-x-0 top-0 h-[10%] origin-top scale-y-0 bg-black transition-transform duration-700 ease-[cubic-bezier(.65,0,.2,1)] group-has-checked:scale-y-100 group-has-checked:delay-200 motion-reduce:scale-y-100 motion-reduce:transition-none"></span>
          <span aria-hidden="true" class="absolute inset-x-0 bottom-0 h-[10%] origin-bottom scale-y-0 bg-black transition-transform duration-700 ease-[cubic-bezier(.65,0,.2,1)] group-has-checked:scale-y-100 group-has-checked:delay-200 motion-reduce:scale-y-100 motion-reduce:transition-none"></span>
          <div class="absolute inset-x-5 top-[calc(10%+14px)] flex items-start justify-between gap-3 sm:inset-x-7">
            <p class="rounded-full bg-black/45 px-3 py-1.5 font-tac31-mono text-[10.5px] tracking-[0.16em] text-tac31-ivory/90 uppercase ring-1 ring-white/15 backdrop-blur-sm">Competition · II</p>
            <p class="flex items-center gap-1.5 rounded-full bg-tac31-ivory px-2.5 py-1 text-[12.5px] font-bold text-tac31-ink"><svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M8 1.5l1.9 4.1 4.5.5-3.4 3 1 4.4L8 11.3l-4 2.2 1-4.4-3.4-3 4.5-.5z" fill="currentColor"/></svg><span><span class="sr-only">Critics rating </span>8.9</span></p>
          </div>
          <div class="absolute inset-x-5 bottom-[calc(10%+18px)] sm:inset-x-7">
            <p class="font-tac31-mono text-[11px] tracking-[0.18em] text-tac31-mut uppercase">dir. T. Okonkwo · 121 min · Nigeria</p>
            <h3 class="mt-2 font-tac31-display text-[clamp(26px,3.6vw,40px)] leading-none font-extrabold tracking-[0.5em] whitespace-nowrap text-tac31-ivory uppercase transition-[letter-spacing,opacity] duration-1000 ease-[cubic-bezier(.2,.7,.2,1)] group-has-checked:tracking-[0.04em] group-has-checked:delay-200 motion-reduce:tracking-[0.04em] motion-reduce:transition-none">Red Harvest</h3>
            <p class="mt-2.5 max-w-[42ch] font-tac31-serif text-[17px] leading-[1.45] text-tac31-ivory/85 italic text-pretty">Three brothers, one orchard, and the season that will decide who keeps it.</p>
            <div class="mt-4 flex items-center gap-3">
              <span aria-hidden="true" class="grid size-11 place-items-center rounded-full bg-tac31-ivory text-tac31-ink shadow-[0_0_0_6px_rgb(255_255_255/.12)]"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M5 3.2v9.6L12.8 8z" fill="currentColor"/></svg></span>
              <span class="text-[13px] font-semibold text-tac31-ivory">Trailer <span class="font-tac31-mono font-normal text-tac31-mut">1:58</span></span>
            </div>
          </div>
        </div>
      </div>
      <div class="group relative h-[4.5rem] shrink-0 overflow-hidden rounded-[5px] transition-[height,flex-grow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] has-checked:h-[30rem] has-focus-visible:ring-2 has-focus-visible:ring-tac31-ivory has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac31-film sm:has-checked:h-[25rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[7] motion-reduce:transition-none" style="--tac31-t:#2f9a63">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-4 px-5 text-tac31-ivory/90 ring-1 ring-white/7 ring-inset transition-[opacity,box-shadow] duration-300 [background:radial-gradient(90%_60%_at_50%_40%,color-mix(in_oklab,var(--tac31-t)_28%,transparent),transparent_75%),var(--color-tac31-frame)] hover:ring-white/20 group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-6 motion-reduce:transition-none">
          <input type="radio" name="tac31-lineup" id="tac31-c" class="sr-only">
          <span class="w-9 font-tac31-serif text-[26px] leading-none text-tac31-ivory/70 italic lg:w-auto">III</span>
          <span class="min-w-0 flex-1 truncate font-tac31-display text-[13px] font-bold tracking-[0.28em] uppercase lg:flex-none lg:[writing-mode:vertical-rl]">Greenhouse</span>
          <span class="font-tac31-mono text-[11px] text-tac31-mut">84′</span>
        </label>
        <div class="invisible absolute inset-0 z-10 overflow-hidden bg-linear-to-b from-[#04100b] via-[#0b2a1c] to-[#123a28] opacity-0 transition-[opacity,visibility] duration-200 group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-150 group-has-checked:duration-500 lg:right-auto lg:w-[max(100%,40rem)] motion-reduce:transition-none">
          <svg class="absolute inset-0 size-full scale-110 transition-transform duration-[2400ms] ease-out group-has-checked:scale-100 motion-reduce:transition-none" viewBox="0 0 640 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <rect x="0" y="282" width="640" height="78" fill="#030a07"/>
              <polygon points="150,282 150,170 320,96 490,170 490,282" fill="#5fd896" opacity="0.13"/>
              <polygon points="150,282 150,170 320,96 490,170 490,282" fill="none" stroke="#9cf0c0" stroke-width="2" opacity="0.55"/>
              <path d="M192 152V282M234 133V282M277 115V282M320 96V282M363 115V282M406 133V282M448 152V282M150 216H490" stroke="#9cf0c0" stroke-width="1" opacity="0.35"/>
              <circle cx="200" cy="262" r="26" fill="#1f6b43"/><circle cx="246" cy="250" r="34" fill="#185a37"/><circle cx="420" cy="254" r="32" fill="#1f6b43"/><circle cx="460" cy="266" r="22" fill="#185a37"/>
              <path d="M300 282V236M300 248 Q284 236 276 240M300 258 Q318 244 326 248" stroke="#2c8a57" stroke-width="4" fill="none" stroke-linecap="round"/>
              <rect x="340" y="246" width="34" height="22" rx="2" fill="#c9ffe0" opacity="0.85"/>
              <rect x="350" y="226" width="11" height="40" rx="5" fill="#020604"/><circle cx="355.5" cy="218" r="8" fill="#020604"/>
              <circle cx="357" cy="257" r="60" fill="#9cf0c0" opacity="0.08"/>
          </svg>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-t from-black/85 via-black/25 via-45% to-transparent"></span>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-r from-black/55 via-black/10 via-55% to-transparent"></span>
          <span aria-hidden="true" class="absolute inset-x-0 top-0 h-[10%] origin-top scale-y-0 bg-black transition-transform duration-700 ease-[cubic-bezier(.65,0,.2,1)] group-has-checked:scale-y-100 group-has-checked:delay-200 motion-reduce:scale-y-100 motion-reduce:transition-none"></span>
          <span aria-hidden="true" class="absolute inset-x-0 bottom-0 h-[10%] origin-bottom scale-y-0 bg-black transition-transform duration-700 ease-[cubic-bezier(.65,0,.2,1)] group-has-checked:scale-y-100 group-has-checked:delay-200 motion-reduce:scale-y-100 motion-reduce:transition-none"></span>
          <div class="absolute inset-x-5 top-[calc(10%+14px)] flex items-start justify-between gap-3 sm:inset-x-7">
            <p class="rounded-full bg-black/45 px-3 py-1.5 font-tac31-mono text-[10.5px] tracking-[0.16em] text-tac31-ivory/90 uppercase ring-1 ring-white/15 backdrop-blur-sm">Competition · III</p>
            <p class="flex items-center gap-1.5 rounded-full bg-tac31-ivory px-2.5 py-1 text-[12.5px] font-bold text-tac31-ink"><svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M8 1.5l1.9 4.1 4.5.5-3.4 3 1 4.4L8 11.3l-4 2.2 1-4.4-3.4-3 4.5-.5z" fill="currentColor"/></svg><span><span class="sr-only">Critics rating </span>7.9</span></p>
          </div>
          <div class="absolute inset-x-5 bottom-[calc(10%+18px)] sm:inset-x-7">
            <p class="font-tac31-mono text-[11px] tracking-[0.18em] text-tac31-mut uppercase">dir. M. Duval · 84 min · Canada</p>
            <h3 class="mt-2 font-tac31-display text-[clamp(26px,3.6vw,40px)] leading-none font-extrabold tracking-[0.5em] whitespace-nowrap text-tac31-ivory uppercase transition-[letter-spacing,opacity] duration-1000 ease-[cubic-bezier(.2,.7,.2,1)] group-has-checked:tracking-[0.04em] group-has-checked:delay-200 motion-reduce:tracking-[0.04em] motion-reduce:transition-none">Greenhouse</h3>
            <p class="mt-2.5 max-w-[42ch] font-tac31-serif text-[17px] leading-[1.45] text-tac31-ivory/85 italic text-pretty">A botanist live-streams her last experiment; the plants start answering back.</p>
            <div class="mt-4 flex items-center gap-3">
              <span aria-hidden="true" class="grid size-11 place-items-center rounded-full bg-tac31-ivory text-tac31-ink shadow-[0_0_0_6px_rgb(255_255_255/.12)]"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M5 3.2v9.6L12.8 8z" fill="currentColor"/></svg></span>
              <span class="text-[13px] font-semibold text-tac31-ivory">Trailer <span class="font-tac31-mono font-normal text-tac31-mut">2:31</span></span>
            </div>
          </div>
        </div>
      </div>
      <div class="group relative h-[4.5rem] shrink-0 overflow-hidden rounded-[5px] transition-[height,flex-grow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] has-checked:h-[30rem] has-focus-visible:ring-2 has-focus-visible:ring-tac31-ivory has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac31-film sm:has-checked:h-[25rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[7] motion-reduce:transition-none" style="--tac31-t:#c04bd6">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-4 px-5 text-tac31-ivory/90 ring-1 ring-white/7 ring-inset transition-[opacity,box-shadow] duration-300 [background:radial-gradient(90%_60%_at_50%_40%,color-mix(in_oklab,var(--tac31-t)_28%,transparent),transparent_75%),var(--color-tac31-frame)] hover:ring-white/20 group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-6 motion-reduce:transition-none">
          <input type="radio" name="tac31-lineup" id="tac31-d" class="sr-only">
          <span class="w-9 font-tac31-serif text-[26px] leading-none text-tac31-ivory/70 italic lg:w-auto">IV</span>
          <span class="min-w-0 flex-1 truncate font-tac31-display text-[13px] font-bold tracking-[0.28em] uppercase lg:flex-none lg:[writing-mode:vertical-rl]">Night Shift</span>
          <span class="font-tac31-mono text-[11px] text-tac31-mut">108′</span>
        </label>
        <div class="invisible absolute inset-0 z-10 overflow-hidden bg-linear-to-b from-[#0a0920] via-[#1e1040] to-[#3b1450] opacity-0 transition-[opacity,visibility] duration-200 group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-150 group-has-checked:duration-500 lg:right-auto lg:w-[max(100%,40rem)] motion-reduce:transition-none">
          <svg class="absolute inset-0 size-full scale-110 transition-transform duration-[2400ms] ease-out group-has-checked:scale-100 motion-reduce:transition-none" viewBox="0 0 640 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <rect x="20" y="96" width="90" height="190" fill="#120f26"/><rect x="118" y="130" width="70" height="156" fill="#17132e"/><rect x="200" y="70" width="104" height="216" fill="#100d22"/>
              <rect x="420" y="110" width="96" height="176" fill="#120f26"/><rect x="526" y="80" width="88" height="206" fill="#17132e"/>
              <path d="M36 116h8M56 116h8M76 116h8M36 140h8M76 140h8M56 164h8M36 188h8M76 188h8M216 92h10M246 92h10M276 92h10M216 120h10M276 120h10M246 148h10M216 176h10M246 204h10M436 130h10M466 130h10M496 130h10M466 160h10M436 190h10M496 190h10M542 100h10M572 100h10M542 130h10M592 160h10M572 190h10" stroke="#ffd36e" stroke-width="7" opacity="0.75"/>
              <rect x="226" y="56" width="52" height="12" rx="3" fill="#ff4fa0"/><rect x="440" y="96" width="56" height="10" rx="3" fill="#47d4ff"/>
              <rect x="0" y="286" width="640" height="74" fill="#07061a"/>
              <path d="M226 302H278M440 300H496M60 316H140M520 322H600" stroke="#ff4fa0" stroke-width="3" opacity="0.4" stroke-linecap="round"/>
              <path d="M240 330H270M448 330H488" stroke="#47d4ff" stroke-width="3" opacity="0.35" stroke-linecap="round"/>
              <rect x="300" y="244" width="130" height="44" rx="6" fill="#1a1630"/><path d="M312 254H418" stroke="#ffe7a8" stroke-width="12" opacity="0.8"/><circle cx="324" cy="290" r="8" fill="#05040f"/><circle cx="406" cy="290" r="8" fill="#05040f"/>
          </svg>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-t from-black/85 via-black/25 via-45% to-transparent"></span>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-r from-black/55 via-black/10 via-55% to-transparent"></span>
          <span aria-hidden="true" class="absolute inset-x-0 top-0 h-[10%] origin-top scale-y-0 bg-black transition-transform duration-700 ease-[cubic-bezier(.65,0,.2,1)] group-has-checked:scale-y-100 group-has-checked:delay-200 motion-reduce:scale-y-100 motion-reduce:transition-none"></span>
          <span aria-hidden="true" class="absolute inset-x-0 bottom-0 h-[10%] origin-bottom scale-y-0 bg-black transition-transform duration-700 ease-[cubic-bezier(.65,0,.2,1)] group-has-checked:scale-y-100 group-has-checked:delay-200 motion-reduce:scale-y-100 motion-reduce:transition-none"></span>
          <div class="absolute inset-x-5 top-[calc(10%+14px)] flex items-start justify-between gap-3 sm:inset-x-7">
            <p class="rounded-full bg-black/45 px-3 py-1.5 font-tac31-mono text-[10.5px] tracking-[0.16em] text-tac31-ivory/90 uppercase ring-1 ring-white/15 backdrop-blur-sm">Competition · IV</p>
            <p class="flex items-center gap-1.5 rounded-full bg-tac31-ivory px-2.5 py-1 text-[12.5px] font-bold text-tac31-ink"><svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M8 1.5l1.9 4.1 4.5.5-3.4 3 1 4.4L8 11.3l-4 2.2 1-4.4-3.4-3 4.5-.5z" fill="currentColor"/></svg><span><span class="sr-only">Critics rating </span>8.2</span></p>
          </div>
          <div class="absolute inset-x-5 bottom-[calc(10%+18px)] sm:inset-x-7">
            <p class="font-tac31-mono text-[11px] tracking-[0.18em] text-tac31-mut uppercase">dir. A. Park · 108 min · South Korea</p>
            <h3 class="mt-2 font-tac31-display text-[clamp(26px,3.6vw,40px)] leading-none font-extrabold tracking-[0.5em] whitespace-nowrap text-tac31-ivory uppercase transition-[letter-spacing,opacity] duration-1000 ease-[cubic-bezier(.2,.7,.2,1)] group-has-checked:tracking-[0.04em] group-has-checked:delay-200 motion-reduce:tracking-[0.04em] motion-reduce:transition-none">Night Shift</h3>
            <p class="mt-2.5 max-w-[42ch] font-tac31-serif text-[17px] leading-[1.45] text-tac31-ivory/85 italic text-pretty">A night-bus driver memorises every regular — until one of them stops getting on.</p>
            <div class="mt-4 flex items-center gap-3">
              <span aria-hidden="true" class="grid size-11 place-items-center rounded-full bg-tac31-ivory text-tac31-ink shadow-[0_0_0_6px_rgb(255_255_255/.12)]"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M5 3.2v9.6L12.8 8z" fill="currentColor"/></svg></span>
              <span class="text-[13px] font-semibold text-tac31-ivory">Trailer <span class="font-tac31-mono font-normal text-tac31-mut">2:05</span></span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-tac31-mono text-[11.5px] text-tac31-mut">tracking-[0.5em] → group-has-checked:tracking-[0.04em] · scale-y-0 letterbox · grow-[7]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac31-bg: #09090b;
  --color-tac31-bg: oklch(0.14 0.004 285);
  --color-tac31-glow: #23181a;
  --color-tac31-glow: oklch(0.22 0.02 15);
  --color-tac31-film: #1c1a1f;
  --color-tac31-film: oklch(0.22 0.008 300);
  --color-tac31-frame: #101013;
  --color-tac31-frame: oklch(0.17 0.005 285);
  --color-tac31-hole: #050506;
  --color-tac31-hole: oklch(0.1 0.003 285);
  --color-tac31-ivory: #f1ece1;
  --color-tac31-ivory: oklch(0.94 0.014 85);
  --color-tac31-mut: #b3ada3;
  --color-tac31-mut: oklch(0.75 0.013 80);
  --color-tac31-ink: #16141a;
  --color-tac31-ink: oklch(0.2 0.01 300);
  --color-tac31-gold: #e2b66a;
  --color-tac31-gold: oklch(0.8 0.1 80);
  --font-tac31-display: 'Archivo', system-ui, sans-serif;
  --font-tac31-sans: 'Archivo', system-ui, sans-serif;
  --font-tac31-serif: 'Instrument Serif', Georgia, serif;
  --font-tac31-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-31 {
  width: 100%;
  min-height: 100svh;
}
```
