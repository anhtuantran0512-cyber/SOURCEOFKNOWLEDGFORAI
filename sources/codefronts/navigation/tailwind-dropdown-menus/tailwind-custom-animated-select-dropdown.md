---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-custom-animated-select-dropdown/"
title: "Tailwind Custom Animated Select Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "A styled replacement for <select>, with the real element still in the DOM for form submission."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Custom Animated Select Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-custom-animated-select-dropdown/

A styled replacement for <select>, with the real element still in the DOM for form submission. Options stagger in on an overshoot curve, selection is aria-selected, open state is aria-expanded &mdash; three declarative states, and a script that only moves values between them.
## HTML
```html
<section class="tdd-22 w-full min-h-svh grid place-items-center bg-linear-[135deg,var(--color-tdd22-bg1),var(--color-tdd22-bg2)_60%,var(--color-tdd22-bg3)] font-tdd22-sans text-tdd22-ink px-5 py-10" aria-label="Custom animated select dropdown demo">
  <div class="flex w-[min(360px,100%)] flex-col gap-3 rounded-[20px] border border-tdd22-edge bg-white px-6 py-7 shadow-[0_8px_40px_oklch(0.75_0.16_70/0.15)]">
    <div>
      <p class="text-xl font-bold tracking-[-0.3px] text-tdd22-ink">Choose your plan</p>
      <p class="mt-1 text-[13px] text-tdd22-mut">Select the option that fits your needs</p>
    </div>
    <label for="tdd22-native" class="sr-only">Plan</label>
    <select id="tdd22-native" tabindex="-1" class="sr-only">
      <option value="">Select a plan&hellip;</option>
      <option value="free">Free &mdash; $0/month</option>
      <option value="pro">Pro &mdash; $12/month</option>
      <option value="team">Team &mdash; $39/month</option>
      <option value="enterprise">Enterprise &mdash; Custom</option>
    </select>
    <div class="group relative z-10">
      <button type="button" id="tdd22-btn" aria-haspopup="listbox" aria-expanded="false" aria-controls="tdd22-list" class="flex min-h-11 w-full cursor-pointer items-center justify-between gap-2 rounded-xl border-2 border-tdd22-edge bg-white px-4 py-3 text-left font-tdd22-sans text-[14.5px] font-medium text-tdd22-mut transition-[border-color,box-shadow,color] duration-200 hover:border-tdd22-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd22-acc aria-expanded:border-tdd22-acc aria-expanded:text-tdd22-ink aria-expanded:shadow-[0_0_0_4px_oklch(0.75_0.16_70/0.16)] data-chosen:font-semibold data-chosen:text-tdd22-ink">
        <span id="tdd22-val">Select a plan&hellip;</span>
        <span class="shrink-0 text-sm text-tdd22-mut transition-transform duration-280 ease-tdd22 group-has-aria-expanded:rotate-180" aria-hidden="true">&#9662;</span>
      </button>
      <ul id="tdd22-list" role="listbox" aria-label="Plan options" tabindex="-1" class="pointer-events-none absolute top-[calc(100%+8px)] right-0 left-0 origin-top scale-y-0 list-none rounded-2xl border border-tdd22-edge bg-white p-1.5 opacity-0 shadow-[0_12px_40px_oklch(0.75_0.16_70/0.18)] transition-[scale,opacity] duration-380 ease-tdd22 group-has-aria-expanded:pointer-events-auto group-has-aria-expanded:scale-y-100 group-has-aria-expanded:opacity-100 motion-reduce:duration-150">
        <li role="option" aria-selected="false" data-value="free" style="--i:0" class="flex min-h-11 cursor-pointer translate-y-1 items-center justify-between rounded-[9px] px-3.5 py-2.5 opacity-0 transition-[opacity,translate,background] duration-280 hover:bg-tdd22-tint data-active:bg-tdd22-tint data-active:outline-2 data-active:-outline-offset-2 data-active:outline-tdd22-acc aria-selected:bg-tdd22-sel group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(40ms+var(--i)*50ms)] motion-reduce:[transition-delay:0ms]"><span class="flex items-center gap-2 text-sm font-semibold text-tdd22-ink after:text-[13px] after:font-bold after:text-tdd22-acc aria-selected:after:content-['\2713']">&#127381; Free</span><span class="text-[12.5px] font-medium text-tdd22-mut">$0/month</span></li>
        <li role="option" aria-selected="false" data-value="pro" style="--i:1" class="flex min-h-11 cursor-pointer translate-y-1 items-center justify-between rounded-[9px] px-3.5 py-2.5 opacity-0 transition-[opacity,translate,background] duration-280 hover:bg-tdd22-tint data-active:bg-tdd22-tint data-active:outline-2 data-active:-outline-offset-2 data-active:outline-tdd22-acc aria-selected:bg-tdd22-sel group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(40ms+var(--i)*50ms)] motion-reduce:[transition-delay:0ms]"><span class="flex items-center gap-2 text-sm font-semibold text-tdd22-ink after:text-[13px] after:font-bold after:text-tdd22-acc aria-selected:after:content-['\2713']">&#128640; Pro</span><span class="text-[12.5px] font-medium text-tdd22-mut">$12/month</span></li>
        <li role="option" aria-selected="false" data-value="team" style="--i:2" class="flex min-h-11 cursor-pointer translate-y-1 items-center justify-between rounded-[9px] px-3.5 py-2.5 opacity-0 transition-[opacity,translate,background] duration-280 hover:bg-tdd22-tint data-active:bg-tdd22-tint data-active:outline-2 data-active:-outline-offset-2 data-active:outline-tdd22-acc aria-selected:bg-tdd22-sel group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(40ms+var(--i)*50ms)] motion-reduce:[transition-delay:0ms]"><span class="flex items-center gap-2 text-sm font-semibold text-tdd22-ink after:text-[13px] after:font-bold after:text-tdd22-acc aria-selected:after:content-['\2713']">&#128101; Team</span><span class="text-[12.5px] font-medium text-tdd22-mut">$39/month</span></li>
        <li role="option" aria-selected="false" data-value="enterprise" style="--i:3" class="mt-1 flex min-h-11 cursor-pointer translate-y-1 items-center justify-between rounded-[9px] border border-dashed border-tdd22-acc px-3.5 py-2.5 opacity-0 transition-[opacity,translate,background] duration-280 hover:bg-tdd22-sel data-active:bg-tdd22-tint data-active:outline-2 data-active:-outline-offset-2 data-active:outline-tdd22-acc aria-selected:bg-tdd22-sel group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(40ms+var(--i)*50ms)] motion-reduce:[transition-delay:0ms]"><span class="flex items-center gap-2 text-sm font-semibold text-tdd22-ink after:text-[13px] after:font-bold after:text-tdd22-acc aria-selected:after:content-['\2713']">&#127959; Enterprise</span><span class="text-[12.5px] font-medium text-tdd22-mut">Custom</span></li>
      </ul>
    </div>
    <button type="button" id="tdd22-submit" class="mt-1 min-h-11 w-full cursor-pointer rounded-xl border-0 bg-tdd22-acc px-3 py-3 font-tdd22-sans text-[15px] font-bold text-white transition-[background,translate] duration-150 hover:-translate-y-px hover:bg-tdd22-accdark focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd22-accdark motion-reduce:transition-none">Continue &#8594;</button>
    <p id="tdd22-status" role="status" class="min-h-4.5 text-center text-[12.5px] italic text-tdd22-mut">No plan selected</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd22-bg1: #fffbeb;
  --color-tdd22-bg1: oklch(0.98 0.02 95);
  --color-tdd22-bg2: #fef3c7;
  --color-tdd22-bg2: oklch(0.95 0.06 92);
  --color-tdd22-bg3: #fde68a;
  --color-tdd22-bg3: oklch(0.91 0.1 90);
  --color-tdd22-ink: #1c1917;
  --color-tdd22-ink: oklch(0.22 0.01 60);
  --color-tdd22-mut: #78716c;
  --color-tdd22-mut: oklch(0.56 0.01 60);
  --color-tdd22-edge: #e7e5e4;
  --color-tdd22-edge: oklch(0.91 0.005 60);
  --color-tdd22-tint: #fffbeb;
  --color-tdd22-tint: oklch(0.98 0.02 95);
  --color-tdd22-sel: #fef3c7;
  --color-tdd22-sel: oklch(0.95 0.06 92);
  --color-tdd22-acc: #f59e0b;
  --color-tdd22-acc: oklch(0.75 0.16 70);
  --color-tdd22-accdark: #d97706;
  --color-tdd22-accdark: oklch(0.65 0.15 60);
  --font-tdd22-sans: 'Inter', system-ui, sans-serif;
  --ease-tdd22: cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tdd-22 {
  width: 100%;
  min-height: 100svh;
}

.tdd-22 ::selection {
  background: var(--color-tdd22-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tdd-22').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var btn = root.querySelector('#tdd22-btn'),
        list = root.querySelector('#tdd22-list'),
        val = root.querySelector('#tdd22-val'),
        native = root.querySelector('#tdd22-native'),
        submit = root.querySelector('#tdd22-submit'),
        status = root.querySelector('#tdd22-status');
    if (!btn || !list || !native) return;
    var opts = Array.from(list.querySelectorAll('[role="option"]'));
    var active = -1;
    var isOpen = function () { return btn.getAttribute('aria-expanded') === 'true'; };

    function highlight(i) {
      opts.forEach(function (o) { o.removeAttribute('data-active'); });
      if (i < 0 || i >= opts.length) return;
      opts[i].setAttribute('data-active', '');
      active = i;
    }
    function setOpen(open) {
      btn.setAttribute('aria-expanded', String(open));
      if (open) {
        var sel = opts.findIndex(function (o) { return o.getAttribute('aria-selected') === 'true'; });
        highlight(sel > -1 ? sel : 0);
      } else { highlight(-1); active = -1; }
    }
    function choose(opt) {
      opts.forEach(function (o) { o.setAttribute('aria-selected', String(o === opt)); });
      var name = opt.children[0].textContent.trim(), price = opt.children[1].textContent.trim();
      val.textContent = name + ' — ' + price;
      btn.toggleAttribute('data-chosen', true);
      native.value = opt.dataset.value;
      native.dispatchEvent(new Event('change', { bubbles: true }));
      status.textContent = 'Selected: ' + name + ' (' + price + ')';
      setOpen(false);
      btn.focus();
    }

    btn.addEventListener('click', function (e) { e.stopPropagation(); setOpen(!isOpen()); });
    btn.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        if (!isOpen()) setOpen(true); else list.focus();
      } else if (e.key === 'Escape' && isOpen()) setOpen(false);
    });
    opts.forEach(function (opt, i) {
      opt.addEventListener('click', function () { choose(opt); });
      opt.addEventListener('mousemove', function () { highlight(i); });
    });
    list.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); highlight((active + 1) % opts.length); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); highlight((active - 1 + opts.length) % opts.length); }
      else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); if (active > -1) choose(opts[active]); }
      else if (e.key === 'Escape' || e.key === 'Tab') { setOpen(false); btn.focus(); }
    });
    document.addEventListener('click', function (e) {
      if (!btn.contains(e.target) && !list.contains(e.target)) setOpen(false);
    });
    submit && submit.addEventListener('click', function () {
      if (!native.value) {
        status.textContent = '⚠ Please select a plan first.';
        btn.style.borderColor = 'oklch(0.63 0.22 25)';
        setTimeout(function () { btn.style.borderColor = ''; }, 1500);
      } else {
        status.textContent = '✓ Proceeding with ' + val.textContent;
      }
    });
  });
})();
```
