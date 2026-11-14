---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/comment-thread/"
title: "Comment Thread Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "Threads load after the post, so the skeleton sits under real content and has to match its rhythm exactly."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Comment Thread Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/comment-thread/

Threads load after the post, so the skeleton sits under real content and has to match its rhythm exactly. Three comment shells — avatar, name, meta, three text lines — plus one indented reply, all built from a real <ul> with the same indent and vertical spacing the resolved thread uses.
## HTML
```html
<div class="sk-16">
  <div class="sk-16__stage">
    <section class="sk-16__wrap" aria-labelledby="sk-16-h">
      <header class="sk-16__head">
        <p class="sk-16__eyebrow">thread · 3 shells + 1 reply</p>
        <h2 class="sk-16__h" id="sk-16-h">The post is real. The thread is pending.</h2>
        <p class="sk-16__sub">Comments load after the article, so the skeleton has to inherit the resolved thread's gaps and indent — otherwise the page re-rhythms when replies land.</p>
      </header>

      <article class="sk-16__post">
        <div class="sk-16__prow">
          <img class="sk-16__pic" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&amp;fit=crop&amp;w=96&amp;h=96&amp;q=70" width="96" height="96" alt="Alex Chen" loading="lazy" decoding="async">
          <div class="sk-16__ident">
            <p class="sk-16__name">Alex Chen</p>
            <p class="sk-16__meta">2 hours ago · 24 replies</p>
          </div>
        </div>
        <p class="sk-16__copy">We replaced every spinner in the review flow with a skeleton that matches its resolved layout. Reviewers stopped reporting “the page jumped” within a week.</p>
      </article>

      <ul class="sk-16__thread" role="status" aria-live="polite">
        <span class="sk-16__vh">Loading 3 comments…</span>
        <li class="sk-16__comment" style="--i:0">
          <article class="sk-16__shell" aria-hidden="true">
            <div class="sk-16__srow">
              <span class="sk-16__bar sk-16__avatar"></span>
              <div class="sk-16__ident"><span class="sk-16__bar sk-16__bar--name" style="inline-size:8rem"></span><span class="sk-16__bar sk-16__bar--meta" style="inline-size:6.5rem"></span></div>
            </div>
            <div class="sk-16__lines"><span class="sk-16__bar"></span><span class="sk-16__bar" style="inline-size:92%"></span><span class="sk-16__bar" style="inline-size:58%"></span></div>
          </article>
        </li>
        <li class="sk-16__comment" style="--i:1">
          <article class="sk-16__shell" aria-hidden="true">
            <div class="sk-16__srow">
              <span class="sk-16__bar sk-16__avatar"></span>
              <div class="sk-16__ident"><span class="sk-16__bar sk-16__bar--name" style="inline-size:10rem"></span><span class="sk-16__bar sk-16__bar--meta" style="inline-size:5.5rem"></span></div>
            </div>
            <div class="sk-16__lines"><span class="sk-16__bar"></span><span class="sk-16__bar" style="inline-size:86%"></span><span class="sk-16__bar" style="inline-size:44%"></span></div>
          </article>
          <ul class="sk-16__replies">
            <li class="sk-16__comment" style="--i:2">
              <article class="sk-16__shell" aria-hidden="true">
                <div class="sk-16__srow">
                  <span class="sk-16__bar sk-16__avatar sk-16__avatar--sm"></span>
                  <div class="sk-16__ident"><span class="sk-16__bar sk-16__bar--name" style="inline-size:7rem"></span><span class="sk-16__bar sk-16__bar--meta" style="inline-size:4.5rem"></span></div>
                </div>
                <div class="sk-16__lines"><span class="sk-16__bar"></span><span class="sk-16__bar" style="inline-size:52%"></span></div>
              </article>
            </li>
          </ul>
        </li>
        <li class="sk-16__comment" style="--i:3">
          <article class="sk-16__shell" aria-hidden="true">
            <div class="sk-16__srow">
              <span class="sk-16__bar sk-16__avatar"></span>
              <div class="sk-16__ident"><span class="sk-16__bar sk-16__bar--name" style="inline-size:9rem"></span><span class="sk-16__bar sk-16__bar--meta" style="inline-size:7rem"></span></div>
            </div>
            <div class="sk-16__lines"><span class="sk-16__bar"></span><span class="sk-16__bar" style="inline-size:90%"></span><span class="sk-16__bar" style="inline-size:62%"></span></div>
          </article>
        </li>
      </ul>

      <aside class="sk-16__spec" aria-label="Recipe">
        <p class="sk-16__srow2"><span class="sk-16__skey">rhythm</span><span class="sk-16__sval">thread gap 1.35rem · line gap .55rem — identical to the resolved thread</span></p>
        <p class="sk-16__srow2"><span class="sk-16__skey">indent</span><span class="sk-16__sval">padding-inline-start: clamp(1.5rem, 4vw, 2.75rem) + a 1px rail</span></p>
        <p class="sk-16__srow2"><span class="sk-16__skey">stagger</span><span class="sk-16__sval">animation-delay: calc(var(--i) * -.22s) per comment, never per bar</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-16 {
  --bg: #07090b;
  --bg2: #0e1215;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #f3f6f7;
  --muted: rgba(243,246,247,.62);
  --faint: rgba(243,246,247,.42);
  --accent: #fdba74;
  --sk: rgba(243,246,247,.1);
  --sheen: rgba(243,246,247,.17);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(56% 40% at 14% -6%, rgba(253,186,116,.1) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-16 *,
.sk-16 *::before,
.sk-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 60)) {
  .sk-16 {
    --ink: oklch(0.97 0.005 200);
    --muted: oklch(0.97 0.005 200 / .62);
    --faint: oklch(0.97 0.005 200 / .42);
    --accent: oklch(0.82 0.11 65);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-16 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 17%, transparent);
  }
}

.sk-16__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-16__wrap {
  inline-size: min(52rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.5rem);
}

.sk-16__head {
  display: grid;
  gap: .6rem;
}

.sk-16__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-16__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-16__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-16__post {
  display: grid;
  gap: .8rem;
  padding: clamp(1rem,1.9vw,1.4rem);
  border: 1px solid var(--line);
  border-radius: 1.05rem;
  background: var(--surface);
}

.sk-16__prow {
  display: flex;
  align-items: center;
  gap: .9rem;
}

.sk-16__pic {
  inline-size: 2.6rem;
  aspect-ratio: 1;
  border-radius: 999px;
  object-fit: cover;
  background: var(--sk);
  flex: none;
}

.sk-16__ident {
  display: grid;
  gap: .45rem;
  min-inline-size: 0;
}

.sk-16__name {
  margin: 0;
  font-size: .98rem;
  font-weight: 500;
}

.sk-16__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.sk-16__copy {
  margin: 0;
  font-size: .95rem;
  line-height: 1.62;
  color: var(--muted);
  max-inline-size: 56ch;
  text-wrap: pretty;
}

.sk-16__thread {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1.35rem;
}

.sk-16__comment {
  display: grid;
  gap: 1.35rem;
}

.sk-16__shell {
  display: grid;
  gap: .8rem;
  padding: clamp(1rem,1.9vw,1.35rem);
  border: 1px solid var(--line);
  border-radius: 1.05rem;
  background: var(--surface);
}

.sk-16__srow {
  display: flex;
  align-items: center;
  gap: .9rem;
}

.sk-16__lines {
  display: grid;
  gap: .55rem;
}

.sk-16__replies {
  list-style: none;
  margin: 0;
  padding-inline-start: clamp(1.5rem,4vw,2.75rem);
  border-inline-start: 1px solid var(--line);
  display: grid;
  gap: 1.35rem;
}

.sk-16__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .72rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-16__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-16-sheen 1.4s linear infinite;
  animation-delay: calc(var(--i,0) * -.22s);
}

@keyframes sk-16-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-16__bar--name {
  block-size: .85rem;
}

.sk-16__bar--meta {
  block-size: .65rem;
}

.sk-16__avatar {
  inline-size: 2.6rem;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}

.sk-16__avatar--sm {
  inline-size: 2.1rem;
}

.sk-16__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-16__srow2 {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-16__skey {
  min-inline-size: 4.2rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-16__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-16[data-theme="light"] {
  --bg: #faf9f7;
  --bg2: #fff;
  --surface: rgba(12,14,16,.026);
  --line: rgba(12,14,16,.11);
  --ink: #0c0e10;
  --muted: rgba(12,14,16,.62);
  --faint: rgba(12,14,16,.44);
  --accent: #b45309;
  background: linear-gradient(178deg,#fff 0%,#f4f1ec 100%);
}

@media (prefers-color-scheme: light) {
  .sk-16:not([data-theme="dark"]) {
    --bg: #faf9f7;
    --bg2: #fff;
    --surface: rgba(12,14,16,.026);
    --line: rgba(12,14,16,.11);
    --ink: #0c0e10;
    --muted: rgba(12,14,16,.62);
    --faint: rgba(12,14,16,.44);
    --accent: #b45309;
    background: linear-gradient(178deg,#fff 0%,#f4f1ec 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-16__bar::after {
    animation: none;
    background: none;
  }

  .sk-16__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-16__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-16__bar::after {
    animation: none;
    background: none;
  }

  .sk-16__shell,
    .sk-16__post,
    .sk-16__spec {
    border-color: CanvasText;
  }
}
```
