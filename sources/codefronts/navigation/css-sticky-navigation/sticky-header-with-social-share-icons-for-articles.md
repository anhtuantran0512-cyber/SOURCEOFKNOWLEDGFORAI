---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-social-share-icons-for-articles/"
title: "Sticky Header with Social Share Icons for Articles"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "Publishers put share actions in the sticky chrome because the moment a reader decides to pass an article on is unpredictable."
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header with Social Share Icons for Articles
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-social-share-icons-for-articles/

Publishers put share actions in the sticky chrome because the moment a reader decides to pass an article on is unpredictable. This build keeps a share cluster in the header, adds a vertical rail that appears once the hero is behind the reader, folds to a thumb-reachable bar on phones, and does it without loading a single third-party widget.
## HTML
```html
<section class="sn-25" aria-label="Sticky header with social share icons demo">
    <header class="sn-25__bar">
      <a class="sn-25__brand" href="#sn-25-hero"><span class="sn-25__logo" aria-hidden="true"></span>The Longform</a>
      <nav class="sn-25__nav" aria-label="Primary">
        <a class="sn-25__link" href="#sn-25-s1" aria-current="page">Essays</a>
        <a class="sn-25__link" href="#sn-25-s2">Field notes</a>
      </nav>
      <div class="sn-25__cluster" role="group" aria-label="Share this article">
        <button class="sn-25__ico" type="button" id="sn-25-share" aria-label="Share this article">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 15V4m0 0L8.2 7.8M12 4l3.8 3.8M5 13v5.5A1.5 1.5 0 0 0 6.5 20h11a1.5 1.5 0 0 0 1.5-1.5V13" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <button class="sn-25__ico" type="button" id="sn-25-copy" aria-label="Copy link to this article">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M10.5 13.5a3.6 3.6 0 0 0 5.1 0l2.6-2.6a3.6 3.6 0 0 0-5.1-5.1l-1.2 1.2m2.6 4a3.6 3.6 0 0 0-5.1 0l-2.6 2.6a3.6 3.6 0 0 0 5.1 5.1l1.2-1.2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </button>
        <button class="sn-25__ico" type="button" id="sn-25-save" aria-label="Save this article" aria-pressed="false">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 4h10v16l-5-3.6L7 20V4Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </header>
    <div class="sn-25__hero" id="sn-25-hero">
      <img class="sn-25__img" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=1400&auto=format&fit=crop" alt="Mist drifting through a pine forest on a hillside" width="1400" height="800" loading="lazy" decoding="async">
      <div class="sn-25__herotext">
        <p class="sn-25__kicker">Field report · 14 min</p>
        <h2 class="sn-25__htitle">What the quiet hours in a forest measure</h2>
      </div>
    </div>
    <div class="sn-25__layout">
      <aside class="sn-25__rail" id="sn-25-rail" aria-label="Share actions">
        <button class="sn-25__ricon" type="button" data-net="X" aria-label="Share on X">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 5l14 14M19 5 5 19" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        </button>
        <button class="sn-25__ricon" type="button" data-net="LinkedIn" aria-label="Share on LinkedIn">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 10v9M6 6.4v.1M11 19v-5a3 3 0 0 1 6 0v5" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        </button>
        <button class="sn-25__ricon" type="button" data-net="email" aria-label="Share by email">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16v10H4V7Zm0 .4 8 5.4 8-5.4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <span class="sn-25__rdiv" aria-hidden="true"></span>
        <button class="sn-25__ricon" type="button" id="sn-25-copy2" aria-label="Copy link to this article">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M10.5 13.5a3.6 3.6 0 0 0 5.1 0l2.6-2.6a3.6 3.6 0 0 0-5.1-5.1l-1.2 1.2m2.6 4a3.6 3.6 0 0 0-5.1 0l-2.6 2.6a3.6 3.6 0 0 0 5.1 5.1l1.2-1.2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </button>
      </aside>
      <article class="sn-25__article">
        <section class="sn-25__sec" id="sn-25-s1">
          <p class="sn-25__p sn-25__p--lede">The rail beside this column is not present when the page loads. It arrives once the hero has scrolled past, because nobody shares an article they have not started.</p>
          <p class="sn-25__p">Sticky share actions are a publishing convention for a practical reason: the moment a reader decides to pass something on is unpredictable, and asking them to scroll back to a byline loses most of them.</p>
        </section>
        <section class="sn-25__sec" id="sn-25-s2">
          <h3 class="sn-25__h">Copying is the action that matters</h3>
          <p class="sn-25__p">Most shares are a pasted link, not a platform button. <code>navigator.clipboard.writeText()</code> handles it in one line, needs a secure context and a real user gesture, and deserves a fallback for everything else.</p>
          <p class="sn-25__p">Confirmation is announced through a live region rather than shown as a fading tick, so the result reaches a screen reader as reliably as it reaches an eye.</p>
        </section>
        <section class="sn-25__sec" id="sn-25-s3">
          <h3 class="sn-25__h">Names, not glyphs</h3>
          <p class="sn-25__p">Each button in the rail is 44px of hit area around an 18px icon, and each one carries a name that says where the link is going. Without it, assistive tech announces four identical buttons.</p>
          <p class="sn-25__p">On touch devices the header's first button upgrades itself to the operating system's own share sheet when the API is present — the same markup, a better destination list.</p>
        </section>
      </article>
    </div>
    <p class="sn-25__status" id="sn-25-status" role="status"></p>
  <footer class="sn-25__pagefoot">
    <p class="sn-25__pagefootin">Sticky navigation pattern 25 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-25-bg);
  --sn-25-bg: oklch(0.19 0.014 285);
  --sn-25-surface: oklch(0.235 0.016 285);
  --sn-25-ink: oklch(0.97 0.005 285);
  --sn-25-mut: oklch(0.71 0.016 285);
  --sn-25-acc: oklch(0.8 0.14 88);
  --sn-25-line: oklch(1 0 0/.12);
  --sn-25-h: 60px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-25-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-25 *,
.sn-25 *::before,
.sn-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-25__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,20px);
  min-height: var(--sn-25-h);
  padding: 0 clamp(12px,2.4vw,20px);
  background: color-mix(in oklch,var(--sn-25-surface) 86%,transparent);
  backdrop-filter: blur(16px) saturate(1.5);
  -webkit-backdrop-filter: blur(16px) saturate(1.5);
  border-bottom: 1px solid var(--sn-25-line);
}

.sn-25__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.03em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-25__logo {
  width: 8px;
  height: 20px;
  border-radius: 2px;
  background: var(--sn-25-acc);
}

.sn-25__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: 8px;
}

.sn-25__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 11px;
  border-radius: 8px;
  font-size: 13.2px;
  font-weight: 600;
  color: var(--sn-25-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-25__link:hover {
  color: var(--sn-25-ink);
  background: oklch(1 0 0/.06);
}

.sn-25__link[aria-current="page"] {
  color: var(--sn-25-acc);
}

.sn-25__cluster {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-25__ico,
.sn-25__ricon {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 0;
  border-radius: 11px;
  background: transparent;
  color: var(--sn-25-mut);
  cursor: pointer;
  transition: color .2s ease,background .2s ease,transform .2s ease;
}

.sn-25__ico svg,
.sn-25__ricon svg {
  inline-size: 18px;
  block-size: 18px;
}

.sn-25__ico:hover,
.sn-25__ricon:hover {
  color: var(--sn-25-ink);
  background: oklch(1 0 0/.08);
}

.sn-25__ico:active,
.sn-25__ricon:active {
  transform: scale(.93);
}

.sn-25__ico[data-done="true"],
.sn-25__ricon[data-done="true"] {
  color: var(--sn-25-acc);
  background: color-mix(in oklch,var(--sn-25-acc) 15%,transparent);
}

.sn-25__ico[aria-pressed="true"] {
  color: var(--sn-25-acc);
}

.sn-25__ico:focus-visible,
.sn-25__ricon:focus-visible,
.sn-25__link:focus-visible,
.sn-25__brand:focus-visible {
  outline: 2px solid var(--sn-25-acc);
  outline-offset: 2px;
}

.sn-25__hero {
  position: relative;
  block-size: min(46svh,300px);
  overflow: hidden;
  background: linear-gradient(150deg,oklch(0.42 0.06 150),oklch(0.24 0.03 260));
}

.sn-25__img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
}

.sn-25__herotext {
  position: absolute;
  inset-block-end: 0;
  inset-inline: 0;
  display: grid;
  gap: 8px;
  padding: clamp(18px,3.4vw,30px);
  background: linear-gradient(to top,oklch(0.14 0.012 285/.94),transparent);
}

.sn-25__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-25-acc);
}

.sn-25__htitle {
  font-size: clamp(21px,3.2vw,31px);
  line-height: 1.1;
  letter-spacing: -.035em;
  font-weight: 730;
  max-width: 22ch;
  text-wrap: balance;
}

.sn-25__layout {
  display: grid;
  grid-template-columns: 60px minmax(0,1fr);
  gap: clamp(10px,2vw,22px);
  padding: clamp(18px,3vw,30px) clamp(16px,3vw,28px) 8px;
}

.sn-25__rail {
  grid-column: 1;
  align-self: start;
  position: sticky;
  top: calc(var(--sn-25-h) + 18px);
  display: grid;
  justify-items: center;
  gap: 2px;
  padding: 6px 4px;
  border: 1px solid var(--sn-25-line);
  border-radius: 16px;
  background: oklch(1 0 0/.03);
  opacity: 0;
  translate: -8px 0;
  pointer-events: none;
  transition: opacity .4s ease,translate .4s cubic-bezier(.32,.72,.3,1);
}

.sn-25[data-past="true"] .sn-25__rail {
  opacity: 1;
  translate: 0 0;
  pointer-events: auto;
}

.sn-25__rdiv {
  inline-size: 20px;
  block-size: 1px;
  background: var(--sn-25-line);
  margin-block: 4px;
}

.sn-25__article {
  grid-column: 2;
  min-width: 0;
  max-width: 62ch;
}

.sn-25__sec {
  scroll-margin-top: calc(var(--sn-25-h) + 12px);
  display: grid;
  gap: 12px;
  padding-block: clamp(16px,3vw,26px);
  border-bottom: 1px solid var(--sn-25-line);
}

.sn-25__sec:last-child {
  border-bottom: 0;
}

.sn-25__h {
  font-size: 18px;
  line-height: 1.2;
  letter-spacing: -.025em;
  font-weight: 690;
}

.sn-25__p {
  font-size: 15px;
  line-height: 1.72;
  color: var(--sn-25-mut);
  text-wrap: pretty;
}

.sn-25__p--lede {
  font-size: 16.5px;
  color: var(--sn-25-ink);
}

.sn-25__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

.sn-25__status {
  min-block-size: 34px;
  padding: 0 clamp(16px,3vw,28px) 14px;
  font-size: 12.8px;
  color: var(--sn-25-acc);
}

@media (max-width: 720px) {
  .sn-25__layout {
    grid-template-columns: minmax(0,1fr);
  }

  .sn-25__article {
    grid-column: 1;
  }

  .sn-25__rail {
    grid-column: 1;
    grid-row: 2;
    position: sticky;
    top: auto;
    bottom: 8px;
    display: flex;
    justify-content: center;
    justify-self: center;
    translate: 0 10px;
    border-radius: 99px;
    background: color-mix(in oklch,var(--sn-25-surface) 92%,transparent);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    z-index: 20;
  }

  .sn-25[data-past="true"] .sn-25__rail {
    translate: 0 0;
  }

  .sn-25__rdiv {
    inline-size: 1px;
    block-size: 20px;
    margin: 0 4px;
  }

  .sn-25__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-25__rail {
    transition: opacity .01ms;
  }

  .sn-25 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-25) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-25-h) + 12px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-25) {
    scroll-behavior: auto;
  }
}

.sn-25__bar,
.sn-25__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-25__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-25__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-25-line);
}

.sn-25__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-25-mut);
  text-align: center;
}

.sn-25__intro-title,
.sn-25__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-25');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const status = root.querySelector('#sn-25-status');
  const url = 'https://codefronts.com/sticky-navigation/social-share';
  const title = 'What the quiet hours in a forest measure';
  const say = (msg) => { status.textContent = msg; };
  const flash = (btn) => { btn.dataset.done = 'true'; setTimeout(() => { delete btn.dataset.done; }, 1600); };
  const copy = async (btn) => {
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(url);
      else throw new Error('fallback');
      say('Link copied to the clipboard');
    } catch (err) {
      const tmp = document.createElement('input');
      tmp.value = url; tmp.setAttribute('readonly', '');
      tmp.style.cssText = 'position:absolute;opacity:0;pointer-events:none';
      root.appendChild(tmp); tmp.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      tmp.remove();
      say(ok ? 'Link copied to the clipboard' : 'Copy blocked here — the link is ' + url);
    }
    flash(btn);
  };
  root.querySelectorAll('#sn-25-copy, #sn-25-copy2').forEach((b) => b.addEventListener('click', () => copy(b)));
  const share = root.querySelector('#sn-25-share');
  share.addEventListener('click', async () => {
    if (navigator.share) {
      try { await navigator.share({ title, url }); say('Share sheet opened'); return; } catch (e) { say('Share dismissed'); return; }
    }
    copy(share);
  });
  const save = root.querySelector('#sn-25-save');
  save.addEventListener('click', () => {
    const on = save.getAttribute('aria-pressed') !== 'true';
    save.setAttribute('aria-pressed', String(on));
    say(on ? 'Saved to your reading list' : 'Removed from your reading list');
  });
  root.querySelectorAll('.sn-25__ricon[data-net]').forEach((b) => b.addEventListener('click', () => {
    say('Opening ' + b.dataset.net + ' with this article — replace with the real intent URL in production');
    flash(b);
  }));
  const io = new IntersectionObserver(([e]) => { root.dataset.past = String(!e.isIntersecting); },
    { root: null, rootMargin: '-70px 0px 0px 0px', threshold: 0 });
  io.observe(root.querySelector('#sn-25-hero'));
})();
```
