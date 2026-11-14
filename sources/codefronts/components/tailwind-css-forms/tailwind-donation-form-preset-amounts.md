---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-donation-form-preset-amounts/"
title: "Tailwind Donation Form with Preset Amounts"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's nonprofit donation form, ported one-for-one to Tailwind v4: a photo cause panel with an animated campaign bar, a one-time/monthly toggle…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Donation Form with Preset Amounts
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-donation-form-preset-amounts/

The CSS collection's nonprofit donation form, ported one-for-one to Tailwind v4: a photo cause panel with an animated campaign bar, a one-time/monthly toggle whose pill slides on has-[[value=monthly]:checked]:before:translate-x-full, four presets paired with concrete impact lines (and their own monthly set), an "Other" amount that auto-selects as you type, an optional fee-cover with the exact extra, a tribute reveal, and a button that always states the total.
## HTML
```html
<div class="tf-11 group/root relative block min-h-svh w-full bg-tf11-bg pt-[72px] font-tf11-sans leading-[normal] text-tf11-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none! motion-reduce:**:before:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3.5rem)]">
    <div class="@container w-full max-w-[60rem]">
      <div class="grid overflow-hidden rounded-[1.75rem] border border-tf11-line bg-tf11-card shadow-[0_40px_80px_-45px_rgba(19,32,23,.5)] @[46rem]:grid-cols-2">
        <div class="relative grid min-h-64 bg-[#5b7a62] text-white">
          <img src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=900&h=900&fit=crop&auto=format&q=70" width="900" height="900" alt="Smiling children gathered together outdoors" loading="lazy" decoding="async" class="size-full object-cover [grid-area:1/1]">
          <div class="grid gap-[.9rem] self-end bg-[linear-gradient(transparent,rgba(8,20,12,.88)_55%)] p-[clamp(1.25rem,4cqi,2.25rem)] [grid-area:1/1]">
            <p class="justify-self-start rounded-full bg-white/18 px-[.7rem] py-[.35rem] text-[.75rem] font-semibold tracking-[.1em] uppercase backdrop-blur-sm">Clean Water Fund</p>
            <h2 class="text-[clamp(1.4rem,4cqi,2rem)] leading-[1.15] font-semibold tracking-[-.02em] text-balance">Every gift brings safe water one step closer.</h2>
            <div class="grid gap-2">
              <div class="h-2 overflow-hidden rounded-full bg-white/22" role="progressbar" aria-valuemin="0" aria-valuemax="250000" aria-valuenow="182400" aria-label="Campaign progress"><i class="block h-full w-[var(--tf-11-p)] animate-tf11-fill rounded-[inherit] bg-[linear-gradient(90deg,#fde68a,#fb923c)] motion-reduce:w-[72.96%]"></i></div>
              <p class="text-[.85rem] font-light opacity-90"><b class="font-semibold">$182,400</b> raised of $250,000 · 2,140 donors</p>
            </div>
          </div>
        </div>
        <div class="grid content-start gap-[1.05rem] p-[clamp(1.25rem,4cqi,2.25rem)]" role="form" aria-labelledby="tf-11-title">
          <h3 id="tf-11-title" class="text-[1.2rem] font-semibold">Choose your gift</h3>
          <fieldset class="relative isolate grid min-w-0 grid-cols-2 rounded-full border border-tf11-line bg-tf11-soft p-[.3rem] before:absolute before:top-[.3rem] before:bottom-[.3rem] before:left-[.3rem] before:-z-1 before:w-[calc(50%-.3rem)] before:rounded-full before:bg-tf11-ink before:[transition:translate_.45s_var(--ease-tf11)] before:content-[''] has-[[value=monthly]:checked]:before:translate-x-full forced-colors:before:bg-[Highlight]">
            <legend class="sr-only">Frequency</legend>
            <label class="relative"><input type="radio" name="tf-11-f" value="once" checked class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 grid-flow-col place-items-center gap-[.35rem] rounded-full text-[.92rem] font-medium text-tf11-muted [transition:color_.3s] peer-checked:text-tf11-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf11-accent">One-time</span></label>
            <label class="relative"><input type="radio" name="tf-11-f" value="monthly" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 grid-flow-col place-items-center gap-[.35rem] rounded-full text-[.92rem] font-medium text-tf11-muted [transition:color_.3s] peer-checked:text-tf11-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf11-accent">Monthly <em class="text-tf11-accent not-italic">♥</em></span></label>
          </fieldset>
          <fieldset class="grid min-w-0 grid-cols-4 gap-2">
            <legend class="sr-only">Amount</legend>
            <label class="group/am relative"><input type="radio" name="tf-11-a" value="25" data-impact="provides a family with a water filter" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid min-h-[3.4rem] place-items-center rounded-2xl border-[1.5px] border-tf11-line text-[1.15rem] font-semibold tabular-nums [transition:all_.25s_var(--ease-tf11)] group-hover/am:border-[color-mix(in_oklab,var(--color-tf11-accent)_45%,var(--color-tf11-line))] peer-checked:scale-103 peer-checked:border-tf11-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf11-accent)_10%,var(--color-tf11-card))] peer-checked:text-tf11-accent peer-checked:shadow-[0_8px_20px_-12px_var(--color-tf11-accent)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf11-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">$25</span></label>
            <label class="group/am relative"><input type="radio" name="tf-11-a" value="50" checked data-impact="gives 10 children clean water for a year" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid min-h-[3.4rem] place-items-center rounded-2xl border-[1.5px] border-tf11-line text-[1.15rem] font-semibold tabular-nums [transition:all_.25s_var(--ease-tf11)] group-hover/am:border-[color-mix(in_oklab,var(--color-tf11-accent)_45%,var(--color-tf11-line))] peer-checked:scale-103 peer-checked:border-tf11-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf11-accent)_10%,var(--color-tf11-card))] peer-checked:text-tf11-accent peer-checked:shadow-[0_8px_20px_-12px_var(--color-tf11-accent)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf11-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">$50</span></label>
            <label class="group/am relative"><input type="radio" name="tf-11-a" value="100" data-impact="trains a local well technician" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid min-h-[3.4rem] place-items-center rounded-2xl border-[1.5px] border-tf11-line text-[1.15rem] font-semibold tabular-nums [transition:all_.25s_var(--ease-tf11)] group-hover/am:border-[color-mix(in_oklab,var(--color-tf11-accent)_45%,var(--color-tf11-line))] peer-checked:scale-103 peer-checked:border-tf11-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf11-accent)_10%,var(--color-tf11-card))] peer-checked:text-tf11-accent peer-checked:shadow-[0_8px_20px_-12px_var(--color-tf11-accent)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf11-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">$100</span></label>
            <label class="group/am relative"><input type="radio" name="tf-11-a" value="250" data-impact="funds a school handwashing station" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid min-h-[3.4rem] place-items-center rounded-2xl border-[1.5px] border-tf11-line text-[1.15rem] font-semibold tabular-nums [transition:all_.25s_var(--ease-tf11)] group-hover/am:border-[color-mix(in_oklab,var(--color-tf11-accent)_45%,var(--color-tf11-line))] peer-checked:scale-103 peer-checked:border-tf11-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf11-accent)_10%,var(--color-tf11-card))] peer-checked:text-tf11-accent peer-checked:shadow-[0_8px_20px_-12px_var(--color-tf11-accent)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf11-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">$250</span></label>
            <label class="relative col-span-full flex items-center rounded-2xl border-[1.5px] border-tf11-line [transition:border-color_.25s] focus-within:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf11-accent)_18%,transparent)] has-[input[type=radio]:checked]:border-tf11-accent has-[input[type=radio]:checked]:bg-[color-mix(in_oklab,var(--color-tf11-accent)_6%,var(--color-tf11-card))]"><input type="radio" name="tf-11-a" value="other" data-impact="goes wherever the need is greatest" aria-label="Other amount" class="absolute inset-0 z-0 m-0 cursor-pointer opacity-0"><span class="pointer-events-none relative z-1 pl-[1.1rem] font-semibold text-tf11-muted" aria-hidden="true">$</span><input type="text" inputmode="decimal" class="tf-11__custom relative z-2 min-h-[3.2rem] min-w-0 flex-1 border-0 bg-transparent pr-4 pl-[.35rem] text-[1.05rem] font-medium text-tf11-ink focus:outline-none" placeholder="Other amount" aria-label="Custom amount in dollars"></label>
          </fieldset>
          <p class="tf-11__impact flex items-center gap-[.6rem] rounded-2xl bg-[color-mix(in_oklab,var(--color-tf11-leaf)_10%,var(--color-tf11-card))] px-4 py-[.8rem] text-[.9rem] leading-[1.4] text-tf11-leaf [&.is-swap]:animate-tf11-swap" aria-live="polite"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-5 flex-none fill-current"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11Z"/></svg><span class="text-tf11-ink"></span></p>
          <label class="flex cursor-pointer items-start gap-[.65rem] text-[.88rem] leading-[1.45] text-tf11-muted"><input type="checkbox" id="tf-11-fee" class="mt-[.12rem] size-[1.15rem] flex-none accent-tf11-accent"><span>Add <b class="tf-11__feeamt font-semibold text-tf11-ink">$1.75</b> to cover processing fees so 100% reaches the field.</span></label>
          <label class="flex cursor-pointer items-start gap-[.65rem] text-[.88rem] leading-[1.45] text-tf11-muted"><input type="checkbox" id="tf-11-tribute" class="mt-[.12rem] size-[1.15rem] flex-none accent-tf11-accent"><span>Give in honour or memory of someone</span></label>
          <fieldset class="hidden min-w-0 gap-[.6rem] rounded-2xl border border-tf11-line bg-tf11-soft p-4 group-has-[#tf-11-tribute:checked]/root:grid group-has-[#tf-11-tribute:checked]/root:animate-tf11-tribute">
            <legend class="sr-only">Tribute details</legend>
            <div class="grid grid-cols-2 gap-[.35rem]"><label class="relative"><input type="radio" name="tf-11-t" checked class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid min-h-10 place-items-center rounded-[.7rem] border border-tf11-line bg-tf11-card text-[.85rem] peer-checked:border-tf11-ink peer-checked:font-semibold peer-focus-visible:outline-2 peer-focus-visible:outline-tf11-accent">In honour of</span></label><label class="relative"><input type="radio" name="tf-11-t" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid min-h-10 place-items-center rounded-[.7rem] border border-tf11-line bg-tf11-card text-[.85rem] peer-checked:border-tf11-ink peer-checked:font-semibold peer-focus-visible:outline-2 peer-focus-visible:outline-tf11-accent">In memory of</span></label></div>
            <label for="tf-11-hon" class="sr-only">Honoree's name</label>
            <input id="tf-11-hon" type="text" placeholder="Honoree's full name" class="min-h-[2.9rem] rounded-[.7rem] border border-tf11-line bg-tf11-card px-[.9rem] py-[.6rem] text-tf11-ink focus-visible:border-tf11-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf11-accent)_20%,transparent)] focus-visible:outline-none">
          </fieldset>
          <button type="button" class="tf-11__donate group/d flex min-h-14 cursor-pointer items-center justify-center gap-[.6rem] rounded-full border-0 bg-tf11-accent text-[1.05rem] font-semibold text-tf11-on shadow-[0_14px_30px_-14px_var(--color-tf11-accent)] [transition:translate_.2s_var(--ease-tf11),filter_.2s] hover:-translate-y-0.5 hover:brightness-105 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf11-ink forced-colors:border forced-colors:border-[ButtonText]"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.2rem] fill-current [transition:scale_.3s_var(--ease-tf11)] group-hover/d:animate-tf11-beat"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"/></svg><span class="tf-11__label">Donate $50</span></button>
          <p class="tf-11__fine text-center text-[.78rem] text-tf11-muted" role="status">Tax-deductible · Registered 501(c)(3) · Cancel monthly gifts anytime</p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf11-bg: #f1f4ef;
  --color-tf11-card: #ffffff;
  --color-tf11-ink: #132017;
  --color-tf11-muted: #5c6b60;
  --color-tf11-line: #dfe6dc;
  --color-tf11-soft: #f6f9f4;
  --color-tf11-accent: #e8553d;
  --color-tf11-on: #fff;
  --color-tf11-leaf: #1f7a4d;
  --font-tf11-sans: "Lexend", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf11: cubic-bezier(0.16,1,0.3,1);
  --animate-tf11-fill: tf11-fill 1.6s 0.3s cubic-bezier(0.16,1,0.3,1) forwards;
  --animate-tf11-swap: tf11-swap 0.45s cubic-bezier(0.16,1,0.3,1);
  --animate-tf11-tribute: tf11-swap 0.4s cubic-bezier(0.16,1,0.3,1);
  --animate-tf11-beat: tf11-beat 0.8s ease-in-out infinite;

  @keyframes tf11-fill {
    to {
      --tf-11-p: 72.96%;
    }
  }

  @keyframes tf11-swap {
    from {
      opacity: 0.2;
      translate: 0 4px;
    }
  }

  @keyframes tf11-beat {
    0%,
        100% {
      scale: 1;
    }

    30% {
      scale: 1.25;
    }

    60% {
      scale: 0.95;
    }
  }
}
/* Registered so the campaign bar's width can animate — an at-rule, so it stays CSS. */

@property --tf-11-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-11[data-theme="dark"] {
  color-scheme: dark;
  --color-tf11-bg: #0c120e;
  --color-tf11-card: #131b16;
  --color-tf11-ink: #e8f0ea;
  --color-tf11-muted: #9aaba0;
  --color-tf11-line: #25322a;
  --color-tf11-soft: #18221c;
  --color-tf11-accent: #ff7a5f;
  --color-tf11-on: #2a0a04;
  --color-tf11-leaf: #4ade80;
}

@media (prefers-color-scheme: dark) {
  .tf-11:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf11-bg: #0c120e;
    --color-tf11-card: #131b16;
    --color-tf11-ink: #e8f0ea;
    --color-tf11-muted: #9aaba0;
    --color-tf11-line: #25322a;
    --color-tf11-soft: #18221c;
    --color-tf11-accent: #ff7a5f;
    --color-tf11-on: #2a0a04;
    --color-tf11-leaf: #4ade80;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-11').forEach((root) => {
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
  const root = document.querySelector('.tf-11');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const fmt = (n) => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: n % 1 ? 2 : 0 }).format(n);
  const ONCE = [25, 50, 100, 250], MONTHLY = [10, 20, 35, 75];
  const presets = [...root.querySelectorAll('[name="tf-11-a"]:not([value="other"])')];
  const other = $('[name="tf-11-a"][value="other"]'), custom = $('.tf-11__custom'), fee = $('#tf-11-fee');
  const impact = $('.tf-11__impact'), label = $('.tf-11__label');
  const amount = () => { const c = $('[name="tf-11-a"]:checked'); return c === other ? Math.max(0, parseFloat(custom.value.replace(/[^0-9.]/g, '')) || 0) : Number(c.value); };
  const update = (swap) => {
    const monthly = $('[name="tf-11-f"]:checked').value === 'monthly', a = amount();
    const f = a ? Math.round((a * 0.029 + 0.3) * 100) / 100 : 0;
    $('.tf-11__feeamt').textContent = fmt(f);
    const total = a + (fee.checked ? f : 0);
    label.textContent = a ? 'Donate ' + fmt(total) + (monthly ? ' monthly' : '') : 'Enter an amount';
    impact.querySelector('span').textContent = (a ? fmt(a) + (monthly ? ' a month ' : ' ') : 'Your gift ') + $('[name="tf-11-a"]:checked').dataset.impact + '.';
    if (swap) { impact.classList.remove('is-swap'); void impact.offsetWidth; impact.classList.add('is-swap'); }
  };
  root.querySelectorAll('[name="tf-11-f"]').forEach((r) => r.addEventListener('change', () => {
    const set = r.value === 'monthly' ? MONTHLY : ONCE;
    presets.forEach((p, i) => { p.value = set[i]; p.nextElementSibling.textContent = fmt(set[i]); });
    update(true);
  }));
  root.querySelectorAll('[name="tf-11-a"]').forEach((r) => r.addEventListener('change', () => { if (r === other) custom.focus(); update(true); }));
  custom.addEventListener('focus', () => { if (!other.checked) { other.checked = true; update(true); } });
  custom.addEventListener('input', () => { other.checked = true; update(false); });
  fee.addEventListener('change', () => update(false));
  $('.tf-11__donate').addEventListener('click', () => {
    if (!amount()) { custom.focus(); return; }
    $('.tf-11__fine').textContent = 'Thank you! Redirecting to secure payment for ' + label.textContent.replace('Donate ', '') + '…';
  });
  update(false);
})();
```
