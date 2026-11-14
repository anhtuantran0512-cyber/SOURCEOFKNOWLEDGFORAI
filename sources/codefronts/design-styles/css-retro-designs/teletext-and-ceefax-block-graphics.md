---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/teletext-and-ceefax-block-graphics/"
title: "Teletext and Ceefax Block Graphics"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "The British broadcast text format, rebuilt cell by cell: 40&times;25 characters, seven saturated colours on black, double-height headline rows, and mosaic…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Teletext and Ceefax Block Graphics
Source: https://codefronts.com/design-styles/css-retro-designs/teletext-and-ceefax-block-graphics/

The British broadcast text format, rebuilt cell by cell: 40&times;25 characters, seven saturated colours on black, double-height headline rows, and mosaic graphics assembled from 2&times;3 subcells inside single character cells. The palette is exactly seven colours plus black for a hardware reason, and the demo says which one.
## HTML
```html
<section class="rt-07" aria-labelledby="rt-07-title">
  <h2 class="rt-07__sr" id="rt-07-title">Teletext Level 1 page with mosaic block graphics</h2>

  <div class="rt-07__theme">
    <input class="rt-07__theme-input" type="checkbox" id="rt-07-theme">
    <label class="rt-07__theme-label" for="rt-07-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-07__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-07__stage">
    <p class="rt-07__badge">Teletext Level 1 &middot; 40 &times; 25 cells &middot; 7 colours + black</p>

    <div class="rt-07__set">
      <div class="rt-07__page">
        <p class="rt-07__row rt-07__hdr"><span class="rt-07__c-w">P170</span> <span class="rt-07__c-c">CEEFAX 170</span> <span class="rt-07__c-g">Mon 31 Aug</span> <span class="rt-07__c-y rt-07__flash">20:14/32</span></p>

        <p class="rt-07__row rt-07__dbl rt-07__c-y">WEATHER</p>
        <p class="rt-07__row rt-07__dbl-pad" aria-hidden="true">&nbsp;</p>

        <p class="rt-07__row rt-07__c-c">────────────────────────────────────────</p>

        <div class="rt-07__mosaic-wrap">
          <div class="rt-07__mosaic" aria-hidden="true"><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx rt-07__sx--y"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx rt-07__sx--w"></i></span><span class="rt-07__mc"><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--w"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i><i class="rt-07__sx"></i><i class="rt-07__sx rt-07__sx--c"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span><span class="rt-07__mc"><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i><i class="rt-07__sx"></i></span></div>
          <p class="rt-07__alt">Mosaic graphic: a yellow sun behind a white cloud, with three cyan rain strokes below it.</p>
        </div>

        <p class="rt-07__row rt-07__c-w">SOUTH EAST&nbsp;&nbsp;&nbsp;&nbsp;<span class="rt-07__c-y">18C</span>&nbsp;&nbsp;SUNNY SPELLS</p>
        <p class="rt-07__row rt-07__c-w">MIDLANDS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="rt-07__c-y">15C</span>&nbsp;&nbsp;SHOWERS LATER</p>
        <p class="rt-07__row rt-07__c-w">HIGHLANDS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="rt-07__c-y">11C</span>&nbsp;&nbsp;RAIN, WINDY</p>
        <p class="rt-07__row rt-07__c-w">N IRELAND&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="rt-07__c-y">14C</span>&nbsp;&nbsp;BRIGHT, COOL</p>

        <p class="rt-07__row rt-07__c-c">────────────────────────────────────────</p>
        <p class="rt-07__row rt-07__c-g">OUTLOOK  Unsettled through midweek with</p>
        <p class="rt-07__row rt-07__c-g">brighter intervals from Thursday.</p>

        <nav class="rt-07__fastext" aria-label="FASTEXT links">
          <ul class="rt-07__fastext-list">
            <li><button class="rt-07__fx rt-07__fx--r" type="button">Index</button></li>
            <li><button class="rt-07__fx rt-07__fx--g" type="button">Regions</button></li>
            <li><button class="rt-07__fx rt-07__fx--y" type="button">Charts</button></li>
            <li><button class="rt-07__fx rt-07__fx--c" type="button">Travel</button></li>
          </ul>
        </nav>
      </div>
    </div>

    <aside class="rt-07__legend">
      <h3 class="rt-07__legend-h">Level 1 palette &mdash; three bits, eight states</h3>
      <ul class="rt-07__legend-list">
        <li><span class="rt-07__chip" style="--rt-07-c: #ff0000"></span>100 red</li>
        <li><span class="rt-07__chip" style="--rt-07-c: #00ff00"></span>010 green</li>
        <li><span class="rt-07__chip" style="--rt-07-c: #ffff00"></span>110 yellow</li>
        <li><span class="rt-07__chip" style="--rt-07-c: #0000ff"></span>001 blue</li>
        <li><span class="rt-07__chip" style="--rt-07-c: #ff00ff"></span>101 magenta</li>
        <li><span class="rt-07__chip" style="--rt-07-c: #00ffff"></span>011 cyan</li>
        <li><span class="rt-07__chip" style="--rt-07-c: #ffffff"></span>111 white</li>
        <li><span class="rt-07__chip" style="--rt-07-c: #000000"></span>000 black</li>
      </ul>
      <p class="rt-07__legend-p">One bit per primary, fully on or fully off. That is the whole palette &mdash; there is no bit left for an intermediate value.</p>
    </aside>
  </div>
</section>
```
## CSS
```css
.rt-07 {
  --rt-07-cols: 40;
  --rt-07-r: #ff0000;
  --rt-07-g: #00ff00;
  --rt-07-y: #ffff00;
  --rt-07-b: #0000ff;
  --rt-07-m: #ff00ff;
  --rt-07-c: #00ffff;
  --rt-07-w: #ffffff;
  --rt-07-k: #000000;
  --rt-07-mono: ui-monospace, SFMono-Regular, "Cascadia Mono", Consolas, "DejaVu Sans Mono", monospace;
  --rt-07-bg: #23252b;
  --rt-07-bg: oklch(26% 0.008 275);
  --rt-07-surface: #32353d;
  --rt-07-surface: oklch(34% 0.01 275);
  --rt-07-ink: #f0f1f5;
  --rt-07-ink: oklch(96% 0.004 275);
  --rt-07-ink-2: #b3b7c0;
  --rt-07-ink-2: oklch(78% 0.01 275);
  --rt-07-line: #4c505a;
  --rt-07-line: oklch(43% 0.012 275);
  --rt-07-acc: #7fd7ff;
  --rt-07-acc: oklch(84% 0.11 225);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-07-bg);
  color: var(--rt-07-ink);
  font-family: var(--rt-07-mono);
  -webkit-text-size-adjust: 100%;
}

.rt-07 *,
.rt-07 *::before,
.rt-07 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .rt-07 {
    --rt-07-bg: #dcdee4;
    --rt-07-bg: oklch(89% 0.007 275);
    --rt-07-surface: #f3f4f7;
    --rt-07-surface: oklch(96% 0.004 275);
    --rt-07-ink: #16181d;
    --rt-07-ink: oklch(20% 0.008 275);
    --rt-07-ink-2: #4a4f59;
    --rt-07-ink-2: oklch(43% 0.013 275);
    --rt-07-line: #a8adb8;
    --rt-07-line: oklch(74% 0.012 275);
    --rt-07-acc: #0f5f8a;
    --rt-07-acc: oklch(45% 0.11 232);
  }
}

.rt-07[data-theme="dark"] {
  --rt-07-bg: #23252b;
  --rt-07-bg: oklch(26% 0.008 275);
  --rt-07-surface: #32353d;
  --rt-07-surface: oklch(34% 0.01 275);
  --rt-07-ink: #f0f1f5;
  --rt-07-ink: oklch(96% 0.004 275);
  --rt-07-ink-2: #b3b7c0;
  --rt-07-ink-2: oklch(78% 0.01 275);
  --rt-07-line: #4c505a;
  --rt-07-line: oklch(43% 0.012 275);
  --rt-07-acc: #7fd7ff;
  --rt-07-acc: oklch(84% 0.11 225);
}

@media (prefers-color-scheme: light) {
  .rt-07:has(.rt-07__theme-input:checked) {
    --rt-07-bg: #23252b;
    --rt-07-bg: oklch(26% 0.008 275);
    --rt-07-surface: #32353d;
    --rt-07-surface: oklch(34% 0.01 275);
    --rt-07-ink: #f0f1f5;
    --rt-07-ink: oklch(96% 0.004 275);
    --rt-07-ink-2: #b3b7c0;
    --rt-07-ink-2: oklch(78% 0.01 275);
    --rt-07-line: #4c505a;
    --rt-07-line: oklch(43% 0.012 275);
    --rt-07-acc: #7fd7ff;
    --rt-07-acc: oklch(84% 0.11 225);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-07:has(.rt-07__theme-input:checked) {
    --rt-07-bg: #dcdee4;
    --rt-07-bg: oklch(89% 0.007 275);
    --rt-07-surface: #f3f4f7;
    --rt-07-surface: oklch(96% 0.004 275);
    --rt-07-ink: #16181d;
    --rt-07-ink: oklch(20% 0.008 275);
    --rt-07-ink-2: #4a4f59;
    --rt-07-ink-2: oklch(43% 0.013 275);
    --rt-07-line: #a8adb8;
    --rt-07-line: oklch(74% 0.012 275);
    --rt-07-acc: #0f5f8a;
    --rt-07-acc: oklch(45% 0.11 232);
  }
}

.rt-07__sr {
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

.rt-07__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-07__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-07__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-07-line);
  background: var(--rt-07-surface);
  color: var(--rt-07-ink-2);
  cursor: pointer;
}

.rt-07__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-07__theme-input:focus-visible + .rt-07__theme-label {
  outline: 2px solid var(--rt-07-acc);
  outline-offset: 2px;
}

.rt-07__stage {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.6rem, 0.4rem + 1.5vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.1rem;
}

.rt-07__badge {
  margin: 0;
  justify-self: start;
  min-inline-size: 0;
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--rt-07-ink-2);
  border: 1px solid var(--rt-07-line);
  padding: 0.35rem 0.7rem;
  background: var(--rt-07-surface);
}

.rt-07__set {
  min-inline-size: 0;
  background: #3a3d42;
  padding: clamp(0.5rem, 0.3rem + 1vw, 0.9rem);
  border-radius: 8px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.2), 0 16px 34px -18px rgba(0,0,0,0.7);
}

.rt-07__page {
  container-type: inline-size;
  min-inline-size: 0;
  background: var(--rt-07-k);
  color: var(--rt-07-w);
  padding: 0.5em 0.5ch;
  overflow: hidden;
  font-size: min(1rem, 4.4cqi);
  line-height: 1.28;
  letter-spacing: 0.02em;
}

@supports not (font-size: 1cqi) {
  .rt-07__page {
    font-size: clamp(0.5rem, 2.6vw, 1rem);
  }
}

.rt-07__row {
  margin: 0;
  white-space: pre;
  overflow: hidden;
  min-inline-size: 0;
}

.rt-07__hdr {
  background: var(--rt-07-k);
}

.rt-07__c-r {
  color: var(--rt-07-r);
}

.rt-07__c-g {
  color: var(--rt-07-g);
}

.rt-07__c-y {
  color: var(--rt-07-y);
}

.rt-07__c-c {
  color: var(--rt-07-c);
}

.rt-07__c-w {
  color: var(--rt-07-w);
}

.rt-07__c-m {
  color: var(--rt-07-m);
}

.rt-07__dbl {
  font-weight: 700;
  transform: scaleY(2);
  transform-origin: top left;
  letter-spacing: 0.06em;
}

.rt-07__dbl-pad {
  block-size: 1.28em;
}

.rt-07__flash {
  animation: rt-07-flash 2s steps(1, end) infinite;
}

@keyframes rt-07-flash {
  0%,
    74% {
    opacity: 1;
  }

  75%,
    100% {
    opacity: 0.25;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rt-07__flash {
    animation: none;
    opacity: 1;
  }
}

.rt-07__mosaic-wrap {
  display: grid;
  gap: 0.5em;
  padding-block: 0.4em;
  min-inline-size: 0;
}

.rt-07__mosaic {
  display: grid;
  grid-template-columns: repeat(15, 2ch);
  gap: 0;
  justify-content: start;
  min-inline-size: 0;
}

.rt-07__mc {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(3, 1fr);
  block-size: 3ch;
}

.rt-07__sx {
  display: block;
  background: transparent;
}

.rt-07__sx--y {
  background: var(--rt-07-y);
}

.rt-07__sx--w {
  background: var(--rt-07-w);
}

.rt-07__sx--c {
  background: var(--rt-07-c);
}

.rt-07__sx--b {
  background: var(--rt-07-b);
}

.rt-07__alt {
  margin: 0;
  font-size: 0.78em;
  line-height: 1.4;
  color: var(--rt-07-c);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-07__fastext {
  margin-block-start: 0.6em;
  min-inline-size: 0;
}

.rt-07__fastext-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
}

.rt-07__fx {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 0.4rem 0.7rem;
  flex: 1 1 auto;
  border: 0;
  font: inherit;
  font-size: 0.82em;
  font-weight: 700;
  cursor: pointer;
  color: var(--rt-07-k);
}

.rt-07__fx--r {
  background: var(--rt-07-r);
  color: #000000;
}

.rt-07__fx--g {
  background: var(--rt-07-g);
}

.rt-07__fx--y {
  background: var(--rt-07-y);
}

.rt-07__fx--c {
  background: var(--rt-07-c);
}

.rt-07__fx:focus-visible {
  outline: 2px solid var(--rt-07-w);
  outline-offset: -4px;
}

.rt-07__legend {
  min-inline-size: 0;
  background: var(--rt-07-surface);
  border: 1px solid var(--rt-07-line);
  padding: clamp(0.8rem, 0.6rem + 0.8vw, 1.1rem);
  display: grid;
  gap: 0.7rem;
  align-content: start;
}

.rt-07__legend-h {
  margin: 0;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rt-07-ink-2);
}

.rt-07__legend-list {
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 8rem), 1fr));
  gap: 0.35rem;
}

.rt-07__legend-list li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  min-inline-size: 0;
  color: var(--rt-07-ink-2);
}

.rt-07__chip {
  inline-size: 18px;
  block-size: 18px;
  flex: none;
  background: var(--rt-07-c);
  border: 1px solid var(--rt-07-line);
}

.rt-07__legend-p {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.55;
  color: var(--rt-07-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

@media (min-width: 56rem) {
  .rt-07__stage {
    grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr);
  }

  .rt-07__badge {
    grid-column: 1 / -1;
  }
}
```
