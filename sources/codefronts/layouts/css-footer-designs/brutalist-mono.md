---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/brutalist-mono/"
title: "Monospaced Developer Portfolio Footer"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "A footer for people who read git log for fun: everything set in a monospace grid measured in ch, an ASCII rule, a blinking block caret, and a build stamp…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Monospaced Developer Portfolio Footer
Source: https://codefronts.com/layouts/css-footer-designs/brutalist-mono/

A footer for people who read git log for fun: everything set in a monospace grid measured in ch, an ASCII rule, a blinking block caret, and a build stamp that makes the site feel like a deployed artefact rather than a page. Restrained, fast, and no ASCII-art clichés.
## HTML
```html
<section class="ft-15" aria-label="Monospaced developer portfolio footer demo">
  <main class="ft-15__main">
    <p class="ft-15__eyebrow">ch units · steps() caret · build stamp</p>
    <h1 class="ft-15__title">footer --format=terminal</h1>
    <p class="ft-15__sub">Every column aligns because the layout is measured in characters, not pixels. The caret blinks on a step curve. The build stamp is the part people actually read.</p>
  </main>
  <footer class="ft-15__foot">
    <div class="ft-15__term">
      <p class="ft-15__rule" aria-hidden="true"></p>
      <div class="ft-15__grid">
        <section class="ft-15__block" aria-labelledby="ft-15-b1">
          <h2 class="ft-15__h" id="ft-15-b1">~/links</h2>
          <ul class="ft-15__list">
            <li><a class="ft-15__link" href="#ft-15-a">projects</a><span class="ft-15__dim">12 repos</span></li>
            <li><a class="ft-15__link" href="#ft-15-a">writing</a><span class="ft-15__dim">38 posts</span></li>
            <li><a class="ft-15__link" href="#ft-15-a">uses</a><span class="ft-15__dim">hardware</span></li>
            <li><a class="ft-15__link" href="#ft-15-a">now</a><span class="ft-15__dim">what I'm on</span></li>
          </ul>
        </section>
        <section class="ft-15__block" aria-labelledby="ft-15-b2">
          <h2 class="ft-15__h" id="ft-15-b2">~/contact</h2>
          <ul class="ft-15__list">
            <li><a class="ft-15__link" href="mailto:[email protected]">[email protected]</a></li>
            <li><a class="ft-15__link" href="#ft-15-a">github/jhalvorsen</a></li>
            <li><a class="ft-15__link" href="#ft-15-a">@[email protected]</a></li>
            <li><a class="ft-15__link" href="#ft-15-a">public key (age)</a></li>
          </ul>
        </section>
        <section class="ft-15__block" aria-labelledby="ft-15-b3">
          <h2 class="ft-15__h" id="ft-15-b3">~/status</h2>
          <dl class="ft-15__dl">
            <div><dt>availability</dt><dd class="ft-15__ok">open · Q4 2026</dd></div>
            <div><dt>location</dt><dd>Bergen, UTC+2</dd></div>
            <div><dt>stack</dt><dd>ts · go · postgres</dd></div>
            <div><dt>reply time</dt><dd>&lt; 2 days</dd></div>
          </dl>
        </section>
      </div>
      <p class="ft-15__rule" aria-hidden="true"></p>
      <p class="ft-15__prompt"><span class="ft-15__sym" aria-hidden="true">&rarr;</span> <span class="ft-15__cmd">echo &quot;thanks for scrolling this far&quot;</span><span class="ft-15__caret" aria-hidden="true"></span></p>
      <div class="ft-15__stamp">
        <span class="ft-15__badge"><span class="ft-15__dot" aria-hidden="true"></span>build ok</span>
        <span class="ft-15__meta">commit <a class="ft-15__link" href="#ft-15-a">a7f31c9</a></span>
        <span class="ft-15__meta">deployed <time datetime="2026-08-05T14:12:00Z">05 Aug 2026, 14:12 UTC</time></span>
        <span class="ft-15__meta">© <time datetime="2026">2026</time> J. Halvorsen · <a class="ft-15__link" href="#ft-15-a">MIT</a></span>
      </div>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-15-bg);
  --ft-15-bg: oklch(0.16 0.014 160);
  --ft-15-foot: oklch(0.13 0.012 160);
  --ft-15-ink: oklch(0.93 0.02 150);
  --ft-15-mut: oklch(0.65 0.02 150);
  --ft-15-dim: oklch(0.5 0.018 150);
  --ft-15-acc: oklch(0.82 0.16 150);
  --ft-15-line: oklch(0.93 0.02 150/.18);
  font-family: ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;
  color: var(--ft-15-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-15 *,
.ft-15 *::before,
.ft-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-15 ul {
  list-style: none;
}

.ft-15__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(40px,8vh,92px);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 82ch)/2));
}

.ft-15__eyebrow {
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ft-15-acc);
}

.ft-15__title {
  font-size: clamp(26px,4.6vw,48px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 600;
}

.ft-15__sub {
  font-size: clamp(14px,1.5vw,16.5px);
  line-height: 1.7;
  color: var(--ft-15-mut);
  max-width: 70ch;
  text-wrap: pretty;
}

.ft-15__foot {
  background: var(--ft-15-foot);
  border-top: 1px solid var(--ft-15-line);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 82ch)/2));
}

.ft-15__term {
  display: grid;
  gap: 16px;
  padding-block: clamp(26px,4vw,40px);
  max-inline-size: 82ch;
}

.ft-15__rule {
  height: 1px;
  background: repeating-linear-gradient(90deg,currentColor 0 .5ch,transparent .5ch 1ch);
  color: var(--ft-15-dim);
  opacity: .6;
}

.ft-15__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(22ch,1fr));
  gap: clamp(18px,2.5vw,30px);
}

.ft-15__block {
  display: grid;
  align-content: start;
  gap: 6px;
  min-width: 0;
}

.ft-15__h {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: .02em;
  color: var(--ft-15-acc);
}

.ft-15__h::before {
  content: '# ';
  color: var(--ft-15-dim);
}

.ft-15__list {
  display: grid;
  gap: 0;
}

.ft-15__list li {
  display: flex;
  align-items: baseline;
  gap: 1ch;
  min-height: 30px;
}

.ft-15__link {
  font-size: 13.5px;
  color: var(--ft-15-ink);
  text-decoration: none;
  border-bottom: 1px dashed color-mix(in oklch,currentColor 35%,transparent);
  transition: color .18s ease,border-color .18s ease;
}

.ft-15__link:hover {
  color: var(--ft-15-acc);
  border-bottom-style: solid;
  border-bottom-color: currentColor;
}

.ft-15__link:focus-visible {
  outline: 2px solid var(--ft-15-acc);
  outline-offset: 3px;
  border-radius: 3px;
}

.ft-15__dim {
  font-size: 12px;
  color: var(--ft-15-dim);
}

.ft-15__dl {
  display: grid;
  gap: 2px;
}

.ft-15__dl>div {
  display: flex;
  gap: 1ch;
  min-height: 28px;
  font-size: 13px;
  align-items: baseline;
}

.ft-15__dl dt {
  width: 13ch;
  flex: none;
  color: var(--ft-15-dim);
}

.ft-15__dl dt::after {
  content: ':';
}

.ft-15__dl dd {
  color: var(--ft-15-mut);
}

.ft-15__ok {
  color: var(--ft-15-acc) !important;
}

.ft-15__prompt {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 1ch;
  font-size: 13.5px;
  line-height: 1.6;
}

.ft-15__sym {
  color: var(--ft-15-acc);
}

.ft-15__cmd {
  color: var(--ft-15-mut);
}

.ft-15__caret {
  display: inline-block;
  width: .62ch;
  height: 1.05em;
  translate: 0 .16em;
  background: var(--ft-15-acc);
  animation: ft-15-blink 1.06s steps(1,end) infinite;
}

@keyframes ft-15-blink {
  50% {
    opacity: 0;
  }
}

.ft-15__stamp {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px 2ch;
  padding-block-start: 6px;
  padding-bottom: calc(6px + env(safe-area-inset-bottom,0px));
  font-size: 12px;
  color: var(--ft-15-dim);
}

.ft-15__badge {
  display: inline-flex;
  align-items: center;
  gap: .8ch;
  padding: 5px 10px;
  border-radius: 6px;
  background: color-mix(in oklch,var(--ft-15-acc) 12%,transparent);
  color: var(--ft-15-acc);
  font-size: 11.5px;
}

.ft-15__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  animation: ft-15-pulse 2.6s ease-in-out infinite;
}

@keyframes ft-15-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .3;
  }
}

.ft-15__meta {
  white-space: nowrap;
}

@media (max-width: 520px) {
  .ft-15__meta {
    white-space: normal;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-15__caret,
    .ft-15__dot {
    animation: none;
  }

  .ft-15 * {
    transition-duration: .01ms !important;
  }
}
```
