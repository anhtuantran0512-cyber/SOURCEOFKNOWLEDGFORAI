---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-team-avatar-hover-card-presence-quick-actions/"
title: "Tailwind Team Avatar Hover Card with Presence and Quick Actions"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "Initials avatars that lift on hover and pop a compact profile: gradient hero band, ringed portrait, role, presence, bio, three stats and two actions."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Team Avatar Hover Card with Presence and Quick Actions
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-team-avatar-hover-card-presence-quick-actions/

Initials avatars that lift on hover and pop a compact profile: gradient hero band, ringed portrait, role, presence, bio, three stats and two actions. The port's honest finding is that per-person gradients are data, so they stay inline as bg-linear-to-br from-[#6028a0] to-[#9060d0] while the card shell &mdash; identical four times &mdash; moves into one @apply class.
## HTML
```html
<section class="ttp-09 w-full min-h-svh flex items-end justify-center bg-white px-7 pt-[300px] pb-10 font-ttp09-sans">
  <div class="flex flex-wrap justify-center gap-3.5">

    <div class="group relative">
      <button type="button" aria-label="Sarah Lindqvist, CEO" aria-describedby="ttp09-p1" class="ttp09-circle bg-linear-to-br from-[#6028a0] to-[#9060d0]">SL</button>
      <div id="ttp09-p1" role="tooltip" class="ttp09-card">
        <div class="relative h-14 bg-linear-to-br from-[#4a1880] to-[#8050c0]"><div class="ttp09-photo bg-linear-to-br from-[#6028a0] to-[#9060d0]">SL</div></div>
        <div class="px-3.5 pt-5 pb-3">
          <div class="text-sm font-semibold text-ttp09-ink">Sarah Lindqvist</div>
          <div class="mt-0.5 text-[10.5px] text-ttp09-muted">CEO · Executive</div>
          <div class="mt-1.5 flex items-center gap-1.25 text-[10.5px] text-ttp09-muted"><span class="h-1.5 w-1.5 rounded-full bg-ttp09-online"></span>Active now</div>
          <div class="mt-2 text-[11.5px] leading-[1.5] text-ttp09-body">Former Stripe PM. Building the next layer of financial infrastructure for SMBs.</div>
          <div class="mt-3 grid grid-cols-3 border-t border-ttp09-rule pt-2.75 text-center">
            <div><div class="text-[15px] font-bold text-ttp09-ink">214</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Team</div></div>
            <div><div class="text-[15px] font-bold text-ttp09-ink">8yr</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Tenure</div></div>
            <div><div class="text-[15px] font-bold text-ttp09-ink">$1.2B</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Valuation</div></div>
          </div>
        </div>
        <div class="flex gap-1.5 border-t border-ttp09-rule px-3.5 py-2.25">
          <button type="button" class="ttp09-btn">Message</button>
          <button type="button" class="ttp09-btn ttp09-btn-prim">View Profile</button>
        </div>
      </div>
    </div>

    <div class="group relative">
      <button type="button" aria-label="Marcus Webb, CTO" aria-describedby="ttp09-p2" class="ttp09-circle bg-linear-to-br from-[#204080] to-[#4070c0]">MW</button>
      <div id="ttp09-p2" role="tooltip" class="ttp09-card">
        <div class="relative h-14 bg-linear-to-br from-[#102060] to-[#3060a0]"><div class="ttp09-photo bg-linear-to-br from-[#204080] to-[#4070c0]">MW</div></div>
        <div class="px-3.5 pt-5 pb-3">
          <div class="text-sm font-semibold text-ttp09-ink">Marcus Webb</div>
          <div class="mt-0.5 text-[10.5px] text-ttp09-muted">CTO · Engineering</div>
          <div class="mt-1.5 flex items-center gap-1.25 text-[10.5px] text-ttp09-muted"><span class="h-1.5 w-1.5 rounded-full bg-ttp09-online"></span>Active now</div>
          <div class="mt-2 text-[11.5px] leading-[1.5] text-ttp09-body">Ex-Google infra. Obsessed with distributed systems and making things fast at scale.</div>
          <div class="mt-3 grid grid-cols-3 border-t border-ttp09-rule pt-2.75 text-center">
            <div><div class="text-[15px] font-bold text-ttp09-ink">96</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Team</div></div>
            <div><div class="text-[15px] font-bold text-ttp09-ink">5yr</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Tenure</div></div>
            <div><div class="text-[15px] font-bold text-ttp09-ink">340</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">PRs</div></div>
          </div>
        </div>
        <div class="flex gap-1.5 border-t border-ttp09-rule px-3.5 py-2.25">
          <button type="button" class="ttp09-btn">Message</button>
          <button type="button" class="ttp09-btn ttp09-btn-prim">View Profile</button>
        </div>
      </div>
    </div>

    <div class="group relative">
      <button type="button" aria-label="Elena Russo, CMO" aria-describedby="ttp09-p3" class="ttp09-circle bg-linear-to-br from-[#0a6050] to-[#1aa080]">ER</button>
      <div id="ttp09-p3" role="tooltip" class="ttp09-card">
        <div class="relative h-14 bg-linear-to-br from-[#054030] to-[#108060]"><div class="ttp09-photo bg-linear-to-br from-[#0a6050] to-[#1aa080]">ER</div></div>
        <div class="px-3.5 pt-5 pb-3">
          <div class="text-sm font-semibold text-ttp09-ink">Elena Russo</div>
          <div class="mt-0.5 text-[10.5px] text-ttp09-muted">CMO · Marketing</div>
          <div class="mt-1.5 flex items-center gap-1.25 text-[10.5px] text-ttp09-muted"><span class="h-1.5 w-1.5 rounded-full bg-ttp09-away"></span>Away · 2h ago</div>
          <div class="mt-2 text-[11.5px] leading-[1.5] text-ttp09-body">Brand strategist. Grew Notion's Europe presence 3×. London-based, GMT+1.</div>
          <div class="mt-3 grid grid-cols-3 border-t border-ttp09-rule pt-2.75 text-center">
            <div><div class="text-[15px] font-bold text-ttp09-ink">68</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Team</div></div>
            <div><div class="text-[15px] font-bold text-ttp09-ink">3yr</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Tenure</div></div>
            <div><div class="text-[15px] font-bold text-ttp09-ink">+84%</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">YoY</div></div>
          </div>
        </div>
        <div class="flex gap-1.5 border-t border-ttp09-rule px-3.5 py-2.25">
          <button type="button" class="ttp09-btn">Message</button>
          <button type="button" class="ttp09-btn ttp09-btn-prim">View Profile</button>
        </div>
      </div>
    </div>

    <div class="group relative">
      <button type="button" aria-label="Aisha Patel, Growth Lead" aria-describedby="ttp09-p4" class="ttp09-circle bg-linear-to-br from-[#802050] to-[#c04080]">AP</button>
      <div id="ttp09-p4" role="tooltip" class="ttp09-card">
        <div class="relative h-14 bg-linear-to-br from-[#601030] to-[#a03060]"><div class="ttp09-photo bg-linear-to-br from-[#802050] to-[#c04080]">AP</div></div>
        <div class="px-3.5 pt-5 pb-3">
          <div class="text-sm font-semibold text-ttp09-ink">Aisha Patel</div>
          <div class="mt-0.5 text-[10.5px] text-ttp09-muted">Growth Lead · Marketing</div>
          <div class="mt-1.5 flex items-center gap-1.25 text-[10.5px] text-ttp09-muted"><span class="h-1.5 w-1.5 rounded-full bg-ttp09-offline"></span>Offline</div>
          <div class="mt-2 text-[11.5px] leading-[1.5] text-ttp09-body">Data-driven growth. 0 → 100k users in 18 months. Runs the acquisition engine.</div>
          <div class="mt-3 grid grid-cols-3 border-t border-ttp09-rule pt-2.75 text-center">
            <div><div class="text-[15px] font-bold text-ttp09-ink">6</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Team</div></div>
            <div><div class="text-[15px] font-bold text-ttp09-ink">1yr</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Tenure</div></div>
            <div><div class="text-[15px] font-bold text-ttp09-ink">$1.2M</div><div class="mt-px text-[8.5px] uppercase tracking-[0.08em] text-ttp09-muted">Budget</div></div>
          </div>
        </div>
        <div class="flex gap-1.5 border-t border-ttp09-rule px-3.5 py-2.25">
          <button type="button" class="ttp09-btn">Message</button>
          <button type="button" class="ttp09-btn ttp09-btn-prim">View Profile</button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp09-ink: #111111;
  --color-ttp09-ink: oklch(0.18 0 0);
  --color-ttp09-body: #4d4d4d;
  --color-ttp09-body: oklch(0.42 0 0);
  --color-ttp09-muted: #6b6b6b;
  --color-ttp09-muted: oklch(0.52 0 0);
  --color-ttp09-rule: #ededed;
  --color-ttp09-rule: oklch(0.93 0 0);
  --color-ttp09-online: #16a34a;
  --color-ttp09-online: oklch(0.6 0.16 150);
  --color-ttp09-away: #d97706;
  --color-ttp09-away: oklch(0.65 0.15 62);
  --color-ttp09-offline: #64748b;
  --color-ttp09-offline: oklch(0.55 0.03 255);
  --font-ttp09-sans: 'Inter', system-ui, sans-serif;
}

.ttp-09 {
  width: 100%;
  min-height: 100svh;
}
/* Four identical card shells, two identical action buttons, four
   identical avatar circles. The per-person gradients stay inline in
   the markup, because those are data, not shape. */

.ttp-09 .ttp09-circle {
  @apply flex h-12 w-12 cursor-help items-center justify-center rounded-full border-0 p-0 text-[13px] font-semibold tracking-[0.03em] text-white transition-[transform,box-shadow] duration-150 group-hover:scale-110 group-hover:-translate-y-[3px] group-hover:shadow-[0_8px_20px_rgba(0,0,0,0.18)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp09-ink;
}

.ttp-09 .ttp09-card {
  @apply pointer-events-none invisible absolute bottom-[calc(100%+12px)] left-1/2 z-30 w-60 max-w-[calc(100vw-48px)] -translate-x-1/2 translate-y-1 overflow-hidden rounded-xl border border-black/7 bg-white text-left opacity-0 shadow-[0_12px_36px_rgba(0,0,0,0.12),0_2px_8px_rgba(0,0,0,0.06)] transition-[opacity,translate,visibility] duration-250 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-hover:pointer-events-auto group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100 group-focus-within:pointer-events-auto;
}

.ttp-09 .ttp09-photo {
  @apply absolute -bottom-3.5 left-3.5 flex h-12 w-12 items-center justify-center rounded-full border-3 border-white text-sm font-bold text-white shadow-[0_2px_8px_rgba(0,0,0,0.14)];
}

.ttp-09 .ttp09-btn {
  @apply flex-1 cursor-pointer rounded-md border border-ttp09-rule bg-ttp09-rule/40 py-1.5 text-center text-[11px] font-medium text-ttp09-body transition-colors hover:bg-ttp09-rule focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp09-ink;
}

.ttp-09 .ttp09-btn-prim {
  @apply border-ttp09-ink bg-ttp09-ink text-white hover:bg-black;
}
```
