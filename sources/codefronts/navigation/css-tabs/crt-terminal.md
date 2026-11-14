---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/crt-terminal/"
title: "CRT Terminal"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Vintage CRT terminal aesthetic: green phosphor text, scanline overlay, macOS traffic lights in the title bar."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CRT Terminal
Source: https://codefronts.com/navigation/css-tabs/crt-terminal/

Vintage CRT terminal aesthetic: green phosphor text, scanline overlay, macOS traffic lights in the title bar. Active tab shows a blinking caret cursor. Pure CSS.
## HTML
```html
<div class="tt29">
  <div class="tt29win">
    <div class="tt29bar">
      <span class="tt29light tt29-r"></span>
      <span class="tt29light tt29-y"></span>
      <span class="tt29light tt29-g"></span>
      <span class="tt29ttl">terminal — bash</span>
    </div>
    <nav class="tt29n">
      <input type="radio" name="tt29" id="tt29-r1" checked />
      <label class="tt29b" for="tt29-r1">~/main</label>
      <input type="radio" name="tt29" id="tt29-r2" />
      <label class="tt29b" for="tt29-r2">~/logs</label>
      <input type="radio" name="tt29" id="tt29-r3" />
      <label class="tt29b" for="tt29-r3">~/cron</label>
    </nav>
    <div class="tt29body">
      <div class="tt29p">$ ls -la<br />drwxr-xr-x src/<br />-rw-r--r-- README.md</div>
      <div class="tt29p">$ tail -f app.log<br />[12:04] OK 200<br />[12:05] OK 200</div>
      <div class="tt29p">$ crontab -l<br />0 * * * * ./sync.sh<br />*/5 * * * * ./ping.sh</div>
    </div>
  </div>
</div>
```
## CSS
```css
.tt29 {
  background: #0a0a0a;
  padding: 18px 16px;
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.tt29win {
  background: #050505;
  border: 1px solid rgba(74, 222, 128, 0.18);
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 0 0 1px rgba(74, 222, 128, 0.04), 0 8px 24px rgba(0, 0, 0, 0.5);
}

.tt29bar {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: #111;
  border-bottom: 1px solid rgba(74, 222, 128, 0.12);
}

.tt29light {
  width: 11px;
  height: 11px;
  border-radius: 50%;
}

.tt29-r {
  background: #ff5f57;
}

.tt29-y {
  background: #febc2e;
}

.tt29-g {
  background: #28c840;
}

.tt29ttl {
  margin-left: 10px;
  font: 11px/1 ui-monospace, monospace;
  color: rgba(255, 255, 255, 0.45);
  letter-spacing: 0.04em;
}

.tt29n {
  display: flex;
  gap: 0;
  background: #0a0a0a;
  border-bottom: 1px solid rgba(74, 222, 128, 0.12);
  min-width: 0;
}

.tt29n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt29b {
  flex: 1;
  min-width: 0;
  padding: 8px 12px;
  font: 11px/1 ui-monospace, monospace;
  color: rgba(74, 222, 128, 0.5);
  cursor: pointer;
  text-align: center;
  white-space: nowrap;
  transition: color 0.2s, background 0.2s;
  border-right: 1px solid rgba(74, 222, 128, 0.08);
}

.tt29b:last-of-type {
  border-right: 0;
}

.tt29b:hover {
  color: rgba(74, 222, 128, 0.85);
  background: rgba(74, 222, 128, 0.04);
}

.tt29n input:checked + .tt29b {
  color: #4ade80;
  background: rgba(74, 222, 128, 0.1);
  text-shadow: 0 0 6px rgba(74, 222, 128, 0.6);
}

.tt29n input:focus-visible + .tt29b {
  outline: 1px dashed #4ade80;
  outline-offset: -3px;
}

.tt29body {
  position: relative;
  padding: 14px 14px;
  min-height: 90px;
  background: repeating-linear-gradient(
      0deg,
      transparent 0,
      transparent 2px,
      rgba(74, 222, 128, 0.04) 2px,
      rgba(74, 222, 128, 0.04) 3px
    );
}

.tt29p {
  display: none;
  font: 11px/1.7 ui-monospace, monospace;
  color: #4ade80;
  text-shadow: 0 0 4px rgba(74, 222, 128, 0.4);
}

.tt29:has(#tt29-r1:checked) .tt29p:nth-of-type(1),
.tt29:has(#tt29-r2:checked) .tt29p:nth-of-type(2),
.tt29:has(#tt29-r3:checked) .tt29p:nth-of-type(3) {
  display: block;
}
```
