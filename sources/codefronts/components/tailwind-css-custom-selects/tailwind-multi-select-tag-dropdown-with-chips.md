---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-multi-select-tag-dropdown-with-chips/"
title: "Tailwind Multi-Select Tag Dropdown With Chips"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "Multi-select with chips in the field, a live count, and a checkbox drawn entirely in utilities &mdash; the tick is an after: pseudo-element with…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Select Tag Dropdown With Chips
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-multi-select-tag-dropdown-with-chips/

Multi-select with chips in the field, a live count, and a checkbox drawn entirely in utilities &mdash; the tick is an after: pseudo-element with after:rotate-45, revealed by group-aria-selected/opt:. The panel stays open while you pick, and Backspace removes the last chip.
## HTML
```html
<section class="tcs-09 w-full min-h-svh grid place-items-center bg-tcs09-bg font-tcs09-sans text-tcs09-ink px-5 py-15" aria-label="Multi-select tag dropdown demo">
  <div class="w-80 max-w-full flex flex-col gap-2.5">
    <span id="tcs09-lbl" class="text-[13px] font-semibold text-tcs09-mut">Filter by skill</span>
    <div data-select class="group relative">
      <button id="tcs09-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs09-list" aria-labelledby="tcs09-lbl tcs09-trigger" class="w-full flex items-center gap-2 min-h-12.5 px-3 py-2 rounded-[14px] border border-tcs09-line bg-tcs09-surface text-left text-tcs09-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs09-line2 focus-visible:outline-none focus-visible:border-tcs09-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs09-acc)_22%,transparent)]">
        <span data-chips class="flex flex-1 flex-wrap items-center gap-1.5 min-w-0"><span data-ph class="text-[14.5px] text-tcs09-ph">Select skills…</span></span>
        <span data-count hidden class="px-2 py-0.5 rounded-full bg-[color-mix(in_oklch,var(--color-tcs09-acc)_18%,transparent)] font-tcs09-mono text-[11px] font-bold text-tcs09-acc2">0</span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 flex-none fill-none stroke-tcs09-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs09-list" role="listbox" aria-multiselectable="true" aria-labelledby="tcs09-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none max-h-62.5 overflow-y-auto p-1.5 rounded-[14px] border border-tcs09-line bg-tcs09-surface shadow-[0_26px_54px_-14px_oklch(0.1_0.02_215/0.7)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.2s,translate_.22s_var(--ease-tcs09),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs09),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs09-o0" role="option" aria-selected="false" data-v="React" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[14.5px] cursor-pointer transition-colors duration-150 data-active:bg-tcs09-hover"><span class="relative w-4.75 h-4.75 flex-none rounded-md border-2 border-tcs09-box transition-[background-color,border-color] duration-150 group-aria-selected/opt:bg-tcs09-acc group-aria-selected/opt:border-tcs09-acc after:content-[''] after:absolute after:left-[5px] after:top-[1px] after:w-1.5 after:h-2.75 after:border-tcs09-bg after:border-r-[2.5px] after:border-b-[2.5px] after:rotate-45 after:opacity-0 group-aria-selected/opt:after:opacity-100" aria-hidden="true"></span>React</li>
        <li id="tcs09-o1" role="option" aria-selected="false" data-v="TypeScript" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[14.5px] cursor-pointer transition-colors duration-150 data-active:bg-tcs09-hover"><span class="relative w-4.75 h-4.75 flex-none rounded-md border-2 border-tcs09-box transition-[background-color,border-color] duration-150 group-aria-selected/opt:bg-tcs09-acc group-aria-selected/opt:border-tcs09-acc after:content-[''] after:absolute after:left-[5px] after:top-[1px] after:w-1.5 after:h-2.75 after:border-tcs09-bg after:border-r-[2.5px] after:border-b-[2.5px] after:rotate-45 after:opacity-0 group-aria-selected/opt:after:opacity-100" aria-hidden="true"></span>TypeScript</li>
        <li id="tcs09-o2" role="option" aria-selected="false" data-v="CSS" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[14.5px] cursor-pointer transition-colors duration-150 data-active:bg-tcs09-hover"><span class="relative w-4.75 h-4.75 flex-none rounded-md border-2 border-tcs09-box transition-[background-color,border-color] duration-150 group-aria-selected/opt:bg-tcs09-acc group-aria-selected/opt:border-tcs09-acc after:content-[''] after:absolute after:left-[5px] after:top-[1px] after:w-1.5 after:h-2.75 after:border-tcs09-bg after:border-r-[2.5px] after:border-b-[2.5px] after:rotate-45 after:opacity-0 group-aria-selected/opt:after:opacity-100" aria-hidden="true"></span>CSS</li>
        <li id="tcs09-o3" role="option" aria-selected="false" data-v="Node.js" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[14.5px] cursor-pointer transition-colors duration-150 data-active:bg-tcs09-hover"><span class="relative w-4.75 h-4.75 flex-none rounded-md border-2 border-tcs09-box transition-[background-color,border-color] duration-150 group-aria-selected/opt:bg-tcs09-acc group-aria-selected/opt:border-tcs09-acc after:content-[''] after:absolute after:left-[5px] after:top-[1px] after:w-1.5 after:h-2.75 after:border-tcs09-bg after:border-r-[2.5px] after:border-b-[2.5px] after:rotate-45 after:opacity-0 group-aria-selected/opt:after:opacity-100" aria-hidden="true"></span>Node.js</li>
        <li id="tcs09-o4" role="option" aria-selected="false" data-v="GraphQL" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[14.5px] cursor-pointer transition-colors duration-150 data-active:bg-tcs09-hover"><span class="relative w-4.75 h-4.75 flex-none rounded-md border-2 border-tcs09-box transition-[background-color,border-color] duration-150 group-aria-selected/opt:bg-tcs09-acc group-aria-selected/opt:border-tcs09-acc after:content-[''] after:absolute after:left-[5px] after:top-[1px] after:w-1.5 after:h-2.75 after:border-tcs09-bg after:border-r-[2.5px] after:border-b-[2.5px] after:rotate-45 after:opacity-0 group-aria-selected/opt:after:opacity-100" aria-hidden="true"></span>GraphQL</li>
        <li id="tcs09-o5" role="option" aria-selected="false" data-v="Rust" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[14.5px] cursor-pointer transition-colors duration-150 data-active:bg-tcs09-hover"><span class="relative w-4.75 h-4.75 flex-none rounded-md border-2 border-tcs09-box transition-[background-color,border-color] duration-150 group-aria-selected/opt:bg-tcs09-acc group-aria-selected/opt:border-tcs09-acc after:content-[''] after:absolute after:left-[5px] after:top-[1px] after:w-1.5 after:h-2.75 after:border-tcs09-bg after:border-r-[2.5px] after:border-b-[2.5px] after:rotate-45 after:opacity-0 group-aria-selected/opt:after:opacity-100" aria-hidden="true"></span>Rust</li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs09-mono text-[11px] text-tcs09-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs09-bg: #03121a;
  --color-tcs09-bg: oklch(0.17 0.03 215);
  --color-tcs09-surface: #08222c;
  --color-tcs09-surface: oklch(0.23 0.04 215);
  --color-tcs09-hover: #0e3140;
  --color-tcs09-hover: oklch(0.29 0.05 215);
  --color-tcs09-line: #15414f;
  --color-tcs09-line: oklch(0.34 0.05 215);
  --color-tcs09-line2: #1d5666;
  --color-tcs09-line2: oklch(0.42 0.06 215);
  --color-tcs09-box: #2b5f6e;
  --color-tcs09-box: oklch(0.45 0.06 215);
  --color-tcs09-ink: #d6f5fb;
  --color-tcs09-ink: oklch(0.93 0.03 215);
  --color-tcs09-mut: #5b8b97;
  --color-tcs09-mut: oklch(0.62 0.05 215);
  --color-tcs09-ph: #4b7581;
  --color-tcs09-ph: oklch(0.55 0.04 215);
  --color-tcs09-acc: #22d3ee;
  --color-tcs09-acc: oklch(0.79 0.14 202);
  --color-tcs09-acc2: #a5f3fc;
  --color-tcs09-acc2: oklch(0.9 0.08 202);
  --font-tcs09-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs09-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs09: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-09 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  var CHIP = 'inline-flex items-center gap-1.5 pl-2.5 pr-1 py-1 rounded-lg border border-[color-mix(in_oklch,var(--color-tcs09-acc)_30%,transparent)] bg-[color-mix(in_oklch,var(--color-tcs09-acc)_16%,transparent)] text-[12.5px] font-semibold text-tcs09-acc2';
  var X = 'grid place-items-center w-4.5 h-4.5 rounded-[5px] border-0 bg-transparent text-tcs09-acc text-[13px] leading-none cursor-pointer hover:bg-[color-mix(in_oklch,var(--color-tcs09-acc)_25%,transparent)] focus-visible:outline-2 focus-visible:outline-tcs09-acc';
  document.querySelectorAll('.tcs-09 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var chips = root.querySelector('[data-chips]');
    var ph = root.querySelector('[data-ph]');
    var count = root.querySelector('[data-count]');
    var live = root.closest('.tcs-09').querySelector('[data-live]');
    var i = -1;
    function set(open) {
      root.toggleAttribute('data-open', open);
      trig.setAttribute('aria-expanded', String(open));
      if (!open) { opts.forEach(function (o) { o.removeAttribute('data-active'); }); i = -1; }
    }
    function mark(n) {
      i = n;
      opts.forEach(function (o, k) { o.toggleAttribute('data-active', k === n); });
      trig.setAttribute('aria-activedescendant', opts[n].id);
      var top = opts[n].offsetTop, bottom = top + opts[n].offsetHeight;
      if (top < list.scrollTop) list.scrollTop = top;
      else if (bottom > list.scrollTop + list.clientHeight) list.scrollTop = bottom - list.clientHeight;
    }
    function render() {
      var on = opts.filter(function (o) { return o.getAttribute('aria-selected') === 'true'; });
      chips.querySelectorAll('[data-chip]').forEach(function (c) { c.remove(); });
      ph.hidden = on.length > 0;
      count.hidden = on.length === 0;
      count.textContent = String(on.length);
      on.forEach(function (o) {
        var chip = document.createElement('span');
        chip.setAttribute('data-chip', '');
        chip.className = CHIP;
        chip.appendChild(document.createTextNode(o.dataset.v));
        var x = document.createElement('button');
        x.type = 'button';
        x.className = X;
        x.setAttribute('aria-label', 'Remove ' + o.dataset.v);
        x.textContent = '×';
        x.addEventListener('click', function (ev) { ev.stopPropagation(); toggle(o); });
        chip.appendChild(x);
        chips.appendChild(chip);
      });
      if (live) live.textContent = on.length ? on.length + ' selected: ' + on.map(function (o) { return o.dataset.v; }).join(', ') : 'No skills selected';
    }
    function toggle(o) {
      o.setAttribute('aria-selected', o.getAttribute('aria-selected') === 'true' ? 'false' : 'true');
      render();
    }
    trig.addEventListener('click', function (e) {
      if (e.target.closest('[data-chip]')) return;
      set(!root.hasAttribute('data-open'));
    });
    opts.forEach(function (o, k) {
      o.addEventListener('click', function (e) { e.stopPropagation(); toggle(o); mark(k); });
      o.addEventListener('mousemove', function () { if (i !== k) mark(k); });
    });
    root.addEventListener('keydown', function (e) {
      var open = root.hasAttribute('data-open');
      if (!open) {
        if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') { e.preventDefault(); set(true); mark(0); }
        return;
      }
      if (e.key === 'ArrowDown') { e.preventDefault(); mark((i + 1) % opts.length); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); mark((i - 1 + opts.length) % opts.length); }
      else if (e.key === 'Home') { e.preventDefault(); mark(0); }
      else if (e.key === 'End') { e.preventDefault(); mark(opts.length - 1); }
      else if ((e.key === 'Enter' || e.key === ' ') && i >= 0) { e.preventDefault(); toggle(opts[i]); }
      else if (e.key === 'Escape') { e.preventDefault(); set(false); trig.focus(); }
      else if (e.key === 'Backspace') {
        var on = opts.filter(function (o) { return o.getAttribute('aria-selected') === 'true'; });
        if (on.length) { e.preventDefault(); toggle(on[on.length - 1]); }
      }
    });
    document.addEventListener('pointerdown', function (e) { if (!root.contains(e.target)) set(false); });
    render();
  });
})();
```
