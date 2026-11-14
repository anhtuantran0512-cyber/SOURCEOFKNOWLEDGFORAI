---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/tailwind-css-blockquote-component/"
title: "Tailwind CSS Blockquote Component"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The Tailwind UI testimonial pattern — dark slate card, ring-1 border, avatar with an indigo ring, quote in font-semibold — rebuilt twice: once as the exact…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Blockquote Component
Source: https://codefronts.com/snippets/css-blockquotes/tailwind-css-blockquote-component/

The Tailwind UI testimonial pattern — dark slate card, ring-1 border, avatar with an indigo ring, quote in font-semibold — rebuilt twice: once as the exact utility-class markup Tailwind users search for, and once as the plain-CSS translation that runs with zero build step (that's what renders here). Every utility is annotated with its CSS equivalent, so the demo doubles as a Tailwind-to-vanilla dictionary: ring-1 ring-white/10 is a box-shadow, not a border; divide-x is a sibling selector; the avatar ring is two stacked shadows.
## HTML
```html
<section class="bq-02" aria-label="Tailwind style blockquote component demo">
  <div class="bq-02__stage">
    <figure class="bq-02__card">
      <svg class="bq-02__logo" viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><path d="M16 4l12 7v10l-12 7L4 21V11z" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="16" cy="16" r="4.2" fill="currentColor"/></svg>
      <blockquote class="bq-02__text-lg">
        <p>“Utility classes made our design system reviewable. Every visual decision is right there in the diff — no hunting through stylesheets to find who set that margin.”</p>
      </blockquote>
      <figcaption class="bq-02__row">
        <img class="bq-02__avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=160&auto=format&fit=crop" alt="" width="40" height="40" loading="lazy">
        <div class="bq-02__who">
          <div class="bq-02__name">Judith Black</div>
          <div class="bq-02__role">CEO of Workcation</div>
        </div>
        <span class="bq-02__x" aria-hidden="true"></span>
        <div class="bq-02__meta">ring-1 · ring-white/10</div>
      </figcaption>
    </figure>
    <p class="bq-02__chip" aria-hidden="true">Tailwind pattern → plain CSS · ring = box-shadow · container query re-stack</p>
  </div>
</section>
```
## CSS
```css
.bq-02,
.bq-02 *,
.bq-02 *::before,
.bq-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.14 0.015 265);
  --card: oklch(0.21 0.02 265);
  --ink: oklch(0.97 0.005 250);
  --mut: oklch(0.67 0.02 260);
  --acc: oklch(0.6 0.19 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-02__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(90% 70% at 50% 110%,oklch(0.22 0.05 275/.6),transparent),var(--bg);
  overflow-y: auto;
}

.bq-02__card {
  width: min(100%,36rem);
  padding: 2rem;
  border-radius: 1rem;
  background: var(--card);
  box-shadow: 0 0 0 1px oklch(1 0 0/.1),0 22px 50px oklch(0 0 0/.42);
  container-type: inline-size;
}

.bq-02__logo {
  color: var(--acc);
  margin-bottom: 1.25rem;
  display: block;
}

.bq-02__text-lg p {
  font-size: 1.125rem;
  line-height: 1.65;
  font-weight: 600;
  letter-spacing: -.008em;
  text-wrap: pretty;
}

.bq-02__row {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-top: 1.5rem;
}

.bq-02__avatar {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 99px;
  object-fit: cover;
  flex: none;
  background: linear-gradient(135deg,oklch(0.5 0.1 275),oklch(0.35 0.06 300));
  box-shadow: 0 0 0 2px var(--acc),0 0 0 4px color-mix(in oklch,var(--acc) 30%,transparent);
}

.bq-02__name {
  font-size: .9rem;
  font-weight: 650;
}

.bq-02__role {
  font-size: .82rem;
  color: var(--mut);
  margin-top: 1px;
}

.bq-02__x {
  width: 1px;
  height: 1.6rem;
  background: oklch(1 0 0/.12);
  margin-left: auto;
}

.bq-02__meta {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .7rem;
  color: var(--mut);
}

.bq-02__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border-radius: 99px;
  box-shadow: 0 0 0 1px oklch(1 0 0/.1);
}

@container (width < 420px) {
  .bq-02__row {
    flex-wrap: wrap;
  }

  .bq-02__x,
    .bq-02__meta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bq-02 * {
    transition-duration: .01ms !important;
  }
}
```
