---
source: "lucianlabs"
id: "021"
title: "Day–night sky switch"
category: "Toggles & Pickers"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#021"
tags: ["toggle", "switch", "day-night", "theme", "sky"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Day–night sky switch (021, Toggles & Pickers)
[What it does] The sun knob rolls across and turns into a cratered moon. The sky deepens to night, the clouds sink away and the stars start to twinkle.
[How to use it] Press the switch to flip between day and night

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
<!-- Lucian UX/UI Prompt #021 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#021 -->
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
.u021{position:relative;width:300px;height:210px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px}
.u021-sw{position:relative;width:224px;height:94px;border:0;padding:0;border-radius:999px;overflow:hidden;isolation:isolate;
  background:linear-gradient(180deg,#5DB7FF,#9ED8FF);box-shadow:inset 0 4px 10px rgba(0,30,80,.28),inset 0 -2px 4px rgba(255,255,255,.4),0 18px 34px -18px rgba(40,110,200,.7);transition:box-shadow .8s var(--ux-ease)}
.u021-sw::before{content:"";position:absolute;inset:0;z-index:0;background:linear-gradient(180deg,#141A3A,#232C5C);opacity:0;transition:opacity .8s var(--ux-ease)}
.u021-sw:focus-visible{outline:2px solid var(--ux-accent);outline-offset:5px}
.u021.is-night .u021-sw::before{opacity:1}
.u021.is-night .u021-sw{box-shadow:inset 0 4px 10px rgba(0,0,0,.5),inset 0 -2px 4px rgba(255,255,255,.08),0 18px 34px -18px rgba(20,24,70,.9)}

.u021-halo{position:absolute;z-index:1;left:47px;top:47px;width:0;height:0;transition:transform .9s var(--ux-spring)}
.u021-halo i{position:absolute;border-radius:50%;background:rgba(255,255,255,.12)}
.u021-halo i:nth-child(1){width:130px;height:130px;margin:-65px}
.u021-halo i:nth-child(2){width:176px;height:176px;margin:-88px}
.u021-halo i:nth-child(3){width:222px;height:222px;margin:-111px}
.u021.is-night .u021-halo{transform:translateX(130px)}
.u021-knob{position:absolute;z-index:3;left:8px;top:8px;width:78px;height:78px;border-radius:50%;overflow:hidden;
  background:radial-gradient(circle at 35% 30%,#FFF1A8,#FFD23F 45%,#F8A91E);box-shadow:0 6px 14px -4px rgba(140,80,0,.5),inset -4px -6px 10px rgba(200,110,0,.35),inset 4px 4px 8px rgba(255,255,255,.5);
  transition:transform .9s var(--ux-spring)}
.u021-moon{position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle at 35% 30%,#F4F6FB,#C9CFDD 60%,#A9B0C2);opacity:0;transform:translateX(100%);transition:transform .8s var(--ux-ease),opacity .4s var(--ux-ease)}
.u021-moon i{position:absolute;border-radius:50%;background:#A3AABC;box-shadow:inset 1px 2px 2px rgba(0,0,0,.18)}
.u021-moon i:nth-child(1){left:20px;top:16px;width:20px;height:20px}
.u021-moon i:nth-child(2){left:46px;top:40px;width:14px;height:14px}
.u021-moon i:nth-child(3){left:24px;top:48px;width:9px;height:9px}
.u021.is-night .u021-knob{transform:translateX(130px) rotate(200deg)}
.u021.is-night .u021-moon{opacity:1;transform:none}
.u021-clouds{position:absolute;z-index:2;inset:0;transition:transform .8s var(--ux-ease),opacity .6s var(--ux-ease)}
.u021-clouds i{position:absolute;border-radius:999px;background:#fff}
.u021-clouds i:nth-child(1){right:-10px;bottom:-18px;width:120px;height:56px;box-shadow:-46px 8px 0 -6px #fff,-80px 18px 0 -10px #fff}
.u021-clouds i:nth-child(2){right:20px;bottom:-30px;width:96px;height:52px;background:#E3F1FF;box-shadow:-44px 6px 0 -8px #E3F1FF;z-index:-1}
.u021.is-night .u021-clouds{transform:translateY(80px);opacity:0}
.u021-stars{position:absolute;z-index:1;inset:0;opacity:0;transform:translateY(-30px);transition:transform .8s var(--ux-ease),opacity .6s var(--ux-ease)}
.u021-stars i{position:absolute;width:4px;height:4px;border-radius:50%;background:#fff;box-shadow:0 0 6px #fff;animation:u021-tw 2.4s ease-in-out infinite}
.u021.is-night .u021-stars{opacity:1;transform:none}
@keyframes u021-tw{50%{opacity:.3;transform:scale(.6)}}
.u021-lab{margin:0;position:relative;width:200px;height:24px;overflow:hidden;text-align:center;font-size:16px;font-weight:720;letter-spacing:-.02em}
.u021-lab span{position:absolute;left:0;right:0;top:0;line-height:24px;transition:transform .55s var(--ux-spring),opacity .3s var(--ux-ease)}
.u021-lab small{font-weight:550;color:var(--ux-ink-3);margin-left:6px}
.u021-lab span+span{transform:translateY(100%);opacity:0}
.u021.is-night .u021-lab span:first-child{transform:translateY(-100%);opacity:0}
.u021.is-night .u021-lab span+span{transform:none;opacity:1}
</style>
<div class="ux u021">
  <button class="u021-sw" type="button" role="switch" aria-checked="false" aria-label="Night sky mode">
    <span class="u021-halo" aria-hidden="true"><i></i><i></i><i></i></span>
    <span class="u021-stars" aria-hidden="true">
      <i style="left:30px;top:20px"></i><i style="left:58px;top:56px;animation-delay:-.6s;width:3px;height:3px"></i><i style="left:86px;top:26px;animation-delay:-1.2s"></i><i style="left:44px;top:72px;animation-delay:-1.8s;width:3px;height:3px"></i><i style="left:110px;top:60px;animation-delay:-.9s;width:2px;height:2px"></i><i style="left:20px;top:46px;animation-delay:-1.5s;width:2px;height:2px"></i>
    </span>
    <span class="u021-clouds" aria-hidden="true"><i></i><i></i></span>
    <span class="u021-knob" aria-hidden="true"><span class="u021-moon"><i></i><i></i><i></i></span></span>
  </button>
  <p class="u021-lab" aria-hidden="true"><span>Clear day<small>2:30 PM</small></span><span>Quiet night<small>9:30 PM</small></span></p>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sw = root.querySelector('.u021-sw');
  sw.addEventListener('click', function () {
    var night = !root.classList.contains('is-night');
    root.classList.toggle('is-night', night);
    sw.setAttribute('aria-checked', String(night));
  });
})();
</script>
--- Code end ---
