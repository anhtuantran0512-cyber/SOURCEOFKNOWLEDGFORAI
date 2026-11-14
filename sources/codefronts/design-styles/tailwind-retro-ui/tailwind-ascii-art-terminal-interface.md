---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-ascii-art-terminal-interface/"
title: "Tailwind ASCII Art Terminal Interface"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A character-cell console on paper white rather than the usual black: box-drawn panels, a block-letter banner, and a working command line that takes input…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind ASCII Art Terminal Interface
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-ascii-art-terminal-interface/

A character-cell console on paper white rather than the usual black: box-drawn panels, a block-letter banner, and a working command line that takes input without a form element. The banner is aria-hidden with a real text alternative, because ASCII art read aloud is several hundred punctuation marks and no information.
## HTML
```html
<section class="twr-16 relative block w-full min-h-svh box-border bg-twr16-bg text-twr16-ink font-twr16-mono" aria-labelledby="twr-16-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-16-title">ASCII art terminal console</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-16-theme">
    <label class="grid place-items-center size-11 border border-twr16-line bg-twr16-paper text-twr16-ink2 cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-twr16-acc peer-focus-visible:outline-offset-2" for="twr-16-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark console</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-4 max-w-[64rem] mx-auto px-[clamp(0.6rem,0.4rem+1.5vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <p class="m-0 justify-self-start min-w-0 border border-twr16-line bg-twr16-paper px-2.5 py-1.5 text-[0.68rem] tracking-[0.12em] uppercase text-twr16-ink2">Character-cell console &middot; code page 437 frames &middot; ink on paper</p>

    <div class="min-w-0 grid gap-4 border border-twr16-line bg-twr16-paper p-[clamp(0.8rem,0.6rem+1.2vw,1.5rem)]">
      <div class="min-w-0">
        <pre class="m-0 min-w-0 overflow-x-auto whitespace-pre font-inherit leading-none text-twr16-ink text-[calc(var(--twr-16-cell)*0.9)]" aria-hidden="true">  ████      ██████    ██████  ██████  ██████
██    ██  ██        ██          ██      ██  
████████    ████    ██          ██      ██  
██    ██        ██  ██          ██      ██  
██    ██  ██████      ██████  ██████  ██████</pre>
        <p class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Block-letter banner reading ASCII, drawn in full-block characters.</p>
      </div>

      <div class="grid gap-4 min-w-0 md:grid-cols-2">
        <div class="min-w-0">
          <pre class="m-0 min-w-0 overflow-x-auto whitespace-pre font-inherit leading-[1.25] text-twr16-ink text-[var(--twr-16-cell)]" aria-hidden="true">┌─ SESSION ──────────────────┐
│ host   northgate.local     │
│ tty    /dev/ttyS0          │
│ rate   9600 8N1            │
│ codec  cp437               │
└────────────────────────────┘</pre>
          <p class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Session panel: host northgate.local, tty /dev/ttyS0, rate 9600 8N1, codec cp437.</p>
        </div>
        <div class="min-w-0">
          <pre class="m-0 min-w-0 overflow-x-auto whitespace-pre font-inherit leading-[1.25] text-twr16-ink text-[var(--twr-16-cell)]" aria-hidden="true">╔═ COMMANDS ═════════════════╗
║ help    list commands      ║
║ ver     print version      ║
║ dir     list files         ║
║ clear   empty the log      ║
╚════════════════════════════╝</pre>
          <p class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Commands panel: help lists commands, ver prints the version, dir lists files, clear empties the log.</p>
        </div>
      </div>

      <ul class="list-none m-0 p-3 min-w-0 grid gap-1 min-h-[9rem] max-h-[16rem] overflow-y-auto border border-twr16-line bg-twr16-bg text-[var(--twr-16-cell)] leading-relaxed" data-twr-16-log aria-live="polite" aria-relevant="additions" aria-label="Console output">
        <li class="min-w-0 [overflow-wrap:anywhere] text-twr16-ink">northgate console ready. type <b class="font-bold text-twr16-acc">help</b> and press Enter.</li>
      </ul>

      <template data-twr-16-line>
        <li class="min-w-0 [overflow-wrap:anywhere] text-twr16-ink data-[kind=err]:text-twr16-acc data-[kind=dim]:text-twr16-ink2"></li>
      </template>

      <div class="flex flex-wrap items-center gap-2 min-w-0">
        <label class="font-bold text-twr16-acc text-[var(--twr-16-cell)]" for="twr-16-input">C:\&gt;</label>
        <input class="flex-1 min-w-0 basis-40 min-h-11 px-2.5 py-2 border border-twr16-line bg-twr16-bg text-twr16-ink font-inherit text-[var(--twr-16-cell)] focus-visible:outline-2 focus-visible:outline-twr16-acc focus-visible:outline-offset-[-2px]" id="twr-16-input" type="text" data-twr-16-input autocomplete="off" spellcheck="false" placeholder="help">
        <button class="min-h-11 min-w-11 px-4 py-2 border border-twr16-ink bg-twr16-ink text-twr16-paper font-inherit text-[0.75rem] tracking-[0.12em] uppercase cursor-pointer focus-visible:outline-2 focus-visible:outline-twr16-acc focus-visible:outline-offset-2" type="button" data-twr-16-run>Run</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr16-paper: #f6f4ec;
  --color-twr16-paper: oklch(0.97 0.008 96);
  --color-twr16-ink: #1a1a16;
  --color-twr16-ink: oklch(0.21 0.008 96);
  --color-twr16-ink2: #5a584e;
  --color-twr16-ink2: oklch(0.47 0.012 96);
  --color-twr16-line: #b6b3a5;
  --color-twr16-line: oklch(0.76 0.014 96);
  --color-twr16-bg: #e2dfd4;
  --color-twr16-bg: oklch(0.90 0.012 96);
  --color-twr16-acc: #8a3a08;
  --color-twr16-acc: oklch(0.43 0.13 55);
  --font-twr16-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, 'Cascadia Mono', Consolas, monospace;
}

.twr-16 {
  --twr-16-cell: clamp(0.58rem, 0.42rem + 0.85vw, 0.85rem);
}

.twr-16:has(#twr-16-theme:checked) {
  --color-twr16-paper: #16160f;
  --color-twr16-paper: oklch(0.20 0.01 96);
  --color-twr16-ink: #f0eee2;
  --color-twr16-ink: oklch(0.95 0.008 96);
  --color-twr16-ink2: #aaa799;
  --color-twr16-ink2: oklch(0.73 0.013 96);
  --color-twr16-line: #464438;
  --color-twr16-line: oklch(0.38 0.014 96);
  --color-twr16-bg: #0e0e09;
  --color-twr16-bg: oklch(0.16 0.008 96);
  --color-twr16-acc: #ff9a52;
  --color-twr16-acc: oklch(0.78 0.13 55);
}
```

