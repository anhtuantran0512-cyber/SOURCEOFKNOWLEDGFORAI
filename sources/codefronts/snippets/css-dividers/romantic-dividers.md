---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/romantic-dividers/"
title: "Wedding Heart Icon Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "An invitation-grade divider: two hairlines fading toward a centred heart, with the heart drawn by clip-path rather than an emoji — so it inherits your…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Wedding Heart Icon Divider CSS
Source: https://codefronts.com/snippets/css-dividers/romantic-dividers/

An invitation-grade divider: two hairlines fading toward a centred heart, with the heart drawn by clip-path rather than an emoji — so it inherits your palette, scales cleanly, and never renders as someone else's cartoon glyph. A slow, tiny beat animation adds life without turning a wedding page into a toy, and the whole thing is one flex row.
## HTML
```html
<section class="div-16" aria-label="Wedding heart icon divider demo">
  <div class="div-16__stage">
    <div class="div-16__frame">
      <p class="div-16__eyebrow">TOGETHER WITH THEIR FAMILIES</p>
      <h2 class="div-16__names">Amara <span class="div-16__amp">&amp;</span> Elias</h2>
      <div class="div-16__rule" role="separator" aria-label="Divider">
        <span class="div-16__heart" aria-hidden="true"></span>
      </div>
      <p class="div-16__date">SATURDAY, THE TWELFTH OF SEPTEMBER<br>TWO THOUSAND TWENTY-SEVEN</p>
      <div class="div-16__rule div-16__rule--short" role="separator" aria-label="Divider">
        <span class="div-16__dot" aria-hidden="true"></span>
      </div>
      <p class="div-16__place">The Old Orangery · Bath, England</p>
    </div>
    <p class="div-16__chip">clip-path:path() heart · inward-fading rules · 4% beat</p>
  </div>
</section>
```
## CSS
```css
.div-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-16-bg);
  --div-16-bg: oklch(0.975 0.012 30);
  --div-16-card: oklch(1 0.004 30);
  --div-16-ink: oklch(0.32 0.03 25);
  --div-16-mut: oklch(0.56 0.03 25);
  --div-16-line: oklch(0.32 0.03 25/.24);
  --div-16-acc: oklch(0.68 0.11 18);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-16-ink);
}

.div-16 *,
.div-16 *::before,
.div-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-16__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 20px;
  padding: clamp(24px,5vw,60px) clamp(20px,5vw,56px);
  background: radial-gradient(100% 70% at 50% 0%,oklch(0.99 0.014 28),transparent);
}

.div-16__frame {
  width: min(92vw,520px);
  background: var(--div-16-card);
  border: 1px solid var(--div-16-line);
  border-radius: 4px;
  padding: clamp(34px,6vw,62px) clamp(24px,5vw,52px);
  text-align: center;
  display: grid;
  justify-items: center;
  gap: clamp(16px,3vw,26px);
  box-shadow: 0 20px 50px oklch(0.32 0.03 25/.09);
  position: relative;
}

.div-16__frame::before {
  content: '';
  position: absolute;
  inset: 9px;
  border: 1px solid oklch(0.68 0.11 18/.3);
  border-radius: 2px;
  pointer-events: none;
}

.div-16__eyebrow {
  font-size: 10.5px;
  letter-spacing: .3em;
  color: var(--div-16-mut);
}

.div-16__names {
  font-family: Georgia,'Iowan Old Style',serif;
  font-size: clamp(32px,7vw,62px);
  line-height: 1.08;
  font-weight: 400;
  letter-spacing: .01em;
  font-style: italic;
}

.div-16__amp {
  color: var(--div-16-acc);
  font-size: .72em;
  padding: 0 .06em;
}

.div-16__rule {
  width: 100%;
  max-width: 320px;
  display: flex;
  align-items: center;
  gap: 14px;
}

.div-16__rule::before,
.div-16__rule::after {
  content: '';
  flex: 1 1 0;
  height: 1px;
}

.div-16__rule::before {
  background: linear-gradient(90deg,transparent,var(--div-16-line) 88%);
}

.div-16__rule::after {
  background: linear-gradient(90deg,var(--div-16-line) 12%,transparent);
}

.div-16__rule--short {
  max-width: 180px;
}

.div-16__heart {
  width: 17px;
  height: 17px;
  flex: none;
  background: var(--div-16-acc);
  clip-path: path('M8.5 15.6 1.9 9.1a4.1 4.1 0 1 1 6.6-4.7 4.1 4.1 0 1 1 6.6 4.7Z');
  animation: div-16-beat 2.4s ease-in-out infinite;
}

@keyframes div-16-beat {
  0%,
    72%,
    100% {
    scale: 1;
  }

  80% {
    scale: 1.04;
  }

  88% {
    scale: 1;
  }
}

.div-16__dot {
  width: 5px;
  height: 5px;
  flex: none;
  border-radius: 99px;
  background: var(--div-16-acc);
  opacity: .8;
}

.div-16__date {
  font-size: 11.5px;
  letter-spacing: .22em;
  line-height: 2.2;
  color: var(--div-16-mut);
}

.div-16__place {
  font-family: Georgia,serif;
  font-style: italic;
  font-size: clamp(14px,1.9vw,17px);
  color: var(--div-16-ink);
}

.div-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-16-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-16-line);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .div-16__heart {
    animation: none;
  }
}
```
