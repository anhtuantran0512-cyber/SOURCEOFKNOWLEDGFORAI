---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-command-palette-header-cmd-k/"
title: "Tailwind CSS Command Palette Header with ⌘K Shortcut"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The developer-tool header of 2026: a muted search pill in the centre of the bar with a <kbd>⌘K</kbd> badge, opening a full command palette that scales and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Command Palette Header with ⌘K Shortcut
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-command-palette-header-cmd-k/

The developer-tool header of 2026: a muted search pill in the centre of the bar with a <kbd>⌘K</kbd> badge, opening a full command palette that scales and fades in. Open/close is pure CSS state read with group-has-[#thd-01-open:checked]/thd01:; the small script adds the global shortcut, live filtering and arrow-key navigation the CSS original never had.
## HTML
```html
<div class="thd-01 group/thd01 relative w-full min-h-svh bg-thd01-s0 bg-[radial-gradient(80rem_36rem_at_80%_-12%,var(--color-thd01-glow),transparent_62%)] font-thd01-sans leading-relaxed text-thd01-ink antialiased">
  <a href="#thd-01-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd01-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-thd01-on">Skip to content</a>

  <header class="thd01-tighten sticky top-0 z-40 flex items-center gap-3 border-b border-transparent bg-thd01-s0/80 px-[clamp(.75rem,3vw,1.75rem)] py-2.5 backdrop-blur-xl backdrop-saturate-150">
    <a href="#thd-01-main" aria-label="Halcyon home" class="flex min-w-0 items-center gap-2 text-[1.02rem] font-bold tracking-tight">
      <svg viewBox="0 0 28 28" fill="none" aria-hidden="true" class="size-6 flex-none text-thd01-acc drop-shadow-[0_0_10px_var(--color-thd01-glow)]"><path d="M14 2.6 24.4 8.6v11.8L14 26.4 3.6 20.4V8.6L14 2.6Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9.2 17.6 14 9.4l4.8 8.2H9.2Z" fill="currentColor"/></svg>
      <span class="truncate">Halcyon</span>
    </a>
    <nav aria-label="Main" class="hidden min-w-0 lg:block">
      <ul class="flex items-center gap-0.5 text-[.86rem] font-medium">
        <li><a href="#thd-01-main" aria-current="page" class="block rounded-lg px-2.5 py-1.5 text-thd01-mut transition-colors hover:bg-thd01-s2 hover:text-thd01-ink aria-[current=page]:bg-thd01-s2 aria-[current=page]:text-thd01-ink">Product</a></li>
        <li><a href="#thd-01-main" class="block rounded-lg px-2.5 py-1.5 text-thd01-mut transition-colors hover:bg-thd01-s2 hover:text-thd01-ink">Docs</a></li>
        <li><a href="#thd-01-main" class="block rounded-lg px-2.5 py-1.5 text-thd01-mut transition-colors hover:bg-thd01-s2 hover:text-thd01-ink">Changelog</a></li>
        <li><a href="#thd-01-main" class="block rounded-lg px-2.5 py-1.5 text-thd01-mut transition-colors hover:bg-thd01-s2 hover:text-thd01-ink">Pricing</a></li>
      </ul>
    </nav>

    <span class="group/cmd relative ml-auto block min-w-0 flex-none sm:mx-auto sm:max-w-[23rem] sm:flex-1">
      <input id="thd-01-open" type="checkbox" aria-label="Open command palette (Command K)" aria-haspopup="dialog" class="peer/cmd absolute inset-0 z-[2] m-0 size-full cursor-pointer appearance-none opacity-0">
      <span aria-hidden="true" class="flex min-h-11 items-center gap-2 rounded-xl border border-thd01-line bg-thd01-s1 py-1.5 pl-3 pr-1.5 text-sm text-thd01-mut transition group-hover/cmd:border-thd01-line2 group-hover/cmd:bg-thd01-s2 peer-focus-visible/cmd:border-thd01-acc peer-focus-visible/cmd:ring-4 peer-focus-visible/cmd:ring-thd01-acc/20">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" class="size-4 flex-none"><circle cx="11" cy="11" r="6.4"/><path d="m15.8 15.8 5.2 5.2"/></svg>
        <span class="hidden min-w-0 flex-1 truncate sm:block">Search or jump to&hellip;</span>
        <kbd class="rounded-md border border-thd01-line2 bg-thd01-s3 px-1.5 py-1 font-thd01-mono text-[11px] leading-none text-thd01-ink">&#8984;K</kbd>
      </span>
    </span>

    <div class="flex items-center gap-1.5 sm:ml-auto">
      <input id="thd-01-t" type="checkbox" class="peer/t sr-only">
      <label for="thd-01-t" class="grid size-11 cursor-pointer place-items-center rounded-full transition-colors hover:bg-thd01-ink/10 peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-offset-2 peer-focus-visible/t:outline-thd01-acc">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px] group-has-[#thd-01-t:checked]/thd01:hidden"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-01-t:checked]/thd01:block"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
        <span class="sr-only">Switch light or dark theme</span>
      </label>
      <a href="#thd-01-main" class="hidden rounded-lg px-3 py-2 text-[.86rem] font-medium text-thd01-mut transition-colors hover:text-thd01-ink md:block">Sign in</a>
      <a href="#thd-01-main" class="grid min-h-11 place-items-center whitespace-nowrap rounded-xl bg-thd01-acc px-4 text-[.86rem] font-semibold text-thd01-on shadow-[0_10px_28px_-10px_var(--color-thd01-acc)] transition hover:-translate-y-px hover:brightness-110">Get started</a>
    </div>
  </header>

  <div class="invisible fixed inset-0 z-50 flex items-start justify-center px-4 pt-[clamp(1rem,10svh,6rem)] opacity-0 transition-[opacity,visibility] duration-200 group-has-[#thd-01-open:checked]/thd01:visible group-has-[#thd-01-open:checked]/thd01:opacity-100">
    <label for="thd-01-open" aria-label="Close command palette" class="absolute inset-0 cursor-default bg-black/60 backdrop-blur-sm"></label>
    <div role="dialog" aria-modal="true" aria-label="Command palette" class="relative flex max-h-[min(32rem,80svh)] w-full max-w-[36rem] -translate-y-2 scale-[.965] flex-col overflow-hidden rounded-2xl border border-thd01-line2 bg-thd01-s1 shadow-[0_40px_80px_-16px_rgb(0_0_0/.7),0_24px_64px_-32px_var(--color-thd01-acc)] ring-1 ring-thd01-acc/15 transition duration-200 ease-[cubic-bezier(.2,.8,.2,1)] group-has-[#thd-01-open:checked]/thd01:translate-y-0 group-has-[#thd-01-open:checked]/thd01:scale-100">
      <div class="flex items-center gap-2.5 border-b border-thd01-line px-4 py-3">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px] flex-none text-thd01-mut"><circle cx="11" cy="11" r="6.4"/><path d="m15.8 15.8 5.2 5.2"/></svg>
        <input id="thd-01-q" type="text" autocomplete="off" placeholder="Type a command or search projects" aria-label="Command or search" class="min-w-0 flex-1 bg-transparent py-1 text-base text-thd01-ink outline-none placeholder:text-thd01-mut">
        <label for="thd-01-open" class="cursor-pointer rounded-md border border-thd01-line2 px-2 py-1 font-thd01-mono text-[11px] uppercase tracking-wider text-thd01-mut transition-colors hover:bg-thd01-s3 hover:text-thd01-ink">esc</label>
      </div>
      <div class="overflow-auto overscroll-contain p-2">
        <div data-group>
          <p id="thd-01-g1" class="px-2.5 pb-1 pt-2 text-[11px] font-semibold uppercase tracking-[.1em] text-thd01-mut">Recent</p>
          <ul role="menu" aria-labelledby="thd-01-g1">
            <li role="none" style="--i:1" class="group-has-[#thd-01-open:checked]/thd01:animate-thd01-in"><button data-row type="button" role="menuitem" class="group/row flex min-h-11 w-full items-center gap-3 rounded-lg px-2.5 text-left text-[.92rem] outline-none transition-colors hover:bg-thd01-acc/15 focus-visible:bg-thd01-acc/15"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true" class="size-[17px] flex-none text-thd01-mut group-hover/row:text-thd01-acc group-focus-visible/row:text-thd01-acc"><rect x="4" y="4.5" width="16" height="15" rx="2.6"/><path d="M8 9.5h8M8 13.5h5"/></svg><span class="min-w-0 flex-1 truncate">Q3 pricing experiment</span><span class="text-xs text-thd01-mut">Project</span></button></li>
            <li role="none" style="--i:2" class="group-has-[#thd-01-open:checked]/thd01:animate-thd01-in"><button data-row type="button" role="menuitem" class="group/row flex min-h-11 w-full items-center gap-3 rounded-lg px-2.5 text-left text-[.92rem] outline-none transition-colors hover:bg-thd01-acc/15 focus-visible:bg-thd01-acc/15"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" aria-hidden="true" class="size-[17px] flex-none text-thd01-mut group-hover/row:text-thd01-acc group-focus-visible/row:text-thd01-acc"><path d="M12 4.5 19.5 9v6L12 19.5 4.5 15V9L12 4.5Z"/></svg><span class="min-w-0 flex-1 truncate">Deploy pipeline &mdash; edge regions</span><span class="text-xs text-thd01-mut">Doc</span></button></li>
            <li role="none" style="--i:3" class="group-has-[#thd-01-open:checked]/thd01:animate-thd01-in"><button data-row type="button" role="menuitem" class="group/row flex min-h-11 w-full items-center gap-3 rounded-lg px-2.5 text-left text-[.92rem] outline-none transition-colors hover:bg-thd01-acc/15 focus-visible:bg-thd01-acc/15"><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-full bg-thd01-acc/20 text-[10px] font-bold text-thd01-acc">PS</span><span class="min-w-0 flex-1 truncate">Priya Sharma</span><span class="text-xs text-thd01-mut">Teammate</span></button></li>
          </ul>
        </div>
        <div data-group>
          <p id="thd-01-g2" class="px-2.5 pb-1 pt-3 text-[11px] font-semibold uppercase tracking-[.1em] text-thd01-mut">Actions</p>
          <ul role="menu" aria-labelledby="thd-01-g2">
            <li role="none" style="--i:4" class="group-has-[#thd-01-open:checked]/thd01:animate-thd01-in"><button data-row type="button" role="menuitem" class="group/row flex min-h-11 w-full items-center gap-3 rounded-lg px-2.5 text-left text-[.92rem] outline-none transition-colors hover:bg-thd01-acc/15 focus-visible:bg-thd01-acc/15"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true" class="size-[17px] flex-none text-thd01-mut group-hover/row:text-thd01-acc group-focus-visible/row:text-thd01-acc"><path d="M12 5v14M5 12h14"/></svg><span class="min-w-0 flex-1 truncate">New project</span><kbd class="rounded border border-thd01-line2 px-1.5 py-0.5 font-thd01-mono text-[11px] text-thd01-mut">N</kbd></button></li>
            <li role="none" style="--i:5" class="group-has-[#thd-01-open:checked]/thd01:animate-thd01-in"><button data-row type="button" role="menuitem" class="group/row flex min-h-11 w-full items-center gap-3 rounded-lg px-2.5 text-left text-[.92rem] outline-none transition-colors hover:bg-thd01-acc/15 focus-visible:bg-thd01-acc/15"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-[17px] flex-none text-thd01-mut group-hover/row:text-thd01-acc group-focus-visible/row:text-thd01-acc"><path d="M4.5 12h15M13 6.5l6 5.5-6 5.5"/></svg><span class="min-w-0 flex-1 truncate">Invite teammate</span><kbd class="rounded border border-thd01-line2 px-1.5 py-0.5 font-thd01-mono text-[11px] text-thd01-mut">I</kbd></button></li>
            <li role="none" style="--i:6" class="group-has-[#thd-01-open:checked]/thd01:animate-thd01-in"><button data-row type="button" role="menuitem" class="group/row flex min-h-11 w-full items-center gap-3 rounded-lg px-2.5 text-left text-[.92rem] outline-none transition-colors hover:bg-thd01-acc/15 focus-visible:bg-thd01-acc/15"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true" class="size-[17px] flex-none text-thd01-mut group-hover/row:text-thd01-acc group-focus-visible/row:text-thd01-acc"><circle cx="12" cy="12" r="3.4"/><path d="M12 3.4v2.2M12 18.4v2.2M3.4 12h2.2M18.4 12h2.2M6 6l1.6 1.6M16.4 16.4 18 18M18 6l-1.6 1.6M7.6 16.4 6 18"/></svg><span class="min-w-0 flex-1 truncate">Toggle appearance</span><kbd class="rounded border border-thd01-line2 px-1.5 py-0.5 font-thd01-mono text-[11px] text-thd01-mut">T</kbd></button></li>
          </ul>
        </div>
        <div data-group>
          <p id="thd-01-g3" class="px-2.5 pb-1 pt-3 text-[11px] font-semibold uppercase tracking-[.1em] text-thd01-mut">Help</p>
          <ul role="menu" aria-labelledby="thd-01-g3">
            <li role="none" style="--i:7" class="group-has-[#thd-01-open:checked]/thd01:animate-thd01-in"><button data-row type="button" role="menuitem" class="group/row flex min-h-11 w-full items-center gap-3 rounded-lg px-2.5 text-left text-[.92rem] outline-none transition-colors hover:bg-thd01-acc/15 focus-visible:bg-thd01-acc/15"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true" class="size-[17px] flex-none text-thd01-mut group-hover/row:text-thd01-acc group-focus-visible/row:text-thd01-acc"><circle cx="12" cy="12" r="8.2"/><path d="M9.8 9.6a2.3 2.3 0 1 1 3.4 2.1c-.8.5-1.2 1-1.2 1.9M12 16.6h.01"/></svg><span class="min-w-0 flex-1 truncate">Keyboard shortcuts</span><span class="text-xs text-thd01-mut">Help</span></button></li>
          </ul>
        </div>
        <p id="thd-01-empty" hidden class="px-3 py-8 text-center text-sm text-thd01-mut">No matches &mdash; try &ldquo;deploy&rdquo; or &ldquo;invite&rdquo;.</p>
      </div>
      <p class="flex items-center gap-1.5 border-t border-thd01-line px-4 py-2.5 text-xs text-thd01-mut"><kbd class="rounded border border-thd01-line2 px-1.5 font-thd01-mono">&#8593;</kbd><kbd class="rounded border border-thd01-line2 px-1.5 font-thd01-mono">&#8595;</kbd> navigate <span aria-hidden="true" class="mx-1.5 h-3.5 w-px bg-thd01-line2"></span><kbd class="rounded border border-thd01-line2 px-1.5 font-thd01-mono">&#8629;</kbd> select</p>
    </div>
  </div>

  <main id="thd-01-main" class="mx-auto max-w-6xl px-[clamp(1rem,4vw,2.5rem)] pb-16 pt-[clamp(2.5rem,8vw,5.5rem)]">
    <p class="mb-4 inline-flex items-center gap-2 rounded-full border border-thd01-line bg-thd01-s1 px-3 py-1 text-xs font-medium text-thd01-mut"><span class="size-1.5 rounded-full bg-thd01-acc shadow-[0_0_8px_var(--color-thd01-acc)]"></span>Changelog &middot; 25 Sep</p>
    <h1 class="max-w-[22ch] text-[clamp(2rem,6vw,3.6rem)] font-bold leading-[1.03] tracking-[-.035em] text-balance">Ship the whole surface, not the strip.</h1>
    <p class="mt-4 max-w-[52ch] text-[1.05rem] text-thd01-mut text-pretty">Press <kbd class="rounded border border-thd01-line2 px-1.5 font-thd01-mono text-sm">&#8984;K</kbd> anywhere &mdash; or tab to the pill and hit space. Type to filter, arrow keys to move. Scroll and the bar tightens against the content.</p>
    <ul class="mt-[clamp(2rem,6vw,3.5rem)] grid grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))] gap-3">
      <li class="rounded-2xl border border-thd01-line bg-thd01-s1 p-5"><h2 class="text-[.95rem] font-semibold">Edge routing</h2><p class="mt-1.5 text-sm text-thd01-mut">Region-aware requests with a 24&nbsp;ms median hop between London and Dublin.</p></li>
      <li class="rounded-2xl border border-thd01-line bg-thd01-s1 p-5"><h2 class="text-[.95rem] font-semibold">Preview envs</h2><p class="mt-1.5 text-sm text-thd01-mut">Every branch gets an isolated database seeded from the last good snapshot.</p></li>
      <li class="rounded-2xl border border-thd01-line bg-thd01-s1 p-5"><h2 class="text-[.95rem] font-semibold">Audit trail</h2><p class="mt-1.5 text-sm text-thd01-mut">Immutable event log, exportable to your own bucket on a nightly schedule.</p></li>
      <li class="rounded-2xl border border-thd01-line bg-thd01-s1 p-5"><h2 class="text-[.95rem] font-semibold">Insights</h2><p class="mt-1.5 text-sm text-thd01-mut">Cold-start, cache-hit and error budgets in one pane, refreshed each minute.</p></li>
    </ul>
    <div aria-hidden="true" class="h-[70svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";
/* Palette tokens are inline so utilities resolve the root's live custom properties —
   that is what lets the checkbox swap the whole theme with zero JS. */

@theme inline {
  --color-thd01-s0: var(--thd01-s0);
  --color-thd01-s1: var(--thd01-s1);
  --color-thd01-s2: var(--thd01-s2);
  --color-thd01-s3: var(--thd01-s3);
  --color-thd01-ink: var(--thd01-ink);
  --color-thd01-mut: var(--thd01-mut);
  --color-thd01-line: var(--thd01-line);
  --color-thd01-line2: var(--thd01-line2);
  --color-thd01-acc: var(--thd01-acc);
  --color-thd01-on: var(--thd01-on);
  --color-thd01-glow: var(--thd01-glow);
}

@theme {
  --font-thd01-sans: 'Geist', system-ui, sans-serif;
  --font-thd01-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-thd01-in: thd01-in 280ms cubic-bezier(0.2,0.8,0.2,1) calc(var(--i, 1) * 28ms + 40ms) backwards;

  @keyframes thd01-in {
    from {
      opacity: 0;
      translate: 0 0.45rem;
    }
  }
}

.thd-01 {
  width: 100%;
  min-height: 100svh;
  --thd01-s0: #0b0a12;
  --thd01-s1: #12111b;
  --thd01-s2: #1a1926;
  --thd01-s3: #232231;
  --thd01-ink: #f4f3fa;
  --thd01-mut: #a4a2b8;
  --thd01-line: rgb(255 255 255 / 0.09);
  --thd01-line2: rgb(255 255 255 / 0.17);
  --thd01-acc: #a78bfa;
  --thd01-on: #13092a;
  --thd01-glow: rgb(167 139 250 / 0.17);
}

.thd-01:has(#thd-01-t:checked) {
  --thd01-s0: #fbfbfd;
  --thd01-s1: #ffffff;
  --thd01-s2: #f1f0f7;
  --thd01-s3: #e7e6f0;
  --thd01-ink: #0e0d16;
  --thd01-mut: #57556b;
  --thd01-line: rgb(14 13 22 / 0.1);
  --thd01-line2: rgb(14 13 22 / 0.18);
  --thd01-acc: #6d28d9;
  --thd01-on: #ffffff;
  --thd01-glow: rgb(109 40 217 / 0.1);
}

@utility thd01-tighten {
  @supports (animation-timeline: scroll()) {
    animation: thd01-tighten linear both;
    animation-timeline: scroll(root);
    animation-range: 0 160px;
  }
}

@keyframes thd01-tighten {
  from {
    background-color: transparent;
  }

  to {
    background-color: color-mix(in srgb, var(--thd01-s1) 90%, transparent);
    border-bottom-color: var(--thd01-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .thd-01 * {
    animation-duration: 1ms !important;
    transition-duration: 1ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.thd-01');
  if (!root) return;
  const box = root.querySelector('#thd-01-open');
  const input = root.querySelector('#thd-01-q');
  const empty = root.querySelector('#thd-01-empty');
  const rows = [...root.querySelectorAll('[data-row]')];
  const focusInput = () => setTimeout(() => input.focus(), 30);
  const setOpen = (on) => { box.checked = on; on ? focusInput() : box.focus(); };
  document.addEventListener('keydown', (e) => {
    const k = e.key.toLowerCase();
    if ((e.metaKey || e.ctrlKey) && k === 'k') { e.preventDefault(); setOpen(!box.checked); }
    else if (k === 'escape' && box.checked) setOpen(false);
    else if (box.checked && (k === 'arrowdown' || k === 'arrowup')) {
      e.preventDefault();
      const vis = rows.filter((r) => !r.parentElement.hidden);
      const i = vis.indexOf(document.activeElement);
      (k === 'arrowdown' ? vis[i + 1] || vis[0] : vis[i - 1] || input)?.focus();
    }
  });
  box.addEventListener('change', () => box.checked && focusInput());
  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    let hits = 0;
    rows.forEach((r) => { const ok = r.textContent.toLowerCase().includes(q); r.parentElement.hidden = !ok; hits += ok; });
    root.querySelectorAll('[data-group]').forEach((g) => { g.hidden = !g.querySelector('li:not([hidden])'); });
    empty.hidden = hits > 0;
  });
})();
```
