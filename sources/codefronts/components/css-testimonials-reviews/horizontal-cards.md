---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/horizontal-cards/"
title: "Horizontal Sliding Testimonial Row"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Two patterns in one component, because they solve different problems: a continuously drifting marquee row for ambient social proof, and a drag-scrollable…"
has_js: "true"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Sliding Testimonial Row
Source: https://codefronts.com/components/css-testimonials-reviews/horizontal-cards/

Two patterns in one component, because they solve different problems: a continuously drifting marquee row for ambient social proof, and a drag-scrollable strip with hidden scrollbars underneath it. A single toggle switches between them, and both respect reduced-motion by stopping dead and becoming a normal scroller.
## HTML
```html
<section class="tr-24" aria-label="Horizontal sliding testimonial row demo">
  <div class="tr-24__stage">
    <header class="tr-24__head">
      <p class="tr-24__eyebrow">Ambient social proof</p>
      <h2 class="tr-24__title">A strip that never asks for vertical space</h2>
      <div class="tr-24__modes" role="group" aria-label="Choose row behaviour">
        <button class="tr-24__mode" type="button" data-mode="auto" aria-pressed="true">Auto-scroll</button>
        <button class="tr-24__mode" type="button" data-mode="manual" aria-pressed="false">Drag to scroll</button>
      </div>
    </header>

    <div class="tr-24__row" data-mode="auto">
      <div class="tr-24__track">
        <figure class="tr-24__card"><p>“Nine minutes to a human at 4am. That is the whole review.”</p><footer><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async"><span><b>Callum Doyle</b>Meridian</span></footer></figure>
        <figure class="tr-24__card"><p>“Replaced three dashboards. Deleted a weekly meeting.”</p><footer><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async"><span><b>Priya Raghunathan</b>Northwind</span></footer></figure>
        <figure class="tr-24__card"><p>“Security cleared it in nine days with no exceptions.”</p><footer><img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async"><span><b>Erin McAllister</b>Larkfield</span></footer></figure>
        <figure class="tr-24__card"><p>“Onboarded 41 people in a day, no training budget.”</p><footer><img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async"><span><b>Amara Diallo</b>Fernbrook</span></footer></figure>
        <figure class="tr-24__card"><p>“The migration guide became our internal training doc.”</p><footer><img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async"><span><b>Hana Sørensen</b>Blomst</span></footer></figure>
        <figure class="tr-24__card"><p>“Renewal took fifteen minutes. The usage report argued for itself.”</p><footer><img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="34" height="34" loading="lazy" decoding="async"><span><b>Grace Whitlock</b>Auryn</span></footer></figure>
        <div class="tr-24__clone" aria-hidden="true"></div>
      </div>
    </div>

    <p class="tr-24__chip" aria-hidden="true">duplicated track · translate:-50% seamless loop · animation-play-state pause · mask edge fade</p>
  </div>
</section>
```
## CSS
```css
.tr-24,
.tr-24 *,
.tr-24 *::before,
.tr-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-24-bg: oklch(0.17 0.02 262);
  --tr-24-card: oklch(0.225 0.024 262);
  --tr-24-ink: oklch(0.97 0.006 262);
  --tr-24-mut: oklch(0.71 0.02 262);
  --tr-24-acc: oklch(0.8 0.15 178);
  background: var(--tr-24-bg);
  color: var(--tr-24-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-24__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(22px,3.4vw,38px);
  padding: clamp(20px,4vw,56px) 0;
}

.tr-24__head {
  text-align: center;
  display: grid;
  justify-items: center;
  gap: 11px;
  padding-inline: 20px;
}

.tr-24__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--tr-24-acc);
}

.tr-24__title {
  font-size: clamp(23px,3.8vw,40px);
  font-weight: 670;
  letter-spacing: -.038em;
  line-height: 1.1;
  text-wrap: balance;
}

.tr-24__modes {
  display: flex;
  gap: 6px;
  margin-top: 6px;
  padding: 5px;
  border-radius: 99px;
  background: oklch(1 0 0/.06);
  border: 1px solid oklch(1 0 0/.1);
}

.tr-24__mode {
  min-height: 40px;
  padding: 0 18px;
  border: 0;
  border-radius: 99px;
  background: transparent;
  color: var(--tr-24-mut);
  font: inherit;
  font-size: 13px;
  font-weight: 580;
  cursor: pointer;
  transition: background .25s,color .25s;
}

.tr-24__mode[aria-pressed='true'] {
  background: var(--tr-24-acc);
  color: oklch(0.19 0.03 178);
}

.tr-24__mode:focus-visible {
  outline: 3px solid var(--tr-24-acc);
  outline-offset: 3px;
}

.tr-24__row {
  width: 100%;
  overflow: hidden;
  -webkit-mask: linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);
  mask: linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);
}

.tr-24__row[data-mode='manual'] {
  overflow-x: auto;
  scrollbar-width: none;
  cursor: grab;
  scroll-snap-type: x proximity;
  overscroll-behavior-x: contain;
}

.tr-24__row[data-mode='manual']::-webkit-scrollbar {
  display: none;
}

.tr-24__row[data-mode='manual'].is-drag {
  cursor: grabbing;
  scroll-snap-type: none;
}

.tr-24__track {
  display: flex;
  gap: clamp(12px,1.6vw,18px);
  width: max-content;
  padding: 14px clamp(12px,1.6vw,18px);
}

.tr-24__row[data-mode='auto'] .tr-24__track {
  animation: tr-24-slide 46s linear infinite;
}

.tr-24__row[data-mode='auto']:hover .tr-24__track,
.tr-24__row[data-mode='auto']:focus-within .tr-24__track {
  animation-play-state: paused;
}

@keyframes tr-24-slide {
  to {
    translate: calc(-50% - clamp(6px,.8vw,9px)) 0;
  }
}

.tr-24__card {
  flex: 0 0 clamp(250px,26vw,310px);
  scroll-snap-align: center;
  display: grid;
  gap: 14px;
  padding: 20px;
  border-radius: 16px;
  background: linear-gradient(165deg,color-mix(in oklch,var(--tr-24-acc) 7%,var(--tr-24-card)),var(--tr-24-card) 68%);
  border: 1px solid oklch(1 0 0/.09);
  transition: border-color .3s,translate .3s cubic-bezier(.16,1,.3,1);
}

.tr-24__card:hover {
  border-color: color-mix(in oklch,var(--tr-24-acc) 42%,transparent);
  translate: 0 -3px;
}

.tr-24__card p {
  font-size: 14.5px;
  line-height: 1.5;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.tr-24__card footer {
  display: flex;
  align-items: center;
  gap: 10px;
  padding-top: 13px;
  border-top: 1px solid oklch(1 0 0/.1);
}

.tr-24__card footer img {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: oklch(0.4 0.04 262);
}

.tr-24__card footer span {
  display: grid;
  font-size: 11px;
  line-height: 1.3;
  color: var(--tr-24-mut);
}

.tr-24__card footer b {
  font-size: 13px;
  font-weight: 640;
  color: var(--tr-24-ink);
  letter-spacing: -.012em;
}

.tr-24__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-24-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
  margin-inline: 16px;
}

@media (prefers-reduced-motion: reduce) {
  .tr-24__row[data-mode='auto'] {
    overflow-x: auto;
  }

  .tr-24__row[data-mode='auto'] .tr-24__track {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tr-24').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const row = root.querySelector('.tr-24__row');
    const track = root.querySelector('.tr-24__track');
    const clone = root.querySelector('.tr-24__clone');

    // duplicate the cards once so translate:-50% loops seamlessly
    root.querySelectorAll('.tr-24__track > .tr-24__card').forEach((c) => clone.append(c.cloneNode(true)));
    clone.style.display = 'contents';

    root.querySelectorAll('.tr-24__mode').forEach((btn) => {
      btn.addEventListener('click', () => {
        root.querySelectorAll('.tr-24__mode').forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
        row.dataset.mode = btn.dataset.mode;
        if (btn.dataset.mode === 'manual') row.scrollLeft = 0;
      });
    });

    let down = false, startX = 0, startL = 0;
    row.addEventListener('pointerdown', (e) => {
      if (row.dataset.mode !== 'manual') return;
      down = true; startX = e.clientX; startL = row.scrollLeft;
      row.classList.add('is-drag'); row.setPointerCapture(e.pointerId);
    });
    row.addEventListener('pointermove', (e) => { if (down) row.scrollLeft = startL - (e.clientX - startX); });
    const end = () => { down = false; row.classList.remove('is-drag'); };
    row.addEventListener('pointerup', end);
    row.addEventListener('pointercancel', end);
  });
})();
```
