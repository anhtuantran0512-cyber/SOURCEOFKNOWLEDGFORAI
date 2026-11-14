---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-toast-notification-alert-components-clay/"
title: "Tailwind Toast Notification & Alert Components (Clay Style)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Four semantic clay toasts — success, info, warning, error — each dismissible in pure CSS, plus a chat-style bubble with an asymmetric tail."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Toast Notification & Alert Components (Clay Style)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-toast-notification-alert-components-clay/

Four semantic clay toasts — success, info, warning, error — each dismissible in pure CSS, plus a chat-style bubble with an asymmetric tail. The toast is a grid-rows-[1fr] that collapses to has-checked:grid-rows-[0fr], so the stack closes the gap smoothly. New: a Clear all control and an "all caught up" empty state, and 44px dismiss targets (were 34px).
## HTML
```html
<section class="tcl-18 group/demo w-full min-h-svh grid place-items-center bg-tcl18-bg bg-[radial-gradient(80%_55%_at_50%_0%,var(--color-tcl18-glow),transparent_66%)] px-5 py-14 font-tcl18-sans text-tcl18-ink" aria-label="Clay toast and floating alert bubbles demo">
  <div class="grid w-full justify-items-center gap-[clamp(20px,3.5vw,32px)]">
    <div class="grid w-full max-w-[460px] gap-3">
      <div class="flex items-center justify-between gap-3 px-1">
        <h2 class="font-tcl18-display text-xl font-extrabold tracking-[-0.02em]">Notifications</h2>
        <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full bg-tcl18-soft px-4 text-[13px] font-semibold text-tcl18-ink shadow-tcl18-chip transition-[translate,opacity] hover:-translate-y-0.5 has-checked:pointer-events-none has-checked:opacity-40 has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl18-ink"><input type="checkbox" id="tcl-18-all" class="sr-only">Clear all</label>
      </div>
      <div class="grid">
        <label role="status" class="tcl18-toast [--tcl18-h:150] [--tcl18-i:0] has-checked:grid-rows-[0fr] has-checked:scale-92 has-checked:opacity-0 has-checked:invisible group-has-[#tcl-18-all:checked]/demo:grid-rows-[0fr] group-has-[#tcl-18-all:checked]/demo:scale-92 group-has-[#tcl-18-all:checked]/demo:opacity-0 group-has-[#tcl-18-all:checked]/demo:invisible">
          <span class="tcl18-inner">
            <span aria-hidden="true" class="tcl18-puck"><svg viewBox="0 0 24 24" width="20" height="20"><path d="m5 12.6 4.2 4.2L19 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="grid min-w-0 flex-1 gap-0.5"><b class="tcl18-title">Snippet copied</b><span class="tcl18-body">All three shadow layers, ready to paste.</span></span>
            <input type="checkbox" class="sr-only" aria-label="Dismiss: snippet copied"><span aria-hidden="true" class="tcl18-x"></span>
          </span>
        </label>
        <label role="status" class="tcl18-toast [--tcl18-h:250] [--tcl18-i:1] has-checked:grid-rows-[0fr] has-checked:scale-92 has-checked:opacity-0 has-checked:invisible group-has-[#tcl-18-all:checked]/demo:grid-rows-[0fr] group-has-[#tcl-18-all:checked]/demo:scale-92 group-has-[#tcl-18-all:checked]/demo:opacity-0 group-has-[#tcl-18-all:checked]/demo:invisible">
          <span class="tcl18-inner">
            <span aria-hidden="true" class="tcl18-puck"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M12 8.2V8m0 3.4v4.4" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><circle cx="12" cy="12" r="8.4" fill="none" stroke="currentColor" stroke-width="2"/></svg></span>
            <span class="grid min-w-0 flex-1 gap-0.5"><b class="tcl18-title">Dark-mode variant available</b><span class="tcl18-body">Recalibrated shadows in demo 19.</span></span>
            <input type="checkbox" class="sr-only" aria-label="Dismiss: dark mode variant available"><span aria-hidden="true" class="tcl18-x"></span>
          </span>
        </label>
        <label role="status" class="tcl18-toast [--tcl18-h:80] [--tcl18-i:2] has-checked:grid-rows-[0fr] has-checked:scale-92 has-checked:opacity-0 has-checked:invisible group-has-[#tcl-18-all:checked]/demo:grid-rows-[0fr] group-has-[#tcl-18-all:checked]/demo:scale-92 group-has-[#tcl-18-all:checked]/demo:opacity-0 group-has-[#tcl-18-all:checked]/demo:invisible">
          <span class="tcl18-inner">
            <span aria-hidden="true" class="tcl18-puck"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M12 4.6 21 20H3z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M12 10.4v3.4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span>
            <span class="grid min-w-0 flex-1 gap-0.5"><b class="tcl18-title">Contrast is borderline</b><span class="tcl18-body">Body copy sits at 4.2:1 on this pastel.</span></span>
            <input type="checkbox" class="sr-only" aria-label="Dismiss: contrast is borderline"><span aria-hidden="true" class="tcl18-x"></span>
          </span>
        </label>
        <label role="alert" class="tcl18-toast [--tcl18-h:25] [--tcl18-i:3] has-checked:grid-rows-[0fr] has-checked:scale-92 has-checked:opacity-0 has-checked:invisible group-has-[#tcl-18-all:checked]/demo:grid-rows-[0fr] group-has-[#tcl-18-all:checked]/demo:scale-92 group-has-[#tcl-18-all:checked]/demo:opacity-0 group-has-[#tcl-18-all:checked]/demo:invisible">
          <span class="tcl18-inner">
            <span aria-hidden="true" class="tcl18-puck"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M7.5 7.5l9 9m0-9-9 9" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg></span>
            <span class="grid min-w-0 flex-1 gap-0.5"><b class="tcl18-title">Publish failed</b><span class="tcl18-body">Two snippets are missing a reduced-motion block.</span></span>
            <input type="checkbox" class="sr-only" aria-label="Dismiss: publish failed"><span aria-hidden="true" class="tcl18-x"></span>
          </span>
        </label>
        <p class="hidden items-center justify-center gap-2 rounded-[30px] bg-tcl18-soft px-5 py-6 text-center text-[14px] font-semibold text-tcl18-mut shadow-tcl18-well group-has-[#tcl-18-all:checked]/demo:flex group-[:not(:has(input[aria-label^=Dismiss]:not(:checked)))]/demo:flex"><span aria-hidden="true">✓</span>You're all caught up.</p>
      </div>
    </div>
    <div class="flex w-full max-w-[460px] items-end gap-3">
      <span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-full bg-[oklch(0.86_0.09_300)] text-[13px] font-bold shadow-tcl18-avatar">AR</span>
      <p class="flex-1 rounded-[32px_32px_32px_10px] bg-tcl18-bubble px-5 py-4 text-sm leading-normal shadow-tcl18-bubble text-pretty"><b class="mb-0.5 block text-xs font-bold text-tcl18-mut">Ari Rowe · 2m</b>Shipped the clay tokens — every component reads from <code class="rounded-lg bg-white/60 px-1.75 py-0.5 font-tcl18-mono text-[12.5px] shadow-[inset_0_3px_5px_-3px_var(--color-tcl18-shade)]">shadow-clay</code> now.</p>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/60 px-4 py-2 text-center font-tcl18-mono text-[11.5px] text-tcl18-mut">grid-rows-[1fr] → has-checked:grid-rows-[0fr] · index-staggered spring · clear-all via group-has</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl18-bg: #dfe8f7;
  --color-tcl18-bg: oklch(0.93 0.022 260);
  --color-tcl18-glow: #edf6ff;
  --color-tcl18-glow: oklch(0.97 0.02 260);
  --color-tcl18-soft: #eaf1fb;
  --color-tcl18-soft: oklch(0.955 0.015 260);
  --color-tcl18-bubble: #d5e6ff;
  --color-tcl18-bubble: oklch(0.92 0.04 260);
  --color-tcl18-shade: #5d729573;
  --color-tcl18-shade: oklch(0.55 0.06 260 / 0.45);
  --color-tcl18-light: #fbfffff2;
  --color-tcl18-light: oklch(1 0.01 260 / 0.95);
  --color-tcl18-ink: #182437;
  --color-tcl18-ink: oklch(0.26 0.04 260);
  --color-tcl18-mut: #4a5669;
  --color-tcl18-mut: oklch(0.45 0.035 260);
  --font-tcl18-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl18-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl18-chip: 0 10px 18px -12px var(--color-tcl18-shade), inset 0 -6px 10px -8px var(--color-tcl18-shade), inset 0 7px 10px -6px var(--color-tcl18-light);
  --shadow-tcl18-well: inset 0 10px 18px -8px var(--color-tcl18-shade), inset 0 -7px 13px -10px var(--color-tcl18-light);
  --shadow-tcl18-avatar: 0 12px 20px -10px var(--color-tcl18-shade), inset 0 -8px 13px -8px oklch(0.5 0.1 300 / 0.5), inset 0 10px 13px -6px var(--color-tcl18-light);
  --shadow-tcl18-bubble: 0 22px 38px -16px var(--color-tcl18-shade), inset 0 -13px 22px -12px oklch(0.5 0.08 260 / 0.45), inset 0 15px 22px -8px var(--color-tcl18-light);
  --animate-tcl18-rise: tcl18-rise 0.55s cubic-bezier(0.34, 1.5, 0.5, 1) backwards;

  @keyframes tcl18-rise {
    from {
      opacity: 0;
      translate: 0 26px;
      scale: 0.94;
    }

    to {
      opacity: 1;
      translate: 0 0;
      scale: 1;
    }
  }
}
/* Hue-driven toast: set [--tcl18-h:<hue>] and [--tcl18-i:<index>] on the label. */

@utility tcl18-toast {
  display: grid;
  grid-template-rows: 1fr;
  margin-bottom: 12px;
  border-radius: 30px;
  background: oklch(0.9 0.06 var(--tcl18-h));
  box-shadow: 0 30px 50px -18px oklch(0.5 0.11 var(--tcl18-h) / 0.5), inset 0 -14px 24px -12px oklch(0.5 0.11 var(--tcl18-h) / 0.5), inset 0 16px 24px -8px oklch(1 0.02 var(--tcl18-h) / 0.95);
  animation: var(--animate-tcl18-rise);
  animation-delay: calc(var(--tcl18-i) * 90ms);
  transition: grid-template-rows 0.38s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.34s, scale 0.38s cubic-bezier(0.4, 0, 0.2, 1), margin 0.38s, visibility 0.38s;

  &:has(:checked),
    :where(.tcl-18:has(#tcl-18-all:checked)) & {
    margin-bottom: 0;
  }

  @media (prefers-reduced-motion: reduce) {
    animation: none;
    transition-duration: 0.01ms;
  }
}

@utility tcl18-inner {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 0;
  overflow: hidden;
  padding: 16px 12px 16px 18px;
  transition: padding-block 0.38s cubic-bezier(0.4, 0, 0.2, 1);

  :where(.tcl18-toast:has(:checked)) &,
    :where(.tcl-18:has(#tcl-18-all:checked)) & {
    padding-block: 0;
  }
}

@utility tcl18-puck {
  display: grid;
  flex: none;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 16px;
  color: oklch(0.34 0.13 var(--tcl18-h));
  background: oklch(0.86 0.09 var(--tcl18-h));
  box-shadow: inset 0 9px 15px -6px oklch(0.5 0.12 var(--tcl18-h) / 0.6), inset 0 -6px 12px -8px oklch(1 0.02 var(--tcl18-h) / 0.9);
}

@utility tcl18-title {
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: oklch(0.27 0.09 var(--tcl18-h));
}

@utility tcl18-body {
  font-size: 12.5px;
  line-height: 1.45;
  color: oklch(0.36 0.07 var(--tcl18-h));
  text-wrap: pretty;
}

@utility tcl18-x {
  position: relative;
  flex: none;
  width: 44px;
  height: 44px;
  border-radius: 15px;
  cursor: pointer;
  background: oklch(0.95 0.03 var(--tcl18-h) / 0.75);
  box-shadow: 0 6px 11px -6px oklch(0.5 0.11 var(--tcl18-h) / 0.5), inset 0 -5px 9px -6px oklch(0.5 0.11 var(--tcl18-h) / 0.4), inset 0 6px 9px -5px oklch(1 0.02 var(--tcl18-h));
  transition: translate 0.2s;

  &:hover {
    translate: 0 -2px;
  }

  &::before,
    &::after {
    content: '';
    position: absolute;
    left: 50%;
    top: 50%;
    width: 15px;
    height: 2.4px;
    border-radius: 2px;
    background: oklch(0.38 0.09 var(--tcl18-h));
    translate: -50% -50%;
  }

  &::before {
    rotate: 45deg;
  }

  &::after {
    rotate: -45deg;
  }

  :where(.tcl18-toast:has(:focus-visible)) & {
    outline: 3px solid oklch(0.32 0.1 var(--tcl18-h));
    outline-offset: 2px;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-18 {
  width: 100%;
  min-height: 100svh;
}
```
