---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-mobile-hamburger-menu-glass-off-canvas-drawer/"
title: "Tailwind Mobile Hamburger Menu with Glass Off-Canvas Drawer"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "A hamburger that slides in a frosted off-canvas drawer over a blurred scrim."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mobile Hamburger Menu with Glass Off-Canvas Drawer
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-mobile-hamburger-menu-glass-off-canvas-drawer/

A hamburger that slides in a frosted off-canvas drawer over a blurred scrim. The CSS original used the checkbox hack, which is invisible to keyboards and screen readers; the port uses the Popover API &mdash; a real <button popovertarget>, Esc to close, light dismiss, focus returned to the trigger &mdash; still with zero JavaScript.
## HTML
```html
<div class="tgn-06 w-full min-h-svh bg-tgn06-b bg-[radial-gradient(100%_100%_at_80%_0%,var(--color-tgn06-a),var(--color-tgn06-b)_45%,var(--color-tgn06-c)_100%)] font-tgn06-sans">
  <div class="relative h-svh overflow-x-hidden overflow-y-auto scroll-smooth">
    <header class="sticky top-4 z-10 m-4 flex h-15 items-center justify-between rounded-2xl border border-white/55 bg-white/40 pr-2 pl-5 shadow-[0_10px_30px_-10px_oklch(0.3_0.12_20/0.45)] backdrop-blur-[14px] backdrop-saturate-[1.7] not-supports-[backdrop-filter:blur(1px)]:bg-tgn06-c/90">
      <a class="rounded-md text-lg font-bold tracking-[-0.02em] text-white [text-shadow:0_1px_6px_oklch(0.3_0.12_20/0.35)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white" href="#">Meridian</a>
      <button type="button" popovertarget="tgn06-drawer" aria-label="Open menu" class="group grid size-11 cursor-pointer place-items-center rounded-xl text-white transition-colors hover:bg-white/25 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
        <svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10" class="transition-[d] duration-200 group-hover:[d:path('M4_7h16M4_12h16M4_17h16')] motion-reduce:transition-none"/></svg>
      </button>
    </header>
    <div class="mx-auto max-w-2xl px-6 pt-8 pb-20 text-white [text-shadow:0_1px_6px_oklch(0.3_0.12_20/0.45)] [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:text-white [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn06-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:border [&_code]:border-white/35 [&_code]:bg-white/25 [&_code]:text-white [&_code]:[text-shadow:none]">
      <h2>Tap the hamburger § scroll to feel the sticky bar</h2>
      <p>The top bar stays pinned as the page moves. Tap the burger and a full-height drawer slides in over a heavily-blurred scrim, so the page shows through as soft frosted colour.</p>
      <p>The scrim is the star. Instead of dimming to grey, it covers the viewport with <code>backdrop-filter:blur(16px)</code> and a faint dark tint — the page behind melts into frosted colour rather than getting hidden.</p>
      <p>Toggle is the CSS checkbox hack: a visually-hidden checkbox whose label is the hamburger. When <code>:checked</code>, a general-sibling selector reveals the scrim and slides the drawer in. Zero JavaScript for the whole open/close mechanic.</p>
      <p>The drawer itself is a second glass surface sliding in with <code>transform:translateX</code>. Transform-based motion runs on the compositor, so the slide stays smooth even during heavy scroll.</p>
      <h3>The full production upgrade path</h3>
      <p>The checkbox-hack is honest about its trade-offs. It has no focus trap, no Esc-to-close, and screen readers announce the toggle as a checkbox rather than a disclosure button. Fine for a demo, wrong for a real product.</p>
      <p>For production, upgrade the checkbox to a <code>&lt;button aria-expanded&gt;</code> plus ~20 lines of vanilla JS. Focus-trap on the drawer while it's open. Esc key closes and returns focus to the trigger. Scrim click closes.</p>
      <p>Body scroll lock when the drawer is open. <code>document.documentElement.style.overflow = 'hidden'</code> when opening, restore on close. This prevents the background from scrolling behind the drawer on iOS Safari.</p>
      <p>The visual layer stays byte-for-byte identical — the CSS never changes. Only the accessibility infrastructure gets upgraded. The user sees the same glass drawer with the same slide animation and the same scrim.</p>
      <h3>Slide direction and anchor variants</h3>
      <p>Slide from the right instead by starting the drawer at <code>translateX(100%)</code> and anchoring it <code>right:0</code>. Same structure, mirrored anchor. Right-slide is more common on Arabic/Hebrew locale sites (RTL matches natural reading direction).</p>
      <p>Slide from the bottom for a mobile-web-app feel: start at <code>translateY(100%)</code>, anchor <code>bottom:0</code>, make the drawer full-width and short-height. This mimics native iOS action sheets and Android bottom sheets.</p>
      <p>Slide from the top for a full-screen menu overlay: start at <code>translateY(-100%)</code>, anchor <code>top:0</code>, full width AND full height. Reads as an app-shell menu take-over, not a side drawer.</p>
      <p>Stagger the drawer link entrances with <code>transition-delay</code> steps (say 40ms per link) for a cascading reveal that feels premium. Keep the total stagger under 200ms so the drawer feels responsive.</p>
      <h3>Common failure modes</h3>
      <p><code>position:fixed</code> inside a transformed or filtered ancestor is positioned relative to that ancestor, not the viewport. If your drawer is inside a component tree with transforms, promote it to a portal / top-layer container.</p>
      <p>Give the drawer a solid-enough fill (55-65% opacity or higher). Pure blur with a low-opacity fill makes link text hard to read when the drawer sits over a busy background page.</p>
      <p>Blur the scrim, not the drawer's parent. Blurring an ancestor of the drawer will blur the drawer's text too — the drawer needs to be either a sibling of the scrim or promoted to the top layer.</p>
      <p>Focus trap needs to move focus back to the trigger button on close, not fling it to <code>document.body</code>. Screen reader users lose their place otherwise.</p>
      <h3>When to use the checkbox-hack anyway</h3>
      <p>Prototyping. Storybook demos. Marketing sites without accessibility requirements. Personal portfolio sites where you're the only user. Educational examples that focus on the CSS technique, not the compliance.</p>
      <p>Never for a shipping product. The audit will catch it, and the audit is right.</p>
      <p>Keep scrolling — the sticky bar demonstrates its pin as the page content flows beneath it.</p>
    </div>
  </div>
  <aside id="tgn06-drawer" popover aria-label="Menu" class="fixed inset-y-0 right-auto left-0 m-0 flex h-dvh max-h-none w-[min(84%,320px)] flex-col border-0 border-r border-white/60 bg-white/62 p-5 font-tgn06-sans text-tgn06-ink shadow-[8px_0_40px_-8px_oklch(0.3_0.12_20/0.4)] backdrop-blur-[22px] backdrop-saturate-[1.8] -translate-x-full transition-[translate,overlay,display] transition-discrete duration-300 ease-[cubic-bezier(.4,0,.2,1)] open:translate-x-0 starting:open:-translate-x-full backdrop:bg-tgn06-scrim/30 backdrop:backdrop-blur-md not-supports-[backdrop-filter:blur(1px)]:bg-white motion-reduce:transition-none">
    <div class="flex items-center justify-between">
      <span class="text-lg font-bold tracking-[-0.02em]">Meridian</span>
      <button type="button" popovertarget="tgn06-drawer" popovertargetaction="hide" aria-label="Close menu" class="grid size-11 cursor-pointer place-items-center rounded-xl text-tgn06-ink transition-colors hover:bg-white/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn06-acc"><svg class="size-5" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 5l10 10M15 5 5 15"/></svg></button>
    </div>
    <nav aria-label="Mobile primary" class="mt-8 flex flex-col gap-1">
      <a href="#" aria-current="page" class="flex h-12 items-center rounded-xl px-4 text-[17px] font-semibold text-tgn06-ink transition-[background-color,opacity,translate] duration-300 hover:bg-white/60 aria-[current=page]:bg-white/60 aria-[current=page]:text-tgn06-acc starting:-translate-x-3 starting:opacity-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn06-acc motion-reduce:transition-none">Home</a>
      <a href="#" class="flex h-12 items-center rounded-xl px-4 text-[17px] font-semibold text-tgn06-ink transition-[background-color,opacity,translate] duration-300 hover:bg-white/60 aria-[current=page]:bg-white/60 aria-[current=page]:text-tgn06-acc starting:-translate-x-3 starting:opacity-0 delay-[120ms] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn06-acc motion-reduce:transition-none">Collections</a>
      <a href="#" class="flex h-12 items-center rounded-xl px-4 text-[17px] font-semibold text-tgn06-ink transition-[background-color,opacity,translate] duration-300 hover:bg-white/60 aria-[current=page]:bg-white/60 aria-[current=page]:text-tgn06-acc starting:-translate-x-3 starting:opacity-0 delay-[160ms] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn06-acc motion-reduce:transition-none">Journal</a>
      <a href="#" class="flex h-12 items-center rounded-xl px-4 text-[17px] font-semibold text-tgn06-ink transition-[background-color,opacity,translate] duration-300 hover:bg-white/60 aria-[current=page]:bg-white/60 aria-[current=page]:text-tgn06-acc starting:-translate-x-3 starting:opacity-0 delay-[200ms] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn06-acc motion-reduce:transition-none">About</a>
      <a href="#" class="flex h-12 items-center rounded-xl px-4 text-[17px] font-semibold text-tgn06-ink transition-[background-color,opacity,translate] duration-300 hover:bg-white/60 aria-[current=page]:bg-white/60 aria-[current=page]:text-tgn06-acc starting:-translate-x-3 starting:opacity-0 delay-[240ms] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn06-acc motion-reduce:transition-none">Contact</a>
    </nav>
    <a href="#" class="mt-auto flex h-12 items-center justify-center rounded-xl bg-tgn06-ink text-[15px] font-semibold text-white transition-colors hover:bg-tgn06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn06-acc">Book a visit</a>
  </aside>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgn06-a: #fc9e47;
  --color-tgn06-a: oklch(0.78 0.15 60);
  --color-tgn06-b: #d64651;
  --color-tgn06-b: oklch(0.6 0.18 20);
  --color-tgn06-c: #73176f;
  --color-tgn06-c: oklch(0.4 0.16 330);
  --color-tgn06-ink: #3e1e1e;
  --color-tgn06-ink: oklch(0.28 0.05 20);
  --color-tgn06-acc: #b71532;
  --color-tgn06-acc: oklch(0.5 0.19 20);
  --color-tgn06-scrim: #250e0e;
  --color-tgn06-scrim: oklch(0.2 0.04 20);
  --font-tgn06-sans: 'Sora', system-ui, sans-serif;
  --font-tgn06-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-06 {
  width: 100%;
  min-height: 100svh;
}
```
