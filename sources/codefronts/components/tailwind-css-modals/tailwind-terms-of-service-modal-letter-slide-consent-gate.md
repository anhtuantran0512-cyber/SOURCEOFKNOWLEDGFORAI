---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-terms-of-service-modal-letter-slide-consent-gate/"
title: "Tailwind Terms of Service Modal with Letter-Slide and Consent Gate"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "Post-signup legal consent with the collection's most restrained motion: a 20px slide down and a fade, ease-out, no overshoot — a document placed on a desk."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Terms of Service Modal with Letter-Slide and Consent Gate
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-terms-of-service-modal-letter-slide-consent-gate/

Post-signup legal consent with the collection's most restrained motion: a 20px slide down and a fade, ease-out, no overshoot — a document placed on a desk. The gate is the substance: Accept stays disabled until the agreement box is ticked, driven by has-[#tw-17-agree:checked]:, with marketing consent kept separate.
## HTML
```html
<section class="tw-17 w-full min-h-svh grid place-items-center bg-tw17-bg font-tw17-sans px-6 py-10">
  <button type="button" data-tw17-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-[9px] border-0 bg-tw17-ink text-[15px] font-semibold text-white cursor-pointer transition-colors duration-200 hover:bg-tw17-inkhover focus-visible:outline-2 focus-visible:outline-tw17-ink focus-visible:outline-offset-2">Complete signup</button>

  <dialog id="tw-17-dlg" aria-labelledby="tw-17-title" class="m-auto w-[min(520px,94vw)] p-0 border-0 rounded-[14px] text-left text-tw17-ink bg-tw17-card shadow-[0_30px_60px_-20px_#0f172a47] opacity-0 -translate-y-5 transition-[opacity,translate,overlay,display] duration-[320ms] ease-out transition-discrete open:opacity-100 open:translate-y-0 open:starting:opacity-0 open:starting:-translate-y-5 open:backdrop:bg-tw17-scrim open:backdrop:backdrop-blur-[4px] motion-reduce:transition-[opacity] motion-reduce:translate-y-0">
    <div class="relative px-8 pt-8 pb-6">
      <button type="button" data-tw17-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-base text-tw17-sub cursor-pointer transition-colors duration-200 hover:bg-tw17-well2 hover:text-tw17-ink focus-visible:outline-2 focus-visible:outline-tw17-ink focus-visible:outline-offset-2">&#10005;</button>

      <p class="inline-block mb-3.5 px-3 py-1.5 rounded-full bg-tw17-well2 font-tw17-mono text-xs font-bold text-tw17-sub">Terms v3.2 · Updated 2026-07-15</p>
      <h2 id="tw-17-title" class="mb-2 text-[1.3rem] font-extrabold tracking-[-0.015em] leading-tight">Terms of Service &amp; Privacy Policy</h2>
      <p class="mb-[18px] text-sm leading-relaxed text-tw17-sub">Please review before continuing. Your acceptance is required to use Northlight.</p>

      <div tabindex="0" aria-label="Terms of Service, scroll to read in full" class="max-h-[230px] overflow-y-auto overscroll-contain mb-[18px] px-[18px] py-4 rounded-[9px] border border-tw17-line bg-tw17-well focus-visible:outline-2 focus-visible:outline-tw17-ink focus-visible:outline-offset-2">
        <h3 class="mb-1.5 text-[0.85rem] font-bold">1. Acceptance of terms</h3>
        <p class="text-[13px] leading-relaxed text-tw17-sub">By accessing Northlight ("the Service"), you agree to be bound by these Terms of Service and our Privacy Policy. If you disagree with any part, do not use the Service.</p>
        <h3 class="mt-3 mb-1.5 text-[0.85rem] font-bold">2. Your account</h3>
        <p class="text-[13px] leading-relaxed text-tw17-sub">You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account. You must notify us immediately of any unauthorized use.</p>
        <h3 class="mt-3 mb-1.5 text-[0.85rem] font-bold">3. Data collection &amp; use</h3>
        <p class="text-[13px] leading-relaxed text-tw17-sub">We collect and process personal data as described in our <a href="#" class="font-semibold text-tw17-ink underline">Privacy Policy</a>. This includes account details, usage analytics, and content you create. We do not sell your data to third parties.</p>
        <h3 class="mt-3 mb-1.5 text-[0.85rem] font-bold">4. Content ownership</h3>
        <p class="text-[13px] leading-relaxed text-tw17-sub">You retain ownership of content you create in the Service. By using the Service, you grant Northlight a limited license to store, process, and display your content for the purpose of providing the Service.</p>
        <h3 class="mt-3 mb-1.5 text-[0.85rem] font-bold">5. Termination</h3>
        <p class="text-[13px] leading-relaxed text-tw17-sub">You may terminate your account at any time. We may suspend or terminate accounts that violate these Terms. Upon termination, we will delete your data within 30 days per GDPR Article 17.</p>
      </div>

      <div class="group/gate">
        <label class="flex items-start gap-2.5 mb-2.5 py-1 text-[13.5px] leading-relaxed cursor-pointer">
          <input type="checkbox" id="tw-17-agree" required class="shrink-0 mt-0.5 size-4 accent-tw17-good cursor-pointer focus-visible:outline-2 focus-visible:outline-tw17-good focus-visible:outline-offset-2">
          <span>I have read and agree to the <a href="#" class="font-semibold text-tw17-ink underline">Terms of Service</a> and <a href="#" class="font-semibold text-tw17-ink underline">Privacy Policy</a></span>
        </label>
        <label class="flex items-start gap-2.5 mb-2.5 py-1 text-[13.5px] leading-relaxed cursor-pointer">
          <input type="checkbox" class="shrink-0 mt-0.5 size-4 accent-tw17-good cursor-pointer focus-visible:outline-2 focus-visible:outline-tw17-good focus-visible:outline-offset-2">
          <span>Send me product updates and newsletter (separate, optional consent)</span>
        </label>

        <div class="grid grid-cols-2 gap-2.5 mt-3.5">
          <button type="button" data-tw17-close class="min-h-11 rounded-[9px] border-0 bg-tw17-well2 text-sm font-bold text-tw17-ink cursor-pointer transition-colors duration-200 hover:bg-tw17-well3 focus-visible:outline-2 focus-visible:outline-tw17-ink focus-visible:outline-offset-2">Decline</button>
          <button type="button" data-tw17-accept data-tw17-close disabled class="min-h-11 rounded-[9px] border-0 bg-tw17-good text-sm font-bold text-white cursor-pointer transition-colors duration-200 hover:bg-tw17-goodhover focus-visible:outline-2 focus-visible:outline-tw17-good focus-visible:outline-offset-2 disabled:bg-tw17-well3 disabled:text-tw17-sub disabled:cursor-not-allowed">Accept &amp; continue</button>
        </div>
        <p class="mt-2.5 text-xs text-tw17-sub group-has-[#tw-17-agree:checked]/gate:invisible">Tick the agreement box to enable Accept.</p>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw17-bg: #f8fafc;
  --color-tw17-bg: oklch(0.98 0.005 250);
  --color-tw17-card: #ffffff;
  --color-tw17-card: oklch(1 0 0);
  --color-tw17-well: #fafbfc;
  --color-tw17-well: oklch(0.98 0.003 255);
  --color-tw17-well2: #f1f5f9;
  --color-tw17-well2: oklch(0.96 0.006 250);
  --color-tw17-well3: #e2e8f0;
  --color-tw17-well3: oklch(0.92 0.01 250);
  --color-tw17-ink: #0f172a;
  --color-tw17-ink: oklch(0.23 0.04 265);
  --color-tw17-inkhover: #1e293b;
  --color-tw17-inkhover: oklch(0.3 0.03 258);
  --color-tw17-sub: #52627a;
  --color-tw17-sub: oklch(0.48 0.03 255);
  --color-tw17-line: #e2e8f0;
  --color-tw17-line: oklch(0.92 0.01 250);
  --color-tw17-good: #047857;
  --color-tw17-good: oklch(0.52 0.12 164);
  --color-tw17-goodhover: #065f46;
  --color-tw17-goodhover: oklch(0.45 0.1 164);
  --color-tw17-scrim: #0f172a8c;
  --color-tw17-scrim: oklch(0.23 0.04 265 / 0.55);
  --font-tw17-sans: 'Outfit', system-ui, sans-serif;
  --font-tw17-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tw-17 {
  width: 100%;
}

#tw-17-dlg::backdrop {
  background: oklch(0.23 0.04 265 / 0);
  backdrop-filter: blur(0px);
  transition: background .2s ease, backdrop-filter .2s ease, overlay .2s allow-discrete, display .2s allow-discrete;
}

@starting-style {
  #tw-17-dlg[open]::backdrop {
    background: oklch(0.23 0.04 265 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-17-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-17');
  var dlg = root.querySelector('#tw-17-dlg');
  var card = dlg.firstElementChild;
  var agree = root.querySelector('#tw-17-agree');
  var accept = root.querySelector('[data-tw17-accept]');

  agree.addEventListener('change', function () { accept.disabled = !agree.checked; });

  root.querySelector('[data-tw17-open]').addEventListener('click', function () {
    dlg.showModal();
    dlg.querySelector('[tabindex="0"]').focus();
  });
  root.querySelectorAll('[data-tw17-close]').forEach(function (b) {
    // Production: log the accepted version, timestamp, IP and user agent here.
    b.addEventListener('click', function () { dlg.close(); });
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
