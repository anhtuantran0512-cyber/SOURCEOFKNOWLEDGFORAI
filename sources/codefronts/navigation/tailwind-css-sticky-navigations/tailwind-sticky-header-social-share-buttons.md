---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-social-share-buttons/"
title: "Tailwind Sticky Header with Social Share Buttons"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "An article header that pins with real share actions: X, LinkedIn and Facebook links built from the page's canonical URL and title, a Copy link button with a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Header with Social Share Buttons
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-social-share-buttons/

An article header that pins with real share actions: X, LinkedIn and Facebook links built from the page's canonical URL and title, a Copy link button with a confirmation toast (and an execCommand fallback for sandboxed frames), and a native Share button that only appears where navigator.share exists. The story title slides into the bar once the headline scrolls away.
## HTML
```html
<div class="tsn-25 w-full min-h-svh bg-tsn25-bg font-tsn25-sans text-tsn25-ink antialiased" aria-label="Sticky header with social share icons demo">
  <header data-tsn25-header data-url="https://example.com/journal/sticky-headers-that-respect-readers" data-title="Sticky headers that respect readers" class="group/hdr sticky top-0 z-40 border-b border-tsn25-line bg-tsn25-bg/90 backdrop-blur-xl">
    <div class="flex h-16 items-center gap-4 px-[max(1.25rem,calc((100%-72rem)/2))]">
      <a href="#tsn-25-top" class="flex min-h-11 flex-none items-center rounded font-tsn25-serif text-2xl italic focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn25-acc">Margins</a>
      <p aria-hidden="true" class="min-w-0 flex-1 translate-y-2 truncate text-sm font-medium text-tsn25-mut opacity-0 transition duration-300 group-data-scrolled/hdr:translate-y-0 group-data-scrolled/hdr:opacity-100 motion-reduce:transition-none max-md:hidden">Sticky headers that respect readers</p>
      <div role="group" aria-label="Share this article" class="ms-auto flex flex-none items-center gap-0.5">
        <a data-tsn25-share="x" href="#" target="_blank" rel="noopener noreferrer" class="group/s relative grid size-11 place-items-center rounded-full text-tsn25-mut transition-colors hover:bg-tsn25-ink/5 hover:text-tsn25-ink focus-visible:outline-2 focus-visible:outline-tsn25-acc "><span class="sr-only">Share on X (opens in a new tab)</span><svg class="size-[18px]" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg><span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+6px)] left-1/2 -translate-x-1/2 translate-y-1 whitespace-nowrap rounded-md bg-tsn25-ink px-2 py-1 text-[11px] font-medium text-tsn25-bg opacity-0 transition group-hover/s:translate-y-0 group-hover/s:opacity-100 group-focus-visible/s:translate-y-0 group-focus-visible/s:opacity-100">Share on X</span></a>
        <a data-tsn25-share="li" href="#" target="_blank" rel="noopener noreferrer" class="group/s relative grid size-11 place-items-center rounded-full text-tsn25-mut transition-colors hover:bg-tsn25-ink/5 hover:text-tsn25-ink focus-visible:outline-2 focus-visible:outline-tsn25-acc max-[380px]:hidden"><span class="sr-only">Share on LinkedIn (opens in a new tab)</span><svg class="size-[18px]" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg><span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+6px)] left-1/2 -translate-x-1/2 translate-y-1 whitespace-nowrap rounded-md bg-tsn25-ink px-2 py-1 text-[11px] font-medium text-tsn25-bg opacity-0 transition group-hover/s:translate-y-0 group-hover/s:opacity-100 group-focus-visible/s:translate-y-0 group-focus-visible/s:opacity-100">Share on LinkedIn</span></a>
        <a data-tsn25-share="fb" href="#" target="_blank" rel="noopener noreferrer" class="group/s relative grid size-11 place-items-center rounded-full text-tsn25-mut transition-colors hover:bg-tsn25-ink/5 hover:text-tsn25-ink focus-visible:outline-2 focus-visible:outline-tsn25-acc max-[420px]:hidden"><span class="sr-only">Share on Facebook (opens in a new tab)</span><svg class="size-[18px]" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M24 12.07C24 5.41 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.04V9.41c0-3.02 1.8-4.7 4.54-4.7 1.31 0 2.68.24 2.68.24v2.97h-1.5c-1.5 0-1.96.93-1.96 1.89v2.26h3.32l-.53 3.5h-2.8V24C19.62 23.1 24 18.1 24 12.07"/></svg><span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+6px)] left-1/2 -translate-x-1/2 translate-y-1 whitespace-nowrap rounded-md bg-tsn25-ink px-2 py-1 text-[11px] font-medium text-tsn25-bg opacity-0 transition group-hover/s:translate-y-0 group-hover/s:opacity-100 group-focus-visible/s:translate-y-0 group-focus-visible/s:opacity-100">Share on Facebook</span></a>
        <button type="button" data-tsn25-copy class="group/c relative inline-flex min-h-11 items-center gap-2 rounded-full border border-tsn25-line px-3.5 text-[13px] font-semibold transition-colors hover:border-tsn25-ink focus-visible:outline-2 focus-visible:outline-tsn25-acc data-copied:border-tsn25-acc data-copied:bg-tsn25-acc data-copied:text-white">
          <span class="grid size-4 place-items-center"><svg class="size-4 group-data-copied/c:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M10 14a5 5 0 0 0 7.07 0l3-3a5 5 0 0 0-7.07-7.07l-1.5 1.5"/><path d="M14 10a5 5 0 0 0-7.07 0l-3 3a5 5 0 0 0 7.07 7.07l1.5-1.5"/></svg><svg class="hidden size-4 group-data-copied/c:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12 5 5 9-10"/></svg></span>
          <span class="group-data-copied/c:hidden">Copy link</span><span class="hidden group-data-copied/c:inline">Copied</span>
        </button>
        <button type="button" data-tsn25-native hidden class="inline-flex min-h-11 items-center gap-2 rounded-full bg-tsn25-ink px-3.5 text-[13px] font-semibold text-tsn25-bg hover:bg-tsn25-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn25-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3v13M7 8l5-5 5 5"/><path d="M5 14v5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5"/></svg><span class="max-sm:sr-only">Share</span></button>
      </div>
    </div>
    <p data-tsn25-status role="status" class="sr-only"></p>
  </header>
  <div id="tsn-25-top"></div>
  <div class="px-[max(1.25rem,calc((100%-44rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn25-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn25-acc">Essay · Interface design</p>
    <h1 class="mt-4 max-w-[18ch] font-tsn25-serif text-[clamp(44px,7vw,80px)] font-normal leading-[0.98] tracking-[-0.015em] text-balance">Sticky headers that respect readers</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn25-mut text-pretty">Every share action in the bar above is real. Copy the link, open a share intent, or — on a phone — use the native share sheet. The title joins the bar once this headline leaves.</p>
  </div>
  <main id="tsn-25-main" class="px-[max(1.25rem,calc((100%-44rem)/2))] grid pb-24">
    <section id="tsn-25-s1" class="scroll-mt-24 min-h-[48svh] border-t border-tsn25-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-25-h1">
      <p class="font-tsn25-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn25-acc">Links</p>
      <h2 id="tsn-25-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Built from the canonical URL</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn25-mut text-pretty">The header carries <code class="rounded-md bg-tsn25-acc/10 px-1.5 py-0.5 font-tsn25-mono text-[0.86em] text-tsn25-ink">data-url</code> and <code class="rounded-md bg-tsn25-acc/10 px-1.5 py-0.5 font-tsn25-mono text-[0.86em] text-tsn25-ink">data-title</code>. The script encodes both into each network’s current share intent, so copied pages never share the wrong address.</p>
    </section>
    <section id="tsn-25-s2" class="scroll-mt-24 min-h-[48svh] border-t border-tsn25-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-25-h2">
      <p class="font-tsn25-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn25-acc">Native</p>
      <h2 id="tsn-25-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">The OS knows best</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn25-mut text-pretty">Where <code class="rounded-md bg-tsn25-acc/10 px-1.5 py-0.5 font-tsn25-mono text-[0.86em] text-tsn25-ink">navigator.share</code> exists, a Share button appears and opens the system sheet — Messages, Mail, Notes, whatever the reader actually uses.</p>
    </section>
    <section id="tsn-25-s3" class="scroll-mt-24 min-h-[48svh] border-t border-tsn25-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-25-h3">
      <p class="font-tsn25-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn25-acc">Copy</p>
      <h2 id="tsn-25-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Confirmed twice</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn25-mut text-pretty">Copy link swaps to a filled “Copied” state for 1.8 seconds and announces “Link copied” through a live region. In sandboxed frames it falls back to <code class="rounded-md bg-tsn25-acc/10 px-1.5 py-0.5 font-tsn25-mono text-[0.86em] text-tsn25-ink">execCommand</code>.</p>
    </section>
    <section id="tsn-25-s4" class="scroll-mt-24 min-h-[48svh] border-t border-tsn25-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-25-h4">
      <p class="font-tsn25-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn25-acc">Restraint</p>
      <h2 id="tsn-25-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Fewer icons, on purpose</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn25-mut text-pretty">On narrow phones Facebook and then LinkedIn step aside; Copy link and native Share cover every other destination without crowding the bar.</p>
    </section>
  </main>
  <footer class="border-t border-tsn25-line px-[max(1.25rem,calc((100%-44rem)/2))] py-10 font-tsn25-mono text-xs text-tsn25-mut">Tailwind sticky navigation · pattern 25 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn25-bg: #fbfaf7;
  --color-tsn25-bg: oklch(0.984 0.005 90);
  --color-tsn25-surface: #ffffff;
  --color-tsn25-surface: oklch(1 0 0);
  --color-tsn25-ink: #1a1817;
  --color-tsn25-ink: oklch(0.21 0.005 50);
  --color-tsn25-mut: #5c5753;
  --color-tsn25-mut: oklch(0.46 0.01 50);
  --color-tsn25-acc: #e0533d;
  --color-tsn25-acc: oklch(0.63 0.18 33);
  --color-tsn25-line: #1a18171a;
  --color-tsn25-line: oklch(0.21 0.005 50 / 0.1);
  --font-tsn25-serif: 'Instrument Serif', Georgia, serif;
  --font-tsn25-sans: 'Geist', system-ui, sans-serif;
  --font-tsn25-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-25 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-25) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  const copyText = async (text) => {
    try { await navigator.clipboard.writeText(text); return true; }
    catch (e) {
      const ta = Object.assign(document.createElement('textarea'), { value: text });
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;opacity:0';
      document.body.append(ta);
      ta.select();
      const ok = document.execCommand('copy');
      ta.remove();
      return ok;
    }
  };
  document.querySelectorAll('.tsn-25').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn25-header]');
    const url = encodeURIComponent(hdr.dataset.url);
    const title = encodeURIComponent(hdr.dataset.title);
    const urls = {
      x: 'https://x.com/intent/post?url=' + url + '&text=' + title,
      li: 'https://www.linkedin.com/sharing/share-offsite/?url=' + url,
      fb: 'https://www.facebook.com/sharer/sharer.php?u=' + url,
    };
    root.querySelectorAll('[data-tsn25-share]').forEach((a) => { a.href = urls[a.dataset.tsn25Share]; });
    const status = root.querySelector('[data-tsn25-status]');
    const copy = root.querySelector('[data-tsn25-copy]');
    let t = 0;
    copy.addEventListener('click', async () => {
      const ok = await copyText(hdr.dataset.url);
      clearTimeout(t);
      if (ok) { copy.setAttribute('data-copied', ''); status.textContent = 'Link copied'; }
      else status.textContent = 'Copy failed. Select the address bar instead.';
      t = setTimeout(() => { copy.removeAttribute('data-copied'); status.textContent = ''; }, 1800);
    });
    const native = root.querySelector('[data-tsn25-native]');
    if (navigator.share) {
      native.hidden = false;
      native.addEventListener('click', () => {
        navigator.share({ title: hdr.dataset.title, url: hdr.dataset.url }).catch(() => {});
      });
    }
    let queued = false;
    const tick = () => { queued = false; hdr.toggleAttribute('data-scrolled', window.scrollY > 320); };
    window.addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(tick); } }, { passive: true });
    tick();
  });
})();
```
