---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-glassmorphism-dropdown-mega-menu-navbar/"
title: "Tailwind Glassmorphism Dropdown & Mega Menu Navbar"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "A glass bar with a three-column mega menu and a compact dropdown, both frosted, both pure CSS via named groups (group/item)."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Dropdown & Mega Menu Navbar
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-glassmorphism-dropdown-mega-menu-navbar/

A glass bar with a three-column mega menu and a compact dropdown, both frosted, both pure CSS via named groups (group/item). The port also fixes the double-blur bug: the bar's frost moves to a before: layer, so the bar is no longer a backdrop root and the panels inside it blur the real page instead of a flat grey copy of the bar.
## HTML
```html
<div class="tgn-05 w-full min-h-svh bg-tgn05-b bg-linear-135 from-tgn05-a via-tgn05-b to-tgn05-c font-tgn05-sans">
  <div class="relative h-svh overflow-y-auto scroll-smooth p-3 sm:p-5">
    <header class="isolate sticky top-0 z-10 flex h-15 items-center gap-4 rounded-2xl border border-white/60 px-4 shadow-[0_8px_28px_-6px_oklch(0.3_0.12_15/0.35)] before:absolute before:inset-0 before:-z-10 before:rounded-[inherit] before:bg-white/50 before:backdrop-blur-lg before:backdrop-saturate-[1.8] not-supports-[backdrop-filter:blur(1px)]:before:bg-white/92 max-sm:h-14 max-sm:gap-1 max-sm:px-3 sm:gap-6 sm:px-5">
      <a class="flex items-center gap-2 rounded-md text-lg font-extrabold tracking-[-0.02em] text-tgn05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc" href="#"><svg class="size-5 text-tgn05-acc" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M2 10h16M10 2c3 3 3 13 0 16M10 2c-3 3-3 13 0 16" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>Atlas</a>
      <nav aria-label="Primary" class="max-sm:ml-auto">
        <ul class="flex">
          <li class="max-sm:hidden"><a href="#" aria-current="page" class="flex h-15 cursor-pointer items-center gap-1.5 px-3.5 text-sm font-semibold text-tgn05-ink transition-colors hover:text-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc max-sm:h-14 max-sm:px-2.5 aria-[current=page]:text-tgn05-acc">Home</a></li>
          <li class="group/item relative">
            <button type="button" aria-haspopup="true" class="flex h-15 cursor-pointer items-center gap-1.5 px-3.5 text-sm font-semibold text-tgn05-ink transition-colors hover:text-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc max-sm:h-14 max-sm:px-2.5">Products <svg class="size-3.5 transition-transform duration-200 group-hover/item:rotate-180 group-focus-within/item:rotate-180 motion-reduce:transition-none" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m4 6 4 4 4-4"/></svg></button>
            <div class="invisible absolute top-[calc(100%+6px)] left-0 z-20 rounded-2xl border border-white/70 bg-white/70 p-3 opacity-0 shadow-[0_18px_44px_-10px_oklch(0.3_0.12_15/0.4)] backdrop-blur-[18px] backdrop-saturate-[1.8] -translate-y-1.5 transition-[opacity,translate,visibility] duration-200 before:absolute before:inset-x-0 before:-top-2 before:h-2 group-hover/item:visible group-hover/item:translate-y-0 group-hover/item:opacity-100 group-focus-within/item:visible group-focus-within/item:translate-y-0 group-focus-within/item:opacity-100 motion-reduce:transition-none not-supports-[backdrop-filter:blur(1px)]:bg-white max-sm:fixed max-sm:inset-x-3 max-sm:top-[82px] grid w-max grid-cols-3 gap-x-2 max-sm:w-auto max-sm:grid-cols-1">
              <div><h4 class="mb-1 px-3 pt-1 text-[11px] font-bold tracking-[0.12em] text-tgn05-mut uppercase">Build</h4><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">Editor</span><span class="mt-0.5 block text-xs text-tgn05-mut">Write and preview live</span></a><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">CLI</span><span class="mt-0.5 block text-xs text-tgn05-mut">Scaffold from the terminal</span></a><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">SDK</span><span class="mt-0.5 block text-xs text-tgn05-mut">Typed clients for every API</span></a></div>
              <div><h4 class="mb-1 px-3 pt-1 text-[11px] font-bold tracking-[0.12em] text-tgn05-mut uppercase">Ship</h4><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">Deploy</span><span class="mt-0.5 block text-xs text-tgn05-mut">Git push to global edge</span></a><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">Analytics</span><span class="mt-0.5 block text-xs text-tgn05-mut">Real-user Web Vitals</span></a><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">Edge</span><span class="mt-0.5 block text-xs text-tgn05-mut">Run code near users</span></a></div>
              <div class="max-sm:hidden"><h4 class="mb-1 px-3 pt-1 text-[11px] font-bold tracking-[0.12em] text-tgn05-mut uppercase">Scale</h4><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">Teams</span><span class="mt-0.5 block text-xs text-tgn05-mut">Roles, SSO and audit logs</span></a><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">Security</span><span class="mt-0.5 block text-xs text-tgn05-mut">SOC 2 Type II, SAML</span></a><a href="#" class="block rounded-xl px-3 py-2.5 transition-colors hover:bg-white/75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc"><span class="block text-[13.5px] font-semibold text-tgn05-ink">SLA</span><span class="mt-0.5 block text-xs text-tgn05-mut">99.99% uptime, in writing</span></a></div>
            </div>
          </li>
          <li class="group/item relative">
            <button type="button" aria-haspopup="true" class="flex h-15 cursor-pointer items-center gap-1.5 px-3.5 text-sm font-semibold text-tgn05-ink transition-colors hover:text-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc max-sm:h-14 max-sm:px-2.5">Company <svg class="size-3.5 transition-transform duration-200 group-hover/item:rotate-180 group-focus-within/item:rotate-180 motion-reduce:transition-none" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m4 6 4 4 4-4"/></svg></button>
            <div class="invisible absolute top-[calc(100%+6px)] left-0 z-20 rounded-2xl border border-white/70 bg-white/70 p-3 opacity-0 shadow-[0_18px_44px_-10px_oklch(0.3_0.12_15/0.4)] backdrop-blur-[18px] backdrop-saturate-[1.8] -translate-y-1.5 transition-[opacity,translate,visibility] duration-200 before:absolute before:inset-x-0 before:-top-2 before:h-2 group-hover/item:visible group-hover/item:translate-y-0 group-hover/item:opacity-100 group-focus-within/item:visible group-focus-within/item:translate-y-0 group-focus-within/item:opacity-100 motion-reduce:transition-none not-supports-[backdrop-filter:blur(1px)]:bg-white max-sm:fixed max-sm:inset-x-3 max-sm:top-[82px] flex min-w-48 flex-col gap-0.5 max-sm:min-w-0"><a href="#" class="flex h-10 items-center rounded-lg px-3 text-[13.5px] font-semibold text-tgn05-ink transition-colors hover:bg-white/75 hover:text-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc">About</a><a href="#" class="flex h-10 items-center rounded-lg px-3 text-[13.5px] font-semibold text-tgn05-ink transition-colors hover:bg-white/75 hover:text-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc">Careers</a><a href="#" class="flex h-10 items-center rounded-lg px-3 text-[13.5px] font-semibold text-tgn05-ink transition-colors hover:bg-white/75 hover:text-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc">Blog</a><a href="#" class="flex h-10 items-center rounded-lg px-3 text-[13.5px] font-semibold text-tgn05-ink transition-colors hover:bg-white/75 hover:text-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc">Press</a></div>
          </li>
          <li class="max-sm:hidden"><a href="#" class="flex h-15 cursor-pointer items-center gap-1.5 px-3.5 text-sm font-semibold text-tgn05-ink transition-colors hover:text-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc max-sm:h-14 max-sm:px-2.5">Pricing</a></li>
        </ul>
      </nav>
      <a href="#" class="ml-auto flex h-10 items-center rounded-xl bg-tgn05-ink px-4 text-[13.5px] font-bold text-white transition-colors hover:bg-tgn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn05-acc max-md:hidden">Get Atlas</a>
    </header>
    <div class="mx-auto max-w-2xl px-2 pt-12 pb-20 text-white [text-shadow:0_1px_6px_oklch(0.3_0.12_15/0.4)] [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:text-white [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn05-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:border [&_code]:border-white/35 [&_code]:bg-white/25 [&_code]:text-white [&_code]:[text-shadow:none]">
      <h2>Hover Products § the mega-menu opens as glass-on-glass</h2>
      <p>The sticky bar frosts the page behind it. The dropdown panels frost the page behind THEM — not the bar — because they're absolutely-positioned siblings anchored to each menu item, not nested inside the bar's blurred surface.</p>
      <p>This dodges the notorious double-blur bug: nesting a <code>backdrop-filter</code> element inside another <code>backdrop-filter</code> element makes the child blur its parent's already-blurred output, producing muddy compound frost and clipping artefacts.</p>
      <p>Open/close is pure CSS. The panels live at <code>opacity:0; visibility:hidden</code> and reveal on <code>li:hover</code> AND <code>li:focus-within</code>, so mouse and keyboard both work. Tabbing into a link inside the panel keeps it open.</p>
      <p>Entrance is animated with <code>@starting-style</code> and <code>transition-behavior:allow-discrete</code> — the modern way to tween an element from <code>display:none</code>. Without both, the panel pops in with no transition.</p>
      <h3>The double-blur bug, illustrated</h3>
      <p>If you nest the panel inside the bar's DOM (a natural place to put it), the panel's <code>backdrop-filter</code> tries to blur the bar's already-blurred pixels. The result reads as a compound frost with visible seams where the two filter regions meet.</p>
      <p>The fix is structural: the panel must be a DOM sibling to the bar, or an absolutely-positioned child of a non-blurred ancestor. Both panels in this demo are children of each <code>&lt;li&gt;</code> with <code>position:absolute; top:calc(100% + 8px)</code>.</p>
      <p>Because the panel is outside the bar's blur surface, it samples the actual page pixels beneath it. Both surfaces frost the same underlying content at the same strength — no compounding, no seams.</p>
      <p>The same rule applies to modals, tooltips, popovers, and any other glass surface that appears above another glass surface. Never nest; always sibling or promote to a portal-style top-layer container.</p>
      <h3>Frost strength ratios</h3>
      <p>Match the two frost strengths deliberately. Identical blur on bar and panel reads as one material. A slightly stronger panel blur reads as closer to the viewer — use that when the panel needs perceptual lift over the bar.</p>
      <p>This demo uses <code>blur(16px) saturate(180%)</code> on the bar and <code>blur(18px) saturate(180%)</code> on the panel. The 2px difference is imperceptible in isolation but reads as depth when they're stacked visually.</p>
      <p>Never blur the panel more than 24px. Above that, the sampling artefact starts to show as a moiré pattern where the panel's blur circle overlaps busy background content.</p>
      <h3>Mega-menu vs dropdown structural difference</h3>
      <p>Widen the panel and switch its layout to <code>grid-template-columns:repeat(3, 1fr)</code> for a mega-menu; keep it narrow with a column of links for a classic dropdown. Same structural pattern, different scale.</p>
      <p>The mega-menu here has three columns: Build, Ship, Scale. Each column carries a small caps heading and a link stack. On mobile widths (below 640px), collapse to a single column with <code>grid-template-columns: 1fr</code>.</p>
      <p>Add a hover-intent delay with <code>transition-delay</code> on the close so the panel doesn't vanish if the pointer clips a corner while moving toward the links.</p>
      <h3>Accessibility contract</h3>
      <p>Every trigger has <code>aria-haspopup="true"</code> so screen readers announce it as opening a submenu. The chevron in the trigger text is a Unicode down-triangle character — announced but decorative.</p>
      <p>Keyboard: focus lands on the trigger, panel opens on focus (via <code>:focus-within</code> on the <code>&lt;li&gt;</code>), tab moves through the panel links, tabbing out of the last link closes the panel and moves to the next top-level trigger.</p>
      <p>Screen readers announce the panel as a menu because the trigger has <code>aria-haspopup</code>. For richer control, add <code>role="menu"</code> to the panel and <code>role="menuitem"</code> to each link — but that's optional for a browse-to-navigate mega menu.</p>
      <p>Add <code>aria-expanded</code> that flips true/false on hover/focus if the pattern needs the announcement. For hover-driven menus (this pattern), most teams skip the announcement to keep the SR experience quiet.</p>
      <p>Keep scrolling — the sticky bar and its dropdowns stay ready to hover as the content passes underneath.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgn05-a: #f3625d;
  --color-tgn05-a: oklch(0.68 0.18 25);
  --color-tgn05-b: #cd4290;
  --color-tgn05-b: oklch(0.6 0.19 350);
  --color-tgn05-c: #6351ca;
  --color-tgn05-c: oklch(0.52 0.18 285);
  --color-tgn05-ink: #3f181d;
  --color-tgn05-ink: oklch(0.27 0.06 15);
  --color-tgn05-mut: #6a4c4e;
  --color-tgn05-mut: oklch(0.45 0.04 15);
  --color-tgn05-acc: #b9003d;
  --color-tgn05-acc: oklch(0.5 0.2 15);
  --font-tgn05-sans: 'Onest', system-ui, sans-serif;
  --font-tgn05-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-05 {
  width: 100%;
  min-height: 100svh;
}
```
