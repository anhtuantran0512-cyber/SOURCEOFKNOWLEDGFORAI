---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/expandable-read-more-testimonial-card/"
title: "Expandable Read More Testimonial Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Long reviews wreck grid layouts."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Read More Testimonial Card
Source: https://codefronts.com/components/css-testimonials-reviews/expandable-read-more-testimonial-card/

Long reviews wreck grid layouts. This card clamps every quote to four lines, then expands it with a genuinely animated height — the thing CSS could not do until interpolate-size: allow-keywords and calc-size() landed. It is built on <details> and <summary>, so the toggle is a native, keyboard-operable, screen-reader-announced disclosure with zero JavaScript and zero ARIA to get wrong.
## HTML
```html
<section class="tr-09" aria-label="Expandable read more testimonial card demo">
  <div class="tr-09__stage">
    <header class="tr-09__head">
      <p class="tr-09__eyebrow">Long-form reviews</p>
      <h2 class="tr-09__title">Four lines, then as much as they wrote</h2>
    </header>

    <div class="tr-09__grid">
      <figure class="tr-09__card">
        <div class="tr-09__top">
          <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Farah Haddad" width="46" height="46" loading="lazy" decoding="async">
          <div><b>Farah Haddad</b><span>Head of Learning · Kestrel Group</span></div>
          <span class="tr-09__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</span>
        </div>
        <blockquote class="tr-09__prev"><p>We ran the pilot with 40 people across three offices and honestly expected the usual half-hearted adoption curve. What happened instead was that the Prague team finished the first module in two days and started asking for the next one, which has never happened with any platform we have bought.</p></blockquote>
        <details class="tr-09__more">
          <summary class="tr-09__sum"><span></span></summary>
          <div class="tr-09__rest">
            <p>The part that changed my mind was the reporting. I could see, per cohort, which sections people re-watched — and it turned out our own onboarding video was the bottleneck, not the tool. We re-recorded it in an afternoon and completion went from 61% to 94%.</p>
            <p>Six months on, the finance team asked me to justify the renewal and the honest answer was that it replaced a contractor. That is not a metric I expected to be able to point at.</p>
          </div>
        </details>
        <footer class="tr-09__f"><time datetime="2026-07-02">2 July 2026</time> · Verified customer · 8 months using</footer>
      </figure>

      <figure class="tr-09__card">
        <div class="tr-09__top">
          <img src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Ethan Park" width="46" height="46" loading="lazy" decoding="async">
          <div><b>Ethan Park</b><span>Founder · Northgate Studio</span></div>
          <span class="tr-09__stars" role="img" aria-label="Rated 4 out of 5">★★★★<span>★</span></span>
        </div>
        <blockquote class="tr-09__prev"><p>I will start with the criticism because it is short: the mobile app was clearly built second and it shows in the editor. Everything else has been the least painful software purchase of my career, and I have made some genuinely painful ones.</p></blockquote>
        <details class="tr-09__more">
          <summary class="tr-09__sum"><span></span></summary>
          <div class="tr-09__rest">
            <p>Setup took an afternoon. Importing eleven years of client records took a support call and a CSV, and the person on that call spotted a duplicate-matching problem in our data that we had been living with since 2019.</p>
            <p>We are a five-person studio. The reason this matters is that nobody here has time to become an admin for anything, and after the first week nobody has had to.</p>
          </div>
        </details>
        <footer class="tr-09__f"><time datetime="2026-05-19">19 May 2026</time> · Verified customer · 2 years using</footer>
      </figure>
    </div>
    <p class="tr-09__chip" aria-hidden="true">&lt;details&gt; · ::details-content · interpolate-size:allow-keywords · calc-size(auto) · line-clamp</p>
  </div>
</section>
```
## CSS
```css
.tr-09,
.tr-09 *,
.tr-09 *::before,
.tr-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  interpolate-size: allow-keywords;
  --tr-09-bg: oklch(0.97 0.01 200);
  --tr-09-card: oklch(1 0 0);
  --tr-09-ink: oklch(0.23 0.02 230);
  --tr-09-mut: oklch(0.55 0.02 230);
  --tr-09-acc: oklch(0.58 0.14 205);
  --tr-09-star: oklch(0.75 0.15 70);
  background: var(--tr-09-bg);
  color: var(--tr-09-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,32px);
  padding: clamp(18px,4vw,54px);
}

.tr-09__head {
  text-align: center;
  display: grid;
  gap: 9px;
}

.tr-09__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tr-09-acc);
}

.tr-09__title {
  font-size: clamp(23px,3.6vw,38px);
  font-weight: 670;
  letter-spacing: -.035em;
  line-height: 1.12;
  text-wrap: balance;
}

.tr-09__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,330px),1fr));
  gap: clamp(14px,2vw,20px);
  width: min(100%,900px);
  align-items: start;
}

.tr-09__card {
  display: grid;
  gap: 14px;
  padding: clamp(20px,2.6vw,26px);
  background: var(--tr-09-card);
  border: 1px solid oklch(0 0 0/.075);
  border-radius: 20px;
  box-shadow: 0 1px 2px oklch(0 0 0/.045),0 22px 46px -32px oklch(0.3 0.05 230/.7);
  animation: tr-09-in .7s cubic-bezier(.16,1,.3,1) both;
}

.tr-09__card:nth-child(2) {
  animation-delay: .1s;
}

@keyframes tr-09-in {
  from {
    opacity: 0;
    translate: 0 16px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-09__top {
  display: flex;
  align-items: center;
  gap: 11px;
}

.tr-09__top img {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: oklch(0.88 0.02 220);
}

.tr-09__top div {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.tr-09__top b {
  font-size: 14.5px;
  font-weight: 650;
  letter-spacing: -.014em;
}

.tr-09__top span {
  font-size: 12px;
  color: var(--tr-09-mut);
}

.tr-09__stars {
  margin-inline-start: auto;
  font-size: 14px;
  letter-spacing: 1.5px;
  color: var(--tr-09-star);
  flex: none;
}

.tr-09__stars span {
  color: oklch(0 0 0/.14);
}

.tr-09__more {
  display: grid;
}

.tr-09__prev p {
  font-size: 15px;
  line-height: 1.62;
  color: color-mix(in oklch,var(--tr-09-ink) 90%,transparent);
  text-wrap: pretty;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  line-clamp: 4;
  overflow: hidden;
  transition: -webkit-line-clamp .4s;
}

.tr-09__card:has(.tr-09__more[open]) .tr-09__prev p {
  -webkit-line-clamp: 24;
  line-clamp: 24;
}

.tr-09__rest {
  display: grid;
  gap: 12px;
  padding-top: 12px;
}

.tr-09__rest p {
  font-size: 15px;
  line-height: 1.62;
  color: color-mix(in oklch,var(--tr-09-ink) 88%,transparent);
  text-wrap: pretty;
}

.tr-09__more::details-content {
  block-size: 0;
  overflow: clip;
  opacity: 0;
  transition: block-size .45s cubic-bezier(.16,1,.3,1),opacity .35s ease,content-visibility .45s allow-discrete;
}

.tr-09__more[open]::details-content {
  block-size: auto;
  opacity: 1;
}

.tr-09__sum {
  list-style: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  margin-top: 6px;
  font-size: 13.5px;
  font-weight: 640;
  color: var(--tr-09-acc);
  cursor: pointer;
  width: fit-content;
  user-select: none;
}

.tr-09__sum::-webkit-details-marker {
  display: none;
}

.tr-09__sum span::after {
  content: 'Read the full review';
}

.tr-09__more[open] .tr-09__sum span::after {
  content: 'Show less';
}

.tr-09__sum::after {
  content: '';
  width: 9px;
  height: 9px;
  border-inline-end: 2px solid currentColor;
  border-block-end: 2px solid currentColor;
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s cubic-bezier(.16,1,.3,1),translate .35s;
}

.tr-09__more[open] .tr-09__sum::after {
  rotate: 225deg;
  translate: 0 2px;
}

.tr-09__sum:focus-visible {
  outline: 3px solid var(--tr-09-acc);
  outline-offset: 4px;
  border-radius: 8px;
}

.tr-09__sum:hover {
  color: color-mix(in oklch,var(--tr-09-acc) 78%,black);
}

.tr-09__f {
  font-size: 11.5px;
  color: var(--tr-09-mut);
  padding-top: 14px;
  border-top: 1px solid oklch(0 0 0/.07);
}

.tr-09__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-09-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.6);
}

@media (prefers-reduced-motion: reduce) {
  .tr-09__card {
    animation: none;
  }

  .tr-09__more::details-content {
    transition: none;
  }

  .tr-09__sum::after {
    transition: none;
  }
}
```
