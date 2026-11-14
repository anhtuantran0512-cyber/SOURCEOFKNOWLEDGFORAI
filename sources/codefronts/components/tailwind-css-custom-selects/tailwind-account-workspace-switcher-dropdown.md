---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-account-workspace-switcher-dropdown/"
title: "Tailwind Account Workspace Switcher Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "A B2B workspace switcher: scrollable team list, plan badges, and a pinned Create workspace action that stays reachable at the bottom."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Account Workspace Switcher Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-account-workspace-switcher-dropdown/

A B2B workspace switcher: scrollable team list, plan badges, and a pinned Create workspace action that stays reachable at the bottom. Each team's logo colour is one number &mdash; style="--h:265" read by an arbitrary hsl() gradient utility, so a new team needs no new CSS at all.
## HTML
```html
<section class="tcs-07 w-full min-h-svh grid place-items-center bg-tcs07-bg font-tcs07-sans text-tcs07-ink px-5 py-15" aria-label="Workspace switcher dropdown demo">
  <div class="w-80 max-w-full flex flex-col gap-2.5">
    <span id="tcs07-lbl" class="text-[13px] font-semibold text-tcs07-mut">Workspace</span>
    <div data-select class="group relative">
      <button id="tcs07-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs07-list" aria-labelledby="tcs07-lbl tcs07-trigger" style="--h:265" class="w-full flex items-center gap-3 min-h-14 px-3.75 rounded-[15px] border border-tcs07-line bg-tcs07-surface text-tcs07-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs07-line2 focus-visible:outline-none focus-visible:border-tcs07-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs07-acc)_25%,transparent)]">
        <span data-logo class="grid place-items-center w-9 h-9 flex-none rounded-[11px] text-white text-[12.5px] font-extrabold tracking-[0.3px] bg-[linear-gradient(140deg,hsl(var(--h)_70%_58%),hsl(calc(var(--h)+28)_65%_44%))]" aria-hidden="true">AC</span>
        <span class="flex-1 flex flex-col text-left leading-[1.3]"><b data-name class="text-[15px]">Acme Corp</b><small data-sub class="text-[11.5px] text-tcs07-mut">12 members</small></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs07-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M8 9l4-4 4 4M8 15l4 4 4-4"/></svg>
      </button>
      <div class="absolute top-[calc(100%+9px)] inset-x-0 z-20 p-1.5 rounded-[15px] border border-tcs07-line bg-tcs07-panel shadow-[0_28px_56px_-14px_oklch(0.1_0.03_295/0.72)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.2s,translate_.24s_var(--ease-tcs07),visibility_0s_.24s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.2s,translate_.24s_var(--ease-tcs07),visibility_0s_0s] motion-reduce:transition-none">
        <div id="tcs07-list" role="listbox" aria-labelledby="tcs07-lbl" tabindex="-1" class="max-h-57.5 overflow-y-auto">
          <div id="tcs07-o0" role="option" aria-selected="true" data-v="Acme Corp" data-sub="12 members" data-h="265" data-ini="AC" style="--h:265" class="group/opt flex items-center gap-3 min-h-13 px-2.5 rounded-xl cursor-pointer transition-colors duration-150 data-active:bg-tcs07-hover"><span class="grid place-items-center w-9 h-9 flex-none rounded-[11px] text-white text-[12.5px] font-extrabold tracking-[0.3px] bg-[linear-gradient(140deg,hsl(var(--h)_70%_58%),hsl(calc(var(--h)+28)_65%_44%))] group-aria-selected/opt:shadow-[0_0_0_2px_var(--color-tcs07-panel),0_0_0_4px_var(--color-tcs07-acc)]" aria-hidden="true">AC</span><span class="flex-1 flex flex-col leading-[1.3]"><b class="text-[14.5px]">Acme Corp</b><small class="text-[11.5px] text-tcs07-mut">12 members</small></span><span class="px-2 py-1 rounded-md text-[10.5px] font-bold tracking-[0.4px] uppercase bg-[color-mix(in_oklch,var(--color-tcs07-acc)_20%,transparent)] text-tcs07-acc2">Pro</span></div>
          <div id="tcs07-o1" role="option" aria-selected="false" data-v="Nova Labs" data-sub="4 members" data-h="190" data-ini="NL" style="--h:190" class="group/opt flex items-center gap-3 min-h-13 px-2.5 rounded-xl cursor-pointer transition-colors duration-150 data-active:bg-tcs07-hover"><span class="grid place-items-center w-9 h-9 flex-none rounded-[11px] text-white text-[12.5px] font-extrabold tracking-[0.3px] bg-[linear-gradient(140deg,hsl(var(--h)_70%_58%),hsl(calc(var(--h)+28)_65%_44%))] group-aria-selected/opt:shadow-[0_0_0_2px_var(--color-tcs07-panel),0_0_0_4px_var(--color-tcs07-acc)]" aria-hidden="true">NL</span><span class="flex-1 flex flex-col leading-[1.3]"><b class="text-[14.5px]">Nova Labs</b><small class="text-[11.5px] text-tcs07-mut">4 members</small></span><span class="px-2 py-1 rounded-md text-[10.5px] font-bold tracking-[0.4px] uppercase bg-tcs07-chip text-tcs07-mut">Free</span></div>
          <div id="tcs07-o2" role="option" aria-selected="false" data-v="Orbit Studio" data-sub="27 members" data-h="150" data-ini="OS" style="--h:150" class="group/opt flex items-center gap-3 min-h-13 px-2.5 rounded-xl cursor-pointer transition-colors duration-150 data-active:bg-tcs07-hover"><span class="grid place-items-center w-9 h-9 flex-none rounded-[11px] text-white text-[12.5px] font-extrabold tracking-[0.3px] bg-[linear-gradient(140deg,hsl(var(--h)_70%_58%),hsl(calc(var(--h)+28)_65%_44%))] group-aria-selected/opt:shadow-[0_0_0_2px_var(--color-tcs07-panel),0_0_0_4px_var(--color-tcs07-acc)]" aria-hidden="true">OS</span><span class="flex-1 flex flex-col leading-[1.3]"><b class="text-[14.5px]">Orbit Studio</b><small class="text-[11.5px] text-tcs07-mut">27 members</small></span><span class="px-2 py-1 rounded-md text-[10.5px] font-bold tracking-[0.4px] uppercase bg-[color-mix(in_oklch,var(--color-tcs07-acc)_20%,transparent)] text-tcs07-acc2">Team</span></div>
          <div id="tcs07-o3" role="option" aria-selected="false" data-v="Pixel Forge" data-sub="8 members" data-h="25" data-ini="PF" style="--h:25" class="group/opt flex items-center gap-3 min-h-13 px-2.5 rounded-xl cursor-pointer transition-colors duration-150 data-active:bg-tcs07-hover"><span class="grid place-items-center w-9 h-9 flex-none rounded-[11px] text-white text-[12.5px] font-extrabold tracking-[0.3px] bg-[linear-gradient(140deg,hsl(var(--h)_70%_58%),hsl(calc(var(--h)+28)_65%_44%))] group-aria-selected/opt:shadow-[0_0_0_2px_var(--color-tcs07-panel),0_0_0_4px_var(--color-tcs07-acc)]" aria-hidden="true">PF</span><span class="flex-1 flex flex-col leading-[1.3]"><b class="text-[14.5px]">Pixel Forge</b><small class="text-[11.5px] text-tcs07-mut">8 members</small></span><span class="px-2 py-1 rounded-md text-[10.5px] font-bold tracking-[0.4px] uppercase bg-[color-mix(in_oklch,var(--color-tcs07-acc)_20%,transparent)] text-tcs07-acc2">Pro</span></div>
        </div>
        <button type="button" class="sticky bottom-0 flex w-full items-center gap-2.5 min-h-11 mt-1 px-3 rounded-xl border-0 bg-tcs07-panel text-[13.5px] font-semibold text-tcs07-acc2 cursor-pointer transition-colors duration-150 hover:bg-tcs07-hover focus-visible:outline-2 focus-visible:outline-tcs07-acc focus-visible:-outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-current [stroke-width:2.2] [stroke-linecap:round]"><path d="M12 5v14M5 12h14"/></svg>Create workspace</button>
      </div>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs07-mono text-[11px] text-tcs07-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs07-bg: #0c0a1a;
  --color-tcs07-bg: oklch(0.16 0.03 295);
  --color-tcs07-surface: #181433;
  --color-tcs07-surface: oklch(0.23 0.05 295);
  --color-tcs07-panel: #150f2e;
  --color-tcs07-panel: oklch(0.21 0.05 295);
  --color-tcs07-hover: #241c4a;
  --color-tcs07-hover: oklch(0.28 0.06 295);
  --color-tcs07-chip: #2a2352;
  --color-tcs07-chip: oklch(0.31 0.05 295);
  --color-tcs07-line: #2e2755;
  --color-tcs07-line: oklch(0.33 0.06 295);
  --color-tcs07-line2: #453a7d;
  --color-tcs07-line2: oklch(0.42 0.09 295);
  --color-tcs07-ink: #eae6ff;
  --color-tcs07-ink: oklch(0.93 0.02 295);
  --color-tcs07-mut: #9b91c7;
  --color-tcs07-mut: oklch(0.68 0.06 295);
  --color-tcs07-acc: #7c3aed;
  --color-tcs07-acc: oklch(0.54 0.24 296);
  --color-tcs07-acc2: #c4b5fd;
  --color-tcs07-acc2: oklch(0.82 0.1 295);
  --font-tcs07-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs07: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-07 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-07 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-07').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-07').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset, t = root.querySelector('[data-logo]');
      t.textContent = d.ini;
      root.querySelector('[data-trigger]').style.setProperty('--h', d.h);
      root.querySelector('[data-name]').textContent = d.v;
      root.querySelector('[data-sub]').textContent = d.sub;
    });
  });
})();
```
