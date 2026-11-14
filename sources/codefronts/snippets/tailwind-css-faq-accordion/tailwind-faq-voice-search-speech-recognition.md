---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-voice-search-speech-recognition/"
title: "Tailwind FAQ with Voice Search Using the Speech Recognition API"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "Speak your question and watch the FAQ filter: a microphone button feeds the Speech Recognition API into the same live filter as demo 18, with interim results…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind FAQ with Voice Search Using the Speech Recognition API
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-voice-search-speech-recognition/

Speak your question and watch the FAQ filter: a microphone button feeds the Speech Recognition API into the same live filter as demo 18, with interim results streaming into the input as you talk and a pulsing listening ring. The part most voice demos skip is the whole point here — the mic only renders where the API exists, the typed filter is the baseline everyone gets, and every state change is announced.
## HTML
```html
<section class="tfa-25 w-full min-h-svh grid place-items-center bg-tfa25-bg font-tfa25-sans text-tfa25-ink px-5 py-12 bg-[radial-gradient(1000px_520px_at_50%_-15%,var(--color-tfa25-glow),transparent_60%)]">
  <div class="w-[min(680px,100%)]">
    <header>
      <h1 class="text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Ask out loud</h1>
      <p class="mt-3 max-w-[56ch] text-[15px] leading-relaxed text-tfa25-mut">Tap the mic and speak, or type — the filter is the same. Voice is the layer on top, never the requirement.</p>
    </header>

    <div class="mt-6 flex min-h-[54px] items-center gap-2.5 rounded-[14px] border border-tfa25-edge bg-tfa25-panel px-4 transition-[border-color,box-shadow] duration-250 focus-within:border-tfa25-acc focus-within:ring-3 focus-within:ring-tfa25-ring">
      <svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" class="shrink-0 text-tfa25-mut"><circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M13.5 13.5L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="tfa25-input" type="search" aria-label="Search or dictate a question" placeholder="Type, or press the mic…" class="min-h-11 w-full min-w-0 flex-1 border-0 bg-transparent text-[15px] text-tfa25-ink outline-none placeholder:text-tfa25-mut [&::-webkit-search-cancel-button]:appearance-none">
      <button type="button" id="tfa25-mic" aria-pressed="false" aria-label="Search by voice" class="relative grid size-11 shrink-0 cursor-pointer place-items-center rounded-full border border-tfa25-edge bg-transparent text-tfa25-acc transition-[background-color,border-color,color] duration-250 hover:border-tfa25-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfa25-acc aria-pressed:border-tfa25-acc aria-pressed:bg-tfa25-acc aria-pressed:text-tfa25-bg">
        <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full bg-tfa25-acc/40 opacity-0"></span>
        <svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true" class="relative"><path d="M12 3.5a3 3 0 013 3v5a3 3 0 01-6 0v-5a3 3 0 013-3z" fill="currentColor"/><path d="M6.5 11a5.5 5.5 0 0011 0M12 16.5V20M9 20h6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
    </div>
    <p id="tfa25-status" aria-live="polite" class="mt-2 min-h-5 font-tfa25-mono text-[11.5px] text-tfa25-acc"></p>

    <div data-panel id="tfa25-list" class="mt-2 flex flex-col gap-2.5">
        <details class="group rounded-[13px] border border-tfa25-edge bg-tfa25-panel transition-[border-color,box-shadow] duration-300 open:border-tfa25-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_290/0.45)]" open>
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa25-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa25-acc [&::-webkit-details-marker]:hidden">How do I reset my password?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa25-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa25-mut">Use the Forgot password link on the sign-in screen — the reset email arrives within a minute and the link is valid for one hour. Passkeys can be added afterwards from Security settings.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa25-edge bg-tfa25-panel transition-[border-color,box-shadow] duration-300 open:border-tfa25-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_290/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa25-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa25-acc [&::-webkit-details-marker]:hidden">Can I change my plan later?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa25-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa25-mut">Any time, in either direction. Upgrades apply instantly and prorate; downgrades take effect at the end of the billing period so you keep what you paid for.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa25-edge bg-tfa25-panel transition-[border-color,box-shadow] duration-300 open:border-tfa25-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_290/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa25-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa25-acc [&::-webkit-details-marker]:hidden">Do you support two-factor authentication?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa25-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa25-mut">Yes — authenticator apps and hardware keys on every plan, free, with enforced 2FA available for whole workspaces.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa25-edge bg-tfa25-panel transition-[border-color,box-shadow] duration-300 open:border-tfa25-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_290/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa25-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa25-acc [&::-webkit-details-marker]:hidden">Where can I download invoices?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa25-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa25-mut">Billing → History, as PDFs with your tax details. Billing-only members can be added for your accountant.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa25-edge bg-tfa25-panel transition-[border-color,box-shadow] duration-300 open:border-tfa25-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_290/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa25-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa25-acc [&::-webkit-details-marker]:hidden">Is there a mobile app?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa25-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa25-mut">Native apps for iOS and Android, plus an installable web app for everything else. Offline edits sync when you reconnect.</p>
        </details>
    </div>

    <div id="tfa25-empty" hidden class="mt-4 rounded-[14px] border border-dashed border-tfa25-edge px-5 py-6 text-center text-tfa25-mut">
      <b class="text-[15px] text-tfa25-ink">Nothing matched that.</b>
      <p class="mt-1.5 text-[13px]">Try fewer words — speech recognition guesses, and sometimes badly.</p>
    </div>

    <p class="mt-5 text-[12.5px] leading-relaxed text-tfa25-mut">Where the API is missing (Firefox today), the mic button is removed at runtime rather than shown broken.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa25-bg: #1c1a26;
  --color-tfa25-bg: oklch(0.21 0.02 290);
  --color-tfa25-panel: #241f31;
  --color-tfa25-panel: oklch(0.25 0.025 290);
  --color-tfa25-glow: #33244a;
  --color-tfa25-glow: oklch(0.29 0.06 290 / 0.55);
  --color-tfa25-ink: #f2f0f7;
  --color-tfa25-ink: oklch(0.96 0.006 290);
  --color-tfa25-mut: #b8b2c6;
  --color-tfa25-mut: oklch(0.79 0.018 290);
  --color-tfa25-edge: #383246;
  --color-tfa25-edge: oklch(0.34 0.028 290);
  --color-tfa25-accedge: #8b6cc8;
  --color-tfa25-accedge: oklch(0.6 0.12 290);
  --color-tfa25-ring: #4b3a7a;
  --color-tfa25-ring: oklch(0.42 0.1 290 / 0.5);
  --color-tfa25-acc: #c2a8f5;
  --color-tfa25-acc: oklch(0.82 0.13 290);
  --font-tfa25-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa25-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-25 {
  width: 100%;
  min-height: 100svh;
}
/* The listening ring: aria-pressed drives it, but the animation needs a keyframe, and a nested
   aria-pressed:[&>span]: variant would be harder to read than four lines. */

.tfa-25 #tfa25-mic[aria-pressed="true"] > span {
  opacity: 1;
  animation: tfa25-ping 1.4s cubic-bezier(0, 0, 0.2, 1) infinite;
}

@keyframes tfa25-ping {
  0% {
    transform: scale(1);
    opacity: .55;
  }

  70%,
    100% {
    transform: scale(1.7);
    opacity: 0;
  }
}

.tfa-25 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-25 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .tfa-25 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-25 #tfa25-mic[aria-pressed="true"] > span {
    animation: none;
    opacity: .5;
  }

  .tfa-25 details::details-content {
    transition-duration: 1ms;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.tfa-25');if(!root||root.dataset.tfa25)return;root.dataset.tfa25='1';
  var input=root.querySelector('#tfa25-input'),status=root.querySelector('#tfa25-status'),
      empty=root.querySelector('#tfa25-empty'),mic=root.querySelector('#tfa25-mic'),
      items=[].slice.call(root.querySelectorAll('#tfa25-list details'));
  items.forEach(function(d){d.dataset.initOpen=d.open?'1':''});
  function filter(){
    var q=input.value.trim().toLowerCase(),hits=0;
    items.forEach(function(d){
      var hit=!q||d.textContent.toLowerCase().indexOf(q)>-1;
      d.hidden=!hit;
      if(q&&hit)d.open=true;
      if(!q)d.open=!!d.dataset.initOpen;
      if(hit)hits++;
    });
    empty.hidden=hits>0;
  }
  input.addEventListener('input',filter);

  var SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR){mic.remove();return;}
  var rec=new SR(),listening=false;
  rec.lang=document.documentElement.lang||'en-US';
  rec.interimResults=true;rec.continuous=false;
  function setListening(on){
    listening=on;
    mic.setAttribute('aria-pressed',String(on));
    status.textContent=on?'Listening… speak now':'';
  }
  mic.addEventListener('click',function(){
    if(listening){rec.stop();return;}
    try{rec.start();setListening(true);}catch(e){setListening(false);}
  });
  rec.onresult=function(e){
    var t='';for(var i=0;i<e.results.length;i++)t+=e.results[i][0].transcript;
    input.value=t;filter();
  };
  rec.onerror=function(e){
    setListening(false);
    status.textContent=e.error==='not-allowed'?'Microphone permission denied — the typed filter still works.':'';
  };
  rec.onend=function(){setListening(false);};
})();
```
