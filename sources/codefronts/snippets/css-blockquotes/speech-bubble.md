---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/speech-bubble/"
title: "Speech Bubble CSS Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "Two ways to grow a tail on a quote bubble, side by side in one conversation: the classic border-triangle ::after (works everywhere, back to ancient browsers)…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Speech Bubble CSS Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/speech-bubble/

Two ways to grow a tail on a quote bubble, side by side in one conversation: the classic border-triangle ::after (works everywhere, back to ancient browsers) and the modern clip-path tail, which can be any shape — here a curved-feeling sliver that border tricks can't draw. Bubbles alternate sides like a chat thread, each anchored to a real avatar, and the tail geometry is annotated in the markup so you can lift whichever technique your support matrix allows.
## HTML
```html
<section class="bq-12" aria-label="Speech bubble blockquote demo">
  <div class="bq-12__stage">
    <div class="bq-12__thread">
      <figure class="bq-12__msg">
        <span class="bq-12__ava" aria-hidden="true" style="--img:url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=120&auto=format&fit=crop')"></span>
        <div class="bq-12__stack">
          <blockquote class="bq-12__bubble bq-12__bubble--classic">
            <p>The tail on this bubble is the old border trick — a zero-size box where only one border edge is painted. Works in literally every browser.</p>
          </blockquote>
          <figcaption class="bq-12__meta">Devon · border-right-color tail</figcaption>
        </div>
      </figure>
      <figure class="bq-12__msg bq-12__msg--me">
        <div class="bq-12__stack">
          <blockquote class="bq-12__bubble bq-12__bubble--modern">
            <p>And this one is clip-path — the tail carries the bubble's gradient, which borders can't do. Any polygon you can imagine.</p>
          </blockquote>
          <figcaption class="bq-12__meta">Ana · clip-path:polygon() tail</figcaption>
        </div>
        <span class="bq-12__ava" aria-hidden="true" style="--img:url('https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=120&auto=format&fit=crop')"></span>
      </figure>
    </div>
    <p class="bq-12__chip" aria-hidden="true">border-triangle vs clip-path tails · drop-shadow() wraps both</p>
  </div>
</section>
```
## CSS
```css
.bq-12,
.bq-12 *,
.bq-12 *::before,
.bq-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.96 0.008 250);
  --ink: oklch(0.25 0.015 260);
  --mut: oklch(0.53 0.015 260);
  --bubble: oklch(1 0 0);
  --b2a: oklch(0.6 0.2 260);
  --b2b: oklch(0.55 0.21 290);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-12__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: linear-gradient(180deg,oklch(0.97 0.01 230),var(--bg));
  overflow-y: auto;
}

.bq-12__thread {
  width: min(100%,560px);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.bq-12__msg {
  display: flex;
  gap: 12px;
  align-items: flex-end;
  filter: drop-shadow(0 6px 14px oklch(0.3 0.03 260/.16));
}

.bq-12__msg--me {
  justify-content: flex-end;
}

.bq-12__ava {
  width: 40px;
  height: 40px;
  border-radius: 99px;
  flex: none;
  background: linear-gradient(135deg,oklch(0.7 0.1 250),oklch(0.55 0.1 300));
  background-image: var(--img),linear-gradient(135deg,oklch(0.7 0.1 250),oklch(0.55 0.1 300));
  background-size: cover;
  background-position: center;
}

.bq-12__stack {
  max-width: 76%;
}

.bq-12__bubble {
  position: relative;
  padding: 13px 17px;
  font-size: 14.5px;
  line-height: 1.58;
}

.bq-12__bubble p {
  text-wrap: pretty;
}

.bq-12__bubble--classic {
  background: var(--bubble);
  border-radius: 18px 18px 18px 6px;
}

.bq-12__bubble--classic::after {
  content: '';
  position: absolute;
  left: -10px;
  bottom: 10px;
  border: 11px solid transparent;
  border-right-color: var(--bubble);
  border-left-width: 0;
}

.bq-12__bubble--modern {
  background: linear-gradient(135deg,var(--b2a),var(--b2b));
  color: oklch(0.99 0.005 260);
  border-radius: 18px 18px 6px 18px;
}

.bq-12__bubble--modern::after {
  content: '';
  position: absolute;
  right: -11px;
  bottom: 8px;
  width: 14px;
  height: 18px;
  background: var(--b2b);
  clip-path: polygon(0 0,100% 78%,0 100%);
}

.bq-12__meta {
  margin-top: 7px;
  font-size: 11.5px;
  color: var(--mut);
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.bq-12__msg--me .bq-12__meta {
  text-align: right;
}

.bq-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .bq-12 * {
    transition-duration: .01ms !important;
  }
}
```
