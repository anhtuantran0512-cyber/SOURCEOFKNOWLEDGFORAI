---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-checkout-payment-form-order-summary/"
title: "Tailwind Checkout Payment Form with Order Summary"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's two-column checkout, ported one-for-one to Tailwind v4: it collapses with a container query (not a viewport query), shows a live 3D card…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Checkout Payment Form with Order Summary
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-checkout-payment-form-order-summary/

The CSS collection's two-column checkout, ported one-for-one to Tailwind v4: it collapses with a container query (not a viewport query), shows a live 3D card preview that mirrors what you type and flips to the CVC on focus, detects the card brand and re-tints the card, switches Card / Wallet / Bank panels with pure group-has-[…]:, and recomputes an order summary with quantity steppers and a working promo code.
## HTML
```html
<div class="tf-03 group/root relative block min-h-svh w-full bg-tf03-bg pt-[72px] font-tf03-sans leading-[normal] text-tf03-ink antialiased [--card-a:#1e293b] [--card-b:#475569] data-[brand=amex]:[--card-a:#0b4f6c] data-[brand=amex]:[--card-b:#14b8a6] data-[brand=mastercard]:[--card-a:#2b1b10] data-[brand=mastercard]:[--card-b:#c2410c] data-[brand=visa]:[--card-a:#1a1f71] data-[brand=visa]:[--card-b:#3b5bdb] motion-reduce:**:animate-none! motion-reduce:**:transition-none!" data-brand="none">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3.5rem)]">
    <div class="@container w-full max-w-[68rem]">
      <div class="grid grid-cols-1 overflow-hidden rounded-3xl border border-tf03-line bg-tf03-surface shadow-[0_1px_2px_rgba(15,23,42,.04),0_30px_70px_-35px_rgba(15,23,42,.35)] @[52rem]:grid-cols-[minmax(0,1.25fr)_minmax(0,1fr)]">
        <section class="grid content-start gap-[1.1rem] p-[clamp(1.25rem,4cqi,2.75rem)]" role="form" aria-labelledby="tf-03-title">
          <div class="flex gap-2 text-[.8rem] text-tf03-muted" aria-label="Checkout progress"><span class="flex items-center gap-2 not-last:after:h-px not-last:after:w-5 not-last:after:bg-tf03-line not-last:after:content-[''] aria-[current=step]:font-semibold aria-[current=step]:text-tf03-ink">Cart</span><span class="flex items-center gap-2 not-last:after:h-px not-last:after:w-5 not-last:after:bg-tf03-line not-last:after:content-[''] aria-[current=step]:font-semibold aria-[current=step]:text-tf03-ink">Shipping</span><span class="flex items-center gap-2 not-last:after:h-px not-last:after:w-5 not-last:after:bg-tf03-line not-last:after:content-[''] aria-[current=step]:font-semibold aria-[current=step]:text-tf03-ink" aria-current="step">Payment</span></div>
          <h2 id="tf-03-title" class="text-[1.75rem] font-bold tracking-[-.03em]">Payment</h2>
          <fieldset class="grid grid-cols-3 gap-[.3rem] rounded-2xl border border-tf03-line bg-tf03-sum p-[.3rem]">
            <legend class="sr-only">Payment method</legend>
            <label class="relative"><input type="radio" name="tf-03-m" value="card" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="flex min-h-11 items-center justify-center gap-2 rounded-[.75rem] text-[.9rem] font-semibold text-tf03-muted [transition:background_.25s,color_.25s,box-shadow_.25s] peer-checked:bg-tf03-surface peer-checked:text-tf03-ink peer-checked:shadow-[0_1px_2px_rgba(0,0,0,.06),0_4px_12px_-4px_rgba(0,0,0,.12)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-tf03-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.15rem] fill-none stroke-current stroke-[1.6] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6 15h4"/></svg>Card</span></label>
            <label class="relative"><input type="radio" name="tf-03-m" value="wallet" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="flex min-h-11 items-center justify-center gap-2 rounded-[.75rem] text-[.9rem] font-semibold text-tf03-muted [transition:background_.25s,color_.25s,box-shadow_.25s] peer-checked:bg-tf03-surface peer-checked:text-tf03-ink peer-checked:shadow-[0_1px_2px_rgba(0,0,0,.06),0_4px_12px_-4px_rgba(0,0,0,.12)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-tf03-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.15rem] fill-none stroke-current stroke-[1.6] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M4 7.5A2.5 2.5 0 0 1 6.5 5H18v3"/><rect x="3" y="8" width="18" height="11" rx="2.5"/><circle cx="16.5" cy="13.5" r="1.3"/></svg>Wallet</span></label>
            <label class="relative"><input type="radio" name="tf-03-m" value="bank" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="flex min-h-11 items-center justify-center gap-2 rounded-[.75rem] text-[.9rem] font-semibold text-tf03-muted [transition:background_.25s,color_.25s,box-shadow_.25s] peer-checked:bg-tf03-surface peer-checked:text-tf03-ink peer-checked:shadow-[0_1px_2px_rgba(0,0,0,.06),0_4px_12px_-4px_rgba(0,0,0,.12)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-tf03-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.15rem] fill-none stroke-current stroke-[1.6] [stroke-linecap:round] [stroke-linejoin:round]"><path d="m3 9 9-5 9 5M5 10v7M9.5 10v7M14.5 10v7M19 10v7M3 20h18"/></svg>Bank</span></label>
          </fieldset>
          <div class="hidden gap-4 group-has-[[value=card]:checked]/root:grid group-has-[[value=card]:checked]/root:animate-tf03-in">
            <div class="relative mx-auto mt-1 mb-2 aspect-[1.586] w-[min(100%,21rem)] [transition:transform_.8s_var(--ease-tf03)] transform-3d group-has-[#tf-03-cvc:focus]/root:rotate-y-180" aria-hidden="true">
              <div class="absolute inset-0 rounded-2xl px-5 py-[1.15rem] text-white backface-hidden [background:radial-gradient(120%_140%_at_0%_0%,color-mix(in_oklab,var(--card-b)_90%,white),transparent_55%),linear-gradient(135deg,var(--card-a),var(--card-b))] shadow-[inset_0_1px_0_rgba(255,255,255,.25),0_24px_40px_-18px_color-mix(in_oklab,var(--card-a)_80%,black)] [transition:background_.5s] forced-colors:border forced-colors:border-[CanvasText] forced-colors:bg-[Canvas] forced-colors:text-[CanvasText] grid grid-rows-[auto_1fr_auto] after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:bg-[linear-gradient(115deg,transparent_30%,rgba(255,255,255,.18)_45%,transparent_60%)] after:content-['']">
                <div class="flex items-center justify-between"><span class="h-7 w-[2.4rem] rounded-[.35rem] bg-[linear-gradient(135deg,#f5d77a,#b8913a)] shadow-[inset_0_0_0_1px_rgba(0,0,0,.2)]"></span><span class="tf-03__brand text-[1rem] font-bold tracking-[.04em] italic"></span></div>
                <div class="tf-03__pnum self-center font-tf03-mono text-[clamp(1rem,4.6cqi,1.3rem)] font-medium tracking-[.08em] whitespace-nowrap [text-shadow:0_1px_1px_rgba(0,0,0,.3)]">•••• •••• •••• ••••</div>
                <div class="flex justify-between gap-4"><span class="grid min-w-0 gap-[.1rem]"><small class="text-[.6rem] tracking-[.12em] uppercase opacity-70">Card holder</small><b class="tf-03__pname truncate text-[.85rem] font-semibold tracking-[.04em] uppercase">Your name</b></span><span class="grid min-w-0 gap-[.1rem]"><small class="text-[.6rem] tracking-[.12em] uppercase opacity-70">Expires</small><b class="tf-03__pexp truncate text-[.85rem] font-semibold tracking-[.04em] uppercase">MM/YY</b></span></div>
              </div>
              <div class="absolute inset-0 rounded-2xl px-5 py-[1.15rem] text-white backface-hidden [background:radial-gradient(120%_140%_at_0%_0%,color-mix(in_oklab,var(--card-b)_90%,white),transparent_55%),linear-gradient(135deg,var(--card-a),var(--card-b))] shadow-[inset_0_1px_0_rgba(255,255,255,.25),0_24px_40px_-18px_color-mix(in_oklab,var(--card-a)_80%,black)] [transition:background_.5s] forced-colors:border forced-colors:border-[CanvasText] forced-colors:bg-[Canvas] forced-colors:text-[CanvasText] grid rotate-y-180 content-center gap-[.8rem] px-0!"><i class="h-[2.4rem] bg-[#0a0a0a]"></i><span class="tf-03__pcvc mr-5 justify-self-end rounded-[.35rem] bg-[#f8fafc] px-[.7rem] py-[.35rem] font-tf03-mono text-[.95rem] font-medium tracking-[.15em] text-[#0f172a]">•••</span></div>
            </div>
            <div class="grid gap-[.4rem]">
              <label for="tf-03-num" class="text-[.85rem] font-semibold">Card number</label>
              <div class="relative">
                <input id="tf-03-num" type="text" inputmode="numeric" autocomplete="cc-number" placeholder="1234 1234 1234 1234" maxlength="19" required aria-describedby="tf-03-brand-live" class="min-h-12 w-full rounded-[.75rem] border border-tf03-line bg-tf03-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf03-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf03)] placeholder:text-tf03-muted/70 focus-visible:border-tf03-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf03-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf03-bad font-tf03-mono text-[.95rem]! tracking-[.02em] pr-[4.25rem]">
                <span class="tf-03__badge absolute top-1/2 right-[.6rem] -translate-y-1/2 scale-80 rounded-[.35rem] border border-tf03-line bg-tf03-sum px-2 py-[.3rem] text-[.65rem] font-bold tracking-[.06em] text-tf03-muted uppercase opacity-0 [transition:opacity_.25s,scale_.3s_var(--ease-tf03)] group-data-[brand=amex]/root:scale-100 group-data-[brand=amex]/root:opacity-100 group-data-[brand=mastercard]/root:scale-100 group-data-[brand=mastercard]/root:opacity-100 group-data-[brand=visa]/root:scale-100 group-data-[brand=visa]/root:opacity-100" aria-hidden="true"></span>
              </div>
              <span class="sr-only" id="tf-03-brand-live" aria-live="polite"></span>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div class="grid gap-[.4rem]"><label for="tf-03-exp" class="text-[.85rem] font-semibold">Expiry</label><input id="tf-03-exp" type="text" inputmode="numeric" autocomplete="cc-exp" placeholder="MM / YY" maxlength="7" required class="min-h-12 w-full rounded-[.75rem] border border-tf03-line bg-tf03-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf03-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf03)] placeholder:text-tf03-muted/70 focus-visible:border-tf03-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf03-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf03-bad font-tf03-mono text-[.95rem]! tracking-[.02em]"></div>
              <div class="grid gap-[.4rem]"><label for="tf-03-cvc" class="text-[.85rem] font-semibold">CVC</label><input id="tf-03-cvc" type="text" inputmode="numeric" autocomplete="cc-csc" placeholder="123" maxlength="4" required class="min-h-12 w-full rounded-[.75rem] border border-tf03-line bg-tf03-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf03-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf03)] placeholder:text-tf03-muted/70 focus-visible:border-tf03-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf03-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf03-bad font-tf03-mono text-[.95rem]! tracking-[.02em]"></div>
            </div>
            <div class="grid gap-[.4rem]"><label for="tf-03-name" class="text-[.85rem] font-semibold">Name on card</label><input id="tf-03-name" type="text" autocomplete="cc-name" placeholder="Taylor Morgan" required class="min-h-12 w-full rounded-[.75rem] border border-tf03-line bg-tf03-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf03-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf03)] placeholder:text-tf03-muted/70 focus-visible:border-tf03-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf03-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf03-bad"></div>
          </div>
          <div class="hidden gap-4 group-has-[[value=wallet]:checked]/root:grid group-has-[[value=wallet]:checked]/root:animate-tf03-in"><p class="rounded-2xl border border-dashed border-tf03-line bg-tf03-sum px-[1.1rem] py-4 leading-[1.55] text-tf03-muted">You'll confirm with your device wallet after pressing Pay. Supported: Apple&nbsp;Pay, Google&nbsp;Pay and Link.</p></div>
          <div class="hidden gap-4 group-has-[[value=bank]:checked]/root:grid group-has-[[value=bank]:checked]/root:animate-tf03-in"><p class="rounded-2xl border border-dashed border-tf03-line bg-tf03-sum px-[1.1rem] py-4 leading-[1.55] text-tf03-muted">Pay directly from your bank via secure open-banking. You'll be redirected to approve the payment.</p></div>
          <label class="flex min-h-11 cursor-pointer items-center gap-[.6rem] text-[.9rem] text-tf03-muted"><input type="checkbox" checked class="m-0 size-[1.1rem] accent-tf03-accent"><span>Save this payment method for next time</span></label>
          <button class="tf-03__paybtn flex min-h-[3.4rem] cursor-pointer items-center justify-center gap-[.6rem] rounded-[.9rem] border-0 bg-tf03-accent text-[1.05rem] font-semibold text-tf03-on shadow-[inset_0_1px_0_rgba(255,255,255,.2),0_12px_26px_-12px_color-mix(in_oklab,var(--color-tf03-accent)_90%,black)] [transition:translate_.2s_var(--ease-tf03),filter_.2s] hover:-translate-y-0.5 hover:brightness-107 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf03-ink active:translate-y-px aria-busy:pointer-events-none aria-busy:saturate-60 forced-colors:border forced-colors:border-[ButtonText]" type="button"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.15rem] fill-none stroke-current stroke-[1.8] [stroke-linecap:round]"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg><span>Pay <b class="tf-03__paytotal tabular-nums">$0.00</b></span></button>
          <p class="tf-03__secure text-center text-[.8rem] text-tf03-muted" role="status">Encrypted end-to-end. You won't be charged until you confirm.</p>
        </section>
        <aside class="-order-1 grid content-start gap-4 border-b border-tf03-line bg-tf03-sum p-[clamp(1.25rem,4cqi,2.75rem)] @[52rem]:order-none @[52rem]:border-b-0 @[52rem]:border-l" aria-labelledby="tf-03-sum">
          <h3 id="tf-03-sum" class="text-[1.1rem] font-bold tracking-[-.01em]">Order summary</h3>
          <ul class="tf-03__items grid list-none gap-4">
            <li data-i="0" class="grid grid-cols-[auto_1fr_auto] items-center gap-[.9rem]">
              <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=240&h=240&fit=crop&auto=format&q=70" width="72" height="72" alt="Matte white over-ear wireless headphones" loading="lazy" decoding="async" class="size-[4.5rem] rounded-[.9rem] border border-tf03-line bg-tf03-line object-cover">
              <div><b class="block text-[.95rem]">Studio Wireless</b><small class="mt-[.1rem] mb-[.4rem] block text-[.8rem] text-tf03-muted">Chalk white</small><div class="tf-03__qty inline-flex items-center rounded-[.6rem] border border-tf03-line bg-tf03-surface"><button type="button" data-d="-1" aria-label="Decrease Studio Wireless quantity" class="size-9 cursor-pointer rounded-[.55rem] border-0 bg-transparent text-[1.1rem] text-tf03-ink hover:bg-tf03-sum focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tf03-accent">−</button><output aria-live="polite" class="min-w-7 text-center font-semibold tabular-nums">1</output><button type="button" data-d="1" aria-label="Increase Studio Wireless quantity" class="size-9 cursor-pointer rounded-[.55rem] border-0 bg-transparent text-[1.1rem] text-tf03-ink hover:bg-tf03-sum focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tf03-accent">+</button></div></div>
              <span class="tf-03__price font-semibold tabular-nums"></span>
            </li>
            <li data-i="1" class="grid grid-cols-[auto_1fr_auto] items-center gap-[.9rem]">
              <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=240&h=240&fit=crop&auto=format&q=70" width="72" height="72" alt="Minimal analogue wristwatch with a white dial" loading="lazy" decoding="async" class="size-[4.5rem] rounded-[.9rem] border border-tf03-line bg-tf03-line object-cover">
              <div><b class="block text-[.95rem]">Field Watch 38</b><small class="mt-[.1rem] mb-[.4rem] block text-[.8rem] text-tf03-muted">Steel / white dial</small><div class="tf-03__qty inline-flex items-center rounded-[.6rem] border border-tf03-line bg-tf03-surface"><button type="button" data-d="-1" aria-label="Decrease Field Watch quantity" class="size-9 cursor-pointer rounded-[.55rem] border-0 bg-transparent text-[1.1rem] text-tf03-ink hover:bg-tf03-sum focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tf03-accent">−</button><output aria-live="polite" class="min-w-7 text-center font-semibold tabular-nums">1</output><button type="button" data-d="1" aria-label="Increase Field Watch quantity" class="size-9 cursor-pointer rounded-[.55rem] border-0 bg-transparent text-[1.1rem] text-tf03-ink hover:bg-tf03-sum focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tf03-accent">+</button></div></div>
              <span class="tf-03__price font-semibold tabular-nums"></span>
            </li>
          </ul>
          <div class="flex gap-2">
            <label for="tf-03-code" class="sr-only">Promo code</label>
            <input id="tf-03-code" type="text" placeholder="Promo code (try SAVE10)" autocomplete="off" aria-describedby="tf-03-code-msg" class="min-h-12 w-full rounded-[.75rem] border border-tf03-line bg-tf03-surface px-[.95rem] py-[.7rem] text-[1rem] text-tf03-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf03)] placeholder:text-tf03-muted/70 focus-visible:border-tf03-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf03-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf03-bad min-w-0 flex-1 uppercase placeholder:normal-case">
            <button type="button" class="tf-03__apply min-h-12 cursor-pointer rounded-[.75rem] border border-tf03-line bg-tf03-surface px-[1.1rem] font-semibold text-tf03-ink hover:border-tf03-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf03-accent">Apply</button>
          </div>
          <p class="tf-03__codemsg -mt-2 min-h-[1em] text-[.8rem] data-[ok=false]:text-tf03-bad data-[ok=true]:text-tf03-ok" id="tf-03-code-msg" aria-live="polite"></p>
          <dl class="grid gap-[.6rem] border-t border-tf03-line pt-4">
            <div class="flex justify-between text-[.92rem]"><dt class="text-tf03-muted">Subtotal</dt><dd class="tabular-nums" data-k="sub"></dd></div>
            <div class="hidden justify-between text-[.92rem] text-tf03-ok in-[.has-disc]:flex"><dt>Discount</dt><dd class="tabular-nums" data-k="disc"></dd></div>
            <div class="flex justify-between text-[.92rem]"><dt class="text-tf03-muted">Shipping</dt><dd class="tabular-nums" data-k="ship"></dd></div>
            <div class="flex justify-between text-[.92rem]"><dt class="text-tf03-muted">Estimated tax</dt><dd class="tabular-nums" data-k="tax"></dd></div>
            <div class="flex justify-between border-t border-dashed border-tf03-line pt-[.8rem] text-[1.15rem] font-bold"><dt class="text-tf03-ink">Total</dt><dd class="tabular-nums" data-k="total"></dd></div>
          </dl>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf03-bg: #eef1f5;
  --color-tf03-surface: #ffffff;
  --color-tf03-sum: #f7f8fb;
  --color-tf03-ink: #0f172a;
  --color-tf03-muted: #64748b;
  --color-tf03-line: #e2e8f0;
  --color-tf03-accent: #4f46e5;
  --color-tf03-on: #fff;
  --color-tf03-ok: #059669;
  --color-tf03-bad: #dc2626;
  --font-tf03-sans: "Figtree", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-tf03-mono: "JetBrains Mono", ui-monospace, Menlo, monospace;
  --ease-tf03: cubic-bezier(0.16,1,0.3,1);
  --animate-tf03-in: tf03-in 0.45s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf03-in {
    from {
      opacity: 0;
      translate: 0 8px;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-03[data-theme="dark"] {
  color-scheme: dark;
  --color-tf03-bg: #0b0f17;
  --color-tf03-surface: #121826;
  --color-tf03-sum: #0f1520;
  --color-tf03-ink: #e7ecf5;
  --color-tf03-muted: #8a96ab;
  --color-tf03-line: #232c3d;
  --color-tf03-accent: #818cf8;
  --color-tf03-on: #0b0d24;
  --color-tf03-ok: #34d399;
  --color-tf03-bad: #f87171;
}

@media (prefers-color-scheme: dark) {
  .tf-03:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf03-bg: #0b0f17;
    --color-tf03-surface: #121826;
    --color-tf03-sum: #0f1520;
    --color-tf03-ink: #e7ecf5;
    --color-tf03-muted: #8a96ab;
    --color-tf03-line: #232c3d;
    --color-tf03-accent: #818cf8;
    --color-tf03-on: #0b0d24;
    --color-tf03-ok: #34d399;
    --color-tf03-bad: #f87171;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-03').forEach((root) => {
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
  const root = document.querySelector('.tf-03');
  if (!root) return;
  const fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
  const items = [{ price: 249, qty: 1 }, { price: 189, qty: 1 }];
  const CODES = { SAVE10: 0.10, WELCOME15: 0.15 };
  const TAX = 0.0825, FREE_SHIP = 300;
  let discount = 0;
  const $ = (s) => root.querySelector(s);
  const render = () => {
    root.querySelectorAll('.tf-03__items li').forEach((li, i) => {
      li.querySelector('output').textContent = items[i].qty;
      li.querySelector('.tf-03__price').textContent = fmt.format(items[i].price * items[i].qty);
    });
    const sub = items.reduce((a, it) => a + it.price * it.qty, 0);
    const disc = sub * discount, ship = sub - disc >= FREE_SHIP || sub === 0 ? 0 : 12;
    const tax = (sub - disc) * TAX, total = sub - disc + ship + tax;
    $('[data-k="sub"]').textContent = fmt.format(sub);
    $('[data-k="disc"]').textContent = '−' + fmt.format(disc);
    $('[data-k="ship"]').textContent = ship ? fmt.format(ship) : 'Free';
    $('[data-k="tax"]').textContent = fmt.format(tax);
    $('[data-k="total"]').textContent = fmt.format(total);
    $('.tf-03__paytotal').textContent = fmt.format(total);
    root.classList.toggle('has-disc', discount > 0);
  };
  root.querySelectorAll('.tf-03__qty button').forEach((b) => b.addEventListener('click', () => {
    const it = items[b.closest('li').dataset.i];
    it.qty = Math.max(0, Math.min(9, it.qty + Number(b.dataset.d)));
    render();
  }));
  $('.tf-03__apply').addEventListener('click', () => {
    const code = $('#tf-03-code').value.trim().toUpperCase(), msg = $('.tf-03__codemsg');
    discount = CODES[code] || 0;
    msg.dataset.ok = discount > 0;
    msg.textContent = discount ? code + ' applied — ' + Math.round(discount * 100) + '% off.' : code ? 'That code isn\'t valid.' : '';
    render();
  });
  const num = $('#tf-03-num'), exp = $('#tf-03-exp'), cvc = $('#tf-03-cvc'), name = $('#tf-03-name');
  const brandOf = (d) => /^3[47]/.test(d) ? 'amex' : /^4/.test(d) ? 'visa' : /^(5[1-5]|2[2-7])/.test(d) ? 'mastercard' : 'none';
  const label = { visa: 'VISA', mastercard: 'Mastercard', amex: 'AMEX', none: '' };
  num.addEventListener('input', () => {
    const before = num.value.slice(0, num.selectionStart).replace(/\D/g, '').length;
    const d = num.value.replace(/\D/g, '').slice(0, 16), brand = brandOf(d);
    const groups = brand === 'amex' ? [4, 6, 5] : [4, 4, 4, 4];
    let out = '', i = 0;
    groups.forEach((g) => { const part = d.slice(i, i + g); if (part) out += (out ? ' ' : '') + part; i += g; });
    num.value = out;
    let pos = 0, seen = 0;
    while (pos < out.length && seen < before) { if (/\d/.test(out[pos])) seen++; pos++; }
    num.setSelectionRange(pos, pos);
    if (root.dataset.brand !== brand) $('#tf-03-brand-live').textContent = label[brand] ? label[brand] + ' detected' : '';
    root.dataset.brand = brand;
    $('.tf-03__badge').textContent = label[brand];
    $('.tf-03__brand').textContent = label[brand];
    const mask = (brand === 'amex' ? '•••• •••••• •••••' : '•••• •••• •••• ••••');
    $('.tf-03__pnum').textContent = out + mask.slice(out.length);
    num.setCustomValidity(d.length >= (brand === 'amex' ? 15 : 16) ? '' : 'Incomplete card number');
  });
  exp.addEventListener('input', (e) => {
    let d = exp.value.replace(/\D/g, '').slice(0, 4);
    if (d.length === 1 && Number(d) > 1) d = '0' + d;
    exp.value = d.length > 2 ? d.slice(0, 2) + ' / ' + d.slice(2) : (d.length === 2 && e.inputType !== 'deleteContentBackward' ? d + ' / ' : d);
    $('.tf-03__pexp').textContent = d.length ? (d.slice(0, 2) + '/' + d.slice(2)).replace(/\/$/, '') : 'MM/YY';
  });
  cvc.addEventListener('input', () => { cvc.value = cvc.value.replace(/\D/g, ''); $('.tf-03__pcvc').textContent = cvc.value || '•••'; });
  name.addEventListener('input', () => { $('.tf-03__pname').textContent = name.value || 'Your name'; });
  $('.tf-03__paybtn').addEventListener('click', () => {
    const btn = $('.tf-03__paybtn'), status = $('.tf-03__secure');
    if (root.querySelector('[value="card"]').checked) {
      const bad = [num, exp, cvc, name].find((f) => !f.value || !f.checkValidity());
      if (bad) { bad.focus(); status.textContent = 'Please complete your card details.'; return; }
    }
    btn.setAttribute('aria-busy', 'true'); btn.querySelector('span').textContent = 'Processing…';
    setTimeout(() => { btn.removeAttribute('aria-busy'); btn.querySelector('span').textContent = 'Paid — thank you'; status.textContent = 'Payment confirmed. A receipt is on its way.'; }, 1400);
  });
  render();
})();
```
