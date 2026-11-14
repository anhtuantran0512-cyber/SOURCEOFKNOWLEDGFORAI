---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-product-return-refund-request-form/"
title: "Tailwind Product Return and Refund Request Form"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's self-serve returns portal, ported one-for-one to Tailwind v4: order items as checkbox cards with product photos, each expanding to ask…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Product Return and Refund Request Form
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-product-return-refund-request-form/

The CSS collection's self-serve returns portal, ported one-for-one to Tailwind v4: order items as checkbox cards with product photos, each expanding to ask its own quantity and reason (group-has-[.tf-14__pick:checked]/it:grid); a final-sale item that is genuinely disabled and says why; refund to card or store credit with a 10% bonus; drop-off or courier return; a dark live summary; and a QR return label on confirm.
## HTML
```html
<div class="tf-14 group/root relative block min-h-svh w-full bg-tf14-bg pt-[72px] font-tf14-sans leading-[normal] text-tf14-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3.5rem)]">
    <div class="grid w-full max-w-[46rem] gap-6 rounded-3xl border border-tf14-line bg-tf14-card p-[clamp(1.25rem,4vw,2.5rem)] shadow-[0_30px_70px_-40px_rgba(0,0,0,.35)]" role="form" aria-labelledby="tf-14-title">
      <header class="flex flex-wrap items-end justify-between gap-4">
        <div><p class="mb-[.2rem] text-[.8rem] font-bold tracking-[.06em] text-tf14-hot uppercase">Returns</p><h2 id="tf-14-title" class="text-[clamp(1.7rem,4vw,2.2rem)] font-extrabold tracking-[-.035em]">Start a return</h2></div>
        <dl class="flex gap-5"><div><dt class="text-[.72rem] font-semibold tracking-[.06em] text-tf14-muted uppercase">Order</dt><dd class="mt-[.1rem] text-[.92rem] font-bold">#NW-48213</dd></div><div><dt class="text-[.72rem] font-semibold tracking-[.06em] text-tf14-muted uppercase">Delivered</dt><dd class="mt-[.1rem] text-[.92rem] font-bold">28 Sep 2026</dd></div><div><dt class="text-[.72rem] font-semibold tracking-[.06em] text-tf14-muted uppercase">Return by</dt><dd class="mt-[.1rem] text-[.92rem] font-bold">28 Oct 2026</dd></div></dl>
      </header>
      <fieldset class="grid min-w-0 gap-[.6rem]">
        <legend class="mb-[.7rem] p-0 text-[.95rem] font-bold">Which items are you returning?</legend>
        <div class="tf-14__item group/it overflow-hidden rounded-[1.1rem] border-[1.5px] border-tf14-line bg-tf14-card [transition:border-color_.25s,box-shadow_.3s_var(--ease-tf14)] [&:not(.is-final)]:hover:border-[color-mix(in_oklab,var(--color-tf14-ink)_30%,var(--color-tf14-line))] has-[.tf-14\_\_pick:checked]:border-tf14-ink has-[.tf-14\_\_pick:checked]:shadow-[0_14px_30px_-20px_rgba(0,0,0,.45)] has-[.tf-14\_\_pick:focus-visible]:outline-2 has-[.tf-14\_\_pick:focus-visible]:outline-offset-3 has-[.tf-14\_\_pick:focus-visible]:outline-tf14-hot [&.is-final]:bg-tf14-soft forced-colors:has-[.tf-14\_\_pick:checked]:outline-2 forced-colors:has-[.tf-14\_\_pick:checked]:outline-[Highlight]">
          <label class="relative grid cursor-pointer grid-cols-[auto_1fr_auto_auto] items-center gap-[.95rem] py-3 pr-4 pl-3 group-[.is-final]/it:cursor-not-allowed group-[.is-final]/it:text-tf14-muted max-[34rem]:grid-cols-[auto_1fr_auto]"><input type="checkbox" class="tf-14__pick absolute inset-0 m-0 cursor-pointer opacity-0" data-price="129" data-max="1"><img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200&h=200&fit=crop&auto=format&q=70" width="72" height="72" alt="" loading="lazy" decoding="async" class="size-[4.25rem] rounded-[.8rem] bg-tf14-soft object-cover"><span><b class="block font-bold">Velocity Runner</b><small class="mt-[.1rem] block text-[.85rem] text-tf14-muted group-[.is-final]/it:font-semibold group-[.is-final]/it:text-tf14-hot">Crimson · UK 9</small></span><em class="font-bold tabular-nums not-italic max-[34rem]:col-start-2 max-[34rem]:row-start-2">$129.00</em><i class="grid size-6 place-items-center rounded-[.45rem] border-[1.5px] border-tf14-line [transition:all_.25s_var(--ease-tf14)] after:h-[.4rem] after:w-[.7rem] after:-translate-y-px after:scale-0 after:-rotate-45 after:border-b-[2.5px] after:border-l-[2.5px] after:border-white after:[transition:scale_.3s_var(--ease-tf14)] after:content-[''] group-has-[.tf-14\_\_pick:checked]/it:border-tf14-hot group-has-[.tf-14\_\_pick:checked]/it:bg-tf14-hot group-has-[.tf-14\_\_pick:checked]/it:after:scale-100 group-[.is-final]/it:border-dashed" aria-hidden="true"></i></label>
          <div class="ml-[5.95rem] hidden grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[.8rem] px-4 pb-4 group-has-[.tf-14\_\_pick:checked]/it:grid group-has-[.tf-14\_\_pick:checked]/it:animate-tf14-in max-[34rem]:ml-0">
            <div class="grid gap-[.35rem]"><label for="tf-14-r1" class="text-[.8rem] font-bold">Reason</label><select id="tf-14-r1" class="tf-14__reason min-h-[2.8rem] w-full cursor-pointer rounded-[.7rem] border border-tf14-line bg-tf14-soft px-[.8rem] py-2 text-[.95rem] text-tf14-ink focus-visible:border-tf14-ink focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf14-hot)_25%,transparent)] focus-visible:outline-none [&.is-missing]:border-tf14-hot"><option value="">Select a reason</option><option>Too small</option><option>Too large</option><option>Not as described</option><option>Damaged or defective</option><option>Changed my mind</option></select></div>
          </div>
        </div>
        <div class="tf-14__item group/it overflow-hidden rounded-[1.1rem] border-[1.5px] border-tf14-line bg-tf14-card [transition:border-color_.25s,box-shadow_.3s_var(--ease-tf14)] [&:not(.is-final)]:hover:border-[color-mix(in_oklab,var(--color-tf14-ink)_30%,var(--color-tf14-line))] has-[.tf-14\_\_pick:checked]:border-tf14-ink has-[.tf-14\_\_pick:checked]:shadow-[0_14px_30px_-20px_rgba(0,0,0,.45)] has-[.tf-14\_\_pick:focus-visible]:outline-2 has-[.tf-14\_\_pick:focus-visible]:outline-offset-3 has-[.tf-14\_\_pick:focus-visible]:outline-tf14-hot [&.is-final]:bg-tf14-soft forced-colors:has-[.tf-14\_\_pick:checked]:outline-2 forced-colors:has-[.tf-14\_\_pick:checked]:outline-[Highlight]">
          <label class="relative grid cursor-pointer grid-cols-[auto_1fr_auto_auto] items-center gap-[.95rem] py-3 pr-4 pl-3 group-[.is-final]/it:cursor-not-allowed group-[.is-final]/it:text-tf14-muted max-[34rem]:grid-cols-[auto_1fr_auto]"><input type="checkbox" class="tf-14__pick absolute inset-0 m-0 cursor-pointer opacity-0" data-price="34" data-max="3"><img src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=200&h=200&fit=crop&auto=format&q=70" width="72" height="72" alt="" loading="lazy" decoding="async" class="size-[4.25rem] rounded-[.8rem] bg-tf14-soft object-cover"><span><b class="block font-bold">Everyday Organic Tee</b><small class="mt-[.1rem] block text-[.85rem] text-tf14-muted group-[.is-final]/it:font-semibold group-[.is-final]/it:text-tf14-hot">White · M · ×3</small></span><em class="font-bold tabular-nums not-italic max-[34rem]:col-start-2 max-[34rem]:row-start-2">$34.00 ea</em><i class="grid size-6 place-items-center rounded-[.45rem] border-[1.5px] border-tf14-line [transition:all_.25s_var(--ease-tf14)] after:h-[.4rem] after:w-[.7rem] after:-translate-y-px after:scale-0 after:-rotate-45 after:border-b-[2.5px] after:border-l-[2.5px] after:border-white after:[transition:scale_.3s_var(--ease-tf14)] after:content-[''] group-has-[.tf-14\_\_pick:checked]/it:border-tf14-hot group-has-[.tf-14\_\_pick:checked]/it:bg-tf14-hot group-has-[.tf-14\_\_pick:checked]/it:after:scale-100 group-[.is-final]/it:border-dashed" aria-hidden="true"></i></label>
          <div class="ml-[5.95rem] hidden grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[.8rem] px-4 pb-4 group-has-[.tf-14\_\_pick:checked]/it:grid group-has-[.tf-14\_\_pick:checked]/it:animate-tf14-in max-[34rem]:ml-0">
            <div class="grid gap-[.35rem]"><label for="tf-14-q2" class="text-[.8rem] font-bold">Quantity</label><select id="tf-14-q2" class="tf-14__qty min-h-[2.8rem] w-full cursor-pointer rounded-[.7rem] border border-tf14-line bg-tf14-soft px-[.8rem] py-2 text-[.95rem] text-tf14-ink focus-visible:border-tf14-ink focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf14-hot)_25%,transparent)] focus-visible:outline-none [&.is-missing]:border-tf14-hot"><option>1</option><option>2</option><option selected>3</option></select></div>
            <div class="grid gap-[.35rem]"><label for="tf-14-r2" class="text-[.8rem] font-bold">Reason</label><select id="tf-14-r2" class="tf-14__reason min-h-[2.8rem] w-full cursor-pointer rounded-[.7rem] border border-tf14-line bg-tf14-soft px-[.8rem] py-2 text-[.95rem] text-tf14-ink focus-visible:border-tf14-ink focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf14-hot)_25%,transparent)] focus-visible:outline-none [&.is-missing]:border-tf14-hot"><option value="">Select a reason</option><option>Too small</option><option>Too large</option><option>Not as described</option><option>Damaged or defective</option><option>Changed my mind</option></select></div>
          </div>
        </div>
        <div class="tf-14__item group/it overflow-hidden rounded-[1.1rem] border-[1.5px] border-tf14-line bg-tf14-card [transition:border-color_.25s,box-shadow_.3s_var(--ease-tf14)] [&:not(.is-final)]:hover:border-[color-mix(in_oklab,var(--color-tf14-ink)_30%,var(--color-tf14-line))] has-[.tf-14\_\_pick:checked]:border-tf14-ink has-[.tf-14\_\_pick:checked]:shadow-[0_14px_30px_-20px_rgba(0,0,0,.45)] has-[.tf-14\_\_pick:focus-visible]:outline-2 has-[.tf-14\_\_pick:focus-visible]:outline-offset-3 has-[.tf-14\_\_pick:focus-visible]:outline-tf14-hot [&.is-final]:bg-tf14-soft forced-colors:has-[.tf-14\_\_pick:checked]:outline-2 forced-colors:has-[.tf-14\_\_pick:checked]:outline-[Highlight]">
          <label class="relative grid cursor-pointer grid-cols-[auto_1fr_auto_auto] items-center gap-[.95rem] py-3 pr-4 pl-3 group-[.is-final]/it:cursor-not-allowed group-[.is-final]/it:text-tf14-muted max-[34rem]:grid-cols-[auto_1fr_auto]"><input type="checkbox" class="tf-14__pick absolute inset-0 m-0 cursor-pointer opacity-0" data-price="89" data-max="1"><img src="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=200&h=200&fit=crop&auto=format&q=70" width="72" height="72" alt="" loading="lazy" decoding="async" class="size-[4.25rem] rounded-[.8rem] bg-tf14-soft object-cover"><span><b class="block font-bold">Commuter Pack 22L</b><small class="mt-[.1rem] block text-[.85rem] text-tf14-muted group-[.is-final]/it:font-semibold group-[.is-final]/it:text-tf14-hot">Slate</small></span><em class="font-bold tabular-nums not-italic max-[34rem]:col-start-2 max-[34rem]:row-start-2">$89.00</em><i class="grid size-6 place-items-center rounded-[.45rem] border-[1.5px] border-tf14-line [transition:all_.25s_var(--ease-tf14)] after:h-[.4rem] after:w-[.7rem] after:-translate-y-px after:scale-0 after:-rotate-45 after:border-b-[2.5px] after:border-l-[2.5px] after:border-white after:[transition:scale_.3s_var(--ease-tf14)] after:content-[''] group-has-[.tf-14\_\_pick:checked]/it:border-tf14-hot group-has-[.tf-14\_\_pick:checked]/it:bg-tf14-hot group-has-[.tf-14\_\_pick:checked]/it:after:scale-100 group-[.is-final]/it:border-dashed" aria-hidden="true"></i></label>
          <div class="ml-[5.95rem] hidden grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[.8rem] px-4 pb-4 group-has-[.tf-14\_\_pick:checked]/it:grid group-has-[.tf-14\_\_pick:checked]/it:animate-tf14-in max-[34rem]:ml-0">
            <div class="grid gap-[.35rem]"><label for="tf-14-r3" class="text-[.8rem] font-bold">Reason</label><select id="tf-14-r3" class="tf-14__reason min-h-[2.8rem] w-full cursor-pointer rounded-[.7rem] border border-tf14-line bg-tf14-soft px-[.8rem] py-2 text-[.95rem] text-tf14-ink focus-visible:border-tf14-ink focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf14-hot)_25%,transparent)] focus-visible:outline-none [&.is-missing]:border-tf14-hot"><option value="">Select a reason</option><option>Not as described</option><option>Damaged or defective</option><option>Changed my mind</option></select></div>
          </div>
        </div>
        <div class="tf-14__item is-final group/it overflow-hidden rounded-[1.1rem] border-[1.5px] border-tf14-line bg-tf14-card [transition:border-color_.25s,box-shadow_.3s_var(--ease-tf14)] [&:not(.is-final)]:hover:border-[color-mix(in_oklab,var(--color-tf14-ink)_30%,var(--color-tf14-line))] has-[.tf-14\_\_pick:checked]:border-tf14-ink has-[.tf-14\_\_pick:checked]:shadow-[0_14px_30px_-20px_rgba(0,0,0,.45)] has-[.tf-14\_\_pick:focus-visible]:outline-2 has-[.tf-14\_\_pick:focus-visible]:outline-offset-3 has-[.tf-14\_\_pick:focus-visible]:outline-tf14-hot [&.is-final]:bg-tf14-soft forced-colors:has-[.tf-14\_\_pick:checked]:outline-2 forced-colors:has-[.tf-14\_\_pick:checked]:outline-[Highlight]">
          <label class="relative grid cursor-pointer grid-cols-[auto_1fr_auto_auto] items-center gap-[.95rem] py-3 pr-4 pl-3 group-[.is-final]/it:cursor-not-allowed group-[.is-final]/it:text-tf14-muted max-[34rem]:grid-cols-[auto_1fr_auto]"><input type="checkbox" class="tf-14__pick absolute inset-0 m-0 cursor-pointer opacity-0" disabled aria-describedby="tf-14-final"><span class="size-[4.25rem] rounded-[.8rem] bg-tf14-soft object-cover grid place-items-center border border-dashed border-tf14-line text-center text-[.7rem] font-bold text-tf14-muted" aria-hidden="true">Gift card</span><span><b class="block font-bold">Digital Gift Card</b><small id="tf-14-final" class="mt-[.1rem] block text-[.85rem] text-tf14-muted group-[.is-final]/it:font-semibold group-[.is-final]/it:text-tf14-hot">Final sale — not returnable</small></span><em class="font-bold tabular-nums not-italic max-[34rem]:col-start-2 max-[34rem]:row-start-2">$50.00</em><i class="grid size-6 place-items-center rounded-[.45rem] border-[1.5px] border-tf14-line [transition:all_.25s_var(--ease-tf14)] after:h-[.4rem] after:w-[.7rem] after:-translate-y-px after:scale-0 after:-rotate-45 after:border-b-[2.5px] after:border-l-[2.5px] after:border-white after:[transition:scale_.3s_var(--ease-tf14)] after:content-[''] group-has-[.tf-14\_\_pick:checked]/it:border-tf14-hot group-has-[.tf-14\_\_pick:checked]/it:bg-tf14-hot group-has-[.tf-14\_\_pick:checked]/it:after:scale-100 group-[.is-final]/it:border-dashed" aria-hidden="true"></i></label>
        </div>
      </fieldset>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,17rem),1fr))] gap-5">
        <fieldset class="grid min-w-0 content-start gap-2"><legend class="mb-[.7rem] p-0 text-[.95rem] font-bold">Refund to</legend>
          <label class="relative"><input type="radio" name="tf-14-m" value="card" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.15rem] rounded-2xl border-[1.5px] border-tf14-line py-[.85rem] pr-4 pl-[2.6rem] [transition:border-color_.2s,background_.2s] before:absolute before:top-4 before:left-4 before:size-4 before:rounded-full before:border-[1.5px] before:border-tf14-muted before:[transition:border_.25s_var(--ease-tf14)] before:content-[''] peer-checked:border-tf14-ink peer-checked:bg-tf14-soft peer-checked:before:border-[5px] peer-checked:before:border-tf14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf14-hot"><b class="text-[.95rem] font-bold">Original payment</b><small class="text-[.82rem] leading-[1.35] text-tf14-muted">Visa •••• 4242 · 3–5 days after we receive it</small></span></label>
          <label class="relative"><input type="radio" name="tf-14-m" value="credit" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.15rem] rounded-2xl border-[1.5px] border-tf14-line py-[.85rem] pr-4 pl-[2.6rem] [transition:border-color_.2s,background_.2s] before:absolute before:top-4 before:left-4 before:size-4 before:rounded-full before:border-[1.5px] before:border-tf14-muted before:[transition:border_.25s_var(--ease-tf14)] before:content-[''] peer-checked:border-tf14-ink peer-checked:bg-tf14-soft peer-checked:before:border-[5px] peer-checked:before:border-tf14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf14-hot"><b class="text-[.95rem] font-bold">Store credit <mark class="ml-1 rounded-[.3rem] bg-tf14-hot/18 px-[.35rem] py-[.05rem] text-[.78rem] text-tf14-hot">+10% bonus</mark></b><small class="text-[.82rem] leading-[1.35] text-tf14-muted">Instant, as soon as you drop it off</small></span></label>
        </fieldset>
        <fieldset class="grid min-w-0 content-start gap-2"><legend class="mb-[.7rem] p-0 text-[.95rem] font-bold">Return method</legend>
          <label class="relative"><input type="radio" name="tf-14-s" value="0" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.15rem] rounded-2xl border-[1.5px] border-tf14-line py-[.85rem] pr-4 pl-[2.6rem] [transition:border-color_.2s,background_.2s] before:absolute before:top-4 before:left-4 before:size-4 before:rounded-full before:border-[1.5px] before:border-tf14-muted before:[transition:border_.25s_var(--ease-tf14)] before:content-[''] peer-checked:border-tf14-ink peer-checked:bg-tf14-soft peer-checked:before:border-[5px] peer-checked:before:border-tf14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf14-hot"><b class="text-[.95rem] font-bold">Drop-off · Free</b><small class="text-[.82rem] leading-[1.35] text-tf14-muted">Any UPS Access Point. Show a QR code — no printer.</small></span></label>
          <label class="relative"><input type="radio" name="tf-14-s" value="5.95" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.15rem] rounded-2xl border-[1.5px] border-tf14-line py-[.85rem] pr-4 pl-[2.6rem] [transition:border-color_.2s,background_.2s] before:absolute before:top-4 before:left-4 before:size-4 before:rounded-full before:border-[1.5px] before:border-tf14-muted before:[transition:border_.25s_var(--ease-tf14)] before:content-[''] peer-checked:border-tf14-ink peer-checked:bg-tf14-soft peer-checked:before:border-[5px] peer-checked:before:border-tf14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf14-hot"><b class="text-[.95rem] font-bold">Courier pickup · $5.95</b><small class="text-[.82rem] leading-[1.35] text-tf14-muted">We'll collect from your door. Deducted from refund.</small></span></label>
        </fieldset>
      </div>
      <div class="grid grid-cols-[minmax(0,1fr)_auto] items-end gap-5 rounded-[1.1rem] bg-tf14-ink p-5 text-tf14-card max-[34rem]:grid-cols-1 forced-colors:border forced-colors:border-[CanvasText] forced-colors:bg-[Canvas] forced-colors:text-[CanvasText]">
        <dl class="grid gap-[.35rem]">
          <div class="flex justify-between gap-4 text-[.9rem]"><dt class="opacity-70">Items (<span class="tf-14__cnt">0</span>)</dt><dd class="font-semibold tabular-nums" data-k="items">$0.00</dd></div>
          <div class="hidden justify-between gap-4 text-[.9rem] group-has-[[value=credit]:checked]/root:flex"><dt class="opacity-70">Store credit bonus</dt><dd class="font-semibold tabular-nums text-[#fdba74]" data-k="bonus">$0.00</dd></div>
          <div class="flex justify-between gap-4 text-[.9rem]"><dt class="opacity-70">Return shipping</dt><dd class="font-semibold tabular-nums" data-k="ship">Free</dd></div>
          <div class="flex justify-between gap-4 mt-1 border-t border-tf14-card/18 pt-2 text-[1.15rem]"><dt class="font-bold">Estimated refund</dt><dd class="font-extrabold tabular-nums" data-k="total">$0.00</dd></div>
        </dl>
        <button type="button" class="tf-14__go min-h-[3.2rem] cursor-pointer rounded-[.9rem] border-0 bg-tf14-hot px-6 text-[1rem] font-extrabold text-[#111] [transition:translate_.2s_var(--ease-tf14),filter_.2s] hover:-translate-y-0.5 hover:brightness-106 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf14-card forced-colors:border forced-colors:border-[ButtonText]">Get return label</button>
      </div>
      <p class="tf-14__status -mt-3 font-semibold text-tf14-hot empty:hidden" role="status"></p>
      <div class="tf-14__label flex animate-tf14-label items-center gap-4 rounded-[1.1rem] border-[1.5px] border-dashed border-tf14-ok p-4" hidden><span class="size-[4.5rem] flex-none rounded-[.4rem] [background:repeating-conic-gradient(var(--color-tf14-ink)_0_25%,var(--color-tf14-card)_0_50%)_0_0/.9rem_.9rem] shadow-[0_0_0_.3rem_var(--color-tf14-card),0_0_0_calc(.3rem+1px)_var(--color-tf14-line)]" aria-hidden="true"></span><div><b class="text-tf14-ok">Return RMA-90231 created</b><p class="mt-[.2rem] text-[.9rem] text-tf14-muted">Show this QR at the drop-off point. We've also emailed it to you.</p></div></div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf14-bg: #f2f2f0;
  --color-tf14-card: #ffffff;
  --color-tf14-ink: #111110;
  --color-tf14-muted: #6b6b66;
  --color-tf14-line: #e6e6e2;
  --color-tf14-soft: #f8f8f6;
  --color-tf14-hot: #ff5a1f;
  --color-tf14-ok: #16a34a;
  --font-tf14-sans: "Urbanist", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf14: cubic-bezier(0.16,1,0.3,1);
  --animate-tf14-in: tf14-in 0.35s cubic-bezier(0.16,1,0.3,1);
  --animate-tf14-label: tf14-in 0.45s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf14-in {
    from {
      opacity: 0;
      translate: 0 -6px;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-14[data-theme="dark"] {
  color-scheme: dark;
  --color-tf14-bg: #0d0d0c;
  --color-tf14-card: #161615;
  --color-tf14-ink: #f5f5f2;
  --color-tf14-muted: #a3a39c;
  --color-tf14-line: #2a2a27;
  --color-tf14-soft: #1d1d1b;
  --color-tf14-hot: #ff7a45;
  --color-tf14-ok: #4ade80;
}

@media (prefers-color-scheme: dark) {
  .tf-14:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf14-bg: #0d0d0c;
    --color-tf14-card: #161615;
    --color-tf14-ink: #f5f5f2;
    --color-tf14-muted: #a3a39c;
    --color-tf14-line: #2a2a27;
    --color-tf14-soft: #1d1d1b;
    --color-tf14-hot: #ff7a45;
    --color-tf14-ok: #4ade80;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-14').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.tf-14');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const BONUS = 0.10, fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
  const qtyOf = (c) => { const q = c.closest('.tf-14__item').querySelector('.tf-14__qty'); return q ? Number(q.value) : 1; };
  const calc = () => {
    const picks = [...root.querySelectorAll('.tf-14__pick:checked')];
    const items = picks.reduce((a, c) => a + Number(c.dataset.price) * qtyOf(c), 0);
    const count = picks.reduce((a, c) => a + qtyOf(c), 0);
    const credit = $('[name="tf-14-m"]:checked').value === 'credit', ship = Number($('[name="tf-14-s"]:checked').value);
    const bonus = credit ? items * BONUS : 0, total = Math.max(0, items + bonus - (items ? ship : 0));
    $('.tf-14__cnt').textContent = count;
    $('[data-k="items"]').textContent = fmt.format(items);
    $('[data-k="bonus"]').textContent = '+' + fmt.format(bonus);
    $('[data-k="ship"]').textContent = ship ? '−' + fmt.format(ship) : 'Free';
    $('[data-k="total"]').textContent = fmt.format(total);
  };
  root.addEventListener('change', (e) => { if (e.target.classList.contains('tf-14__reason')) e.target.classList.remove('is-missing'); calc(); });
  $('.tf-14__go').addEventListener('click', () => {
    const status = $('.tf-14__status'), picks = [...root.querySelectorAll('.tf-14__pick:checked')];
    if (!picks.length) { status.textContent = 'Select at least one item to return.'; root.querySelector('.tf-14__pick:not(:disabled)').focus(); return; }
    const missing = picks.map((c) => c.closest('.tf-14__item').querySelector('.tf-14__reason')).find((s) => !s.value);
    if (missing) { missing.classList.add('is-missing'); status.textContent = 'Please choose a reason for each selected item.'; missing.focus(); return; }
    status.textContent = '';
    const label = $('.tf-14__label'); label.hidden = false;
    $('.tf-14__go').textContent = 'Label ready';
  });
  calc();
})();
```
