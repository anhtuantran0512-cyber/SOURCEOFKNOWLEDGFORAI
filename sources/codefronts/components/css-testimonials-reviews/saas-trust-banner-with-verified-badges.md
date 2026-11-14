---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/saas-trust-banner-with-verified-badges/"
title: "SaaS Trust Banner with Verified Badges"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The compressed strip of credibility that sits directly under a SaaS hero — avatar stack, aggregate rating, two hard metrics and a rotating verified quote,…"
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Trust Banner with Verified Badges
Source: https://codefronts.com/components/css-testimonials-reviews/saas-trust-banner-with-verified-badges/

The compressed strip of credibility that sits directly under a SaaS hero — avatar stack, aggregate rating, two hard metrics and a rotating verified quote, all in one 88-pixel-tall band. CRO teams in Tier-1 markets consistently find this the highest-leverage 100 lines on a landing page, because it answers "do real companies use this?" before the visitor has scrolled once.
## HTML
```html
<section class="tr-02" aria-label="SaaS trust banner with verified badges demo">
  <div class="tr-02__stage">
    <div class="tr-02__hero" aria-hidden="true">
      <p class="tr-02__kicker">Deploy previews for every branch</p>
      <h2 class="tr-02__h">Ship on Friday.<br>Sleep on Saturday.</h2>
    </div>

    <div class="tr-02__band">
      <div class="tr-02__seg">
        <div class="tr-02__stack" aria-hidden="true">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=96&h=96&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=96&h=96&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=96&h=96&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=96&h=96&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async">
          <span class="tr-02__more">+9k</span>
        </div>
        <p class="tr-02__label">Trusted by <b>9,240</b> engineering teams</p>
      </div>

      <div class="tr-02__seg">
        <div class="tr-02__rating" role="img" aria-label="Rated 4.8 out of 5 from 2,140 verified reviews">
          <span class="tr-02__stars" aria-hidden="true">
            <svg viewBox="0 0 20 20"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg class="tr-02__half" viewBox="0 0 20 20"><defs><linearGradient id="tr-02-hg"><stop offset="80%" stop-color="currentColor"/><stop offset="80%" stop-color="transparent"/></linearGradient></defs><path fill="url(#tr-02-hg)" d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
          </span>
          <b class="tr-02__score">4.8</b>
        </div>
        <p class="tr-02__label">2,140 verified reviews</p>
      </div>

      <div class="tr-02__seg tr-02__seg--pills">
        <span class="tr-02__pill"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 2l6 2.6v5c0 3.9-2.5 7.4-6 8.4-3.5-1-6-4.5-6-8.4v-5L10 2z" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M7.2 10.1l1.9 1.9 3.7-3.9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>SOC 2 Type II</span>
        <span class="tr-02__pill"><b>99.99%</b> uptime, 12&nbsp;mo</span>
        <span class="tr-02__pill"><b>&lt;40ms</b> p95 edge</span>
      </div>

      <div class="tr-02__seg tr-02__seg--quote">
        <div class="tr-02__rotator">
          <figure class="tr-02__q" style="--tr-02-i:0">
            <blockquote>“Cut our release cycle from ten days to a morning.”</blockquote>
            <figcaption><b>Tomas Lindqvist</b> · Head of Eng, Ardent <span class="tr-02__ver"><svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.4" fill="currentColor"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="oklch(0.16 0.02 260)" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified customer</span></figcaption>
          </figure>
          <figure class="tr-02__q" style="--tr-02-i:1">
            <blockquote>“The only vendor our security team approved without a call.”</blockquote>
            <figcaption><b>Ayesha Nkomo</b> · CISO, Brightline <span class="tr-02__ver"><svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.4" fill="currentColor"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="oklch(0.16 0.02 260)" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified customer</span></figcaption>
          </figure>
          <figure class="tr-02__q" style="--tr-02-i:2">
            <blockquote>“Onboarded 40 engineers in a day with no training budget.”</blockquote>
            <figcaption><b>Ruth Kelleher</b> · VP Product, Camber <span class="tr-02__ver"><svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.4" fill="currentColor"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="oklch(0.16 0.02 260)" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified customer</span></figcaption>
          </figure>
        </div>
      </div>
    </div>

    <p class="tr-02__chip" aria-hidden="true">flex band · negative-margin avatar stack · ring via box-shadow · CSS-only quote rotator</p>
  </div>
</section>
```
## CSS
```css
.tr-02,
.tr-02 *,
.tr-02 *::before,
.tr-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-02-bg: oklch(0.18 0.028 264);
  --tr-02-band: oklch(0.23 0.03 264);
  --tr-02-ink: oklch(0.97 0.006 260);
  --tr-02-mut: oklch(0.72 0.02 264);
  --tr-02-acc: oklch(0.83 0.16 152);
  --tr-02-star: oklch(0.84 0.15 88);
  background: var(--tr-02-bg);
  color: var(--tr-02-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(26px,4vw,44px);
  padding: clamp(22px,5vw,60px);
  background: radial-gradient(80% 55% at 50% 0%,color-mix(in oklch,var(--tr-02-acc) 14%,transparent),transparent 62%);
}

.tr-02__hero {
  text-align: center;
  display: grid;
  gap: 12px;
}

.tr-02__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tr-02-acc);
}

.tr-02__h {
  font-size: clamp(30px,5.6vw,58px);
  font-weight: 680;
  line-height: 1.05;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.tr-02__band {
  width: min(100%,1120px);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: clamp(14px,2.4vw,28px);
  padding: 16px clamp(16px,2.4vw,26px);
  border-radius: 20px;
  background: color-mix(in oklch,var(--tr-02-band) 88%,transparent);
  border: 1px solid oklch(1 0 0/.1);
  box-shadow: 0 24px 60px -30px oklch(0 0 0/.9),inset 0 1px 0 oklch(1 0 0/.06);
  backdrop-filter: blur(14px);
  animation: tr-02-up .8s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-02-up {
  from {
    opacity: 0;
    translate: 0 18px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-02__seg {
  display: flex;
  align-items: center;
  gap: 12px;
  position: relative;
  min-height: 44px;
}

.tr-02__seg+.tr-02__seg::before {
  content: '';
  position: absolute;
  inset-inline-start: calc(-1*clamp(7px,1.2vw,14px));
  inline-size: 1px;
  block-size: 34px;
  background: oklch(1 0 0/.14);
}

.tr-02__stack {
  display: flex;
  align-items: center;
}

.tr-02__stack>*+* {
  margin-inline-start: -12px;
}

.tr-02__stack img {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 0 0 3px var(--tr-02-band);
  background: linear-gradient(135deg,oklch(0.6 0.1 264),oklch(0.5 0.12 300));
}

.tr-02__more {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--tr-02-acc) 88%,black);
  color: oklch(0.2 0.03 160);
  font-size: 11px;
  font-weight: 750;
  box-shadow: 0 0 0 3px var(--tr-02-band);
}

.tr-02__label {
  font-size: 13px;
  line-height: 1.35;
  color: var(--tr-02-mut);
}

.tr-02__label b {
  color: var(--tr-02-ink);
  font-weight: 650;
  font-variant-numeric: tabular-nums;
}

.tr-02__rating {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tr-02__stars {
  display: flex;
  gap: 2px;
  color: var(--tr-02-star);
}

.tr-02__stars svg {
  width: 16px;
  height: 16px;
  fill: var(--tr-02-star);
}

.tr-02__half {
  fill: none;
}

.tr-02__score {
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.tr-02__seg--pills {
  flex-wrap: wrap;
  gap: 8px;
}

.tr-02__pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 12px;
  border-radius: 10px;
  background: oklch(1 0 0/.06);
  border: 1px solid oklch(1 0 0/.1);
  font-size: 12.5px;
  color: var(--tr-02-mut);
  font-variant-numeric: tabular-nums;
}

.tr-02__pill b {
  color: var(--tr-02-ink);
  font-weight: 680;
}

.tr-02__pill svg {
  width: 15px;
  height: 15px;
  color: var(--tr-02-acc);
}

.tr-02__seg--quote {
  flex: 1 1 300px;
  min-width: 260px;
}

.tr-02__rotator {
  display: grid;
  width: 100%;
}

.tr-02__q {
  grid-area: 1/1;
  opacity: 0;
  animation: tr-02-rot 13.5s cubic-bezier(.16,1,.3,1) infinite;
  animation-delay: calc(var(--tr-02-i)*4.5s);
}

@keyframes tr-02-rot {
  0% {
    opacity: 0;
    translate: 0 8px;
  }

  4%,
    30% {
    opacity: 1;
    translate: 0 0;
  }

  34%,
    100% {
    opacity: 0;
    translate: 0 -8px;
  }
}

.tr-02__q blockquote {
  font-size: 14.5px;
  line-height: 1.45;
  letter-spacing: -.012em;
  text-wrap: pretty;
}

.tr-02__q figcaption {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-top: 7px;
  font-size: 12px;
  color: var(--tr-02-mut);
}

.tr-02__q figcaption b {
  color: var(--tr-02-ink);
  font-weight: 620;
}

.tr-02__ver {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 9px 3px 5px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--tr-02-acc) 16%,transparent);
  color: color-mix(in oklch,var(--tr-02-acc) 80%,white);
  font-size: 11px;
  font-weight: 640;
}

.tr-02__ver svg {
  width: 14px;
  height: 14px;
  color: var(--tr-02-acc);
}

.tr-02__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-02-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
}

@media (max-width: 760px) {
  .tr-02__seg+.tr-02__seg::before {
    display: none;
  }

  .tr-02__band {
    gap: 16px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tr-02__band {
    animation: none;
  }

  .tr-02__q {
    animation: none;
    opacity: 0;
  }

  .tr-02__q:first-child {
    opacity: 1;
  }
}
```
