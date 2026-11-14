---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/follow-button-with-following-toggle/"
title: "Follow Button with Following Toggle"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "Follow becomes Following, and hovering Following reveals Unfollow in red — the three-state affordance real products ship."
has_js: "true"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Follow Button with Following Toggle
Source: https://codefronts.com/snippets/css-social-buttons/follow-button-with-following-toggle/

Follow becomes Following, and hovering Following reveals Unfollow in red — the three-state affordance real products ship. All three labels occupy the same grid cell, so the button never changes width as the state changes. A single data-state attribute drives every visual, and aria-pressed carries the same fact to assistive technology.
## HTML
```html
<div class="soc-12">
  <div class="soc-12__stage">
    <div class="soc-12__card">
      <div class="soc-12__who">
        <span class="soc-12__avatar" aria-hidden="true">PS</span>
        <span class="soc-12__id">
          <strong class="soc-12__name">Priya Sharma</strong>
          <span class="soc-12__handle">@priya.builds</span>
        </span>
      </div>
      <p class="soc-12__bio">Design engineer. Writes about CSS layout, motion and the parts of accessibility nobody tests.</p>
      <div class="soc-12__row">
        <button class="soc-12__btn" type="button" data-state="idle" aria-pressed="false">
          <span class="soc-12__icons" aria-hidden="true">
            <svg class="soc-12__i-plus" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M12 6v12"/><path d="M6 12h12"/></svg>
            <svg class="soc-12__i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
            <svg class="soc-12__i-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"><path d="M6 6l12 12"/><path d="M18 6 6 18"/></svg>
          </span>
          <span class="soc-12__labels">
            <span class="soc-12__l-follow">Follow</span>
            <span class="soc-12__l-following">Following</span>
            <span class="soc-12__l-unfollow">Unfollow</span>
          </span>
        </button>
        <p class="soc-12__count"><strong class="soc-12__num">18,204</strong> followers</p>
      </div>
      <p class="soc-12__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');

.soc-12 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --brand: #111117;
  --on-brand: #ffffff;
  --danger: #c8382f;
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
  .soc-12 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
    --danger: oklch(54% .19 27);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-12:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
    --brand: #f2f2f5;
    --on-brand: #0f0f14;
    --danger: #ff6f61;
  }
}

.soc-12[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
  --brand: #f2f2f5;
  --on-brand: #0f0f14;
  --danger: #ff6f61;
}

.soc-12,
.soc-12 *,
.soc-12 *::before,
.soc-12 *::after {
  box-sizing: border-box;
}

.soc-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-12__card {
  inline-size: min(30rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.35rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 22px 48px -30px rgb(9 9 20/.45);
}

.soc-12__who {
  display: flex;
  align-items: center;
  gap: .8rem;
  margin-block-end: 1rem;
  min-inline-size: 0;
}

.soc-12__avatar {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 3rem;
  block-size: 3rem;
  border-radius: 50%;
  background: linear-gradient(140deg,#7c5cff,#2ec8b0);
  color: #fff;
  font-size: .9rem;
  font-weight: 700;
  letter-spacing: .02em;
}

.soc-12__id {
  display: grid;
  min-inline-size: 0;
}

.soc-12__name {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.soc-12__handle {
  font-size: .85rem;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.soc-12__bio {
  margin: 0 0 1.5rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.soc-12__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .85rem;
}

.soc-12__btn {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.875rem;
  padding: 0 1.2rem;
  border: 1px solid var(--brand);
  border-radius: 999px;
  background: var(--brand);
  color: var(--on-brand);
  font: inherit;
  font-size: .92rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color .2s ease, color .2s ease, border-color .2s ease, translate .18s cubic-bezier(.16,1,.3,1);
}

.soc-12__btn:active {
  translate: 0 1px;
}

.soc-12__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-12__icons {
  display: grid;
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.soc-12__icons svg {
  grid-area: 1/1;
  inline-size: 1.05rem;
  block-size: 1.05rem;
  opacity: 0;
  transition: opacity .16s ease;
}

.soc-12__labels {
  display: grid;
}

.soc-12__labels span {
  grid-area: 1/1;
  opacity: 0;
  white-space: nowrap;
  transition: opacity .16s ease;
}

.soc-12__btn[data-state="idle"] .soc-12__l-follow,
.soc-12__btn[data-state="idle"] .soc-12__i-plus {
  opacity: 1;
}

.soc-12__btn[data-state="following"] {
  background: var(--surface);
  color: var(--fg);
  border-color: var(--line);
}

.soc-12__btn[data-state="following"] .soc-12__l-following,
.soc-12__btn[data-state="following"] .soc-12__i-check {
  opacity: 1;
}

.soc-12__btn[data-state="following"]:hover,
.soc-12__btn[data-state="following"]:focus-visible {
  background: color-mix(in oklab,var(--danger) 12%,var(--surface));
  border-color: var(--danger);
  color: var(--danger);
}

.soc-12__btn[data-state="following"]:hover .soc-12__l-following,
.soc-12__btn[data-state="following"]:focus-visible .soc-12__l-following,
.soc-12__btn[data-state="following"]:hover .soc-12__i-check,
.soc-12__btn[data-state="following"]:focus-visible .soc-12__i-check {
  opacity: 0;
}

.soc-12__btn[data-state="following"]:hover .soc-12__l-unfollow,
.soc-12__btn[data-state="following"]:focus-visible .soc-12__l-unfollow,
.soc-12__btn[data-state="following"]:hover .soc-12__i-x,
.soc-12__btn[data-state="following"]:focus-visible .soc-12__i-x {
  opacity: 1;
}

.soc-12__count {
  margin: 0;
  font-size: .88rem;
  color: var(--muted);
}

.soc-12__num {
  color: var(--fg);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.soc-12__live {
  margin: 1.1rem 0 0;
  min-block-size: 1.1rem;
  font-size: .8rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .soc-12__btn,
    .soc-12__labels span,
    .soc-12__icons svg {
    transition-duration: 1ms;
  }

  .soc-12__btn:active {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-12__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }

  .soc-12__btn[data-state="following"]:hover {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.soc-12');
  if (!root) return;
  const btn = root.querySelector('.soc-12__btn');
  const num = root.querySelector('.soc-12__num');
  const live = root.querySelector('.soc-12__live');
  let count = 18204;
  btn.addEventListener('click', () => {
    const following = btn.dataset.state === 'following';
    btn.dataset.state = following ? 'idle' : 'following';
    btn.setAttribute('aria-pressed', String(!following));
    count += following ? -1 : 1;
    num.textContent = count.toLocaleString('en-US');
    live.textContent = following ? 'Unfollowed Priya Sharma.' : 'Following Priya Sharma.';
  });
})();
```
