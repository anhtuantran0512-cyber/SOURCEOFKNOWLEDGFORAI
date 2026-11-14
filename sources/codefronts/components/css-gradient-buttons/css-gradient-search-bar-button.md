---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-search-bar-button/"
title: "CSS Gradient Search Bar Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A travel-search bar where a rounded input and a sunset-gradient search button live inside one seamless pill, and :focus-within lights a gradient ring around…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Search Bar Button
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-search-bar-button/

A travel-search bar where a rounded input and a sunset-gradient search button live inside one seamless pill, and :focus-within lights a gradient ring around the entire bar.
## HTML
```html
<div class="gb-15">
  <div class="gb-15__hero">
    <h3 class="gb-15__h">Where to <span>next?</span></h3>
    <p class="gb-15__sub">Search 12,000+ stays, tours and hidden beaches</p>
    <div class="gb-15__bar">
      <input class="gb-15__input" id="gb-15-q" type="text" placeholder="Try &quot;Lisbon in October&quot;" aria-label="Search destinations">
      <button class="gb-15__btn" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path></svg>
        <span>Search</span>
      </button>
    </div>
    <div class="gb-15__chips">
      <button class="gb-15__chip" type="button">Kyoto ryokans</button>
      <button class="gb-15__chip" type="button">Amalfi coast</button>
      <button class="gb-15__chip" type="button">Patagonia treks</button>
    </div>
  </div>
</div>
```
## CSS
```css
.gb-15,
.gb-15 *,
.gb-15 *::before,
.gb-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-15 ::selection {
  background: #f97316;
  color: #fff;
}

.gb-15 {
  --sunset-a: #f97316;
  --sunset-b: #ec4899;
  --sunset-c: #8b5cf6;
  --sand: #fff8f2;
  --ink: #3b2b20;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: linear-gradient(180deg,#fff3e8 0%,#ffe9f2 60%,#f3ecff 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-15__hero {
  width: 100%;
  max-width: 520px;
  text-align: center;
}

.gb-15__h {
  font-size: 30px;
  font-weight: 900;
  letter-spacing: -1px;
  color: var(--ink);
  margin-bottom: 8px;
}

.gb-15__h span {
  background: linear-gradient(100deg,var(--sunset-a),var(--sunset-b),var(--sunset-c));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.gb-15__sub {
  font-size: 15px;
  color: #9a8574;
  margin-bottom: 32px;
}
/* Rounded input seamlessly joined to the gradient action button.
   :focus-within lights a gradient ring + soft glow around the
   whole bar — no JS required. */

.gb-15__bar {
  display: flex;
  align-items: stretch;
  background: #fff;
  border-radius: 9999px;
  padding: 7px;
  gap: 7px;
  box-shadow: 0 18px 44px -20px rgba(236,72,153,.35),0 2px 6px rgba(59,43,32,.06),0 0 0 1.5px #f4e4d8;
  transition: box-shadow .35s ease;
}

.gb-15__bar:focus-within {
  box-shadow: 0 22px 52px -18px rgba(139,92,246,.4),0 2px 6px rgba(59,43,32,.06),0 0 0 2.5px var(--sunset-b);
}

.gb-15__input {
  flex: 1;
  min-width: 0;
  border: none;
  background: none;
  padding: 12px 14px 12px 22px;
  font-family: inherit;
  font-size: 15.5px;
  color: var(--ink);
}

.gb-15__input::placeholder {
  color: #c4ad9c;
}

.gb-15__input:focus {
  outline: none;
}

.gb-15__btn {
  flex: none;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  padding: 13px 28px;
  border: none;
  border-radius: 9999px;
  font-family: inherit;
  font-size: 15px;
  font-weight: 800;
  color: #fff;
  cursor: pointer;
  background-image: linear-gradient(110deg,var(--sunset-a) 0%,var(--sunset-b) 50%,var(--sunset-c) 100%);
  background-size: 180% auto;
  background-position: left center;
  box-shadow: 0 8px 20px -8px rgba(236,72,153,.6);
  transition: background-position .5s ease,transform .25s ease,box-shadow .35s ease;
  -webkit-tap-highlight-color: transparent;
}

.gb-15__btn svg {
  width: 16px;
  height: 16px;
  flex: none;
}

.gb-15__btn:hover {
  background-position: right center;
  transform: translateY(-1px);
  box-shadow: 0 12px 26px -8px rgba(139,92,246,.65);
}

.gb-15__btn:active {
  transform: translateY(0) scale(.97);
}

.gb-15__btn:focus-visible {
  outline: 3px solid var(--sunset-c);
  outline-offset: 3px;
}

.gb-15__chips {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 20px;
}

.gb-15__chip {
  font-size: 12.5px;
  font-weight: 600;
  color: #a08670;
  background: rgba(255,255,255,.7);
  border: 1px solid #f0dfd2;
  border-radius: 999px;
  padding: 7px 14px;
  cursor: pointer;
  transition: color .25s ease,border-color .25s ease;
}

.gb-15__chip:hover {
  color: var(--sunset-b);
  border-color: var(--sunset-b);
}

@media (prefers-reduced-motion: reduce) {
  .gb-15__bar,
    .gb-15__btn,
    .gb-15__chip {
    transition: none;
  }

  .gb-15__btn:hover {
    transform: none;
    background-position: left center;
  }
}

@media (max-width: 420px) {
  .gb-15__btn span {
    display: none;
  }

  .gb-15__btn {
    padding: 13px 18px;
  }
}
```
