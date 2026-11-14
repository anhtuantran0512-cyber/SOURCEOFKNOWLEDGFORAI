---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/terminal-log/"
title: "Terminal Log Timeline — Command-Line Session with Typing Caret"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "Developer-docs native: a dark terminal session where each timeline event is a timestamped log line with severity-colored level tags, a blinking block caret…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal Log Timeline — Command-Line Session with Typing Caret
Source: https://codefronts.com/layouts/css-timelines/terminal-log/

Developer-docs native: a dark terminal session where each timeline event is a timestamped log line with severity-colored level tags, a blinking block caret typing the newest entry via steps() animation, and a window-chrome header — the format for deploy logs, system journals, incident timelines and CLI tutorials.
## HTML
```html
<section class="tls-19" aria-label="Terminal log timeline demo">
  <div class="tls-19__term">
    <div class="tls-19__chrome" aria-hidden="true"><span></span><span></span><span></span><p>deploy · production · ssh</p></div>
    <samp class="tls-19__screen">
      <span class="tls-19__ln"><time class="tls-19__ts" datetime="2026-07-18T14:02:01">14:02:01</time><b class="tls-19__lv" data-lv="ok">[ ok ]</b><span class="tls-19__msg">build completed in 42s · 0 warnings</span></span>
      <span class="tls-19__ln"><time class="tls-19__ts" datetime="2026-07-18T14:02:44">14:02:44</time><b class="tls-19__lv" data-lv="ok">[ ok ]</b><span class="tls-19__msg">integration suite: 214 passed</span></span>
      <span class="tls-19__ln"><time class="tls-19__ts" datetime="2026-07-18T14:03:10">14:03:10</time><b class="tls-19__lv" data-lv="warn">[warn]</b><span class="tls-19__msg">bundle +4.2 kB over budget (icons)</span></span>
      <span class="tls-19__ln tls-19__ln--fail"><time class="tls-19__ts" datetime="2026-07-18T14:03:58">14:03:58</time><b class="tls-19__lv" data-lv="fail">[FAIL]</b><span class="tls-19__msg">canary check: p99 latency 840ms &gt; 500ms</span></span>
      <span class="tls-19__ln"><time class="tls-19__ts" datetime="2026-07-18T14:04:02">14:04:02</time><b class="tls-19__lv" data-lv="info">[info]</b><span class="tls-19__msg">rollback initiated automatically</span></span>
      <span class="tls-19__ln"><time class="tls-19__ts" datetime="2026-07-18T14:04:31">14:04:31</time><b class="tls-19__lv" data-lv="ok">[ ok ]</b><span class="tls-19__msg tls-19__msg--type">rollback complete · traffic 100%</span></span>
    </samp>
  </div>
</section>
```
## CSS
```css
.tls-19,
.tls-19 *,
.tls-19 *::before,
.tls-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-19 {
  min-height: 100vh;
  width: 100%;
  --tl-ok: #34d399;
  --tl-warn: #fbbf24;
  --tl-fail: #f87171;
  --tl-info: #60a5fa;
  --tl-ink: #c8d3dc;
  --tl-mut: #55616d;
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
  background: #11151a;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-19__term {
  width: min(640px,100%);
  background: #0a0e12;
  border: 1px solid #232a33;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 24px 60px -30px rgba(0,0,0,.7);
}

.tls-19__chrome {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 11px 14px;
  border-bottom: 1px solid #1a212a;
  background: #0e1319;
}

.tls-19__chrome span {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #2d3742;
}

.tls-19__chrome span:nth-child(1) {
  background: #f87171;
}

.tls-19__chrome span:nth-child(2) {
  background: #fbbf24;
}

.tls-19__chrome span:nth-child(3) {
  background: #34d399;
}

.tls-19__chrome p {
  margin-left: 8px;
  font-size: 11px;
  color: var(--tl-mut);
  letter-spacing: .04em;
}

.tls-19__screen {
  display: flex;
  flex-direction: column;
  gap: 7px;
  padding: 18px 20px 22px;
  font-size: 12.5px;
  line-height: 1.5;
}

.tls-19__ln {
  display: grid;
  grid-template-columns: 9ch 7ch 1fr;
  gap: 12px;
  align-items: baseline;
}

.tls-19__ln--fail {
  background: rgba(248,113,113,.07);
  margin-inline: -20px;
  padding-inline: 20px;
  border-left: 2px solid var(--tl-fail);
}

.tls-19__ts {
  color: var(--tl-mut);
  font-variant-numeric: tabular-nums;
}

.tls-19__lv {
  font-weight: 700;
}

.tls-19__lv[data-lv="ok"] {
  color: var(--tl-ok);
}

.tls-19__lv[data-lv="warn"] {
  color: var(--tl-warn);
}

.tls-19__lv[data-lv="fail"] {
  color: var(--tl-fail);
}

.tls-19__lv[data-lv="info"] {
  color: var(--tl-info);
}

.tls-19__msg {
  color: var(--tl-ink);
}

.tls-19__msg--type {
  position: relative;
  display: inline-block;
}

.tls-19__msg--type::after {
  content: '';
  display: inline-block;
  width: 8px;
  height: 15px;
  background: var(--tl-ok);
  vertical-align: -2px;
  margin-left: 2px;
}

@media (prefers-reduced-motion: no-preference) {
  .tls-19__msg--type {
    overflow: hidden;
    white-space: nowrap;
    width: 30ch;
    animation: tls-19-type 2.1s steps(30) .4s backwards;
  }

  @keyframes tls-19-type {
    from {
      width: 0;
    }
  }

  .tls-19__msg--type::after {
    animation: tls-19-blink 1s steps(1) infinite;
  }

  @keyframes tls-19-blink {
    50% {
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
/* No JavaScript — typing is width:0→30ch with steps(30) on a monospace span (1 step = 1 character); the caret blinks with steps(1); both gated behind no-preference. */
```
