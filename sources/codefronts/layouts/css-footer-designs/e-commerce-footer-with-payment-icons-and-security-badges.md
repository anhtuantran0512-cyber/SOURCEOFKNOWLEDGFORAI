---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/e-commerce-footer-with-payment-icons-and-security-badges/"
title: "E-Commerce Footer with Payment Icons & Security Badges"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The footer that closes the sale: accepted-payment marks, an SSL/secure-checkout statement, returns and shipping promises, all built from inline SVG that…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Footer with Payment Icons & Security Badges
Source: https://codefronts.com/layouts/css-footer-designs/e-commerce-footer-with-payment-icons-and-security-badges/

The footer that closes the sale: accepted-payment marks, an SSL/secure-checkout statement, returns and shipping promises, all built from inline SVG that inherits currentColor so the whole rail re-themes with one token. No image sprites, no 12 network requests for card logos, no blurry PNGs on a retina display.
## HTML
```html
<section class="ft-05" aria-label="E-commerce footer with payment icons demo">
  <main class="ft-05__main">
    <p class="ft-05__eyebrow">Trust rail · payment marks · SSL</p>
    <h1 class="ft-05__title">The last 200 pixels before checkout</h1>
    <p class="ft-05__sub">Shoppers scroll to the footer to answer three questions: can I pay how I want, can I send it back, and is this site safe. Answer all three, above the copyright line.</p>
  </main>
  <footer class="ft-05__foot">
    <div class="ft-05__inner">
      <ul class="ft-05__promises">
        <li class="ft-05__promise">
          <span class="ft-05__pico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M3 7h13v10H3z"/><path d="M16 10h3.5L22 13v4h-6"/><circle cx="7" cy="18" r="1.8"/><circle cx="18" cy="18" r="1.8"/></svg></span>
          <span class="ft-05__ptitle">Free delivery over £40</span>
          <span class="ft-05__pdesc">DPD next-day, ordered before 6pm</span>
        </li>
        <li class="ft-05__promise">
          <span class="ft-05__pico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg></span>
          <span class="ft-05__ptitle">30-day free returns</span>
          <span class="ft-05__pdesc">Prepaid label in every box</span>
        </li>
        <li class="ft-05__promise">
          <span class="ft-05__pico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg></span>
          <span class="ft-05__ptitle">Secure checkout</span>
          <span class="ft-05__pdesc">TLS 1.3 · PCI DSS Level 1</span>
        </li>
        <li class="ft-05__promise">
          <span class="ft-05__pico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M12 3l7 3v6c0 4.4-3 7.6-7 9-4-1.4-7-4.6-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg></span>
          <span class="ft-05__ptitle">2-year guarantee</span>
          <span class="ft-05__pdesc">Repair, replace or refund</span>
        </li>
      </ul>
      <div class="ft-05__cols">
        <div class="ft-05__brandcol">
          <div class="ft-05__brand"><span class="ft-05__mark" aria-hidden="true"></span>Halyard Supply</div>
          <p class="ft-05__blurb">Outdoor equipment, tested on the west coast of Scotland since 2014.</p>
          <div class="ft-05__rating"><span class="ft-05__stars" aria-hidden="true">★★★★★</span><span class="ft-05__rtext">4.8 / 5 from 21,904 verified reviews</span></div>
        </div>
        <nav class="ft-05__col" aria-labelledby="ft-05-c1"><h2 class="ft-05__h" id="ft-05-c1">Shop</h2><ul class="ft-05__list"><li><a class="ft-05__link" href="#ft-05-a">New in</a></li><li><a class="ft-05__link" href="#ft-05-a">Jackets</a></li><li><a class="ft-05__link" href="#ft-05-a">Packs</a></li><li><a class="ft-05__link" href="#ft-05-a">Outlet</a></li></ul></nav>
        <nav class="ft-05__col" aria-labelledby="ft-05-c2"><h2 class="ft-05__h" id="ft-05-c2">Help</h2><ul class="ft-05__list"><li><a class="ft-05__link" href="#ft-05-a">Track my order</a></li><li><a class="ft-05__link" href="#ft-05-a">Start a return</a></li><li><a class="ft-05__link" href="#ft-05-a">Size guide</a></li><li><a class="ft-05__link" href="#ft-05-a">Contact us</a></li></ul></nav>
        <nav class="ft-05__col" aria-labelledby="ft-05-c3"><h2 class="ft-05__h" id="ft-05-c3">About</h2><ul class="ft-05__list"><li><a class="ft-05__link" href="#ft-05-a">Our repairs shop</a></li><li><a class="ft-05__link" href="#ft-05-a">Materials</a></li><li><a class="ft-05__link" href="#ft-05-a">Stores</a></li><li><a class="ft-05__link" href="#ft-05-a">Careers</a></li></ul></nav>
      </div>
      <div class="ft-05__paybar">
        <ul class="ft-05__pay" aria-label="Accepted payment methods">
          <li class="ft-05__card"><svg viewBox="0 0 48 30" width="44" height="28" aria-hidden="true" focusable="false"><rect x="1" y="1" width="46" height="28" rx="5" fill="none" stroke="currentColor" stroke-opacity=".35"/><path class="ft-05__acc" d="M17.4 20.3l2.6-10.6h3.3l-2.6 10.6zM31.6 9.9c-.7-.3-1.7-.5-3-.5-3.3 0-5.6 1.7-5.6 4.1 0 1.8 1.6 2.8 2.9 3.4 1.3.6 1.7 1 1.7 1.5 0 .8-1 1.2-2 1.2-1.3 0-2-.2-3.1-.7l-.4-.2-.5 2.7c.8.3 2.2.6 3.7.6 3.5 0 5.8-1.7 5.8-4.2 0-1.4-.9-2.5-2.8-3.4-1.2-.6-1.9-1-1.9-1.6 0-.5.6-1.1 1.9-1.1 1.1 0 1.9.2 2.5.5l.3.1z" fill="currentColor"/><path class="ft-05__acc2" d="M38.6 9.7h-2.5c-.8 0-1.4.2-1.7 1l-4.8 9.6h3.4l.7-1.9h4.1l.4 1.9h3zm-4 6.3l1.3-3.4.7 3.4zM13.9 9.7l-3.2 7.2-.3-1.7c-.6-2-2.4-4.1-4.4-5.2l2.9 10.3h3.4l5.1-10.6z" fill="currentColor"/></svg><span class="ft-05__sr">Visa</span></li>
          <li class="ft-05__card"><svg viewBox="0 0 48 30" width="44" height="28" aria-hidden="true" focusable="false"><rect x="1" y="1" width="46" height="28" rx="5" fill="none" stroke="currentColor" stroke-opacity=".35"/><circle cx="19" cy="15" r="7.5" fill="currentColor" opacity=".85"/><circle cx="29" cy="15" r="7.5" fill="currentColor" opacity=".45"/></svg><span class="ft-05__sr">Mastercard</span></li>
          <li class="ft-05__card"><svg viewBox="0 0 48 30" width="44" height="28" aria-hidden="true" focusable="false"><rect x="1" y="1" width="46" height="28" rx="5" fill="none" stroke="currentColor" stroke-opacity=".35"/><path d="M13 21l2-12h6.2c3 0 4.6 1.5 4.2 4-.4 2.9-2.6 4.4-5.8 4.4h-2.3L16.6 21z" fill="currentColor" opacity=".85"/><path d="M22 23l2-12h6.2c3 0 4.6 1.5 4.2 4-.4 2.9-2.6 4.4-5.8 4.4h-2.3L25.6 23z" fill="currentColor" opacity=".45"/></svg><span class="ft-05__sr">PayPal</span></li>
          <li class="ft-05__card"><svg viewBox="0 0 48 30" width="44" height="28" aria-hidden="true" focusable="false"><rect x="1" y="1" width="46" height="28" rx="5" fill="none" stroke="currentColor" stroke-opacity=".35"/><path d="M22.7 10.4c.7-.9 1.2-2 1-3.2-1 .05-2.3.7-3 1.6-.7.8-1.3 2-1.1 3.1 1.2.1 2.4-.6 3.1-1.5z" fill="currentColor"/><path d="M25.6 15.9c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.8-1.5-.15-2.8.85-3.5.85-.7 0-1.8-.83-3-.8-1.5.02-2.9.9-3.7 2.25-1.6 2.75-.4 6.8 1.1 9 .75 1.1 1.65 2.3 2.83 2.25 1.13-.05 1.56-.73 2.93-.73 1.36 0 1.75.73 2.95.7 1.22-.02 2-1.1 2.75-2.2.86-1.26 1.22-2.48 1.24-2.55-.03-.02-2.38-.92-2.4-3.62z" fill="currentColor"/><path d="M33 20.8V10h4.2c2.2 0 3.6 1.4 3.6 3.5s-1.4 3.5-3.7 3.5h-2.3v3.8z" fill="currentColor" opacity=".55"/></svg><span class="ft-05__sr">Apple Pay</span></li>
          <li class="ft-05__card"><svg viewBox="0 0 48 30" width="44" height="28" aria-hidden="true" focusable="false"><rect x="1" y="1" width="46" height="28" rx="5" fill="none" stroke="currentColor" stroke-opacity=".35"/><path d="M24 9a6 6 0 1 0 0 12 6 6 0 0 0 0-12zm0 2.2a3.8 3.8 0 1 1 0 7.6 3.8 3.8 0 0 1 0-7.6z" fill="currentColor"/><path d="M30 15h6v2h-6zM12 15h6v2h-6z" fill="currentColor" opacity=".5"/></svg><span class="ft-05__sr">Google Pay</span></li>
          <li class="ft-05__card"><svg viewBox="0 0 48 30" width="44" height="28" aria-hidden="true" focusable="false"><rect x="1" y="1" width="46" height="28" rx="5" fill="none" stroke="currentColor" stroke-opacity=".35"/><path d="M14 20V10h4.5c3.3 0 5.5 1.9 5.5 5s-2.2 5-5.5 5zm3-2.2h1.3c1.8 0 2.9-1 2.9-2.8s-1.1-2.8-2.9-2.8H17z" fill="currentColor"/><circle cx="31" cy="15" r="4.4" fill="currentColor" opacity=".5"/></svg><span class="ft-05__sr">Klarna</span></li>
        </ul>
        <p class="ft-05__secure"><span class="ft-05__lock" aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" focusable="false"><rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg></span>256-bit TLS encryption · verified by <a class="ft-05__slink" href="#ft-05-a">DigiCert</a></p>
      </div>
      <div class="ft-05__bar">
        <p class="ft-05__copy">© <time datetime="2026">2026</time> Halyard Supply Co. · VAT GB 411 8827 05</p>
        <ul class="ft-05__legal"><li><a class="ft-05__slink" href="#ft-05-a">Privacy</a></li><li><a class="ft-05__slink" href="#ft-05-a">Terms</a></li><li><a class="ft-05__slink" href="#ft-05-a">Cookies</a></li><li><a class="ft-05__slink" href="#ft-05-a">Modern slavery statement</a></li></ul>
      </div>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-05-bg);
  --ft-05-bg: oklch(0.97 0.008 105);
  --ft-05-foot: oklch(0.24 0.03 160);
  --ft-05-ink: oklch(0.23 0.03 160);
  --ft-05-mut: oklch(0.55 0.02 160);
  --ft-05-acc: oklch(0.58 0.14 150);
  --ft-05-line: oklch(0.23 0.03 160/.1);
  --ft-05-fink: oklch(0.97 0.008 150);
  --ft-05-fmut: oklch(0.78 0.02 150);
  --ft-05-fline: oklch(0.97 0.008 150/.15);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-05-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-05 *,
.ft-05 *::before,
.ft-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-05 ul {
  list-style: none;
}

.ft-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ft-05__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(40px,8vh,88px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1200px)/2));
}

.ft-05__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-05-acc);
}

.ft-05__title {
  font-size: clamp(29px,5.2vw,56px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-05__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-05-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-05__foot {
  background: var(--ft-05-foot);
  color: var(--ft-05-fink);
}

.ft-05__inner {
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1200px)/2));
}

.ft-05__promises {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(13rem,100%),1fr));
  gap: clamp(14px,2vw,26px);
  padding-block: clamp(24px,3.4vw,34px);
  border-bottom: 1px solid var(--ft-05-fline);
}

.ft-05__promise {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 2px 12px;
  align-items: start;
}

.ft-05__pico {
  grid-row: span 2;
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: color-mix(in oklch,var(--ft-05-acc) 18%,transparent);
  color: var(--ft-05-acc);
}

.ft-05__ptitle {
  font-size: 14.5px;
  font-weight: 660;
  letter-spacing: -.01em;
}

.ft-05__pdesc {
  font-size: 12.8px;
  line-height: 1.45;
  color: var(--ft-05-fmut);
  text-wrap: pretty;
}

.ft-05__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: clamp(26px,3.5vw,40px) clamp(18px,2.4vw,32px);
  padding-block: clamp(30px,4vw,48px);
}

.ft-05__brandcol {
  display: grid;
  align-content: start;
  gap: 12px;
  min-width: 0;
}

.ft-05__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-05__mark {
  width: 24px;
  height: 24px;
  border-radius: 7px;
  background: linear-gradient(150deg,var(--ft-05-acc),oklch(0.75 0.13 120));
}

.ft-05__blurb {
  font-size: 14px;
  line-height: 1.6;
  color: var(--ft-05-fmut);
  max-width: 32ch;
  text-wrap: pretty;
}

.ft-05__rating {
  display: grid;
  gap: 2px;
}

.ft-05__stars {
  font-size: 15px;
  letter-spacing: .14em;
  color: oklch(0.83 0.16 85);
}

.ft-05__rtext {
  font-size: 12.5px;
  color: var(--ft-05-fmut);
}

.ft-05__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-05__h {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-block-end: 8px;
}

.ft-05__list {
  display: grid;
  gap: 1px;
}

.ft-05__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14.2px;
  color: var(--ft-05-fmut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease;
}

.ft-05__link:hover {
  color: var(--ft-05-fink);
  text-decoration: underline;
  text-underline-offset: .25em;
}

.ft-05__link:focus-visible,
.ft-05__slink:focus-visible {
  outline: 2px solid var(--ft-05-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-05__paybar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px 26px;
  padding-block: 20px;
  border-block: 1px solid var(--ft-05-fline);
}

.ft-05__pay {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.ft-05__card {
  position: relative;
  display: grid;
  place-items: center;
  padding: 5px 7px;
  border-radius: 9px;
  background: oklch(0.97 0.008 150/.07);
  color: var(--ft-05-fink);
  transition: background .2s ease,transform .2s ease;
}

.ft-05__card:hover {
  background: oklch(0.97 0.008 150/.14);
  transform: translateY(-2px);
}

.ft-05__secure {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-inline-start: auto;
  font-size: 12.8px;
  color: var(--ft-05-fmut);
}

.ft-05__lock {
  display: grid;
  place-items: center;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--ft-05-acc) 22%,transparent);
  color: var(--ft-05-acc);
}

.ft-05__slink {
  color: var(--ft-05-fink);
  text-decoration: underline;
  text-underline-offset: .25em;
  text-decoration-color: color-mix(in oklch,currentColor 35%,transparent);
}

.ft-05__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
}

.ft-05__copy {
  font-size: 12.8px;
  color: var(--ft-05-fmut);
}

.ft-05__legal {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 16px;
  margin-inline-start: auto;
}

.ft-05__legal a {
  display: flex;
  align-items: center;
  min-height: 36px;
  font-size: 12.8px;
  color: var(--ft-05-fmut);
  text-decoration: none;
}

.ft-05__legal a:hover {
  color: var(--ft-05-fink);
  text-decoration: underline;
  text-underline-offset: .25em;
}

@media (prefers-contrast: more) {
  .ft-05__card,
    .ft-05__pico {
    outline: 2px solid currentColor;
  }

  .ft-05__pdesc,
    .ft-05__copy,
    .ft-05__rtext {
    color: var(--ft-05-fink);
  }
}

@media (max-width: 640px) {
  .ft-05__secure,
    .ft-05__legal {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-05 * {
    transition-duration: .01ms !important;
  }
}
```
