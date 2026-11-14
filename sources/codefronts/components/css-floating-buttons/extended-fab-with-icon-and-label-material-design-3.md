---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/extended-fab-with-icon-and-label-material-design-3/"
title: "Extended FAB with Icon and Label (Material Design 3)"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "Material's extended FAB — 56px tall, icon plus label, 16px radius — with the behaviour that makes it worth using: it collapses to an icon-only FAB as the…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Extended FAB with Icon and Label (Material Design 3)
Source: https://codefronts.com/components/css-floating-buttons/extended-fab-with-icon-and-label-material-design-3/

Material's extended FAB — 56px tall, icon plus label, 16px radius — with the behaviour that makes it worth using: it collapses to an icon-only FAB as the user scrolls down and re-extends when they scroll back up, so the label sells the action on arrival and the button stops eating screen width once reading starts.
## HTML
```html
<section class="fb-06" aria-label="Extended floating action button demo">
  <div class="fb-06__frame">
    <div class="fb-06__scroll" id="fb-06-scroll" tabindex="0" aria-label="Scrollable article, scroll to collapse the button">
      <div class="fb-06__hero">
        <p class="fb-06__eyebrow">Material 3 · extended FAB</p>
        <h2 class="fb-06__title">Scroll down. Watch it shrink.</h2>
        <p class="fb-06__sub">The label sells the action on arrival, then gets out of the way once reading starts. Scroll back up and it returns.</p>
      </div>
      <article class="fb-06__body">
        <p>An extended FAB is 56 CSS pixels tall with a 16px corner radius, 16px of leading padding, 20px trailing, and a 12px gap between icon and label. Those numbers are the spec, and they are the difference between a Material button and a rounded rectangle.</p>
        <p>The collapse is direction-based, not position-based: sampling <code>scrollTop</code> against the previous frame with a small dead zone means a jittery trackpad never flaps the state, and a user who scrolls two pixels never sees the button twitch.</p>
        <p>Because the label is clipped rather than removed, the accessible name is stable in both states. A screen-reader user who tabs to the button after scrolling hears exactly the same thing as one who tabs to it at the top of the page.</p>
        <p>Keep the right edge pinned. If the pill shrinks from both sides, the tap target slides out from under a thumb that is already reaching for it — a small thing that feels broken without being nameable.</p>
        <p>The same technique drives search bars that collapse into an icon, save buttons that shrink after the first edit, and toolbars that condense on scroll. Once the grid track is doing the measuring, the state machine is trivial.</p>
      </article>
    </div>
    <button class="fb-06__efab" id="fb-06-efab" type="button" data-state="extended">
      <span class="fb-06__ico" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25z" fill="currentColor"/><path d="M20.71 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z" fill="currentColor"/></svg></span>
      <span class="fb-06__label">Compose</span>
    </button>
  </div>
  <p class="fb-06__chip">grid track + padding transition · rAF scroll sampling</p>
</section>
```
## CSS
```css
.fb-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-06-bg);
  --fb-06-bg: oklch(0.96 0.014 265);
  --fb-06-container: oklch(0.55 0.18 265);
  --fb-06-on: oklch(0.99 0.01 265);
  --fb-06-ink: oklch(0.23 0.025 265);
  --fb-06-mut: oklch(0.53 0.02 265);
  --fb-06-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-06-ink);
  display: grid;
  place-items: center;
  align-content: center;
  gap: 16px;
  padding: clamp(18px,4vw,44px);
}

.fb-06 *,
.fb-06 *::before,
.fb-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-06__frame {
  position: relative;
  width: min(100%,560px);
  height: min(72svh,620px);
  border-radius: 28px;
  overflow: hidden;
  background: var(--fb-06-card);
  border: 1px solid oklch(0.23 0.025 265/.1);
  box-shadow: 0 24px 60px -30px oklch(0.23 0.025 265/.7);
}

.fb-06__scroll {
  height: 100%;
  overflow: auto;
  scroll-behavior: smooth;
  padding: 0 0 92px;
  scrollbar-width: thin;
}

.fb-06__scroll:focus-visible {
  outline: 3px solid var(--fb-06-container);
  outline-offset: -3px;
}

.fb-06__hero {
  padding: clamp(26px,5vw,44px) clamp(20px,4vw,34px) 22px;
  display: grid;
  gap: 10px;
  background: linear-gradient(160deg,oklch(0.93 0.04 265),oklch(0.98 0.01 265));
}

.fb-06__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-06-container);
}

.fb-06__title {
  font-size: clamp(24px,4vw,34px);
  line-height: 1.08;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-06__sub {
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--fb-06-mut);
  text-wrap: pretty;
}

.fb-06__body {
  display: grid;
  gap: 15px;
  padding: 22px clamp(20px,4vw,34px) 0;
}

.fb-06__body p {
  font-size: 14.5px;
  line-height: 1.72;
  color: oklch(0.36 0.02 265);
  text-wrap: pretty;
}

.fb-06__body code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.55 0.18 265/.1);
  padding: 2px 6px;
  border-radius: 6px;
}

.fb-06__efab {
  position: absolute;
  right: 20px;
  bottom: 20px;
  z-index: 3;
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: 12px;
  block-size: 56px;
  padding-inline: 16px 20px;
  border: 0;
  border-radius: 16px;
  background: var(--fb-06-container);
  color: var(--fb-06-on);
  font-size: 15px;
  font-weight: 640;
  letter-spacing: -.01em;
  cursor: pointer;
  box-shadow: 0 8px 24px -8px oklch(0.4 0.16 265/.8),0 2px 5px oklch(0.3 0.1 265/.28);
  transition: grid-template-columns .32s cubic-bezier(.2,.8,.2,1),gap .32s cubic-bezier(.2,.8,.2,1),padding-inline .32s cubic-bezier(.2,.8,.2,1),box-shadow .25s ease,transform .2s ease;
}

.fb-06__efab[data-state="collapsed"] {
  grid-template-columns: auto 0fr;
  gap: 0;
  padding-inline: 16px;
}

.fb-06__ico {
  display: grid;
  place-items: center;
}

.fb-06__ico svg {
  width: 24px;
  height: 24px;
}

.fb-06__label {
  overflow: hidden;
  white-space: nowrap;
}

.fb-06__efab:hover {
  box-shadow: 0 12px 30px -8px oklch(0.4 0.16 265/.85);
  transform: translateY(-1px);
}

.fb-06__efab:active {
  transform: scale(.96);
}

.fb-06__efab:focus-visible {
  outline: 3px solid oklch(0.4 0.16 265);
  outline-offset: 3px;
}

.fb-06__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-06-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.23 0.025 265/.14);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .fb-06__efab {
    transition: none;
  }

  .fb-06__scroll {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
(() => {
  const scroller = document.getElementById('fb-06-scroll');
  const efab = document.getElementById('fb-06-efab');
  if (!scroller || !efab || efab.dataset.fbWired) return;
  efab.dataset.fbWired = '1';
  let last = 0, ticking = false;
  const update = () => {
    const y = scroller.scrollTop;
    if (Math.abs(y - last) > 12) {
      efab.dataset.state = y > last && y > 40 ? 'collapsed' : 'extended';
      last = y;
    }
    ticking = false;
  };
  scroller.addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }, { passive: true });
  efab.addEventListener('click', () => {
    efab.dataset.state = efab.dataset.state === 'collapsed' ? 'extended' : 'collapsed';
  });
})();
```
