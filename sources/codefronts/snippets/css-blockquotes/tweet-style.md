---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/tweet-style/"
title: "Twitter / X Card Style CSS Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "A social-post quote card that looks like a native embed but ships as pure HTML/CSS — no third-party script, no tracking pixel, no layout-shifting iframe (the…"
has_js: "true"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Twitter / X Card Style CSS Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/tweet-style/

A social-post quote card that looks like a native embed but ships as pure HTML/CSS — no third-party script, no tracking pixel, no layout-shifting iframe (the real embed script pulls ~100KB and phones home). Semantically it's still a <blockquote> with a cite link to the original post, so it degrades to a correct citation with CSS off. Verified badge, engagement row and timestamp are all in place, plus a 12-line JS bonus that renders the timestamp as '3h ago' relative time.
## HTML
```html
<section class="bq-19" aria-label="Social post card blockquote demo">
  <div class="bq-19__stage">
    <blockquote class="bq-19__post" cite="https://example.social/webfoundry/status/91442">
      <header class="bq-19__head">
        <img class="bq-19__ava" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=120&auto=format&fit=crop" alt="" width="44" height="44" loading="lazy">
        <div class="bq-19__id">
          <p class="bq-19__name">Web Foundry <svg class="bq-19__badge" viewBox="0 0 22 22" aria-label="Verified account" role="img"><path d="M11 1.6l2.4 1.8 3-.2 1 2.9 2.5 1.6-.9 2.9.9 2.9-2.5 1.6-1 2.9-3-.2-2.4 1.8-2.4-1.8-3 .2-1-2.9L2.1 14l.9-2.9-.9-2.9 2.5-1.6 1-2.9 3 .2z" fill="currentColor"/><path d="M7.4 11.2l2.5 2.5 4.7-5" fill="none" stroke="oklch(0.16 0.01 250)" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></p>
          <p class="bq-19__handle">@webfoundry</p>
        </div>
        <span class="bq-19__x" aria-hidden="true">✕</span>
      </header>
      <p class="bq-19__body">Hot take: the fastest social embed is no embed. A styled &lt;blockquote&gt; with a cite link loads in 3KB, ships zero trackers, and your CLS graph goes flat. The official script is a 100KB iframe you're renting.</p>
      <footer class="bq-19__foot">
        <a class="bq-19__time" href="https://example.social/webfoundry/status/91442" data-bq19-time="2026-08-05T09:14:00Z">9:14 AM · Aug 5, 2026</a>
        <ul class="bq-19__actions" aria-label="Engagement">
          <li><button type="button" class="bq-19__act bq-19__act--reply" aria-label="612 replies"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path d="M12 3.5c-4.9 0-8.8 3.4-8.8 7.7 0 4.2 3.9 7.6 8.8 7.6.6 0 1.2 0 1.7-.1l4.6 2.3-1-3.9c2.1-1.4 3.5-3.5 3.5-5.9 0-4.3-3.9-7.7-8.8-7.7z" fill="none" stroke="currentColor" stroke-width="1.7"/></svg><span>612</span></button></li>
          <li><button type="button" class="bq-19__act bq-19__act--rt" aria-label="2,148 reposts"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path d="M7 5.5h7a3 3 0 0 1 3 3v2M17 18.5h-7a3 3 0 0 1-3-3v-2" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M14.5 3l3 2.5-3 2.5M9.5 21l-3-2.5 3-2.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span>2,148</span></button></li>
          <li><button type="button" class="bq-19__act bq-19__act--like" aria-label="9,802 likes"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path d="M12 20s-7.5-4.6-9.3-9.3C1.5 7.5 3.6 4.5 6.7 4.5c2 0 3.7 1.1 4.6 2.8h1.4c.9-1.7 2.6-2.8 4.6-2.8 3.1 0 5.2 3 4 6.2C19.5 15.4 12 20 12 20z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg><span>9,802</span></button></li>
        </ul>
      </footer>
    </blockquote>
    <p class="bq-19__chip" aria-hidden="true">3KB vs 100KB embed · cite attribute · tabular-nums</p>
  </div>
</section>
```
## CSS
```css
.bq-19,
.bq-19 *,
.bq-19 *::before,
.bq-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.19 0.015 250);
  --card: oklch(0.16 0.01 250);
  --ink: oklch(0.95 0.005 250);
  --mut: oklch(0.6 0.015 250);
  --line: oklch(0.32 0.015 250);
  --blue: oklch(0.68 0.14 240);
  --green: oklch(0.7 0.15 155);
  --pink: oklch(0.68 0.19 0);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-19__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 55% at 50% 0%,oklch(0.23 0.03 255/.7),transparent),var(--bg);
  overflow-y: auto;
}

.bq-19__post {
  width: min(100%,500px);
  padding: 18px 20px 12px;
  border-radius: 16px;
  background: var(--card);
  border: 1px solid var(--line);
}

.bq-19__head {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 11px;
}

.bq-19__ava {
  width: 44px;
  height: 44px;
  border-radius: 99px;
  object-fit: cover;
  background: linear-gradient(135deg,oklch(0.5 0.1 240),oklch(0.4 0.08 280));
}

.bq-19__id {
  min-width: 0;
}

.bq-19__name {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 15px;
  font-weight: 750;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.bq-19__badge {
  width: 1.15em;
  height: 1.15em;
  color: var(--blue);
  flex: none;
}

.bq-19__handle {
  font-size: 13.5px;
  color: var(--mut);
}

.bq-19__x {
  font-size: 15px;
  color: var(--mut);
  align-self: start;
}

.bq-19__body {
  margin-top: 12px;
  font-size: 15.5px;
  line-height: 1.55;
  text-wrap: pretty;
}

.bq-19__foot {
  margin-top: 12px;
}

.bq-19__time {
  display: inline-block;
  font-size: 13px;
  color: var(--mut);
  text-decoration: none;
  padding-block: 6px;
}

.bq-19__time:hover,
.bq-19__time:focus-visible {
  text-decoration: underline;
  color: var(--ink);
}

.bq-19__time:focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
  border-radius: 4px;
}

.bq-19__actions {
  display: flex;
  justify-content: space-between;
  max-width: 320px;
  list-style: none;
  margin-top: 4px;
  border-top: 1px solid var(--line);
  padding-top: 4px;
}

.bq-19__act {
  --tone: var(--mut);
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 10px;
  border: 0;
  background: none;
  border-radius: 99px;
  color: var(--mut);
  font-size: 13px;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: color .2s,background .2s;
}

.bq-19__act:hover,
.bq-19__act:focus-visible {
  color: var(--tone);
  background: color-mix(in oklch,var(--tone) 12%,transparent);
}

.bq-19__act:focus-visible {
  outline: 2px solid var(--tone);
  outline-offset: -2px;
}

.bq-19__act--reply {
  --tone: var(--blue);
}

.bq-19__act--rt {
  --tone: var(--green);
}

.bq-19__act--like {
  --tone: var(--pink);
}

.bq-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid var(--line);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .bq-19 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const rtf = new Intl.RelativeTimeFormat(undefined, { numeric: 'auto' });
  document.querySelectorAll('[data-bq19-time]').forEach((a) => {
    if (a.dataset.wired) return;
    a.dataset.wired = '1';
    const then = new Date(a.dataset.bq19Time).getTime();
    if (Number.isNaN(then)) return;
    const mins = Math.round((then - Date.now()) / 60000);
    const [v, u] = Math.abs(mins) < 60 ? [mins, 'minute']
      : Math.abs(mins) < 1440 ? [Math.round(mins / 60), 'hour']
      : [Math.round(mins / 1440), 'day'];
    a.textContent = rtf.format(v, u) + ' · ' + a.textContent;
  });
})();
```
