---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/social-share-buttons-with-intent-urls/"
title: "Social Share Buttons with Intent URLs"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "Share links that are just links: each anchor points at a platform intent endpoint with the title and URL already encoded into the query string, so the whole…"
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social Share Buttons with Intent URLs
Source: https://codefronts.com/snippets/css-social-buttons/social-share-buttons-with-intent-urls/

Share links that are just links: each anchor points at a platform intent endpoint with the title and URL already encoded into the query string, so the whole row works with JavaScript switched off. The demo shows which parameter each platform actually reads — they disagree, and sending the wrong one silently drops your copy.
## HTML
```html
<div class="soc-07">
  <div class="soc-07__stage">
    <div class="soc-07__card">
      <p class="soc-07__eyebrow">Share this post</p>
      <h2 class="soc-07__title">Why your design tokens keep drifting</h2>
      <ul class="soc-07__grid">
        <li><a class="soc-07__btn" style="--brand:#0f1419" href="https://x.com/intent/post?text=Why%20your%20design%20tokens%20keep%20drifting&amp;url=https%3A%2F%2Fexample.com%2Ftokens" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg>
          <span class="soc-07__name">Post on X</span>
          <code class="soc-07__param">text + url</code>
        </a></li>
        <li><a class="soc-07__btn" style="--brand:#0a66c2" href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fexample.com%2Ftokens" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg>
          <span class="soc-07__name">Share on LinkedIn</span>
          <code class="soc-07__param">url only</code>
        </a></li>
        <li><a class="soc-07__btn" style="--brand:#1877f2" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fexample.com%2Ftokens" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><path d="M14.6 8.2h-1.3a1.9 1.9 0 0 0-1.9 1.9v6.3"/><path d="M9.9 12.4h4.2"/></svg>
          <span class="soc-07__name">Share on Facebook</span>
          <code class="soc-07__param">u only</code>
        </a></li>
        <li><a class="soc-07__btn" style="--brand:#ff4500" href="https://www.reddit.com/submit?url=https%3A%2F%2Fexample.com%2Ftokens&amp;title=Why%20your%20design%20tokens%20keep%20drifting" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="7.4"/><circle cx="9.4" cy="12.4" r=".95" fill="currentColor" stroke="none"/><circle cx="14.6" cy="12.4" r=".95" fill="currentColor" stroke="none"/><path d="M9.3 15.6a4.2 4.2 0 0 0 5.4 0"/><path d="M12 5.6 13.4 3"/></svg>
          <span class="soc-07__name">Post to Reddit</span>
          <code class="soc-07__param">url + title</code>
        </a></li>
      </ul>
      <p class="soc-07__foot">Values are encoded per parameter with encodeURIComponent — never encode the assembled string.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.soc-07 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
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
  .soc-07 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-07:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
  }
}

.soc-07[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
}

.soc-07,
.soc-07 *,
.soc-07 *::before,
.soc-07 *::after {
  box-sizing: border-box;
}

.soc-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-07__card {
  inline-size: min(38rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-07__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-07__title {
  margin: 0 0 1.5rem;
  font-size: clamp(1.1rem,1rem + .9vw,1.4rem);
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.soc-07__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
  gap: .6rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.soc-07__btn {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .65rem;
  min-block-size: 3.25rem;
  padding: 0 .9rem;
  min-inline-size: 0;
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  color: var(--fg);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 550;
  transition: border-color .2s ease, background-color .2s ease, color .2s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.soc-07__btn svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
  color: var(--muted);
  transition: color .2s ease;
}

.soc-07__name {
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.soc-07__param {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: -.01em;
  color: var(--muted);
  background: color-mix(in oklab,var(--fg) 5%,var(--surface));
  border: 1px solid var(--line);
  border-radius: .4rem;
  padding: .15rem .35rem;
  white-space: nowrap;
}

.soc-07__btn:hover {
  translate: 0 -2px;
  color: var(--brand);
  border-color: color-mix(in oklab,var(--brand) 42%,var(--line));
  background: color-mix(in oklab,var(--brand) 7%,var(--surface));
}

.soc-07__btn:hover svg {
  color: var(--brand);
}

.soc-07__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-07__foot {
  margin: 1.4rem 0 0;
  font-size: .78rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .soc-07__btn {
    transition-duration: 1ms;
  }

  .soc-07__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-07__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .soc-07__btn:hover {
    background: Highlight;
    color: HighlightText;
  }
}
```
