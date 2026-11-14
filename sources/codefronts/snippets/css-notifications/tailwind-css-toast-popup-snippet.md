---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/tailwind-css-toast-popup-snippet/"
title: "Tailwind CSS Toast Popup Snippet"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Two production-shaped Tailwind toasts: a success popup built entirely from utilities (ring-1, shadow-lg, backdrop-blur) with its slide-in as a one-line…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Toast Popup Snippet
Source: https://codefronts.com/snippets/css-notifications/tailwind-css-toast-popup-snippet/

Two production-shaped Tailwind toasts: a success popup built entirely from utilities (ring-1, shadow-lg, backdrop-blur) with its slide-in as a one-line custom keyframe consumed via animate-[…] arbitrary values, and a responsive dark-mode-aware toast that sits full-width above the home indicator on phones and docks top-right from the sm: breakpoint up.
## HTML
```html
<div class="ntf-08-group">
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config={corePlugins:{preflight:false},darkMode:'selector'}</script>
<section class="ntf-08a" aria-label="Tailwind utility toast">
  <div class="mx-auto w-full max-w-md text-center">
    <h2 class="text-2xl font-semibold tracking-tight text-slate-100">Utilities all the way down</h2>
    <p class="mt-2 text-sm leading-6 text-slate-400">Layout, ring, shadow, blur — all classes. Only the slide-in keyframe is hand-written CSS, consumed with <code class="rounded bg-white/10 px-1.5 py-0.5 text-xs">animate-[…]</code>.</p>
    <button id="ntf-08a-btn" type="button" class="mt-6 rounded-xl bg-emerald-400 px-6 py-3 text-sm font-semibold text-slate-950 shadow-lg shadow-emerald-400/25 transition hover:bg-emerald-300 active:scale-95">Complete order</button>
  </div>
  <div id="ntf-08a-region" role="status" aria-live="polite" class="pointer-events-none absolute right-4 top-4 flex w-80 max-w-[calc(100%-2rem)] flex-col gap-3"></div>
  <template id="ntf-08a-tpl">
    <div class="pointer-events-auto flex items-center gap-3 rounded-2xl bg-white/95 p-4 shadow-xl shadow-slate-950/40 ring-1 ring-slate-900/10 backdrop-blur animate-[ntf-08a-in_.5s_cubic-bezier(.22,1.2,.36,1)_both]">
      <span class="grid h-9 w-9 flex-none place-items-center rounded-xl bg-emerald-500 text-white" aria-hidden="true"><svg class="h-4.5 w-4.5" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
      <span class="grid min-w-0 gap-0.5"><b class="text-[13.5px] font-semibold text-slate-900">Order confirmed</b><small class="text-xs text-slate-500">#8412 · receipt emailed</small></span>
      <button type="button" data-dismiss class="ml-auto grid h-7 w-7 flex-none place-items-center rounded-lg text-slate-400 transition hover:bg-slate-900/5 hover:text-slate-700" aria-label="Dismiss">&#10005;</button>
    </div>
  </template>
</section>
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config={corePlugins:{preflight:false},darkMode:'selector'}</script>
<section class="ntf-08b" aria-label="Responsive dark-mode Tailwind toast">
  <div id="ntf-08b-scope" class="absolute inset-0 grid place-items-center bg-slate-100 p-6 transition-colors duration-300 [&.dark]:bg-slate-950">
    <div class="w-full max-w-md text-center">
      <h2 class="text-2xl font-semibold tracking-tight text-slate-900 [.dark_&]:text-slate-100">Bottom sheet → corner toast</h2>
      <p class="mt-2 text-sm leading-6 text-slate-500 [.dark_&]:text-slate-400">Resize the preview: full-width above the home indicator on phones, docked top-right from <code class="rounded bg-slate-900/10 px-1.5 py-0.5 text-xs [.dark_&]:bg-white/10">sm:</code> up. Same element.</p>
      <div class="mt-6 flex items-center justify-center gap-3">
        <button id="ntf-08b-btn" type="button" class="rounded-xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white shadow-lg transition hover:bg-slate-700 active:scale-95 [.dark_&]:bg-white [.dark_&]:text-slate-900 [.dark_&]:hover:bg-slate-200">Show toast</button>
        <button id="ntf-08b-mode" type="button" class="rounded-xl px-5 py-3 text-sm font-semibold text-slate-600 ring-1 ring-slate-900/15 transition hover:bg-slate-900/5 [.dark_&]:text-slate-300 [.dark_&]:ring-white/20 [.dark_&]:hover:bg-white/5">Toggle dark</button>
      </div>
    </div>
    <div id="ntf-08b-region" role="status" aria-live="polite" class="pointer-events-none absolute inset-x-3 bottom-3 sm:inset-x-auto sm:bottom-auto sm:right-4 sm:top-4 sm:w-80"></div>
    <template id="ntf-08b-tpl">
      <div class="pointer-events-auto flex items-center gap-3 rounded-2xl bg-white/95 p-4 shadow-xl shadow-slate-900/15 ring-1 ring-slate-900/10 backdrop-blur animate-[ntf-08b-up_.45s_cubic-bezier(.22,1.2,.36,1)_both] [.dark_&]:bg-slate-900/95 [.dark_&]:shadow-black/50 [.dark_&]:ring-white/15">
        <span class="grid h-9 w-9 flex-none place-items-center rounded-xl bg-sky-500 text-white" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></span>
        <span class="grid min-w-0 gap-0.5"><b class="text-[13.5px] font-semibold text-slate-900 [.dark_&]:text-slate-100">Message sent</b><small class="text-xs text-slate-500 [.dark_&]:text-slate-400">Ana will get it when she's online</small></span>
        <button type="button" data-dismiss class="ml-auto grid h-7 w-7 flex-none place-items-center rounded-lg text-slate-400 transition hover:bg-slate-900/5 hover:text-slate-700 [.dark_&]:hover:bg-white/10 [.dark_&]:hover:text-slate-200" aria-label="Dismiss">&#10005;</button>
      </div>
    </template>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-08-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-08-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-08a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#0f172a,#020617);
  font-family: ui-sans-serif,'Segoe UI',system-ui,sans-serif;
}

@keyframes ntf-08a-in {
  from {
    opacity: 0;
    translate: 16rem 0;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-08a [class*="animate-"] {
    animation-name: ntf-08a-fade!important;
    animation-duration: .25s!important;
  }

  @keyframes ntf-08a-fade {
    from {
      opacity: 0;
    }

    to {
      opacity: 1;
    }
  }
}

.ntf-08b {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  font-family: ui-sans-serif,'Segoe UI',system-ui,sans-serif;
}

@keyframes ntf-08b-up {
  from {
    opacity: 0;
    translate: 0 1.5rem;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-08b [class*="animate-"] {
    animation-name: ntf-08b-fade!important;
    animation-duration: .25s!important;
  }

  @keyframes ntf-08b-fade {
    from {
      opacity: 0;
    }

    to {
      opacity: 1;
    }
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('ntf-08a-btn'); if(!btn) return;
  var region=document.getElementById('ntf-08a-region'),tpl=document.getElementById('ntf-08a-tpl');
  btn.addEventListener('click',function(){
    var toast=tpl.content.firstElementChild.cloneNode(true);
    toast.querySelector('[data-dismiss]').addEventListener('click',function(){ toast.remove(); });
    region.appendChild(toast);
    setTimeout(function(){ if(toast.isConnected) toast.remove(); },5000);
  });
})();

(function(){
  var scope=document.getElementById('ntf-08b-scope'); if(!scope) return;
  var region=document.getElementById('ntf-08b-region'),tpl=document.getElementById('ntf-08b-tpl');
  document.getElementById('ntf-08b-btn').addEventListener('click',function(){
    region.textContent='';
    var toast=tpl.content.firstElementChild.cloneNode(true);
    toast.querySelector('[data-dismiss]').addEventListener('click',function(){ toast.remove(); });
    region.appendChild(toast);
    setTimeout(function(){ if(toast.isConnected) toast.remove(); },5000);
  });
  document.getElementById('ntf-08b-mode').addEventListener('click',function(){
    scope.classList.toggle('dark'); /* darkMode:'selector' — the class, not the OS, decides */
  });
})();
```
