---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-expanding-image-gallery-accordion/"
title: "Tailwind CSS Expanding Image Gallery Accordion"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "The portfolio showstopper as a travel journal: four full-bleed scene panels that expand on selection while their siblings sit desaturated with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Expanding Image Gallery Accordion
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-expanding-image-gallery-accordion/

The portfolio showstopper as a travel journal: four full-bleed scene panels that expand on selection while their siblings sit desaturated with grayscale-[.85] brightness-[.62]. The open panel blooms into full colour, its scene eases out of a slow Ken Burns zoom, and a serif caption with EXIF chips rises from a scrim. Every scene is inline SVG — swap in a photo and nothing else changes.
## HTML
```html
<section class="tac-26 w-full min-h-svh grid place-items-center bg-tac26-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tac26-glow),transparent_70%)] px-5 py-14 font-tac26-sans text-tac26-ink" aria-label="Expanding image gallery accordion demo">
  <div class="grid w-full max-w-5xl gap-8">
    <header class="flex flex-wrap items-end justify-between gap-x-10 gap-y-4">
      <div>
        <p class="font-tac26-mono text-xs tracking-[0.16em] text-tac26-acc uppercase">Field Notes · Vol. 07</p>
        <h2 class="mt-3 max-w-[18ch] font-tac26-serif text-[clamp(34px,5vw,54px)] leading-[0.98] tracking-[-0.01em] text-balance">Four places that <em class="text-tac26-acc">rearranged</em> our sense of scale.</h2>
      </div>
      <p class="max-w-[32ch] text-sm leading-relaxed text-tac26-mut">A year on foot, by boat and by switchback. Select a frame to open the full plate and its notes.</p>
    </header>

    <div class="@container w-full">
      <div role="radiogroup" aria-label="Expedition gallery" class="flex h-[29rem] gap-2.5 @max-2xl:h-auto @max-2xl:flex-col">

        <label class="group/p relative flex min-w-14 grow basis-0 cursor-pointer overflow-hidden rounded-[20px] bg-tac26-card ring-1 ring-white/10 transition-[flex-grow,box-shadow] duration-700 ease-[cubic-bezier(.65,0,.35,1)] hover:ring-white/25 has-checked:grow-[5] has-checked:shadow-tac26-lift has-checked:ring-white/20 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tac26-acc motion-reduce:transition-none @max-2xl:basis-auto @max-2xl:flex-col">
          <input type="radio" name="tac26-trip" id="tac26-erg" class="sr-only" checked>
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-b from-tac26-s1a to-tac26-s1b brightness-[.62] grayscale-[.85] transition-[filter] duration-700 group-hover/p:brightness-[.8] group-hover/p:grayscale-[.4] group-has-checked/p:brightness-100 group-has-checked/p:grayscale-0 motion-reduce:transition-none">
            <svg class="absolute inset-0 size-full scale-110 transition-transform duration-[1400ms] ease-out group-has-checked/p:scale-100 motion-reduce:transition-none" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <circle cx="520" cy="250" r="150" fill="#ffd9a0" opacity="0.22"/>
              <circle cx="520" cy="250" r="64" fill="#ffe7bd"/>
              <path d="M0 330 C120 290 220 300 330 320 S560 280 800 310 V500 H0Z" fill="#d9774a"/>
              <path d="M0 380 C150 330 260 350 380 390 S620 340 800 370 V500 H0Z" fill="#b34f3a"/>
              <path d="M380 390 C460 410 540 395 620 360" fill="none" stroke="#ffc59a" stroke-width="2" opacity="0.45"/>
              <path d="M0 440 C180 400 320 420 460 455 S700 420 800 430 V500 H0Z" fill="#6f2b3c"/>
              <path d="M640 298 l4 -12 l4 12 M660 296 l4 -12 l4 12 M680 295 l4 -12 l4 12" fill="none" stroke="#5a2230" stroke-width="2.5" stroke-linecap="round"/>
            </svg>
          </span>
          <span class="absolute inset-0 flex flex-col items-center justify-between bg-linear-to-t from-black/60 to-transparent to-45% py-4 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl:relative @max-2xl:min-h-16 @max-2xl:flex-row @max-2xl:justify-start @max-2xl:gap-3 @max-2xl:bg-linear-to-r @max-2xl:from-black/70 @max-2xl:to-black/10 @max-2xl:px-4 @max-2xl:py-0 @max-2xl:group-has-checked/p:opacity-100 @max-2xl:group-has-checked/p:bg-linear-to-b @max-2xl:group-has-checked/p:from-black/50 @max-2xl:group-has-checked/p:to-transparent">
            <i class="rounded-full bg-black/50 px-2 py-1 font-tac26-mono text-[11px] font-medium not-italic text-white ring-1 ring-white/20">01</i>
            <b class="rotate-180 text-[13px] font-semibold tracking-[0.16em] text-white uppercase [writing-mode:vertical-rl] @max-2xl:rotate-0 @max-2xl:[writing-mode:horizontal-tb]">Erg Chebbi</b>
          </span>
          <span class="relative flex min-w-0 flex-1 translate-y-3 items-end opacity-0 transition-[opacity,translate] duration-500 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-300 motion-reduce:transition-none @max-2xl:grid @max-2xl:grid-rows-[0fr] @max-2xl:translate-y-0 @max-2xl:transition-[grid-template-rows,opacity] @max-2xl:group-has-checked/p:grid-rows-[1fr] @max-2xl:group-has-checked/p:delay-0">
            <span class="absolute top-5 left-6 flex items-center gap-2 rounded-full bg-black/45 py-1 pr-3 pl-1 font-tac26-mono text-[11px] text-white ring-1 ring-white/15 backdrop-blur-md @max-2xl:hidden"><span class="rounded-full bg-white px-2 py-0.5 font-semibold text-tac26-bg">01 / 04</span>Erg Chebbi</span>
            <span class="block w-full min-w-[22rem] overflow-hidden @max-2xl:min-h-0 @max-2xl:min-w-0">
              <span class="block bg-linear-to-t from-black/85 via-black/50 to-transparent px-7 pt-28 pb-7 @max-2xl:px-5 @max-2xl:pt-44 @max-2xl:pb-5">
                <span class="block font-tac26-mono text-[11px] tracking-[0.12em] text-white/80 uppercase">Morocco · 31.1°N 4.0°W</span>
                <b class="mt-2 block font-tac26-serif text-[clamp(32px,4.2vw,46px)] leading-none font-normal tracking-[-0.01em] text-white">Desert dawn</b>
                <span class="mt-3 block max-w-[44ch] text-[15px] leading-relaxed text-white/85">First light on the dune sea. 41°C by nine, and a silence so complete you can hear the sand settle.</span>
                <span class="mt-5 flex flex-wrap gap-1.5 font-tac26-mono text-[11px] text-white/90"><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">35mm</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">f/8</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">1/500s</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">ISO 100</span></span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p relative flex min-w-14 grow basis-0 cursor-pointer overflow-hidden rounded-[20px] bg-tac26-card ring-1 ring-white/10 transition-[flex-grow,box-shadow] duration-700 ease-[cubic-bezier(.65,0,.35,1)] hover:ring-white/25 has-checked:grow-[5] has-checked:shadow-tac26-lift has-checked:ring-white/20 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tac26-acc motion-reduce:transition-none @max-2xl:basis-auto @max-2xl:flex-col">
          <input type="radio" name="tac26-trip" id="tac26-fjord" class="sr-only">
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-b from-tac26-s2a to-tac26-s2b brightness-[.62] grayscale-[.85] transition-[filter] duration-700 group-hover/p:brightness-[.8] group-hover/p:grayscale-[.4] group-has-checked/p:brightness-100 group-has-checked/p:grayscale-0 motion-reduce:transition-none">
            <svg class="absolute inset-0 size-full scale-110 transition-transform duration-[1400ms] ease-out group-has-checked/p:scale-100 motion-reduce:transition-none" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <ellipse cx="560" cy="110" rx="120" ry="18" fill="#ffffff" opacity="0.35"/>
              <ellipse cx="250" cy="80" rx="90" ry="12" fill="#ffffff" opacity="0.25"/>
              <path d="M0 260 L90 190 L170 235 L260 160 L340 220 L420 170 L520 240 L610 180 L700 230 L800 200 V330 H0Z" fill="#5f86a5"/>
              <path d="M0 120 L120 150 L210 260 L260 330 L0 340Z" fill="#1f3346"/>
              <path d="M800 90 L690 140 L600 250 L540 330 L800 340Z" fill="#172838"/>
              <rect x="0" y="325" width="800" height="175" fill="#23435c"/>
              <path d="M240 360 H330 M470 352 H560 M300 420 H420 M520 450 H640 M120 470 H200" stroke="#a8d0ea" stroke-width="2" stroke-linecap="round" opacity="0.4"/>
              <path d="M582 358 L500 372" stroke="#ffffff" stroke-width="2" opacity="0.45"/>
              <path d="M570 350 L622 350 L613 361 L578 361Z" fill="#f2f5f8"/>
              <rect x="590" y="338" width="10" height="12" rx="1" fill="#e2552f"/>
            </svg>
          </span>
          <span class="absolute inset-0 flex flex-col items-center justify-between bg-linear-to-t from-black/60 to-transparent to-45% py-4 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl:relative @max-2xl:min-h-16 @max-2xl:flex-row @max-2xl:justify-start @max-2xl:gap-3 @max-2xl:bg-linear-to-r @max-2xl:from-black/70 @max-2xl:to-black/10 @max-2xl:px-4 @max-2xl:py-0 @max-2xl:group-has-checked/p:opacity-100 @max-2xl:group-has-checked/p:bg-linear-to-b @max-2xl:group-has-checked/p:from-black/50 @max-2xl:group-has-checked/p:to-transparent">
            <i class="rounded-full bg-black/50 px-2 py-1 font-tac26-mono text-[11px] font-medium not-italic text-white ring-1 ring-white/20">02</i>
            <b class="rotate-180 text-[13px] font-semibold tracking-[0.16em] text-white uppercase [writing-mode:vertical-rl] @max-2xl:rotate-0 @max-2xl:[writing-mode:horizontal-tb]">Lysefjord</b>
          </span>
          <span class="relative flex min-w-0 flex-1 translate-y-3 items-end opacity-0 transition-[opacity,translate] duration-500 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-300 motion-reduce:transition-none @max-2xl:grid @max-2xl:grid-rows-[0fr] @max-2xl:translate-y-0 @max-2xl:transition-[grid-template-rows,opacity] @max-2xl:group-has-checked/p:grid-rows-[1fr] @max-2xl:group-has-checked/p:delay-0">
            <span class="absolute top-5 left-6 flex items-center gap-2 rounded-full bg-black/45 py-1 pr-3 pl-1 font-tac26-mono text-[11px] text-white ring-1 ring-white/15 backdrop-blur-md @max-2xl:hidden"><span class="rounded-full bg-white px-2 py-0.5 font-semibold text-tac26-bg">02 / 04</span>Lysefjord</span>
            <span class="block w-full min-w-[22rem] overflow-hidden @max-2xl:min-h-0 @max-2xl:min-w-0">
              <span class="block bg-linear-to-t from-black/85 via-black/50 to-transparent px-7 pt-28 pb-7 @max-2xl:px-5 @max-2xl:pt-44 @max-2xl:pb-5">
                <span class="block font-tac26-mono text-[11px] tracking-[0.12em] text-white/80 uppercase">Norway · 59.0°N 6.2°E</span>
                <b class="mt-2 block font-tac26-serif text-[clamp(32px,4.2vw,46px)] leading-none font-normal tracking-[-0.01em] text-white">Fjord crossing</b>
                <span class="mt-3 block max-w-[44ch] text-[15px] leading-relaxed text-white/85">Six hours by open boat between walls of thousand-metre granite, the engine the only sound for miles.</span>
                <span class="mt-5 flex flex-wrap gap-1.5 font-tac26-mono text-[11px] text-white/90"><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">24mm</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">f/11</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">1/250s</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">ISO 200</span></span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p relative flex min-w-14 grow basis-0 cursor-pointer overflow-hidden rounded-[20px] bg-tac26-card ring-1 ring-white/10 transition-[flex-grow,box-shadow] duration-700 ease-[cubic-bezier(.65,0,.35,1)] hover:ring-white/25 has-checked:grow-[5] has-checked:shadow-tac26-lift has-checked:ring-white/20 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tac26-acc motion-reduce:transition-none @max-2xl:basis-auto @max-2xl:flex-col">
          <input type="radio" name="tac26-trip" id="tac26-cloud" class="sr-only">
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-b from-tac26-s3a to-tac26-s3b brightness-[.62] grayscale-[.85] transition-[filter] duration-700 group-hover/p:brightness-[.8] group-hover/p:grayscale-[.4] group-has-checked/p:brightness-100 group-has-checked/p:grayscale-0 motion-reduce:transition-none">
            <svg class="absolute inset-0 size-full scale-110 transition-transform duration-[1400ms] ease-out group-has-checked/p:scale-100 motion-reduce:transition-none" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <path d="M0 250 Q200 170 400 230 T800 210 V500 H0Z" fill="#6f9f80"/>
              <rect x="556" y="215" width="8" height="110" rx="4" fill="#f4fff6" opacity="0.6"/>
              <path d="M0 300 Q40 255 80 300 Q120 248 160 300 Q200 262 240 300 Q290 252 330 300 Q370 258 410 300 Q460 248 500 300 Q540 262 580 300 Q630 252 670 300 Q710 258 750 300 Q780 268 800 290 V500 H0Z" fill="#3b6e50"/>
              <ellipse cx="400" cy="318" rx="520" ry="38" fill="#ffffff" opacity="0.28"/>
              <path d="M0 390 Q60 320 120 390 Q190 315 260 390 Q330 330 400 390 Q470 318 540 390 Q610 326 680 390 Q740 330 800 380 V500 H0Z" fill="#1d4231"/>
              <ellipse cx="300" cy="410" rx="420" ry="26" fill="#ffffff" opacity="0.16"/>
              <path d="M0 500 L0 455 Q50 420 90 470 Q120 430 170 475 Q220 440 260 480 L800 480 L800 500Z" fill="#10291d"/>
            </svg>
          </span>
          <span class="absolute inset-0 flex flex-col items-center justify-between bg-linear-to-t from-black/60 to-transparent to-45% py-4 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl:relative @max-2xl:min-h-16 @max-2xl:flex-row @max-2xl:justify-start @max-2xl:gap-3 @max-2xl:bg-linear-to-r @max-2xl:from-black/70 @max-2xl:to-black/10 @max-2xl:px-4 @max-2xl:py-0 @max-2xl:group-has-checked/p:opacity-100 @max-2xl:group-has-checked/p:bg-linear-to-b @max-2xl:group-has-checked/p:from-black/50 @max-2xl:group-has-checked/p:to-transparent">
            <i class="rounded-full bg-black/50 px-2 py-1 font-tac26-mono text-[11px] font-medium not-italic text-white ring-1 ring-white/20">03</i>
            <b class="rotate-180 text-[13px] font-semibold tracking-[0.16em] text-white uppercase [writing-mode:vertical-rl] @max-2xl:rotate-0 @max-2xl:[writing-mode:horizontal-tb]">Monteverde</b>
          </span>
          <span class="relative flex min-w-0 flex-1 translate-y-3 items-end opacity-0 transition-[opacity,translate] duration-500 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-300 motion-reduce:transition-none @max-2xl:grid @max-2xl:grid-rows-[0fr] @max-2xl:translate-y-0 @max-2xl:transition-[grid-template-rows,opacity] @max-2xl:group-has-checked/p:grid-rows-[1fr] @max-2xl:group-has-checked/p:delay-0">
            <span class="absolute top-5 left-6 flex items-center gap-2 rounded-full bg-black/45 py-1 pr-3 pl-1 font-tac26-mono text-[11px] text-white ring-1 ring-white/15 backdrop-blur-md @max-2xl:hidden"><span class="rounded-full bg-white px-2 py-0.5 font-semibold text-tac26-bg">03 / 04</span>Monteverde</span>
            <span class="block w-full min-w-[22rem] overflow-hidden @max-2xl:min-h-0 @max-2xl:min-w-0">
              <span class="block bg-linear-to-t from-black/85 via-black/50 to-transparent px-7 pt-28 pb-7 @max-2xl:px-5 @max-2xl:pt-44 @max-2xl:pb-5">
                <span class="block font-tac26-mono text-[11px] tracking-[0.12em] text-white/80 uppercase">Costa Rica · 10.3°N 84.8°W</span>
                <b class="mt-2 block font-tac26-serif text-[clamp(32px,4.2vw,46px)] leading-none font-normal tracking-[-0.01em] text-white">Cloud forest</b>
                <span class="mt-3 block max-w-[44ch] text-[15px] leading-relaxed text-white/85">Every surface grows something. GPS was useless under the canopy, so we navigated by the sound of the river.</span>
                <span class="mt-5 flex flex-wrap gap-1.5 font-tac26-mono text-[11px] text-white/90"><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">50mm</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">f/2.8</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">1/125s</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">ISO 800</span></span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p relative flex min-w-14 grow basis-0 cursor-pointer overflow-hidden rounded-[20px] bg-tac26-card ring-1 ring-white/10 transition-[flex-grow,box-shadow] duration-700 ease-[cubic-bezier(.65,0,.35,1)] hover:ring-white/25 has-checked:grow-[5] has-checked:shadow-tac26-lift has-checked:ring-white/20 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tac26-acc motion-reduce:transition-none @max-2xl:basis-auto @max-2xl:flex-col">
          <input type="radio" name="tac26-trip" id="tac26-pass" class="sr-only">
          <span aria-hidden="true" class="absolute inset-0 bg-linear-to-b from-tac26-s4a to-tac26-s4b brightness-[.62] grayscale-[.85] transition-[filter] duration-700 group-hover/p:brightness-[.8] group-hover/p:grayscale-[.4] group-has-checked/p:brightness-100 group-has-checked/p:grayscale-0 motion-reduce:transition-none">
            <svg class="absolute inset-0 size-full scale-110 transition-transform duration-[1400ms] ease-out group-has-checked/p:scale-100 motion-reduce:transition-none" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <circle cx="120" cy="70" r="1.6" fill="#ffffff"/><circle cx="210" cy="40" r="1.2" fill="#ffffff" opacity="0.8"/><circle cx="330" cy="95" r="1.4" fill="#ffffff"/><circle cx="430" cy="50" r="1" fill="#ffffff" opacity="0.7"/><circle cx="560" cy="80" r="1.5" fill="#ffffff"/><circle cx="700" cy="45" r="1.2" fill="#ffffff" opacity="0.8"/><circle cx="760" cy="120" r="1" fill="#ffffff" opacity="0.6"/><circle cx="60" cy="150" r="1" fill="#ffffff" opacity="0.6"/>
              <circle cx="640" cy="105" r="22" fill="#f5f2e3"/>
              <path d="M0 330 L120 220 L190 270 L300 140 L380 230 L460 180 L560 260 L650 170 L800 300 V500 H0Z" fill="#6c79b0"/>
              <path d="M300 140 L338 188 L318 182 L302 198 L286 180 L264 186Z" fill="#eef1ff"/>
              <path d="M650 170 L686 212 L668 206 L652 220 L636 205 L618 210Z" fill="#eef1ff"/>
              <path d="M460 180 L484 206 L470 203 L458 212 L446 202Z" fill="#eef1ff"/>
              <path d="M0 420 L200 350 L340 390 L480 330 L620 380 L800 350 V500 H0Z" fill="#262c4c"/>
              <path d="M470 352 Q600 300 790 318" fill="none" stroke="#e5e7f5" stroke-width="1.5" opacity="0.6"/>
              <rect x="500" y="338" width="12" height="16" fill="#e94f4f"/><rect x="535" y="327" width="12" height="16" fill="#f2c14e"/><rect x="570" y="319" width="12" height="16" fill="#4f8fe9"/><rect x="605" y="313" width="12" height="16" fill="#f5f5f5"/><rect x="640" y="309" width="12" height="16" fill="#4fbf7a"/><rect x="675" y="308" width="12" height="16" fill="#e94f4f"/><rect x="710" y="308" width="12" height="16" fill="#f2c14e"/><rect x="745" y="310" width="12" height="16" fill="#4f8fe9"/>
            </svg>
          </span>
          <span class="absolute inset-0 flex flex-col items-center justify-between bg-linear-to-t from-black/60 to-transparent to-45% py-4 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl:relative @max-2xl:min-h-16 @max-2xl:flex-row @max-2xl:justify-start @max-2xl:gap-3 @max-2xl:bg-linear-to-r @max-2xl:from-black/70 @max-2xl:to-black/10 @max-2xl:px-4 @max-2xl:py-0 @max-2xl:group-has-checked/p:opacity-100 @max-2xl:group-has-checked/p:bg-linear-to-b @max-2xl:group-has-checked/p:from-black/50 @max-2xl:group-has-checked/p:to-transparent">
            <i class="rounded-full bg-black/50 px-2 py-1 font-tac26-mono text-[11px] font-medium not-italic text-white ring-1 ring-white/20">04</i>
            <b class="rotate-180 text-[13px] font-semibold tracking-[0.16em] text-white uppercase [writing-mode:vertical-rl] @max-2xl:rotate-0 @max-2xl:[writing-mode:horizontal-tb]">Thorong La</b>
          </span>
          <span class="relative flex min-w-0 flex-1 translate-y-3 items-end opacity-0 transition-[opacity,translate] duration-500 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-300 motion-reduce:transition-none @max-2xl:grid @max-2xl:grid-rows-[0fr] @max-2xl:translate-y-0 @max-2xl:transition-[grid-template-rows,opacity] @max-2xl:group-has-checked/p:grid-rows-[1fr] @max-2xl:group-has-checked/p:delay-0">
            <span class="absolute top-5 left-6 flex items-center gap-2 rounded-full bg-black/45 py-1 pr-3 pl-1 font-tac26-mono text-[11px] text-white ring-1 ring-white/15 backdrop-blur-md @max-2xl:hidden"><span class="rounded-full bg-white px-2 py-0.5 font-semibold text-tac26-bg">04 / 04</span>Thorong La</span>
            <span class="block w-full min-w-[22rem] overflow-hidden @max-2xl:min-h-0 @max-2xl:min-w-0">
              <span class="block bg-linear-to-t from-black/85 via-black/50 to-transparent px-7 pt-28 pb-7 @max-2xl:px-5 @max-2xl:pt-44 @max-2xl:pb-5">
                <span class="block font-tac26-mono text-[11px] tracking-[0.12em] text-white/80 uppercase">Nepal · 28.8°N 83.9°E</span>
                <b class="mt-2 block font-tac26-serif text-[clamp(32px,4.2vw,46px)] leading-none font-normal tracking-[-0.01em] text-white">High pass</b>
                <span class="mt-3 block max-w-[44ch] text-[15px] leading-relaxed text-white/85">5,416 metres at dusk. The tea froze in the cup before we had finished pouring the second round.</span>
                <span class="mt-5 flex flex-wrap gap-1.5 font-tac26-mono text-[11px] text-white/90"><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">16mm</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">f/4</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">8s</span><span class="rounded-md bg-white/10 px-2 py-1 ring-1 ring-white/15">ISO 1600</span></span>
              </span>
            </span>
          </span>
        </label>

      </div>
    </div>

    <p aria-hidden="true" class="max-w-full justify-self-center rounded-full border border-white/12 px-3.5 py-2 text-center font-tac26-mono text-[11.5px] text-balance text-tac26-mut">grayscale-[.85] · has-checked:grow-[5] · bg-linear-to-t</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac26-bg: #0b0d11;
  --color-tac26-bg: oklch(0.16 0.008 260);
  --color-tac26-glow: #1d2230;
  --color-tac26-glow: oklch(0.25 0.025 265);
  --color-tac26-card: #161a22;
  --color-tac26-card: oklch(0.21 0.015 260);
  --color-tac26-ink: #f5f1e9;
  --color-tac26-ink: oklch(0.96 0.01 80);
  --color-tac26-mut: #a7acb8;
  --color-tac26-mut: oklch(0.75 0.018 265);
  --color-tac26-acc: #f0b37a;
  --color-tac26-acc: oklch(0.82 0.1 65);
  --color-tac26-s1a: #f3a86b;
  --color-tac26-s1a: oklch(0.79 0.12 60);
  --color-tac26-s1b: #b9524a;
  --color-tac26-s1b: oklch(0.57 0.14 28);
  --color-tac26-s2a: #a9cde4;
  --color-tac26-s2a: oklch(0.83 0.05 235);
  --color-tac26-s2b: #4f7fa3;
  --color-tac26-s2b: oklch(0.56 0.08 245);
  --color-tac26-s3a: #c7e3cb;
  --color-tac26-s3a: oklch(0.89 0.045 150);
  --color-tac26-s3b: #6e9f7f;
  --color-tac26-s3b: oklch(0.65 0.07 155);
  --color-tac26-s4a: #141a36;
  --color-tac26-s4a: oklch(0.22 0.06 275);
  --color-tac26-s4b: #6a5d96;
  --color-tac26-s4b: oklch(0.5 0.09 295);
  --shadow-tac26-lift: 0 30px 60px -20px oklch(0 0 0 / 0.7), 0 0 0 1px oklch(1 0 0 / 0.06);
  --font-tac26-serif: 'Instrument Serif', Georgia, serif;
  --font-tac26-sans: 'Manrope', system-ui, sans-serif;
  --font-tac26-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-26 {
  width: 100%;
  min-height: 100svh;
}
```
