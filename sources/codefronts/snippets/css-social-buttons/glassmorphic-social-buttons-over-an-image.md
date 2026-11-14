---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/glassmorphic-social-buttons-over-an-image/"
title: "Glassmorphic Social Buttons over an Image"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "Frosted social buttons floating over a photograph: backdrop-filter blur with a saturation boost, a hairline inner highlight along the top edge, and a…"
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphic Social Buttons over an Image
Source: https://codefronts.com/snippets/css-social-buttons/glassmorphic-social-buttons-over-an-image/

Frosted social buttons floating over a photograph: backdrop-filter blur with a saturation boost, a hairline inner highlight along the top edge, and a translucent border that reads as glass thickness. A @supports block declares a solid fallback first, so browsers without backdrop-filter get an opaque button instead of an unreadable one.
## HTML
```html
<div class="soc-17">
  <div class="soc-17__stage">
    <img class="soc-17__bg" src="https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=1600&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="1600" height="1000" loading="lazy" decoding="async">
    <div class="soc-17__scrim" aria-hidden="true"></div>
    <div class="soc-17__glass">
      <p class="soc-17__eyebrow">Photograph series</p>
      <h2 class="soc-17__title">Golden hour, Fitzroy Gardens</h2>
      <p class="soc-17__meta">Print available · Sam Rivera</p>
      <div class="soc-17__row">
        <a class="soc-17__btn" style="--brand:#e1306c" href="https://example.com/samrivera" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><circle cx="12" cy="12" r="3.9"/><circle cx="17.1" cy="6.9" r="1.15" fill="currentColor" stroke="none"/></svg>
          <span>Instagram</span>
        </a>
        <a class="soc-17__btn" style="--brand:#0f1419" href="https://example.com/samrivera" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg>
          <span>Post</span>
        </a>
        <a class="soc-17__btn soc-17__btn--icon" href="https://example.com/share" target="_blank" rel="noopener" aria-label="Share this photograph">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="17.5" cy="5.5" r="2.6"/><circle cx="6.5" cy="12" r="2.6"/><circle cx="17.5" cy="18.5" r="2.6"/><path d="m8.9 10.7 6.2-3.6"/><path d="m8.9 13.3 6.2 3.6"/></svg>
        </a>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-17 {
  --fg: #ffffff;
  --muted: rgb(255 255 255 / .78);
  --plate: rgb(255 255 255 / .12);
  --edge: rgb(255 255 255 / .24);
  --ring: #ffffff;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: #0c1013;
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.soc-17[data-theme="light"] {
  --plate: rgb(255 255 255 / .3);
  --edge: rgb(255 255 255 / .5);
}

.soc-17,
.soc-17 *,
.soc-17 *::before,
.soc-17 *::after {
  box-sizing: border-box;
}

.soc-17__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
  overflow: hidden;
}

.soc-17__bg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  background: #1a2228;
}

.soc-17__scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(160deg,rgb(6 10 14 / .35),rgb(6 10 14 / .68));
}

.soc-17__glass {
  position: relative;
  inline-size: min(30rem,100%);
  padding: clamp(1.5rem,4vw,2.25rem);
  border-radius: 1.5rem;
  border: 1px solid var(--edge);
  background: var(--plate);
  box-shadow: inset 0 1px 0 rgb(255 255 255 / .35), 0 30px 60px -30px rgb(0 0 0 / .8);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  backdrop-filter: blur(20px) saturate(170%);
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .soc-17__glass {
    background: rgb(14 18 22 / .88);
  }

  .soc-17__btn {
    background: rgb(255 255 255 / .16);
  }
}

.soc-17__eyebrow {
  margin: 0 0 .5rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-17__title {
  margin: 0 0 .3rem;
  font-size: clamp(1.2rem,1rem + 1.1vw,1.6rem);
  font-weight: 600;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.soc-17__meta {
  margin: 0 0 1.6rem;
  font-size: .85rem;
  color: var(--muted);
}

.soc-17__row {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.soc-17__btn {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.875rem;
  padding: 0 1.1rem;
  border-radius: .9rem;
  border: 1px solid var(--edge);
  background: rgb(255 255 255 / .1);
  color: var(--fg);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 550;
  min-inline-size: 0;
  box-shadow: inset 0 1px 0 rgb(255 255 255 / .3);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
  transition: background-color .22s ease, translate .22s cubic-bezier(.16,1,.3,1), border-color .22s ease;
}

.soc-17__btn--icon {
  padding: 0;
  inline-size: 2.875rem;
  justify-content: center;
}

.soc-17__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.soc-17__btn:hover {
  background: rgb(255 255 255 / .2);
  translate: 0 -2px;
  border-color: rgb(255 255 255 / .42);
}

.soc-17__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .soc-17__btn {
    transition-duration: 1ms;
  }

  .soc-17__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-17__glass,
    .soc-17__btn {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }

  .soc-17__scrim {
    display: none;
  }
}
```
