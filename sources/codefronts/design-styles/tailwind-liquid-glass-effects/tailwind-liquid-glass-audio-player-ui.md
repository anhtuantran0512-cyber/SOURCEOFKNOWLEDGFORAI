---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-audio-player-ui/"
title: "Tailwind Liquid Glass Audio Player UI"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "The floating playbar: a compact glass card over a blown-up, heavily blurred copy of the album art it is playing."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Audio Player UI
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-audio-player-ui/

The floating playbar: a compact glass card over a blown-up, heavily blurred copy of the album art it is playing. Progress is a custom property the script updates, so a ticking transport never touches a class &mdash; and the vendor slider-thumb rules, which have no utility, stay in CSS where they are honest.
## HTML
```html
<section id="lgt-12-root" class="lgt-12 grid w-full min-h-svh place-items-center bg-lgt12-bg p-15 font-lgt12-sans" style="--art:url('https://picsum.photos/seed/lgaudio1/400/400');--p:30" aria-label="Tailwind liquid glass audio player">
  <div class="relative isolate flex w-[min(440px,94vw)] items-center gap-4.5 overflow-hidden rounded-[26px] border border-white/28 bg-white/8 p-4.5 backdrop-blur-[20px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_30px_60px_-30px_rgba(0,0,0,.7)] before:absolute before:-inset-[40%] before:-z-1 before:scale-120 before:[background:var(--art)_center/cover] before:[filter:blur(40px)_saturate(160%)_brightness(.7)]">
    <div aria-hidden="true" class="size-21 flex-none rounded-[16px] [background:var(--art)_center/cover] shadow-[0_10px_24px_-10px_rgba(0,0,0,.7),inset_0_0_0_1px_rgba(255,255,255,.25)]"></div>

    <div class="min-w-0 flex-1">
      <p id="lgt-12-track" aria-live="polite" class="mb-2.5 truncate text-[15px] font-extrabold text-white">Neon Tide &mdash; Aurora</p>
      <input id="lgt-12-seek" type="range" min="0" max="100" value="30" aria-label="Seek" class="lgt-12-seek h-1.5 w-full cursor-pointer appearance-none rounded-full outline-none [background:linear-gradient(90deg,#fff_calc(var(--p,30)*1%),rgb(255_255_255/0.25)_0)] focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-white">
      <div class="mt-1.5 mb-3 flex justify-between text-[11px] tabular-nums text-white/70"><span id="lgt-12-cur">1:04</span><span>3:32</span></div>
      <div class="flex items-center justify-center gap-3.5">
        <button id="lgt-12-prev" type="button" aria-label="Previous track" class="grid size-10 cursor-pointer place-items-center rounded-full border border-white/30 bg-white/14 text-[15px] text-white backdrop-blur-[8px] transition-[transform,background-color] duration-200 hover:scale-108 hover:bg-white/24 focus-visible:scale-108 active:scale-94 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-colors">&#9198;</button>
        <button id="lgt-12-play" type="button" aria-label="Play" aria-pressed="false" class="grid size-13 cursor-pointer place-items-center rounded-full border border-lgt12-accent/60 bg-lgt12-accent text-[18px] text-white transition-[transform,filter] duration-200 hover:scale-108 hover:brightness-110 focus-visible:scale-108 active:scale-94 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">&#9654;</button>
        <button id="lgt-12-next" type="button" aria-label="Next track" class="grid size-10 cursor-pointer place-items-center rounded-full border border-white/30 bg-white/14 text-[15px] text-white backdrop-blur-[8px] transition-[transform,background-color] duration-200 hover:scale-108 hover:bg-white/24 focus-visible:scale-108 active:scale-94 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-colors">&#9197;</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt12-bg: #0c0a16;
  --color-lgt12-accent: #a06ef0;
  --color-lgt12-accent: oklch(0.68 0.18 300);
  --font-lgt12-sans: 'Manrope', system-ui, sans-serif;
}
/* Vendor range thumbs: they need -webkit-appearance before they accept any styling,
   they cannot share a rule, and there is no utility for either. This is where CSS stays. */

.lgt-12-seek::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgb(0 0 0 / 0.5), 0 0 0 4px color-mix(in oklab, var(--color-lgt12-accent) 60%, transparent);
}

.lgt-12-seek::-moz-range-thumb {
  width: 15px;
  height: 15px;
  border: none;
  border-radius: 50%;
  background: #fff;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lgt-12-root');
  const play = root.querySelector('#lgt-12-play');
  const seek = root.querySelector('#lgt-12-seek');
  const cur = root.querySelector('#lgt-12-cur');
  const trackEl = root.querySelector('#lgt-12-track');
  const tracks = [
    { t: 'Neon Tide — Aurora', art: "url('https://picsum.photos/seed/lgaudio1/400/400')", a: 'oklch(0.68 0.18 300)' },
    { t: 'Slow Static — Kioto', art: "url('https://picsum.photos/seed/lgaudio2/400/400')", a: 'oklch(0.7 0.17 200)' },
    { t: 'Amber Room — Vell', art: "url('https://picsum.photos/seed/lgaudio3/400/400')", a: 'oklch(0.72 0.17 60)' }
  ];
  let i = 0, playing = false, p = 30, timer = null;
  const DUR = 212;
  const fmt = s => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');

  const paint = () => {
    root.style.setProperty('--p', p);
    seek.value = p;
    cur.textContent = fmt(p / 100 * DUR);
  };
  const tick = () => { p = Math.min(100, p + 100 / DUR); paint(); if (p >= 100) next(); };
  const toggle = () => {
    playing = !playing;
    play.textContent = playing ? '❚❚' : '▶';
    play.setAttribute('aria-label', playing ? 'Pause' : 'Play');
    play.setAttribute('aria-pressed', String(playing));
    clearInterval(timer);
    if (playing) timer = setInterval(tick, 1000);
  };
  const load = () => {
    const tk = tracks[i];
    trackEl.textContent = tk.t;
    root.style.setProperty('--art', tk.art);
    root.style.setProperty('--color-lgt12-accent', tk.a);
    p = 0; paint();
  };
  const next = () => { i = (i + 1) % tracks.length; load(); };
  const prev = () => { i = (i - 1 + tracks.length) % tracks.length; load(); };

  play.addEventListener('click', toggle);
  root.querySelector('#lgt-12-next').addEventListener('click', next);
  root.querySelector('#lgt-12-prev').addEventListener('click', prev);
  seek.addEventListener('input', () => { p = +seek.value; paint(); });
  paint();
})();
```
