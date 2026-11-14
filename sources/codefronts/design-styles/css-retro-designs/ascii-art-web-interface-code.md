---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/ascii-art-web-interface-code/"
title: "ASCII Art Terminal Interface"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A character-cell console on paper white rather than the usual black: box-drawn panels, a block-letter banner, and a working command line that takes input…"
has_js: "true"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: ASCII Art Terminal Interface
Source: https://codefronts.com/design-styles/css-retro-designs/ascii-art-web-interface-code/

A character-cell console on paper white rather than the usual black: box-drawn panels, a block-letter banner, and a working command line that takes input without a form element. The banner is aria-hidden with a real text alternative, because ASCII art read aloud is several hundred punctuation marks and no information.
## HTML
```html
<section class="rt-16" aria-labelledby="rt-16-title">
  <h2 class="rt-16__sr" id="rt-16-title">ASCII art terminal console</h2>

  <div class="rt-16__theme">
    <input class="rt-16__theme-input" type="checkbox" id="rt-16-theme">
    <label class="rt-16__theme-label" for="rt-16-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-16__sr">Toggle dark console</span>
    </label>
  </div>

  <div class="rt-16__stage">
    <p class="rt-16__badge">Character-cell console &middot; code page 437 frames &middot; ink on paper</p>

    <div class="rt-16__term">
      <div class="rt-16__banner-wrap">
        <pre class="rt-16__banner" aria-hidden="true">  ████      ██████    ██████  ██████  ██████
██    ██  ██        ██          ██      ██  
████████    ████    ██          ██      ██  
██    ██        ██  ██          ██      ██  
██    ██  ██████      ██████  ██████  ██████</pre>
        <p class="rt-16__sr">Block-letter banner reading ASCII, drawn in full-block characters.</p>
      </div>

      <div class="rt-16__frames">
        <pre class="rt-16__frame" aria-hidden="true">┌─ SESSION ──────────────────┐
│ host   northgate.local     │
│ tty    /dev/ttyS0          │
│ rate   9600 8N1            │
│ codec  cp437               │
└────────────────────────────┘</pre>
        <p class="rt-16__sr">Session panel: host northgate.local, tty /dev/ttyS0, rate 9600 8N1, codec cp437.</p>

        <pre class="rt-16__frame" aria-hidden="true">╔═ COMMANDS ═════════════════╗
║ help    list commands      ║
║ ver     print version      ║
║ dir     list files         ║
║ clear   empty the log      ║
╚════════════════════════════╝</pre>
        <p class="rt-16__sr">Commands panel: help lists commands, ver prints the version, dir lists files, clear empties the log.</p>
      </div>

      <ul class="rt-16__log" data-rt-16-log aria-live="polite" aria-relevant="additions" aria-label="Console output">
        <li class="rt-16__line">northgate console ready. type <b>help</b> and press Enter.</li>
      </ul>

      <div class="rt-16__prompt">
        <label class="rt-16__ps1" for="rt-16-input">C:\&gt;</label>
        <input class="rt-16__input" id="rt-16-input" type="text" data-rt-16-input autocomplete="off" spellcheck="false" placeholder="help">
        <button class="rt-16__run" type="button" data-rt-16-run>Run</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-16 {
  --rt-16-cell: clamp(0.58rem, 0.42rem + 0.85vw, 0.85rem);
  --rt-16-mono: ui-monospace, SFMono-Regular, "Cascadia Mono", Consolas, "DejaVu Sans Mono", "Liberation Mono", monospace;
  --rt-16-paper: #f6f4ec;
  --rt-16-paper: oklch(97% 0.008 96);
  --rt-16-ink: #1a1a16;
  --rt-16-ink: oklch(21% 0.008 96);
  --rt-16-ink-2: #5a584e;
  --rt-16-ink-2: oklch(47% 0.012 96);
  --rt-16-line: #b6b3a5;
  --rt-16-line: oklch(76% 0.014 96);
  --rt-16-bg: #e2dfd4;
  --rt-16-bg: oklch(90% 0.012 96);
  --rt-16-acc: #8a3a08;
  --rt-16-acc: oklch(43% 0.13 55);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-16-bg);
  color: var(--rt-16-ink);
  font-family: var(--rt-16-mono);
  -webkit-text-size-adjust: 100%;
}

.rt-16 *,
.rt-16 *::before,
.rt-16 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-16 {
    --rt-16-paper: #16160f;
    --rt-16-paper: oklch(20% 0.01 96);
    --rt-16-ink: #f0eee2;
    --rt-16-ink: oklch(95% 0.008 96);
    --rt-16-ink-2: #aaa799;
    --rt-16-ink-2: oklch(73% 0.013 96);
    --rt-16-line: #464438;
    --rt-16-line: oklch(38% 0.014 96);
    --rt-16-bg: #0e0e09;
    --rt-16-bg: oklch(16% 0.008 96);
    --rt-16-acc: #ff9a52;
    --rt-16-acc: oklch(78% 0.13 55);
  }
}

.rt-16[data-theme="dark"],
.rt-16:has(.rt-16__theme-input:checked) {
  --rt-16-paper: #16160f;
  --rt-16-paper: oklch(20% 0.01 96);
  --rt-16-ink: #f0eee2;
  --rt-16-ink: oklch(95% 0.008 96);
  --rt-16-ink-2: #aaa799;
  --rt-16-ink-2: oklch(73% 0.013 96);
  --rt-16-line: #464438;
  --rt-16-line: oklch(38% 0.014 96);
  --rt-16-bg: #0e0e09;
  --rt-16-bg: oklch(16% 0.008 96);
  --rt-16-acc: #ff9a52;
  --rt-16-acc: oklch(78% 0.13 55);
}

@media (prefers-color-scheme: light) {
  .rt-16:has(.rt-16__theme-input:checked) {
    --rt-16-paper: #16160f;
    --rt-16-paper: oklch(20% 0.01 96);
    --rt-16-ink: #f0eee2;
    --rt-16-ink: oklch(95% 0.008 96);
    --rt-16-ink-2: #aaa799;
    --rt-16-ink-2: oklch(73% 0.013 96);
    --rt-16-line: #464438;
    --rt-16-line: oklch(38% 0.014 96);
    --rt-16-bg: #0e0e09;
    --rt-16-bg: oklch(16% 0.008 96);
    --rt-16-acc: #ff9a52;
    --rt-16-acc: oklch(78% 0.13 55);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-16:has(.rt-16__theme-input:checked) {
    --rt-16-paper: #f6f4ec;
    --rt-16-paper: oklch(97% 0.008 96);
    --rt-16-ink: #1a1a16;
    --rt-16-ink: oklch(21% 0.008 96);
    --rt-16-ink-2: #5a584e;
    --rt-16-ink-2: oklch(47% 0.012 96);
    --rt-16-line: #b6b3a5;
    --rt-16-line: oklch(76% 0.014 96);
    --rt-16-bg: #e2dfd4;
    --rt-16-bg: oklch(90% 0.012 96);
    --rt-16-acc: #8a3a08;
    --rt-16-acc: oklch(43% 0.13 55);
  }
}

.rt-16__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-16__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-16__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-16__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-16-line);
  background: var(--rt-16-paper);
  color: var(--rt-16-ink-2);
  cursor: pointer;
}

.rt-16__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-16__theme-input:focus-visible + .rt-16__theme-label {
  outline: 2px solid var(--rt-16-acc);
  outline-offset: 2px;
}

.rt-16__stage {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.6rem, 0.4rem + 1.5vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1rem;
}

.rt-16__badge {
  margin: 0;
  justify-self: start;
  min-inline-size: 0;
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--rt-16-ink-2);
  border: 1px solid var(--rt-16-line);
  padding: 0.35rem 0.7rem;
  background: var(--rt-16-paper);
}

.rt-16__term {
  min-inline-size: 0;
  background: var(--rt-16-paper);
  border: 2px solid var(--rt-16-ink);
  padding: clamp(0.75rem, 0.5rem + 1.4vw, 1.4rem);
  display: grid;
  gap: 1rem;
  box-shadow: 6px 6px 0 0 var(--rt-16-line);
}

.rt-16__banner-wrap {
  min-inline-size: 0;
  overflow-x: auto;
}

.rt-16__banner {
  margin: 0;
  font-family: inherit;
  white-space: pre;
  line-height: 1;
  font-size: calc(var(--rt-16-cell) * 0.9);
  color: var(--rt-16-acc);
  min-inline-size: 0;
}

.rt-16__frames {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.85rem;
}

.rt-16__frame {
  margin: 0;
  font-family: inherit;
  white-space: pre;
  line-height: 1.2;
  overflow-x: auto;
  font-size: var(--rt-16-cell);
  color: var(--rt-16-ink);
  min-inline-size: 0;
}

.rt-16__log {
  list-style: none;
  margin: 0;
  padding: 0.6rem 0.7rem;
  min-inline-size: 0;
  border: 1px solid var(--rt-16-line);
  background: var(--rt-16-bg);
  display: grid;
  gap: 0.2rem;
  align-content: start;
  min-block-size: 9rem;
  max-block-size: 16rem;
  overflow-y: auto;
  font-size: var(--rt-16-cell);
}

.rt-16__line {
  min-inline-size: 0;
  overflow-wrap: anywhere;
  color: var(--rt-16-ink);
}

.rt-16__line b {
  color: var(--rt-16-acc);
}

.rt-16__line--echo {
  color: var(--rt-16-ink-2);
}

.rt-16__prompt {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  min-inline-size: 0;
}

.rt-16__ps1 {
  font-size: var(--rt-16-cell);
  color: var(--rt-16-acc);
  flex: none;
  letter-spacing: 0.05em;
}

.rt-16__input {
  flex: 1 1 10rem;
  min-inline-size: 0;
  min-block-size: 44px;
  padding: 0.5rem 0.7rem;
  font: inherit;
  font-size: var(--rt-16-cell);
  color: var(--rt-16-ink);
  background: var(--rt-16-bg);
  border: 1px solid var(--rt-16-ink);
}

.rt-16__input:focus-visible {
  outline: 2px solid var(--rt-16-acc);
  outline-offset: 2px;
}

.rt-16__run {
  min-block-size: 44px;
  min-inline-size: 5rem;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font: inherit;
  font-size: var(--rt-16-cell);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: var(--rt-16-ink);
  color: var(--rt-16-paper);
  border: 1px solid var(--rt-16-ink);
}

.rt-16__run:active {
  background: var(--rt-16-acc);
  border-color: var(--rt-16-acc);
}

.rt-16__run:focus-visible {
  outline: 2px solid var(--rt-16-acc);
  outline-offset: 2px;
}

@media (min-width: 46rem) {
  .rt-16__frames {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```

