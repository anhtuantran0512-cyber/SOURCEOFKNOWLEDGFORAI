---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-nineties-web-guestbook-widget/"
title: "Tailwind Nineties Web Guestbook Widget"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A personal-homepage guestbook: odometer hit counter, webring navigation, signed entries and a &ldquo;best viewed in&rdquo; badge, on the grey ground and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Nineties Web Guestbook Widget
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-nineties-web-guestbook-widget/

A personal-homepage guestbook: odometer hit counter, webring navigation, signed entries and a &ldquo;best viewed in&rdquo; badge, on the grey ground and ridged borders of the era. The point it makes is the one that matters most about this period &mdash; reproduce the look, never the markup, because everything that made these pages work is now the reason they fail.
## HTML
```html
<section class="twr-17 relative block w-full min-h-svh box-border bg-twr17-face text-twr17-ink font-twr17-sans [background-image:repeating-conic-gradient(var(--color-twr17-tileb)_0%_25%,var(--color-twr17-face)_0%_50%)] [background-size:8px_8px]" aria-labelledby="twr-17-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-17-title">Nineties personal homepage guestbook</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-17-theme">
    <label class="grid place-items-center size-11 cursor-pointer bg-twr17-face2 text-twr17-ink2 twr17-ridge peer-focus-visible:outline-2 peer-focus-visible:outline-twr17-acc peer-focus-visible:outline-offset-2" for="twr-17-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark ground</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-5 max-w-[64rem] mx-auto px-[clamp(0.75rem,0.5rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <header class="min-w-0 grid justify-items-center gap-1.5 text-center bg-twr17-face2 px-4 py-5 twr17-ridge">
      <h3 class="m-0 min-w-0 font-twr17-serif font-bold text-[clamp(1.5rem,1.1rem+2.4vw,2.6rem)] text-twr17-acc [text-shadow:1px_1px_0_var(--color-twr17-hi)]">Dave&rsquo;s Homepage</h3>
      <p class="m-0 font-twr17-mono text-[0.75rem] text-twr17-hot">~ under construction since 1997 ~</p>
    </header>

    <div class="grid grid-cols-[minmax(0,1fr)] gap-5 lg:grid-cols-[minmax(0,1.6fr)_minmax(0,1fr)] lg:items-start">
      <article class="min-w-0 grid content-start gap-3 bg-twr17-face2 p-[clamp(0.85rem,0.6rem+1vw,1.25rem)] twr17-ridge" aria-labelledby="twr-17-gb">
        <h4 class="m-0 font-twr17-serif text-[1rem] font-bold text-twr17-acc" id="twr-17-gb">Sign my guestbook</h4>
        <ol class="list-none m-0 p-0 grid gap-3 min-w-0">
          <li class="flex gap-3 min-w-0 border-b border-twr17-sh/40 pb-3 last:border-b-0 last:pb-0">
            <span class="flex-none grid place-items-center size-10 bg-twr17-acc text-white font-twr17-sans text-[0.75rem] font-bold twr17-ridge" aria-hidden="true">AC</span>
            <div class="min-w-0 grid gap-1">
              <p class="m-0 min-w-0 font-twr17-sans text-[0.72rem] text-twr17-ink2"><b class="font-bold text-twr17-ink">Alex Chen</b> &middot; 14 Nov 1997 &middot; Manchester</p>
              <p class="m-0 min-w-0 font-twr17-serif text-[0.92rem] leading-normal text-pretty">Great page! Love the MIDI. Come see my Star Trek shrine sometime.</p>
            </div>
          </li>
          <li class="flex gap-3 min-w-0 border-b border-twr17-sh/40 pb-3 last:border-b-0 last:pb-0">
            <span class="flex-none grid place-items-center size-10 bg-twr17-acc text-white font-twr17-sans text-[0.75rem] font-bold twr17-ridge" aria-hidden="true">PS</span>
            <div class="min-w-0 grid gap-1">
              <p class="m-0 min-w-0 font-twr17-sans text-[0.72rem] text-twr17-ink2"><b class="font-bold text-twr17-ink">Priya Sharma</b> &middot; 2 Dec 1997 &middot; Leeds</p>
              <p class="m-0 min-w-0 font-twr17-serif text-[0.92rem] leading-normal text-pretty">Added you to the ring. The tiled background is a bold choice and I respect it.</p>
            </div>
          </li>
          <li class="flex gap-3 min-w-0 border-b border-twr17-sh/40 pb-3 last:border-b-0 last:pb-0">
            <span class="flex-none grid place-items-center size-10 bg-twr17-acc text-white font-twr17-sans text-[0.75rem] font-bold twr17-ridge" aria-hidden="true">JL</span>
            <div class="min-w-0 grid gap-1">
              <p class="m-0 min-w-0 font-twr17-sans text-[0.72rem] text-twr17-ink2"><b class="font-bold text-twr17-ink">Jordan Lee</b> &middot; 19 Jan 1998 &middot; Bristol</p>
              <p class="m-0 min-w-0 font-twr17-serif text-[0.92rem] leading-normal text-pretty">Your links page is the best on the web. Signed, a fellow traveller.</p>
            </div>
          </li>
        </ol>
        <p class="m-0 min-w-0 text-[0.75rem] leading-relaxed text-pretty text-twr17-ink2">Entries are a real ordered list. No table, no spacer image, no <code class="font-twr17-mono bg-twr17-face px-1">&lt;font&gt;</code> anywhere in this widget.</p>
      </article>

      <aside class="min-w-0 grid content-start gap-5">
        <div class="min-w-0 grid content-start gap-3 bg-twr17-face2 p-[clamp(0.85rem,0.6rem+1vw,1.25rem)] twr17-ridge">
          <h4 class="m-0 font-twr17-serif text-[1rem] font-bold text-twr17-acc">Visitors</h4>
          <div class="flex gap-1 min-w-0" role="img" aria-label="Visitor count: 0 0 4 2 1 8 7">
            <span class="grid place-items-center w-6 h-9 bg-[#111] text-[#7dff9a] font-twr17-mono text-[1.05rem] tabular-nums [box-shadow:inset_0_2px_4px_rgba(0,0,0,0.9)]">0</span><span class="grid place-items-center w-6 h-9 bg-[#111] text-[#7dff9a] font-twr17-mono text-[1.05rem] tabular-nums [box-shadow:inset_0_2px_4px_rgba(0,0,0,0.9)]">0</span><span class="grid place-items-center w-6 h-9 bg-[#111] text-[#7dff9a] font-twr17-mono text-[1.05rem] tabular-nums [box-shadow:inset_0_2px_4px_rgba(0,0,0,0.9)]">4</span><span class="grid place-items-center w-6 h-9 bg-[#111] text-[#7dff9a] font-twr17-mono text-[1.05rem] tabular-nums [box-shadow:inset_0_2px_4px_rgba(0,0,0,0.9)]">2</span><span class="grid place-items-center w-6 h-9 bg-[#111] text-[#7dff9a] font-twr17-mono text-[1.05rem] tabular-nums [box-shadow:inset_0_2px_4px_rgba(0,0,0,0.9)]">1</span><span class="grid place-items-center w-6 h-9 bg-[#111] text-[#7dff9a] font-twr17-mono text-[1.05rem] tabular-nums [box-shadow:inset_0_2px_4px_rgba(0,0,0,0.9)]">8</span><span class="grid place-items-center w-6 h-9 bg-[#111] text-[#7dff9a] font-twr17-mono text-[1.05rem] tabular-nums [box-shadow:inset_0_2px_4px_rgba(0,0,0,0.9)]">7</span>
          </div>
          <p class="m-0 text-[0.72rem] text-twr17-ink2">since 12 August 1997</p>
        </div>

        <nav class="min-w-0 grid content-start gap-3 bg-twr17-face2 p-[clamp(0.85rem,0.6rem+1vw,1.25rem)] twr17-ridge" aria-labelledby="twr-17-ring">
          <h4 class="m-0 font-twr17-serif text-[1rem] font-bold text-twr17-acc" id="twr-17-ring">The Retro Web Ring</h4>
          <ul class="list-none m-0 p-0 grid gap-2 min-w-0 sm:grid-cols-2">
            <li><button class="w-full min-h-11 px-3 py-2 border-0 cursor-pointer font-twr17-sans text-[0.8rem] bg-twr17-face text-twr17-ink twr17-ridge active:twr17-ridge-in focus-visible:outline-2 focus-visible:outline-twr17-acc focus-visible:outline-offset-2" type="button">&#171; Prev</button></li>
            <li><button class="w-full min-h-11 px-3 py-2 border-0 cursor-pointer font-twr17-sans text-[0.8rem] bg-twr17-face text-twr17-ink twr17-ridge active:twr17-ridge-in focus-visible:outline-2 focus-visible:outline-twr17-acc focus-visible:outline-offset-2" type="button">Random</button></li>
            <li><button class="w-full min-h-11 px-3 py-2 border-0 cursor-pointer font-twr17-sans text-[0.8rem] bg-twr17-face text-twr17-ink twr17-ridge active:twr17-ridge-in focus-visible:outline-2 focus-visible:outline-twr17-acc focus-visible:outline-offset-2" type="button">List</button></li>
            <li><button class="w-full min-h-11 px-3 py-2 border-0 cursor-pointer font-twr17-sans text-[0.8rem] bg-twr17-face text-twr17-ink twr17-ridge active:twr17-ridge-in focus-visible:outline-2 focus-visible:outline-twr17-acc focus-visible:outline-offset-2" type="button">Next &#187;</button></li>
          </ul>
        </nav>

        <div class="min-w-0 grid content-start gap-3 bg-twr17-face2 p-[clamp(0.85rem,0.6rem+1vw,1.25rem)] twr17-ridge">
          <h4 class="m-0 font-twr17-serif text-[1rem] font-bold text-twr17-acc">Best viewed in</h4>
          <p class="m-0 justify-self-start px-3 py-2 bg-twr17-hot text-white font-twr17-mono text-[0.72rem] tracking-[0.08em] animate-twr17-pulse motion-reduce:animate-none">800 &times; 600 &middot; 256 colours</p>
          <p class="m-0 min-w-0 text-[0.72rem] leading-relaxed text-pretty text-twr17-ink2">The badge pulses on a two second cycle and stops under reduced motion. The era flashed it; that is the one thing not worth reproducing.</p>
        </div>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr17-face: #c8c8c8;
  --color-twr17-face2: #dcdcdc;
  --color-twr17-tileb: #bdbdbd;
  --color-twr17-hi: #ffffff;
  --color-twr17-sh: #7a7a7a;
  --color-twr17-ink: #16161a;
  --color-twr17-ink: oklch(0.20 0.006 280);
  --color-twr17-ink2: #4a4a52;
  --color-twr17-ink2: oklch(0.42 0.01 280);
  --color-twr17-acc: #0f3fa8;
  --color-twr17-acc: oklch(0.42 0.19 262);
  --color-twr17-hot: #a01414;
  --color-twr17-hot: oklch(0.43 0.18 27);
  --font-twr17-serif: Georgia, ui-serif, 'Times New Roman', Times, serif;
  --font-twr17-sans: Verdana, ui-sans-serif, Geneva, 'Trebuchet MS', system-ui, sans-serif;
  --font-twr17-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --animate-twr17-pulse: twr-17-pulse 2s ease-in-out infinite;
}
/* border-style: ridge derives its tones from border-color by an unspecified
   rule, so it differs per engine and occupies layout space. Four insets do not. */

@utility twr17-ridge {
  box-shadow: inset 2px 2px 0 0 var(--color-twr17-hi), inset -2px -2px 0 0 var(--color-twr17-sh), inset 4px 4px 0 0 var(--color-twr17-sh), inset -4px -4px 0 0 var(--color-twr17-hi);
}

@utility twr17-ridge-in {
  box-shadow: inset 2px 2px 0 0 var(--color-twr17-sh), inset -2px -2px 0 0 var(--color-twr17-hi), inset 4px 4px 0 0 var(--color-twr17-hi), inset -4px -4px 0 0 var(--color-twr17-sh);
}
/* A pulse, not a blink: 2s period, and it stops entirely under motion-reduce. */

@keyframes twr-17-pulse {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 0 rgba(160, 20, 20, 0);
  }

  50% {
    transform: scale(1.03);
    box-shadow: 0 0 12px rgba(160, 20, 20, 0.55);
  }
}

.twr-17:has(#twr-17-theme:checked) {
  --color-twr17-face: #2a2a2e;
  --color-twr17-face2: #35353a;
  --color-twr17-tileb: #303034;
  --color-twr17-hi: #55555c;
  --color-twr17-sh: #17171a;
  --color-twr17-ink: #eeeef2;
  --color-twr17-ink: oklch(0.95 0.004 280);
  --color-twr17-ink2: #b0b0b8;
  --color-twr17-ink2: oklch(0.76 0.008 280);
  --color-twr17-acc: #8fb4ff;
  --color-twr17-acc: oklch(0.79 0.12 262);
  --color-twr17-hot: #ff8f8f;
  --color-twr17-hot: oklch(0.78 0.14 27);
}
```
