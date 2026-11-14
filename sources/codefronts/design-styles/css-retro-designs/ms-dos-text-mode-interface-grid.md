---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/ms-dos-text-mode-interface-grid/"
title: "MS DOS Text Mode Interface Grid"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A character-cell interface, reproduced as one: an 80&times;25 field where every cell is exactly one monospace advance, laid out with CSS Grid and ch units,…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: MS DOS Text Mode Interface Grid
Source: https://codefronts.com/design-styles/css-retro-designs/ms-dos-text-mode-interface-grid/

A character-cell interface, reproduced as one: an 80&times;25 field where every cell is exactly one monospace advance, laid out with CSS Grid and ch units, framed with code page 437 box-drawing characters and restricted to the 16-colour CGA palette as tokens. The constraint is the subject &mdash; nothing can sit between two cells, so every alignment decision is an integer.
## HTML
```html
<section class="rt-06" aria-labelledby="rt-06-title">
  <h2 class="rt-06__sr" id="rt-06-title">MS-DOS text mode character grid</h2>

  <div class="rt-06__theme">
    <input class="rt-06__theme-input" type="checkbox" id="rt-06-theme">
    <label class="rt-06__theme-label" for="rt-06-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-06__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-06__stage">
    <p class="rt-06__badge">IBM CGA &middot; 16 colours &middot; 80 &times; 25 text mode &middot; code page 437</p>

    <div class="rt-06__frame">
      <div class="rt-06__screen">
        <div class="rt-06__menu" role="presentation">
          <span class="rt-06__menu-hi">F</span><span>ile</span>
          <span class="rt-06__menu-gap"></span>
          <span class="rt-06__menu-hi">E</span><span>dit</span>
          <span class="rt-06__menu-gap"></span>
          <span class="rt-06__menu-hi">S</span><span>earch</span>
          <span class="rt-06__menu-gap"></span>
          <span class="rt-06__menu-hi">O</span><span>ptions</span>
          <span class="rt-06__menu-tail">MEM 640K</span>
        </div>

        <pre class="rt-06__art rt-06__art--wide" aria-hidden="true">╔══════════════════════════════════════════════════════════════════════════════╗
║  C:\ ─ Directory of drive C  ─  6 file(s)  ─  90,671 bytes                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Name            Size      Date        Attr    Type                          ║
║  ────────────────────────────────────────────────────────────────────        ║
║  AUTOEXEC.BAT      1,024   04-12-1995  A       Batch file                    ║
║  COMMAND.COM      54,619   05-31-1994  RA      Command interpreter           ║
║  CONFIG.SYS          412   04-12-1995  A       System configuration          ║
║  HIMEM.SYS        29,136   05-31-1994  RA      Extended memory manager       ║
║  README.TXT        7,880   11-03-1995  A       Text                          ║
║                                                                              ║
║  Every glyph above occupies exactly one cell. Nothing sits between two cells.║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝</pre>
        <pre class="rt-06__art rt-06__art--narrow" aria-hidden="true">╔══════════════════════════════════════╗
║  C:\ ─ 6 file(s), 90,671 bytes       ║
╠══════════════════════════════════════╣
║ Name          Size    Attr           ║
║ ─────────────────────────────────────║
║ AUTOEXEC.BAT  1,024   A              ║
║ COMMAND.COM  54,619   RA             ║
║ CONFIG.SYS      412   A              ║
║ HIMEM.SYS    29,136   RA             ║
║ README.TXT    7,880   A              ║
║                                      ║
║  One glyph = one cell. No between.   ║
║                                      ║
║                                      ║
╚══════════════════════════════════════╝</pre>
        <p class="rt-06__sr">A DOS-style file manager panel listing AUTOEXEC.BAT, CONFIG.SYS, COMMAND.COM and HIMEM.SYS with sizes and dates, framed in double-line box characters.</p>

        <div class="rt-06__status">
          <span><span class="rt-06__key">F1</span> Help</span>
          <span><span class="rt-06__key">F3</span> Open</span>
          <span><span class="rt-06__key">F10</span> Menu</span>
          <span class="rt-06__status-tail">80 &times; 25</span>
        </div>
      </div>
    </div>

    <aside class="rt-06__inspect">
      <h3 class="rt-06__inspect-h">Cell inspector &mdash; the grid the text lands on</h3>
      <div class="rt-06__cells" aria-hidden="true">
        <span class="rt-06__cell">╔</span><span class="rt-06__cell">═</span><span class="rt-06__cell">═</span><span class="rt-06__cell">╦</span><span class="rt-06__cell">═</span><span class="rt-06__cell">═</span><span class="rt-06__cell">╗</span><span class="rt-06__cell rt-06__cell--hi">█</span><span class="rt-06__cell rt-06__cell--hi">▓</span><span class="rt-06__cell rt-06__cell--hi">▒</span><span class="rt-06__cell rt-06__cell--hi">░</span><span class="rt-06__cell"> </span>
        <span class="rt-06__cell">║</span><span class="rt-06__cell">A</span><span class="rt-06__cell">B</span><span class="rt-06__cell">║</span><span class="rt-06__cell">C</span><span class="rt-06__cell">D</span><span class="rt-06__cell">║</span><span class="rt-06__cell">─</span><span class="rt-06__cell">┼</span><span class="rt-06__cell">─</span><span class="rt-06__cell">┤</span><span class="rt-06__cell"> </span>
        <span class="rt-06__cell">╚</span><span class="rt-06__cell">═</span><span class="rt-06__cell">═</span><span class="rt-06__cell">╩</span><span class="rt-06__cell">═</span><span class="rt-06__cell">═</span><span class="rt-06__cell">╝</span><span class="rt-06__cell">└</span><span class="rt-06__cell">┴</span><span class="rt-06__cell">┘</span><span class="rt-06__cell"> </span><span class="rt-06__cell"> </span>
      </div>
      <p class="rt-06__inspect-p">Each box is <code>1ch</code> wide and one line-height tall. The frame is characters, not borders &mdash; a border would have to live between two cells, and there is no between.</p>
    </aside>

    <aside class="rt-06__pal">
      <h3 class="rt-06__inspect-h">CGA palette &mdash; 16 defined values</h3>
      <ul class="rt-06__pal-list">
        <li style="--rt-06-c: #000000">0 black</li>
        <li style="--rt-06-c: #0000aa">1 blue</li>
        <li style="--rt-06-c: #00aa00">2 green</li>
        <li style="--rt-06-c: #00aaaa">3 cyan</li>
        <li style="--rt-06-c: #aa0000">4 red</li>
        <li style="--rt-06-c: #aa00aa">5 magenta</li>
        <li style="--rt-06-c: #aa5500">6 brown</li>
        <li style="--rt-06-c: #aaaaaa">7 lt grey</li>
        <li style="--rt-06-c: #555555">8 dk grey</li>
        <li style="--rt-06-c: #5555ff">9 lt blue</li>
        <li style="--rt-06-c: #55ff55">10 lt green</li>
        <li style="--rt-06-c: #55ffff">11 lt cyan</li>
        <li style="--rt-06-c: #ff5555">12 lt red</li>
        <li style="--rt-06-c: #ff55ff">13 lt magenta</li>
        <li style="--rt-06-c: #ffff55">14 yellow</li>
        <li style="--rt-06-c: #ffffff">15 white</li>
      </ul>
    </aside>
  </div>
</section>
```
## CSS
```css
.rt-06 {
  --rt-06-cols: 80;
  --rt-06-k: #000000;
  --rt-06-blue: #0000aa;
  --rt-06-cyan: #00aaaa;
  --rt-06-ltgrey: #aaaaaa;
  --rt-06-dkgrey: #555555;
  --rt-06-ltcyan: #55ffff;
  --rt-06-yellow: #ffff55;
  --rt-06-white: #ffffff;
  --rt-06-red: #aa0000;
  --rt-06-mono: ui-monospace, SFMono-Regular, "Cascadia Mono", Consolas, "DejaVu Sans Mono", "Liberation Mono", monospace;
  --rt-06-bg: #c9ccd2;
  --rt-06-bg: oklch(84% 0.008 260);
  --rt-06-surface: #eef0f3;
  --rt-06-surface: oklch(95% 0.004 260);
  --rt-06-ink: #14171c;
  --rt-06-ink: oklch(19% 0.008 260);
  --rt-06-ink-2: #464e58;
  --rt-06-ink-2: oklch(42% 0.014 260);
  --rt-06-line: #9aa1ab;
  --rt-06-line: oklch(71% 0.012 260);
  --rt-06-acc: #1247c9;
  --rt-06-acc: oklch(45% 0.2 264);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-06-bg);
  color: var(--rt-06-ink);
  font-family: var(--rt-06-mono);
  -webkit-text-size-adjust: 100%;
}

.rt-06 *,
.rt-06 *::before,
.rt-06 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-06 {
    --rt-06-bg: #101318;
    --rt-06-bg: oklch(18% 0.008 260);
    --rt-06-surface: #1a1e25;
    --rt-06-surface: oklch(24% 0.01 260);
    --rt-06-ink: #eef1f5;
    --rt-06-ink: oklch(96% 0.004 260);
    --rt-06-ink-2: #a3abb6;
    --rt-06-ink-2: oklch(74% 0.012 260);
    --rt-06-line: #39414c;
    --rt-06-line: oklch(35% 0.014 260);
    --rt-06-acc: #7fa8ff;
    --rt-06-acc: oklch(76% 0.13 264);
  }
}

.rt-06[data-theme="dark"],
.rt-06:has(.rt-06__theme-input:checked) {
  --rt-06-bg: #101318;
  --rt-06-bg: oklch(18% 0.008 260);
  --rt-06-surface: #1a1e25;
  --rt-06-surface: oklch(24% 0.01 260);
  --rt-06-ink: #eef1f5;
  --rt-06-ink: oklch(96% 0.004 260);
  --rt-06-ink-2: #a3abb6;
  --rt-06-ink-2: oklch(74% 0.012 260);
  --rt-06-line: #39414c;
  --rt-06-line: oklch(35% 0.014 260);
  --rt-06-acc: #7fa8ff;
  --rt-06-acc: oklch(76% 0.13 264);
}

@media (prefers-color-scheme: light) {
  .rt-06:has(.rt-06__theme-input:checked) {
    --rt-06-bg: #101318;
    --rt-06-bg: oklch(18% 0.008 260);
    --rt-06-surface: #1a1e25;
    --rt-06-surface: oklch(24% 0.01 260);
    --rt-06-ink: #eef1f5;
    --rt-06-ink: oklch(96% 0.004 260);
    --rt-06-ink-2: #a3abb6;
    --rt-06-ink-2: oklch(74% 0.012 260);
    --rt-06-line: #39414c;
    --rt-06-line: oklch(35% 0.014 260);
    --rt-06-acc: #7fa8ff;
    --rt-06-acc: oklch(76% 0.13 264);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-06:has(.rt-06__theme-input:checked) {
    --rt-06-bg: #c9ccd2;
    --rt-06-bg: oklch(84% 0.008 260);
    --rt-06-surface: #eef0f3;
    --rt-06-surface: oklch(95% 0.004 260);
    --rt-06-ink: #14171c;
    --rt-06-ink: oklch(19% 0.008 260);
    --rt-06-ink-2: #464e58;
    --rt-06-ink-2: oklch(42% 0.014 260);
    --rt-06-line: #9aa1ab;
    --rt-06-line: oklch(71% 0.012 260);
    --rt-06-acc: #1247c9;
    --rt-06-acc: oklch(45% 0.2 264);
  }
}

.rt-06__sr {
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

.rt-06__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-06__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-06__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-06-line);
  background: var(--rt-06-surface);
  color: var(--rt-06-ink-2);
  cursor: pointer;
}

.rt-06__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-06__theme-input:focus-visible + .rt-06__theme-label {
  outline: 2px solid var(--rt-06-acc);
  outline-offset: 2px;
}

.rt-06__stage {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.6rem, 0.4rem + 1.5vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.1rem;
}

.rt-06__badge {
  margin: 0;
  justify-self: start;
  min-inline-size: 0;
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--rt-06-ink-2);
  border: 1px solid var(--rt-06-line);
  padding: 0.35rem 0.7rem;
  background: var(--rt-06-surface);
}

.rt-06__frame {
  min-inline-size: 0;
  background: #6d6f70;
  padding: clamp(0.5rem, 0.3rem + 1vw, 1rem);
  border-radius: 6px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.35), inset 0 -2px 0 rgba(0,0,0,0.4), 0 14px 30px -16px rgba(0,0,0,0.6);
}

.rt-06__screen {
  container-type: inline-size;
  min-inline-size: 0;
  overflow: hidden;
  background: var(--rt-06-blue);
  color: var(--rt-06-ltgrey);
  padding: 0;
  border: 2px solid #1b1d1f;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  align-content: start;
}

.rt-06__menu {
  display: flex;
  align-items: center;
  min-block-size: 1.6em;
  padding-inline: 0.5ch;
  background: var(--rt-06-ltgrey);
  color: var(--rt-06-k);
  font-size: clamp(0.66rem, 0.55rem + 0.6vw, 0.85rem);
  min-inline-size: 0;
  overflow: hidden;
  white-space: nowrap;
}
/* CGA dark red (index 4) rather than bright red (index 12): 4.71:1 on the
   light-grey menu bar where bright red is only 3.34:1, and both are real
   entries in the same 16-colour palette. */

.rt-06__menu-hi {
  color: #800000;
  font-weight: 700;
}

.rt-06__menu-gap {
  inline-size: 2ch;
  flex: none;
}

.rt-06__menu-tail {
  margin-inline-start: auto;
  color: #303030;
  padding-inline-start: 1ch;
}

.rt-06__art {
  margin: 0;
  padding: 0.5em 0;
  font-family: inherit;
  white-space: pre;
  color: var(--rt-06-ltcyan);
  min-inline-size: 0;
  overflow: hidden;
  font-size: min(0.95rem, 2.02cqi);
  line-height: 1.16;
  text-align: center;
}

@supports not (font-size: 1cqi) {
  .rt-06__art {
    font-size: clamp(0.35rem, 1.6vw, 0.95rem);
  }
}

.rt-06__art--narrow {
  display: block;
}

.rt-06__art--wide {
  display: none;
}

@media (min-width: 52rem) {
  .rt-06__art--narrow {
    display: none;
  }

  .rt-06__art--wide {
    display: block;
  }
}

.rt-06__status {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0 2ch;
  min-block-size: 1.6em;
  padding-inline: 0.5ch;
  background: var(--rt-06-ltgrey);
  color: var(--rt-06-k);
  font-size: clamp(0.66rem, 0.55rem + 0.6vw, 0.85rem);
  min-inline-size: 0;
}

.rt-06__key {
  color: #800000;
  font-weight: 700;
}

.rt-06__status-tail {
  margin-inline-start: auto;
  color: #303030;
}

.rt-06__inspect,
.rt-06__pal {
  min-inline-size: 0;
  background: var(--rt-06-surface);
  border: 1px solid var(--rt-06-line);
  padding: clamp(0.8rem, 0.6rem + 0.8vw, 1.1rem);
  display: grid;
  gap: 0.7rem;
  align-content: start;
}

.rt-06__inspect-h {
  margin: 0;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rt-06-ink-2);
}

.rt-06__cells {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1px;
  background: var(--rt-06-line);
  border: 1px solid var(--rt-06-line);
  min-inline-size: 0;
  font-size: clamp(0.8rem, 0.6rem + 1.4vw, 1.35rem);
}

.rt-06__cell {
  display: grid;
  place-items: center;
  aspect-ratio: 1 / 1;
  min-inline-size: 0;
  background: var(--rt-06-blue);
  color: var(--rt-06-ltcyan);
  line-height: 1;
}

.rt-06__cell--hi {
  color: var(--rt-06-yellow);
}

.rt-06__inspect-p {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.55;
  color: var(--rt-06-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-06__inspect-p code {
  background: var(--rt-06-bg);
  padding: 0.05em 0.3em;
}

.rt-06__pal-list {
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 7.5rem), 1fr));
  gap: 2px;
}

.rt-06__pal-list li {
  min-inline-size: 0;
  font-size: 0.68rem;
  padding: 0.4rem 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--rt-06-ink-2);
  border: 1px solid var(--rt-06-line);
}

.rt-06__pal-list li::before {
  content: "";
  inline-size: 16px;
  block-size: 16px;
  flex: none;
  background: var(--rt-06-c);
  border: 1px solid var(--rt-06-line);
}

@media (min-width: 56rem) {
  .rt-06__stage {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .rt-06__badge,
    .rt-06__frame {
    grid-column: 1 / -1;
  }
}
```
