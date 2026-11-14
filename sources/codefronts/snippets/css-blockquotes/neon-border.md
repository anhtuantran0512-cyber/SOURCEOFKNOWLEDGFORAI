---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/neon-border/"
title: "Glowing Neon Border CSS Quote Box"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "A neon sign built from box-shadows: the tube is a 2px border in a hot cyan, and the glow is four stacked shadows at increasing blur radii and decreasing…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glowing Neon Border CSS Quote Box
Source: https://codefronts.com/snippets/css-blockquotes/neon-border/

A neon sign built from box-shadows: the tube is a 2px border in a hot cyan, and the glow is four stacked shadows at increasing blur radii and decreasing alpha — the same falloff a real gas tube produces. The heading text glows with the matching text-shadow stack, and a once-in-a-while flicker (opacity keyframes with long steady holds) sells the electricity without strobing — and shuts off entirely under prefers-reduced-motion, because flicker is exactly what vestibular and photosensitive users need gone.
## HTML
```html
<section class="bq-10" aria-label="Neon border quote box demo">
  <div class="bq-10__stage">
    <figure class="bq-10__sign">
      <div class="bq-10__neon">
        <p class="bq-10__open" aria-hidden="true">EST · 2026</p>
        <blockquote>
          <p>The future is already here — it's just not evenly distributed.</p>
        </blockquote>
      </div>
      <figcaption class="bq-10__cap">WILLIAM GIBSON</figcaption>
    </figure>
    <p class="bq-10__chip" aria-hidden="true">4-layer box-shadow falloff · inset cast · flicker off under reduced-motion</p>
  </div>
</section>
```
## CSS
```css
.bq-10,
.bq-10 *,
.bq-10 *::before,
.bq-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.13 0.02 280);
  --ink: oklch(0.97 0.01 195);
  --cyan: oklch(0.85 0.15 195);
  --pink: oklch(0.8 0.16 350);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-10__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 30px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 30%,oklch(0.18 0.04 280),var(--bg) 75%);
  overflow-y: auto;
}

.bq-10__sign {
  display: grid;
  justify-items: center;
  gap: 22px;
  width: min(100%,560px);
}

.bq-10__neon {
  width: 100%;
  padding: clamp(26px,4.5vw,40px);
  border: 2px solid var(--cyan);
  border-radius: 18px;
  background: oklch(0.15 0.025 265/.65);
  box-shadow: 0 0 6px oklch(0.8 0.16 195/.9),0 0 18px oklch(0.75 0.17 195/.5),0 0 46px oklch(0.7 0.18 195/.3),inset 0 0 14px oklch(0.8 0.16 195/.22);
  animation: bq10-flicker 8s linear infinite;
}

.bq-10__open {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .34em;
  color: var(--cyan);
  text-shadow: 0 0 8px oklch(0.8 0.16 195/.8);
  margin-bottom: 14px;
}

.bq-10__neon blockquote p {
  font-size: clamp(21px,3vw,30px);
  line-height: 1.35;
  font-weight: 750;
  letter-spacing: -.01em;
  text-wrap: balance;
  color: var(--ink);
  text-shadow: 0 0 4px oklch(0.9 0.1 195/.9),0 0 14px oklch(0.8 0.16 195/.55),0 0 34px oklch(0.75 0.17 195/.3);
}

.bq-10__cap {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .3em;
  color: var(--pink);
  border: 1.5px solid var(--pink);
  border-radius: 99px;
  padding: 9px 18px;
  text-shadow: 0 0 8px oklch(0.75 0.17 350/.8);
  box-shadow: 0 0 6px oklch(0.75 0.17 350/.7),0 0 20px oklch(0.7 0.18 350/.35),inset 0 0 10px oklch(0.75 0.17 350/.18);
}

@keyframes bq10-flicker {
  0%,
    41%,
    43%,
    78%,
    80%,
    100% {
    opacity: 1;
  }

  42% {
    opacity: .62;
  }

  79% {
    opacity: .74;
  }
}

.bq-10__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: oklch(0.65 0.03 240);
  padding: 7px 13px;
  border: 1px solid oklch(1 0 0/.12);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .bq-10 * {
    transition-duration: .01ms !important;
  }

  .bq-10__neon {
    animation: none;
  }
}
```
