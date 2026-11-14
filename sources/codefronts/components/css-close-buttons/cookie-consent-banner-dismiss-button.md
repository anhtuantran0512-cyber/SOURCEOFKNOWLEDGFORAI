---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/cookie-consent-banner-dismiss-button/"
title: "Cookie Consent Banner Dismiss Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A GDPR-honest dismiss: the banner's decline action is a pill combining the word \"Dismiss\" with a small ×, given exactly equal visual weight to Accept — no…"
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cookie Consent Banner Dismiss Button
Source: https://codefronts.com/components/css-close-buttons/cookie-consent-banner-dismiss-button/

A GDPR-honest dismiss: the banner's decline action is a pill combining the word "Dismiss" with a small ×, given exactly equal visual weight to Accept — no dark patterns, no ghost-grey decline. Flexbox pairs text and icon with one gap; hover lifts the pill with a soft shadow; clicking slides the banner away with a transform.
## HTML
```html
<section class="ccb-05" aria-label="Cookie banner dismiss button demo">
  <div class="ccb-05__banner" id="ccb-05-banner" role="region" aria-label="Cookie consent">
    <p class="ccb-05__text">We use cookies to improve your experience and analyse traffic.</p>
    <div class="ccb-05__actions">
      <button class="ccb-05__btn ccb-05__btn--accept" type="button">Accept all</button>
      <button class="ccb-05__btn ccb-05__btn--dismiss" id="ccb-05-dismiss" type="button">
        Dismiss
        <span class="ccb-05__x" aria-hidden="true"></span>
      </button>
    </div>
  </div>
  <button class="ccb-05__reset" id="ccb-05-reset" type="button" hidden>Show banner again</button>
</section>
```
## CSS
```css
.ccb-05,
.ccb-05 *,
.ccb-05 *::before,
.ccb-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-05 {
  --surface: oklch(0.23 0.02 270);
  --ink: oklch(0.93 0.01 270);
  --accent: oklch(0.75 0.14 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.96 0.008 200),oklch(0.92 0.015 210));
}

.ccb-05 .ccb-05__banner {
  width: min(520px,100%);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px 24px;
  background: var(--surface);
  color: var(--ink);
  border-radius: 18px;
  padding: 20px 24px;
  box-shadow: 0 24px 54px -26px oklch(0.3 0.04 270 / .7);
  transition: transform .35s ease,opacity .35s ease;
}

.ccb-05 .ccb-05__banner.is-dismissed {
  transform: translateY(120%);
  opacity: 0;
}

.ccb-05 .ccb-05__text {
  flex: 1 1 220px;
  font-size: 13.5px;
  line-height: 1.55;
  color: color-mix(in oklab,var(--ink) 85%,transparent);
}

.ccb-05 .ccb-05__actions {
  display: flex;
  gap: 10px;
}

.ccb-05 .ccb-05__btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font: 600 13.5px/1 'Segoe UI',system-ui,sans-serif;
  padding: 12px 18px;
  border-radius: 999px;
  cursor: pointer;
  transition: transform .15s ease,box-shadow .15s ease;
}

.ccb-05 .ccb-05__btn--accept {
  border: 1.5px solid var(--accent);
  background: var(--accent);
  color: oklch(0.2 0.03 160);
}

.ccb-05 .ccb-05__btn--dismiss {
  border: 1.5px solid color-mix(in oklab,var(--ink) 45%,transparent);
  background: transparent;
  color: var(--ink);
}

.ccb-05 .ccb-05__btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 18px -8px rgba(0,0,0,.5);
}

.ccb-05 .ccb-05__btn:active {
  transform: translateY(0) scale(.97);
}

.ccb-05 .ccb-05__btn:focus-visible {
  outline: 2.5px solid var(--accent);
  outline-offset: 2px;
}

.ccb-05 .ccb-05__x {
  position: relative;
  width: 10px;
  height: 10px;
}

.ccb-05 .ccb-05__x::before,
.ccb-05 .ccb-05__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 12px;
  height: 1.8px;
  border-radius: 2px;
  background: currentColor;
}

.ccb-05 .ccb-05__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-05 .ccb-05__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-05 .ccb-05__reset {
  font: 500 12px/1 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.45 0.05 210);
  background: none;
  border: none;
  border-bottom: 1px dashed currentColor;
  cursor: pointer;
  padding: 2px 0;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-05 .ccb-05__banner,
    .ccb-05 .ccb-05__btn {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const banner = document.getElementById('ccb-05-banner'); if (!banner) return;
  const dismiss = document.getElementById('ccb-05-dismiss');
  const reset = document.getElementById('ccb-05-reset');
  dismiss.addEventListener('click', () => {
    banner.classList.add('is-dismissed');
    // TODO in production: localStorage.setItem('consent', 'dismissed')
    setTimeout(() => { banner.style.visibility = 'hidden'; reset.hidden = false; reset.focus(); }, 350);
  });
  reset.addEventListener('click', () => {
    banner.style.visibility = ''; banner.classList.remove('is-dismissed'); reset.hidden = true;
  });
})();
```
