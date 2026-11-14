---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-scroll-spy-active-highlight-navbar/"
title: "Tailwind Scroll Spy Active Highlight Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "An IntersectionObserver scroll spy with a springy pill that hops between links and a progress hairline underneath."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll Spy Active Highlight Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-scroll-spy-active-highlight-navbar/

An IntersectionObserver scroll spy with a springy pill that hops between links and a progress hairline underneath. The port changes what the script writes: two custom properties (--x, --w) and one aria-current per link. The pill's motion, spring curve and the progress fill are all declared in utilities.
## HTML
```html
<div class="tnb-20 group w-full min-h-svh bg-tnb20-paper font-tnb20-sans text-tnb20-page" style="--tnb20-read:0" aria-label="Scroll spy active highlight navbar demo">
  <input type="checkbox" id="tnb20-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-100">
    <div class="flex h-16 items-center justify-between gap-6 border-b border-white/6 bg-tnb20-page px-5 md:px-8">
      <a href="#top" class="flex shrink-0 items-center gap-2.5 text-lg font-extrabold tracking-[-0.03em] text-tnb20-ink no-underline">
        <span class="grid size-7.5 place-items-center rounded-md bg-tnb20-acc text-sm text-tnb20-page" aria-hidden="true">&#10022;</span>Prism
      </a>
      <ul id="tnb20-links" class="relative hidden list-none items-center gap-0.5 md:flex" style="--tnb20-x:0px;--tnb20-w:0px">
        <li aria-hidden="true" class="pointer-events-none absolute top-1/2 left-0 z-0 h-9.5 w-[var(--tnb20-w)] -translate-y-1/2 translate-x-[var(--tnb20-x)] rounded-full border border-tnb20-acc/25 bg-tnb20-acc/12 transition-[translate,width] duration-350 ease-tnb20 motion-reduce:transition-none"></li>
        <li class="relative z-1"><a href="#sec-about" aria-current="page" class="flex h-9.5 items-center justify-center rounded-full px-3.5 text-sm font-medium whitespace-nowrap text-tnb20-mut no-underline transition-colors duration-200 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc">About</a></li>
        <li class="relative z-1"><a href="#sec-work" class="flex h-9.5 items-center justify-center rounded-full px-3.5 text-sm font-medium whitespace-nowrap text-tnb20-mut no-underline transition-colors duration-200 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc">Work</a></li>
        <li class="relative z-1"><a href="#sec-services" class="flex h-9.5 items-center justify-center rounded-full px-3.5 text-sm font-medium whitespace-nowrap text-tnb20-mut no-underline transition-colors duration-200 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc">Services</a></li>
        <li class="relative z-1"><a href="#sec-team" class="flex h-9.5 items-center justify-center rounded-full px-3.5 text-sm font-medium whitespace-nowrap text-tnb20-mut no-underline transition-colors duration-200 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc">Team</a></li>
        <li class="relative z-1"><a href="#sec-contact" class="flex h-9.5 items-center justify-center rounded-full px-3.5 text-sm font-medium whitespace-nowrap text-tnb20-mut no-underline transition-colors duration-200 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc">Contact</a></li>
      </ul>
      <div class="hidden shrink-0 items-center gap-2.5 md:flex">
        <a href="#login" class="flex h-9 items-center rounded-full border border-white/12 px-4 text-[13px] font-medium text-tnb20-mut no-underline transition-colors duration-200 hover:border-white/30 hover:text-tnb20-ink">Log in</a>
        <a href="#start" class="flex h-9 items-center rounded-full bg-tnb20-acc px-4.5 text-[13px] font-bold text-tnb20-page no-underline transition-transform duration-150 hover:scale-103 motion-reduce:transition-none motion-reduce:hover:scale-100">Get started &rarr;</a>
      </div>
      <label for="tnb20-menu" class="flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb20-ink transition-transform duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb20-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb20-ink transition-transform duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </div>
    <div class="h-0.5 bg-white/5">
      <div class="h-full origin-left scale-x-[var(--tnb20-read)] bg-tnb20-acc"></div>
    </div>
    <div id="tnb20-mobile" class="hidden bg-tnb20-page px-4 py-3 max-md:group-has-checked:grid">
      <a href="#sec-about" aria-current="page" class="flex min-h-11 items-center justify-between rounded-lg px-3 text-[15px] font-medium text-tnb20-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc aria-[current=page]:after:text-[8px] aria-[current=page]:after:content-['●']">About</a>
      <a href="#sec-work" class="flex min-h-11 items-center justify-between rounded-lg px-3 text-[15px] font-medium text-tnb20-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc aria-[current=page]:after:text-[8px] aria-[current=page]:after:content-['●']">Work</a>
      <a href="#sec-services" class="flex min-h-11 items-center justify-between rounded-lg px-3 text-[15px] font-medium text-tnb20-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc aria-[current=page]:after:text-[8px] aria-[current=page]:after:content-['●']">Services</a>
      <a href="#sec-team" class="flex min-h-11 items-center justify-between rounded-lg px-3 text-[15px] font-medium text-tnb20-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc aria-[current=page]:after:text-[8px] aria-[current=page]:after:content-['●']">Team</a>
      <a href="#sec-contact" class="flex min-h-11 items-center justify-between rounded-lg px-3 text-[15px] font-medium text-tnb20-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb20-ink aria-[current=page]:text-tnb20-acc aria-[current=page]:after:text-[8px] aria-[current=page]:after:content-['●']">Contact</a>
    </div>
  </header>
  <main class="mx-auto max-w-3xl px-5 pt-8 pb-24 md:px-8">
    <section id="sec-about" class="border-b border-tnb20-edge py-14">
      <p class="mb-3 text-xs font-bold tracking-[0.1em] text-tnb20-gold uppercase">About</p>
      <h1 class="mb-4 text-[clamp(2rem,5vw,2.6rem)] leading-[1.15] font-extrabold tracking-[-0.04em] text-tnb20-page">Scroll down to watch<br>the navbar update</h1>
      <p class="max-w-xl text-lg leading-relaxed text-tnb20-body">The pill hops on a spring because it translates rather than repositions, and the hairline under the bar fills from one custom property.</p>
    </section>
    <section id="sec-work" class="border-b border-tnb20-edge py-14">
      <p class="mb-3 text-xs font-bold tracking-[0.1em] text-tnb20-gold uppercase">Work</p>
      <h2 class="mb-4 text-3xl font-extrabold tracking-[-0.04em] text-tnb20-page">Selected projects</h2>
      <p class="max-w-xl leading-relaxed text-tnb20-body">The observer activates a section when it crosses the reading band — 25% down, 40% up — so a section becomes current only when you are actually reading it.</p>
      <div class="mt-6 grid gap-4 sm:grid-cols-2">
        <div class="grid h-35 place-items-center rounded-xl bg-tnb20-page text-lg font-bold text-tnb20-acc">Project A</div>
        <div class="grid h-35 place-items-center rounded-xl bg-tnb20-page2 text-lg font-bold text-tnb20-lilac">Project B</div>
      </div>
    </section>
    <section id="sec-services" class="border-b border-tnb20-edge py-14">
      <p class="mb-3 text-xs font-bold tracking-[0.1em] text-tnb20-gold uppercase">Services</p>
      <h2 class="mb-4 text-3xl font-extrabold tracking-[-0.04em] text-tnb20-page">What we do</h2>
      <p class="max-w-xl leading-relaxed text-tnb20-body">Width transitions between links of different lengths, which is why the pill takes its width from a property rather than a fixed value.</p>
      <div class="mt-6 grid gap-3 sm:grid-cols-3">
        <div class="rounded-xl border border-tnb20-acc/25 bg-tnb20-acc/10 p-5 text-sm font-semibold text-tnb20-page">Strategy</div>
        <div class="rounded-xl border border-tnb20-acc/25 bg-tnb20-acc/10 p-5 text-sm font-semibold text-tnb20-page">Design</div>
        <div class="rounded-xl border border-tnb20-acc/25 bg-tnb20-acc/10 p-5 text-sm font-semibold text-tnb20-page">Build</div>
      </div>
    </section>
    <section id="sec-team" class="border-b border-tnb20-edge py-14">
      <p class="mb-3 text-xs font-bold tracking-[0.1em] text-tnb20-gold uppercase">Team</p>
      <h2 class="mb-4 text-3xl font-extrabold tracking-[-0.04em] text-tnb20-page">Meet the crew</h2>
      <p class="max-w-xl leading-relaxed text-tnb20-body">Four people, one shared obsession: making software feel inevitable. Small by design — it keeps us close to the work.</p>
      <div class="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-4">
        <div class="rounded-xl border border-tnb20-edge bg-white p-4 text-center"><span class="mx-auto mb-2 grid size-10 place-items-center rounded-full bg-tnb20-page font-extrabold text-tnb20-acc">A</span><span class="block text-[13px] font-semibold text-tnb20-page">Alex</span><span class="block text-xs text-tnb20-mut2">Design</span></div>
        <div class="rounded-xl border border-tnb20-edge bg-white p-4 text-center"><span class="mx-auto mb-2 grid size-10 place-items-center rounded-full bg-tnb20-page font-extrabold text-tnb20-acc">J</span><span class="block text-[13px] font-semibold text-tnb20-page">Jamie</span><span class="block text-xs text-tnb20-mut2">Dev</span></div>
        <div class="rounded-xl border border-tnb20-edge bg-white p-4 text-center"><span class="mx-auto mb-2 grid size-10 place-items-center rounded-full bg-tnb20-page font-extrabold text-tnb20-acc">S</span><span class="block text-[13px] font-semibold text-tnb20-page">Sam</span><span class="block text-xs text-tnb20-mut2">Strategy</span></div>
        <div class="rounded-xl border border-tnb20-edge bg-white p-4 text-center"><span class="mx-auto mb-2 grid size-10 place-items-center rounded-full bg-tnb20-page font-extrabold text-tnb20-acc">R</span><span class="block text-[13px] font-semibold text-tnb20-page">Riley</span><span class="block text-xs text-tnb20-mut2">Growth</span></div>
      </div>
    </section>
    <section id="sec-contact" class="py-14">
      <p class="mb-3 text-xs font-bold tracking-[0.1em] text-tnb20-gold uppercase">Contact</p>
      <h2 class="mb-4 text-3xl font-extrabold tracking-[-0.04em] text-tnb20-page">Let's talk</h2>
      <p class="max-w-xl leading-relaxed text-tnb20-body">At the bottom the hairline is full. One observer callback drives the desktop pill and the mobile marker, because both read the same <code class="rounded bg-tnb20-page/8 px-1.5 py-0.5 text-[0.9em]">aria-current</code>.</p>
      <a href="#start" class="mt-6 inline-flex h-11.5 items-center rounded-full bg-tnb20-page px-7 text-[15px] font-bold text-tnb20-acc no-underline">Start a project &rarr;</a>
    </section>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb20-page: #0d0d0d;
  --color-tnb20-page: oklch(0.18 0 0);
  --color-tnb20-page2: #1a1a2e;
  --color-tnb20-page2: oklch(0.24 0.04 280);
  --color-tnb20-paper: #f8f6f2;
  --color-tnb20-paper: oklch(0.97 0.006 85);
  --color-tnb20-ink: #e8e4dc;
  --color-tnb20-ink: oklch(0.92 0.01 85);
  --color-tnb20-mut: #a19c92;
  --color-tnb20-mut: oklch(0.68 0.01 85);
  --color-tnb20-mut2: #7d7870;
  --color-tnb20-mut2: oklch(0.56 0.01 85);
  --color-tnb20-body: #5c5750;
  --color-tnb20-body: oklch(0.45 0.01 85);
  --color-tnb20-edge: #e5e0d8;
  --color-tnb20-edge: oklch(0.91 0.01 85);
  --color-tnb20-acc: #f0c14b;
  --color-tnb20-acc: oklch(0.83 0.14 85);
  --color-tnb20-gold: #96742c;
  --color-tnb20-gold: oklch(0.56 0.1 85);
  --color-tnb20-lilac: #a78bfa;
  --color-tnb20-lilac: oklch(0.74 0.15 295);
  --font-tnb20-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --ease-tnb20: cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tnb-20 {
  width: 100%;
  min-height: 100svh;
}

.tnb-20 ::selection {
  background: var(--color-tnb20-acc);
  color: #0d0d0d;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tnb-20').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var list = root.querySelector('#tnb20-links');
    var mobile = root.querySelector('#tnb20-mobile');
    if (!list) return;
    var links = Array.prototype.slice.call(list.querySelectorAll('a[href^="#"]'));
    var mLinks = mobile ? Array.prototype.slice.call(mobile.querySelectorAll('a[href^="#"]')) : [];

    function movePill(link) {
      var l = link.getBoundingClientRect(), c = list.getBoundingClientRect();
      list.style.setProperty('--tnb20-x', (l.left - c.left) + 'px');
      list.style.setProperty('--tnb20-w', l.width + 'px');
    }

    function setActive(id) {
      links.concat(mLinks).forEach(function (a) {
        var on = a.getAttribute('href') === '#' + id;
        if (on) { a.setAttribute('aria-current', 'page'); if (links.indexOf(a) > -1) movePill(a); }
        else a.removeAttribute('aria-current');
      });
    }

    var ticking = false;
    function readProgress() {
      ticking = false;
      var total = document.documentElement.scrollHeight - window.innerHeight;
      root.style.setProperty('--tnb20-read', total > 0 ? String(Math.min(1, window.scrollY / total)) : '0');
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(readProgress); }
    }, { passive: true });
    readProgress();

    var sections = links.map(function (a) { return root.querySelector(a.getAttribute('href')); }).filter(Boolean);
    var io = new IntersectionObserver(function (entries) {
      var hit = entries.filter(function (e) { return e.isIntersecting; })
        .sort(function (a, b) { return a.boundingClientRect.top - b.boundingClientRect.top; })[0];
      if (hit) setActive(hit.target.id);
    }, { rootMargin: '-25% 0px -60% 0px', threshold: 0 });
    sections.forEach(function (s) { io.observe(s); });

    function syncPill() {
      var cur = links.find(function (a) { return a.hasAttribute('aria-current'); }) || links[0];
      if (cur) movePill(cur);
    }
    // The bar may still be unstyled when this runs (CDN build, late fonts), so measure
    // again on every event that can change the links' geometry.
    requestAnimationFrame(function () { requestAnimationFrame(syncPill); });
    window.addEventListener('load', syncPill);
    setTimeout(syncPill, 400);
    setTimeout(syncPill, 1200);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(syncPill);
    if (window.ResizeObserver) new ResizeObserver(syncPill).observe(list);
    window.addEventListener('resize', syncPill, { passive: true });
  });
})();
```
