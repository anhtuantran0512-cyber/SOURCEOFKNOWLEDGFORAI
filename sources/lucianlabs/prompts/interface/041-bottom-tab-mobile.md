---
source: "lucianlabs"
id: "041"
title: "Notched bottom tab bar"
category: "Menus & Tabs"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#041"
tags: ["tab-bar", "mobile", "navigation", "notch", "indicator"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Notched bottom tab bar (041, Menus & Tabs)
[What it does] A round button rises above the selected tab while the top edge of the bar dips into a matching notch and slides along with it. The icon lifts up into the circle and the label appears below.
[How to use it] Press the tabs one by one. With a keyboard, use the left and right arrow keys

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
<!-- Lucian UX/UI Prompt #041 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#041 -->
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
.u041{--x:34px;position:relative;width:350px;height:170px;display:flex;align-items:flex-end}
.u041-bar{position:relative;width:100%;height:84px;border-radius:28px;background:var(--ux-surface);
  -webkit-mask:radial-gradient(circle 42px at var(--x) -4px,transparent 96%,#000 100%);mask:radial-gradient(circle 42px at var(--x) -4px,transparent 96%,#000 100%);
  box-shadow:0 0 0 1px var(--ux-line)}
.u041-shadow{position:absolute;left:0;right:0;bottom:0;height:84px;border-radius:28px;box-shadow:0 24px 40px -24px var(--ux-shadow-strong);pointer-events:none}
.u041-bub{position:absolute;left:var(--x);top:calc(100% - 84px - 35px);width:62px;height:62px;margin-left:-31px;border-radius:50%;background:var(--ux-grad);box-shadow:0 14px 26px -12px rgba(91,72,255,.7)}
.u041-tabs{position:absolute;left:0;right:0;bottom:0;height:84px;display:flex;margin:0;padding:0 14px;list-style:none}
.u041-tabs>li{flex:1;display:flex}
.u041-tab{position:relative;flex:1;height:100%;border:0;padding:0;background:none;color:var(--ux-ink-3)}
.u041-tab:hover .u041-ic{color:var(--ux-ink)}
.u041-tab:focus-visible{outline:2px solid var(--ux-accent);outline-offset:-6px;border-radius:18px}
.u041-ic{position:absolute;left:50%;top:22px;width:26px;height:26px;margin-left:-13px;transition:transform .55s var(--ux-spring),color .3s}
.u041-ic svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.u041-lab{position:absolute;left:0;right:0;bottom:12px;font-size:11.5px;font-weight:700;color:var(--ux-ink);opacity:0;transform:translateY(6px);transition:opacity .3s,transform .45s var(--ux-spring)}
.u041-tab[aria-selected="true"] .u041-ic{transform:translateY(-39px);color:var(--ux-accent-ink)}
.u041-tab[aria-selected="true"] .u041-ic svg{stroke-width:2.2}
.u041-tab[aria-selected="true"] .u041-lab{opacity:1;transform:none}
.u041-bd{position:absolute;left:calc(50% + 6px);top:16px;min-width:18px;height:18px;padding:0 5px;border-radius:9px;background:#FF5A6E;color:#fff;font-size:10.5px;font-weight:800;line-height:18px;font-style:normal;box-shadow:0 0 0 2.5px var(--ux-surface);transition:transform .45s var(--ux-spring),opacity .3s}
.u041-tab[aria-selected="true"] .u041-bd{transform:scale(0);opacity:0}
</style>
<div class="ux u041">
  <span class="u041-shadow" aria-hidden="true"></span>
  <div class="u041-bar" aria-hidden="true"></div>
  <span class="u041-bub" aria-hidden="true"></span>
  <ul class="u041-tabs" role="tablist" aria-label="Bottom navigation">
    <li role="none"><button class="u041-tab" type="button" role="tab" aria-selected="true"><span class="u041-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 11l8-6.5 8 6.5V19a1 1 0 0 1-1 1h-4.5v-5h-5v5H5a1 1 0 0 1-1-1z"/></svg></span><span class="u041-lab">Home</span></button></li>
    <li role="none"><button class="u041-tab" type="button" role="tab" aria-selected="false"><span class="u041-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/></svg></span><span class="u041-lab">Explore</span></button></li>
    <li role="none"><button class="u041-tab" type="button" role="tab" aria-selected="false"><span class="u041-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6.5 3.5h11a1 1 0 0 1 1 1v16l-6.5-4.5-6.5 4.5v-16a1 1 0 0 1 1-1z"/></svg></span><span class="u041-lab">Saved</span></button></li>
    <li role="none"><button class="u041-tab" type="button" role="tab" aria-selected="false"><span class="u041-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15zM10 20.5a2.2 2.2 0 0 0 4 0"/></svg></span><em class="u041-bd" aria-label="3 new alerts">3</em><span class="u041-lab">Alerts</span></button></li>
    <li role="none"><button class="u041-tab" type="button" role="tab" aria-selected="false"><span class="u041-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="8.5" r="3.8"/><path d="M4.5 20c.9-3.8 3.8-5.8 7.5-5.8s6.6 2 7.5 5.8"/></svg></span><span class="u041-lab">Me</span></button></li>
  </ul>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var tabs = Array.prototype.slice.call(root.querySelectorAll('.u041-tab'));
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var x = 0, v = 0, target = 0, raf = 0;
  function center(t) { return t.parentNode.offsetLeft + t.offsetWidth / 2; }
  function step() {
    var a = (target - x) * 0.16 - v * 0.42;
    v += a; x += v;
    root.style.setProperty('--x', x.toFixed(2) + 'px');
    if (Math.abs(target - x) > 0.3 || Math.abs(v) > 0.3) raf = requestAnimationFrame(step);
    else { x = target; v = 0; root.style.setProperty('--x', x + 'px'); raf = 0; }
  }
  function select(i, focus) {
    tabs.forEach(function (t, k) { t.setAttribute('aria-selected', String(k === i)); t.tabIndex = k === i ? 0 : -1; });
    if (focus) tabs[i].focus();
    target = center(tabs[i]);
    if (rm) { x = target; root.style.setProperty('--x', x + 'px'); return; }
    if (!raf) raf = requestAnimationFrame(step);
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { select(i); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (d) { e.preventDefault(); select((i + d + tabs.length) % tabs.length, true); }
    });
  });
  x = target = center(tabs[0]);
  root.style.setProperty('--x', x + 'px');
  select(0);
})();
</script>
--- Code end ---
