---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/css-masonry-testimonial-wall-review-cards/"
title: "CSS Masonry Testimonial Wall Review Cards"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "The SaaS 'wall of love': one-line raves and paragraph-long reviews packed gap-free by CSS columns, star strips, a highlighted pull-quote card, and a big stat…"
has_js: "false"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Testimonial Wall Review Cards
Source: https://codefronts.com/layouts/css-masonry-layouts/css-masonry-testimonial-wall-review-cards/

The SaaS 'wall of love': one-line raves and paragraph-long reviews packed gap-free by CSS columns, star strips, a highlighted pull-quote card, and a big stat card sitting inside the flow. The wall fades out through a mask-image gradient into a 'Read all 2,314 reviews' call-to-action — the tasteful way to truncate social proof — and where scroll-driven animations are supported, cards float in as they enter the viewport. All CSS.
## HTML
```html
<section class="msn-08" aria-label="CSS masonry testimonial wall demo">
  <div class="msn-08__stage" tabindex="0">
    <header class="msn-08__head">
      <span class="msn-08__eyebrow">Wall of love</span>
      <h2>Teams ship faster on Lattice CI</h2>
      <p>2,314 verified reviews · 4.9 average</p>
    </header>
    <div class="msn-08__wallWrap">
      <div class="msn-08__wall">
        <article class="msn-08__card"><p class="msn-08__stars" style="--r:100%" aria-hidden="true"></p><span class="msn-08__sr">5 out of 5</span><blockquote>Cut our pipeline from 22 minutes to 6. The team thought the dashboard was lying.</blockquote><footer><i style="--a:oklch(0.78 0.1 40);--b:oklch(0.55 0.13 20)"></i><div><strong>Maya Lindqvist</strong><span>Platform lead, Fathom</span></div></footer></article>
        <article class="msn-08__card"><p class="msn-08__stars" style="--r:100%" aria-hidden="true"></p><span class="msn-08__sr">5 out of 5</span><blockquote>Onboarded 40 repos in an afternoon.</blockquote><footer><i style="--a:oklch(0.75 0.11 300);--b:oklch(0.5 0.13 330)"></i><div><strong>Dev Anand</strong><span>CTO, Brightline</span></div></footer></article>
        <article class="msn-08__card msn-08__card--accent"><p class="msn-08__stars" style="--r:100%" aria-hidden="true"></p><span class="msn-08__sr">5 out of 5</span><blockquote>The flaky-test quarantine alone paid for the year. Our on-call channel went from a horror feed to weather smalltalk. I have never seen a tool change team mood this fast.</blockquote><footer><i style="--a:oklch(0.85 0.08 90);--b:oklch(0.6 0.1 70)"></i><div><strong>Grace Obi</strong><span>Eng director, Northwind</span></div></footer></article>
        <article class="msn-08__stat"><strong>4.9</strong><p class="msn-08__stars" style="--r:98%" aria-hidden="true"></p><span class="msn-08__sr">4.9 out of 5 average</span><div class="msn-08__bars"><i style="--w:88%"></i><i style="--w:9%"></i><i style="--w:2%"></i><i style="--w:1%"></i><i style="--w:0%"></i></div><p>from 2,314 reviews on G2 &amp; Capterra</p></article>
        <article class="msn-08__card"><p class="msn-08__stars" style="--r:90%" aria-hidden="true"></p><span class="msn-08__sr">4.5 out of 5</span><blockquote>Migrated off Jenkins in a week. The PR annotations are so good our juniors stopped asking 'why did CI fail' in standup — the answer is already on the diff line.</blockquote><footer><i style="--a:oklch(0.72 0.09 220);--b:oklch(0.48 0.11 240)"></i><div><strong>Tomás Rivera</strong><span>Staff eng, Kelp</span></div></footer></article>
        <article class="msn-08__card"><p class="msn-08__stars" style="--r:100%" aria-hidden="true"></p><span class="msn-08__sr">5 out of 5</span><blockquote>Support answered at 2am on a Saturday. With the fix.</blockquote><footer><i style="--a:oklch(0.8 0.1 150);--b:oklch(0.55 0.12 170)"></i><div><strong>Hana Sato</strong><span>SRE, Loom &amp; Field</span></div></footer></article>
        <article class="msn-08__card"><p class="msn-08__stars" style="--r:100%" aria-hidden="true"></p><span class="msn-08__sr">5 out of 5</span><blockquote>We stopped writing 'CI is red, not my PR' in Slack. That sentence used to cost us an hour a day across the org.</blockquote><footer><i style="--a:oklch(0.7 0.12 330);--b:oklch(0.46 0.13 350)"></i><div><strong>Jonah Weiss</strong><span>Tech lead, Parcel</span></div></footer></article>
        <article class="msn-08__card"><p class="msn-08__stars" style="--r:95%" aria-hidden="true"></p><span class="msn-08__sr">4.7 out of 5</span><blockquote>Pricing that doesn't punish you for growing the team. Refreshing.</blockquote><footer><i style="--a:oklch(0.76 0.1 190);--b:oklch(0.5 0.11 210)"></i><div><strong>Amelia Clarke</strong><span>VP Eng, Statement</span></div></footer></article>
        <article class="msn-08__card"><p class="msn-08__stars" style="--r:100%" aria-hidden="true"></p><span class="msn-08__sr">5 out of 5</span><blockquote>The audit log export made our SOC 2 auditor smile. I didn't know they could.</blockquote><footer><i style="--a:oklch(0.82 0.07 60);--b:oklch(0.58 0.1 40)"></i><div><strong>Ravi Kapoor</strong><span>Security, Alpenglow</span></div></footer></article>
      </div>
    </div>
    <div class="msn-08__readAll"><a href="#reviews">Read all 2,314 reviews</a><span>Independently verified · updated weekly</span></div>
  </div>
</section>
```
## CSS
```css
.msn-08,
.msn-08 *,
.msn-08 *::before,
.msn-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-08 {
  --bg: oklch(0.975 0.008 85);
  --card: oklch(0.995 0.003 85);
  --ink: oklch(0.25 0.02 60);
  --mut: oklch(0.53 0.02 60);
  --line: oklch(0.9 0.01 85);
  --acc: oklch(0.55 0.16 155);
  --star: oklch(0.72 0.15 75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-08__stage {
  width: 100%;
  container: msn08/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-08__head {
  text-align: center;
  padding: clamp(28px,6cqi,52px) 20px 8px;
  display: grid;
  gap: 8px;
  justify-items: center;
}

.msn-08__eyebrow {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.msn-08__head h2 {
  font-size: clamp(22px,3.6cqi,34px);
  letter-spacing: -.025em;
  text-wrap: balance;
  max-width: 22ch;
}

.msn-08__head p {
  font-size: 13px;
  color: var(--mut);
}

.msn-08__wallWrap {
  mask-image: linear-gradient(180deg,#000 72%,transparent 97%);
}

.msn-08__wall {
  columns: 280px;
  column-gap: 14px;
  padding: clamp(18px,3cqi,30px);
}

.msn-08__card,
.msn-08__stat {
  break-inside: avoid;
  margin-bottom: 14px;
  border-radius: 16px;
  border: 1px solid var(--line);
  background: var(--card);
  padding: 18px 18px 16px;
  display: grid;
  gap: 11px;
  transition: translate .25s,box-shadow .25s;
}

.msn-08__card:hover {
  translate: 0 -3px;
  box-shadow: 0 12px 26px -14px oklch(0.4 0.05 60/.3);
}

.msn-08__stars {
  --pct: var(--r,100%);
  font-size: 13px;
  letter-spacing: 2.5px;
  line-height: 1;
}

.msn-08__stars::before {
  content: "★★★★★";
  background: linear-gradient(90deg,var(--star) var(--pct),oklch(0.88 0.01 85) var(--pct));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.msn-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.msn-08__card {
  position: relative;
}

.msn-08__card blockquote {
  font-size: 14px;
  line-height: 1.6;
  text-wrap: pretty;
}

.msn-08__card blockquote::before {
  content: "“";
  display: block;
  font-family: Georgia,serif;
  font-size: 30px;
  line-height: .4;
  color: var(--acc);
  margin-bottom: 8px;
}

.msn-08__card footer {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 2px;
}

.msn-08__card footer i {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  flex: none;
  background: linear-gradient(140deg,var(--a),var(--b));
}

.msn-08__card footer strong {
  display: block;
  font-size: 12.5px;
}

.msn-08__card footer span {
  display: block;
  font-size: 11.5px;
  color: var(--mut);
}

.msn-08__card--accent {
  background: var(--ink);
  border-color: var(--ink);
  color: oklch(0.97 0.005 85);
}

.msn-08__card--accent blockquote::before {
  color: oklch(0.8 0.12 155);
}

.msn-08__card--accent footer span {
  color: oklch(0.72 0.015 60);
}

.msn-08__stat {
  position: relative;
  text-align: left;
}

.msn-08__stat>strong {
  font-size: 44px;
  letter-spacing: -.04em;
  line-height: 1;
}

.msn-08__bars {
  display: grid;
  gap: 4px;
}

.msn-08__bars i {
  height: 7px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--acc) var(--w),oklch(0.92 0.01 85) var(--w));
}

.msn-08__stat p:last-child {
  font-size: 12px;
  color: var(--mut);
}

.msn-08__readAll {
  display: grid;
  justify-items: center;
  gap: 8px;
  padding: 0 20px clamp(28px,5cqi,48px);
}

.msn-08__readAll a {
  display: grid;
  place-items: center;
  min-height: 46px;
  padding: 0 24px;
  border-radius: 99px;
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.99 0 0);
  background: var(--acc);
  transition: background .2s,translate .2s;
}

.msn-08__readAll a:hover,
.msn-08__readAll a:focus-visible {
  background: oklch(0.48 0.16 155);
  translate: 0 -1px;
}

.msn-08__readAll a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.msn-08__readAll span {
  font-size: 11.5px;
  color: var(--mut);
}

@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    @keyframes msn08-in {
      from {
        opacity: 0;
        translate: 0 22px;
      }

      to {
        opacity: 1;
        translate: 0 0;
      }
    }

    .msn-08__card,
        .msn-08__stat {
      animation: msn08-in linear both;
      animation-timeline: view();
      animation-range: entry 0% entry 60%;
    }
  }
}

@container msn08 (width < 480px) {
  .msn-08__wall {
    columns: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-08 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
