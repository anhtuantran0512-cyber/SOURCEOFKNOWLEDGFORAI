---
source: "lucianlabs"
id: "231"
title: "Tilt-to-flat product screen"
category: "Hero & Backgrounds"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#231"
tags: ["hero", "scroll", "perspective", "product-shot", "landing"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Tilt-to-flat product screen (231, Hero & Backgrounds)
[What it does] Below a landing page hero, the product screen starts small and tilted back, then stands up, grows and casts a deeper shadow as you scroll down until it faces you flat. Once it's flat the chart bars inside fill up, and scrolling back up lays it down again. The hint arrow at the bottom disappears once you start scrolling.
[How to use it] Scroll down inside the card to watch the product screen straighten

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
<!-- Lucian UX/UI Prompt #231 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#231 -->
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
.u231{position:relative;width:300px;height:480px;border-radius:32px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u231-sc{position:absolute;inset:0;overflow-y:auto;overscroll-behavior:contain;scrollbar-width:none;perspective:900px;background:radial-gradient(110% 50% at 50% 0%,var(--ux-accent-soft),transparent 70%)}
.u231-sc::-webkit-scrollbar{display:none}
.u231-sc:focus-visible{outline:2px solid var(--ux-accent);outline-offset:-4px;border-radius:32px}
.u231-hd{padding:34px 22px 0;text-align:center}
.u231-hd small{display:inline-block;padding:4px 10px;border-radius:999px;background:var(--ux-surface);box-shadow:inset 0 0 0 1px var(--ux-line);font-size:10px;font-weight:800;color:var(--ux-accent)}
.u231-hd h3{margin:12px 0 0;font-size:26px;line-height:1.15;font-weight:900;letter-spacing:-.04em}
.u231-hd p{margin:9px 0 0;font-size:11.5px;font-weight:600;color:var(--ux-ink-2)}
.u231-hd b{display:inline-block;margin-top:14px;padding:8px 16px;border-radius:999px;background:var(--ux-ink);color:var(--ux-surface);font-size:11.5px;font-weight:800}
.u231-st{margin:26px 14px 0;transform-origin:50% 0;will-change:transform}
.u231-win{border-radius:14px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 var(--sy,10px) var(--sb,20px) -12px var(--ux-shadow-strong);overflow:hidden}
.u231-tb{display:flex;gap:4px;padding:8px 10px;background:var(--ux-surface-2)}
.u231-tb i{width:7px;height:7px;border-radius:50%;background:var(--ux-line)}
.u231-bd{padding:10px 12px 12px}
.u231-kp{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.u231-kp div{padding:7px 8px;border-radius:9px;background:var(--ux-surface-2)}
.u231-kp small{display:block;font-size:8px;font-weight:800;color:var(--ux-ink-3)}
.u231-kp b{font-size:13px;font-weight:900;font-variant-numeric:tabular-nums}
.u231-ch{display:flex;align-items:flex-end;gap:5px;height:74px;margin-top:9px;padding:6px 4px 0;border-radius:9px;background:linear-gradient(var(--ux-line) 1px,transparent 1px) 0 0/100% 18px}
.u231-ch i{flex:1;height:100%;border-radius:4px 4px 0 0;background:linear-gradient(var(--ux-accent),color-mix(in srgb,var(--ux-accent) 45%,transparent));transform-origin:50% 100%;transform:scaleY(var(--g,.15));transition:transform .7s cubic-bezier(.3,1.3,.5,1);transition-delay:calc(var(--i) * 50ms)}
.u231-lg{margin:30px 22px 0;text-align:center;font-size:10px;font-weight:800;color:var(--ux-ink-3)}
.u231-lgs{display:flex;justify-content:center;gap:16px;margin-top:10px;font-size:13px;font-weight:900;color:var(--ux-ink-3);opacity:.7;letter-spacing:-.02em}
.u231-ft{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:22px 16px 40px}
.u231-ft div{padding:12px;border-radius:14px;background:var(--ux-surface-2)}
.u231-ft b{display:block;font-size:12px;font-weight:850}
.u231-ft span{font-size:10px;font-weight:600;color:var(--ux-ink-3)}
.u231-hint{position:absolute;left:50%;bottom:14px;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:2px;font-size:9.5px;font-weight:800;color:var(--ux-ink-3);pointer-events:none;transition:opacity .3s}
.u231-hint svg{width:14px;height:14px;animation:u231-b 1.4s ease-in-out infinite}
@keyframes u231-b{50%{transform:translateY(4px)}}
@media (prefers-reduced-motion: reduce){.u231-hint svg{animation:none}.u231-ch i{transition:none}}
</style>
<div class="ux u231">
  <div class="u231-sc" tabindex="0" aria-label="Landing page preview">
    <div class="u231-hd"><small>Team dashboard</small><h3>Every number<br>on one screen</h3><p>Pulls scattered metrics together, live.</p><b>Free trial</b></div>
    <div class="u231-st" aria-hidden="true"><div class="u231-win"><div class="u231-tb"><i></i><i></i><i></i></div><div class="u231-bd">
      <div class="u231-kp"><div><small>Monthly revenue</small><b>₩48M</b></div><div><small>Sign-ups</small><b>1,284</b></div><div><small>Return rate</small><b>62%</b></div></div>
      <div class="u231-ch"></div>
    </div></div></div>
    <div class="u231-lg">Teams using it<div class="u231-lgs"><span>Northwind</span><span>Acme</span><span>Globex</span></div></div>
    <div class="u231-ft"><div><b>Live sync</b><span>Updates every second</span></div><div><b>Permissions</b><span>Split views by team</span></div></div>
  </div>
  <div class="u231-hint" aria-hidden="true">Scroll<svg viewBox="0 0 14 14"><path d="M3 5l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u231-sc'), st = root.querySelector('.u231-st'), win = root.querySelector('.u231-win'), ch = root.querySelector('.u231-ch'), hint = root.querySelector('.u231-hint');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var H = [0.42, 0.58, 0.5, 0.72, 0.64, 0.86, 0.78, 0.95];
  H.forEach(function (h, i) { var b = document.createElement('i'); b.style.setProperty('--i', i); b.dataset.h = h; ch.appendChild(b); });
  var bars = ch.querySelectorAll('i'), full = false, raf = 0;
  function paint() {
    raf = 0;
    var p = rm ? 1 : Math.max(0, Math.min(1, sc.scrollTop / 210)), e = 1 - Math.pow(1 - p, 2);
    st.style.transform = 'rotateX(' + (34 * (1 - e)).toFixed(2) + 'deg) scale(' + (0.84 + 0.16 * e).toFixed(3) + ') translateY(' + (-18 * e).toFixed(1) + 'px)';
    win.style.setProperty('--sy', (10 + 24 * e).toFixed(1) + 'px'); win.style.setProperty('--sb', (20 + 34 * e).toFixed(1) + 'px');
    hint.style.opacity = sc.scrollTop > 8 ? 0 : 1;
    var f = p > 0.88;
    if (f !== full) { full = f; bars.forEach(function (b) { b.style.setProperty('--g', f ? b.dataset.h : 0.15); }); }
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(paint); }, { passive: true });
  paint();
})();
</script>
--- Code end ---
