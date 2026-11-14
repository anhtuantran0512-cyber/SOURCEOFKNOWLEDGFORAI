---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-language-flashcard-flip-phonetics-example-memory-tip/"
title: "Tailwind Language Flashcard Flip with Phonetics, Example & Memory Tip"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A vocabulary card: word and phonetics on the front, definition, example sentence and mnemonic on the back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Language Flashcard Flip with Phonetics, Example & Memory Tip
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-language-flashcard-flip-phonetics-example-memory-tip/

A vocabulary card: word and phonetics on the front, definition, example sentence and mnemonic on the back. The port adds the thing every flashcard actually needs and the CSS version lacked &mdash; a keyboard flip, because study decks are driven from the keyboard, not the mouse. Japanese text now carries lang="ja" so screen readers and font stacks both pick the right engine.
## HTML
```html
<section class="tfc-06 w-full min-h-svh grid place-items-center content-center gap-5 bg-tfc06-bg font-tfc06-sans px-5 py-10 text-tfc06-ink">
  <div class="flex justify-center gap-3">
    <button type="button" class="min-h-11 rounded-full border border-tfc06-purple/25 bg-tfc06-purple/8 px-5 text-xs font-semibold text-tfc06-ink/65 transition-colors duration-200 hover:bg-tfc06-purple/18 hover:text-tfc06-purple focus-visible:outline-2 focus-visible:outline-tfc06-purple focus-visible:outline-offset-2">&larr; Prev</button>
    <button type="button" class="min-h-11 rounded-full border border-tfc06-purple/25 bg-tfc06-purple/8 px-5 text-xs font-semibold text-tfc06-ink/65 transition-colors duration-200 hover:bg-tfc06-purple/18 hover:text-tfc06-purple focus-visible:outline-2 focus-visible:outline-tfc06-purple focus-visible:outline-offset-2">Next &rarr;</button>
  </div>
  <p class="text-center text-xs tracking-[0.08em] text-tfc06-dim">Card 7 of 24 &middot; Japanese N3</p>

  <div class="group relative mx-auto w-[340px] max-w-full h-[400px] @container/card [perspective:1200px] rounded-3xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc06-purple has-[:focus-visible]:outline-offset-4">
    <input id="tfc-06-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-06-flip" class="absolute inset-0 z-20 cursor-pointer rounded-3xl"><span class="sr-only">Reveal the definition of komorebi</span></label>

    <div class="relative w-full h-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex flex-col items-center justify-center gap-3 rounded-3xl overflow-hidden px-8 py-10 bg-linear-145 from-tfc06-panel to-tfc06-panel2 border border-tfc06-purple/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.45_0.18_295/0.5)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden] before:absolute before:inset-0 before:bg-[radial-gradient(circle_at_50%_30%,oklch(0.7_0.15_295/0.1),transparent_60%)]">
        <p class="relative z-1 text-[10px] font-semibold uppercase tracking-[0.2em] text-tfc06-dim">Japanese &middot; N3</p>
        <p lang="ja" class="relative z-1 bg-linear-135 from-tfc06-purple to-tfc06-indigo bg-clip-text text-center font-tfc06-jp text-[clamp(2.25rem,9cqi,3.25rem)] font-black leading-tight text-transparent">木漏れ日</p>
        <p class="relative z-1 text-base italic tracking-[0.04em] text-tfc06-muted">/ ko&middot;mo&middot;re&middot;bi /</p>
        <button type="button" aria-disabled="true" title="Demo only — wire this to window.speechSynthesis.speak()" class="relative z-30 inline-flex min-h-11 items-center gap-2 rounded-full border border-tfc06-purple/20 bg-tfc06-purple/10 px-5 text-xs font-semibold text-tfc06-purple transition-colors duration-200 hover:bg-tfc06-purple/20 focus-visible:outline-2 focus-visible:outline-tfc06-purple focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          Play audio
        </button>
        <p class="absolute bottom-5 text-[10px] tracking-[0.08em] text-tfc06-dim">Hover, tap or press Space for the definition &rarr;</p>
      </div>

      <div class="absolute inset-0 flex flex-col gap-3 rounded-3xl overflow-hidden p-7 bg-linear-145 from-tfc06-back to-tfc06-back2 border border-tfc06-mint/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.5_0.12_160/0.4)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <p class="text-[10px] font-bold uppercase tracking-[0.15em] text-tfc06-mint">Definition</p>
        <p class="w-fit rounded-full border border-tfc06-mint/20 bg-tfc06-mint/10 px-2.5 py-0.5 text-[10px] italic text-tfc06-mint">noun &middot; untranslatable</p>
        <p class="text-base font-bold leading-snug text-white text-pretty">Sunlight filtering through leaves; the interplay of light and shadow when sun shines through a canopy of trees.</p>
        <p class="mt-1 text-[10px] uppercase tracking-[0.12em] text-tfc06-dim">Example sentence</p>
        <p class="border-l-2 border-tfc06-mint/30 pl-3 text-[13px] italic leading-[1.7] text-tfc06-ink/70"><span lang="ja" class="font-tfc06-jp">「公園の木漏れ日の中で読書するのが好きです。」</span><br>&ldquo;I love reading in the komorebi of the park.&rdquo;</p>
        <p class="mt-auto rounded-xl border border-tfc06-purple/12 bg-tfc06-purple/6 p-3 text-xs leading-[1.6] text-tfc06-ink/60"><strong class="text-tfc06-purple">Memory tip:</strong> <span lang="ja" class="font-tfc06-jp">木</span> (ki = tree) + <span lang="ja" class="font-tfc06-jp">漏れ</span> (more = leaking) + <span lang="ja" class="font-tfc06-jp">日</span> (hi = sun) &rarr; &ldquo;sun leaking through trees&rdquo; &mdash; paint the picture.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc06-bg: #080612;
  --color-tfc06-bg: oklch(0.13 0.03 295);
  --color-tfc06-panel: #130d2e;
  --color-tfc06-panel: oklch(0.2 0.07 295);
  --color-tfc06-panel2: #0e0a22;
  --color-tfc06-panel2: oklch(0.16 0.05 295);
  --color-tfc06-back: #0a1a0e;
  --color-tfc06-back: oklch(0.19 0.05 155);
  --color-tfc06-back2: #0d1f12;
  --color-tfc06-back2: oklch(0.21 0.05 155);
  --color-tfc06-purple: #a78bfa;
  --color-tfc06-purple: oklch(0.73 0.16 295);
  --color-tfc06-indigo: #6366f1;
  --color-tfc06-indigo: oklch(0.58 0.2 280);
  --color-tfc06-mint: #34d399;
  --color-tfc06-mint: oklch(0.8 0.14 165);
  --color-tfc06-ink: #f5f3ff;
  --color-tfc06-ink: oklch(0.97 0.015 295);
  --color-tfc06-muted: #b6b0cf;
  --color-tfc06-muted: oklch(0.78 0.04 295);
  --color-tfc06-dim: #8a84a3;
  --color-tfc06-dim: oklch(0.63 0.03 295);
  --font-tfc06-sans: 'Sora', system-ui, sans-serif;
  --font-tfc06-jp: 'Hiragino Mincho ProN', 'Yu Mincho', 'Noto Serif JP', serif;
}

.tfc-06 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-06 * {
    transition-duration: 1ms !important;
  }
}
```
