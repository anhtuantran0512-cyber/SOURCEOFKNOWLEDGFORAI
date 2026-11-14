---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/glassmorphism-faq-accordion-with-drop-shadow/"
title: "Glassmorphism FAQ Accordion with Drop Shadow"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "Frosted-glass FAQ panels floating over a photographic backdrop: backdrop-filter: blur() + saturate() does the glass, a 1px inset highlight fakes the beveled…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism FAQ Accordion with Drop Shadow
Source: https://codefronts.com/snippets/css-faq-accordion/glassmorphism-faq-accordion-with-drop-shadow/

Frosted-glass FAQ panels floating over a photographic backdrop: backdrop-filter: blur() + saturate() does the glass, a 1px inset highlight fakes the beveled edge, and a soft colored drop shadow lifts each card off the scene. The open panel brightens and blurs deeper, so state reads through the material itself. Includes the two rules 90% of glassmorphism tutorials miss — the saturation boost and the top-edge highlight — plus a no-blur fallback that keeps text legible everywhere.
## HTML
```html
<section class="cfa-07" aria-label="Glassmorphism FAQ accordion">
  <div class="cfa-07__scene">
    <div class="cfa-07__wrap">
      <header class="cfa-07__head">
        <h1>Membership FAQ</h1>
        <p>Four layers make the glass: tint, frost, edge, highlight. The open panel frosts deeper.</p>
      </header>
      <div class="cfa-07__list">
        <details class="cfa-07__item" open>
          <summary class="cfa-07__q">What does membership include?<i aria-hidden="true"></i></summary>
          <div class="cfa-07__a"><p>Unlimited access to every studio location, all live classes, and the on-demand library. Founding members also lock their rate for life — it never increases while the membership stays active.</p></div>
        </details>
        <details class="cfa-07__item">
          <summary class="cfa-07__q">Can I freeze my membership?<i aria-hidden="true"></i></summary>
          <div class="cfa-07__a"><p>Yes — up to 3 months per year, in one-month blocks, straight from the app. Frozen months push your renewal date back, so you never pay for time you can't use.</p></div>
        </details>
        <details class="cfa-07__item">
          <summary class="cfa-07__q">Do you offer day passes for guests?<i aria-hidden="true"></i></summary>
          <div class="cfa-07__a"><p>Every member gets 2 free guest passes a month. Additional passes are $15 and guests who join within 7 days get their pass credited toward the first month.</p></div>
        </details>
        <details class="cfa-07__item">
          <summary class="cfa-07__q">Which locations are open 24/7?<i aria-hidden="true"></i></summary>
          <div class="cfa-07__a"><p>All flagship locations run 24/7 with app-based entry. Neighborhood studios open 5am–11pm; the app map badges each one with live hours and current capacity.</p></div>
        </details>
      </div>
      <p class="cfa-07__foot">backdrop-filter: blur(18px) saturate(1.6) — the saturate() is what makes it glass, not smear.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cfa-07,
.cfa-07 *,
.cfa-07 *::before,
.cfa-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-07 {
  --ink: oklch(0.99 0.003 280);
  --mut: oklch(0.93 0.015 285);
  --blur: 18px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-07__scene {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background-image: linear-gradient(160deg,oklch(0.45 0.2 290/.55),oklch(0.5 0.22 340/.35) 55%,oklch(0.55 0.18 240/.5)),url('https://images.unsplash.com/photo-1518098268026-4e89f1a2cd8e?q=80&w=1800&auto=format&fit=crop');
  background-size: cover;
  background-position: center;
}

.cfa-07__wrap {
  width: min(100%,620px);
}

.cfa-07__head h1 {
  font-size: clamp(28px,4.5cqi,40px);
  font-weight: 800;
  letter-spacing: -.025em;
  text-shadow: 0 2px 24px oklch(0.2 0.08 290/.6);
}

.cfa-07__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
  text-shadow: 0 1px 12px oklch(0.2 0.08 290/.7);
}

.cfa-07__list {
  margin-top: 26px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  interpolate-size: allow-keywords;
}

.cfa-07__item {
  background: oklch(1 0 0/.14);
  -webkit-backdrop-filter: blur(var(--blur)) saturate(1.6);
  backdrop-filter: blur(var(--blur)) saturate(1.6);
  border: 1px solid oklch(1 0 0/.28);
  border-radius: 18px;
  box-shadow: inset 0 1px 0 oklch(1 0 0/.35),0 24px 48px oklch(0.3 0.12 290/.35);
  transition: background .35s,box-shadow .35s,-webkit-backdrop-filter .35s,backdrop-filter .35s;
}

.cfa-07__item[open] {
  background: oklch(1 0 0/.22);
  -webkit-backdrop-filter: blur(26px) saturate(1.8);
  backdrop-filter: blur(26px) saturate(1.8);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.45),0 30px 60px oklch(0.3 0.12 290/.45);
}

@supports not (backdrop-filter: blur(1px)) {
  .cfa-07__item {
    background: oklch(0.35 0.08 290/.92);
  }

  .cfa-07__item[open] {
    background: oklch(0.32 0.08 290/.96);
  }
}

.cfa-07__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 17px 20px;
  cursor: pointer;
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.01em;
  list-style: none;
}

.cfa-07__q::-webkit-details-marker {
  display: none;
}

.cfa-07__q:focus-visible {
  outline: 2px solid oklch(0.99 0.003 280);
  outline-offset: -2px;
  border-radius: 18px;
}

.cfa-07__q i {
  flex: none;
  display: grid;
  place-items: center;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 1.5px solid oklch(1 0 0/.4);
  position: relative;
  transition: rotate .4s cubic-bezier(.4,0,.2,1),background .3s;
}

.cfa-07__q i::before {
  content: "";
  width: 8px;
  height: 8px;
  border-right: 1.5px solid var(--ink);
  border-bottom: 1.5px solid var(--ink);
  rotate: 45deg;
  translate: 0 -1.5px;
}

.cfa-07__item[open] .cfa-07__q i {
  rotate: 180deg;
  background: oklch(1 0 0/.18);
}

.cfa-07__q:hover i {
  background: oklch(1 0 0/.18);
}

.cfa-07__a p {
  padding: 0 20px 18px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 58ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-07__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .4s cubic-bezier(.4,0,.2,1),opacity .32s,content-visibility .4s allow-discrete;
  }

  .cfa-07__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-07__foot {
  margin-top: 22px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  color: var(--mut);
  text-shadow: 0 1px 10px oklch(0.2 0.08 290/.7);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-07 *,
    .cfa-07 .cfa-07__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
