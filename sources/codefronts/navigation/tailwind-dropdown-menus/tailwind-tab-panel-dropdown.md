---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-tab-panel-dropdown/"
title: "Tailwind Tab Panel Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "A dropdown containing a real tabbed interface."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tab Panel Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-tab-panel-dropdown/

A dropdown containing a real tabbed interface. Both states read off ARIA: the panel opens on the trigger's aria-expanded, and the tabs style themselves from aria-selected &mdash; so the tab strip's appearance and its announcement can never disagree.
## HTML
```html
<section class="tdd-21 w-full min-h-svh grid justify-center content-start bg-linear-[135deg,var(--color-tdd21-bg1),var(--color-tdd21-bg2)] font-tdd21-sans text-tdd21-ink px-5 py-8" aria-label="Tab panel dropdown demo">
  <nav class="relative z-10 flex w-[min(600px,100%)] items-center gap-1 rounded-2xl border border-tdd21-edge bg-white py-2.5 pr-2.5 pl-5 shadow-[0_4px_24px_oklch(0.7_0.16_163/0.12)]" aria-label="Primary">
    <span class="mr-3 text-[17px] font-bold text-tdd21-acc">&#9672; Mosaic</span>
    <div class="group relative">
      <button type="button" id="tdd21-btn" aria-expanded="false" aria-controls="tdd21-drop" class="min-h-11 cursor-pointer rounded-lg border-0 bg-transparent px-3.5 py-2 font-tdd21-sans text-sm font-semibold text-tdd21-ink transition-colors duration-150 hover:bg-tdd21-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd21-acc aria-expanded:bg-tdd21-tint aria-expanded:text-tdd21-acc">Explore &#9662;</button>
      <div id="tdd21-drop" class="pointer-events-none invisible absolute top-[calc(100%+10px)] left-0 w-65 -translate-y-2 overflow-hidden rounded-2xl border border-tdd21-edge bg-white opacity-0 shadow-[0_12px_40px_oklch(0.7_0.16_163/0.14)] transition-[opacity,translate,visibility] duration-280 ease-tdd21 group-data-open:pointer-events-auto group-data-open:visible group-data-open:translate-y-0 group-data-open:opacity-100 motion-reduce:transition-none">
        <div role="tablist" aria-label="Explore sections" class="flex gap-0.5 border-b border-tdd21-edge px-1.5 pt-1.5">
          <button type="button" role="tab" aria-selected="true" aria-controls="tdd21-p1" class="-mb-px flex-1 cursor-pointer rounded-t-lg border-0 border-b-2 border-b-transparent bg-transparent px-1.5 py-2 font-tdd21-sans text-[13px] font-semibold text-tdd21-mut transition-colors duration-150 hover:bg-tdd21-tint2 hover:text-tdd21-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdd21-acc aria-selected:border-b-tdd21-acc aria-selected:bg-tdd21-tint2 aria-selected:text-tdd21-acc">Popular</button>
          <button type="button" role="tab" aria-selected="false" aria-controls="tdd21-p2" class="-mb-px flex-1 cursor-pointer rounded-t-lg border-0 border-b-2 border-b-transparent bg-transparent px-1.5 py-2 font-tdd21-sans text-[13px] font-semibold text-tdd21-mut transition-colors duration-150 hover:bg-tdd21-tint2 hover:text-tdd21-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdd21-acc aria-selected:border-b-tdd21-acc aria-selected:bg-tdd21-tint2 aria-selected:text-tdd21-acc">New</button>
          <button type="button" role="tab" aria-selected="false" aria-controls="tdd21-p3" class="-mb-px flex-1 cursor-pointer rounded-t-lg border-0 border-b-2 border-b-transparent bg-transparent px-1.5 py-2 font-tdd21-sans text-[13px] font-semibold text-tdd21-mut transition-colors duration-150 hover:bg-tdd21-tint2 hover:text-tdd21-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdd21-acc aria-selected:border-b-tdd21-acc aria-selected:bg-tdd21-tint2 aria-selected:text-tdd21-acc">Topics</button>
        </div>
        <div class="min-h-35 p-1.5">
          <div role="tabpanel" id="tdd21-p1" class="flex flex-col gap-0.5 [&:not([hidden])]:animate-tdd21-fade">
            <a href="#most-visited" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#128293; Most Visited</a>
            <a href="#editor-picks" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#127775; Editor Picks</a>
            <a href="#trending" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#128202; Trending Now</a>
            <a href="#all-time" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#127942; All-Time Best</a>
          </div>
          <div role="tabpanel" id="tdd21-p2" hidden class="flex flex-col gap-0.5 [&:not([hidden])]:animate-tdd21-fade">
            <a href="#just-launched" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#128640; Just Launched</a>
            <a href="#this-week" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#128336; This Week</a>
            <a href="#this-month" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#128197; This Month</a>
            <a href="#coming-soon" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#127381; Coming Soon</a>
          </div>
          <div role="tabpanel" id="tdd21-p3" hidden class="flex flex-col gap-0.5 [&:not([hidden])]:animate-tdd21-fade">
            <a href="#design" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#127775; Design</a>
            <a href="#engineering" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#128187; Engineering</a>
            <a href="#product" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#128640; Product</a>
            <a href="#business" class="flex items-center gap-2 rounded-[9px] px-3 py-2.5 text-[13.5px] font-medium text-tdd21-ink no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-acc focus-visible:bg-tdd21-tint focus-visible:outline-none">&#128218; Business</a>
          </div>
        </div>
      </div>
    </div>
    <a href="#pricing" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tdd21-mut no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd21-acc">Pricing</a>
    <a href="#blog" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tdd21-mut no-underline transition-colors duration-150 hover:bg-tdd21-tint hover:text-tdd21-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd21-acc">Blog</a>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd21-bg1: #ecfdf5;
  --color-tdd21-bg1: oklch(0.98 0.02 165);
  --color-tdd21-bg2: #d1fae5;
  --color-tdd21-bg2: oklch(0.92 0.06 165);
  --color-tdd21-ink: #064e3b;
  --color-tdd21-ink: oklch(0.36 0.08 165);
  --color-tdd21-mut: #6b7280;
  --color-tdd21-mut: oklch(0.55 0.02 265);
  --color-tdd21-edge: #d1fae5;
  --color-tdd21-edge: oklch(0.92 0.06 165);
  --color-tdd21-tint: #ecfdf5;
  --color-tdd21-tint: oklch(0.98 0.02 165);
  --color-tdd21-tint2: #f0fdf4;
  --color-tdd21-tint2: oklch(0.98 0.02 150);
  --color-tdd21-acc: #10b981;
  --color-tdd21-acc: oklch(0.7 0.16 163);
  --font-tdd21-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --ease-tdd21: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tdd21-fade: tdd21-fade 0.22s ease;
}
/* Keyframes are the one thing utilities cannot express; the token above turns
   this into a real animate-tdd21-fade utility. */

@keyframes tdd21-fade {
  from {
    opacity: 0;
    transform: translateY(4px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.tdd-21 {
  width: 100%;
  min-height: 100svh;
}

.tdd-21 ::selection {
  background: var(--color-tdd21-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tdd-21').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var wrap = root.querySelector('.group'),
        btn = root.querySelector('#tdd21-btn'),
        drop = root.querySelector('#tdd21-drop');
    if (!wrap || !btn || !drop) return;
    var tabs = Array.from(drop.querySelectorAll('[role="tab"]'));

    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        var panel = root.querySelector('#' + t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
    }
    function setOpen(open) {
      wrap.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab); });
      tab.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        e.preventDefault();
        var n = e.key === 'ArrowRight' ? (i + 1) % tabs.length : (i - 1 + tabs.length) % tabs.length;
        tabs[n].focus(); select(tabs[n]);
      });
    });

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      setOpen(btn.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) setOpen(false); });
    root.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && wrap.hasAttribute('data-open')) { setOpen(false); btn.focus(); }
    });
  });
})();
```