## JavaScript
```js
const root = document.currentScript.closest('.rt-16') || document.querySelector('.rt-16');
const log = root.querySelector('[data-rt-16-log]');
const input = root.querySelector('[data-rt-16-input]');
const run = root.querySelector('[data-rt-16-run]');
const replies = {
  help: 'commands: help, ver, dir, clear',
  ver: 'northgate console 2.4 — cp437, 9600 8N1',
  dir: 'AUTOEXEC.BAT  COMMAND.COM  CONFIG.SYS  README.TXT'
};
const say = (text, echo) => {
  const li = document.createElement('li');
  li.className = echo ? 'rt-16__line rt-16__line--echo' : 'rt-16__line';
  li.textContent = text;
  log.append(li);
  while (log.childElementCount > 40) log.firstElementChild.remove();
};
const submit = () => {
  const cmd = input.value.trim().toLowerCase();
  if (!cmd) return;
  input.value = '';
  if (cmd === 'clear') { log.replaceChildren(); return; }
  say('C:\\> ' + cmd, true);
  say(replies[cmd] || ('bad command or file name: ' + cmd));
};
const onKey = (e) => { if (e.key === 'Enter') { e.preventDefault(); submit(); } };
run.addEventListener('click', submit);
input.addEventListener('keydown', onKey);
root.__rtCleanup = () => { run.removeEventListener('click', submit); input.removeEventListener('keydown', onKey); };
```
