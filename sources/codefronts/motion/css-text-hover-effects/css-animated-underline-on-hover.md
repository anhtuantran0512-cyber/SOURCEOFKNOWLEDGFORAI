---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/css-animated-underline-on-hover/"
title: "CSS Animated Underline on Hover"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "The four underline animations every navbar ships in 2026, side by side: grow left→right, bloom from center, slide-through (the line exits the far side…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Underline on Hover
Source: https://codefronts.com/motion/css-text-hover-effects/css-animated-underline-on-hover/

The four underline animations every navbar ships in 2026, side by side: grow left→right, bloom from center, slide-through (the line exits the far side instead of retreating), and the pure text-decoration version that needs no pseudo-element at all. The first three are one background-image gradient sized from 0%→100% — cheaper than ::after, works on inline links that wrap — and the fourth animates text-decoration-color, thickness and underline-offset directly, which finally transitions in every modern engine.
## HTML
```html
<section class="cth-01" aria-label="Animated underline on hover demo">
  <div class="cth-01__stage">
    <div class="cth-01__scene">
      <header class="cth-01__masthead">
        <a class="cth-01__brand" href="#cth01-top" id="cth01-top">Ledger<span>&amp;</span>Loom</a>
        <span class="cth-01__chip">background-size: 0% &rarr; 100%</span>
      </header>
      <nav class="cth-01__nav" aria-label="Underline animation styles">
        <div class="cth-01__row">
          <span class="cth-01__tag">01 &middot; left &rarr; right</span>
          <a class="cth-01__link cth-01__link--ltr" href="#cth01-top">Selected work</a>
        </div>
        <div class="cth-01__row">
          <span class="cth-01__tag">02 &middot; center out</span>
          <a class="cth-01__link cth-01__link--center" href="#cth01-top">Studio journal</a>
        </div>
        <div class="cth-01__row">
          <span class="cth-01__tag">03 &middot; slide through</span>
          <a class="cth-01__link cth-01__link--thru" href="#cth01-top">About the practice</a>
        </div>
        <div class="cth-01__row">
          <span class="cth-01__tag">04 &middot; text-decoration</span>
          <a class="cth-01__link cth-01__link--native" href="#cth01-top">Get in touch</a>
        </div>
      </nav>
      <p class="cth-01__prose">Underlines also live inside prose: the <a href="#cth01-top">type specimens</a> and the <a href="#cth01-top">2026 grid audit</a> use the same gradient at marker weight &mdash; and because they're real inline links, they keep underlining when they wrap.</p>
      <p class="cth-01__hint">Hover the links &mdash; or press <kbd>Tab</kbd>. Every variant also fires on <code>:focus-visible</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-01,
.cth-01 *,
.cth-01 *::before,
.cth-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-01 {
  --bg: oklch(0.975 0.007 95);
  --ink: oklch(0.25 0.02 55);
  --mut: oklch(0.52 0.02 60);
  --acc: oklch(0.60 0.19 33);
  --line: oklch(0.89 0.012 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-01__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth01/inline-size;
}

.cth-01__scene {
  width: min(100%,780px);
  display: flex;
  flex-direction: column;
  gap: clamp(20px,3.5cqi,30px);
}

.cth-01__masthead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding-bottom: 16px;
  border-bottom: 1.5px solid var(--ink);
}

.cth-01__brand {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: inherit;
  text-decoration: none;
}

.cth-01__brand span {
  color: var(--acc);
}

.cth-01__brand:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 4px;
}

.cth-01__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  font-weight: 600;
  color: var(--acc);
  border: 1px solid color-mix(in oklch,var(--acc) 45%,transparent);
  border-radius: 99px;
  padding: 5px 11px;
  white-space: nowrap;
}

.cth-01__row {
  display: grid;
  grid-template-columns: 170px 1fr;
  gap: 6px 24px;
  align-items: baseline;
  padding: clamp(12px,2.2cqi,18px) 0;
  border-bottom: 1px solid var(--line);
}

.cth-01__tag {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-01__link {
  justify-self: start;
  font-size: clamp(24px,4.6cqi,38px);
  font-weight: 700;
  letter-spacing: -.02em;
  line-height: 1.2;
  color: inherit;
  text-decoration: none;
  padding-bottom: .12em;
}

.cth-01__link:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 5px;
  border-radius: 2px;
}

.cth-01__link--ltr,
.cth-01__link--center,
.cth-01__link--thru {
  background-image: linear-gradient(var(--acc),var(--acc));
  background-repeat: no-repeat;
  background-size: 0% .09em;
  transition: background-size .45s cubic-bezier(.22,1,.36,1);
}

.cth-01__link--ltr {
  background-position: 0% 100%;
}

.cth-01__link--center {
  background-position: 50% 100%;
}

.cth-01__link--thru {
  background-position: 100% 100%;
}

.cth-01__link--ltr:hover,
.cth-01__link--ltr:focus-visible,
.cth-01__link--center:hover,
.cth-01__link--center:focus-visible {
  background-size: 100% .09em;
}

.cth-01__link--thru:hover,
.cth-01__link--thru:focus-visible {
  background-position: 0% 100%;
  background-size: 100% .09em;
}

.cth-01__link--native {
  text-decoration-line: underline;
  text-decoration-color: transparent;
  text-decoration-thickness: .06em;
  text-underline-offset: .32em;
  text-decoration-skip-ink: auto;
  transition: text-decoration-color .35s ease,text-underline-offset .35s cubic-bezier(.22,1,.36,1),text-decoration-thickness .35s ease;
}

.cth-01__link--native:hover,
.cth-01__link--native:focus-visible {
  text-decoration-color: var(--acc);
  text-underline-offset: .14em;
  text-decoration-thickness: .1em;
}

.cth-01__prose {
  font-size: 15px;
  line-height: 1.75;
  color: var(--mut);
  max-width: 58ch;
}

.cth-01__prose a {
  color: var(--ink);
  font-weight: 650;
  text-decoration: none;
  background-image: linear-gradient(color-mix(in oklch,var(--acc) 32%,transparent),color-mix(in oklch,var(--acc) 32%,transparent));
  background-repeat: no-repeat;
  background-position: 0 88%;
  background-size: 100% .14em;
  transition: background-size .3s ease;
}

.cth-01__prose a:hover,
.cth-01__prose a:focus-visible {
  background-size: 100% .6em;
}

.cth-01__prose a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cth-01__hint {
  font-size: 12.5px;
  color: var(--mut);
}

.cth-01__hint kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 2px 6px;
  background: oklch(1 0 0);
}

.cth-01__hint code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .92em;
  background: oklch(0.93 0.01 95);
  padding: 1px 5px;
  border-radius: 4px;
}

@container cth01 (width < 560px) {
  .cth-01__row {
    grid-template-columns: 1fr;
  }

  .cth-01__chip {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cth-01 * {
    transition-duration: .01ms !important;
  }
}
```
