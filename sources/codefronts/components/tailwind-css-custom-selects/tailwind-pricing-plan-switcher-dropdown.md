---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-pricing-plan-switcher-dropdown/"
title: "Tailwind Pricing Plan Switcher Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "A plan picker whose highlight glides instead of jumping: one absolutely-positioned bar reads --n from the list and moves with [translate:0_calc(var(--n)*60px)]."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Plan Switcher Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-pricing-plan-switcher-dropdown/

A plan picker whose highlight glides instead of jumping: one absolutely-positioned bar reads --n from the list and moves with [translate:0_calc(var(--n)*60px)]. The accent itself is a runtime variable the script rewrites per tier, which is exactly the case for a plain custom property rather than an @theme token.
## HTML
```html
<section class="tcs-04 w-full min-h-svh grid place-items-center bg-tcs04-bg font-tcs04-sans text-tcs04-ink px-5 py-15" aria-label="Pricing plan switcher demo">
  <div class="w-85 max-w-full flex flex-col gap-2.5">
    <span id="tcs04-lbl" class="text-[13px] font-semibold text-tcs04-mut">Choose your plan</span>
    <div data-select class="group relative">
      <button id="tcs04-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs04-list" aria-labelledby="tcs04-lbl tcs04-trigger" class="w-full flex items-center gap-3.25 min-h-13 px-4 rounded-2xl border border-tcs04-line bg-tcs04-surface text-tcs04-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs04-line2 focus-visible:outline-none focus-visible:border-[var(--tcs04-acc)] focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--tcs04-acc)_26%,transparent)]">
        <span data-orb class="w-6.5 h-6.5 rounded-full shadow-[0_0_14px_-2px_var(--tcs04-acc)] bg-[radial-gradient(circle_at_30%_30%,#c084fc,#a855f7)]" aria-hidden="true"></span>
        <span class="flex-1 flex flex-col text-left leading-[1.25]"><b data-name class="text-[15px]">Pro</b><small data-sub class="text-[11.5px] text-tcs04-mut">Most popular</small></span>
        <span class="text-[17px] font-extrabold tabular-nums"><span data-price>$29</span><i class="not-italic text-[11px] font-semibold text-tcs04-mut">/mo</i></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs04-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs04-list" role="listbox" aria-labelledby="tcs04-lbl" tabindex="-1" style="--n:1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none p-2 rounded-2xl border border-tcs04-line bg-tcs04-panel shadow-[0_28px_58px_-14px_oklch(0.1_0.03_300/0.72)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.22s,translate_.22s_var(--ease-tcs04),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.22s,translate_.22s_var(--ease-tcs04),visibility_0s_0s] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute left-2 right-2 top-2 h-15 rounded-xl pointer-events-none bg-linear-[90deg,color-mix(in_oklch,var(--tcs04-acc)_22%,transparent),transparent] shadow-[inset_0_0_0_1px_color-mix(in_oklch,var(--tcs04-acc)_40%,transparent)] [translate:0_calc(var(--n)*60px)] transition-[translate] duration-300 ease-tcs04 motion-reduce:transition-none"></span>
        <li id="tcs04-o0" role="option" aria-selected="false" data-v="Starter" data-t="starter" data-sub="For side projects" data-price="$9" class="group/opt relative z-1 flex items-center gap-3.25 h-15 px-3 rounded-xl cursor-pointer"><span class="w-6.5 h-6.5 rounded-full bg-[radial-gradient(circle_at_30%_30%,#38bdf8,#0ea5e9)]" aria-hidden="true"></span><span class="flex-1 flex flex-col leading-[1.25]"><b class="text-[15px]">Starter</b><small class="text-[11.5px] text-tcs04-mut">For side projects</small></span><span class="text-base font-extrabold tabular-nums">$9<i class="not-italic text-[11px] font-semibold text-tcs04-mut">/mo</i></span></li>
        <li id="tcs04-o1" role="option" aria-selected="true" data-v="Pro" data-t="pro" data-sub="Most popular" data-price="$29" class="group/opt relative z-1 flex items-center gap-3.25 h-15 px-3 rounded-xl cursor-pointer"><span class="w-6.5 h-6.5 rounded-full bg-[radial-gradient(circle_at_30%_30%,#c084fc,#a855f7)]" aria-hidden="true"></span><span class="flex-1 flex flex-col leading-[1.25]"><b class="text-[15px]">Pro</b><small class="text-[11.5px] text-tcs04-mut">Most popular</small></span><span class="text-base font-extrabold tabular-nums">$29<i class="not-italic text-[11px] font-semibold text-tcs04-mut">/mo</i></span></li>
        <li id="tcs04-o2" role="option" aria-selected="false" data-v="Enterprise" data-t="enterprise" data-sub="Advanced controls" data-price="$99" class="group/opt relative z-1 flex items-center gap-3.25 h-15 px-3 rounded-xl cursor-pointer"><span class="w-6.5 h-6.5 rounded-full bg-[radial-gradient(circle_at_30%_30%,#fbbf24,#f59e0b)]" aria-hidden="true"></span><span class="flex-1 flex flex-col leading-[1.25]"><b class="text-[15px]">Enterprise</b><small class="text-[11.5px] text-tcs04-mut">Advanced controls</small></span><span class="text-base font-extrabold tabular-nums">$99<i class="not-italic text-[11px] font-semibold text-tcs04-mut">/mo</i></span></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs04-mono text-[11px] text-tcs04-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs04-bg: #0d0b1f;
  --color-tcs04-bg: oklch(0.17 0.04 300);
  --color-tcs04-surface: #1a1636;
  --color-tcs04-surface: oklch(0.24 0.05 300);
  --color-tcs04-panel: #160f30;
  --color-tcs04-panel: oklch(0.21 0.05 300);
  --color-tcs04-line: #322b57;
  --color-tcs04-line: oklch(0.34 0.06 300);
  --color-tcs04-line2: #463d75;
  --color-tcs04-line2: oklch(0.42 0.08 300);
  --color-tcs04-ink: #efeaff;
  --color-tcs04-ink: oklch(0.94 0.02 300);
  --color-tcs04-mut: #9d94c4;
  --color-tcs04-mut: oklch(0.69 0.06 300);
  --font-tcs04-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs04-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs04: cubic-bezier(0.34, 1.4, 0.64, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-04 {
  width: 100%;
  min-height: 100svh;
}
/* Not an @theme entry on purpose: --tcs04-acc is per-tier runtime state the script
   writes, not a design token, so it must NOT mint utilities. */

.tcs-04 {
  --tcs04-acc: oklch(0.65 0.22 300);
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-04 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-04').querySelector('[data-live]');
    var i = opts.findIndex(function (o) { return o.getAttribute('aria-selected') === 'true'; });
    if (i < 0) i = 0;
    var typed = '', timer;
    function keepInView(el) {
      var top = el.offsetTop, bottom = top + el.offsetHeight;
      if (top < list.scrollTop) list.scrollTop = top;
      else if (bottom > list.scrollTop + list.clientHeight) list.scrollTop = bottom - list.clientHeight;
    }
    function mark(n) {
      i = n;
      opts.forEach(function (o, k) { o.toggleAttribute('data-active', k === n); });
      if (opts[n].id) trig.setAttribute('aria-activedescendant', opts[n].id);
      keepInView(opts[n]);
    }
    function set(open) {
      root.toggleAttribute('data-open', open);
      trig.setAttribute('aria-expanded', String(open));
      if (open) mark(i);
      else {
        opts.forEach(function (o) { o.removeAttribute('data-active'); });
        trig.removeAttribute('aria-activedescendant');
      }
    }
    function pick(n) {
      opts.forEach(function (o) { o.setAttribute('aria-selected', 'false'); });
      opts[n].setAttribute('aria-selected', 'true');
      i = n;
      root.dispatchEvent(new CustomEvent('tcs:pick', { bubbles: true, detail: { opt: opts[n], index: n } }));
      if (live) live.textContent = (opts[n].dataset.v || opts[n].textContent).trim() + ' selected';
      set(false);
      trig.focus();
    }
    trig.addEventListener('click', function () { set(!root.hasAttribute('data-open')); });
    opts.forEach(function (o, k) {
      o.addEventListener('click', function () { pick(k); });
      o.addEventListener('mousemove', function () { if (i !== k && root.hasAttribute('data-open')) mark(k); });
    });
    root.addEventListener('keydown', function (e) {
      var open = root.hasAttribute('data-open');
      if (!open) {
        if (e.key === 'ArrowDown' || e.key === 'ArrowUp' || e.key === 'Enter' || e.key === ' ') { e.preventDefault(); set(true); }
        return;
      }
      if (e.key === 'ArrowDown') { e.preventDefault(); mark((i + 1) % opts.length); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); mark((i - 1 + opts.length) % opts.length); }
      else if (e.key === 'Home') { e.preventDefault(); mark(0); }
      else if (e.key === 'End') { e.preventDefault(); mark(opts.length - 1); }
      else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(i); }
      else if (e.key === 'Escape' || e.key === 'Tab') { set(false); if (e.key === 'Escape') { e.preventDefault(); trig.focus(); } }
      else if (e.key.length === 1 && e.key.trim()) {
        clearTimeout(timer);
        typed += e.key.toLowerCase();
        timer = setTimeout(function () { typed = ''; }, 600);
        var hit = opts.findIndex(function (o) { return (o.dataset.v || o.textContent).trim().toLowerCase().indexOf(typed) === 0; });
        if (hit >= 0) mark(hit);
      }
    });
    document.addEventListener('pointerdown', function (e) { if (!root.contains(e.target)) set(false); });
  });
})();
(function () {
  var TIER = { starter: 'oklch(0.7 0.15 230)', pro: 'oklch(0.65 0.22 300)', enterprise: 'oklch(0.78 0.16 70)' };
  var ORB = {
    starter: 'radial-gradient(circle at 30% 30%,#38bdf8,#0ea5e9)',
    pro: 'radial-gradient(circle at 30% 30%,#c084fc,#a855f7)',
    enterprise: 'radial-gradient(circle at 30% 30%,#fbbf24,#f59e0b)'
  };
  document.querySelectorAll('.tcs-04').forEach(function (root) {
    var list = root.querySelector('[role="listbox"]');
    function place() {
      var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
      var n = opts.findIndex(function (o) { return o.getAttribute('aria-selected') === 'true'; });
      list.style.setProperty('--n', String(n < 0 ? 0 : n));
    }
    place();
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset;
      root.style.setProperty('--tcs04-acc', TIER[d.t]);
      root.querySelector('[data-orb]').style.background = ORB[d.t];
      root.querySelector('[data-name]').textContent = d.v;
      root.querySelector('[data-sub]').textContent = d.sub;
      root.querySelector('[data-price]').textContent = d.price;
      place();
    });
  });
})();
```
