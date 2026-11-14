---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-warm-dark-mode-writing-editor/"
title: "Tailwind Warm Dark Mode Writing Editor (Mocha Theme)"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "Dark mode without the cold: roasted-brown surfaces, cream ink and a single burnt-orange accent, built as a focus writing surface with a title field, tag…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Warm Dark Mode Writing Editor (Mocha Theme)
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-warm-dark-mode-writing-editor/

Dark mode without the cold: roasted-brown surfaces, cream ink and a single burnt-orange accent, built as a focus writing surface with a title field, tag chips, word count and long-form copy. Light mode becomes a latte paper, not a white page. The ember only marks the caret, the selection, the active tags and the primary action — everything else is substrate, ink and one hairline.
## HTML
```html
<div class="tdm-15 scheme-light-dark has-[#tdm-15-toggle:checked]:scheme-dark dark:has-[#tdm-15-toggle:checked]:scheme-light w-full min-h-svh bg-tdm15-bean bg-[radial-gradient(110%_70%_at_15%_0%,var(--color-tdm15-glow),transparent_62%)] font-tdm15-sans text-tdm15-cream antialiased selection:bg-tdm15-sel selection:text-tdm15-cream transition-colors duration-300">
  <div class="mx-auto grid min-h-svh max-w-3xl content-start gap-8 px-5 py-10 sm:px-8">
    <header class="flex flex-wrap items-center gap-x-5 gap-y-2 text-[13px] text-tdm15-milk">
      <span class="flex items-center gap-2 font-semibold text-tdm15-cream"><svg class="size-4 text-tdm15-ember" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16Z"/><path d="m13.5 6.5 4 4"/></svg>Mocha</span>
      <span class="flex items-center gap-1.5"><span class="size-1.5 rounded-full bg-tdm15-ok" aria-hidden="true"></span>Draft · saved 2 min ago</span>
      <span class="font-tdm15-mono tabular-nums">1,248 words</span>
      <span class="ml-auto"><label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm15-line bg-tdm15-surface transition duration-200 hover:-translate-y-px hover:border-tdm15-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm15-focus motion-reduce:transition-none ">
        <input id="tdm-15-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm15-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm15-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label></span>
    </header>
    <div class="grid gap-4">
      <label for="tdm-15-title" class="sr-only">Document title</label>
      <input id="tdm-15-title" type="text" value="Designing for the last hour of the day" spellcheck="false" class="w-full rounded-lg bg-transparent font-tdm15-serif text-[clamp(2rem,5vw,3rem)] leading-[1.1] tracking-[-0.02em] text-tdm15-cream caret-tdm15-ember outline-none placeholder:text-tdm15-milk focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tdm15-focus/60">
      <fieldset class="flex flex-wrap gap-2">
        <legend class="sr-only">Tags</legend>
        <label class="inline-flex min-h-9 cursor-pointer items-center gap-1.5 rounded-full border border-tdm15-hair px-3.5 text-[13px] text-tdm15-milk transition hover:border-tdm15-ember/50 has-checked:border-tdm15-ember/50 has-checked:bg-tdm15-ember/15 has-checked:text-tdm15-cream has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm15-focus"><input type="checkbox" class="peer sr-only" checked><span class="text-tdm15-ember" aria-hidden="true">#</span>craft</label>
        <label class="inline-flex min-h-9 cursor-pointer items-center gap-1.5 rounded-full border border-tdm15-hair px-3.5 text-[13px] text-tdm15-milk transition hover:border-tdm15-ember/50 has-checked:border-tdm15-ember/50 has-checked:bg-tdm15-ember/15 has-checked:text-tdm15-cream has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm15-focus"><input type="checkbox" class="peer sr-only" checked><span class="text-tdm15-ember" aria-hidden="true">#</span>dark mode</label>
        <label class="inline-flex min-h-9 cursor-pointer items-center gap-1.5 rounded-full border border-tdm15-hair px-3.5 text-[13px] text-tdm15-milk transition hover:border-tdm15-ember/50 has-checked:border-tdm15-ember/50 has-checked:bg-tdm15-ember/15 has-checked:text-tdm15-cream has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm15-focus"><input type="checkbox" class="peer sr-only"><span class="text-tdm15-ember" aria-hidden="true">#</span>typography</label>
        <label class="inline-flex min-h-9 cursor-pointer items-center gap-1.5 rounded-full border border-tdm15-hair px-3.5 text-[13px] text-tdm15-milk transition hover:border-tdm15-ember/50 has-checked:border-tdm15-ember/50 has-checked:bg-tdm15-ember/15 has-checked:text-tdm15-cream has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm15-focus"><input type="checkbox" class="peer sr-only"><span class="text-tdm15-ember" aria-hidden="true">#</span>research</label>
      </fieldset>
    </div>
    <article class="grid max-w-[65ch] gap-5 font-tdm15-serif text-[clamp(1.05rem,1.6vw,1.2rem)]/[1.75] text-pretty text-tdm15-cream/92">
      <p>Most dark themes are built at noon. They are drawn on a bright display in a bright room, then shipped to people reading at eleven at night with the lights off — which is why so many of them feel like a photographic negative rather than a designed surface.</p>
      <p>Warm neutrals fix more than they should. Pulling the substrate toward brown drops the blue component of a mostly-lit screen, and cream ink stays comfortable far longer than pure white. The palette does the work an eye-strain setting pretends to.</p>
      <p>The rule I keep: one accent, and it earns its place. Here the ember only marks the caret, the active tags and the primary action. Everything else is substrate, ink and one hairline.</p>
      <blockquote class="border-l-2 border-tdm15-ember py-1 pl-5 text-[1.15em] italic text-tdm15-cream">A dark theme is not a colour inversion. It is a second design with the same information architecture.</blockquote>
    </article>
    <footer class="sticky bottom-4 flex flex-wrap items-center gap-3 rounded-2xl border border-tdm15-hair bg-tdm15-crema/90 p-2.5 pl-4 text-[13px] text-tdm15-milk shadow-[0_20px_40px_-20px_rgb(0_0_0/.5)] backdrop-blur-md">
      <span class="flex items-center gap-1.5"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 12S6 5 12 5s9.5 7 9.5 7-3.5 7-9.5 7-9.5-7-9.5-7Z"/><circle cx="12" cy="12" r="3"/></svg>Focus mode</span>
      <span class="hidden font-tdm15-mono sm:inline">65ch measure</span>
      <span class="ml-auto flex gap-2">
        <button type="button" class="min-h-11 rounded-xl px-4 font-medium text-tdm15-cream transition hover:bg-tdm15-foam focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm15-focus">Preview</button>
        <button type="button" class="min-h-11 rounded-xl bg-tdm15-ember px-5 font-semibold text-tdm15-ember-ink transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm15-focus">Publish draft</button>
      </span>
    </footer>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm15-bean: light-dark(#f6efe6, #171210);
  --color-tdm15-glow: light-dark(#fdf8f2, #221a16);
  --color-tdm15-crema: light-dark(#fffaf4, #1f1815);
  --color-tdm15-foam: light-dark(#efe4d6, #2a201c);
  --color-tdm15-surface: light-dark(#fffaf4, #1f1815);
  --color-tdm15-hair: light-dark(rgb(43 31 24 / .14), rgb(243 233 223 / .13));
  --color-tdm15-line: light-dark(rgb(43 31 24 / .14), rgb(243 233 223 / .13));
  --color-tdm15-cream: light-dark(#2b1f18, #f3e9df);
  --color-tdm15-milk: light-dark(#6e5a4d, #c4ae9f);
  --color-tdm15-ember: light-dark(#b4501f, #e0703c);
  --color-tdm15-acc: light-dark(#b4501f, #e0703c);
  --color-tdm15-ember-ink: light-dark(#ffffff, #1a0a04);
  --color-tdm15-focus: light-dark(#b4501f, #f0a06a);
  --color-tdm15-sel: light-dark(rgb(180 80 31 / .22), rgb(224 112 60 / .32));
  --color-tdm15-ok: light-dark(#4d7c0f, #a3d977);
  --color-tdm15-sun: light-dark(#b4501f, transparent);
  --color-tdm15-moon: light-dark(transparent, #f0a06a);
  --font-tdm15-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm15-serif: 'Newsreader', Georgia, serif;
  --font-tdm15-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
