---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-shipping-address-form-autocomplete/"
title: "Tailwind Shipping Address Form with Autocomplete"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's address form, ported one-for-one to Tailwind v4: correct autocomplete tokens so browsers fill every field in one tap, an ARIA 1.2…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shipping Address Form with Autocomplete
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-shipping-address-form-autocomplete/

The CSS collection's address form, ported one-for-one to Tailwind v4: correct autocomplete tokens so browsers fill every field in one tap, an ARIA 1.2 combobox that suggests full addresses with the match highlighted, a map header whose pin hops when an address is chosen, country-aware ZIP / Postcode / Postal code labels and patterns for all five Tier-1 markets, and delivery-speed cards with live arrival dates.
## HTML
```html
<div class="tf-04 relative block min-h-svh w-full bg-tf04-bg pt-[72px] font-tf04-sans leading-[normal] text-tf04-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="w-full max-w-[36rem] overflow-hidden rounded-3xl border border-tf04-line bg-tf04-surface shadow-[0_30px_60px_-35px_rgba(16,32,22,.45)]" role="form" aria-labelledby="tf-04-title">
      <div class="relative h-36 border-b border-tf04-line [background:radial-gradient(circle_at_50%_60%,color-mix(in_oklab,var(--color-tf04-accent)_18%,transparent),transparent_40%),repeating-linear-gradient(28deg,transparent_0_34px,color-mix(in_oklab,var(--color-tf04-line)_90%,var(--color-tf04-ink)_6%)_34px_36px),repeating-linear-gradient(-62deg,transparent_0_58px,color-mix(in_oklab,var(--color-tf04-line)_90%,var(--color-tf04-ink)_6%)_58px_61px),linear-gradient(160deg,var(--color-tf04-soft),color-mix(in_oklab,var(--color-tf04-accent)_8%,var(--color-tf04-soft)))] after:absolute after:top-[62%] after:-right-[5%] after:-left-[5%] after:h-[10px] after:-rotate-6 after:bg-tf04-surface/80 after:shadow-[0_0_0_1px_var(--color-tf04-line)] after:content-['']" aria-hidden="true"><span class="absolute top-[22%] left-1/2 z-2 size-7 -translate-x-1/2 -rotate-45 animate-tf04-drop rounded-[50%_50%_50%_0] bg-tf04-accent shadow-[0_6px_12px_-4px_color-mix(in_oklab,var(--color-tf04-accent)_70%,black)] in-[.is-filled]:animate-tf04-hop after:absolute after:inset-[30%] after:rounded-full after:bg-tf04-surface after:content-['']"></span><span class="absolute top-[calc(22%+1.9rem)] left-1/2 z-1 h-[.4rem] w-4 -translate-x-1/2 animate-tf04-pulse rounded-[50%] bg-tf04-accent/50"></span></div>
      <div class="grid gap-[1.1rem] p-[clamp(1.25rem,5vw,2.25rem)]">
        <h2 id="tf-04-title" class="text-[clamp(1.5rem,4vw,1.85rem)] font-bold tracking-[-.025em]">Where should we send it?</h2>
        <p class="-mt-[.6rem] mb-[.1rem] text-tf04-muted">Start typing your address — or fill it in manually.</p>
        <div class="group/f relative grid gap-[.4rem]">
          <label for="tf-04-country" class="text-[.85rem] font-semibold">Country / region</label>
          <select id="tf-04-country" autocomplete="shipping country" class="min-h-12 w-full rounded-[.8rem] border border-tf04-line bg-tf04-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf04-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf04)] focus-visible:border-tf04-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf04-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf04-bad cursor-pointer appearance-none bg-[image:var(--tf04-chevron)] bg-[length:1.1rem] bg-[position:right_.8rem_center] bg-no-repeat pr-10">
            <option value="US">United States</option><option value="GB">United Kingdom</option><option value="CA">Canada</option><option value="AU">Australia</option><option value="NZ">New Zealand</option>
          </select>
        </div>
        <div class="group/f relative grid gap-[.4rem]">
          <label for="tf-04-line1" class="text-[.85rem] font-semibold">Street address</label>
          <div class="relative">
            <svg viewBox="0 0 24 24" aria-hidden="true" class="pointer-events-none absolute top-1/2 left-[.9rem] size-[1.1rem] -translate-y-1/2 fill-none stroke-tf04-muted stroke-[1.8] [stroke-linecap:round]"><circle cx="11" cy="11" r="6.5"/><path d="m20 20-4-4"/></svg>
            <input id="tf-04-line1" type="text" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="tf-04-list" autocomplete="shipping address-line1" placeholder="Start typing, e.g. 1 Market" required class="min-h-12 w-full rounded-[.8rem] border border-tf04-line bg-tf04-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf04-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf04)] focus-visible:border-tf04-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf04-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf04-bad pl-[2.6rem]">
          </div>
          <ul id="tf-04-list" class="absolute inset-x-0 top-[calc(100%+.35rem)] z-10 m-0 max-h-64 animate-tf04-pop list-none overflow-auto rounded-2xl border border-tf04-line bg-tf04-surface p-[.35rem] shadow-[0_20px_40px_-18px_rgba(0,0,0,.35)] *:grid *:cursor-pointer *:grid-cols-[auto_1fr] *:gap-x-[.7rem] *:gap-y-[.15rem] *:rounded-[.7rem] *:px-3 *:py-[.65rem] *:before:row-span-2 *:before:size-[1.9rem] *:before:self-center *:before:rounded-[.55rem] *:before:bg-tf04-soft *:before:bg-[image:var(--tf04-pin)] *:before:bg-[length:1rem] *:before:bg-center *:before:bg-no-repeat *:before:content-[''] *:hover:bg-tf04-soft *:aria-selected:bg-tf04-soft *:aria-selected:shadow-[inset_3px_0_0_var(--color-tf04-accent)] forced-colors:*:aria-selected:bg-[Highlight] forced-colors:*:aria-selected:text-[HighlightText] [&_.tf-04\_\_none]:block [&_.tf-04\_\_none]:cursor-default [&_.tf-04\_\_none]:text-tf04-muted [&_.tf-04\_\_none]:before:hidden [&_b]:text-[.95rem] [&_b]:font-semibold [&_mark]:rounded-[.2rem] [&_mark]:bg-tf04-mark [&_mark]:px-[.1rem] [&_mark]:text-inherit [&_small]:text-[.8rem] [&_small]:text-tf04-muted" role="listbox" aria-label="Address suggestions" hidden></ul>
          <p class="sr-only" aria-live="polite" id="tf-04-live"></p>
        </div>
        <div class="group/f relative grid gap-[.4rem]"><label for="tf-04-line2" class="text-[.85rem] font-semibold">Apartment, suite, etc. <span class="ml-1 font-normal text-tf04-muted">Optional</span></label><input id="tf-04-line2" type="text" autocomplete="shipping address-line2" class="min-h-12 w-full rounded-[.8rem] border border-tf04-line bg-tf04-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf04-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf04)] focus-visible:border-tf04-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf04-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf04-bad"></div>
        <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,9rem),1fr))] gap-4">
          <div class="group/f relative grid gap-[.4rem]"><label for="tf-04-city" class="text-[.85rem] font-semibold">City</label><input id="tf-04-city" type="text" autocomplete="shipping address-level2" required class="min-h-12 w-full rounded-[.8rem] border border-tf04-line bg-tf04-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf04-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf04)] focus-visible:border-tf04-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf04-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf04-bad"></div>
          <div class="group/f relative grid gap-[.4rem]"><label for="tf-04-region" class="tf-04__regionlabel text-[.85rem] font-semibold">State</label><input id="tf-04-region" type="text" autocomplete="shipping address-level1" required class="min-h-12 w-full rounded-[.8rem] border border-tf04-line bg-tf04-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf04-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf04)] focus-visible:border-tf04-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf04-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf04-bad"></div>
          <div class="group/f relative grid gap-[.4rem]"><label for="tf-04-zip" class="tf-04__ziplabel text-[.85rem] font-semibold">ZIP code</label><input id="tf-04-zip" type="text" autocomplete="shipping postal-code" required pattern="\d{5}(-\d{4})?" placeholder="94103" aria-describedby="tf-04-zip-err" class="min-h-12 w-full rounded-[.8rem] border border-tf04-line bg-tf04-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf04-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf04)] focus-visible:border-tf04-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf04-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf04-bad"><p class="hidden text-[.78rem] text-tf04-bad group-has-[input:user-invalid]/f:block" id="tf-04-zip-err">Enter a valid <span class="tf-04__zipname">ZIP code</span>.</p></div>
        </div>
        <fieldset class="grid gap-[.55rem]">
          <legend class="mb-[.55rem] text-[.85rem] font-semibold">Delivery speed</legend>
          <label class="tf-04__opt-card group/o relative grid cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-[.85rem] rounded-2xl border border-tf04-line px-4 py-[.85rem] text-[.85rem] font-normal [transition:border-color_.2s,background_.2s,box-shadow_.25s] hover:border-[color-mix(in_oklab,var(--color-tf04-accent)_40%,var(--color-tf04-line))] has-checked:border-tf04-accent has-checked:bg-[color-mix(in_oklab,var(--color-tf04-accent)_6%,var(--color-tf04-surface))] has-checked:shadow-[0_0_0_1px_var(--color-tf04-accent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-tf04-accent forced-colors:has-checked:outline-2 forced-colors:has-checked:outline-[Highlight]"><input type="radio" name="tf-04-speed" data-days="5" checked class="absolute inset-0 m-0 cursor-pointer opacity-0"><span class="size-[1.2rem] rounded-full border-2 border-tf04-line [transition:border_.25s_var(--ease-tf04)] group-has-checked/o:border-[6px] group-has-checked/o:border-tf04-accent" aria-hidden="true"></span><span><b class="block text-[.95rem]">Standard</b><small class="text-[.82rem] text-tf04-muted">Arrives <span class="tf-04__eta"></span></small></span><em class="text-[.92rem] font-semibold not-italic">Free</em></label>
          <label class="tf-04__opt-card group/o relative grid cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-[.85rem] rounded-2xl border border-tf04-line px-4 py-[.85rem] text-[.85rem] font-normal [transition:border-color_.2s,background_.2s,box-shadow_.25s] hover:border-[color-mix(in_oklab,var(--color-tf04-accent)_40%,var(--color-tf04-line))] has-checked:border-tf04-accent has-checked:bg-[color-mix(in_oklab,var(--color-tf04-accent)_6%,var(--color-tf04-surface))] has-checked:shadow-[0_0_0_1px_var(--color-tf04-accent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-tf04-accent forced-colors:has-checked:outline-2 forced-colors:has-checked:outline-[Highlight]"><input type="radio" name="tf-04-speed" data-days="2" class="absolute inset-0 m-0 cursor-pointer opacity-0"><span class="size-[1.2rem] rounded-full border-2 border-tf04-line [transition:border_.25s_var(--ease-tf04)] group-has-checked/o:border-[6px] group-has-checked/o:border-tf04-accent" aria-hidden="true"></span><span><b class="block text-[.95rem]">Express</b><small class="text-[.82rem] text-tf04-muted">Arrives <span class="tf-04__eta"></span></small></span><em class="text-[.92rem] font-semibold not-italic">$9.95</em></label>
          <label class="tf-04__opt-card group/o relative grid cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-[.85rem] rounded-2xl border border-tf04-line px-4 py-[.85rem] text-[.85rem] font-normal [transition:border-color_.2s,background_.2s,box-shadow_.25s] hover:border-[color-mix(in_oklab,var(--color-tf04-accent)_40%,var(--color-tf04-line))] has-checked:border-tf04-accent has-checked:bg-[color-mix(in_oklab,var(--color-tf04-accent)_6%,var(--color-tf04-surface))] has-checked:shadow-[0_0_0_1px_var(--color-tf04-accent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-tf04-accent forced-colors:has-checked:outline-2 forced-colors:has-checked:outline-[Highlight]"><input type="radio" name="tf-04-speed" data-days="1" class="absolute inset-0 m-0 cursor-pointer opacity-0"><span class="size-[1.2rem] rounded-full border-2 border-tf04-line [transition:border_.25s_var(--ease-tf04)] group-has-checked/o:border-[6px] group-has-checked/o:border-tf04-accent" aria-hidden="true"></span><span><b class="block text-[.95rem]">Next day</b><small class="text-[.82rem] text-tf04-muted">Arrives <span class="tf-04__eta"></span></small></span><em class="text-[.92rem] font-semibold not-italic">$19.95</em></label>
        </fieldset>
        <label class="flex min-h-11 cursor-pointer items-center gap-[.6rem] text-[.85rem] font-normal text-tf04-muted"><input type="checkbox" checked class="m-0 size-[1.15rem] accent-tf04-accent"><span>Billing address is the same as shipping</span></label>
        <button class="tf-04__cta min-h-[3.25rem] cursor-pointer rounded-[.9rem] border-0 bg-tf04-accent text-[1rem] font-semibold text-tf04-on shadow-[0_12px_24px_-14px_var(--color-tf04-accent)] [transition:translate_.2s_var(--ease-tf04),filter_.2s] hover:-translate-y-0.5 hover:brightness-108 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf04-ink" type="button">Continue to payment</button>
        <p class="tf-04__status -mt-[.4rem] text-center text-[.85rem] text-tf04-accent empty:hidden" role="status"></p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf04-bg: #e9efe9;
  --color-tf04-surface: #ffffff;
  --color-tf04-soft: #f3f6f3;
  --color-tf04-ink: #102016;
  --color-tf04-muted: #5a6b60;
  --color-tf04-line: #dbe3dc;
  --color-tf04-accent: #0f766e;
  --color-tf04-on: #fff;
  --color-tf04-mark: #ccfbf1;
  --color-tf04-bad: #c2410c;
  --font-tf04-sans: "Albert Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf04: cubic-bezier(0.16,1,0.3,1);
  --animate-tf04-drop: tf04-drop 0.9s cubic-bezier(0.16,1,0.3,1) both;
  --animate-tf04-hop: tf04-hop 0.6s cubic-bezier(0.16,1,0.3,1);
  --animate-tf04-pulse: tf04-pulse 2.2s ease-out infinite;
  --animate-tf04-pop: tf04-pop 0.25s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf04-drop {
    from {
      translate: -50% -60px;
      opacity: 0;
    }
  }

  @keyframes tf04-hop {
    40% {
      translate: -50% -14px;
    }
  }

  @keyframes tf04-pulse {
    from {
      scale: 1;
      opacity: 0.9;
    }

    to {
      scale: 5;
      opacity: 0;
    }
  }

  @keyframes tf04-pop {
    from {
      opacity: 0;
      translate: 0 -6px;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch, plus the two data-URI icons (url() values with
   spaces can't live in an arbitrary class). Dark values override the @theme variables. */

.tf-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
  --tf04-chevron: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%235a6b60' stroke-width='2' stroke-linecap='round'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E");
  --tf04-pin: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230f766e' stroke-width='1.8'%3E%3Cpath d='M12 21s-6-5.3-6-10.5A6 6 0 0 1 18 10.5C18 15.7 12 21 12 21Z'/%3E%3Ccircle cx='12' cy='10.5' r='2'/%3E%3C/svg%3E");
}

.tf-04[data-theme="dark"] {
  color-scheme: dark;
  --color-tf04-bg: #0b1310;
  --color-tf04-surface: #111c17;
  --color-tf04-soft: #16241e;
  --color-tf04-ink: #e3efe8;
  --color-tf04-muted: #8da397;
  --color-tf04-line: #24362d;
  --color-tf04-accent: #2dd4bf;
  --color-tf04-on: #032420;
  --color-tf04-mark: #134e4a;
  --color-tf04-bad: #fb923c;
}

@media (prefers-color-scheme: dark) {
  .tf-04:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf04-bg: #0b1310;
    --color-tf04-surface: #111c17;
    --color-tf04-soft: #16241e;
    --color-tf04-ink: #e3efe8;
    --color-tf04-muted: #8da397;
    --color-tf04-line: #24362d;
    --color-tf04-accent: #2dd4bf;
    --color-tf04-on: #032420;
    --color-tf04-mark: #134e4a;
    --color-tf04-bad: #fb923c;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-04').forEach((root) => {
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
  const root = document.querySelector('.tf-04');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const ADDRESSES = [
    { c: 'US', line1: '1 Market Street', city: 'San Francisco', region: 'CA', zip: '94105' },
    { c: 'US', line1: '1600 Amphitheatre Parkway', city: 'Mountain View', region: 'CA', zip: '94043' },
    { c: 'US', line1: '350 Fifth Avenue', city: 'New York', region: 'NY', zip: '10118' },
    { c: 'US', line1: '233 South Wacker Drive', city: 'Chicago', region: 'IL', zip: '60606' },
    { c: 'GB', line1: '10 Downing Street', city: 'London', region: 'Greater London', zip: 'SW1A 2AA' },
    { c: 'GB', line1: '221B Baker Street', city: 'London', region: 'Greater London', zip: 'NW1 6XE' },
    { c: 'GB', line1: '1 Princes Street', city: 'Edinburgh', region: 'Midlothian', zip: 'EH2 2EQ' },
    { c: 'CA', line1: '290 Bremner Boulevard', city: 'Toronto', region: 'ON', zip: 'M5V 3L9' },
    { c: 'CA', line1: '1 Market Square', city: 'Saint John', region: 'NB', zip: 'E2L 4Z6' },
    { c: 'AU', line1: '1 Macquarie Street', city: 'Sydney', region: 'NSW', zip: '2000' },
    { c: 'AU', line1: '10 Market Lane', city: 'Melbourne', region: 'VIC', zip: '3000' },
    { c: 'NZ', line1: '1 Queen Street', city: 'Auckland', region: 'Auckland', zip: '1010' }
  ];
  const COUNTRY = {
    US: { zip: 'ZIP code', ph: '94103', re: '\\d{5}(-\\d{4})?', region: 'State' },
    GB: { zip: 'Postcode', ph: 'SW1A 1AA', re: '[A-Za-z]{1,2}\\d[A-Za-z\\d]? ?\\d[A-Za-z]{2}', region: 'County' },
    CA: { zip: 'Postal code', ph: 'K1A 0B1', re: '[A-Za-z]\\d[A-Za-z] ?\\d[A-Za-z]\\d', region: 'Province' },
    AU: { zip: 'Postcode', ph: '2000', re: '\\d{4}', region: 'State / territory' },
    NZ: { zip: 'Postcode', ph: '1010', re: '\\d{4}', region: 'Region' }
  };
  const input = $('#tf-04-line1'), list = $('#tf-04-list'), live = $('#tf-04-live'), country = $('#tf-04-country');
  let results = [], active = -1;
  const esc = (s) => s.replace(/[&<>"]/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[ch]);
  const hl = (text, q) => { const i = text.toLowerCase().indexOf(q.toLowerCase()); return i < 0 ? esc(text) : esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length)); };
  const close = () => { list.hidden = true; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant'); active = -1; };
  const setActive = (i) => {
    active = i;
    list.querySelectorAll('[role="option"]').forEach((li, j) => li.setAttribute('aria-selected', j === i));
    if (i >= 0) { input.setAttribute('aria-activedescendant', 'tf-04-opt-' + i); const el = list.children[i]; if (el) list.scrollTop = Math.max(0, el.offsetTop - list.clientHeight + el.offsetHeight); }
  };
  const open = () => {
    const q = input.value.trim();
    if (q.length < 2) { close(); return; }
    results = ADDRESSES.filter((a) => a.c === country.value && (a.line1 + ' ' + a.city).toLowerCase().includes(q.toLowerCase())).slice(0, 6);
    list.innerHTML = results.length
      ? results.map((a, i) => '<li role="option" id="tf-04-opt-' + i + '" aria-selected="false"><b>' + hl(a.line1, q) + '</b><small>' + esc(a.city + ', ' + a.region + ' ' + a.zip) + '</small></li>').join('')
      : '<li class="tf-04__none" role="option" aria-disabled="true">No matches — keep typing or enter manually.</li>';
    list.hidden = false; input.setAttribute('aria-expanded', 'true');
    live.textContent = results.length ? results.length + ' suggestions. Use up and down arrows to review.' : 'No suggestions.';
    setActive(-1);
  };
  const pick = (i) => {
    const a = results[i]; if (!a) return;
    input.value = a.line1; $('#tf-04-city').value = a.city; $('#tf-04-region').value = a.region; $('#tf-04-zip').value = a.zip;
    close(); live.textContent = 'Address filled: ' + a.line1 + ', ' + a.city;
    root.classList.remove('is-filled'); void root.offsetWidth; root.classList.add('is-filled');
    $('#tf-04-line2').focus();
  };
  input.addEventListener('input', open);
  input.addEventListener('keydown', (e) => {
    if (list.hidden && e.key === 'ArrowDown') { open(); return; }
    if (e.key === 'ArrowDown') { e.preventDefault(); setActive(Math.min(results.length - 1, active + 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(Math.max(0, active - 1)); }
    else if (e.key === 'Enter' && active >= 0) { e.preventDefault(); pick(active); }
    else if (e.key === 'Escape') close();
  });
  list.addEventListener('mousedown', (e) => { const li = e.target.closest('[id^="tf-04-opt-"]'); if (li) { e.preventDefault(); pick(Number(li.id.split('-').pop())); } });
  input.addEventListener('blur', () => setTimeout(close, 120));
  const applyCountry = () => {
    const c = COUNTRY[country.value], zip = $('#tf-04-zip');
    $('.tf-04__ziplabel').textContent = c.zip; $('.tf-04__zipname').textContent = c.zip;
    $('.tf-04__regionlabel').textContent = c.region; zip.placeholder = c.ph; zip.pattern = c.re;
  };
  country.addEventListener('change', () => { applyCountry(); close(); });
  applyCountry();
  const d = new Intl.DateTimeFormat('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
  root.querySelectorAll('.tf-04__opt-card').forEach((card) => {
    const days = Number(card.querySelector('input').dataset.days), t = new Date();
    let added = 0; while (added < days) { t.setDate(t.getDate() + 1); if (t.getDay() % 6) added++; }
    card.querySelector('.tf-04__eta').textContent = d.format(t);
  });
  $('.tf-04__cta').addEventListener('click', () => {
    const bad = [...root.querySelectorAll('input[required]')].find((f) => !f.checkValidity());
    if (bad) { bad.focus(); bad.reportValidity(); return; }
    $('.tf-04__status').textContent = 'Address saved. Continuing to payment…';
  });
})();
```
