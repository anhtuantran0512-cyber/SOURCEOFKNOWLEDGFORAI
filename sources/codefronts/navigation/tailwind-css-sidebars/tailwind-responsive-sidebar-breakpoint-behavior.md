---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-responsive-sidebar-breakpoint-behavior/"
title: "Tailwind Responsive Sidebar Breakpoint Behavior"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "The same sidebar is a persistent rail on a laptop and a modal drawer on a phone &mdash; which means its ROLE changes with the viewport, not just its width."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Sidebar Breakpoint Behavior
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-responsive-sidebar-breakpoint-behavior/

The same sidebar is a persistent rail on a laptop and a modal drawer on a phone &mdash; which means its ROLE changes with the viewport, not just its width. The port's discipline is the interesting part: the breakpoint is declared once, in matchMedia, and the class list keys off the resulting data-mode attribute rather than repeating the number as a Tailwind variant.
## HTML
```html
<section class="tsb-12 block relative w-full min-h-svh bg-tsb12-bg text-tsb12-ink font-tsb12-sans leading-[1.55]" aria-label="Orbit banking">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-12-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-12-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[0.9rem] border border-tsb12-line bg-tsb12-surf text-tsb12-ink cursor-pointer shadow-[0_0.3rem_0.8rem_oklch(20%_0.04_292/0.14)] peer-focus-visible:outline-2 peer-focus-visible:outline-tsb12-acc peer-focus-visible:outline-offset-2" for="tsb-12-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="group relative overflow-hidden flex min-w-0 min-h-svh bg-tsb12-surf" id="tsb-12-app" data-mode="persistent">
    <div class="flex-1 flex flex-col min-w-0 transition-opacity duration-200 inert:opacity-50 motion-reduce:transition-none" id="tsb-12-content">
      <div class="flex items-center gap-2 py-2.5 pl-3.5 pr-[4.2rem] border-b border-tsb12-line">
        <button class="grid place-items-center w-11 h-11 rounded-[0.8rem] border-0 bg-tsb12-surf2 text-tsb12-ink cursor-pointer [&>svg]:w-4.5 [&>svg]:h-4.5 group-data-[mode=persistent]:hidden focus-visible:outline-2 focus-visible:outline-tsb12-acc focus-visible:outline-offset-2" type="button" id="tsb-12-open" aria-expanded="false" aria-controls="tsb-12-rail">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Open navigation</span>
        </button>
        <p class="mr-auto m-0 font-tsb12-display text-[1.15rem] font-bold tracking-[-0.02em] text-tsb12-acc">Orbit</p>
        <a class="inline-flex items-center min-h-11 px-2.5 text-[0.86rem] text-tsb12-mut no-underline hover:text-tsb12-ink focus-visible:outline-2 focus-visible:outline-tsb12-acc focus-visible:outline-offset-2" href="#tsb-12-content">Help</a>
      </div>
      <div class="grid grid-cols-2 gap-2.5 px-4 pt-4 pb-2">
        <div class="min-w-0 px-4 py-3.5 rounded-2xl bg-tsb12-surf2"><p class="m-0 mb-1 text-[0.72rem] tracking-[0.06em] uppercase text-tsb12-mut">Current account</p><p class="m-0 font-tsb12-display text-[1.25rem] font-bold tabular-nums">&euro;4,182.60</p></div>
        <div class="min-w-0 px-4 py-3.5 rounded-2xl bg-tsb12-surf2"><p class="m-0 mb-1 text-[0.72rem] tracking-[0.06em] uppercase text-tsb12-mut">Savings</p><p class="m-0 font-tsb12-display text-[1.25rem] font-bold tabular-nums">&euro;16,400.00</p></div>
      </div>
      <ul class="list-none m-0 grid gap-1.5 px-4 pt-2 pb-6 [&>li]:flex [&>li]:gap-2.5 [&>li]:min-w-0 [&>li]:px-3 [&>li]:py-2.5 [&>li]:rounded-[0.7rem] [&>li]:bg-tsb12-surf2 [&>li]:text-[0.88rem] [&>li>span]:min-w-0 [&>li>span]:overflow-hidden [&>li>span]:text-ellipsis [&>li>span]:whitespace-nowrap [&>li>em]:ml-auto [&>li>em]:not-italic [&>li>em]:tabular-nums [&>li>em]:text-tsb12-mut">
        <li><span>Meridian Ltd</span><em>&minus;&euro;42.00</em></li>
        <li><span>Fern Studio</span><em>+&euro;1,250.00</em></li>
        <li><span>Basalt Hosting</span><em>&minus;&euro;18.00</em></li>
        <li><span>Kestrel Rail</span><em>&minus;&euro;64.40</em></li>
        <li><span>Slack Water Co</span><em>+&euro;320.00</em></li>
      </ul>
    </div>

    <div class="absolute inset-0 z-20 bg-[oklch(18%_0.04_292/0.45)] [&[hidden]]:hidden" data-tsb-12-scrim hidden></div>

    <aside class="flex-none flex flex-col min-w-0 w-56 order-[-1] bg-tsb12-surf2 border-r border-tsb12-line group-data-[mode=modal]:absolute group-data-[mode=modal]:inset-y-0 group-data-[mode=modal]:left-0 group-data-[mode=modal]:z-30 group-data-[mode=modal]:w-[min(15rem,82%)] group-data-[mode=modal]:-translate-x-full group-data-[mode=modal]:shadow-[0_0_2rem_oklch(18%_0.04_292/0.4)] group-data-[mode=modal]:transition-transform group-data-[mode=modal]:duration-[220ms] group-data-[mode=modal]:ease-[cubic-bezier(0.22,1,0.36,1)] group-data-[mode=modal]:group-data-open:translate-x-0 motion-reduce:group-data-[mode=modal]:duration-[1ms] [&[hidden]]:hidden" id="tsb-12-rail" aria-labelledby="tsb-12-rail-h">
      <div class="flex items-center gap-2 p-2.5">
        <p class="mr-auto m-0 text-[0.74rem] tracking-[0.1em] uppercase text-tsb12-mut" id="tsb-12-rail-h">Accounts</p>
        <button class="grid place-items-center w-11 h-11 rounded-[0.8rem] border-0 bg-tsb12-surf text-tsb12-ink cursor-pointer [&>svg]:w-4 [&>svg]:h-4 group-data-[mode=persistent]:hidden focus-visible:outline-2 focus-visible:outline-tsb12-acc focus-visible:outline-offset-2" type="button" data-tsb-12-close>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Close navigation</span>
        </button>
      </div>
      <nav class="flex-1 min-h-0 overflow-y-auto px-2 pt-1 pb-2.5 [overscroll-behavior:contain]" aria-label="Orbit accounts">
        <ul class="list-none m-0 p-0 grid gap-0.5">
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.9rem] text-tsb12-ink no-underline hover:bg-tsb12-surf focus-visible:outline-2 focus-visible:outline-tsb12-acc focus-visible:outline-offset-2 aria-[current=page]:bg-tsb12-acc aria-[current=page]:text-tsb12-onacc aria-[current=page]:font-semibold" href="#tsb-12-content" aria-current="page">Overview</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.9rem] text-tsb12-ink no-underline hover:bg-tsb12-surf focus-visible:outline-2 focus-visible:outline-tsb12-acc focus-visible:outline-offset-2" href="#tsb-12-content">Payments</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.9rem] text-tsb12-ink no-underline hover:bg-tsb12-surf focus-visible:outline-2 focus-visible:outline-tsb12-acc focus-visible:outline-offset-2" href="#tsb-12-content">Standing orders</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.9rem] text-tsb12-ink no-underline hover:bg-tsb12-surf focus-visible:outline-2 focus-visible:outline-tsb12-acc focus-visible:outline-offset-2" href="#tsb-12-content">Statements</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.7rem] text-[0.9rem] text-tsb12-ink no-underline hover:bg-tsb12-surf focus-visible:outline-2 focus-visible:outline-tsb12-acc focus-visible:outline-offset-2" href="#tsb-12-content">Team settings</a></li>
        </ul>
      </nav>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb12-bg: #f4f1fb;
  --color-tsb12-bg: oklch(96% 0.014 292);
  --color-tsb12-surf: #ffffff;
  --color-tsb12-surf: oklch(100% 0 0);
  --color-tsb12-surf2: #ece7f9;
  --color-tsb12-surf2: oklch(93.5% 0.022 292);
  --color-tsb12-line: #d9d1f0;
  --color-tsb12-line: oklch(87% 0.035 292);
  --color-tsb12-ink: #1d1830;
  --color-tsb12-ink: oklch(22% 0.04 292);
  --color-tsb12-mut: #625b80;
  --color-tsb12-mut: oklch(48% 0.05 292);
  --color-tsb12-acc: #6b3fd4;
  --color-tsb12-acc: oklch(52% 0.2 292);
  --color-tsb12-accsoft: #e6dcfb;
  --color-tsb12-accsoft: oklch(92% 0.04 292);
  --color-tsb12-onacc: #ffffff;
  --color-tsb12-onacc: oklch(100% 0 0);
  --font-tsb12-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb12-display: 'Plus Jakarta Sans', 'SF Pro Display', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract. The mode breakpoint is deliberately NOT here — it
   lives once, in the script's matchMedia, and the markup keys off data-mode. */

.tsb-12 {
  width: 100%;
  min-height: 100svh;
}

.tsb-12 *,
.tsb-12 *::before,
.tsb-12 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-12:has(.tsb-12-theme-input:checked) {
  --color-tsb12-bg: #0d0a17;
  --color-tsb12-surf: #151020;
  --color-tsb12-surf2: #1d1730;
  --color-tsb12-line: #2b2342;
  --color-tsb12-ink: #ece8f8;
  --color-tsb12-mut: #a099c0;
  --color-tsb12-acc: #b394ff;
  --color-tsb12-acc: oklch(80% 0.14 292);
  --color-tsb12-accsoft: #241c3c;
  --color-tsb12-onacc: #0d0a17;
}

@media (prefers-color-scheme: dark) {
  .tsb-12 {
    --color-tsb12-bg: #0d0a17;
    --color-tsb12-surf: #151020;
    --color-tsb12-surf2: #1d1730;
    --color-tsb12-line: #2b2342;
    --color-tsb12-ink: #ece8f8;
    --color-tsb12-mut: #a099c0;
    --color-tsb12-acc: #b394ff;
    --color-tsb12-acc: oklch(80% 0.14 292);
    --color-tsb12-accsoft: #241c3c;
    --color-tsb12-onacc: #0d0a17;
  }

  .tsb-12:has(.tsb-12-theme-input:checked) {
    --color-tsb12-bg: #f4f1fb;
    --color-tsb12-surf: #ffffff;
    --color-tsb12-surf2: #ece7f9;
    --color-tsb12-line: #d9d1f0;
    --color-tsb12-ink: #1d1830;
    --color-tsb12-mut: #625b80;
    --color-tsb12-acc: #6b3fd4;
    --color-tsb12-acc: oklch(52% 0.2 292);
    --color-tsb12-accsoft: #e6dcfb;
    --color-tsb12-onacc: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-12:has(.tsb-12-theme-input:checked) {
    --color-tsb12-bg: #0d0a17;
    --color-tsb12-surf: #151020;
    --color-tsb12-surf2: #1d1730;
    --color-tsb12-line: #2b2342;
    --color-tsb12-ink: #ece8f8;
    --color-tsb12-mut: #a099c0;
    --color-tsb12-acc: #b394ff;
    --color-tsb12-acc: oklch(80% 0.14 292);
    --color-tsb12-accsoft: #241c3c;
    --color-tsb12-onacc: #0d0a17;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tsb-12').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var app = root.querySelector('#tsb-12-app'),
        rail = root.querySelector('#tsb-12-rail'),
        content = root.querySelector('#tsb-12-content'),
        scrim = root.querySelector('[data-tsb-12-scrim]'),
        trigger = root.querySelector('#tsb-12-open'),
        supportsInert = 'inert' in HTMLElement.prototype,
        // One source of truth for the mode: the markup keys off data-mode, never its own
        // copy of the breakpoint.
        mq = window.matchMedia('(min-width: 44rem)'),
        open = false, returnTo = null;
    function modal() { return !mq.matches; }
    function onKey(e) { if (e.key === 'Escape' && open) setOpen(false); }
    function paint() {
      app.setAttribute('data-mode', modal() ? 'modal' : 'persistent');
      app.toggleAttribute('data-open', open);
      rail.hidden = modal() && !open;
      scrim.hidden = !(modal() && open);
      rail.setAttribute('role', modal() ? 'dialog' : 'complementary');
      if (modal()) rail.setAttribute('aria-modal', 'true'); else rail.removeAttribute('aria-modal');
      trigger.setAttribute('aria-expanded', String(modal() && open));
      var block = modal() && open;
      if (supportsInert) content.inert = block;
      else content.setAttribute('aria-hidden', String(block));
    }
    function setOpen(next) {
      open = next;
      if (next) { returnTo = document.activeElement; document.addEventListener('keydown', onKey); }
      else document.removeEventListener('keydown', onKey);
      paint();
      if (next) requestAnimationFrame(function () { rail.querySelector('[data-tsb-12-close]').focus(); });
      else if (returnTo) { returnTo.focus({ preventScroll: true }); returnTo = null; }
    }
    function onModeChange() { if (open && !modal()) setOpen(false); else paint(); }
    mq.addEventListener('change', onModeChange);
    trigger.addEventListener('click', function () { setOpen(true); });
    scrim.addEventListener('click', function () { setOpen(false); });
    root.querySelectorAll('[data-tsb-12-close]').forEach(function (b) { b.addEventListener('click', function () { setOpen(false); }); });
    paint();
    // matchMedia can read stale at parse time, so settle the mode after first layout too.
    requestAnimationFrame(paint);
    root.__tsbCleanup = function () {
      document.removeEventListener('keydown', onKey);
      mq.removeEventListener('change', onModeChange);
    };
  });
})();
```
