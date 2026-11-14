---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-trivia-quiz-flip-card-answer-reveal-score/"
title: "Tailwind Trivia Quiz Flip Card with Answer Reveal & Score Readout"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A trivia question with four options on the front and the answer, context and score on the back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Trivia Quiz Flip Card with Answer Reveal & Score Readout
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-trivia-quiz-flip-card-answer-reveal-score/

A trivia question with four options on the front and the answer, context and score on the back. The port resolves the CSS original's stated conflict head-on: options were divs with hover highlights that fought the card's own hover flip. Here they are real radio inputs, so a choice can be made before the reveal &mdash; which is what a quiz card is for.
## HTML
```html
<section class="tfc-07 w-full min-h-svh grid place-items-center bg-tfc07-bg font-tfc07-sans px-5 py-10 text-tfc07-ink">
  <div class="group relative w-[360px] max-w-full h-[440px] [perspective:1200px] rounded-3xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc07-amber has-[:focus-visible]:outline-offset-4">
    <input id="tfc-07-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-07-flip" class="absolute inset-0 z-20 cursor-pointer rounded-3xl"><span class="sr-only">Reveal the answer to question 7</span></label>

    <div class="relative w-full h-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex flex-col items-center rounded-3xl overflow-hidden px-7 py-9 bg-linear-145 from-tfc07-panel to-tfc07-panel2 border border-tfc07-yellow/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.6_0.15_85/0.3)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden] before:absolute before:inset-0 before:bg-[radial-gradient(ellipse_at_50%_0%,oklch(0.78_0.16_85/0.12),transparent_60%)]">
        <span aria-hidden="true" class="absolute top-5 right-6 text-[80px] font-black italic leading-none text-tfc07-yellow/8">Q7</span>
        <p class="relative z-1 flex items-center gap-1.5 text-[10px] font-bold uppercase tracking-[0.15em] text-tfc07-amber"><span class="size-1.5 rounded-full bg-tfc07-amber"></span>Space &amp; Astronomy</p>
        <p role="img" aria-label="Difficulty: 3 of 5" class="relative z-1 mt-1.5 flex gap-1 text-sm text-tfc07-yellow"><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span><span class="opacity-20">&#9733;</span><span class="opacity-20">&#9733;</span></p>
        <h2 class="relative z-1 mt-6 text-center text-xl font-bold leading-[1.45] tracking-[-0.01em] text-white text-pretty">Which planet in our solar system has the most known natural moons?</h2>
        <fieldset class="relative z-30 mt-7 flex w-full flex-col gap-2.5">
          <legend class="sr-only">Choose an answer</legend>
          <input id="tfc-07-a" type="radio" name="tfc-07-answer" class="peer/a sr-only">
          <label for="tfc-07-a" class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-xl border border-tfc07-yellow/15 bg-white/4 px-4 text-[13px] text-tfc07-ink/70 transition-colors duration-200 hover:border-tfc07-yellow/35 hover:bg-tfc07-yellow/10 hover:text-white peer-checked/a:border-tfc07-amber peer-checked/a:bg-tfc07-amber/15 peer-checked/a:text-white peer-focus-visible/a:outline-2 peer-focus-visible/a:outline-tfc07-amber peer-focus-visible/a:outline-offset-2"><span class="grid size-5.5 shrink-0 place-items-center rounded-md bg-tfc07-yellow/15 text-[11px] font-bold text-tfc07-amber">A</span>Jupiter</label>
          <input id="tfc-07-b" type="radio" name="tfc-07-answer" class="peer/b sr-only">
          <label for="tfc-07-b" class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-xl border border-tfc07-yellow/15 bg-white/4 px-4 text-[13px] text-tfc07-ink/70 transition-colors duration-200 hover:border-tfc07-yellow/35 hover:bg-tfc07-yellow/10 hover:text-white peer-checked/b:border-tfc07-amber peer-checked/b:bg-tfc07-amber/15 peer-checked/b:text-white peer-focus-visible/b:outline-2 peer-focus-visible/b:outline-tfc07-amber peer-focus-visible/b:outline-offset-2"><span class="grid size-5.5 shrink-0 place-items-center rounded-md bg-tfc07-yellow/15 text-[11px] font-bold text-tfc07-amber">B</span>Saturn</label>
          <input id="tfc-07-c" type="radio" name="tfc-07-answer" class="peer/c sr-only">
          <label for="tfc-07-c" class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-xl border border-tfc07-yellow/15 bg-white/4 px-4 text-[13px] text-tfc07-ink/70 transition-colors duration-200 hover:border-tfc07-yellow/35 hover:bg-tfc07-yellow/10 hover:text-white peer-checked/c:border-tfc07-amber peer-checked/c:bg-tfc07-amber/15 peer-checked/c:text-white peer-focus-visible/c:outline-2 peer-focus-visible/c:outline-tfc07-amber peer-focus-visible/c:outline-offset-2"><span class="grid size-5.5 shrink-0 place-items-center rounded-md bg-tfc07-yellow/15 text-[11px] font-bold text-tfc07-amber">C</span>Uranus</label>
          <input id="tfc-07-d" type="radio" name="tfc-07-answer" class="peer/d sr-only">
          <label for="tfc-07-d" class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-xl border border-tfc07-yellow/15 bg-white/4 px-4 text-[13px] text-tfc07-ink/70 transition-colors duration-200 hover:border-tfc07-yellow/35 hover:bg-tfc07-yellow/10 hover:text-white peer-checked/d:border-tfc07-amber peer-checked/d:bg-tfc07-amber/15 peer-checked/d:text-white peer-focus-visible/d:outline-2 peer-focus-visible/d:outline-tfc07-amber peer-focus-visible/d:outline-offset-2"><span class="grid size-5.5 shrink-0 place-items-center rounded-md bg-tfc07-yellow/15 text-[11px] font-bold text-tfc07-amber">D</span>Neptune</label>
        </fieldset>
        <p class="mt-auto text-[10px] tracking-[0.08em] text-tfc07-dim">Hover, tap or press Space to reveal &rarr;</p>
      </div>

      <div class="absolute inset-0 flex flex-col items-center gap-4 rounded-3xl overflow-hidden px-7 py-9 bg-linear-145 from-tfc07-back to-tfc07-back2 border border-tfc07-green/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.6_0.17_150/0.3)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden] before:absolute before:inset-0 before:bg-[radial-gradient(ellipse_at_50%_30%,oklch(0.7_0.17_150/0.1),transparent_60%)]">
        <p class="relative z-1 text-[11px] font-bold uppercase tracking-[0.15em] text-tfc07-green">Correct answer</p>
        <span class="relative z-1 grid size-12 place-items-center rounded-full border-2 border-tfc07-green/35 bg-tfc07-green/15">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="text-tfc07-green" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        </span>
        <p class="relative z-1 text-center text-[26px] font-black leading-tight tracking-[-0.02em] text-white">B &mdash; Saturn</p>
        <span class="relative z-1 h-0.5 w-15 bg-linear-to-r from-transparent via-tfc07-green/40 to-transparent"></span>
        <p class="relative z-1 text-center text-[13px] leading-[1.7] text-tfc07-ink/65 text-pretty">Saturn holds the record with 146 confirmed moons as of 2025, edging past Jupiter's 95. Saturn's moon Titan has a thick atmosphere and lakes of liquid methane.</p>
        <dl class="relative z-1 mt-auto flex gap-6 text-center">
          <div><dd class="text-[22px] font-extrabold text-tfc07-green">+10</dd><dt class="text-[10px] uppercase tracking-[0.1em] text-tfc07-dim">Points</dt></div>
          <div><dd class="text-[22px] font-extrabold text-tfc07-green">7/10</dd><dt class="text-[10px] uppercase tracking-[0.1em] text-tfc07-dim">Progress</dt></div>
        </dl>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc07-bg: #0c0c00;
  --color-tfc07-bg: oklch(0.14 0.02 100);
  --color-tfc07-panel: #1a1400;
  --color-tfc07-panel: oklch(0.2 0.04 95);
  --color-tfc07-panel2: #150f00;
  --color-tfc07-panel2: oklch(0.17 0.035 95);
  --color-tfc07-back: #051a08;
  --color-tfc07-back: oklch(0.19 0.05 150);
  --color-tfc07-back2: #071a0e;
  --color-tfc07-back2: oklch(0.2 0.045 155);
  --color-tfc07-yellow: #eab308;
  --color-tfc07-yellow: oklch(0.78 0.16 90);
  --color-tfc07-amber: #f59e0b;
  --color-tfc07-amber: oklch(0.77 0.16 70);
  --color-tfc07-green: #22c55e;
  --color-tfc07-green: oklch(0.73 0.18 150);
  --color-tfc07-ink: #fefce8;
  --color-tfc07-ink: oklch(0.98 0.02 100);
  --color-tfc07-dim: #8e8a6b;
  --color-tfc07-dim: oklch(0.63 0.03 95);
  --font-tfc07-sans: 'Sora', system-ui, sans-serif;
}

.tfc-07 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-07 * {
    transition-duration: 1ms !important;
  }
}
```
