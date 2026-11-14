---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-scroll-triggered-word-reveal/"
title: "CSS Typewriter Scroll-Triggered Word Reveal"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "Words in a long-form paragraph reveal sequentially only when the element enters the viewport — IntersectionObserver triggers staggered CSS class additions…"
has_js: "true"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Scroll-Triggered Word Reveal
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-scroll-triggered-word-reveal/

Words in a long-form paragraph reveal sequentially only when the element enters the viewport — IntersectionObserver triggers staggered CSS class additions for a scroll-activated typewriter effect.
## HTML
```html
<div class="tw-14">
  <article class="tw-14__article">
    <h2 class="tw-14__heading tw-14__reveal">The art of good design.</h2>
    <p class="tw-14__body tw-14__reveal">Good design is not just about how something looks — it is about how it works, how it feels, and how it makes people feel in return. Every decision carries weight.</p>
    <p class="tw-14__body tw-14__reveal">Typography, spacing, colour, motion — each is a tool in the designer's hand. Used well, they create clarity. Used poorly, they create noise. The difference is intention.</p>
    <p class="tw-14__pullquote tw-14__reveal">Design is intelligence made visible.</p>
  </article>
</div>
```
## CSS
```css
.tw-14,
.tw-14 *,
.tw-14 *::before,
.tw-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-14 ::selection {
  background: #0ea5e9;
  color: #001a28;
}

.tw-14 {
  --blue: #0ea5e9;
  --sky: #38bdf8;
  --bg: #020d17;
  --text: #e0f2fe;
  --muted: #334e5e;
  font-family: 'Georgia', 'Times New Roman', serif;
  min-height: 340px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 48px 24px;
}

.tw-14__article {
  max-width: 520px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.tw-14__heading {
  font-size: clamp(1.8rem, 5vw, 2.8rem);
  font-weight: 700;
  color: var(--text);
  line-height: 1.2;
}

.tw-14__body {
  font-size: 1.05rem;
  line-height: 1.8;
  color: #94a3b8;
}

.tw-14__pullquote {
  font-size: 1.2rem;
  font-style: italic;
  color: var(--sky);
  border-left: 3px solid var(--blue);
  padding-left: 20px;
}
/* Word reveal state machine */

.tw-14__reveal .tw-14-word {
  display: inline-block;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.4s ease, transform 0.4s ease;
  transition-delay: min(calc(var(--wi) * 40ms), 900ms);
}

.tw-14__reveal.visible .tw-14-word {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .tw-14__reveal .tw-14-word {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  const targets = document.querySelectorAll('.tw-14__reveal');
  if (!targets.length) return;

  // Split text into word spans
  targets.forEach((el) => {
    const words = el.textContent.split(/(s+)/);
    el.innerHTML = words.map((part, i) => {
      if (/^s+$/.test(part)) return part;
      return `<span class="tw-14-word" style="--wi:${i}" aria-hidden="false">${part}</span>`;
    }).join('');
  });

  // Observe each element
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting && entry.intersectionRatio > 0) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  targets.forEach((el) => observer.observe(el));
})();
```
