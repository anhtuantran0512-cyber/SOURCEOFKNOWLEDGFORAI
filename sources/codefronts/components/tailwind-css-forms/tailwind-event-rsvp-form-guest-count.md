---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-event-rsvp-form-guest-count/"
title: "Tailwind Event RSVP Form with Guest Count"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's invitation-style RSVP, ported one-for-one to Tailwind v4: a gold-foil names headline (animated bg-clip-text), accept / maybe / decline…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Event RSVP Form with Guest Count
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-event-rsvp-form-guest-count/

The CSS collection's invitation-style RSVP, ported one-for-one to Tailwind v4: a gold-foil names headline (animated bg-clip-text), accept / maybe / decline as large radio cards, a guest stepper that clones a named row with meal choice from a <template> and lets it fade in with starting:, dietary chips, a song request, and a decline path that swaps everything for a note to the couple via group-has-[[value=no]:checked]/root:.
## HTML
```html
<div class="tf-13 group/root relative block min-h-svh w-full [background:var(--tf13-wash),var(--color-tf13-bg)] pt-[72px] font-tf13-sans leading-[normal] text-tf13-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="relative w-full max-w-[36rem] overflow-hidden rounded-[.5rem] bg-tf13-card shadow-[0_1px_0_var(--color-tf13-line),0_40px_80px_-40px_rgba(50,35,15,.5)] before:pointer-events-none before:absolute before:inset-[.6rem] before:z-2 before:rounded-[.25rem] before:border before:border-[color-mix(in_oklab,#b08a48_45%,transparent)] before:content-['']">
      <figure class="h-44 bg-[#cdbfa8]">
        <img src="https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=1000&h=520&fit=crop&auto=format&q=70" width="1000" height="520" alt="Candle-lit reception tables with flowers" loading="lazy" decoding="async" class="block size-full object-cover">
      </figure>
      <div class="grid gap-[1.3rem] p-[clamp(1.5rem,6vw,2.75rem)]" role="form" aria-labelledby="tf-13-title">
        <header class="grid gap-2 border-b border-tf13-line pb-[1.4rem] text-center">
          <p class="text-[.72rem] font-semibold tracking-[.24em] text-tf13-muted uppercase">Together with their families</p>
          <h2 id="tf-13-title" class="my-[.2rem] animate-tf13-foil bg-[image:var(--tf13-foil)] bg-[length:200%_100%] bg-clip-text font-tf13-serif text-[clamp(2.4rem,9vw,3.5rem)] leading-none font-normal tracking-[-.01em] text-transparent forced-colors:bg-none forced-colors:text-[CanvasText]">Amelia <span class="italic">&amp;</span> Theo</h2>
          <p class="font-tf13-serif text-[1.1rem] leading-[1.5] font-normal italic">Saturday, 12 June 2027 · 4 pm<br>Hedsor House, Buckinghamshire</p>
          <p class="text-[.72rem] font-semibold tracking-[.24em] text-tf13-muted uppercase">Kindly reply by 1 May</p>
        </header>
        <div class="grid gap-[.4rem]"><label for="tf-13-name" class="text-[.82rem] font-semibold">Your name</label><input id="tf-13-name" autocomplete="name" required placeholder="As written on your invitation" class="min-h-[2.9rem] w-full rounded-none border-b border-tf13-line bg-transparent px-[.1rem] py-[.6rem] text-[1rem] text-tf13-ink [transition:border-color_.2s] focus-visible:border-tf13-ink focus-visible:shadow-[0_1px_0_var(--color-tf13-ink)] focus-visible:outline-none user-invalid:border-[#b42318]"></div>
        <fieldset class="grid min-w-0 grid-cols-3 gap-2 max-[28rem]:grid-cols-1">
          <legend class="mb-[.65rem] text-[.82rem] font-semibold">Will you be joining us?</legend>
          <label class="group/at relative text-[.82rem] font-semibold"><input type="radio" name="tf-13-a" value="yes" checked class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid h-full gap-[.2rem] rounded-[.4rem] border border-tf13-line bg-tf13-soft px-[.8rem] py-4 text-center [transition:all_.3s_var(--ease-tf13)] peer-checked:border-tf13-accent peer-checked:bg-tf13-accent peer-checked:text-tf13-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf13-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]"><b class="font-tf13-serif text-[1rem] leading-[1.2] font-normal">Joyfully accept</b><small class="text-[.72rem] font-normal text-tf13-muted group-has-checked/at:text-inherit group-has-checked/at:opacity-75">Count me in</small></span></label>
          <label class="group/at relative text-[.82rem] font-semibold"><input type="radio" name="tf-13-a" value="maybe" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid h-full gap-[.2rem] rounded-[.4rem] border border-tf13-line bg-tf13-soft px-[.8rem] py-4 text-center [transition:all_.3s_var(--ease-tf13)] peer-checked:border-tf13-accent peer-checked:bg-tf13-accent peer-checked:text-tf13-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf13-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]"><b class="font-tf13-serif text-[1rem] leading-[1.2] font-normal">Not sure yet</b><small class="text-[.72rem] font-normal text-tf13-muted group-has-checked/at:text-inherit group-has-checked/at:opacity-75">I'll confirm soon</small></span></label>
          <label class="group/at relative text-[.82rem] font-semibold"><input type="radio" name="tf-13-a" value="no" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid h-full gap-[.2rem] rounded-[.4rem] border border-tf13-line bg-tf13-soft px-[.8rem] py-4 text-center [transition:all_.3s_var(--ease-tf13)] peer-checked:border-tf13-accent peer-checked:bg-tf13-accent peer-checked:text-tf13-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf13-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]"><b class="font-tf13-serif text-[1rem] leading-[1.2] font-normal">Regretfully decline</b><small class="text-[.72rem] font-normal text-tf13-muted group-has-checked/at:text-inherit group-has-checked/at:opacity-75">Celebrating in spirit</small></span></label>
        </fieldset>
        <div class="grid gap-[1.3rem] group-has-[[value=no]:checked]/root:hidden">
          <div class="grid gap-[.4rem]"><label for="tf-13-meal" class="text-[.82rem] font-semibold">Your meal</label>
            <select id="tf-13-meal" class="min-h-[2.9rem] w-full rounded-none border-b border-tf13-line bg-transparent px-[.1rem] py-[.6rem] text-[1rem] text-tf13-ink [transition:border-color_.2s] focus-visible:border-tf13-ink focus-visible:shadow-[0_1px_0_var(--color-tf13-ink)] focus-visible:outline-none user-invalid:border-[#b42318] cursor-pointer"><option>Herb-crusted lamb</option><option>Pan-roasted sea bass</option><option>Wild mushroom risotto (V)</option><option>Vegan garden plate (VG)</option></select></div>
          <div class="flex items-center justify-between gap-4 rounded-[.4rem] border border-tf13-line bg-tf13-soft px-4 py-[.9rem]">
            <div><span id="tf-13-g-l" class="text-[.82rem] font-semibold">Additional guests</span><small class="mt-[.15rem] block text-[.78rem] text-tf13-muted">Your invitation includes up to 3</small></div>
            <div class="tf-13__stepper flex items-center gap-[.3rem]" role="group" aria-labelledby="tf-13-g-l">
              <button type="button" data-d="-1" aria-label="Remove a guest" disabled class="size-11 cursor-pointer rounded-full border border-tf13-line bg-tf13-card text-[1.2rem] text-tf13-ink [transition:background_.2s,border-color_.2s] enabled:hover:border-tf13-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf13-ink disabled:cursor-not-allowed disabled:opacity-35">−</button>
              <output aria-live="polite" class="min-w-8 text-center font-tf13-serif text-[1.6rem] font-normal">0</output>
              <button type="button" data-d="1" aria-label="Add a guest" class="size-11 cursor-pointer rounded-full border border-tf13-line bg-tf13-card text-[1.2rem] text-tf13-ink [transition:background_.2s,border-color_.2s] enabled:hover:border-tf13-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf13-ink disabled:cursor-not-allowed disabled:opacity-35">+</button>
            </div>
          </div>
          <div class="tf-13__guests grid gap-3 empty:hidden"></div>
          <fieldset class="flex min-w-0 flex-wrap gap-[.4rem]"><legend class="mb-[.65rem] w-full text-[.82rem] font-semibold">Dietary needs in your party</legend>
            <label class="relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center rounded-full border border-tf13-line px-[.9rem] text-[.82rem] font-medium transition-all duration-200 peer-checked:border-tf13-ink peer-checked:bg-tf13-ink peer-checked:text-tf13-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf13-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Gluten-free</span></label><label class="relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center rounded-full border border-tf13-line px-[.9rem] text-[.82rem] font-medium transition-all duration-200 peer-checked:border-tf13-ink peer-checked:bg-tf13-ink peer-checked:text-tf13-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf13-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Nut allergy</span></label><label class="relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center rounded-full border border-tf13-line px-[.9rem] text-[.82rem] font-medium transition-all duration-200 peer-checked:border-tf13-ink peer-checked:bg-tf13-ink peer-checked:text-tf13-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf13-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Dairy-free</span></label><label class="relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center rounded-full border border-tf13-line px-[.9rem] text-[.82rem] font-medium transition-all duration-200 peer-checked:border-tf13-ink peer-checked:bg-tf13-ink peer-checked:text-tf13-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf13-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Halal</span></label><label class="relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center rounded-full border border-tf13-line px-[.9rem] text-[.82rem] font-medium transition-all duration-200 peer-checked:border-tf13-ink peer-checked:bg-tf13-ink peer-checked:text-tf13-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf13-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Kosher</span></label>
          </fieldset>
          <div class="grid gap-[.4rem]"><label for="tf-13-song" class="text-[.82rem] font-semibold">A song that'll get you dancing <span class="font-normal text-tf13-muted">Optional</span></label><input id="tf-13-song" placeholder="e.g. September — Earth, Wind &amp; Fire" class="min-h-[2.9rem] w-full rounded-none border-b border-tf13-line bg-transparent px-[.1rem] py-[.6rem] text-[1rem] text-tf13-ink [transition:border-color_.2s] focus-visible:border-tf13-ink focus-visible:shadow-[0_1px_0_var(--color-tf13-ink)] focus-visible:outline-none user-invalid:border-[#b42318]"></div>
        </div>
        <div class="hidden gap-2 group-has-[[value=no]:checked]/root:grid group-has-[[value=no]:checked]/root:animate-tf13-in"><label for="tf-13-note" class="text-[.82rem] font-semibold">Leave a note for the couple</label><textarea id="tf-13-note" rows="3" placeholder="We'll miss you!" class="min-h-[2.9rem] w-full resize-y rounded-[.4rem] border border-tf13-line bg-transparent px-[.85rem] py-[.7rem] text-[1rem] text-tf13-ink [transition:border-color_.2s] focus-visible:border-tf13-ink focus-visible:shadow-[0_0_0_1px_var(--color-tf13-ink)] focus-visible:outline-none"></textarea></div>
        <button type="button" class="tf-13__send min-h-[3.2rem] cursor-pointer rounded-[.35rem] border-0 bg-tf13-accent text-[.8rem] font-bold tracking-[.24em] text-tf13-on uppercase [transition:filter_.2s,translate_.2s_var(--ease-tf13)] hover:-translate-y-px hover:brightness-112 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf13-ink">Send RSVP</button>
        <p class="tf-13__status -mt-[.4rem] text-center font-tf13-serif text-[1.1rem] font-normal italic empty:hidden" role="status"></p>
      </div>
    </div>
  </div>
  <template class="tf-13__tpl">
    <div class="tf-13__guest grid grid-cols-[auto_1fr_1fr] items-end gap-[.9rem] pt-1 pb-2 [transition:opacity_.45s_var(--ease-tf13),translate_.45s_var(--ease-tf13)] starting:translate-y-2.5 starting:opacity-0 max-[28rem]:grid-cols-[auto_1fr] max-[28rem]:[&>*:last-child]:col-start-2">
      <span class="tf-13__gnum mb-[.45rem] grid size-8 place-items-center rounded-full border border-[color-mix(in_oklab,#b08a48_60%,transparent)] font-tf13-serif text-[.95rem] font-normal text-[#a07a3c] italic" aria-hidden="true"></span>
      <div class="grid gap-[.4rem]"><label data-for="gn" class="text-[.82rem] font-semibold">Guest name</label><input data-id="gn" placeholder="Full name" class="min-h-[2.9rem] w-full rounded-none border-b border-tf13-line bg-transparent px-[.1rem] py-[.6rem] text-[1rem] text-tf13-ink [transition:border-color_.2s] focus-visible:border-tf13-ink focus-visible:shadow-[0_1px_0_var(--color-tf13-ink)] focus-visible:outline-none user-invalid:border-[#b42318]"></div>
      <div class="grid gap-[.4rem]"><label data-for="gm" class="text-[.82rem] font-semibold">Meal</label><select data-id="gm" class="min-h-[2.9rem] w-full rounded-none border-b border-tf13-line bg-transparent px-[.1rem] py-[.6rem] text-[1rem] text-tf13-ink [transition:border-color_.2s] focus-visible:border-tf13-ink focus-visible:shadow-[0_1px_0_var(--color-tf13-ink)] focus-visible:outline-none user-invalid:border-[#b42318] cursor-pointer"><option>Herb-crusted lamb</option><option>Pan-roasted sea bass</option><option>Wild mushroom risotto (V)</option><option>Vegan garden plate (VG)</option><option>Children's menu</option></select></div>
    </div>
  </template>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf13-bg: #efe9df;
  --color-tf13-card: #fffdf8;
  --color-tf13-ink: #231d17;
  --color-tf13-muted: #7a6f63;
  --color-tf13-line: #e8dfd1;
  --color-tf13-soft: #f8f4ec;
  --color-tf13-accent: #3f4a3c;
  --color-tf13-on: #fdfaf3;
  --font-tf13-serif: "Bodoni Moda", ui-serif, Didot, Georgia, serif;
  --font-tf13-sans: "Manrope", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf13: cubic-bezier(0.16,1,0.3,1);
  --animate-tf13-foil: tf13-foil 6s ease-in-out infinite alternate;
  --animate-tf13-in: tf13-in 0.4s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf13-foil {
    to {
      background-position: 100% 0;
    }
  }

  @keyframes tf13-in {
    from {
      opacity: 0;
      translate: 0 8px;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch, the paper wash and the gold foil gradient.
   @theme holds the light values; dark values override the same variables. */

.tf-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
  --tf13-foil: linear-gradient(100deg, #a07a3c, #e6c983 35%, #b08a48 60%, #f2dca2);
  --tf13-wash: radial-gradient(circle at 20% 20%, #f7f1e6, transparent 50%), radial-gradient(circle at 80% 80%, #e5dccd, transparent 55%);
}

.tf-13[data-theme="dark"] {
  color-scheme: dark;
  --tf13-wash: none;
  --color-tf13-bg: #141210;
  --color-tf13-card: #1c1916;
  --color-tf13-ink: #f1e9dc;
  --color-tf13-muted: #a99d8e;
  --color-tf13-line: #332d26;
  --color-tf13-soft: #221e1a;
  --color-tf13-accent: #c9d3b8;
  --color-tf13-on: #171a14;
}

@media (prefers-color-scheme: dark) {
  .tf-13:not([data-theme="light"]) {
    color-scheme: dark;
    --tf13-wash: none;
    --color-tf13-bg: #141210;
    --color-tf13-card: #1c1916;
    --color-tf13-ink: #f1e9dc;
    --color-tf13-muted: #a99d8e;
    --color-tf13-line: #332d26;
    --color-tf13-soft: #221e1a;
    --color-tf13-accent: #c9d3b8;
    --color-tf13-on: #171a14;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-13').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
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
  const root = document.querySelector('.tf-13');
  if (!root) return;
  const MAX = 3;
  const wrap = root.querySelector('.tf-13__guests'), tpl = root.querySelector('.tf-13__tpl'), out = root.querySelector('.tf-13__stepper output');
  const minus = root.querySelector('[data-d="-1"]'), plus = root.querySelector('[data-d="1"]');
  let n = 0;
  const addRow = (k) => {
    const row = tpl.content.firstElementChild.cloneNode(true);
    row.querySelector('.tf-13__gnum').textContent = k;
    row.querySelectorAll('[data-id]').forEach((el) => { el.id = 'tf-13-' + el.dataset.id + '-' + k; });
    row.querySelectorAll('[data-for]').forEach((el) => { el.htmlFor = 'tf-13-' + el.dataset.for + '-' + k; el.textContent += ' ' + k; });
    wrap.append(row);
    return row;
  };
  const set = (next) => {
    next = Math.max(0, Math.min(MAX, next));
    if (next > n) { for (let k = n + 1; k <= next; k++) { const r = addRow(k); if (k === next) r.querySelector('input').focus(); } }
    else { while (wrap.children.length > next) wrap.lastElementChild.remove(); }
    n = next; out.textContent = n; minus.disabled = n === 0; plus.disabled = n === MAX;
  };
  minus.addEventListener('click', () => { set(n - 1); if (minus.disabled) plus.focus(); });
  plus.addEventListener('click', () => { set(n + 1); });
  root.querySelector('.tf-13__send').addEventListener('click', () => {
    const name = root.querySelector('#tf-13-name'), status = root.querySelector('.tf-13__status');
    if (!name.value.trim()) { name.focus(); name.reportValidity(); return; }
    const a = root.querySelector('[name="tf-13-a"]:checked').value, first = name.value.trim().split(' ')[0];
    status.textContent = a === 'no' ? 'Thank you, ' + first + ' — you will be missed.' : a === 'maybe' ? 'Thanks, ' + first + '. We\'ll hold a place until 1 May.' : 'Wonderful! See you there, ' + first + (n ? ' + ' + n + ' guest' + (n > 1 ? 's' : '') : '') + '.';
  });
})();
```
