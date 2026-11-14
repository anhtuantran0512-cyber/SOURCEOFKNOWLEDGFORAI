---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-contact-support-modal-live-validation/"
title: "Tailwind Contact Support Modal with Live Validation"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A support form that opens over the dashboard instead of navigating away: two-column identity fields, a topic select, priority radios and a counted message box."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Contact Support Modal with Live Validation
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-contact-support-modal-live-validation/

A support form that opens over the dashboard instead of navigating away: two-column identity fields, a topic select, priority radios and a counted message box. Validation styling uses user-invalid:, so a field only turns red after the user has actually left it wrong.
## HTML
```html
<section class="tm-16 w-full min-h-svh grid place-items-center bg-tm16-bg font-tm16-sans px-6 py-10">
  <button type="button" data-tm16-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-xl text-[15px] font-semibold text-tm16-ink bg-tm16-btn border border-tm16-btnedge cursor-pointer transition-colors duration-200 hover:bg-tm16-btnhover hover:border-tm16-acc focus-visible:outline-2 focus-visible:outline-tm16-acc focus-visible:outline-offset-2">Contact support</button>

  <dialog id="tm-16-dlg" data-state="form" aria-labelledby="tm-16-title" class="group m-auto w-[min(520px,94vw)] max-h-[92dvh] overflow-auto p-0 border-0 rounded-[20px] text-tm16-ink bg-tm16-card shadow-[0_40px_90px_-30px_#000,0_0_0_1px_var(--color-tm16-edge)] opacity-0 translate-y-3 scale-[0.97] transition-[opacity,translate,scale,overlay,display] duration-[280ms] transition-discrete open:opacity-100 open:translate-y-0 open:scale-100 open:starting:opacity-0 open:starting:translate-y-3 open:starting:scale-[0.97] open:backdrop:bg-tm16-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div class="p-7">
      <header class="flex items-start justify-between gap-4 mb-5">
        <div>
          <h2 id="tm-16-title" class="text-[20px] font-bold text-tm16-hi">Contact support</h2>
          <p class="mt-1 text-[13px] text-tm16-mut">We usually reply within a few hours.</p>
        </div>
        <button type="button" data-tm16-close aria-label="Close" class="grid place-items-center size-11 shrink-0 rounded-lg border-0 bg-transparent text-tm16-mut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm16-well hover:text-white focus-visible:outline-2 focus-visible:outline-tm16-acc focus-visible:outline-offset-2">&times;</button>
      </header>

      <form data-tm16-form novalidate class="flex flex-col gap-4 group-data-[state=sent]:hidden">
        <div class="grid grid-cols-2 gap-3 max-[420px]:grid-cols-1">
          <div>
            <label for="tm-16-name" class="block mb-1.5 text-[12.5px] font-semibold text-tm16-mut">Name</label>
            <input id="tm-16-name" type="text" required autocomplete="name" class="peer w-full min-h-11 px-3.5 rounded-[10px] border border-tm16-edge bg-tm16-well text-sm text-tm16-hi transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm16-acc focus:shadow-[0_0_0_3px_var(--color-tm16-ring)] user-invalid:border-tm16-bad">
            <p class="hidden mt-1 text-[11.5px] text-tm16-bad peer-user-invalid:block">Please enter your name.</p>
          </div>
          <div>
            <label for="tm-16-email" class="block mb-1.5 text-[12.5px] font-semibold text-tm16-mut">Email</label>
            <input id="tm-16-email" type="email" required autocomplete="email" class="peer w-full min-h-11 px-3.5 rounded-[10px] border border-tm16-edge bg-tm16-well text-sm text-tm16-hi transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm16-acc focus:shadow-[0_0_0_3px_var(--color-tm16-ring)] user-invalid:border-tm16-bad">
            <p class="hidden mt-1 text-[11.5px] text-tm16-bad peer-user-invalid:block">Enter a valid email address.</p>
          </div>
        </div>

        <div>
          <label for="tm-16-topic" class="block mb-1.5 text-[12.5px] font-semibold text-tm16-mut">Topic</label>
          <select id="tm-16-topic" required class="w-full min-h-11 px-3 rounded-[10px] border border-tm16-edge bg-tm16-well text-sm text-tm16-hi cursor-pointer transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm16-acc focus:shadow-[0_0_0_3px_var(--color-tm16-ring)] user-invalid:border-tm16-bad">
            <option value="">Choose a topic…</option>
            <option>Billing &amp; plans</option>
            <option>Technical issue</option>
            <option>Feature request</option>
            <option>Something else</option>
          </select>
        </div>

        <fieldset class="border-0 p-0">
          <legend class="mb-1.5 text-[12.5px] font-semibold text-tm16-mut">Priority</legend>
          <div class="flex flex-wrap gap-4">
            <label class="inline-flex items-center gap-2 min-h-11 text-sm text-tm16-ink cursor-pointer"><input type="radio" name="tm-16-p" checked class="size-[18px] accent-tm16-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm16-acc focus-visible:outline-offset-2"> Low</label>
            <label class="inline-flex items-center gap-2 min-h-11 text-sm text-tm16-ink cursor-pointer"><input type="radio" name="tm-16-p" class="size-[18px] accent-tm16-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm16-acc focus-visible:outline-offset-2"> Normal</label>
            <label class="inline-flex items-center gap-2 min-h-11 text-sm text-tm16-ink cursor-pointer"><input type="radio" name="tm-16-p" class="size-[18px] accent-tm16-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm16-acc focus-visible:outline-offset-2"> Urgent</label>
          </div>
        </fieldset>

        <div>
          <label for="tm-16-msg" class="block mb-1.5 text-[12.5px] font-semibold text-tm16-mut">Message</label>
          <textarea id="tm-16-msg" data-tm16-msg required maxlength="500" rows="4" placeholder="Describe what&#39;s happening…" class="peer w-full min-h-28 max-h-60 p-3.5 rounded-[10px] border border-tm16-edge bg-tm16-well text-sm leading-relaxed text-tm16-hi placeholder:text-tm16-faint resize-y [field-sizing:content] transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm16-acc focus:shadow-[0_0_0_3px_var(--color-tm16-ring)] user-invalid:border-tm16-bad"></textarea>
          <div class="flex justify-between mt-1">
            <p class="hidden text-[11.5px] text-tm16-bad peer-user-invalid:block">Tell us what&#39;s happening.</p>
            <p class="ml-auto text-[11.5px] text-tm16-faint"><b data-tm16-count class="text-tm16-mut">0</b>/500</p>
          </div>
        </div>

        <div class="grid grid-cols-[auto_1fr] gap-3 mt-1">
          <button type="button" data-tm16-cancel class="min-h-12 px-5 rounded-xl border border-tm16-btnedge bg-tm16-btn text-sm font-semibold text-tm16-ink cursor-pointer transition-colors duration-200 hover:bg-tm16-btnhover focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Cancel</button>
          <button type="submit" class="min-h-12 rounded-xl border-0 bg-tm16-acc text-[14.5px] font-bold text-tm16-onacc cursor-pointer transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Send message</button>
        </div>
      </form>

      <div role="status" class="hidden text-center group-data-[state=sent]:block">
        <div aria-hidden="true" class="grid place-items-center size-14 mx-auto mb-4 rounded-2xl text-2xl bg-tm16-oktint text-tm16-ok shadow-[inset_0_0_0_1px_var(--color-tm16-okedge)]">✓</div>
        <h3 class="mb-2 text-lg font-bold text-tm16-hi">Message sent</h3>
        <p class="mb-5 text-sm leading-relaxed text-tm16-mut">Thanks &mdash; we&#39;ve logged your request and emailed a copy to your inbox.</p>
        <button type="button" data-tm16-done class="w-full min-h-12 rounded-xl border-0 bg-tm16-acc text-[14.5px] font-bold text-tm16-onacc cursor-pointer transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Close</button>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm16-bg: #08080d;
  --color-tm16-bg: oklch(0.14 0.012 275);
  --color-tm16-card: #15161f;
  --color-tm16-card: oklch(0.21 0.015 275);
  --color-tm16-well: #0e0f18;
  --color-tm16-well: oklch(0.17 0.013 275);
  --color-tm16-btn: #1a1c2a;
  --color-tm16-btn: oklch(0.23 0.02 275);
  --color-tm16-btnhover: #232537;
  --color-tm16-btnhover: oklch(0.27 0.028 275);
  --color-tm16-btnedge: #333552;
  --color-tm16-btnedge: oklch(0.32 0.03 275);
  --color-tm16-edge: #2a2c42;
  --color-tm16-edge: oklch(0.29 0.025 275);
  --color-tm16-hi: #f2f2fb;
  --color-tm16-hi: oklch(0.96 0.008 275);
  --color-tm16-ink: #dcdcec;
  --color-tm16-ink: oklch(0.89 0.015 275);
  --color-tm16-mut: #9c9cba;
  --color-tm16-mut: oklch(0.71 0.025 275);
  --color-tm16-faint: #7c7c9a;
  --color-tm16-faint: oklch(0.6 0.03 275);
  --color-tm16-acc: #8aa0ff;
  --color-tm16-acc: oklch(0.73 0.15 272);
  --color-tm16-onacc: #070a1f;
  --color-tm16-onacc: oklch(0.17 0.05 272);
  --color-tm16-ring: #8aa0ff3d;
  --color-tm16-ring: oklch(0.73 0.15 272 / 0.24);
  --color-tm16-bad: #f08a8a;
  --color-tm16-bad: oklch(0.72 0.15 22);
  --color-tm16-ok: #7ae2a8;
  --color-tm16-ok: oklch(0.85 0.16 155);
  --color-tm16-oktint: #142a1f;
  --color-tm16-oktint: oklch(0.25 0.05 155);
  --color-tm16-okedge: #37785a;
  --color-tm16-okedge: oklch(0.48 0.09 155);
  --color-tm16-scrim: #08080da3;
  --color-tm16-scrim: oklch(0.12 0.01 275 / 0.64);
  --font-tm16-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tm-16 {
  width: 100%;
}

#tm-16-dlg::backdrop {
  background: oklch(0.12 0.01 275 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-16-dlg[open]::backdrop {
    background: oklch(0.12 0.01 275 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-16');
  var dlg = root.querySelector('#tm-16-dlg');
  var form = root.querySelector('[data-tm16-form]');
  var msg = root.querySelector('[data-tm16-msg]');
  var count = root.querySelector('[data-tm16-count]');

  root.querySelector('[data-tm16-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tm16-close]').addEventListener('click', function () { dlg.close(); });
  root.querySelector('[data-tm16-cancel]').addEventListener('click', function () { dlg.close(); });
  root.querySelector('[data-tm16-done]').addEventListener('click', function () { dlg.close(); });
  msg.addEventListener('input', function () { count.textContent = msg.value.length; });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }  // native constraints first
    dlg.dataset.state = 'sent';                                     // values are never cleared
    root.querySelector('[data-tm16-done]').focus();
  });
  dlg.addEventListener('close', function () { dlg.dataset.state = 'form'; });
})();
```
