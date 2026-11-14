---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-top-header-with-flexbox-layout-logo-links-cta/"
title: "Sticky Top Header with Flexbox Layout (Logo · Links · CTA)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The three-zone product header — brand locked left, navigation held in the true optical centre, action button pinned right — that stays balanced when the link…"
has_js: "false"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Top Header with Flexbox Layout (Logo · Links · CTA)
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-top-header-with-flexbox-layout-logo-links-cta/

The three-zone product header — brand locked left, navigation held in the true optical centre, action button pinned right — that stays balanced when the link set grows or a locale doubles the label lengths. Built on auto margins rather than space-between, which is why the centre group does not drift every time the CTA text changes.
## HTML
```html
<section class="sn-02" aria-label="Flexbox sticky header demo">
    <header class="sn-02__bar">
      <div class="sn-02__zone sn-02__zone--start">
        <a class="sn-02__brand" href="#sn-02-s1"><span class="sn-02__logo" aria-hidden="true">◈</span>Halcyon Labs</a>
      </div>
      <nav class="sn-02__nav" aria-label="Primary">
        <a class="sn-02__link" href="#sn-02-s1" aria-current="page">Platform</a>
        <a class="sn-02__link" href="#sn-02-s2">Solutions</a>
        <a class="sn-02__link" href="#sn-02-s3">Developers</a>
        <a class="sn-02__link" href="#sn-02-s4">Company</a>
      </nav>
      <div class="sn-02__zone sn-02__zone--end">
        <a class="sn-02__ghost" href="#sn-02-s3">Sign in</a>
        <a class="sn-02__cta" href="#sn-02-s4">Book a demo</a>
      </div>
    </header>
  <div class="sn-02__intro">
    <div class="sn-02__introin">
    <p class="sn-02__intro-eyebrow">flex · gap · margin-inline: auto</p>
    <h2 class="sn-02__intro-title">Logo left · links centre · CTA right</h2>
    </div>
  </div>
    <main>
      <section class="sn-02__sec" id="sn-02-s1">
        <p class="sn-02__kicker">Platform</p>
        <h3 class="sn-02__h">Equal side zones, true centre</h3>
        <p class="sn-02__p">Both outer zones carry <code>flex:1 1 0</code>, so they always claim the same share of free space. The nav lands on the optical centre line whatever the button says.</p>
      </section>
      <section class="sn-02__sec" id="sn-02-s2">
        <p class="sn-02__kicker">Solutions</p>
        <h3 class="sn-02__h">Why not space-between</h3>
        <p class="sn-02__p">Space-between positions the middle group as a side effect of its neighbours' widths. Translate the CTA into German and the nav visibly drifts.</p>
      </section>
      <section class="sn-02__sec" id="sn-02-s3">
        <p class="sn-02__kicker">Developers</p>
        <h3 class="sn-02__h">min-width: 0 stops the overflow</h3>
        <p class="sn-02__p">A flex item refuses to shrink below its content by default. That single rule is behind most mystery horizontal scrollbars in headers.</p>
      </section>
      <section class="sn-02__sec" id="sn-02-s4">
        <p class="sn-02__kicker">Company</p>
        <h3 class="sn-02__h">Gap, not margins</h3>
        <p class="sn-02__p">Spacing that lives between items survives reordering, RTL mirroring and CMS-driven link lists with no trailing whitespace to clean up.</p>
      </section>
    </main>
  <footer class="sn-02__pagefoot">
    <p class="sn-02__pagefootin">Sticky navigation pattern 02 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-02-bg);
  --sn-02-bg: oklch(0.19 0.024 260);
  --sn-02-surface: oklch(0.235 0.028 262);
  --sn-02-ink: oklch(0.97 0.006 260);
  --sn-02-mut: oklch(0.73 0.018 260);
  --sn-02-acc: oklch(0.83 0.16 172);
  --sn-02-line: oklch(1 0 0/.1);
  --sn-02-h: 66px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-02-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-02 *,
.sn-02 *::before,
.sn-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-02__eyebrow,
.sn-02__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sn-02-acc);
}

.sn-02__title,
.sn-02__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-02__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,24px);
  min-height: var(--sn-02-h);
  padding: 0 clamp(14px,2.4vw,24px);
  background: color-mix(in oklch,var(--sn-02-surface) 82%,transparent);
  backdrop-filter: blur(16px) saturate(1.4);
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
  border-bottom: 1px solid var(--sn-02-line);
}

.sn-02__zone {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1 1 0;
  min-width: 0;
}

.sn-02__zone--end {
  justify-content: flex-end;
}

.sn-02__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  min-width: 0;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sn-02__logo {
  flex: none;
  display: grid;
  place-items: center;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  font-size: 13px;
  color: oklch(0.19 0.024 260);
  background: var(--sn-02-acc);
}

.sn-02__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  flex: none;
}

.sn-02__link {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-02-mut);
  text-decoration: none;
  white-space: nowrap;
  transition: color .18s ease,background .18s ease;
}

.sn-02__link:hover {
  color: var(--sn-02-ink);
  background: oklch(1 0 0/.06);
}

.sn-02__link[aria-current="page"] {
  color: var(--sn-02-acc);
  background: color-mix(in oklch,var(--sn-02-acc) 14%,transparent);
}

.sn-02__ghost {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.4px;
  font-weight: 600;
  color: var(--sn-02-mut);
  text-decoration: none;
  white-space: nowrap;
  transition: color .18s ease;
}

.sn-02__ghost:hover {
  color: var(--sn-02-ink);
}

.sn-02__cta {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 16px;
  border-radius: 9px;
  font-size: 13.4px;
  font-weight: 670;
  color: oklch(0.19 0.024 260);
  background: var(--sn-02-acc);
  text-decoration: none;
  white-space: nowrap;
  box-shadow: 0 6px 18px -8px var(--sn-02-acc);
  transition: transform .18s ease,filter .18s ease;
}

.sn-02__cta:hover {
  transform: translateY(-1px);
  filter: brightness(1.06);
}

.sn-02__link:focus-visible,
.sn-02__ghost:focus-visible,
.sn-02__cta:focus-visible,
.sn-02__brand:focus-visible {
  outline: 2px solid var(--sn-02-acc);
  outline-offset: 2px;
}

.sn-02__sec {
  scroll-margin-top: var(--sn-02-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 70svh;
  padding: clamp(24px,4vw,46px);
  border-bottom: 1px solid var(--sn-02-line);
}

.sn-02__sec:nth-child(even) {
  background: oklch(1 0 0/.025);
}

.sn-02__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-02-acc);
}

.sn-02__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-02__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-02-mut);
  text-wrap: pretty;
}

.sn-02__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 780px) {
  .sn-02__nav {
    display: none;
  }

  .sn-02__zone {
    flex: 0 1 auto;
  }

  .sn-02__zone--end {
    margin-inline-start: auto;
  }
}

@media (max-width: 480px) {
  .sn-02__ghost {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-02 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-02) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-02-h) + 10px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-02) {
    scroll-behavior: auto;
  }
}

.sn-02__bar,
.sn-02__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-02__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-02__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(85% 55% at 50% 0%,oklch(0.3 0.06 190/.5),transparent);
}

.sn-02__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-02__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-02__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-02__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-02__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-02-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-02-mut);
  animation: sn-02-cue 2.6s ease-in-out infinite;
}

@keyframes sn-02-cue {
  0%,
    100% {
    transform: translateY(0);
    opacity: .75;
  }

  50% {
    transform: translateY(5px);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-02__intro::after {
    animation: none;
  }
}

.sn-02__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-02-line);
}

.sn-02__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-02-mut);
  text-align: center;
}

.sn-02__intro-title,
.sn-02__intro-sub {
  text-wrap: balance;
}
```