## JavaScript
```js
/* No form submit: a sandboxed iframe without form permission never fires one.
   Lines are cloned from the template so every utility exists in the source. */
(function () {
  var root = document.querySelector('.twr-16');
  if (!root) return;
  var log = root.querySelector('[data-twr-16-log]');
  var input = root.querySelector('[data-twr-16-input]');
  var run = root.querySelector('[data-twr-16-run]');
  var tpl = root.querySelector('[data-twr-16-line]');

  var replies = {
    help: ['help  ver  dir  clear', 'dim'],
    ver: ['northgate console 2.4 (cp437)', ''],
    dir: ['AUTOEXEC.BAT  CONFIG.SYS  README.TXT', '']
  };

  function print(text, kind) {
    var li = tpl.content.firstElementChild.cloneNode(true);
    if (kind) li.setAttribute('data-kind', kind);
    li.textContent = text;
    log.appendChild(li);
    while (log.childElementCount > 40) log.removeChild(log.firstElementChild);
    log.scrollTop = log.scrollHeight;
  }

  function submit() {
    var cmd = input.value.trim().toLowerCase();
    if (!cmd) return;
    print('C:\> ' + cmd, 'dim');
    if (cmd === 'clear') {
      log.textContent = '';
    } else if (replies[cmd]) {
      print(replies[cmd][0], replies[cmd][1]);
    } else {
      print('bad command or file name: ' + cmd, 'err');
    }
    input.value = '';
  }

  function onKey(e) { if (e.key === 'Enter') { e.preventDefault(); submit(); } }
  run.addEventListener('click', submit);
  input.addEventListener('keydown', onKey);

  root.__twrCleanup = function () {
    run.removeEventListener('click', submit);
    input.removeEventListener('keydown', onKey);
  };
})();
```
