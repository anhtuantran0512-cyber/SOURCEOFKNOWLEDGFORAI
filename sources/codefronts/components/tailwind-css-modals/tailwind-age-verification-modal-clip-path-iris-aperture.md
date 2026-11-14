---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-age-verification-modal-clip-path-iris-aperture/"
title: "Tailwind Age Verification Modal with Clip-Path Iris Aperture"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A 21+ gate that opens like a camera iris — clip-path: circle(0%) expanding past the card's corners."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Age Verification Modal with Clip-Path Iris Aperture
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-age-verification-modal-clip-path-iris-aperture/

A 21+ gate that opens like a camera iris — clip-path: circle(0%) expanding past the card's corners. Tailwind ships no clip-path scale, so the port uses arbitrary properties on the two states, which is the idiomatic answer: an iris radius is not a design-scale value.
## HTML
```html
<section class="tw-06 w-full min-h-svh grid place-items-center bg-tw06-bg font-tw06-sans px-6 py-10">
  <button type="button" data-tw06-open class="inline-flex items-center justify-center min-h-11 px-7 rounded-lg border border-tw06-brand bg-transparent text-[15px] font-semibold text-tw06-brandlt cursor-pointer transition-colors duration-200 hover:bg-tw06-brand hover:text-white focus-visible:outline-2 focus-visible:outline-tw06-brandlt focus-visible:outline-offset-2">Enter shop</button>

  <dialog id="tw-06-dlg" aria-labelledby="tw-06-title" class="m-auto w-[min(400px,94vw)] p-0 border border-tw06-cardedge rounded-[14px] text-center text-tw06-ink bg-tw06-card shadow-[0_40px_60px_-20px_#1a0f0899] opacity-0 [clip-path:circle(0%_at_50%_50%)] transition-[opacity,clip-path,overlay,display] duration-[550ms] ease-[cubic-bezier(.65,0,.35,1)] transition-discrete open:opacity-100 open:[clip-path:circle(150%_at_50%_50%)] open:starting:opacity-0 open:starting:[clip-path:circle(0%_at_50%_50%)] open:backdrop:bg-tw06-scrim open:backdrop:backdrop-blur-[6px] motion-reduce:transition-[opacity] motion-reduce:duration-150 motion-reduce:[clip-path:none]">
    <div class="px-6 pt-9 pb-7">
      <span aria-hidden="true" class="inline-grid place-items-center size-13 mb-3.5 rounded-full bg-tw06-tint text-[22px] text-tw06-brand">&#128274;</span>
      <h2 id="tw-06-title" class="mb-2 font-tw06-display text-[1.4rem] font-extrabold tracking-[-0.015em] leading-tight">You must be 21 or older</h2>
      <p class="mb-[22px] text-sm leading-relaxed text-tw06-sub text-pretty">This site sells products intended for adults 21+. Please verify your date of birth to continue.</p>

      <form method="dialog" data-tw06-form class="flex flex-col gap-3.5">
        <div class="grid grid-cols-[1fr_1fr_1.4fr] gap-2 text-left">
          <label class="flex flex-col gap-1.5 min-w-0">
            <span class="text-[0.7rem] font-bold uppercase tracking-[0.06em] text-tw06-sub">Month</span>
            <input type="text" autofocus required inputmode="numeric" maxlength="2" pattern="[0-9]{1,2}" autocomplete="bday-month" placeholder="MM" class="min-h-11 w-full min-w-0 px-2 rounded-lg border border-tw06-line bg-white text-center text-[15px] text-tw06-ink tabular-nums placeholder:text-tw06-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw06-brand focus:shadow-[0_0_0_3px_var(--color-tw06-ring)]">
          </label>
          <label class="flex flex-col gap-1.5 min-w-0">
            <span class="text-[0.7rem] font-bold uppercase tracking-[0.06em] text-tw06-sub">Day</span>
            <input type="text" required inputmode="numeric" maxlength="2" pattern="[0-9]{1,2}" autocomplete="bday-day" placeholder="DD" class="min-h-11 w-full min-w-0 px-2 rounded-lg border border-tw06-line bg-white text-center text-[15px] text-tw06-ink tabular-nums placeholder:text-tw06-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw06-brand focus:shadow-[0_0_0_3px_var(--color-tw06-ring)]">
          </label>
          <label class="flex flex-col gap-1.5 min-w-0">
            <span class="text-[0.7rem] font-bold uppercase tracking-[0.06em] text-tw06-sub">Year</span>
            <input type="text" required inputmode="numeric" maxlength="4" pattern="[0-9]{4}" autocomplete="bday-year" placeholder="YYYY" class="min-h-11 w-full min-w-0 px-2 rounded-lg border border-tw06-line bg-white text-center text-[15px] text-tw06-ink tabular-nums placeholder:text-tw06-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw06-brand focus:shadow-[0_0_0_3px_var(--color-tw06-ring)]">
          </label>
        </div>

        <label class="flex items-center gap-2.5 text-[13px] text-tw06-sub cursor-pointer">
          <input type="checkbox" class="size-4 accent-tw06-brand cursor-pointer focus-visible:outline-2 focus-visible:outline-tw06-brand focus-visible:outline-offset-2">
          <span>Remember me for 30 days on this device</span>
        </label>

        <p data-tw06-error hidden role="alert" class="text-[13px] font-semibold text-tw06-brand">Sorry — you must be 21 or older to enter.</p>

        <button type="submit" class="min-h-11 mt-1.5 px-5 rounded-lg border-0 bg-tw06-brand text-[15px] font-bold text-white shadow-[0_8px_18px_-6px_var(--color-tw06-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw06-branddark hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw06-brand focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0">Enter site &rarr;</button>
        <button type="button" data-tw06-leave class="min-h-11 px-5 rounded-md border-0 bg-transparent text-[13px] font-medium text-tw06-sub cursor-pointer transition-colors duration-200 hover:text-tw06-ink hover:underline focus-visible:outline-2 focus-visible:outline-tw06-brand focus-visible:outline-offset-2">I'm under 21</button>
      </form>

      <p class="pt-4 mt-1.5 border-t border-tw06-line text-xs leading-relaxed text-tw06-sub">Alcohol is intended for adults 21+. Please drink responsibly. Site restricted per US federal law.</p>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw06-bg: #1a0f08;
  --color-tw06-bg: oklch(0.2 0.04 50);
  --color-tw06-card: #f5ead0;
  --color-tw06-card: oklch(0.94 0.04 87);
  --color-tw06-cardedge: #2a181014;
  --color-tw06-cardedge: oklch(0.25 0.04 50 / 0.08);
  --color-tw06-ink: #2a1810;
  --color-tw06-ink: oklch(0.26 0.04 50);
  --color-tw06-sub: #6b4e33;
  --color-tw06-sub: oklch(0.44 0.06 60);
  --color-tw06-line: #2a181029;
  --color-tw06-line: oklch(0.26 0.04 50 / 0.16);
  --color-tw06-brand: #a8441f;
  --color-tw06-brand: oklch(0.5 0.14 43);
  --color-tw06-brandlt: #e0703f;
  --color-tw06-brandlt: oklch(0.66 0.15 43);
  --color-tw06-branddark: #8a3517;
  --color-tw06-branddark: oklch(0.43 0.13 43);
  --color-tw06-tint: #c8552a29;
  --color-tw06-tint: oklch(0.57 0.15 43 / 0.16);
  --color-tw06-ring: #c8552a26;
  --color-tw06-ring: oklch(0.57 0.15 43 / 0.15);
  --color-tw06-glow: #c8552a80;
  --color-tw06-glow: oklch(0.57 0.15 43 / 0.5);
  --color-tw06-scrim: #1a0f08d9;
  --color-tw06-scrim: oklch(0.2 0.04 50 / 0.85);
  --font-tw06-sans: 'Outfit', system-ui, sans-serif;
  --font-tw06-display: 'Playfair Display', Georgia, serif;
}

.tw-06 {
  width: 100%;
}
/* The card's warm paper gradient: a two-stop background is not a utility's job. */

#tw-06-dlg {
  background-image: linear-gradient(180deg, oklch(0.94 0.04 87), oklch(0.91 0.05 84));
}

#tw-06-dlg::backdrop {
  background: oklch(0.2 0.04 50 / 0);
  backdrop-filter: blur(0px);
  transition: background .25s ease, backdrop-filter .25s ease, overlay .25s allow-discrete, display .25s allow-discrete;
}

@starting-style {
  #tw-06-dlg[open]::backdrop {
    background: oklch(0.2 0.04 50 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-06-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-06');
  var dlg = root.querySelector('#tw-06-dlg');
  var card = dlg.firstElementChild;
  var form = root.querySelector('[data-tw06-form]');
  var err = root.querySelector('[data-tw06-error]');
  var MIN_AGE = 21;

  root.querySelector('[data-tw06-open]').addEventListener('click', function () { dlg.showModal(); });

  form.addEventListener('submit', function (e) {
    var i = form.querySelectorAll('input[inputmode=numeric]');
    var m = +i[0].value, d = +i[1].value, y = +i[2].value;
    var dob = new Date(y, m - 1, d), now = new Date();
    var age = now.getFullYear() - y - ((now.getMonth() < m - 1 || (now.getMonth() === m - 1 && now.getDate() < d)) ? 1 : 0);
    if (!(dob.getFullYear() === y && age >= MIN_AGE)) { e.preventDefault(); err.hidden = false; return; }
    err.hidden = true; // Production: persist the pass before letting the dialog close.
  });

  // Production age gates navigate away instead of revealing the page.
  root.querySelector('[data-tw06-leave]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
