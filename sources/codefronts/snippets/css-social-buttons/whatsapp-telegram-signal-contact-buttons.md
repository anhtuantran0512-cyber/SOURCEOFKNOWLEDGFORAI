---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/whatsapp-telegram-signal-contact-buttons/"
title: "WhatsApp Telegram Signal Contact Buttons"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "A static support card of direct-message buttons: WhatsApp, Telegram and Signal, each in its own brand colour with a prefilled deep link."
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: WhatsApp Telegram Signal Contact Buttons
Source: https://codefronts.com/snippets/css-social-buttons/whatsapp-telegram-signal-contact-buttons/

A static support card of direct-message buttons: WhatsApp, Telegram and Signal, each in its own brand colour with a prefilled deep link. It sits in the page as a contact block — not a corner-pinned floating bubble — so it works inside a help section, a footer column or a product support tab, with a realistic reply-time line above it.
## HTML
```html
<div class="soc-15">
  <div class="soc-15__stage">
    <section class="soc-15__card" aria-labelledby="soc-15-h">
      <p class="soc-15__eyebrow"><span class="soc-15__dot" aria-hidden="true"></span>Support online</p>
      <h2 class="soc-15__title" id="soc-15-h">Message the Northline team</h2>
      <p class="soc-15__meta">Mon–Fri, 9am–6pm AEST · typically replies in minutes</p>
      <div class="soc-15__set">
        <a class="soc-15__btn" style="--brand:#1fa855;--on-brand:#ffffff" href="https://wa.me/15551234567?text=Hi%20Northline%2C%20I%20have%20a%20question%20about%20my%20order" target="_blank" rel="noopener">
          <span class="soc-15__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 11.6a8.4 8.4 0 0 1-12.4 7.3L3.5 20.4l1.6-4.5A8.4 8.4 0 1 1 20.5 11.6Z"/><path d="M9.2 9.4c.6 2.4 2.6 4.3 5 4.9"/></svg></span>
          <span class="soc-15__label">Chat on WhatsApp<small>Order help · fastest reply</small></span>
          <svg class="soc-15__arrow" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13"/><path d="m12.5 6 6 6-6 6"/></svg>
        </a>
        <a class="soc-15__btn" style="--brand:#2196d1;--on-brand:#ffffff" href="https://t.me/northlinesupport" target="_blank" rel="noopener">
          <span class="soc-15__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 4 3.4 10.6l6.2 2.3L12 20l3-5.4"/><path d="m9.6 12.9 5.6-5.3"/></svg></span>
          <span class="soc-15__label">Message on Telegram<small>@northlinesupport</small></span>
          <svg class="soc-15__arrow" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13"/><path d="m12.5 6 6 6-6 6"/></svg>
        </a>
        <a class="soc-15__btn" style="--brand:#3a6df0;--on-brand:#ffffff" href="https://signal.me/#p/+15551234567" target="_blank" rel="noopener">
          <span class="soc-15__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.6a8.4 8.4 0 0 1 6.6 13.6l.9 3.2-3.4-.9A8.4 8.4 0 1 1 12 3.6Z"/><path d="M9.4 12h5.2"/></svg></span>
          <span class="soc-15__label">Talk on Signal<small>End-to-end encrypted</small></span>
          <svg class="soc-15__arrow" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13"/><path d="m12.5 6 6 6-6 6"/></svg>
        </a>
      </div>
      <p class="soc-15__foot">Prefer email? <a class="soc-15__link" href="mailto:[email protected]">[email protected]</a></p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-15 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --live: #1fa855;
  --row: 3.5rem;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-15 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
    --live: oklch(62% .16 152);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-15:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
  }
}

.soc-15[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
}

.soc-15,
.soc-15 *,
.soc-15 *::before,
.soc-15 *::after {
  box-sizing: border-box;
}

.soc-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-15__card {
  inline-size: min(29rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.35rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 22px 48px -30px rgb(9 9 20/.45);
}

.soc-15__eyebrow {
  display: flex;
  align-items: center;
  gap: .45rem;
  margin: 0 0 .6rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-15__dot {
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 50%;
  background: var(--live);
  box-shadow: 0 0 0 .2rem color-mix(in oklab,var(--live) 22%,transparent);
}

.soc-15__title {
  margin: 0 0 .35rem;
  font-size: clamp(1.1rem,1rem + .9vw,1.4rem);
  font-weight: 600;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.soc-15__meta {
  margin: 0 0 1.5rem;
  font-size: .82rem;
  color: var(--muted);
}

.soc-15__set {
  display: grid;
  gap: .6rem;
}

.soc-15__btn {
  display: grid;
  grid-template-columns: 2.4rem 1fr 1.2rem;
  align-items: center;
  gap: .8rem;
  min-block-size: var(--row);
  padding: .5rem .85rem;
  min-inline-size: 0;
  border: 1px solid var(--brand);
  border-radius: 1rem;
  background: var(--brand);
  color: var(--on-brand);
  text-decoration: none;
  box-shadow: 0 12px 26px -20px color-mix(in oklab,var(--brand) 90%,transparent);
  transition: translate .2s cubic-bezier(.16,1,.3,1), filter .2s ease, box-shadow .2s ease;
}

.soc-15__tile {
  display: grid;
  place-items: center;
  inline-size: 2.4rem;
  block-size: 2.4rem;
  border-radius: .7rem;
  background: color-mix(in oklab,#ffffff 22%,transparent);
}

.soc-15__tile svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
}

.soc-15__label {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.01em;
  overflow-wrap: anywhere;
}

.soc-15__label small {
  font-size: .75rem;
  font-weight: 400;
  opacity: .85;
}

.soc-15__arrow {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  opacity: .85;
  transition: translate .2s cubic-bezier(.16,1,.3,1);
}

.soc-15__btn:hover {
  translate: 0 -2px;
  filter: brightness(1.04);
  box-shadow: 0 18px 34px -20px color-mix(in oklab,var(--brand) 90%,transparent);
}

.soc-15__btn:hover .soc-15__arrow {
  translate: .22rem 0;
}

.soc-15__btn:focus-visible {
  outline: 2px solid var(--fg);
  outline-offset: 3px;
}

.soc-15__btn:focus-visible .soc-15__arrow {
  translate: .22rem 0;
}

.soc-15__foot {
  margin: 1.4rem 0 0;
  font-size: .82rem;
  color: var(--muted);
}

.soc-15__link {
  color: var(--fg);
  text-decoration-thickness: 1px;
  text-underline-offset: .2em;
}

.soc-15__link:hover {
  color: var(--ring);
}

@media (prefers-reduced-motion: reduce) {
  .soc-15__btn,
    .soc-15__arrow {
    transition-duration: 1ms;
  }

  .soc-15__btn:hover {
    translate: none;
  }

  .soc-15__btn:hover .soc-15__arrow {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-15__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .soc-15__tile {
    border: 1px solid ButtonText;
  }
}
```
