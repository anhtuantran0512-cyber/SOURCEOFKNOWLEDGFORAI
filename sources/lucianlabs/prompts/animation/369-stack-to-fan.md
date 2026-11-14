---
source: "lucianlabs"
id: "369"
title: "Photo stack that fans out"
category: "Sections & Content"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#369"
tags: ["stack", "fan", "photos", "layout", "morph"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Photo stack that fans out (369, Sections & Content)
[What it does] Hover the stack of polaroids and it fans out slightly; tap it and the photos fly out into a neat grid. Tap one photo in the grid and the photos gather back into a stack with that one on top, each landing at a slightly different angle.
[How to use it] Hover the stack, tap it to spread it out, then tap a photo to gather them again

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
<!-- Lucian UX/UI Prompt #369 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#369 -->
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
.u369{position:relative;width:340px;height:330px;border-radius:28px;background:var(--ux-surface-2);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u369-p{position:absolute;left:50%;top:50%;width:96px;height:112px;margin:-56px 0 0 -48px;border:0;padding:7px 7px 24px;border-radius:6px;background:#fff;box-shadow:0 10px 20px -10px rgba(0,0,0,.45),0 0 0 1px rgba(0,0,0,.05);transition:transform .7s cubic-bezier(.3,1.2,.4,1);transition-delay:var(--dl,0ms)}
.u369-p i{display:block;width:100%;height:100%;border-radius:2px;background:var(--bg)}
.u369-p span{position:absolute;left:0;right:0;bottom:5px;text-align:center;font:600 10.5px/1 ui-rounded,-apple-system,sans-serif;color:#555}
.u369-p:focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
</style>
<div class="ux u369"></div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var CAP = ['Sea', 'Alley', 'Sunset', 'Forest path', 'Snow', 'Flowers'];
  var BG = ['linear-gradient(#74C0FC,#1C7ED6)', 'linear-gradient(135deg,#FFD8A8,#E8590C)', 'linear-gradient(#FFD43B,#F76707 55%,#5F3DC4)', 'linear-gradient(#B2F2BB,#2F9E44)', 'linear-gradient(#F1F3F5,#ADB5BD)', 'radial-gradient(circle at 40% 40%,#FFDEEB,#E64980)'];
  var order = [0, 1, 2, 3, 4, 5], spread = false, hover = false;
  var tilt = CAP.map(function () { return (Math.random() - 0.5) * 16; });
  var ps = CAP.map(function (c, i) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'u369-p';
    b.innerHTML = '<i style="--bg:' + BG[i] + '"></i><span></span>';
    b.querySelector('span').textContent = c;
    b.addEventListener('click', function () { tap(i); });
    b.addEventListener('pointerenter', function () { hover = true; if (!spread) place(); });
    b.addEventListener('pointerleave', function () { hover = false; if (!spread) place(); });
    root.appendChild(b);
    return b;
  });
  function place() {
    order.forEach(function (i, z) {
      var b = ps[i], t;
      b.style.zIndex = spread ? 1 : z + 1;
      if (spread) {
        var col = z % 3, row = Math.floor(z / 3);
        t = 'translate(' + ((col - 1) * 104) + 'px,' + ((row - 0.5) * 124) + 'px) rotate(0deg)';
        b.style.setProperty('--dl', (z * 40) + 'ms');
        b.setAttribute('aria-label', CAP[i] + ', tap to gather with this on top');
      } else {
        var k = z - (order.length - 1);
        t = hover ? 'translate(' + (k * 16) + 'px,' + (k * -3) + 'px) rotate(' + (k * 7 + 2) + 'deg)' : 'translate(' + (k * 1.5) + 'px,' + (k * -1.5) + 'px) rotate(' + tilt[i] + 'deg)';
        b.style.setProperty('--dl', ((order.length - 1 - z) * 30) + 'ms');
        b.setAttribute('aria-label', 'Photo stack, tap to spread');
        b.tabIndex = z === order.length - 1 ? 0 : -1;
      }
      if (spread) b.tabIndex = 0;
      b.style.transform = t;
    });
  }
  function tap(i) {
    if (!spread) { spread = true; hover = false; place(); return; }
    order = order.filter(function (x) { return x !== i; }).concat(i);
    tilt = tilt.map(function () { return (Math.random() - 0.5) * 16; });
    tilt[i] = (Math.random() - 0.5) * 6;
    spread = false; place();
    ps[i].focus({ preventScroll: true });
  }
  place();
})();
</script>
--- Code end ---
