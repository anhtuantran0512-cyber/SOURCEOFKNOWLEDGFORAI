---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-gdpr-cookie-consent-banner-details-disclosure/"
title: "Tailwind GDPR Cookie Consent Banner with details Disclosure"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A corner consent sheet with equal-weight Accept and Reject, a <details> preferences panel and real toggle switches."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind GDPR Cookie Consent Banner with details Disclosure
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-gdpr-cookie-consent-banner-details-disclosure/

A corner consent sheet with equal-weight Accept and Reject, a <details> preferences panel and real toggle switches. The port deletes state-tracking JavaScript twice over: the disclosure becomes a <details> read by open:, and the slide-in becomes data-in read by data-[in]:.
## HTML
```html
<section class="tm-13 relative w-full min-h-svh px-8 py-8 bg-tm13-bg font-tm13-sans">
  <div class="min-h-[calc(100svh-64px)] grid place-items-center gap-4 content-center">
    <p class="font-tm13-mono text-[13px] tracking-[0.1em] text-tm13-faint">Demo content behind the banner &mdash; the page stays usable.</p>
    <button type="button" data-tm13-reopen hidden class="inline-flex items-center justify-center min-h-11 px-5 rounded-xl border border-tm13-edge bg-tm13-panel text-[13px] font-semibold text-tm13-ink cursor-pointer transition-colors duration-200 hover:border-tm13-acc focus-visible:outline-2 focus-visible:outline-tm13-acc focus-visible:outline-offset-2">Cookie settings</button>
  </div>

  <section data-tm13-banner role="region" aria-label="Cookie consent" class="fixed left-6 bottom-6 z-10 w-[min(420px,calc(100vw-48px))] rounded-2xl bg-tm13-card border border-tm13-cardedge shadow-[0_30px_70px_-24px_#000] translate-y-[140%] opacity-0 transition-[translate,opacity] duration-[400ms] ease-[cubic-bezier(0.4,0,0.2,1)] data-[in]:translate-y-0 data-[in]:opacity-100 motion-reduce:transition-none">
    <div class="px-5 pt-5 pb-5">
      <h2 class="mb-2 text-[17px] font-bold text-tm13-hi">We value your privacy</h2>
      <p class="mb-4 text-[13px] leading-relaxed text-tm13-mut">We use cookies to run the site and, with your consent, to analyse traffic and personalise content. <a href="#privacy" class="text-tm13-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tm13-acc focus-visible:outline-offset-2">Cookie Policy</a>.</p>

      <details data-tm13-prefs class="group mb-4 border-t border-tm13-edge">
        <summary class="flex items-center justify-between gap-3 min-h-11 list-none cursor-pointer text-[13px] font-semibold text-tm13-ink focus-visible:outline-2 focus-visible:outline-tm13-acc focus-visible:outline-offset-2 rounded-md">
          Preferences
          <span aria-hidden="true" class="text-tm13-mut transition-transform duration-200 group-open:rotate-180 motion-reduce:transition-none">&#9662;</span>
        </summary>

        <div class="flex flex-col gap-0.5 pb-1">
          <label class="flex items-center justify-between gap-4 py-2.5 cursor-not-allowed">
            <input type="checkbox" checked disabled aria-label="Strictly necessary (always on)" class="peer order-2 shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm13-acc opacity-70 cursor-not-allowed before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-white before:transition-transform before:duration-200 checked:before:translate-x-5 motion-reduce:before:transition-none">
            <span class="order-1 flex flex-col gap-0.5 peer-disabled:opacity-80"><b class="text-[13.5px] font-semibold text-tm13-ink">Strictly necessary</b><small class="text-[11.5px] text-tm13-faint">Required for the site to function.</small></span>
          </label>
          <label class="flex items-center justify-between gap-4 py-2.5 cursor-pointer">
            <input type="checkbox" id="tm-13-an" class="peer order-2 shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm13-off cursor-pointer transition-colors duration-200 checked:bg-tm13-acc before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-tm13-knob before:transition-transform before:duration-200 checked:before:translate-x-5 checked:before:bg-white focus-visible:outline-2 focus-visible:outline-tm13-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
            <span class="order-1 flex flex-col gap-0.5"><b class="text-[13.5px] font-semibold text-tm13-ink">Analytics</b><small class="text-[11.5px] text-tm13-faint">Helps us understand usage.</small></span>
          </label>
          <label class="flex items-center justify-between gap-4 py-2.5 cursor-pointer">
            <input type="checkbox" id="tm-13-mk" class="peer order-2 shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm13-off cursor-pointer transition-colors duration-200 checked:bg-tm13-acc before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-tm13-knob before:transition-transform before:duration-200 checked:before:translate-x-5 checked:before:bg-white focus-visible:outline-2 focus-visible:outline-tm13-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
            <span class="order-1 flex flex-col gap-0.5"><b class="text-[13.5px] font-semibold text-tm13-ink">Marketing</b><small class="text-[11.5px] text-tm13-faint">Personalised offers &amp; ads.</small></span>
          </label>
        </div>

        <button type="button" data-tm13-save class="w-full min-h-11 mb-1 rounded-[10px] border border-tm13-edge bg-tm13-btn text-[13px] font-semibold text-tm13-ink cursor-pointer transition-colors duration-200 hover:bg-tm13-btnhover focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Save choices</button>
      </details>

      <div class="grid grid-cols-2 gap-2">
        <button type="button" data-tm13-reject class="min-h-11 px-3 rounded-[10px] border border-tm13-edge bg-tm13-btn text-[13px] font-semibold text-tm13-ink cursor-pointer transition-colors duration-200 hover:bg-tm13-btnhover focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Reject all</button>
        <button type="button" data-tm13-accept class="min-h-11 px-3 rounded-[10px] border-0 bg-tm13-acc text-[13px] font-bold text-tm13-onacc cursor-pointer transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Accept all</button>
      </div>
    </div>
  </section>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm13-bg: #07080b;
  --color-tm13-bg: oklch(0.15 0.012 260);
  --color-tm13-card: #151a24;
  --color-tm13-card: oklch(0.21 0.017 260);
  --color-tm13-panel: #141822;
  --color-tm13-panel: oklch(0.2 0.016 260);
  --color-tm13-btn: #1a2030;
  --color-tm13-btn: oklch(0.23 0.02 260);
  --color-tm13-btnhover: #232b3d;
  --color-tm13-btnhover: oklch(0.27 0.025 260);
  --color-tm13-edge: #2e3849;
  --color-tm13-edge: oklch(0.32 0.02 260);
  --color-tm13-cardedge: #273041;
  --color-tm13-cardedge: oklch(0.29 0.02 260);
  --color-tm13-off: #2a3342;
  --color-tm13-off: oklch(0.3 0.02 260);
  --color-tm13-knob: #9aa3b4;
  --color-tm13-knob: oklch(0.71 0.018 260);
  --color-tm13-hi: #f1f4fa;
  --color-tm13-hi: oklch(0.96 0.006 260);
  --color-tm13-ink: #dbe1ec;
  --color-tm13-ink: oklch(0.9 0.012 260);
  --color-tm13-mut: #9aa3b4;
  --color-tm13-mut: oklch(0.71 0.018 260);
  --color-tm13-faint: #81899c;
  --color-tm13-faint: oklch(0.64 0.02 260);
  --color-tm13-acc: #7fb0ff;
  --color-tm13-acc: oklch(0.75 0.14 250);
  --color-tm13-onacc: #06101f;
  --color-tm13-onacc: oklch(0.18 0.04 250);
  --font-tm13-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm13-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tm-13 {
  width: 100%;
}
/* Safari still paints a marker on a list-none <summary>. */

.tm-13 summary::-webkit-details-marker {
  display: none;
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-13');
  var banner = root.querySelector('[data-tm13-banner]');
  var reopen = root.querySelector('[data-tm13-reopen]');
  var prefs = root.querySelector('[data-tm13-prefs]');
  var KEY = 'tm-13-consent';

  function store(v) { try { localStorage.setItem(KEY, JSON.stringify(Object.assign({ at: Date.now() }, v))); } catch (e) {} }
  function read() { try { return JSON.parse(localStorage.getItem(KEY)); } catch (e) { return null; } }
  function hide() {
    delete banner.dataset.in;
    setTimeout(function () { banner.style.display = 'none'; }, 400);
    reopen.hidden = false;
  }
  function open() {
    banner.style.display = ''; reopen.hidden = true; prefs.open = false;
    requestAnimationFrame(function () { banner.dataset.in = ''; });
  }

  root.querySelector('[data-tm13-accept]').addEventListener('click', function () {
    store({ necessary: true, analytics: true, marketing: true }); hide();
  });
  root.querySelector('[data-tm13-reject]').addEventListener('click', function () {
    store({ necessary: true, analytics: false, marketing: false }); hide();
  });
  root.querySelector('[data-tm13-save]').addEventListener('click', function () {
    store({
      necessary: true,
      analytics: root.querySelector('#tm-13-an').checked,
      marketing: root.querySelector('#tm-13-mk').checked
    });
    hide();
  });
  reopen.addEventListener('click', open);

  if (read()) { banner.style.display = 'none'; reopen.hidden = false; }
  else requestAnimationFrame(function () { banner.dataset.in = ''; });
})();
```
