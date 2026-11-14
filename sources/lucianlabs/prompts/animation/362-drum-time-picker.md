---
source: "lucianlabs"
id: "362"
title: "Rolling drum time picker"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#362"
tags: ["picker", "time", "wheel", "scroll-snap", "3d"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Rolling drum time picker (362, Scroll Motion)
[What it does] Three drums for AM/PM, hours and minutes roll like cylinders, and whatever sits on the middle line is selected. Let go and it settles neatly on the nearest slot, while the values above and below tilt and fade as if curving around the back of the drum. The alarm label and time remaining at the top update as you pick.
[How to use it] Scroll each drum up and down, or focus a drum and press ↑/↓

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
<!-- Lucian UX/UI Prompt #362 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#362 -->
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
.u362{position:relative;width:340px;height:330px;display:flex;flex-direction:column;padding:18px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u362-al{margin:0;font-size:20px;font-weight:850;letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.u362-sub{margin:2px 0 0;font-size:12.5px;font-weight:700;color:var(--ux-ink-3)}
.u362-pk{position:relative;display:flex;justify-content:center;gap:4px;margin-top:auto;height:216px;-webkit-mask-image:linear-gradient(transparent,#000 30%,#000 70%,transparent);mask-image:linear-gradient(transparent,#000 30%,#000 70%,transparent)}
.u362-band{position:absolute;left:0;right:0;top:90px;height:36px;border-radius:12px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line)}
.u362-col{position:relative;width:76px;height:216px;overflow-y:auto;scroll-snap-type:y mandatory;scrollbar-width:none;perspective:300px;outline:none;border-radius:12px}
.u362-col::-webkit-scrollbar{display:none}
.u362-col:focus-visible{box-shadow:inset 0 0 0 2px var(--ux-accent)}
.u362-col ul{margin:0;padding:90px 0;list-style:none}
.u362-col li{height:36px;display:flex;align-items:center;justify-content:center;scroll-snap-align:center;font-size:22px;font-weight:750;color:var(--ux-ink);font-variant-numeric:tabular-nums;transform-style:preserve-3d;backface-visibility:hidden}
.u362-col.ap li{font-size:17px}
</style>
<div class="ux u362">
  <p class="u362-al" aria-live="polite"></p>
  <p class="u362-sub"><span class="u362-left"></span> · Repeats on weekdays</p>
  <div class="u362-pk">
    <span class="u362-band" aria-hidden="true"></span>
    <div class="u362-col ap" tabindex="0" role="listbox" aria-label="AM or PM"><ul></ul></div>
    <div class="u362-col" tabindex="0" role="listbox" aria-label="Hour"><ul></ul></div>
    <div class="u362-col" tabindex="0" role="listbox" aria-label="Minute"><ul></ul></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var cols = Array.prototype.slice.call(root.querySelectorAll('.u362-col')), al = root.querySelector('.u362-al'), left = root.querySelector('.u362-left');
  var AP = ['AM', 'PM'];
  var DATA = [AP, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], []];
  for (var m = 0; m < 60; m += 5) DATA[2].push(String(m).padStart(2, '0'));
  var IH = 36, sel = [0, 6, 6];
  cols.forEach(function (c, ci) {
    var ul = c.querySelector('ul');
    DATA[ci].forEach(function (v, k) { var li = document.createElement('li'); li.textContent = v; li.setAttribute('role', 'option'); ul.appendChild(li); });
    var raf = 0, t = 0;
    c.addEventListener('scroll', function () {
      if (!raf) raf = requestAnimationFrame(function () { raf = 0; bend(c, ci); });
      clearTimeout(t);
      t = setTimeout(function () { pick(c, ci); }, 120);
    }, { passive: true });
    c.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowDown' ? 1 : e.key === 'ArrowUp' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      c.scrollTo({ top: Math.max(0, Math.min(DATA[ci].length - 1, sel[ci] + d)) * IH, behavior: 'smooth' });
    });
  });
  function bend(c, ci) {
    var mid = c.scrollTop + 108;
    Array.prototype.forEach.call(c.querySelectorAll('li'), function (li, k) {
      var d = (k * IH + 90 + 18 - mid) / IH, a = Math.max(-80, Math.min(80, d * 22));
      li.style.transform = 'rotateX(' + (-a).toFixed(1) + 'deg) translateZ(' + (-Math.abs(d) * 4).toFixed(1) + 'px)';
      li.style.opacity = Math.max(0.15, 1 - Math.abs(d) * 0.28).toFixed(2);
    });
  }
  function pick(c, ci) {
    var k = Math.max(0, Math.min(DATA[ci].length - 1, Math.round(c.scrollTop / IH)));
    sel[ci] = k;
    Array.prototype.forEach.call(c.querySelectorAll('li'), function (li, j) { li.setAttribute('aria-selected', String(j === k)); });
    text();
  }
  function text() {
    var hour = DATA[1][sel[1]], mm = DATA[2][sel[2]];
    al.textContent = 'Alarm ' + hour + ':' + mm + ' ' + AP[sel[0]];
    var target = (hour % 12 + (sel[0] ? 12 : 0)) * 60 + (+mm), now = 22 * 60 + 40, diff = (target - now + 1440) % 1440;
    var h = Math.floor(diff / 60), m = diff % 60;
    left.textContent = 'Rings in ' + h + ' h ' + m + ' min';
  }
  [0, 6, 6].forEach(function (k, ci) { cols[ci].scrollTop = k * IH; bend(cols[ci], ci); pick(cols[ci], ci); });
})();
</script>
--- Code end ---
