---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-form-field-help-tooltip-side-anchored-hint-pill/"
title: "Tailwind Form Field Help Tooltip with Side-Anchored Hint Pill"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "Small help circles beside form labels that reveal a one-line rule to the right, so the hint never covers the field above."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Form Field Help Tooltip with Side-Anchored Hint Pill
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-form-field-help-tooltip-side-anchored-hint-pill/

Small help circles beside form labels that reveal a one-line rule to the right, so the hint never covers the field above. The port's correction is semantic: the hint is wired to the INPUT with aria-describedby, which means a screen reader reads the rule while typing &mdash; not only when something is hovered.
## HTML
```html
<section class="ttp-21 w-full min-h-svh bg-white py-10 pr-[320px] pl-7 font-ttp21-sans max-xl:pr-7">
  <form class="mx-auto max-w-[400px]">
    <div class="mb-4.5">
      <label for="ttp21-f1" class="ttp21-label">Username
        <span class="group relative inline-flex items-center">
          <button type="button" aria-label="About the username field" aria-describedby="ttp21-h1" class="ttp21-icon">?</button>
          <span id="ttp21-h1" role="tooltip" class="ttp21-tip">Letters, numbers and underscores only. 3–20 characters.</span>
        </span>
      </label>
      <input id="ttp21-f1" aria-describedby="ttp21-h1" class="ttp21-input" type="text" value="kalani_a" readonly>
    </div>

    <div class="mb-4.5">
      <label for="ttp21-f2" class="ttp21-label">Email address
        <span class="group relative inline-flex items-center">
          <button type="button" aria-label="About the email field" aria-describedby="ttp21-h2" class="ttp21-icon">?</button>
          <span id="ttp21-h2" role="tooltip" class="ttp21-tip">Used for login and account recovery. Never shown publicly.</span>
        </span>
      </label>
      <input id="ttp21-f2" aria-describedby="ttp21-h2" class="ttp21-input" type="email" value="[email protected]" readonly>
    </div>

    <div class="mb-4.5">
      <label for="ttp21-f3" class="ttp21-label">Website
        <span class="group relative inline-flex items-center">
          <button type="button" aria-label="About the website field" aria-describedby="ttp21-h3" class="ttp21-icon">?</button>
          <span id="ttp21-h3" role="tooltip" class="ttp21-tip">Include https:// — displayed on your public profile page.</span>
        </span>
      </label>
      <input id="ttp21-f3" aria-describedby="ttp21-h3" class="ttp21-input" type="text" value="https://kalani.dev" readonly>
    </div>

    <div class="mb-4.5">
      <label for="ttp21-f4" class="ttp21-label">Bio
        <span class="group relative inline-flex items-center">
          <button type="button" aria-label="About the bio field" aria-describedby="ttp21-h4" class="ttp21-icon">?</button>
          <span id="ttp21-h4" role="tooltip" class="ttp21-tip">Shown below your name on your profile. Max 160 characters.</span>
        </span>
      </label>
      <input id="ttp21-f4" aria-describedby="ttp21-h4" class="ttp21-input" type="text" value="Building things on the web. Based in Honolulu." readonly>
    </div>

    <div>
      <label for="ttp21-f5" class="ttp21-label">Time zone
        <span class="group relative inline-flex items-center">
          <button type="button" aria-label="About the time zone field" aria-describedby="ttp21-h5" class="ttp21-icon">?</button>
          <span id="ttp21-h5" role="tooltip" class="ttp21-tip">Used to display timestamps and schedule notifications correctly.</span>
        </span>
      </label>
      <input id="ttp21-f5" aria-describedby="ttp21-h5" class="ttp21-input" type="text" value="Pacific/Honolulu (UTC −10:00)" readonly>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp21-ink: #111111;
  --color-ttp21-ink: oklch(0.18 0 0);
  --color-ttp21-field: #374151;
  --color-ttp21-field: oklch(0.37 0.03 260);
  --color-ttp21-icon: #6b7280;
  --color-ttp21-icon: oklch(0.55 0.02 260);
  --color-ttp21-chip: #e5e7eb;
  --color-ttp21-chip: oklch(0.92 0.005 260);
  --color-ttp21-chiphover: #cbd0d8;
  --color-ttp21-chiphover: oklch(0.85 0.008 260);
  --color-ttp21-pill: #18181b;
  --color-ttp21-pill: oklch(0.21 0.005 285);
  --color-ttp21-focus: #4f46e5;
  --color-ttp21-focus: oklch(0.51 0.21 277);
  --font-ttp21-sans: system-ui, -apple-system, sans-serif;
}

.ttp-21 {
  width: 100%;
  min-height: 100svh;
}
/* Five fields, one help affordance. */

.ttp-21 .ttp21-label {
  @apply mb-1.5 flex items-center gap-1.25 text-[12.5px] font-medium text-ttp21-ink;
}

.ttp-21 .ttp21-icon {
  @apply inline-flex h-4 w-4 shrink-0 cursor-help items-center justify-center rounded-full border-0 bg-ttp21-chip p-0 text-[9.5px] font-bold leading-none text-ttp21-icon transition-colors duration-100 hover:bg-ttp21-chiphover hover:text-ttp21-field focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp21-focus;
}

.ttp-21 .ttp21-tip {
  @apply pointer-events-none invisible absolute top-1/2 left-[calc(100%+8px)] z-100 block w-60 max-w-[calc(100vw-48px)] -translate-y-1/2 translate-x-1 rounded-[5px] bg-ttp21-pill px-2.75 py-1.75 text-[11.5px] leading-[1.4] text-white opacity-0 transition-[opacity,translate,visibility] duration-150 ease-[cubic-bezier(0.22,1,0.36,1)] after:absolute after:top-1/2 after:right-full after:-translate-y-1/2 after:border-4 after:border-transparent after:border-r-ttp21-pill after:content-[''] group-hover:visible group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-x-0 group-focus-within:opacity-100;
}

.ttp-21 .ttp21-input {
  @apply w-full rounded-md border border-ttp21-chip bg-[oklch(0.98_0_0)] px-2.75 py-2 text-[12.5px] text-ttp21-field outline-none focus:border-ttp21-focus focus:bg-white;
}
/* Under 640px there is no room to the side: the pill anchors above
   the label and the arrow moves to the bottom edge. */

@media (max-width: 639px) {
  .ttp-21 .ttp21-tip {
    @apply bottom-[calc(100%+8px)] top-auto left-0 w-[calc(100vw-40px)] max-w-[280px] translate-x-0 translate-y-1 group-hover:translate-y-0 group-focus-within:translate-y-0 after:top-full after:right-auto after:left-3 after:translate-y-0 after:border-r-transparent after:border-t-ttp21-pill;
  }
}
```
