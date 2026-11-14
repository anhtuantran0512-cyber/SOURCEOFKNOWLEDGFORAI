---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/testimonial-card/"
title: "Customer Testimonial Blockquote Card HTML CSS"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The conversion-page workhorse: a testimonial card with a five-star rating done accessibly (one img-role SVG with a real label — not five emoji a screen…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Customer Testimonial Blockquote Card HTML CSS
Source: https://codefronts.com/snippets/css-blockquotes/testimonial-card/

The conversion-page workhorse: a testimonial card with a five-star rating done accessibly (one img-role SVG with a real label — not five emoji a screen reader announces as 'star star star star star'), verified-purchase badge, avatar, and a metric callout — because testimonials with a number ('cut our onboarding time 40%') convert measurably better than adjectives. The card lifts on hover with translate + shadow deepening, and the whole layout re-stacks via container query when pasted into a narrow column.
## HTML
```html
<section class="bq-14" aria-label="Customer testimonial card demo">
  <div class="bq-14__stage">
    <figure class="bq-14__card" tabindex="0">
      <div class="bq-14__top">
        <p class="bq-14__stars"><svg role="img" aria-label="Rated 5 out of 5 stars" viewBox="0 0 128 24" width="112" height="21"><defs><path id="bq14s" d="M12 2.2l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17l-5.8 3.1 1.1-6.5L2.6 9l6.5-.9z"/></defs><use href="#bq14s" fill="currentColor"/><use href="#bq14s" x="26" fill="currentColor"/><use href="#bq14s" x="52" fill="currentColor"/><use href="#bq14s" x="78" fill="currentColor"/><use href="#bq14s" x="104" fill="currentColor"/></svg></p>
        <span class="bq-14__badge"><svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M8 1.4l1.8 1.3 2.2-.1.7 2.1 1.9 1.2-.7 2.1.7 2.1-1.9 1.2-.7 2.1-2.2-.1L8 14.6l-1.8-1.3-2.2.1-.7-2.1L1.4 10l.7-2.1-.7-2.1 1.9-1.2.7-2.1 2.2.1z" fill="currentColor" opacity=".25"/><path d="M5.2 8.2l1.9 1.9 3.7-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified customer</span>
      </div>
      <blockquote class="bq-14__quote">
        <p>Rollouts used to be a two-week negotiation with our ops team. With Relay's staged deploys we shipped to 40 clinics in an afternoon — and nobody had to stay late.</p>
      </blockquote>
      <div class="bq-14__foot">
        <figcaption class="bq-14__who">
          <img class="bq-14__ava" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=120&auto=format&fit=crop" alt="" width="40" height="40" loading="lazy">
          <span><strong>Dr. Priya Raman</strong><br><em>Director of Operations, Northcare Health</em></span>
        </figcaption>
        <p class="bq-14__stat"><b>−63%</b><span>deploy time</span></p>
      </div>
    </figure>
    <p class="bq-14__chip" aria-hidden="true">role="img" star rating · metric callout · container-query re-stack</p>
  </div>
</section>
```
## CSS
```css
.bq-14,
.bq-14 *,
.bq-14 *::before,
.bq-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.965 0.006 160);
  --card: oklch(1 0 0);
  --ink: oklch(0.26 0.02 180);
  --mut: oklch(0.52 0.02 180);
  --acc: oklch(0.55 0.12 170);
  --gold: oklch(0.78 0.14 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-14__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% -10%,oklch(0.93 0.03 165/.8),transparent),var(--bg);
  overflow-y: auto;
}

.bq-14__card {
  width: min(100%,420px);
  padding: 24px 26px 22px;
  border-radius: 18px;
  background: var(--card);
  border: 1px solid oklch(0 0 0/.07);
  box-shadow: 0 2px 6px oklch(0.3 0.03 180/.06),0 14px 34px oklch(0.3 0.03 180/.1);
  transition: translate .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s;
  container-type: inline-size;
}

.bq-14__card:hover,
.bq-14__card:focus-visible {
  translate: 0 -4px;
  box-shadow: 0 4px 10px oklch(0.3 0.03 180/.08),0 26px 52px oklch(0.3 0.03 180/.16);
  transition-duration: .15s;
}

.bq-14__card:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.bq-14__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.bq-14__stars {
  color: var(--gold);
  line-height: 0;
}

.bq-14__badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 650;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  border-radius: 99px;
  padding: 5px 10px;
  white-space: nowrap;
}

.bq-14__quote {
  margin-top: 16px;
}

.bq-14__quote p {
  font-size: 15.5px;
  line-height: 1.62;
  text-wrap: pretty;
}

.bq-14__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid oklch(0 0 0/.07);
}

.bq-14__who {
  display: flex;
  align-items: center;
  gap: 11px;
  font-size: 12.5px;
  line-height: 1.45;
  color: var(--mut);
}

.bq-14__who strong {
  color: var(--ink);
  font-size: 13.5px;
  font-weight: 650;
}

.bq-14__who em {
  font-style: normal;
}

.bq-14__ava {
  width: 40px;
  height: 40px;
  border-radius: 99px;
  object-fit: cover;
  flex: none;
  background: linear-gradient(135deg,oklch(0.75 0.06 170),oklch(0.6 0.08 200));
}

.bq-14__stat {
  text-align: right;
  flex: none;
}

.bq-14__stat b {
  display: block;
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--acc);
}

.bq-14__stat span {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--mut);
}

@container (width < 340px) {
  .bq-14__foot {
    flex-direction: column;
    align-items: flex-start;
  }

  .bq-14__stat {
    text-align: left;
  }

  .bq-14__badge {
    display: none;
  }
}

.bq-14__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.09);
  border-radius: 99px;
  background: var(--card);
}

@media (prefers-reduced-motion: reduce) {
  .bq-14 * {
    transition-duration: .01ms !important;
  }
}
```
