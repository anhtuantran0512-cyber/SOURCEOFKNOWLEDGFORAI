---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-hipaa-consent-modal-scroll-gated-agreement/"
title: "Tailwind HIPAA Patient Consent Modal with Scroll-Gated Agreement"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A patient authorization sheet whose entrance is deliberately nothing: a 200ms opacity fade, no transform, because decorative motion measurably lowers…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind HIPAA Patient Consent Modal with Scroll-Gated Agreement
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-hipaa-consent-modal-scroll-gated-agreement/

A patient authorization sheet whose entrance is deliberately nothing: a 200ms opacity fade, no transform, because decorative motion measurably lowers perceived security on medical consent. The port's real work is the gate — has-[#tw-05-agree:checked]: plus a scroll flag turns the consent button on only when the patient has both read and agreed.
## HTML
```html
<section class="tw-05 w-full min-h-svh grid place-items-center bg-tw05-bg font-tw05-sans px-6 py-10">
  <button type="button" data-tw05-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-[9px] border-0 text-[15px] font-semibold text-white bg-tw05-brand shadow-[0_8px_20px_-6px_var(--color-tw05-glow)] cursor-pointer transition-colors duration-200 hover:bg-tw05-brandhover focus-visible:outline-2 focus-visible:outline-tw05-brand focus-visible:outline-offset-2">Start telehealth visit</button>

  <dialog id="tw-05-dlg" aria-labelledby="tw-05-title" class="group m-auto w-[min(520px,94vw)] p-0 border-0 rounded-[14px] text-left text-tw05-ink bg-tw05-card shadow-[0_30px_60px_-20px_#0f172a47] opacity-0 transition-[opacity,overlay,display] duration-200 transition-discrete open:opacity-100 open:starting:opacity-0 open:backdrop:bg-tw05-scrim open:backdrop:backdrop-blur-[4px]">
    <div class="relative px-8 pt-8 pb-6">
      <button type="button" data-tw05-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tw05-sub text-base cursor-pointer transition-colors duration-200 hover:bg-tw05-well hover:text-tw05-ink focus-visible:outline-2 focus-visible:outline-tw05-brand focus-visible:outline-offset-2">&#10005;</button>

      <p class="inline-flex items-center gap-2 mb-4 px-3 py-1.5 rounded-full bg-tw05-tint text-xs font-semibold tracking-wide text-tw05-brand"><span aria-hidden="true">&#9877;</span>HIPAA-compliant consent · Form v2.3</p>
      <h2 id="tw-05-title" class="mb-2 text-[1.3rem] font-extrabold tracking-[-0.015em] leading-tight">Authorization to share medical information</h2>
      <p class="mb-[18px] text-sm leading-relaxed text-tw05-sub text-pretty">Please review before your telehealth visit. This authorization is required to connect you with a licensed provider.</p>

      <div tabindex="0" data-tw05-body aria-label="Consent text, scroll to read in full" class="max-h-[220px] overflow-y-auto overscroll-contain mb-[18px] px-[18px] py-4 rounded-[9px] border border-tw05-line bg-tw05-well focus-visible:outline-2 focus-visible:outline-tw05-brand focus-visible:outline-offset-2">
        <h3 class="mb-1.5 text-[0.85rem] font-bold text-tw05-ink">What we collect and share</h3>
        <p class="text-[13px] leading-relaxed text-tw05-sub">To provide telehealth services, we collect: your date of birth, insurance ID, symptom description, current medications, and appointment history. We share this with your assigned provider and, when medically necessary, with your primary care physician.</p>
        <h3 class="mt-3.5 mb-1.5 text-[0.85rem] font-bold text-tw05-ink">Your rights under HIPAA</h3>
        <p class="text-[13px] leading-relaxed text-tw05-sub">You have the right to (1) access your PHI, (2) request amendments, (3) receive an accounting of disclosures, and (4) file a complaint. Read the full <a href="#" class="text-tw05-brand underline">Notice of Privacy Practices</a> and <a href="#" class="text-tw05-brand underline">Rights Under HIPAA</a>.</p>
        <h3 class="mt-3.5 mb-1.5 text-[0.85rem] font-bold text-tw05-ink">Withdrawing consent</h3>
        <p class="text-[13px] leading-relaxed text-tw05-sub">You may withdraw this authorization at any time by contacting our Privacy Officer at <a href="#" class="text-tw05-brand underline">[email protected]</a>. Withdrawal is effective going forward and does not affect PHI already disclosed.</p>
      </div>

      <div class="group/gate" data-tw05-gate>
        <label class="flex items-start gap-2.5 mb-2.5 py-1 text-[13.5px] leading-relaxed cursor-pointer">
          <input type="checkbox" id="tw-05-agree" required class="shrink-0 mt-0.5 size-4 accent-tw05-good cursor-pointer focus-visible:outline-2 focus-visible:outline-tw05-good focus-visible:outline-offset-2">
          <span>I have read and understand this authorization. I consent to the collection and sharing of my PHI as described above for this telehealth visit.</span>
        </label>
        <label class="flex items-start gap-2.5 mb-2.5 py-1 text-[13.5px] leading-relaxed cursor-pointer">
          <input type="checkbox" class="shrink-0 mt-0.5 size-4 accent-tw05-good cursor-pointer focus-visible:outline-2 focus-visible:outline-tw05-good focus-visible:outline-offset-2">
          <span>Optional: send me appointment reminders and health tips (separate consent)</span>
        </label>

        <div class="grid grid-cols-2 gap-2.5 mt-3.5">
          <button type="button" data-tw05-close class="min-h-11 rounded-[9px] border-0 text-sm font-bold text-tw05-ink bg-tw05-well2 cursor-pointer transition-colors duration-200 hover:bg-tw05-well3 focus-visible:outline-2 focus-visible:outline-tw05-ink focus-visible:outline-offset-2">I don't consent</button>
          <button type="button" data-tw05-close disabled class="min-h-11 rounded-[9px] border-0 text-sm font-bold text-white bg-tw05-good cursor-pointer transition-colors duration-200 hover:bg-tw05-goodhover focus-visible:outline-2 focus-visible:outline-tw05-good focus-visible:outline-offset-2 disabled:bg-tw05-well3 disabled:text-tw05-sub disabled:cursor-not-allowed group-has-[#tw-05-agree:checked]/gate:group-data-[read=true]/gate:enabled:bg-tw05-good">Sign and begin visit</button>
        </div>
        <p class="mt-2.5 text-xs text-tw05-sub group-data-[read=true]/gate:has-[#tw-05-agree:checked]:invisible">Scroll the authorization to the end and tick the box to continue.</p>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw05-bg: #f0f7fc;
  --color-tw05-bg: oklch(0.97 0.015 235);
  --color-tw05-card: #ffffff;
  --color-tw05-card: oklch(1 0 0);
  --color-tw05-well: #fafbfc;
  --color-tw05-well: oklch(0.98 0.003 255);
  --color-tw05-well2: #f1f5f9;
  --color-tw05-well2: oklch(0.96 0.006 250);
  --color-tw05-well3: #e2e8f0;
  --color-tw05-well3: oklch(0.92 0.01 250);
  --color-tw05-ink: #0f172a;
  --color-tw05-ink: oklch(0.23 0.04 265);
  --color-tw05-sub: #52627a;
  --color-tw05-sub: oklch(0.48 0.03 255);
  --color-tw05-line: #dbe3ec;
  --color-tw05-line: oklch(0.9 0.012 245);
  --color-tw05-brand: #2563eb;
  --color-tw05-brand: oklch(0.53 0.2 262);
  --color-tw05-brandhover: #1d4ed8;
  --color-tw05-brandhover: oklch(0.48 0.2 262);
  --color-tw05-tint: #3b82f61a;
  --color-tw05-tint: oklch(0.62 0.19 259 / 0.1);
  --color-tw05-glow: #3b82f680;
  --color-tw05-glow: oklch(0.62 0.19 259 / 0.5);
  --color-tw05-good: #047857;
  --color-tw05-good: oklch(0.52 0.12 164);
  --color-tw05-goodhover: #065f46;
  --color-tw05-goodhover: oklch(0.45 0.1 164);
  --color-tw05-scrim: #0f172a8c;
  --color-tw05-scrim: oklch(0.23 0.04 265 / 0.55);
  --font-tw05-sans: 'Outfit', system-ui, sans-serif;
}

.tw-05 {
  width: 100%;
}

#tw-05-dlg::backdrop {
  background: oklch(0.23 0.04 265 / 0);
  backdrop-filter: blur(0px);
  transition: background .2s ease, backdrop-filter .2s ease, overlay .2s allow-discrete, display .2s allow-discrete;
}

@starting-style {
  #tw-05-dlg[open]::backdrop {
    background: oklch(0.23 0.04 265 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-05-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-05');
  var dlg = root.querySelector('#tw-05-dlg');
  var card = dlg.firstElementChild;
  var body = root.querySelector('[data-tw05-body]');
  var gate = root.querySelector('[data-tw05-gate]');
  var agree = root.querySelector('#tw-05-agree');
  var submit = gate.querySelector('button[disabled], button:last-of-type');

  function markRead() {
    if (body.scrollTop + body.clientHeight >= body.scrollHeight - 4) gate.dataset.read = 'true';
    sync();
  }
  function sync() {
    submit.disabled = !(gate.dataset.read === 'true' && agree.checked);
  }
  body.addEventListener('scroll', markRead);
  agree.addEventListener('change', sync);

  root.querySelector('[data-tw05-open]').addEventListener('click', function () {
    dlg.showModal();
    body.focus();
    // Short consent text may already be fully visible — do not trap the patient.
    markRead();
  });
  root.querySelectorAll('[data-tw05-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
