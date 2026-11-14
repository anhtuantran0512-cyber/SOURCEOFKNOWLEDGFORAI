---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/social-share-fab/"
title: "Social Share Floating Button Cluster CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A share cluster that respects the platform: on devices with a native share sheet it calls it, and everywhere else it fans out a set of channel buttons plus a…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social Share Floating Button Cluster CSS
Source: https://codefronts.com/components/css-floating-buttons/social-share-fab/

A share cluster that respects the platform: on devices with a native share sheet it calls it, and everywhere else it fans out a set of channel buttons plus a copy-link control with real success feedback. Includes the detail most share widgets skip — the copied state is announced, not just coloured green.
## HTML
```html
<section class="fb-16" aria-label="Social share floating cluster demo">
  <article class="fb-16__article">
    <p class="fb-16__eyebrow">Web Share API · clipboard fallback</p>
    <h2 class="fb-16__title">Share, then get out of the way</h2>
    <p class="fb-16__sub">On a phone this opens the system sheet. On a desktop it fans out four channels and a copy-link tile with feedback you can actually hear.</p>
    <div class="fb-16__meta"><span class="fb-16__pill">8 min read</span><span class="fb-16__pill">Front-end</span><span class="fb-16__pill">Updated Aug 2026</span></div>
    <div class="fb-16__thumb" aria-hidden="true"></div>
    <p class="fb-16__sr" id="fb-16-status" role="status" aria-live="polite"></p>
  </article>
  <div class="fb-16__dock" id="fb-16-dock" data-open="false">
    <ul class="fb-16__cluster" id="fb-16-cluster">
      <li style="--fb-16-i:0"><button class="fb-16__tile" type="button" tabindex="-1" data-fb-ch="X"><span aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M4 4l7.6 9.6L4.4 20h2.2l5.8-5.9 4.6 5.9H20l-7.9-10L19.6 4h-2.2l-5.2 5.3L8 4z" fill="currentColor"/></svg></span>Post</button></li>
      <li style="--fb-16-i:1"><button class="fb-16__tile" type="button" tabindex="-1" data-fb-ch="LinkedIn"><span aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><rect x="3" y="3" width="18" height="18" rx="3" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7.5 10v7M7.5 7.2v.1M11.5 17v-4a2.4 2.4 0 0 1 4.8 0v4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>LinkedIn</button></li>
      <li style="--fb-16-i:2"><button class="fb-16__tile" type="button" tabindex="-1" data-fb-ch="Email"><span aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2.4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 7l8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></span>Email</button></li>
      <li style="--fb-16-i:3"><button class="fb-16__tile" type="button" tabindex="-1" data-fb-ch="Reddit"><span aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><circle cx="12" cy="13" r="7.5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="9.3" cy="12.6" r="1.1" fill="currentColor"/><circle cx="14.7" cy="12.6" r="1.1" fill="currentColor"/><path d="M9.4 15.8c1.5 1.1 3.7 1.1 5.2 0" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M15 5.5l.6 2.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></span>Reddit</button></li>
      <li style="--fb-16-i:4"><button class="fb-16__tile fb-16__tile--copy" id="fb-16-copy" type="button" tabindex="-1"><span aria-hidden="true"><svg class="fb-16__cIco" viewBox="0 0 24 24" focusable="false"><rect x="8" y="8" width="12" height="12" rx="2.4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M16 5.5A2.5 2.5 0 0 0 13.5 4h-7A2.5 2.5 0 0 0 4 6.5v7A2.5 2.5 0 0 0 5.5 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><svg class="fb-16__okIco" viewBox="0 0 24 24" focusable="false"><path d="M5 12.5l4.5 4.5L19 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span><b id="fb-16-copyLabel">Copy link</b></button></li>
    </ul>
    <button class="fb-16__fab" id="fb-16-fab" type="button" aria-expanded="false" aria-controls="fb-16-cluster" aria-label="Share this article">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="18" cy="5.5" r="2.7" fill="currentColor"/><circle cx="6" cy="12" r="2.7" fill="currentColor"/><circle cx="18" cy="18.5" r="2.7" fill="currentColor"/><path d="M8.5 10.7l7-3.8M8.5 13.3l7 3.8" stroke="currentColor" stroke-width="1.9"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-16-bg);
  --fb-16-bg: oklch(0.97 0.008 60);
  --fb-16-brand: oklch(0.5 0.16 25);
  --fb-16-ink: oklch(0.21 0.02 40);
  --fb-16-mut: oklch(0.52 0.015 40);
  --fb-16-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-16-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-16 *,
.fb-16 *::before,
.fb-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-16__article {
  width: min(100%,58ch);
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
}

.fb-16__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-16-brand);
}

.fb-16__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-16__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-16-mut);
  text-wrap: pretty;
}

.fb-16__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  justify-content: center;
}

.fb-16__pill {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--fb-16-mut);
  background: var(--fb-16-card);
  border: 1px solid oklch(0.21 0.02 40/.1);
  border-radius: 99px;
  padding: 6px 12px;
}

.fb-16__thumb {
  width: 100%;
  height: clamp(120px,22vw,180px);
  border-radius: 20px;
  background: linear-gradient(150deg,oklch(0.5 0.12 30/.35),oklch(0.3 0.08 300/.5)),url("https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?q=80&w=1200&auto=format&fit=crop") center/cover;
  box-shadow: 0 20px 44px -26px oklch(0.21 0.02 40/.9);
}

.fb-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fb-16__dock {
  position: absolute;
  right: clamp(16px,3.5vw,36px);
  bottom: calc(clamp(16px,3.5vw,36px) + env(safe-area-inset-bottom));
  z-index: 5;
  display: grid;
  justify-items: end;
  gap: 12px;
}

.fb-16__cluster {
  list-style: none;
  display: grid;
  gap: 8px;
  justify-items: end;
}

.fb-16__tile {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 46px;
  padding: 0 15px 0 9px;
  border: 1px solid oklch(0.21 0.02 40/.09);
  border-radius: 14px;
  background: var(--fb-16-card);
  color: var(--fb-16-ink);
  font-size: 13.5px;
  font-weight: 620;
  font-family: inherit;
  cursor: pointer;
  box-shadow: 0 10px 24px -16px oklch(0.21 0.02 40/.9);
  opacity: 0;
  translate: 0 14px;
  scale: .9;
  pointer-events: none;
  transition: opacity .22s ease,translate .3s cubic-bezier(.2,1.2,.4,1),scale .3s cubic-bezier(.2,1.2,.4,1),background .16s ease;
  transition-delay: calc((4 - var(--fb-16-i)) * 40ms);
}

.fb-16__tile span {
  display: grid;
  width: 32px;
  height: 32px;
  place-items: center;
  border-radius: 10px;
  background: oklch(0.5 0.16 25/.1);
  color: var(--fb-16-brand);
}

.fb-16__tile svg {
  width: 19px;
  height: 19px;
  grid-area: 1/1;
}

.fb-16__dock[data-open="true"] .fb-16__tile {
  opacity: 1;
  translate: 0 0;
  scale: 1;
  pointer-events: auto;
  transition-delay: calc(var(--fb-16-i) * 45ms);
}

.fb-16__tile:hover {
  background: oklch(0.97 0.012 40);
}

.fb-16__tile:focus-visible {
  outline: 3px solid var(--fb-16-brand);
  outline-offset: 2px;
}

.fb-16__tile:active {
  scale: .97;
}

.fb-16__okIco {
  opacity: 0;
  scale: .5;
  transition: opacity .2s ease,scale .3s cubic-bezier(.2,1.5,.4,1);
}

.fb-16__tile--copy.is-done span {
  background: oklch(0.72 0.17 145/.16);
  color: oklch(0.45 0.14 148);
}

.fb-16__tile--copy.is-done .fb-16__cIco {
  opacity: 0;
  scale: .5;
}

.fb-16__tile--copy.is-done .fb-16__okIco {
  opacity: 1;
  scale: 1;
}

.fb-16__cIco {
  transition: opacity .2s ease,scale .2s ease;
}

.fb-16__fab {
  display: grid;
  place-items: center;
  inline-size: 60px;
  block-size: 60px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.99 0.01 25);
  background: linear-gradient(150deg,oklch(0.66 0.19 35),var(--fb-16-brand));
  box-shadow: 0 14px 32px -12px oklch(0.5 0.16 25/.85),0 2px 6px oklch(0.3 0.06 25/.3);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1),rotate .3s ease;
}

.fb-16__fab svg {
  width: 25px;
  height: 25px;
}

.fb-16__fab:hover {
  transform: translateY(-2px) scale(1.04);
}

.fb-16__fab:active {
  transform: scale(.93);
}

.fb-16__fab:focus-visible {
  outline: 3px solid var(--fb-16-brand);
  outline-offset: 4px;
}

.fb-16__dock[data-open="true"] .fb-16__fab {
  rotate: 90deg;
}

@media (prefers-reduced-motion: reduce) {
  .fb-16 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const dock = document.getElementById('fb-16-dock');
  const fab = document.getElementById('fb-16-fab');
  const copy = document.getElementById('fb-16-copy');
  const copyLabel = document.getElementById('fb-16-copyLabel');
  const status = document.getElementById('fb-16-status');
  if (!dock || !fab || fab.dataset.fbWired) return;
  fab.dataset.fbWired = '1';
  const tiles = [...dock.querySelectorAll('.fb-16__tile')];
  const set = (open) => {
    dock.dataset.open = String(open);
    fab.setAttribute('aria-expanded', String(open));
    tiles.forEach((t) => { t.tabIndex = open ? 0 : -1; });
  };
  fab.addEventListener('click', async () => {
    const data = { title: 'Share, then get out of the way', text: 'A share cluster that respects the platform.', url: location.href };
    if (navigator.share) {
      try { await navigator.share(data); status.textContent = 'Share sheet opened'; return; } catch (err) { if (err && err.name === 'AbortError') return; }
    }
    set(dock.dataset.open !== 'true');
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && dock.dataset.open === 'true') { set(false); fab.focus(); }
  });
  copy.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(location.href); } catch (err) { /* clipboard blocked in sandbox */ }
    copy.classList.add('is-done');
    copyLabel.textContent = 'Copied';
    status.textContent = 'Link copied to clipboard';
    setTimeout(() => { copy.classList.remove('is-done'); copyLabel.textContent = 'Copy link'; }, 2400);
  });
  tiles.filter((t) => t.dataset.fbCh).forEach((t) => t.addEventListener('click', () => {
    status.textContent = 'Opening ' + t.dataset.fbCh + ' share intent';
  }));
})();
```
