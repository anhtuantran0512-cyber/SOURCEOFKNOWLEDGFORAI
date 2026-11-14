---
source: "lucianlabs"
id: "236"
title: "Curtain-reveal footer"
category: "Navigation"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#236"
tags: ["footer", "reveal", "scroll", "newsletter", "layout"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Curtain-reveal footer (236, Navigation)
[What it does] Scroll to the end of the page and the content rises like a curtain to reveal a dark footer fixed beneath it. As it's revealed the footer grows slightly and brightens, and the big brand wordmark at the bottom floats up. Enter an address in the footer's newsletter field and press Subscribe to turn the button into a check.
[How to use it] Scroll to the bottom inside the card to reveal the footer

Please add the UI element below to my project.

[Check first]
1. Find out the project’s framework (React, Next, Vue, Svelte, plain HTML, etc.), styling approach (CSS modules, Tailwind, global CSS) and existing theming approach (data-theme, a dark class, CSS variables).
2. Locate the file and any existing element at the insertion point first, and report where that element is used.

[How to apply]
3. Add it as a new component at the insertion point. If there is a replacement target, replace that element with the one below.
4. Keep existing data, props, event handlers, form values and accessibility attributes (labels, aria, keyboard support) as they are.
5. Port the structure, shapes and motion values (durations, curves, delays) of the code below as they are. Convert it into components and state for the framework, but do not guess a new design.
6. Map the --ux-* color tokens below to the project’s existing theme variables. Keep both the light and dark values and check both themes.
7. Keep styles inside this element’s class (.uNNN) and do not change global CSS or global scripts. Make sure the class names do not clash with existing ones.
8. Replace the sample copy and sample data with the project’s real data. Do not bring over gallery-only screens or demo code. Keep the one-line license comment at the top of the new component file.
9. Check that the feature and its final states still work with prefers-reduced-motion turned on.

[Report when done]
10. List the files you changed, behavior that differs from the old element, what you checked (both themes, mobile width, keyboard) and anything you could not check.

[Insertion point] Write the page or component name here
[Replacement target] Write the file path or component name of the existing element, or "none"

--- Code start (this whole code is the working original) ---
<!-- Lucian UX/UI Prompt #236 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#236 -->
<style>
/* lucianLabs UI 요소 — 공통 테마 토큰 (라이트 / 다크)
   라이트 기본값 → 시스템이 다크면 다크 → data-theme으로 명시하면 그 값을 우선합니다.
   요소 CSS는 --ux-* 토큰만 참조하므로, 프로젝트 테마 변수에 이 값을 매핑하면 됩니다. */
:root{
  color-scheme:light;
  --ux-page:#F4F2EE;
  --ux-surface:#FFFFFF;
  --ux-surface-2:#F5F3EF;
  --ux-surface-3:#EAE7E1;
  --ux-ink:#16151B;
  --ux-ink-2:#57535F;
  --ux-ink-3:#8E8A97;
  --ux-line:rgba(22,21,27,.09);
  --ux-line-2:rgba(22,21,27,.17);
  --ux-accent:#6A57F2;
  --ux-accent-2:#2F8FE0;
  --ux-accent-soft:rgba(106,87,242,.12);
  --ux-accent-ink:#FFFFFF;
  --ux-mint:#119C72;
  --ux-warn:#D6731E;
  --ux-danger:#D93A55;
  --ux-glass:rgba(255,255,255,.58);
  --ux-glass-line:rgba(255,255,255,.85);
  --ux-shadow:rgba(40,30,80,.14);
  --ux-shadow-strong:rgba(40,30,80,.3);
  --ux-grad:linear-gradient(120deg,#7B61FF,#3D8BFF 55%,#1FB89A);
  --ux-ease:cubic-bezier(.2,.8,.2,1);
  --ux-spring:cubic-bezier(.34,1.45,.64,1);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    color-scheme:dark;
    --ux-page:#07080D;
    --ux-surface:#13141C;
    --ux-surface-2:#1A1B25;
    --ux-surface-3:#252632;
    --ux-ink:#F4F0E8;
    --ux-ink-2:rgba(244,240,232,.68);
    --ux-ink-3:rgba(244,240,232,.42);
    --ux-line:rgba(255,255,255,.08);
    --ux-line-2:rgba(255,255,255,.16);
    --ux-accent:#B7A4FF;
    --ux-accent-2:#7DB4FF;
    --ux-accent-soft:rgba(183,164,255,.15);
    --ux-accent-ink:#0B0C12;
    --ux-mint:#7EE8C0;
    --ux-warn:#FFB26B;
    --ux-danger:#FF7D8C;
    --ux-glass:rgba(255,255,255,.07);
    --ux-glass-line:rgba(255,255,255,.18);
    --ux-shadow:rgba(0,0,0,.45);
    --ux-shadow-strong:rgba(0,0,0,.72);
    --ux-grad:linear-gradient(120deg,#B7A4FF,#7DB4FF 55%,#A5F2D3);
  }
}
:root[data-theme="dark"]{
  color-scheme:dark;
  --ux-page:#07080D;
  --ux-surface:#13141C;
  --ux-surface-2:#1A1B25;
  --ux-surface-3:#252632;
  --ux-ink:#F4F0E8;
  --ux-ink-2:rgba(244,240,232,.68);
  --ux-ink-3:rgba(244,240,232,.42);
  --ux-line:rgba(255,255,255,.08);
  --ux-line-2:rgba(255,255,255,.16);
  --ux-accent:#B7A4FF;
  --ux-accent-2:#7DB4FF;
  --ux-accent-soft:rgba(183,164,255,.15);
  --ux-accent-ink:#0B0C12;
  --ux-mint:#7EE8C0;
  --ux-warn:#FFB26B;
  --ux-danger:#FF7D8C;
  --ux-glass:rgba(255,255,255,.07);
  --ux-glass-line:rgba(255,255,255,.18);
  --ux-shadow:rgba(0,0,0,.45);
  --ux-shadow-strong:rgba(0,0,0,.72);
  --ux-grad:linear-gradient(120deg,#B7A4FF,#7DB4FF 55%,#A5F2D3);
}
/* 요소 공통 베이스 — 루트에 .ux 클래스를 붙입니다 */
.ux,.ux *,.ux *::before,.ux *::after{box-sizing:border-box}
.ux{
  font-family:"Pretendard Variable",Pretendard,-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Segoe UI",Roboto,"Noto Sans KR",sans-serif;
  color:var(--ux-ink);-webkit-font-smoothing:antialiased;letter-spacing:-.01em;
  -webkit-tap-highlight-color:transparent;
  word-break:keep-all;overflow-wrap:break-word;
}
/* :where()로 명시도를 0으로 둬서, 요소 클래스가 버튼·입력의 색과 글꼴을 덮어쓸 수 있게 합니다 */
:where(.ux) :is(button,input,textarea,select){font:inherit;color:inherit}
:where(.ux) button{cursor:pointer}
.ux :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
.ux [hidden]{display:none!important}
/* 모션 줄이기: 전환은 즉시 끝나고, 무한 반복은 한 번으로 줄여 최종 상태가 보이게 합니다 */
@media (prefers-reduced-motion:reduce){
  .ux,.ux *,.ux *::before,.ux *::after{
    animation-duration:.001ms!important;animation-iteration-count:1!important;
    transition-duration:.001ms!important;scroll-behavior:auto!important;
  }
}
</style>

<style>
.u236{position:relative;width:300px;height:480px;border-radius:32px;overflow:hidden;background:#0E0F14;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u236-ft{position:absolute;left:0;right:0;bottom:0;height:300px;padding:22px 20px;color:#E8E9F2;transform-origin:50% 100%;transform:scale(calc(.94 + .06 * var(--r,0)));opacity:calc(.35 + .65 * var(--r,0))}
.u236-nl small{font-size:10px;font-weight:850;letter-spacing:.08em;color:#8B8FA8}
.u236-nl b{display:block;margin:4px 0 10px;font-size:15px;font-weight:850}
.u236-fm{display:flex;gap:6px}
.u236-fm input{flex:1;min-width:0;height:36px;padding:0 12px;border:0;border-radius:11px;background:rgba(255,255,255,.08);color:#fff;font:inherit;font-size:12px;font-weight:600;outline:none;box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)}
.u236-fm input:focus{box-shadow:inset 0 0 0 1.5px #818CF8}
.u236-go{height:36px;padding:0 14px;border:0;border-radius:11px;background:#fff;color:#0E0F14;font:inherit;font-size:12px;font-weight:850;cursor:pointer;display:inline-flex;align-items:center;gap:5px;transition:background .25s,color .25s}
.u236-go svg{width:13px;height:13px;display:none}
.u236-go.is-ok{background:#34D399;color:#05261A}
.u236-go.is-ok svg{display:block}
.u236-go:focus-visible{outline:2px solid #818CF8;outline-offset:2px}
.u236-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:22px;font-size:11px;font-weight:650;color:#8B8FA8}
.u236-cols b{display:block;margin-bottom:6px;font-size:11px;font-weight:850;color:#E8E9F2}
.u236-cols span{display:block;margin-top:4px}
.u236-wm{position:absolute;left:14px;right:14px;bottom:8px;font-size:68px;line-height:.9;font-weight:950;letter-spacing:-.06em;background:linear-gradient(180deg,#fff,rgba(255,255,255,.08));-webkit-background-clip:text;background-clip:text;color:transparent;transform:translateY(calc(26px * (1 - var(--r,0))))}
.u236-sc{position:absolute;inset:0;overflow-y:auto;overscroll-behavior:contain;scrollbar-width:none;pointer-events:none}
.u236-sc::-webkit-scrollbar{display:none}
.u236-sc:focus-visible{outline:2px solid #818CF8;outline-offset:-4px;border-radius:32px}
.u236-mn{position:relative;z-index:1;pointer-events:auto;background:var(--ux-surface);border-radius:0 0 28px 28px;box-shadow:0 20px 40px -10px rgba(0,0,0,.5);padding:38px 22px 30px}
.u236-mn small{font-size:10px;font-weight:850;letter-spacing:.08em;color:var(--ux-accent)}
.u236-mn h3{margin:8px 0 0;font-size:25px;line-height:1.15;font-weight:900;letter-spacing:-.04em}
.u236-mn p{margin:10px 0 0;font-size:12px;line-height:1.6;font-weight:600;color:var(--ux-ink-2)}
.u236-cs{margin-top:22px;padding:16px;border-radius:18px;background:var(--ux-surface-2)}
.u236-cs small{color:var(--ux-ink-3)}
.u236-cs b{display:block;margin-top:4px;font-size:16px;font-weight:900;letter-spacing:-.02em}
.u236-cs i{display:block;height:120px;margin-top:12px;border-radius:12px;background:linear-gradient(135deg,var(--ux-accent-soft),color-mix(in srgb,var(--ux-accent) 30%,var(--ux-surface)))}
.u236-sp{height:300px;pointer-events:none}
@media (prefers-reduced-motion: reduce){.u236-ft{transform:none;opacity:1}.u236-wm{transform:none}}
</style>
<div class="ux u236">
  <footer class="u236-ft">
    <div class="u236-nl"><small>Newsletter</small><b>Once a month, only useful news</b><form class="u236-fm"><input type="email" placeholder="Email address" aria-label="Email address" autocomplete="off"><button type="submit" class="u236-go"><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M2.5 7.5l3 3 6-6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span></span></button></form></div>
    <div class="u236-cols"><div><b>Product</b><span>Features</span><span>Pricing</span></div><div><b>Company</b><span>About</span><span>Careers</span></div><div><b>Help</b><span>Docs</span><span>Contact</span></div></div>
    <div class="u236-wm" aria-hidden="true">Quiet.</div>
  </footer>
  <div class="u236-sc" tabindex="0" aria-label="Page">
    <div class="u236-mn"><small>Final section</small><h3>Good tools<br>work quietly</h3><p>We handle the rest so your team can focus on the work.</p><div class="u236-cs"><small>Case study</small><b>Cut launch time in half</b><i></i></div></div>
    <div class="u236-sp"></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u236-sc'), sp = root.querySelector('.u236-sp'), fm = root.querySelector('.u236-fm'), inp = fm.querySelector('input'), go = root.querySelector('.u236-go'), lb = go.querySelector('span');
  function onScroll() { var max = sc.scrollHeight - sc.clientHeight, r = Math.max(0, Math.min(1, 1 - (max - sc.scrollTop) / sp.offsetHeight)); root.style.setProperty('--r', r.toFixed(3)); }
  sc.addEventListener('scroll', onScroll, { passive: true });
  fm.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!inp.value) inp.value = 'hello@quiet.so';
    go.classList.add('is-ok'); lb.textContent = 'Subscribed';
  });
  lb.textContent = 'Subscribe';
  onScroll();
})();
</script>
--- Code end ---
