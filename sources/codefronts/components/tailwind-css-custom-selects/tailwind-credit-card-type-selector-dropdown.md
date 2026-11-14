---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-credit-card-type-selector-dropdown/"
title: "Tailwind Credit Card Type Selector Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "A saved-cards picker on a glass panel: backdrop-blur-[14px] is a utility, the spring open curve is a token, and the selected row's accent rail is…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Credit Card Type Selector Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-credit-card-type-selector-dropdown/

A saved-cards picker on a glass panel: backdrop-blur-[14px] is a utility, the spring open curve is a token, and the selected row's accent rail is aria-selected:border-l-tcs03-rail &mdash; the indicator and the semantics are the same attribute. The four brand marks stay in CSS, where attribute-keyed artwork belongs.
## HTML
```html
<section class="tcs-03 w-full min-h-svh grid place-items-center bg-tcs03-bg font-tcs03-sans text-tcs03-ink px-5 py-15" aria-label="Credit card type selector demo">
  <div class="w-80 max-w-full flex flex-col gap-2.5">
    <span id="tcs03-lbl" class="text-[13px] font-semibold text-tcs03-mut">Payment method</span>
    <div data-select class="group relative">
      <button id="tcs03-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs03-list" aria-labelledby="tcs03-lbl tcs03-trigger" class="w-full flex items-center gap-3.25 min-h-13 px-4 rounded-[15px] border border-tcs03-line bg-tcs03-surface text-[15px] text-tcs03-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs03-line2 focus-visible:outline-none focus-visible:border-tcs03-rail focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs03-rail)_22%,transparent)]">
        <span class="tcs03-mark" data-brand="visa" aria-hidden="true"></span>
        <span class="flex-1 flex items-center gap-2.5 text-left"><span data-name>Visa</span><span data-pan class="font-tcs03-mono text-[13px] tracking-[1px] text-tcs03-mut">•••• 4242</span></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs03-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs03-list" role="listbox" aria-labelledby="tcs03-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none p-1.75 rounded-[15px] border border-tcs03-line bg-tcs03-glass backdrop-blur-[14px] shadow-[0_28px_56px_-14px_oklch(0.1_0.02_290/0.7)] invisible opacity-0 -translate-y-2.5 scale-98 origin-top [transition:opacity_.24s,translate_.34s_var(--ease-tcs03),scale_.34s_var(--ease-tcs03),visibility_0s_.34s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:[transition:opacity_.24s,translate_.34s_var(--ease-tcs03),scale_.34s_var(--ease-tcs03),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs03-o0" role="option" aria-selected="true" data-v="Visa" data-brand="visa" data-pan="•••• 4242" class="group/opt flex items-center gap-3 min-h-13 px-3 rounded-[11px] cursor-pointer border-l-3 border-l-transparent transition-[background-color,border-color] duration-150 data-active:bg-tcs03-hover aria-selected:border-l-tcs03-rail aria-selected:bg-tcs03-sel"><span class="tcs03-mark" data-brand="visa" aria-hidden="true"></span><span class="flex-1 text-[14.5px]">Visa</span><span class="font-tcs03-mono text-[13px] tracking-[1px] text-tcs03-mut">•••• 4242</span></li>
        <li id="tcs03-o1" role="option" aria-selected="false" data-v="Mastercard" data-brand="mc" data-pan="•••• 8210" class="group/opt flex items-center gap-3 min-h-13 px-3 rounded-[11px] cursor-pointer border-l-3 border-l-transparent transition-[background-color,border-color] duration-150 data-active:bg-tcs03-hover aria-selected:border-l-tcs03-rail aria-selected:bg-tcs03-sel"><span class="tcs03-mark" data-brand="mc" aria-hidden="true"></span><span class="flex-1 text-[14.5px]">Mastercard</span><span class="font-tcs03-mono text-[13px] tracking-[1px] text-tcs03-mut">•••• 8210</span></li>
        <li id="tcs03-o2" role="option" aria-selected="false" data-v="American Express" data-brand="amex" data-pan="•••• 3005" class="group/opt flex items-center gap-3 min-h-13 px-3 rounded-[11px] cursor-pointer border-l-3 border-l-transparent transition-[background-color,border-color] duration-150 data-active:bg-tcs03-hover aria-selected:border-l-tcs03-rail aria-selected:bg-tcs03-sel"><span class="tcs03-mark" data-brand="amex" aria-hidden="true"></span><span class="flex-1 text-[14.5px]">American Express</span><span class="font-tcs03-mono text-[13px] tracking-[1px] text-tcs03-mut">•••• 3005</span></li>
        <li id="tcs03-o3" role="option" aria-selected="false" data-v="Discover" data-brand="disc" data-pan="•••• 6011" class="group/opt flex items-center gap-3 min-h-13 px-3 rounded-[11px] cursor-pointer border-l-3 border-l-transparent transition-[background-color,border-color] duration-150 data-active:bg-tcs03-hover aria-selected:border-l-tcs03-rail aria-selected:bg-tcs03-sel"><span class="tcs03-mark" data-brand="disc" aria-hidden="true"></span><span class="flex-1 text-[14.5px]">Discover</span><span class="font-tcs03-mono text-[13px] tracking-[1px] text-tcs03-mut">•••• 6011</span></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs03-mono text-[11px] text-tcs03-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs03-bg: #0f1226;
  --color-tcs03-bg: oklch(0.18 0.04 285);
  --color-tcs03-surface: #262042;
  --color-tcs03-surface: oklch(0.28 0.05 290);
  --color-tcs03-glass: #1e1936;
  --color-tcs03-glass: oklch(0.25 0.05 290 / 0.82);
  --color-tcs03-line: #3a3363;
  --color-tcs03-line: oklch(0.36 0.06 290);
  --color-tcs03-line2: #544c85;
  --color-tcs03-line2: oklch(0.46 0.08 290);
  --color-tcs03-hover: #3a336399;
  --color-tcs03-hover: oklch(0.36 0.06 290 / 0.55);
  --color-tcs03-sel: #3a336366;
  --color-tcs03-sel: oklch(0.36 0.06 290 / 0.4);
  --color-tcs03-ink: #ece9ff;
  --color-tcs03-ink: oklch(0.93 0.02 290);
  --color-tcs03-mut: #9a93c9;
  --color-tcs03-mut: oklch(0.68 0.06 290);
  --color-tcs03-rail: #fbbf24;
  --color-tcs03-rail: oklch(0.82 0.16 82);
  --font-tcs03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs03: cubic-bezier(0.34, 1.56, 0.64, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-03 {
  width: 100%;
  min-height: 100svh;
}
/* Brand marks stay CSS: four attribute-keyed paint recipes, each needing two
   pseudo-elements. They are artwork, not design-scale values. */

.tcs-03 .tcs03-mark {
  width: 40px;
  height: 26px;
  flex: none;
  position: relative;
  border-radius: 5px;
  background: #fff;
  box-shadow: inset 0 0 0 1px oklch(0 0 0 / 0.08);
}

.tcs-03 .tcs03-mark[data-brand="visa"] {
  background: linear-gradient(135deg, #1a1f71, #2434b0);
}

.tcs-03 .tcs03-mark[data-brand="visa"]::before {
  content: "VISA";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #fff;
  font: italic 800 11px/1 'Space Grotesk', sans-serif;
  letter-spacing: .5px;
}

.tcs-03 .tcs03-mark[data-brand="mc"] {
  background: #20143b;
}

.tcs-03 .tcs03-mark[data-brand="mc"]::before {
  content: "";
  position: absolute;
  left: 9px;
  top: 50%;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #eb001b;
  transform: translateY(-50%);
}

.tcs-03 .tcs03-mark[data-brand="mc"]::after {
  content: "";
  position: absolute;
  right: 9px;
  top: 50%;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #f79e1b;
  mix-blend-mode: screen;
  transform: translateY(-50%);
}

.tcs-03 .tcs03-mark[data-brand="amex"] {
  background: linear-gradient(135deg, #2e77bb, #1e5a9c);
}

.tcs-03 .tcs03-mark[data-brand="amex"]::before {
  content: "AMEX";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #fff;
  font: 800 9px/1 'Space Grotesk', sans-serif;
  letter-spacing: .5px;
}

.tcs-03 .tcs03-mark[data-brand="disc"] {
  background: #1a1730;
  overflow: hidden;
}

.tcs-03 .tcs03-mark[data-brand="disc"]::before {
  content: "";
  position: absolute;
  right: -3px;
  top: 50%;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: radial-gradient(circle, #ff6b00, #f79e1b);
  transform: translateY(-50%);
}

.tcs-03 .tcs03-mark[data-brand="disc"]::after {
  content: "DISC";
  position: absolute;
  left: 5px;
  top: 50%;
  color: #fff;
  font: 800 8px/1 'Space Grotesk', sans-serif;
  transform: translateY(-50%);
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-03 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-03').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-03').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset;
      root.querySelector('[data-trigger] .tcs03-mark').setAttribute('data-brand', d.brand);
      root.querySelector('[data-name]').textContent = d.v;
      root.querySelector('[data-pan]').textContent = d.pan;
    });
  });
})();
```
