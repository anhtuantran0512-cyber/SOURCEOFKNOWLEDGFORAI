---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/css-footer-with-social-media-follow-icons/"
title: "CSS Footer with Social Media Follow Icons"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "Social icons done without an icon font and without a single external request: six inline SVG marks, each carrying its own brand colour as a custom property,…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Footer with Social Media Follow Icons
Source: https://codefronts.com/layouts/css-footer-designs/css-footer-with-social-media-follow-icons/

Social icons done without an icon font and without a single external request: six inline SVG marks, each carrying its own brand colour as a custom property, with a hover that lifts, tints and ripples. The accessible name says what the link does ("Follow us on Instagram"), not what the picture is.
## HTML
```html
<section class="ft-09" aria-label="Footer with social media icons demo">
  <main class="ft-09__main">
    <p class="ft-09__eyebrow">Inline SVG · per-icon --brand token</p>
    <h1 class="ft-09__title">Follow buttons that don't cost a request</h1>
    <p class="ft-09__sub">Six marks, zero icon fonts, zero network calls, and an accessible name on every link that says what happens when you click it.</p>
  </main>
  <footer class="ft-09__foot">
    <div class="ft-09__cta">
      <div>
        <h2 class="ft-09__h">Come and say hello</h2>
        <p class="ft-09__sub2">Weekly build notes, occasional live streams, and a lot of CSS experiments.</p>
      </div>
      <ul class="ft-09__socials">
        <li><a class="ft-09__social" style="--ft-09-brand:oklch(0.62 0.19 20)" href="#ft-09-a" rel="me noopener" aria-label="Follow us on Instagram — 84,200 followers">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>
          <span class="ft-09__count">84.2k</span></a></li>
        <li><a class="ft-09__social" style="--ft-09-brand:oklch(0.68 0.15 235)" href="#ft-09-a" rel="me noopener" aria-label="Follow us on Bluesky — 31,900 followers">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true" focusable="false"><path d="M12 10.8C10.7 8.2 7.2 4.4 4.6 4.1 2.4 3.8 2 5.4 2 7v4.3c0 1.7.9 2.6 2.6 2.9 1 .2 2.2.2 3.2 0-2.4.4-4.6 1.4-1.6 4.6 3.3 3.4 4.6-.9 5.8-3.6 1.2 2.7 2.5 7 5.8 3.6 3-3.2.8-4.2-1.6-4.6 1 .2 2.2.2 3.2 0 1.7-.3 2.6-1.2 2.6-2.9V7c0-1.6-.4-3.2-2.6-2.9-2.6.3-6.1 4.1-7.4 6.7z"/></svg>
          <span class="ft-09__count">31.9k</span></a></li>
        <li><a class="ft-09__social" style="--ft-09-brand:oklch(0.7 0.16 300)" href="#ft-09-a" rel="me noopener" aria-label="Follow us on Mastodon — 12,400 followers">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true" focusable="false"><path d="M21.3 9c0-3.9-2.5-5-2.5-5C17.5 3.4 15.4 3.1 13.2 3h-.1c-2.2 0-4.3.3-5.6.9 0 0-2.5 1.1-2.5 5v3.4c0 4.4.3 8 4.4 9.1 1.9.5 3.5.6 4.8.5 2.4-.1 3.7-.8 3.7-.8l-.1-1.8s-1.7.6-3.7.5c-2-.1-4-.2-4.4-2.7l-.1-.8c3.6.9 6.7.4 7.6.3 2.4-.3 4.5-1.8 4.8-3.2.4-2.2.4-5.4.4-5.4zM18 13.5h-2.1V8.9c0-1-.4-1.5-1.2-1.5-.9 0-1.4.6-1.4 1.8v2.5h-2.1V9.2c0-1.2-.5-1.8-1.4-1.8-.8 0-1.2.5-1.2 1.5v4.6H6.4V8.7c0-1 .2-1.7.7-2.3.5-.6 1.2-.9 2-.9 1 0 1.7.4 2.2 1.1l.5.9.5-.9c.5-.7 1.2-1.1 2.2-1.1.8 0 1.5.3 2 .9.5.6.7 1.3.7 2.3z"/></svg>
          <span class="ft-09__count">12.4k</span></a></li>
        <li><a class="ft-09__social" style="--ft-09-brand:oklch(0.55 0.02 265)" href="#ft-09-a" rel="me noopener" aria-label="Follow us on GitHub — 9,800 stars">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true" focusable="false"><path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.7c-2.8.6-3.4-1.3-3.4-1.3-.5-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.5 2.4 1.1 3 .8.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.7 1a9.4 9.4 0 0 1 5 0c1.9-1.3 2.7-1 2.7-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.9-2.4 4.7-4.6 5 .4.3.7.9.7 1.9v2.8c0 .3.2.6.7.5A10 10 0 0 0 12 2z"/></svg>
          <span class="ft-09__count">9.8k</span></a></li>
        <li><a class="ft-09__social" style="--ft-09-brand:oklch(0.58 0.22 25)" href="#ft-09-a" rel="me noopener" aria-label="Subscribe on YouTube — 47,300 subscribers">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true" focusable="false"><path d="M22.5 7.2a2.7 2.7 0 0 0-1.9-1.9C18.9 4.8 12 4.8 12 4.8s-6.9 0-8.6.5A2.7 2.7 0 0 0 1.5 7.2 28 28 0 0 0 1 12a28 28 0 0 0 .5 4.8 2.7 2.7 0 0 0 1.9 1.9c1.7.5 8.6.5 8.6.5s6.9 0 8.6-.5a2.7 2.7 0 0 0 1.9-1.9A28 28 0 0 0 23 12a28 28 0 0 0-.5-4.8zM9.8 15.3V8.7l5.7 3.3z"/></svg>
          <span class="ft-09__count">47.3k</span></a></li>
        <li><a class="ft-09__social" style="--ft-09-brand:oklch(0.55 0.14 250)" href="#ft-09-a" rel="me noopener" aria-label="Follow us on LinkedIn — 22,100 followers">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true" focusable="false"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9.5 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.4c0-1.3-.02-3-1.83-3-1.83 0-2.11 1.43-2.11 2.9V21h-4z"/></svg>
          <span class="ft-09__count">22.1k</span></a></li>
      </ul>
    </div>
    <div class="ft-09__bar">
      <div class="ft-09__brand"><span class="ft-09__mark" aria-hidden="true"></span>Copperline</div>
      <nav class="ft-09__nav" aria-label="Footer"><a class="ft-09__link" href="#ft-09-a">Blog</a><a class="ft-09__link" href="#ft-09-a">Press kit</a><a class="ft-09__link" href="#ft-09-a">Community rules</a><a class="ft-09__link" href="#ft-09-a">Contact</a></nav>
      <p class="ft-09__copy">© <time datetime="2026">2026</time> Copperline</p>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-09-bg);
  --ft-09-bg: oklch(0.15 0.015 255);
  --ft-09-foot: oklch(0.19 0.018 255);
  --ft-09-ink: oklch(0.97 0.005 255);
  --ft-09-mut: oklch(0.73 0.015 255);
  --ft-09-acc: oklch(0.8 0.14 75);
  --ft-09-line: oklch(0.97 0.005 255/.13);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-09-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-09 *,
.ft-09 *::before,
.ft-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-09 ul {
  list-style: none;
}

.ft-09__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(40px,8vh,92px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1100px)/2));
  background: radial-gradient(75% 55% at 20% 0%,oklch(0.3 0.09 75/.35),transparent);
}

.ft-09__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-09-acc);
}

.ft-09__title {
  font-size: clamp(29px,5.4vw,58px);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-09__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-09-mut);
  max-width: 54ch;
  text-wrap: pretty;
}

.ft-09__foot {
  background: var(--ft-09-foot);
  border-top: 1px solid var(--ft-09-line);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1100px)/2));
}

.ft-09__cta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 24px 40px;
  padding-block: clamp(28px,4vw,44px);
}

.ft-09__h {
  font-size: clamp(20px,2.4vw,27px);
  font-weight: 690;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ft-09__sub2 {
  margin-block-start: 6px;
  font-size: 14.5px;
  line-height: 1.55;
  color: var(--ft-09-mut);
  max-width: 40ch;
  text-wrap: pretty;
}

.ft-09__socials {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-inline-start: auto;
}

.ft-09__social {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 48px;
  padding: 0 16px 0 14px;
  border-radius: 99px;
  border: 1px solid var(--ft-09-line);
  background: oklch(0.97 0.005 255/.04);
  color: var(--ft-09-ink);
  text-decoration: none;
  overflow: hidden;
  transition: transform .32s cubic-bezier(.34,1.56,.64,1),color .25s ease,border-color .25s ease,background .25s ease;
}

.ft-09__social::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(60% 120% at 50% 120%,var(--ft-09-brand),transparent 70%);
  opacity: 0;
  transition: opacity .3s ease;
}

.ft-09__social:hover,
.ft-09__social:focus-visible {
  transform: translateY(-3px);
  color: oklch(0.99 0.005 255);
  border-color: color-mix(in oklch,var(--ft-09-brand) 60%,transparent);
  background: color-mix(in oklch,var(--ft-09-brand) 16%,transparent);
}

.ft-09__social:hover::before {
  opacity: .28;
}

.ft-09__social:focus-visible {
  outline: 2px solid var(--ft-09-brand);
  outline-offset: 3px;
}

.ft-09__social svg {
  position: relative;
  flex: none;
  transition: transform .32s cubic-bezier(.34,1.56,.64,1);
}

.ft-09__social:hover svg {
  transform: scale(1.12) rotate(-4deg);
}

.ft-09__count {
  position: relative;
  font-size: 13px;
  font-weight: 650;
  font-variant-numeric: tabular-nums;
  color: var(--ft-09-mut);
  transition: color .25s ease;
}

.ft-09__social:hover .ft-09__count {
  color: oklch(0.99 0.005 255);
}

.ft-09__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px 24px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-09-line);
}

.ft-09__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ft-09__mark {
  width: 20px;
  height: 20px;
  border-radius: 6px;
  background: linear-gradient(140deg,var(--ft-09-acc),oklch(0.62 0.2 25));
}

.ft-09__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  margin-inline-start: auto;
}

.ft-09__link {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 11px;
  border-radius: 9px;
  font-size: 13.5px;
  color: var(--ft-09-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-09__link:hover {
  color: var(--ft-09-ink);
  background: oklch(0.97 0.005 255/.07);
}

.ft-09__link:focus-visible {
  outline: 2px solid var(--ft-09-acc);
  outline-offset: 2px;
}

.ft-09__copy {
  font-size: 13px;
  color: var(--ft-09-mut);
}

@media (max-width: 720px) {
  .ft-09__socials,
    .ft-09__nav {
    margin-inline-start: 0;
  }
}

@media (max-width: 420px) {
  .ft-09__count {
    display: none;
  }

  .ft-09__social {
    padding: 0 14px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-09 * {
    transition-duration: .01ms !important;
  }

  .ft-09__social:hover {
    transform: none;
  }
}
```
