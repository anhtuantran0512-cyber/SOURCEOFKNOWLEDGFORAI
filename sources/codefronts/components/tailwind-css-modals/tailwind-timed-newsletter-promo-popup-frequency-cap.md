---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-timed-newsletter-promo-popup-frequency-cap/"
title: "Tailwind Timed Newsletter Promo Popup with Frequency Cap"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "The conversion popup, rebuilt on v4: a cream card with a gradient cap, one email field and a strong CTA, opened once after a delay and then never again this…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Timed Newsletter Promo Popup with Frequency Cap
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-timed-newsletter-promo-popup-frequency-cap/

The conversion popup, rebuilt on v4: a cream card with a gradient cap, one email field and a strong CTA, opened once after a delay and then never again this session. The port moves the palette out of arbitrary neutral-* picks into @theme tokens, so the card retints from one line.
## HTML
```html
<section class="tm-07 w-full min-h-svh grid place-items-center bg-tm07-bg font-tm07-sans px-6 py-10">
  <div class="flex flex-col items-center gap-3">
    <button type="button" data-tm07-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-xl border border-tm07-edge bg-tm07-btn text-[15px] font-semibold text-tm07-ink cursor-pointer transition-colors duration-200 hover:bg-tm07-btnhover focus-visible:outline-2 focus-visible:outline-tm07-acc focus-visible:outline-offset-2">Show popup</button>
    <span class="font-tm07-mono text-xs tracking-[0.14em] text-tm07-faint">auto-opens once per session, after 3s</span>
  </div>

  <dialog id="tm-07-dlg" data-state="ask" aria-labelledby="tm-07-title" class="group m-auto w-[min(430px,94vw)] overflow-hidden p-0 rounded-3xl border border-black/10 bg-tm07-card text-tm07-oncard shadow-[0_40px_90px_-30px_#000] opacity-0 translate-y-4 scale-[0.96] transition-[opacity,translate,scale,overlay,display] duration-300 transition-discrete open:opacity-100 open:translate-y-0 open:scale-100 open:starting:opacity-0 open:starting:translate-y-4 open:starting:scale-[0.96] open:backdrop:bg-tm07-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div class="relative">
      <button type="button" data-tm07-close aria-label="Close popup" class="absolute right-3 top-3 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tm07-cardmut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-black/5 hover:text-tm07-oncard focus-visible:outline-2 focus-visible:outline-tm07-acc focus-visible:outline-offset-2">&times;</button>
      <div class="h-2 w-full bg-linear-to-r from-tm07-acc via-tm07-acc2 to-tm07-acc3"></div>

      <div class="px-8 pt-9 pb-8 text-center">
        <div class="group-data-[state=done]:hidden">
          <p class="mb-2 text-xs font-bold uppercase tracking-[0.2em] text-tm07-acc">Members get 15% off</p>
          <h2 id="tm-07-title" class="mb-2 text-[26px] font-extrabold leading-tight tracking-tight">Unlock your welcome code</h2>
          <p class="mb-6 text-sm leading-relaxed text-tm07-cardmut">Join the list for first access to drops and a coupon in your inbox today.</p>
          <form data-tm07-form class="flex flex-col gap-3">
            <label for="tm-07-email" class="sr-only">Email address</label>
            <input id="tm-07-email" type="email" required placeholder="[email protected]" class="w-full min-h-12 px-4 rounded-xl border border-tm07-cardedge bg-white text-[15px] text-tm07-oncard placeholder:text-tm07-cardfaint transition-[border-color,box-shadow] duration-200 focus:border-tm07-acc focus:outline-none focus:ring-4 focus:ring-tm07-ring user-invalid:border-tm07-bad">
            <button type="submit" class="w-full min-h-12 rounded-xl border-0 bg-tm07-oncard text-[15px] font-bold text-white cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tm07-btnink active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tm07-acc motion-reduce:active:translate-y-0">Claim my 15% off</button>
          </form>
          <p class="mt-4 text-[11px] text-tm07-cardfaint">No spam. Unsubscribe anytime.</p>
        </div>

        <div aria-live="polite" class="hidden group-data-[state=done]:block">
          <div aria-hidden="true" class="grid place-items-center size-14 mx-auto mb-4 rounded-2xl bg-tm07-oktint text-2xl text-tm07-ok">&#10003;</div>
          <h2 class="mb-2 text-[26px] font-extrabold leading-tight tracking-tight">You&#39;re in</h2>
          <p class="mb-6 text-sm leading-relaxed text-tm07-cardmut">Your code <b data-tm07-code class="font-tm07-mono font-semibold text-tm07-oncard">WELCOME15</b> is on its way to <span data-tm07-mail class="font-semibold text-tm07-oncard">your inbox</span>.</p>
          <button type="button" data-tm07-done class="w-full min-h-12 rounded-xl border-0 bg-tm07-oncard text-[15px] font-bold text-white cursor-pointer transition-[background-color] duration-200 hover:bg-tm07-btnink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tm07-acc">Start shopping</button>
        </div>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm07-bg: #08060b;
  --color-tm07-bg: oklch(0.14 0.02 300);
  --color-tm07-btn: #1a1424;
  --color-tm07-btn: oklch(0.22 0.03 300);
  --color-tm07-btnhover: #241b32;
  --color-tm07-btnhover: oklch(0.27 0.045 300);
  --color-tm07-edge: #362b47;
  --color-tm07-edge: oklch(0.34 0.05 300);
  --color-tm07-ink: #ece7f3;
  --color-tm07-ink: oklch(0.93 0.015 300);
  --color-tm07-faint: #7d738c;
  --color-tm07-faint: oklch(0.6 0.03 300);
  --color-tm07-card: #fafaf9;
  --color-tm07-card: oklch(0.98 0.002 90);
  --color-tm07-oncard: #1b1a19;
  --color-tm07-oncard: oklch(0.24 0.004 90);
  --color-tm07-btnink: #343230;
  --color-tm07-btnink: oklch(0.34 0.005 90);
  --color-tm07-cardmut: #6f6c68;
  --color-tm07-cardmut: oklch(0.56 0.006 90);
  --color-tm07-cardfaint: #a6a29d;
  --color-tm07-cardfaint: oklch(0.72 0.008 90);
  --color-tm07-cardedge: #d8d5d1;
  --color-tm07-cardedge: oklch(0.87 0.005 90);
  --color-tm07-acc: #c026d3;
  --color-tm07-acc: oklch(0.58 0.25 322);
  --color-tm07-acc2: #e11d6b;
  --color-tm07-acc2: oklch(0.58 0.23 8);
  --color-tm07-acc3: #f5a524;
  --color-tm07-acc3: oklch(0.79 0.16 75);
  --color-tm07-ring: #c026d333;
  --color-tm07-ring: oklch(0.58 0.25 322 / 0.2);
  --color-tm07-ok: #16794a;
  --color-tm07-ok: oklch(0.5 0.13 155);
  --color-tm07-oktint: #d7f2e3;
  --color-tm07-oktint: oklch(0.93 0.06 155);
  --color-tm07-bad: #c2410c;
  --color-tm07-bad: oklch(0.55 0.18 40);
  --color-tm07-scrim: #06060a99;
  --color-tm07-scrim: oklch(0.12 0.01 300 / 0.6);
  --font-tm07-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm07-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tm-07 {
  width: 100%;
}

#tm-07-dlg::backdrop {
  background: oklch(0.12 0.01 300 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-07-dlg[open]::backdrop {
    background: oklch(0.12 0.01 300 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-07');
  var dlg = root.querySelector('#tm-07-dlg');
  var KEY = 'tm-07-seen';
  function open() { if (!dlg.open) { dlg.showModal(); try { sessionStorage.setItem(KEY, '1'); } catch (e) {} } }
  root.querySelector('[data-tm07-open]').addEventListener('click', open);
  root.querySelector('[data-tm07-close]').addEventListener('click', function () { dlg.close(); });
  root.querySelector('[data-tm07-done]').addEventListener('click', function () { dlg.close(); });

  var seen = false;
  try { seen = sessionStorage.getItem(KEY) === '1'; } catch (e) {}
  if (!seen) setTimeout(function () { if (!dlg.open) open(); }, 3000);

  root.querySelector('[data-tm07-form]').addEventListener('submit', function (e) {
    e.preventDefault();
    root.querySelector('[data-tm07-mail]').textContent = root.querySelector('#tm-07-email').value;
    dlg.dataset.state = 'done';
    root.querySelector('[data-tm07-done]').focus();
  });
  dlg.addEventListener('close', function () { dlg.dataset.state = 'ask'; });
})();
```
