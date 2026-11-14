---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-restaurant-table-reservation-form/"
title: "Tailwind Restaurant Table Reservation Form"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's fine-dining booking widget, ported one-for-one to Tailwind v4: candle-lit black and gold, a party-size stepper, a horizontally scrolling…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Restaurant Table Reservation Form
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-restaurant-table-reservation-form/

The CSS collection's fine-dining booking widget, ported one-for-one to Tailwind v4: candle-lit black and gold, a party-size stepper, a horizontally scrolling date strip of radios with snap-x snap-mandatory, a time grid where fully booked slots are genuinely disabled and struck through, seating cards with photography that wake from greyscale when chosen, an occasion selector, and a live sentence summary — “Table for 4 · Fri 9 Oct · 8:00 pm · Terrace”.
## HTML
```html
<div class="tf-10 relative block min-h-svh w-full [background:var(--tf10-wash),var(--color-tf10-bg)] pt-[72px] font-tf10-sans leading-[normal] text-tf10-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="w-full max-w-[40rem] overflow-hidden rounded-3xl border border-tf10-line bg-tf10-card shadow-[0_40px_90px_-40px_rgba(0,0,0,.9),0_0_0_1px_color-mix(in_oklab,var(--color-tf10-gold)_12%,transparent)]">
      <figure class="relative h-48 bg-[#2a1e10] after:absolute after:inset-0 after:bg-[linear-gradient(transparent_20%,var(--color-tf10-card))] after:content-['']">
        <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1000&h=500&fit=crop&auto=format&q=70" width="1000" height="500" alt="Warmly lit restaurant dining room with set tables" loading="lazy" decoding="async" class="block size-full object-cover contrast-105 saturate-90">
        <figcaption class="absolute bottom-2 left-[clamp(1.25rem,5vw,2.25rem)] z-1 grid"><span class="font-tf10-serif text-[clamp(2rem,6vw,2.75rem)] leading-none font-medium tracking-[.01em] text-tf10-gold-2">Maison Ardent</span><small class="mt-[.3rem] text-[.75rem] tracking-[.22em] text-tf10-muted uppercase">Modern French · Mayfair, London</small></figcaption>
      </figure>
      <div class="grid gap-[1.4rem] px-[clamp(1.25rem,5vw,2.25rem)] pt-5 pb-[clamp(1.25rem,5vw,2.25rem)]" role="form" aria-labelledby="tf-10-title">
        <h2 id="tf-10-title" class="font-tf10-serif text-[1.5rem] font-medium text-tf10-muted italic">Reserve a table</h2>
        <div class="flex items-center justify-between rounded-2xl border border-tf10-line bg-tf10-raised px-4 py-3">
          <span id="tf-10-party-l" class="text-[.75rem] font-medium tracking-[.16em] text-tf10-muted uppercase">Guests</span>
          <div class="tf-10__stepper flex items-center gap-[.4rem]" role="group" aria-labelledby="tf-10-party-l">
            <button type="button" data-d="-1" aria-label="Fewer guests" class="size-11 cursor-pointer rounded-full border border-tf10-line bg-transparent text-[1.25rem] text-tf10-gold-2 [transition:background_.2s,border-color_.2s] enabled:hover:border-tf10-gold enabled:hover:bg-tf10-gold/12 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf10-gold disabled:cursor-not-allowed disabled:opacity-30">−</button>
            <output aria-live="polite" class="tf-10__n min-w-10 text-center font-tf10-serif text-[1.75rem] font-semibold [font-variant-numeric:lining-nums]">2</output>
            <button type="button" data-d="1" aria-label="More guests" class="size-11 cursor-pointer rounded-full border border-tf10-line bg-transparent text-[1.25rem] text-tf10-gold-2 [transition:background_.2s,border-color_.2s] enabled:hover:border-tf10-gold enabled:hover:bg-tf10-gold/12 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf10-gold disabled:cursor-not-allowed disabled:opacity-30">+</button>
          </div>
        </div>
        <fieldset class="grid min-w-0 gap-[.7rem]"><legend class="mb-[.7rem] flex items-baseline gap-[.6rem] p-0 text-[.75rem] font-medium tracking-[.16em] text-tf10-muted uppercase">Date</legend><div class="tf-10__dates grid snap-x snap-mandatory auto-cols-[4.25rem] grid-flow-col gap-2 overflow-x-auto -m-[.2rem] p-[.2rem] [mask:linear-gradient(90deg,#000_85%,transparent)] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden *:snap-start [&_input]:absolute [&_input]:inset-0 [&_input]:z-1 [&_input]:m-0 [&_input]:cursor-pointer [&_input]:opacity-0 [&_input:focus-visible+span]:outline-2 [&_input:focus-visible+span]:outline-offset-2 [&_input:focus-visible+span]:outline-tf10-gold-2 forced-colors:[&_input:checked+span]:bg-[Highlight] forced-colors:[&_input:checked+span]:text-[HighlightText] *:relative *:text-[.75rem] *:font-medium *:text-tf10-muted [&_span]:grid [&_span]:justify-items-center [&_span]:gap-[.1rem] [&_span]:rounded-2xl [&_span]:border [&_span]:border-tf10-line [&_span]:bg-tf10-raised [&_span]:py-[.7rem] [&_span]:text-tf10-ink [&_span]:[transition:all_.25s_var(--ease-tf10)] [&_small]:text-[.66rem] [&_small]:tracking-[.14em] [&_small]:text-tf10-muted [&_small]:uppercase [&_b]:font-tf10-serif [&_b]:text-[1.6rem] [&_b]:leading-none [&_b]:font-semibold [&_input:checked+span]:border-transparent [&_input:checked+span]:bg-[linear-gradient(160deg,var(--color-tf10-gold-2),var(--color-tf10-gold))] [&_input:checked+span]:text-tf10-on [&_input:checked+span]:shadow-[0_10px_24px_-12px_var(--color-tf10-gold)] [&_input:checked+span_small]:text-inherit [&_input:checked+span_small]:opacity-80"></div></fieldset>
        <fieldset class="grid min-w-0 gap-[.7rem]"><legend class="mb-[.7rem] flex items-baseline gap-[.6rem] p-0 text-[.75rem] font-medium tracking-[.16em] text-tf10-muted uppercase">Time <span class="tf-10__avail text-[.8rem] tracking-[.04em] text-tf10-gold normal-case"></span></legend><div class="tf-10__times grid grid-cols-[repeat(auto-fill,minmax(5.25rem,1fr))] gap-[.45rem] [&_input]:absolute [&_input]:inset-0 [&_input]:z-1 [&_input]:m-0 [&_input]:cursor-pointer [&_input]:opacity-0 [&_input:focus-visible+span]:outline-2 [&_input:focus-visible+span]:outline-offset-2 [&_input:focus-visible+span]:outline-tf10-gold-2 forced-colors:[&_input:checked+span]:bg-[Highlight] forced-colors:[&_input:checked+span]:text-[HighlightText] *:relative *:text-[.75rem] *:font-medium *:text-tf10-muted [&_span]:grid [&_span]:min-h-11 [&_span]:animate-tf10-in [&_span]:place-items-center [&_span]:rounded-[.7rem] [&_span]:border [&_span]:border-tf10-line [&_span]:text-[.92rem] [&_span]:text-tf10-ink [&_span]:tabular-nums [&_span]:transition-all [&_span]:duration-200 [&_span]:[animation-delay:calc(var(--k,0)*25ms)] [&_label:hover_input:not(:disabled)+span]:border-tf10-gold [&_input:checked+span]:border-tf10-gold [&_input:checked+span]:bg-tf10-gold/20 [&_input:checked+span]:font-semibold [&_input:checked+span]:text-tf10-gold-2 [&_input:disabled]:cursor-not-allowed [&_input:disabled+span]:line-through [&_input:disabled+span]:opacity-35"></div><p class="tf-10__large text-[.9rem] text-tf10-muted" hidden>For parties of 9 or more, please call <a href="tel:+442070000000" class="text-tf10-gold-2 underline hover:text-tf10-gold">020 7000 0000</a>.</p></fieldset>
        <fieldset class="grid min-w-0 gap-[.7rem]">
          <legend class="mb-[.7rem] flex items-baseline gap-[.6rem] p-0 text-[.75rem] font-medium tracking-[.16em] text-tf10-muted uppercase">Seating</legend>
          <div class="grid grid-cols-3 gap-[.6rem] max-[30rem]:grid-cols-1">
            <label class="group/a relative grid overflow-hidden rounded-2xl border border-tf10-line bg-tf10-raised text-[.75rem] font-medium text-tf10-muted [transition:border-color_.25s,box-shadow_.25s] has-checked:border-tf10-gold has-checked:shadow-[0_0_0_1px_var(--color-tf10-gold)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tf10-gold-2 max-[30rem]:grid-cols-[5rem_1fr] max-[30rem]:items-center forced-colors:has-checked:outline-2 forced-colors:has-checked:outline-[Highlight]"><input type="radio" name="tf-10-area" value="Dining room" checked class="absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=400&h=260&fit=crop&auto=format&q=60" width="400" height="260" alt="" loading="lazy" decoding="async" class="block aspect-[3/2] h-auto w-full bg-[#2a1e10] object-cover brightness-70 grayscale-60 [transition:filter_.4s_var(--ease-tf10),scale_.6s_var(--ease-tf10)] group-hover/a:scale-105 group-has-checked/a:filter-none"><span class="px-[.7rem] py-[.55rem] text-[.85rem] text-tf10-ink">Dining room</span></label>
            <label class="group/a relative grid overflow-hidden rounded-2xl border border-tf10-line bg-tf10-raised text-[.75rem] font-medium text-tf10-muted [transition:border-color_.25s,box-shadow_.25s] has-checked:border-tf10-gold has-checked:shadow-[0_0_0_1px_var(--color-tf10-gold)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tf10-gold-2 max-[30rem]:grid-cols-[5rem_1fr] max-[30rem]:items-center forced-colors:has-checked:outline-2 forced-colors:has-checked:outline-[Highlight]"><input type="radio" name="tf-10-area" value="Terrace" class="absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><img src="https://images.unsplash.com/photo-1559339352-11d035aa65de?w=400&h=260&fit=crop&auto=format&q=60" width="400" height="260" alt="" loading="lazy" decoding="async" class="block aspect-[3/2] h-auto w-full bg-[#2a1e10] object-cover brightness-70 grayscale-60 [transition:filter_.4s_var(--ease-tf10),scale_.6s_var(--ease-tf10)] group-hover/a:scale-105 group-has-checked/a:filter-none"><span class="px-[.7rem] py-[.55rem] text-[.85rem] text-tf10-ink">Terrace</span></label>
            <label class="group/a relative grid overflow-hidden rounded-2xl border border-tf10-line bg-tf10-raised text-[.75rem] font-medium text-tf10-muted [transition:border-color_.25s,box-shadow_.25s] has-checked:border-tf10-gold has-checked:shadow-[0_0_0_1px_var(--color-tf10-gold)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tf10-gold-2 max-[30rem]:grid-cols-[5rem_1fr] max-[30rem]:items-center forced-colors:has-checked:outline-2 forced-colors:has-checked:outline-[Highlight]"><input type="radio" name="tf-10-area" value="Chef's counter" class="absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><img src="https://images.unsplash.com/photo-1552566626-52f8b828add9?w=400&h=260&fit=crop&auto=format&q=60" width="400" height="260" alt="" loading="lazy" decoding="async" class="block aspect-[3/2] h-auto w-full bg-[#2a1e10] object-cover brightness-70 grayscale-60 [transition:filter_.4s_var(--ease-tf10),scale_.6s_var(--ease-tf10)] group-hover/a:scale-105 group-has-checked/a:filter-none"><span class="px-[.7rem] py-[.55rem] text-[.85rem] text-tf10-ink">Chef's counter</span></label>
          </div>
        </fieldset>
        <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
          <div class="grid gap-[.45rem]"><label for="tf-10-name" class="text-[.75rem] font-medium tracking-[.16em] text-tf10-muted uppercase">Name</label><input id="tf-10-name" autocomplete="name" required class="min-h-[2.9rem] w-full rounded-[.7rem] border border-tf10-line bg-tf10-raised px-[.9rem] py-[.6rem] text-[.95rem] text-tf10-ink focus-visible:border-tf10-gold focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf10-gold)_22%,transparent)] focus-visible:outline-none user-invalid:border-[#e57373]"></div>
          <div class="grid gap-[.45rem]"><label for="tf-10-tel" class="text-[.75rem] font-medium tracking-[.16em] text-tf10-muted uppercase">Phone</label><input id="tf-10-tel" type="tel" autocomplete="tel" required class="min-h-[2.9rem] w-full rounded-[.7rem] border border-tf10-line bg-tf10-raised px-[.9rem] py-[.6rem] text-[.95rem] text-tf10-ink focus-visible:border-tf10-gold focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf10-gold)_22%,transparent)] focus-visible:outline-none user-invalid:border-[#e57373]"></div>
        </div>
        <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
          <div class="grid gap-[.45rem]"><label for="tf-10-occ" class="text-[.75rem] font-medium tracking-[.16em] text-tf10-muted uppercase">Occasion</label><select id="tf-10-occ" class="min-h-[2.9rem] w-full rounded-[.7rem] border border-tf10-line bg-tf10-raised px-[.9rem] py-[.6rem] text-[.95rem] text-tf10-ink focus-visible:border-tf10-gold focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf10-gold)_22%,transparent)] focus-visible:outline-none user-invalid:border-[#e57373]"><option>None</option><option>Birthday</option><option>Anniversary</option><option>Business</option><option>Date night</option></select></div>
          <div class="grid gap-[.45rem]"><label for="tf-10-req" class="text-[.75rem] font-medium tracking-[.16em] text-tf10-muted uppercase">Requests <span class="tracking-normal normal-case opacity-70">Optional</span></label><input id="tf-10-req" placeholder="Allergies, high chair, quiet table…" class="min-h-[2.9rem] w-full rounded-[.7rem] border border-tf10-line bg-tf10-raised px-[.9rem] py-[.6rem] text-[.95rem] text-tf10-ink focus-visible:border-tf10-gold focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf10-gold)_22%,transparent)] focus-visible:outline-none user-invalid:border-[#e57373]"></div>
        </div>
        <div class="grid gap-[.8rem] border-t border-tf10-line pt-[1.2rem]"><p role="status" class="tf-10__sum text-center font-tf10-serif text-[1.25rem] leading-[1.3] font-medium text-balance text-tf10-gold-2"></p><button type="button" class="tf-10__book min-h-[3.3rem] cursor-pointer rounded-full border-0 bg-[linear-gradient(110deg,var(--color-tf10-gold),var(--color-tf10-gold-2),var(--color-tf10-gold))] bg-[length:200%_100%] text-[.82rem] font-semibold tracking-[.2em] text-tf10-on uppercase [transition:background-position_.8s_var(--ease-tf10),translate_.2s_var(--ease-tf10)] hover:-translate-y-0.5 hover:bg-[position:100%_0] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf10-gold-2 forced-colors:border forced-colors:border-[ButtonText]">Confirm reservation</button></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf10-bg: #0d0b09;
  --color-tf10-card: #15120f;
  --color-tf10-raised: #1d1915;
  --color-tf10-ink: #f3ebdf;
  --color-tf10-muted: #a69a89;
  --color-tf10-line: #2e2821;
  --color-tf10-gold: #d4a95a;
  --color-tf10-gold-2: #f0d39a;
  --color-tf10-on: #1a1206;
  --font-tf10-serif: "Cormorant Garamond", ui-serif, Georgia, serif;
  --font-tf10-sans: "Jost", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf10: cubic-bezier(0.16,1,0.3,1);
  --animate-tf10-in: tf10-in 0.4s cubic-bezier(0.16,1,0.3,1) both;

  @keyframes tf10-in {
    from {
      opacity: 0;
      translate: 0 6px;
    }
  }
}
/* Root rule: full-bleed contract. Dark-first like its CSS original: @theme holds the dark values,
   data-theme="light" overrides them and drops the candle-glow wash. */

.tf-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: dark;
  --tf10-wash: radial-gradient(50rem 30rem at 50% 0%, #2a1e10, transparent 70%);
}

.tf-10[data-theme="light"] {
  color-scheme: light;
  --tf10-wash: none;
  --color-tf10-bg: #f4eee4;
  --color-tf10-card: #fffaf2;
  --color-tf10-raised: #f6efe3;
  --color-tf10-ink: #2a2017;
  --color-tf10-muted: #7b6c5b;
  --color-tf10-line: #e5d9c6;
  --color-tf10-gold: #9a7232;
  --color-tf10-gold-2: #b88a3e;
  --color-tf10-on: #fff;
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-10').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : true);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.tf-10');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const DAYS = 10, MAX = 12, SLOTS = ['17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00'];
  let party = 2;
  const wd = new Intl.DateTimeFormat('en-GB', { weekday: 'short' }), full = new Intl.DateTimeFormat('en-GB', { weekday: 'short', day: 'numeric', month: 'short' });
  const dates = $('.tf-10__dates'), times = $('.tf-10__times');
  const days = [...Array(DAYS)].map((_, i) => { const d = new Date(); d.setDate(d.getDate() + i); return d; });
  dates.innerHTML = days.map((d, i) => '<label><input type="radio" name="tf-10-date" value="' + i + '"' + (i === 0 ? ' checked' : '') + ' aria-label="' + full.format(d) + '"><span aria-hidden="true"><small>' + (i === 0 ? 'Today' : wd.format(d)) + '</small><b>' + d.getDate() + '</b></span></label>').join('');
  const fmt12 = (t) => { let [h, m] = t.split(':').map(Number); const ap = h >= 12 ? 'pm' : 'am'; h = h % 12 || 12; return h + ':' + String(m).padStart(2, '0') + ' ' + ap; };
  const isBooked = (dayIdx, slotIdx) => ((dayIdx * 7 + slotIdx * 3 + party * 5) % 10) < (party > 4 ? 6 : 3);
  const renderTimes = () => {
    const day = Number(root.querySelector('[name="tf-10-date"]:checked').value);
    const prev = (root.querySelector('[name="tf-10-time"]:checked') || {}).value;
    const large = party > 8;
    $('.tf-10__large').hidden = !large;
    times.hidden = large;
    times.innerHTML = SLOTS.map((t, i) => { const b = isBooked(day, i); return '<label><input type="radio" name="tf-10-time" value="' + t + '"' + (b ? ' disabled' : '') + (t === prev && !b ? ' checked' : '') + ' aria-label="' + fmt12(t) + (b ? ', fully booked' : '') + '"><span style="--k:' + i + '" aria-hidden="true">' + fmt12(t) + '</span></label>'; }).join('');
    const open = SLOTS.filter((_, i) => !isBooked(day, i)).length;
    $('.tf-10__avail').textContent = large ? '' : open + ' of ' + SLOTS.length + ' available';
    summary();
  };
  const summary = () => {
    const d = days[Number(root.querySelector('[name="tf-10-date"]:checked').value)];
    const t = root.querySelector('[name="tf-10-time"]:checked'), a = root.querySelector('[name="tf-10-area"]:checked').value;
    $('.tf-10__sum').textContent = 'Table for ' + party + ' · ' + full.format(d) + ' · ' + (t ? fmt12(t.value) : 'choose a time') + ' · ' + a;
  };
  root.querySelectorAll('.tf-10__stepper button').forEach((b) => b.addEventListener('click', () => {
    party = Math.max(1, Math.min(MAX, party + Number(b.dataset.d)));
    $('.tf-10__n').textContent = party;
    root.querySelector('[data-d="-1"]').disabled = party === 1; root.querySelector('[data-d="1"]').disabled = party === MAX;
    renderTimes();
  }));
  dates.addEventListener('change', renderTimes);
  root.addEventListener('change', (e) => { if (e.target.name === 'tf-10-time' || e.target.name === 'tf-10-area') summary(); });
  $('.tf-10__book').addEventListener('click', () => {
    if (!root.querySelector('[name="tf-10-time"]:checked')) { (times.querySelector('input:not(:disabled)') || $('.tf-10__book')).focus(); $('.tf-10__sum').textContent = 'Please choose a time.'; return; }
    const bad = [...root.querySelectorAll('[required]')].find((f) => !f.checkValidity());
    if (bad) { bad.reportValidity(); return; }
    $('.tf-10__sum').textContent = 'Confirmed — ' + $('.tf-10__sum').textContent + '. A confirmation text is on its way.';
    $('.tf-10__book').textContent = 'Reservation confirmed';
  });
  renderTimes();
})();
```
