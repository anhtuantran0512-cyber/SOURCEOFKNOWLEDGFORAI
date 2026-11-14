---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/glassmorphism-vertical-tabs-in-tailwind-css-backdrop-blur/"
title: "Glassmorphism Vertical Tabs in Tailwind CSS (Backdrop Blur)"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A frosted Aurora OS settings window floating over a hand-drawn aurora night (a pastel dawn in light mode): one glass surface built from bg-tvt17-glass…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Vertical Tabs in Tailwind CSS (Backdrop Blur)
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/glassmorphism-vertical-tabs-in-tailwind-css-backdrop-blur/

A frosted Aurora OS settings window floating over a hand-drawn aurora night (a pastel dawn in light mode): one glass surface built from bg-tvt17-glass backdrop-blur-2xl backdrop-saturate-[1.8], a hairline edge and an inset top highlight &mdash; but only behind supports-[backdrop-filter:blur(1px)]:, so browsers without the filter get an opaque, readable panel. Four radio tabs switch panels with has-checked: and group-has-[…]/win:, and the Saturation panel shows blur-only versus blur-plus-saturate side by side, live.
## HTML
```html
<section class="tvt-17 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-tvt17-sky1 px-4 pt-20 pb-14 font-tvt17-sans text-tvt17-ink antialiased sm:px-6" aria-label="Glassmorphism vertical tabs in Tailwind CSS demo">
  <svg aria-hidden="true" focusable="false" class="absolute inset-0 -z-10 size-full" viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice">
    <defs>
      <linearGradient id="tvt-17-sky" x1="0" x2="0" y1="0" y2="1"><stop offset="0" style="stop-color:var(--color-tvt17-sky1)"/><stop offset=".55" style="stop-color:var(--color-tvt17-sky2)"/><stop offset="1" style="stop-color:var(--color-tvt17-sky3)"/></linearGradient>
      <linearGradient id="tvt-17-lake" x1="0" x2="0" y1="0" y2="1"><stop offset="0" style="stop-color:var(--color-tvt17-lake)"/><stop offset="1" style="stop-color:var(--color-tvt17-mtn2)"/></linearGradient>
      <filter id="tvt-17-soft" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="38"/></filter>
    </defs>
    <rect width="1600" height="1000" fill="url(#tvt-17-sky)"/>
    <g style="fill:var(--color-tvt17-star)"><circle cx="120" cy="90" r="1.6"/><circle cx="260" cy="210" r="1.2"/><circle cx="410" cy="60" r="1.8"/><circle cx="560" cy="150" r="1.1"/><circle cx="720" cy="40" r="1.4"/><circle cx="880" cy="120" r="1.7"/><circle cx="1010" cy="70" r="1.2"/><circle cx="1180" cy="170" r="1.5"/><circle cx="1320" cy="50" r="1.9"/><circle cx="1480" cy="130" r="1.2"/><circle cx="1540" cy="260" r="1.4"/><circle cx="60" cy="300" r="1.1"/><circle cx="330" cy="330" r="1.3"/><circle cx="960" cy="260" r="1.1"/></g>
    <g filter="url(#tvt-17-soft)" opacity=".9">
      <g class="origin-center animate-tvt17-drift motion-reduce:animate-none">
        <path d="M-100 420 C 200 180, 420 520, 760 300 S 1300 120, 1700 330 L 1700 420 C 1300 230, 1000 470, 760 420 S 260 330, -100 520Z" style="fill:var(--color-tvt17-au1)"/>
        <path d="M-50 300 C 260 120, 560 360, 900 180 S 1400 60, 1700 160 L 1700 250 C 1350 170, 1100 330, 880 300 S 300 250, -50 380Z" style="fill:var(--color-tvt17-au2)" opacity=".85"/>
      </g>
      <g class="origin-center animate-tvt17-drift2 motion-reduce:animate-none">
        <ellipse cx="1250" cy="380" rx="300" ry="120" style="fill:var(--color-tvt17-au3)" opacity=".8"/>
        <ellipse cx="300" cy="230" rx="260" ry="90" style="fill:var(--color-tvt17-au3)" opacity=".55"/>
      </g>
    </g>
    <path d="M0 720 L140 600 L230 650 L380 520 L520 640 L610 590 L760 700 L900 560 L1040 660 L1180 540 L1330 650 L1450 600 L1600 680 V1000 H0Z" style="fill:var(--color-tvt17-mtn1)"/>
    <path d="M0 780 L180 690 L330 740 L470 660 L640 760 L820 680 L980 770 L1150 690 L1300 760 L1460 700 L1600 750 V1000 H0Z" style="fill:var(--color-tvt17-mtn2)"/>
    <rect y="830" width="1600" height="170" fill="url(#tvt-17-lake)"/>
    <g opacity=".35" filter="url(#tvt-17-soft)"><ellipse cx="760" cy="900" rx="520" ry="40" style="fill:var(--color-tvt17-au1)"/><ellipse cx="1250" cy="920" rx="260" ry="26" style="fill:var(--color-tvt17-au3)"/></g>
    <g style="stroke:var(--color-tvt17-star)" stroke-width="2" stroke-linecap="round" opacity=".35"><path d="M300 870h120M520 905h80M900 880h160M1180 915h90"/></g>
  </svg>

  <div class="absolute inset-x-0 top-0 flex h-10 items-center gap-5 px-4 text-[13px] font-semibold bg-tvt17-solid supports-[backdrop-filter:blur(1px)]:bg-tvt17-glass supports-[backdrop-filter:blur(1px)]:backdrop-blur-2xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-[1.8] border border-tvt17-edge shadow-tvt17-glass border-x-0 border-t-0 shadow-none sm:px-6" aria-hidden="true">
    <span class="flex items-center gap-2 font-tvt17-display"><span class="size-3.5 rounded-full bg-linear-to-br from-tvt17-acc to-tvt17-acc2"></span>Aurora</span>
    <span class="max-sm:hidden">File</span><span class="max-sm:hidden">View</span><span class="max-sm:hidden">Window</span>
    <span class="ms-auto font-tvt17-mono text-[12px] tabular-nums">Wed 9:41</span>
  </div>

  <article class="@container/win group/win relative w-full max-w-[58rem] overflow-hidden rounded-[26px] bg-tvt17-solid supports-[backdrop-filter:blur(1px)]:bg-tvt17-glass supports-[backdrop-filter:blur(1px)]:backdrop-blur-2xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-[1.8] border border-tvt17-edge shadow-tvt17-glass starting:translate-y-4 starting:scale-[0.98] starting:opacity-0 transition-[opacity,translate,scale] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
    <div aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-[inherit] bg-linear-to-b from-tvt17-scrim to-transparent"></div>
    <header class="relative flex items-center gap-3 border-b border-tvt17-edge px-4 py-3 sm:px-5">
      <span aria-hidden="true" class="flex gap-1.5"><span class="size-3 rounded-full bg-[oklch(0.68_0.2_25)]"></span><span class="size-3 rounded-full bg-[oklch(0.82_0.16_85)]"></span><span class="size-3 rounded-full bg-[oklch(0.74_0.18_150)]"></span></span>
      <h2 class="flex-1 text-center font-tvt17-display text-[14px] font-semibold tracking-[-0.01em]">Aurora OS · <span class="text-tvt17-mut">Glass settings</span></h2>
      <span aria-hidden="true" class="w-[42px]"></span>
    </header>
    <div class="relative grid grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]/win:grid-cols-1">
      <div role="radiogroup" aria-label="Glass settings sections" class="flex flex-col gap-1 border-e border-tvt17-edge bg-tvt17-sel/30 p-3 @max-[40rem]/win:flex-row @max-[40rem]/win:gap-1.5 @max-[40rem]/win:overflow-x-auto @max-[40rem]/win:border-e-0 @max-[40rem]/win:border-b @max-[40rem]/win:[scrollbar-width:none]">
        <p class="px-2.5 pt-1 pb-2 font-tvt17-mono text-[10.5px] font-medium tracking-[0.18em] text-tvt17-mut uppercase @max-[40rem]/win:hidden">Display</p>

            <label class="group/tab relative flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-2.5 py-2 text-[14px] font-semibold text-tvt17-mut transition-[background-color,color,box-shadow] duration-200 select-none hover:bg-tvt17-sel/60 hover:text-tvt17-ink has-checked:bg-tvt17-sel has-checked:text-tvt17-ink has-checked:shadow-tvt17-chip has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt17-ring motion-reduce:transition-none @max-[40rem]/win:shrink-0 @max-[40rem]/win:pe-3.5">
              <input type="radio" name="tvt-17-tabs" id="tvt-17-t1" class="sr-only" checked>
              <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-[10px] bg-tvt17-sel ring-1 ring-tvt17-edge transition-colors duration-200 group-has-checked/tab:bg-linear-to-br group-has-checked/tab:from-tvt17-acc group-has-checked/tab:to-tvt17-acc2 group-has-checked/tab:text-tvt17-on group-has-checked/tab:ring-0"><svg viewBox="0 0 20 20" width="17" height="17" focusable="false"><path d="M10 2.8 17.5 6.6 10 10.4 2.5 6.6Z M2.5 10 10 13.8 17.5 10 M2.5 13.4 10 17.2 17.5 13.4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
              <span class="grid leading-tight"><span>Four layers</span><span class="text-[11.5px] font-medium text-tvt17-mut @max-[40rem]/win:hidden">Tint · frost · edge</span></span>
            </label>

            <label class="group/tab relative flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-2.5 py-2 text-[14px] font-semibold text-tvt17-mut transition-[background-color,color,box-shadow] duration-200 select-none hover:bg-tvt17-sel/60 hover:text-tvt17-ink has-checked:bg-tvt17-sel has-checked:text-tvt17-ink has-checked:shadow-tvt17-chip has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt17-ring motion-reduce:transition-none @max-[40rem]/win:shrink-0 @max-[40rem]/win:pe-3.5">
              <input type="radio" name="tvt-17-tabs" id="tvt-17-t2" class="sr-only">
              <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-[10px] bg-tvt17-sel ring-1 ring-tvt17-edge transition-colors duration-200 group-has-checked/tab:bg-linear-to-br group-has-checked/tab:from-tvt17-acc group-has-checked/tab:to-tvt17-acc2 group-has-checked/tab:text-tvt17-on group-has-checked/tab:ring-0"><svg viewBox="0 0 20 20" width="17" height="17" focusable="false"><circle cx="10" cy="10" r="7" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 3a7 7 0 0 1 0 14Z" fill="currentColor"/></svg></span>
              <span class="grid leading-tight"><span>Saturation</span><span class="text-[11.5px] font-medium text-tvt17-mut @max-[40rem]/win:hidden">Avoid grey plastic</span></span>
            </label>

            <label class="group/tab relative flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-2.5 py-2 text-[14px] font-semibold text-tvt17-mut transition-[background-color,color,box-shadow] duration-200 select-none hover:bg-tvt17-sel/60 hover:text-tvt17-ink has-checked:bg-tvt17-sel has-checked:text-tvt17-ink has-checked:shadow-tvt17-chip has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt17-ring motion-reduce:transition-none @max-[40rem]/win:shrink-0 @max-[40rem]/win:pe-3.5">
              <input type="radio" name="tvt-17-tabs" id="tvt-17-t3" class="sr-only">
              <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-[10px] bg-tvt17-sel ring-1 ring-tvt17-edge transition-colors duration-200 group-has-checked/tab:bg-linear-to-br group-has-checked/tab:from-tvt17-acc group-has-checked/tab:to-tvt17-acc2 group-has-checked/tab:text-tvt17-on group-has-checked/tab:ring-0"><svg viewBox="0 0 20 20" width="17" height="17" focusable="false"><path d="M1.8 10S4.8 4.5 10 4.5 18.2 10 18.2 10 15.2 15.5 10 15.5 1.8 10 1.8 10Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="10" cy="10" r="2.6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></span>
              <span class="grid leading-tight"><span>Legibility</span><span class="text-[11.5px] font-medium text-tvt17-mut @max-[40rem]/win:hidden">Contrast floor</span></span>
            </label>

            <label class="group/tab relative flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-2.5 py-2 text-[14px] font-semibold text-tvt17-mut transition-[background-color,color,box-shadow] duration-200 select-none hover:bg-tvt17-sel/60 hover:text-tvt17-ink has-checked:bg-tvt17-sel has-checked:text-tvt17-ink has-checked:shadow-tvt17-chip has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt17-ring motion-reduce:transition-none @max-[40rem]/win:shrink-0 @max-[40rem]/win:pe-3.5">
              <input type="radio" name="tvt-17-tabs" id="tvt-17-t4" class="sr-only">
              <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-[10px] bg-tvt17-sel ring-1 ring-tvt17-edge transition-colors duration-200 group-has-checked/tab:bg-linear-to-br group-has-checked/tab:from-tvt17-acc group-has-checked/tab:to-tvt17-acc2 group-has-checked/tab:text-tvt17-on group-has-checked/tab:ring-0"><svg viewBox="0 0 20 20" width="17" height="17" focusable="false"><path d="M11 2.5 4.5 11.2H10l-1 6.3 6.5-8.7H10Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
              <span class="grid leading-tight"><span>Performance</span><span class="text-[11.5px] font-medium text-tvt17-mut @max-[40rem]/win:hidden">Compositor cost</span></span>
            </label>
        <div class="mt-auto rounded-xl bg-tvt17-sel/60 p-3 ring-1 ring-tvt17-edge @max-[40rem]/win:hidden">
          <p class="text-[12px] font-semibold">backdrop-blur-2xl</p>
          <p class="mt-0.5 font-tvt17-mono text-[11px] text-tvt17-mut">blur(40px) saturate(1.8)</p>
        </div>
      </div>
      <div class="grid min-h-[23rem] p-6 sm:p-8">

            <article aria-labelledby="tvt-17-h1" class="invisible col-start-1 row-start-1 translate-y-2 opacity-0 transition-[opacity,translate,visibility] duration-400 ease-[cubic-bezier(.16,1,.3,1)] group-has-[#tvt-17-t1:checked]/win:visible group-has-[#tvt-17-t1:checked]/win:translate-y-0 group-has-[#tvt-17-t1:checked]/win:opacity-100 motion-reduce:transition-none">
              <p class="font-tvt17-mono text-[11px] font-medium tracking-[0.16em] text-tvt17-mut uppercase">Layer anatomy</p>
              <h3 id="tvt-17-h1" class="mt-1.5 font-tvt17-display text-[clamp(22px,2.8vw,28px)] leading-[1.1] font-semibold tracking-[-0.02em] text-balance">Tint, frost, edge, highlight</h3>
              <p class="mt-2.5 max-w-[50ch] text-[14.5px] leading-relaxed font-medium text-tvt17-mut text-pretty">Glass is four layers, not one blur. The 1px inset top highlight does more for the illusion than another ten pixels of blur ever will.</p>
              <ol class="mt-5 grid gap-2">
                <li class="flex items-center gap-3 rounded-xl bg-tvt17-sel/50 px-3 py-2.5 ring-1 ring-tvt17-edge"><span class="font-tvt17-mono text-[11px] text-tvt17-mut tabular-nums">01</span><span aria-hidden="true" class="size-5 shrink-0 rounded-md bg-tvt17-glass ring-1 ring-tvt17-edge"></span><span class="flex-1 text-[13.5px] font-semibold">Tint</span><code class="truncate font-tvt17-mono text-[11.5px] text-tvt17-mut max-[430px]:hidden">bg-white/40</code></li>
                <li class="flex items-center gap-3 rounded-xl bg-tvt17-sel/50 px-3 py-2.5 ring-1 ring-tvt17-edge"><span class="font-tvt17-mono text-[11px] text-tvt17-mut tabular-nums">02</span><span aria-hidden="true" class="size-5 shrink-0 rounded-md bg-linear-to-br from-tvt17-au2/60 to-tvt17-au1/60 blur-[2px]"></span><span class="flex-1 text-[13.5px] font-semibold">Frost</span><code class="truncate font-tvt17-mono text-[11.5px] text-tvt17-mut max-[430px]:hidden">backdrop-blur-2xl</code></li>
                <li class="flex items-center gap-3 rounded-xl bg-tvt17-sel/50 px-3 py-2.5 ring-1 ring-tvt17-edge"><span class="font-tvt17-mono text-[11px] text-tvt17-mut tabular-nums">03</span><span aria-hidden="true" class="size-5 shrink-0 rounded-md ring-2 ring-tvt17-edge"></span><span class="flex-1 text-[13.5px] font-semibold">Edge</span><code class="truncate font-tvt17-mono text-[11.5px] text-tvt17-mut max-[430px]:hidden">border-white/60</code></li>
                <li class="flex items-center gap-3 rounded-xl bg-tvt17-sel/50 px-3 py-2.5 ring-1 ring-tvt17-edge"><span class="font-tvt17-mono text-[11px] text-tvt17-mut tabular-nums">04</span><span aria-hidden="true" class="size-5 shrink-0 rounded-md bg-linear-to-b from-tvt17-hi to-transparent ring-1 ring-tvt17-edge"></span><span class="flex-1 text-[13.5px] font-semibold">Highlight</span><code class="truncate font-tvt17-mono text-[11.5px] text-tvt17-mut max-[430px]:hidden">inset-shadow-[0_1px_0]</code></li>
              </ol>
            </article>

            <article aria-labelledby="tvt-17-h2" class="invisible col-start-1 row-start-1 translate-y-2 opacity-0 transition-[opacity,translate,visibility] duration-400 ease-[cubic-bezier(.16,1,.3,1)] group-has-[#tvt-17-t2:checked]/win:visible group-has-[#tvt-17-t2:checked]/win:translate-y-0 group-has-[#tvt-17-t2:checked]/win:opacity-100 motion-reduce:transition-none">
              <p class="font-tvt17-mono text-[11px] font-medium tracking-[0.16em] text-tvt17-mut uppercase">Optics</p>
              <h3 id="tvt-17-h2" class="mt-1.5 font-tvt17-display text-[clamp(22px,2.8vw,28px)] leading-[1.1] font-semibold tracking-[-0.02em] text-balance">saturate(180%) or grey plastic</h3>
              <p class="mt-2.5 max-w-[50ch] text-[14.5px] leading-relaxed font-medium text-tvt17-mut text-pretty">Blurring averages colours together and drains them. Pushing saturation back up is how real frosted surfaces behave — compare the two live chips below.</p>
              <div class="relative mt-5 grid h-36 grid-cols-2 gap-3 overflow-hidden rounded-2xl bg-[repeating-linear-gradient(115deg,oklch(0.72_0.2_25)_0_18px,oklch(0.8_0.17_85)_18px_36px,oklch(0.7_0.17_160)_36px_54px,oklch(0.62_0.2_260)_54px_72px,oklch(0.6_0.24_320)_72px_90px)] p-3 ring-1 ring-tvt17-edge">
                <div class="grid place-content-center rounded-xl border border-white/50 bg-white/10 text-center text-white backdrop-blur-lg"><p class="text-[13px] font-bold [text-shadow:0_1px_2px_oklch(0_0_0/.5)]">blur only</p><p class="font-tvt17-mono text-[11px] [text-shadow:0_1px_2px_oklch(0_0_0/.5)]">backdrop-blur-lg</p></div>
                <div class="grid place-content-center rounded-xl border border-white/50 bg-white/10 text-center text-white backdrop-blur-lg backdrop-saturate-[1.8]"><p class="text-[13px] font-bold [text-shadow:0_1px_2px_oklch(0_0_0/.5)]">blur + saturate</p><p class="font-tvt17-mono text-[11px] [text-shadow:0_1px_2px_oklch(0_0_0/.5)]">backdrop-saturate-[1.8]</p></div>
              </div>
            </article>

            <article aria-labelledby="tvt-17-h3" class="invisible col-start-1 row-start-1 translate-y-2 opacity-0 transition-[opacity,translate,visibility] duration-400 ease-[cubic-bezier(.16,1,.3,1)] group-has-[#tvt-17-t3:checked]/win:visible group-has-[#tvt-17-t3:checked]/win:translate-y-0 group-has-[#tvt-17-t3:checked]/win:opacity-100 motion-reduce:transition-none">
              <p class="font-tvt17-mono text-[11px] font-medium tracking-[0.16em] text-tvt17-mut uppercase">Accessibility</p>
              <h3 id="tvt-17-h3" class="mt-1.5 font-tvt17-display text-[clamp(22px,2.8vw,28px)] leading-[1.1] font-semibold tracking-[-0.02em] text-balance">Test the worst image</h3>
              <p class="mt-2.5 max-w-[50ch] text-[14.5px] leading-relaxed font-medium text-tvt17-mut text-pretty">A translucent panel over an arbitrary photo can land anywhere from 1.2:1 to 12:1. A theme-biased tint plus a scrim keeps the floor safe — and body copy goes one weight heavier.</p>
              <ul class="mt-5 grid gap-3.5">
                <li><p class="flex items-baseline justify-between gap-3 text-[13px] font-semibold"><span>Bare glass over a bright photo</span><span class="font-tvt17-mono text-[12px] tabular-nums">1.9:1 <span class="text-[oklch(0.6_0.2_25)]">fail</span></span></p><div class="mt-1.5 h-2 overflow-hidden rounded-full bg-tvt17-sel ring-1 ring-tvt17-edge"><div class="h-full rounded-full bg-linear-to-r from-tvt17-acc to-tvt17-acc2 w-[16%]"></div></div></li>
                <li><p class="flex items-baseline justify-between gap-3 text-[13px] font-semibold"><span>+ biased tint</span><span class="font-tvt17-mono text-[12px] tabular-nums">4.6:1 <span class="text-tvt17-mut">AA</span></span></p><div class="mt-1.5 h-2 overflow-hidden rounded-full bg-tvt17-sel ring-1 ring-tvt17-edge"><div class="h-full rounded-full bg-linear-to-r from-tvt17-acc to-tvt17-acc2 w-[48%]"></div></div></li>
                <li><p class="flex items-baseline justify-between gap-3 text-[13px] font-semibold"><span>+ tint + gradient scrim</span><span class="font-tvt17-mono text-[12px] tabular-nums">8.1:1 <span class="text-tvt17-mut">AAA</span></span></p><div class="mt-1.5 h-2 overflow-hidden rounded-full bg-tvt17-sel ring-1 ring-tvt17-edge"><div class="h-full rounded-full bg-linear-to-r from-tvt17-acc to-tvt17-acc2 w-[84%]"></div></div></li>
              </ul>
            </article>

            <article aria-labelledby="tvt-17-h4" class="invisible col-start-1 row-start-1 translate-y-2 opacity-0 transition-[opacity,translate,visibility] duration-400 ease-[cubic-bezier(.16,1,.3,1)] group-has-[#tvt-17-t4:checked]/win:visible group-has-[#tvt-17-t4:checked]/win:translate-y-0 group-has-[#tvt-17-t4:checked]/win:opacity-100 motion-reduce:transition-none">
              <p class="font-tvt17-mono text-[11px] font-medium tracking-[0.16em] text-tvt17-mut uppercase">Rendering</p>
              <h3 id="tvt-17-h4" class="mt-1.5 font-tvt17-display text-[clamp(22px,2.8vw,28px)] leading-[1.1] font-semibold tracking-[-0.02em] text-balance">Few and large</h3>
              <p class="mt-2.5 max-w-[50ch] text-[14.5px] leading-relaxed font-medium text-tvt17-mut text-pretty">Every glass surface re-blurs whatever moves behind it. Keep them few, keep them big, and never animate the blur radius — animate opacity and transform instead.</p>
              <dl class="mt-5 grid grid-cols-3 gap-2.5">
                <div class="rounded-2xl bg-tvt17-sel/50 p-3.5 ring-1 ring-tvt17-edge"><dt class="text-[12px] font-semibold text-tvt17-mut">Glass layers</dt><dd class="mt-1 font-tvt17-display text-[26px] font-semibold tabular-nums">2</dd></div>
                <div class="rounded-2xl bg-tvt17-sel/50 p-3.5 ring-1 ring-tvt17-edge"><dt class="text-[12px] font-semibold text-tvt17-mut">Animated blur</dt><dd class="mt-1 font-tvt17-display text-[26px] font-semibold tabular-nums">0</dd></div>
                <div class="rounded-2xl bg-tvt17-sel/50 p-3.5 ring-1 ring-tvt17-edge"><dt class="text-[12px] font-semibold text-tvt17-mut">Frame time</dt><dd class="mt-1 font-tvt17-display text-[26px] font-semibold tabular-nums">9.2<span class="text-[13px] text-tvt17-mut">ms</span></dd></div>
              </dl>
              <div class="mt-3 rounded-2xl bg-tvt17-sel/50 p-3.5 ring-1 ring-tvt17-edge"><p class="flex justify-between text-[12.5px] font-semibold"><span>16.7 ms frame budget</span><span class="text-tvt17-mut tabular-nums">55% used</span></p><div class="mt-2 h-2 rounded-full bg-tvt17-sel"><div class="h-full w-[55%] rounded-full bg-linear-to-r from-tvt17-acc to-tvt17-acc2"></div></div></div>
            </article>
      </div>
    </div>
  </article>
  <p aria-hidden="true" class="absolute inset-x-4 bottom-4 mx-auto w-fit max-w-[calc(100%-2rem)] rounded-full px-3.5 text-center max-sm:hidden py-1.5 font-tvt17-mono text-[11px] text-tvt17-ink bg-tvt17-solid supports-[backdrop-filter:blur(1px)]:bg-tvt17-glass supports-[backdrop-filter:blur(1px)]:backdrop-blur-2xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-[1.8] border border-tvt17-edge shadow-tvt17-glass shadow-none">supports-[backdrop-filter]: · has-checked: · group-has-[…]/win:</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt17-sky1: #9da3ef;
  --color-tvt17-sky1: oklch(0.74 0.11 280);
  --color-tvt17-sky2: #f0bfea;
  --color-tvt17-sky2: oklch(0.86 0.08 330);
  --color-tvt17-sky3: #ffe2cb;
  --color-tvt17-sky3: oklch(0.93 0.07 60);
  --color-tvt17-au1: #54e8bd;
  --color-tvt17-au1: oklch(0.84 0.14 170);
  --color-tvt17-au2: #cb89fa;
  --color-tvt17-au2: oklch(0.74 0.17 310);
  --color-tvt17-au3: #40d1f7;
  --color-tvt17-au3: oklch(0.8 0.13 220);
  --color-tvt17-mtn1: #857db9;
  --color-tvt17-mtn1: oklch(0.62 0.09 290);
  --color-tvt17-mtn2: #5f5c8f;
  --color-tvt17-mtn2: oklch(0.5 0.08 285);
  --color-tvt17-lake: #8e9ad7;
  --color-tvt17-lake: oklch(0.7 0.09 275);
  --color-tvt17-star: #ffffff00;
  --color-tvt17-star: oklch(1 0 0 / 0);
  --color-tvt17-glass: #fcfbff80;
  --color-tvt17-glass: oklch(0.99 0.01 300 / 0.5);
  --color-tvt17-solid: #f5f4fd;
  --color-tvt17-solid: oklch(0.97 0.012 290);
  --color-tvt17-edge: #ffffffa6;
  --color-tvt17-edge: oklch(1 0 0 / 0.65);
  --color-tvt17-hi: #ffffffe6;
  --color-tvt17-hi: oklch(1 0 0 / 0.9);
  --color-tvt17-sel: #ffffff9e;
  --color-tvt17-sel: oklch(1 0 0 / 0.62);
  --color-tvt17-scrim: #ffffff4d;
  --color-tvt17-scrim: oklch(1 0 0 / 0.3);
  --color-tvt17-ink: #16142e;
  --color-tvt17-ink: oklch(0.21 0.05 285);
  --color-tvt17-mut: #454462;
  --color-tvt17-mut: oklch(0.4 0.05 285);
  --color-tvt17-acc: #8038d1;
  --color-tvt17-acc: oklch(0.52 0.22 300);
  --color-tvt17-acc2: #007e9a;
  --color-tvt17-acc2: oklch(0.55 0.14 220);
  --color-tvt17-on: #ffffff;
  --color-tvt17-on: oklch(1 0 0);
  --color-tvt17-ring: #7235d0;
  --color-tvt17-ring: oklch(0.5 0.22 295);
  --font-tvt17-display: 'Sora', system-ui, sans-serif;
  --font-tvt17-sans: 'Manrope', system-ui, sans-serif;
  --font-tvt17-mono: 'Fira Code', ui-monospace, monospace;
  --shadow-tvt17-glass: inset 0 1px 0 var(--color-tvt17-hi), 0 30px 80px -30px oklch(0.15 0.06 280 / 0.55), 0 2px 6px oklch(0.15 0.06 280 / 0.12);
  --shadow-tvt17-chip: inset 0 1px 0 var(--color-tvt17-hi), 0 6px 18px -8px oklch(0.2 0.08 290 / 0.45);
  --animate-tvt17-drift: tvt17-drift 22s ease-in-out infinite alternate;
  --animate-tvt17-drift2: tvt17-drift2 28s ease-in-out infinite alternate;

  @keyframes tvt17-drift {
    to {
      transform: translate(-60px, 30px) scale(1.06);
    }
  }

  @keyframes tvt17-drift2 {
    to {
      transform: translate(70px, -25px);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-17 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-17:not([data-theme="light"]) {
    --color-tvt17-sky1: #050719;
    --color-tvt17-sky1: oklch(0.14 0.04 275);
    --color-tvt17-sky2: #140f34;
    --color-tvt17-sky2: oklch(0.2 0.07 285);
    --color-tvt17-sky3: #002945;
    --color-tvt17-sky3: oklch(0.27 0.08 245);
    --color-tvt17-au1: #00d18a;
    --color-tvt17-au1: oklch(0.76 0.2 160);
    --color-tvt17-au2: #9d40e8;
    --color-tvt17-au2: oklch(0.58 0.24 305);
    --color-tvt17-au3: #00abc0;
    --color-tvt17-au3: oklch(0.68 0.16 210);
    --color-tvt17-mtn1: #11172b;
    --color-tvt17-mtn1: oklch(0.21 0.04 270);
    --color-tvt17-mtn2: #070a18;
    --color-tvt17-mtn2: oklch(0.15 0.03 270);
    --color-tvt17-lake: #08152c;
    --color-tvt17-lake: oklch(0.2 0.05 260);
    --color-tvt17-star: #ffffffd9;
    --color-tvt17-star: oklch(1 0 0 / 0.85);
    --color-tvt17-glass: #0e0f2380;
    --color-tvt17-glass: oklch(0.18 0.04 280 / 0.5);
    --color-tvt17-solid: #131428;
    --color-tvt17-solid: oklch(0.2 0.04 280);
    --color-tvt17-edge: #ffffff29;
    --color-tvt17-edge: oklch(1 0 0 / 0.16);
    --color-tvt17-hi: #ffffff42;
    --color-tvt17-hi: oklch(1 0 0 / 0.26);
    --color-tvt17-sel: #ffffff1a;
    --color-tvt17-sel: oklch(1 0 0 / 0.1);
    --color-tvt17-scrim: #0404114d;
    --color-tvt17-scrim: oklch(0.12 0.03 280 / 0.3);
    --color-tvt17-ink: #f3f4fc;
    --color-tvt17-ink: oklch(0.97 0.01 280);
    --color-tvt17-mut: #c6c9de;
    --color-tvt17-mut: oklch(0.84 0.03 280);
    --color-tvt17-acc: #37e4aa;
    --color-tvt17-acc: oklch(0.82 0.16 165);
    --color-tvt17-acc2: #c09aff;
    --color-tvt17-acc2: oklch(0.76 0.16 300);
    --color-tvt17-on: #0e0f23;
    --color-tvt17-on: oklch(0.18 0.04 280);
    --color-tvt17-ring: #64eab7;
    --color-tvt17-ring: oklch(0.85 0.14 165);
  }
}

.tvt-17[data-theme="dark"] {
  --color-tvt17-sky1: #050719;
  --color-tvt17-sky1: oklch(0.14 0.04 275);
  --color-tvt17-sky2: #140f34;
  --color-tvt17-sky2: oklch(0.2 0.07 285);
  --color-tvt17-sky3: #002945;
  --color-tvt17-sky3: oklch(0.27 0.08 245);
  --color-tvt17-au1: #00d18a;
  --color-tvt17-au1: oklch(0.76 0.2 160);
  --color-tvt17-au2: #9d40e8;
  --color-tvt17-au2: oklch(0.58 0.24 305);
  --color-tvt17-au3: #00abc0;
  --color-tvt17-au3: oklch(0.68 0.16 210);
  --color-tvt17-mtn1: #11172b;
  --color-tvt17-mtn1: oklch(0.21 0.04 270);
  --color-tvt17-mtn2: #070a18;
  --color-tvt17-mtn2: oklch(0.15 0.03 270);
  --color-tvt17-lake: #08152c;
  --color-tvt17-lake: oklch(0.2 0.05 260);
  --color-tvt17-star: #ffffffd9;
  --color-tvt17-star: oklch(1 0 0 / 0.85);
  --color-tvt17-glass: #0e0f2380;
  --color-tvt17-glass: oklch(0.18 0.04 280 / 0.5);
  --color-tvt17-solid: #131428;
  --color-tvt17-solid: oklch(0.2 0.04 280);
  --color-tvt17-edge: #ffffff29;
  --color-tvt17-edge: oklch(1 0 0 / 0.16);
  --color-tvt17-hi: #ffffff42;
  --color-tvt17-hi: oklch(1 0 0 / 0.26);
  --color-tvt17-sel: #ffffff1a;
  --color-tvt17-sel: oklch(1 0 0 / 0.1);
  --color-tvt17-scrim: #0404114d;
  --color-tvt17-scrim: oklch(0.12 0.03 280 / 0.3);
  --color-tvt17-ink: #f3f4fc;
  --color-tvt17-ink: oklch(0.97 0.01 280);
  --color-tvt17-mut: #c6c9de;
  --color-tvt17-mut: oklch(0.84 0.03 280);
  --color-tvt17-acc: #37e4aa;
  --color-tvt17-acc: oklch(0.82 0.16 165);
  --color-tvt17-acc2: #c09aff;
  --color-tvt17-acc2: oklch(0.76 0.16 300);
  --color-tvt17-on: #0e0f23;
  --color-tvt17-on: oklch(0.18 0.04 280);
  --color-tvt17-ring: #64eab7;
  --color-tvt17-ring: oklch(0.85 0.14 165);
}
```
