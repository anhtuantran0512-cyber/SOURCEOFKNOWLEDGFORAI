---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/cookie-consent-banner-slide-in/"
title: "Cookie Consent Banner Slide-In"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A GDPR/CCPA-compliant cookie consent banner that slides up from the bottom edge showing plain-language consent copy, three action buttons (Accept all /…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cookie Consent Banner Slide-In
Source: https://codefronts.com/motion/css-slide-in-animation/cookie-consent-banner-slide-in/

A GDPR/CCPA-compliant cookie consent banner that slides up from the bottom edge showing plain-language consent copy, three action buttons (Accept all / Reject all / Customize), and a Privacy Policy link — the pattern required for EU/CA compliance and used by every major website since 2018.
## HTML
```html
<div class="sl-17">
  <div class="sl-17__banner" role="region" aria-label="Cookie consent">
    <div class="sl-17__body">
      <p class="sl-17__title">We value your privacy</p>
      <p class="sl-17__copy">We use cookies to enhance your browsing experience, analyze site traffic, and improve our services. You can accept all cookies, reject non-essential ones, or customize your preferences. Read our <a href="#">Privacy Policy</a> and <a href="#">Cookie Policy</a> for details.</p>
    </div>
    <div class="sl-17__actions">
      <button class="sl-17__btn sl-17__btn--ghost">Customize</button>
      <button class="sl-17__btn sl-17__btn--secondary">Reject all</button>
      <button class="sl-17__btn sl-17__btn--primary">Accept all</button>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-17 {
  --bg: #f5f5f7;
  --banner: #0a0a14;
  --accent: #8b5cf6;
  --text: #f4f4f5;
  --sub: #a1a1aa;
  --line: rgba(255,255,255,.1);
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  padding: 32px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  background: var(--bg);
  color: #333;
  overflow: hidden;
}

.sl-17 *,
.sl-17 *::before,
.sl-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-17 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-17__banner {
  display: flex;
  align-items: center;
  gap: 20px;
  width: min(920px,100%);
  padding: 20px 24px;
  border-radius: 14px;
  background: var(--banner);
  color: var(--text);
  border: 1px solid var(--line);
  box-shadow: 0 30px 60px -20px rgba(0,0,0,.5);
  opacity: 0;
  transform: translateY(100%);
  animation: sl-17-in .5s cubic-bezier(.16,1,.3,1) .4s forwards;
}

.sl-17__body {
  flex: 1;
  min-width: 0;
}

.sl-17__title {
  font-size: .95rem;
  font-weight: 700;
  letter-spacing: -.01em;
  color: var(--text);
  margin-bottom: 4px;
}

.sl-17__copy {
  font-size: .82rem;
  color: var(--sub);
  line-height: 1.5;
}

.sl-17__copy a {
  color: var(--text);
  text-decoration: underline;
}

.sl-17__copy a:hover {
  color: var(--accent);
}

.sl-17__actions {
  display: flex;
  gap: 8px;
  flex-shrink: 0;
}

.sl-17__btn {
  padding: 10px 18px;
  border: none;
  border-radius: 8px;
  font-family: inherit;
  font-size: .82rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: background .18s ease,transform .12s ease;
}

.sl-17__btn:active {
  transform: translateY(1px);
}

.sl-17__btn--ghost {
  background: transparent;
  color: var(--sub);
  border: 1px solid transparent;
}

.sl-17__btn--ghost:hover {
  color: var(--text);
}

.sl-17__btn--secondary {
  background: rgba(255,255,255,.08);
  color: var(--text);
  border: 1px solid rgba(255,255,255,.14);
}

.sl-17__btn--secondary:hover {
  background: rgba(255,255,255,.14);
}

.sl-17__btn--primary {
  background: var(--text);
  color: var(--banner);
  border: 1px solid var(--text);
}

.sl-17__btn--primary:hover {
  background: #fff;
  color: #0a0a14;
}

@keyframes sl-17-in {
  from {
    opacity: 0;
    transform: translateY(100%);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-17__banner {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 720px) {
  .sl-17__banner {
    flex-direction: column;
    align-items: stretch;
    text-align: left;
    padding: 16px 18px;
  }

  .sl-17__actions {
    justify-content: flex-end;
    flex-wrap: wrap;
  }

  .sl-17__btn {
    flex: 1;
    min-width: 0;
  }
}
```
