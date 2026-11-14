---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/auto-detect-os-keyboard-shortcuts-cmd-ctrl-tailwind/"
title: "Auto-Detect OS Keyboard Shortcuts (Cmd or Ctrl) in Tailwind"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "Show ⌘ to Mac visitors and Ctrl to everyone else, automatically."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Auto-Detect OS Keyboard Shortcuts (Cmd or Ctrl) in Tailwind
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/auto-detect-os-keyboard-shortcuts-cmd-ctrl-tailwind/

Show ⌘ to Mac visitors and Ctrl to everyone else, automatically. Eight lines of script read navigator.userAgentData.platform and write one data-os attribute on the root; a @custom-variant kbd08-mac does the rest in markup. A manual macOS / Windows override uses aria-pressed:, because detection is a guess and the visitor knows better.
## HTML
```html
<section id="kbd-08-root" class="kbd-08 relative w-full min-h-svh scheme-light kbd08-dark:scheme-dark bg-kbd08-bg text-kbd08-ink font-kbd08-sans" aria-label="Auto OS detection shortcut demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[30rem] rounded-2xl border border-kbd08-rule bg-kbd08-panel p-6 shadow-[0_1px_2px_var(--color-kbd08-shade),0_16px_40px_-16px_var(--color-kbd08-shade)] sm:p-7">
        <div class="flex flex-wrap items-end justify-between gap-4">
          <div class="min-w-0">
            <p class="text-[10.5px] font-semibold uppercase tracking-[0.2em] text-kbd08-acc">Showing shortcuts for</p>
            <p class="mt-1.5 text-2xl font-semibold tracking-tight"><span class="hidden kbd08-mac:inline">macOS</span><span class="kbd08-mac:hidden">Windows / Linux</span></p>
            <p data-how class="mt-1 text-xs text-kbd08-mut">Default labels · script not run</p>
          </div>
          <div role="group" aria-label="Override platform" class="flex gap-1 rounded-xl bg-kbd08-seg p-1"><button type="button" data-pick="mac" aria-pressed="false" class="min-h-11 rounded-lg px-3.5 text-[13px] font-medium text-kbd08-mut transition-colors hover:text-kbd08-ink aria-pressed:bg-kbd08-segon aria-pressed:text-kbd08-ink aria-pressed:shadow-[0_0_0_1px_var(--color-kbd08-rule),0_1px_2px_var(--color-kbd08-shade)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-kbd08-acc">macOS</button><button type="button" data-pick="win" aria-pressed="false" class="min-h-11 rounded-lg px-3.5 text-[13px] font-medium text-kbd08-mut transition-colors hover:text-kbd08-ink aria-pressed:bg-kbd08-segon aria-pressed:text-kbd08-ink aria-pressed:shadow-[0_0_0_1px_var(--color-kbd08-rule),0_1px_2px_var(--color-kbd08-shade)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-kbd08-acc">Windows</button></div>
        </div>
        <ul class="mt-4 divide-y divide-kbd08-rule border-t border-kbd08-rule">
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Go to file</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd08-rim bg-kbd08-cap px-2 font-kbd08-mono text-[12px] font-medium leading-none text-kbd08-capink shadow-[0_1px_0_var(--color-kbd08-edge)]"><span class="hidden kbd08-mac:inline"><span aria-hidden="true" class="font-kbd08-sans text-[15px]">⌘</span><span class="sr-only">Command</span></span><span class="kbd08-mac:hidden">Ctrl</span></kbd><span class="text-[11px] text-kbd08-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd08-rim bg-kbd08-cap px-2 font-kbd08-mono text-[12px] font-medium leading-none text-kbd08-capink shadow-[0_1px_0_var(--color-kbd08-edge)]">P</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Find in project</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd08-rim bg-kbd08-cap px-2 font-kbd08-mono text-[12px] font-medium leading-none text-kbd08-capink shadow-[0_1px_0_var(--color-kbd08-edge)]"><span class="hidden kbd08-mac:inline"><span aria-hidden="true" class="font-kbd08-sans text-[15px]">⇧</span><span class="sr-only">Shift</span></span><span class="kbd08-mac:hidden">Shift</span></kbd><span class="text-[11px] text-kbd08-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd08-rim bg-kbd08-cap px-2 font-kbd08-mono text-[12px] font-medium leading-none text-kbd08-capink shadow-[0_1px_0_var(--color-kbd08-edge)]"><span class="hidden kbd08-mac:inline"><span aria-hidden="true" class="font-kbd08-sans text-[15px]">⌘</span><span class="sr-only">Command</span></span><span class="kbd08-mac:hidden">Ctrl</span></kbd><span class="text-[11px] text-kbd08-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd08-rim bg-kbd08-cap px-2 font-kbd08-mono text-[12px] font-medium leading-none text-kbd08-capink shadow-[0_1px_0_var(--color-kbd08-edge)]">F</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Comment line</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd08-rim bg-kbd08-cap px-2 font-kbd08-mono text-[12px] font-medium leading-none text-kbd08-capink shadow-[0_1px_0_var(--color-kbd08-edge)]"><span class="hidden kbd08-mac:inline"><span aria-hidden="true" class="font-kbd08-sans text-[15px]">⌘</span><span class="sr-only">Command</span></span><span class="kbd08-mac:hidden">Ctrl</span></kbd><span class="text-[11px] text-kbd08-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd08-rim bg-kbd08-cap px-2 font-kbd08-mono text-[12px] font-medium leading-none text-kbd08-capink shadow-[0_1px_0_var(--color-kbd08-edge)]">/</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Rename symbol</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd08-rim bg-kbd08-cap px-2 font-kbd08-mono text-[12px] font-medium leading-none text-kbd08-capink shadow-[0_1px_0_var(--color-kbd08-edge)]">F2</kbd></kbd></li>
        </ul>
        <p class="mt-4 border-t border-kbd08-rule pt-4 font-kbd08-mono text-[11.5px] text-kbd08-mut">one data-os attribute on the root · every key reads it</p>
      </section>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-08-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-08-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd08-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd08-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd08-dark:bg-transparent kbd08-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd08-dark:hidden">Light</span><span class="hidden kbd08-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd08-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-08:not(:has(#kbd-08-theme:checked)), .kbd-08:not(:has(#kbd-08-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-08:has(#kbd-08-theme:checked), .kbd-08:has(#kbd-08-theme:checked) *) {
      @slot;
    }
  }
}

@custom-variant kbd08-mac (&: where(.kbd-08[data-os=mac] *, .kbd-08[data-os=mac]));
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd08-bg: light-dark(#f1f2f4, #0e0f12);
  --color-kbd08-bg: light-dark(oklch(0.961 0.003 264.5), oklch(0.169 0.006 271));
  --color-kbd08-panel: light-dark(#ffffff, #16181d);
  --color-kbd08-panel: light-dark(oklch(1 0 0), oklch(0.209 0.01 268.2));
  --color-kbd08-shade: light-dark(#10203414, #00000080);
  --color-kbd08-shade: light-dark(oklch(0.241 0.044 254.8 / 0.08), oklch(0 0 0 / 0.5));
  --color-kbd08-ink: light-dark(#121418, #eceef1);
  --color-kbd08-ink: light-dark(oklch(0.191 0.009 264.3), oklch(0.948 0.005 258.3));
  --color-kbd08-mut: light-dark(#555d68, #9aa3af);
  --color-kbd08-mut: light-dark(oklch(0.475 0.02 256.4), oklch(0.712 0.02 255.6));
  --color-kbd08-rule: light-dark(#e5e7eb, #272b32);
  --color-kbd08-rule: light-dark(oklch(0.928 0.006 264.5), oklch(0.288 0.014 261.7));
  --color-kbd08-seg: light-dark(#eceef1, #0f1216);
  --color-kbd08-seg: light-dark(oklch(0.948 0.005 258.3), oklch(0.181 0.01 255.6));
  --color-kbd08-segon: light-dark(#ffffff, #2a2f38);
  --color-kbd08-segon: light-dark(oklch(1 0 0), oklch(0.304 0.018 262.2));
  --color-kbd08-cap: light-dark(#f8f9fb, #20242b);
  --color-kbd08-cap: light-dark(oklch(0.982 0.003 264.5), oklch(0.259 0.014 261.7));
  --color-kbd08-rim: light-dark(#cdd2d9, #3b414b);
  --color-kbd08-rim: light-dark(oklch(0.862 0.011 256.7), oklch(0.374 0.019 260.7));
  --color-kbd08-edge: light-dark(#b3b9c2, #050608);
  --color-kbd08-edge: light-dark(oklch(0.784 0.014 258.4), oklch(0.122 0.006 261.6));
  --color-kbd08-capink: light-dark(#1b1f25, #e9ecf0);
  --color-kbd08-capink: light-dark(oklch(0.238 0.013 258.4), oklch(0.942 0.006 255.5));
  --color-kbd08-acc: light-dark(#5b3fd6, #a594ff);
  --color-kbd08-acc: light-dark(oklch(0.496 0.217 283.6), oklch(0.726 0.152 289.3));
  --font-kbd08-sans: 'Geist', system-ui, sans-serif;
  --font-kbd08-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-08 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('kbd-08-root');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  // Presentation hint only: a platform string is spoofable and never a capability signal.
  const plat = navigator.userAgentData?.platform || navigator.platform || '';
  const how = root.querySelector('[data-how]');
  const set = (os, why) => {
    root.dataset.os = os;
    root.querySelectorAll('[data-pick]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.pick === os)));
    how.textContent = why;
  };
  set(/mac|iphone|ipad|ipod/i.test(plat) ? 'mac' : 'win', 'Detected from your browser');
  root.querySelectorAll('[data-pick]').forEach((b) => b.addEventListener('click', () => set(b.dataset.pick, 'Chosen manually')));
})();
```
