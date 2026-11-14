---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-profile-hover-card-tooltip-staggered-reveal/"
title: "Tailwind Profile Hover Card Tooltip with Staggered Reveal"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "The hover card behind every @mention: a roster row reveals a 320px panel whose parts arrive in sequence &mdash; hero glow, then portrait, then name, tagline…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Profile Hover Card Tooltip with Staggered Reveal
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-profile-hover-card-tooltip-staggered-reveal/

The hover card behind every @mention: a roster row reveals a 320px panel whose parts arrive in sequence &mdash; hero glow, then portrait, then name, tagline and stats &mdash; so the card unfolds instead of flicking on. The port's win is the stagger: group-hover:delay-50 and group-hover:delay-[180ms] sit on the children that wait, not in a pile of nth-child rules.
## HTML
```html
<section class="ttp-05 w-full min-h-svh flex items-start justify-center bg-ttp05-bg font-ttp05-sans px-7 pt-9 pb-[400px]">
  <div class="w-full max-w-[560px] rounded-[2px] border border-white/6 bg-white/2">
    <div class="flex items-center justify-between border-b border-white/6 px-5 py-3 font-ttp05-mono text-[10px] uppercase tracking-[0.2em] text-ttp05-dim">
      <span>Editorial Team · Vol XII</span><span>3 active</span>
    </div>

    <div class="group relative grid grid-cols-[40px_1fr_auto_auto] items-center gap-3.5 border-b border-white/4 px-5 py-3.5 text-ttp05-ink transition-colors hover:bg-white/3 focus-within:bg-white/3">
      <button type="button" aria-describedby="ttp05-c1" aria-label="Profile: Mira Vance" class="block h-9 w-9 shrink-0 overflow-hidden rounded-full border border-white/10 p-0 cursor-pointer transition-transform duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:scale-[1.08] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp05-gold">
        <svg viewBox="0 0 100 100" class="block h-full w-full" aria-hidden="true"><defs><linearGradient id="ttp05-av1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c1422c"/><stop offset="1" stop-color="#7a2415"/></linearGradient></defs><rect width="100" height="100" fill="url(#ttp05-av1)"/><text x="50" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="38" font-style="italic" fill="#f7d18e">M</text></svg>
      </button>
      <div>
        <div class="font-ttp05-serif text-[17px]">Mira <em class="font-light italic text-ttp05-gold">Vance</em></div>
        <div class="mt-0.5 font-ttp05-mono text-[10.5px] text-ttp05-dim">@miravance</div>
      </div>
      <div class="font-ttp05-mono text-[10px] uppercase tracking-[0.15em] text-ttp05-dim">Editor-in-Chief</div>
      <div class="h-1.5 w-1.5 rounded-full bg-ttp05-online shadow-[0_0_8px_rgba(111,207,151,0.6)]"></div>

      <div id="ttp05-c1" role="tooltip" class="pointer-events-none invisible absolute top-[calc(100%+12px)] left-5 z-30 w-[320px] max-w-[calc(100vw-56px)] translate-y-2 overflow-hidden rounded-[2px] border border-ttp05-gold/15 bg-linear-to-b from-ttp05-card to-ttp05-bg opacity-0 shadow-[0_25px_60px_-16px_rgba(0,0,0,0.8),0_0_0_1px_rgba(247,209,142,0.05),inset_0_1px_0_rgba(247,209,142,0.08)] transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100 before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-px before:opacity-50 before:bg-linear-to-r before:from-transparent before:via-ttp05-gold before:to-transparent">
        <div class="relative h-19 translate-y-1.5 opacity-0 overflow-hidden bg-[radial-gradient(circle_at_30%_60%,rgba(193,66,44,0.4),transparent_50%),radial-gradient(circle_at_80%_40%,rgba(247,209,142,0.3),transparent_50%),linear-gradient(135deg,#2a201a_0%,#14110d_100%)] transition-[opacity,translate] duration-400 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-50 group-focus-within:translate-y-0 group-focus-within:opacity-100 after:content-[''] after:absolute after:inset-0 after:bg-[repeating-linear-gradient(45deg,transparent_0,transparent_6px,rgba(247,209,142,0.04)_6px,rgba(247,209,142,0.04)_7px)]"></div>
        <div class="relative translate-y-1.5 px-4.5 pb-4 opacity-0 transition-[opacity,translate] duration-400 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-[180ms] group-focus-within:translate-y-0 group-focus-within:opacity-100">
          <div class="-mt-7 h-14 w-14 overflow-hidden rounded-full border-2 border-ttp05-bg bg-ttp05-card shadow-[0_0_0_1px_rgba(247,209,142,0.3)]">
            <svg viewBox="0 0 100 100" width="100%" height="100%" aria-hidden="true"><rect width="100" height="100" fill="url(#ttp05-av1)"/><text x="50" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="40" font-style="italic" fill="#f7d18e">M</text></svg>
          </div>
          <div class="mt-3 font-ttp05-serif text-[22px] leading-[1.15] text-ttp05-ink">Mira <em class="font-light italic text-ttp05-gold">Vance</em></div>
          <div class="mt-1.5 font-ttp05-serif text-[13.5px] italic leading-[1.4] text-ttp05-soft">"Words first; everything else negotiated after."</div>
          <div class="mt-3.5 grid grid-cols-3 gap-2.5 border-t border-white/6 pt-3">
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">142</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">essays</div></div>
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">8.4k</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">readers</div></div>
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">VII</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">volumes</div></div>
          </div>
        </div>
      </div>
    </div>

    <div class="group relative grid grid-cols-[40px_1fr_auto_auto] items-center gap-3.5 border-b border-white/4 px-5 py-3.5 text-ttp05-ink transition-colors hover:bg-white/3 focus-within:bg-white/3">
      <button type="button" aria-describedby="ttp05-c2" aria-label="Profile: Adesh Kothari" class="block h-9 w-9 shrink-0 overflow-hidden rounded-full border border-white/10 p-0 cursor-pointer transition-transform duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:scale-[1.08] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp05-gold">
        <svg viewBox="0 0 100 100" class="block h-full w-full" aria-hidden="true"><defs><linearGradient id="ttp05-av2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2d4a3e"/><stop offset="1" stop-color="#0d1f17"/></linearGradient></defs><rect width="100" height="100" fill="url(#ttp05-av2)"/><text x="50" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="38" font-style="italic" fill="#f7d18e">A</text></svg>
      </button>
      <div>
        <div class="font-ttp05-serif text-[17px]">Adesh <em class="font-light italic text-ttp05-gold">Kothari</em></div>
        <div class="mt-0.5 font-ttp05-mono text-[10.5px] text-ttp05-dim">@adesh.k</div>
      </div>
      <div class="font-ttp05-mono text-[10px] uppercase tracking-[0.15em] text-ttp05-dim">Design Director</div>
      <div class="h-1.5 w-1.5 rounded-full bg-ttp05-gold shadow-[0_0_8px_rgba(247,209,142,0.6)]"></div>

      <div id="ttp05-c2" role="tooltip" class="pointer-events-none invisible absolute top-[calc(100%+12px)] left-5 z-30 w-[320px] max-w-[calc(100vw-56px)] translate-y-2 overflow-hidden rounded-[2px] border border-ttp05-gold/15 bg-linear-to-b from-ttp05-card to-ttp05-bg opacity-0 shadow-[0_25px_60px_-16px_rgba(0,0,0,0.8),0_0_0_1px_rgba(247,209,142,0.05),inset_0_1px_0_rgba(247,209,142,0.08)] transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100 before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-px before:opacity-50 before:bg-linear-to-r before:from-transparent before:via-ttp05-gold before:to-transparent">
        <div class="relative h-19 translate-y-1.5 opacity-0 overflow-hidden bg-[radial-gradient(circle_at_30%_60%,rgba(45,74,62,0.5),transparent_50%),radial-gradient(circle_at_80%_40%,rgba(247,209,142,0.3),transparent_50%),linear-gradient(135deg,#1a2a23_0%,#14110d_100%)] transition-[opacity,translate] duration-400 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-50 group-focus-within:translate-y-0 group-focus-within:opacity-100 after:content-[''] after:absolute after:inset-0 after:bg-[repeating-linear-gradient(45deg,transparent_0,transparent_6px,rgba(247,209,142,0.04)_6px,rgba(247,209,142,0.04)_7px)]"></div>
        <div class="relative translate-y-1.5 px-4.5 pb-4 opacity-0 transition-[opacity,translate] duration-400 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-[180ms] group-focus-within:translate-y-0 group-focus-within:opacity-100">
          <div class="-mt-7 h-14 w-14 overflow-hidden rounded-full border-2 border-ttp05-bg bg-ttp05-card shadow-[0_0_0_1px_rgba(247,209,142,0.3)]">
            <svg viewBox="0 0 100 100" width="100%" height="100%" aria-hidden="true"><rect width="100" height="100" fill="url(#ttp05-av2)"/><text x="50" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="40" font-style="italic" fill="#f7d18e">A</text></svg>
          </div>
          <div class="mt-3 font-ttp05-serif text-[22px] leading-[1.15] text-ttp05-ink">Adesh <em class="font-light italic text-ttp05-gold">Kothari</em></div>
          <div class="mt-1.5 font-ttp05-serif text-[13.5px] italic leading-[1.4] text-ttp05-soft">"Restraint is also a flourish, if you commit to it."</div>
          <div class="mt-3.5 grid grid-cols-3 gap-2.5 border-t border-white/6 pt-3">
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">96</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">covers</div></div>
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">12</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">awards</div></div>
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">04</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">books</div></div>
          </div>
        </div>
      </div>
    </div>

    <div class="group relative grid grid-cols-[40px_1fr_auto_auto] items-center gap-3.5 px-5 py-3.5 text-ttp05-ink transition-colors hover:bg-white/3 focus-within:bg-white/3">
      <button type="button" aria-describedby="ttp05-c3" aria-label="Profile: June Lacroix" class="block h-9 w-9 shrink-0 overflow-hidden rounded-full border border-white/10 p-0 cursor-pointer transition-transform duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:scale-[1.08] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp05-gold">
        <svg viewBox="0 0 100 100" class="block h-full w-full" aria-hidden="true"><defs><linearGradient id="ttp05-av3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6b4226"/><stop offset="1" stop-color="#2a1810"/></linearGradient></defs><rect width="100" height="100" fill="url(#ttp05-av3)"/><text x="50" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="38" font-style="italic" fill="#f7d18e">J</text></svg>
      </button>
      <div>
        <div class="font-ttp05-serif text-[17px]">June <em class="font-light italic text-ttp05-gold">Lacroix</em></div>
        <div class="mt-0.5 font-ttp05-mono text-[10.5px] text-ttp05-dim">@junelacroix</div>
      </div>
      <div class="font-ttp05-mono text-[10px] uppercase tracking-[0.15em] text-ttp05-dim">Photo Editor</div>
      <div class="h-1.5 w-1.5 rounded-full bg-ttp05-online shadow-[0_0_8px_rgba(111,207,151,0.6)]"></div>

      <div id="ttp05-c3" role="tooltip" class="pointer-events-none invisible absolute top-[calc(100%+12px)] left-5 z-30 w-[320px] max-w-[calc(100vw-56px)] translate-y-2 overflow-hidden rounded-[2px] border border-ttp05-gold/15 bg-linear-to-b from-ttp05-card to-ttp05-bg opacity-0 shadow-[0_25px_60px_-16px_rgba(0,0,0,0.8),0_0_0_1px_rgba(247,209,142,0.05),inset_0_1px_0_rgba(247,209,142,0.08)] transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100 before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-px before:opacity-50 before:bg-linear-to-r before:from-transparent before:via-ttp05-gold before:to-transparent">
        <div class="relative h-19 translate-y-1.5 opacity-0 overflow-hidden bg-[radial-gradient(circle_at_30%_60%,rgba(107,66,38,0.5),transparent_50%),radial-gradient(circle_at_80%_40%,rgba(247,209,142,0.25),transparent_50%),linear-gradient(135deg,#2a201a_0%,#14110d_100%)] transition-[opacity,translate] duration-400 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-50 group-focus-within:translate-y-0 group-focus-within:opacity-100 after:content-[''] after:absolute after:inset-0 after:bg-[repeating-linear-gradient(45deg,transparent_0,transparent_6px,rgba(247,209,142,0.04)_6px,rgba(247,209,142,0.04)_7px)]"></div>
        <div class="relative translate-y-1.5 px-4.5 pb-4 opacity-0 transition-[opacity,translate] duration-400 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-[180ms] group-focus-within:translate-y-0 group-focus-within:opacity-100">
          <div class="-mt-7 h-14 w-14 overflow-hidden rounded-full border-2 border-ttp05-bg bg-ttp05-card shadow-[0_0_0_1px_rgba(247,209,142,0.3)]">
            <svg viewBox="0 0 100 100" width="100%" height="100%" aria-hidden="true"><rect width="100" height="100" fill="url(#ttp05-av3)"/><text x="50" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="40" font-style="italic" fill="#f7d18e">J</text></svg>
          </div>
          <div class="mt-3 font-ttp05-serif text-[22px] leading-[1.15] text-ttp05-ink">June <em class="font-light italic text-ttp05-gold">Lacroix</em></div>
          <div class="mt-1.5 font-ttp05-serif text-[13.5px] italic leading-[1.4] text-ttp05-soft">"A photograph is the slowest sentence a magazine can run."</div>
          <div class="mt-3.5 grid grid-cols-3 gap-2.5 border-t border-white/6 pt-3">
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">311</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">shoots</div></div>
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">28</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">cities</div></div>
            <div><div class="font-ttp05-serif text-lg font-medium text-ttp05-gold">VI</div><div class="mt-0.5 font-ttp05-mono text-[9px] uppercase tracking-[0.15em] text-ttp05-dim">years</div></div>
          </div>
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
  --color-ttp05-bg: #14110d;
  --color-ttp05-bg: oklch(0.17 0.012 70);
  --color-ttp05-card: #1f1a14;
  --color-ttp05-card: oklch(0.23 0.015 70);
  --color-ttp05-ink: #efece6;
  --color-ttp05-ink: oklch(0.94 0.008 85);
  --color-ttp05-soft: #cfcabf;
  --color-ttp05-soft: oklch(0.84 0.012 85);
  --color-ttp05-dim: #a9a49a;
  --color-ttp05-dim: oklch(0.71 0.012 85);
  --color-ttp05-gold: #f7d18e;
  --color-ttp05-gold: oklch(0.87 0.09 82);
  --color-ttp05-online: #6fcf97;
  --color-ttp05-online: oklch(0.79 0.13 155);
  --font-ttp05-sans: 'Inter', system-ui, sans-serif;
  --font-ttp05-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttp05-serif: Georgia, 'Times New Roman', serif;
}

.ttp-05 {
  width: 100%;
  min-height: 100svh;
}
```
