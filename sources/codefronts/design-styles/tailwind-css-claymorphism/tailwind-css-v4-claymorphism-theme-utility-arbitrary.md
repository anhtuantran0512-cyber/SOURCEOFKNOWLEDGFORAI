---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-css-v4-claymorphism-theme-utility-arbitrary/"
title: "Tailwind CSS v4 Claymorphism: @theme Tokens, @utility & Arbitrary Values"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "The CSS collection's version of this demo could only mirror Tailwind's output."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS v4 Claymorphism: @theme Tokens, @utility & Arbitrary Values
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-css-v4-claymorphism-theme-utility-arbitrary/

The CSS collection's version of this demo could only mirror Tailwind's output. This one runs it. Three live buttons are built three ways — an @theme shadow token, a one-class @utility clay, and a raw arbitrary value — beside tabbed, copyable source for each. The tabs are native radios; the Copy button is the only script.
## HTML
```html
<section class="tcl-08 w-full min-h-svh grid place-items-center bg-tcl08-bg px-5 py-14 font-tcl08-sans text-tcl08-ink" aria-label="Tailwind CSS claymorphism implementation demo">
  <div class="grid w-full justify-items-center gap-[clamp(24px,4vw,36px)]">
    <header class="grid max-w-[62ch] gap-2.5 text-center">
      <h2 class="font-tcl08-display text-[clamp(28px,4vw,40px)] font-extrabold leading-[1.05] tracking-[-0.03em] text-balance">Clay, the Tailwind way</h2>
      <p class="text-[15px] leading-relaxed text-tcl08-mut text-pretty">Three live buttons, built three different ways, with identical output. Pick a tab to read the source, then copy it.</p>
    </header>
    <div class="group/lab grid w-full max-w-[1000px] items-center gap-[clamp(20px,3vw,30px)] min-[880px]:grid-cols-[minmax(0,.8fr)_minmax(0,1.2fr)]">
      <div class="grid justify-items-center gap-5">
        <button type="button" class="min-h-14 w-full max-w-[280px] cursor-pointer rounded-tcl08-clay bg-tcl08-clay px-7 font-tcl08-mono text-sm font-semibold shadow-tcl08-clay transition-[translate,box-shadow] duration-200 ease-[cubic-bezier(.34,1.4,.5,1)] hover:-translate-y-1 active:translate-y-0.5 active:shadow-tcl08-press focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl08-ink">shadow-tcl08-clay</button>
        <button type="button" class="min-h-14 w-full max-w-[280px] cursor-pointer px-7 font-tcl08-mono text-sm font-semibold tcl08-clay focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl08-ink">tcl08-clay</button>
        <button type="button" class="min-h-14 w-full max-w-[280px] cursor-pointer rounded-[40px] bg-[oklch(0.85_0.09_355)] px-7 font-tcl08-mono text-sm font-semibold shadow-[0_24px_44px_-12px_rgb(190_100_110/.55),inset_0_-16px_26px_-10px_rgb(190_100_110/.55),inset_0_18px_26px_-8px_rgb(255_255_255/.9)] transition-[translate,box-shadow] duration-200 hover:-translate-y-1 active:translate-y-0.5 active:shadow-[inset_0_14px_22px_-8px_rgb(190_100_110/.6)] focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl08-ink">shadow-[…arbitrary]</button>
      </div>
      <div class="grid gap-3 rounded-[36px] bg-tcl08-code p-[clamp(16px,2.6vw,24px)] text-tcl08-codeink shadow-tcl08-panel" data-tcl08-panel>
        <div class="flex flex-wrap items-center justify-between gap-3">
          <div role="radiogroup" aria-label="Implementation" class="flex gap-1 rounded-[22px] bg-tcl08-well p-1 shadow-[inset_0_8px_14px_-10px_oklch(0_0_0/0.8)]">
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-[18px] px-3.5 text-xs font-bold tracking-[0.04em] text-tcl08-codemut transition-colors hover:text-white has-checked:bg-tcl08-clay has-checked:text-tcl08-ink has-focus-visible:outline-2 has-focus-visible:outline-white"><input class="sr-only" type="radio" name="tcl-08-tab" id="tcl-08-t1" checked>@theme token</label>
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-[18px] px-3.5 text-xs font-bold tracking-[0.04em] text-tcl08-codemut transition-colors hover:text-white has-checked:bg-tcl08-clay has-checked:text-tcl08-ink has-focus-visible:outline-2 has-focus-visible:outline-white"><input class="sr-only" type="radio" name="tcl-08-tab" id="tcl-08-t2">@utility</label>
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-[18px] px-3.5 text-xs font-bold tracking-[0.04em] text-tcl08-codemut transition-colors hover:text-white has-checked:bg-tcl08-clay has-checked:text-tcl08-ink has-focus-visible:outline-2 has-focus-visible:outline-white"><input class="sr-only" type="radio" name="tcl-08-tab" id="tcl-08-t3">Arbitrary</label>
          </div>
          <button type="button" data-copy class="group/btn inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-[18px] border border-white/15 px-4 text-xs font-bold text-tcl08-codeink transition-colors hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white data-copied:border-tcl08-ok data-copied:text-tcl08-ok">
            <svg class="size-3.5 group-data-copied/btn:hidden" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="5" y="5" width="8.5" height="8.5" rx="2"/><path d="M11 5V3.5A1.5 1.5 0 0 0 9.5 2h-6A1.5 1.5 0 0 0 2 3.5v6A1.5 1.5 0 0 0 3.5 11H5"/></svg>
            <svg class="hidden size-3.5 group-data-copied/btn:block" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 8.5l3.2 3L13 4.5"/></svg>
            <span class="group-data-copied/btn:hidden">Copy</span><span class="hidden group-data-copied/btn:inline">Copied</span>
          </button>
        </div>
        <pre data-code="t1" class="m-0 hidden overflow-x-auto rounded-[22px] bg-tcl08-well px-4 py-3.5 font-tcl08-mono text-xs leading-[1.75] shadow-[inset_0_8px_14px_-10px_oklch(0_0_0/0.8)] group-has-[#tcl-08-t1:checked]/lab:block"><code>@theme {
  --radius-clay: 40px;
  --shadow-clay:
    0 24px 44px -12px var(--sh),
    inset 0 -16px 26px -10px var(--sh),
    inset 0 18px 26px -8px var(--hl);
  --shadow-clay-press: inset 0 14px 22px -8px var(--sh);
}

&lt;button class="rounded-clay bg-rose-200 shadow-clay
  hover:-translate-y-1 active:shadow-clay-press"&gt;</code></pre>
        <pre data-code="t2" class="m-0 hidden overflow-x-auto rounded-[22px] bg-tcl08-well px-4 py-3.5 font-tcl08-mono text-xs leading-[1.75] shadow-[inset_0_8px_14px_-10px_oklch(0_0_0/0.8)] group-has-[#tcl-08-t2:checked]/lab:block"><code>@utility clay {
  border-radius: 40px;
  background: var(--color-clay);
  box-shadow: 0 24px 44px -12px var(--sh),
    inset 0 -16px 26px -10px var(--sh),
    inset 0 18px 26px -8px var(--hl);
  transition: translate .2s, box-shadow .2s;
  &amp;:hover { translate: 0 -4px; }
  &amp;:active { translate: 0 2px; box-shadow: inset 0 14px 22px -8px var(--sh); }
}

&lt;button class="clay"&gt;</code></pre>
        <pre data-code="t3" class="m-0 hidden overflow-x-auto rounded-[22px] bg-tcl08-well px-4 py-3.5 font-tcl08-mono text-xs leading-[1.75] shadow-[inset_0_8px_14px_-10px_oklch(0_0_0/0.8)] group-has-[#tcl-08-t3:checked]/lab:block"><code>&lt;button class="rounded-[40px] bg-rose-200
  shadow-[0_24px_44px_-12px_rgb(190_100_110/.55),
  inset_0_-16px_26px_-10px_rgb(190_100_110/.55),
  inset_0_18px_26px_-8px_rgb(255_255_255/.9)]
  hover:-translate-y-1
  active:shadow-[inset_0_14px_22px_-8px_rgb(190_100_110/.6)]"&gt;</code></pre>
        <span role="status" aria-live="polite" class="sr-only"></span>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/60 px-4 py-2 text-center font-tcl08-mono text-[11.5px] text-tcl08-mut">underscores for spaces · shadow utilities replace, never merge · tokens theme, arbitrary values don’t</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl08-bg: #e5f0fc;
  --color-tcl08-bg: oklch(0.95 0.02 250);
  --color-tcl08-clay: #feb6d1;
  --color-tcl08-clay: oklch(0.85 0.09 355);
  --color-tcl08-shade: #b463808c;
  --color-tcl08-shade: oklch(0.6 0.11 358 / 0.55);
  --color-tcl08-light: #fffdffeb;
  --color-tcl08-light: oklch(1 0.01 340 / 0.92);
  --color-tcl08-ink: #2c243a;
  --color-tcl08-ink: oklch(0.28 0.04 300);
  --color-tcl08-mut: #5b536b;
  --color-tcl08-mut: oklch(0.46 0.04 300);
  --color-tcl08-code: #222234;
  --color-tcl08-code: oklch(0.26 0.035 285);
  --color-tcl08-well: #171626;
  --color-tcl08-well: oklch(0.21 0.03 285);
  --color-tcl08-codeink: #d2eef0;
  --color-tcl08-codeink: oklch(0.93 0.03 200);
  --color-tcl08-codemut: #bdbad6;
  --color-tcl08-codemut: oklch(0.8 0.04 290);
  --color-tcl08-ok: #86eaab;
  --color-tcl08-ok: oklch(0.86 0.13 155);
  --font-tcl08-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl08-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --radius-tcl08-clay: 40px;
  --shadow-tcl08-clay: 0 24px 44px -12px var(--color-tcl08-shade), inset 0 -16px 26px -10px var(--color-tcl08-shade), inset 0 18px 26px -8px var(--color-tcl08-light);
  --shadow-tcl08-press: 0 0 0 0 transparent, inset 0 14px 22px -8px var(--color-tcl08-shade), inset 0 0 0 0 transparent;
  --shadow-tcl08-panel: 0 30px 56px -22px oklch(0.3 0.05 290 / 0.6), inset 0 -14px 24px -14px oklch(0 0 0 / 0.6), inset 0 16px 24px -12px oklch(1 0 0 / 0.14);
}

@utility tcl08-clay {
  border-radius: var(--radius-tcl08-clay);
  background: var(--color-tcl08-clay);
  box-shadow: var(--shadow-tcl08-clay);
  transition: translate 0.2s cubic-bezier(0.34, 1.4, 0.5, 1), box-shadow 0.2s;

  &:hover {
    translate: 0 -4px;
  }

  &:active {
    translate: 0 2px;
    box-shadow: var(--shadow-tcl08-press);
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-08 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const copyText = async (text) => {
    try { await navigator.clipboard.writeText(text); return true; }
    catch {
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
  document.querySelectorAll('[data-tcl08-panel]').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const btn = panel.querySelector('[data-copy]');
    const status = panel.querySelector('[role="status"]');
    let t = 0;
    btn.addEventListener('click', async () => {
      const tab = panel.querySelector('input[name="tcl-08-tab"]:checked').id.slice(-2);
      const ok = await copyText(panel.querySelector('[data-code="' + tab + '"]').textContent);
      clearTimeout(t);
      if (ok) { btn.setAttribute('data-copied', ''); status.textContent = 'Code copied to clipboard'; }
      else status.textContent = 'Copy failed — select the code instead';
      t = setTimeout(() => { btn.removeAttribute('data-copied'); status.textContent = ''; }, 1800);
    });
  });
})();
```
