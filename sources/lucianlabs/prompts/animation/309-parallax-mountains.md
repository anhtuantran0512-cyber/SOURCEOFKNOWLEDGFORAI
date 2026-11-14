---
source: "lucianlabs"
id: "309"
title: "Layered mountain parallax"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#309"
tags: ["scroll", "parallax", "landscape", "hero", "depth"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Layered mountain parallax (309, Scroll Motion)
[What it does] Scroll inside and the sky, far mountains, near mountains and forest move at different speeds to create depth, while the sun sets with the scroll and the sky warms into dusk. The title sinks behind the mountains, then body cards rise over the forest and cover the scene.
[How to use it] Scroll up and down inside the card

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
<!-- Lucian UX/UI Prompt #309 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#309 -->
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
.u309{position:relative;width:300px;height:500px;border-radius:30px;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u309-sc{position:absolute;inset:0;overflow-y:auto;scrollbar-width:none;outline:none}
.u309-sc::-webkit-scrollbar{display:none}
.u309-scene{position:sticky;top:0;height:500px;overflow:hidden;background:linear-gradient(var(--s1,#7EC4F2),var(--s2,#D7EEFF))}
.u309-sun{position:absolute;left:50%;top:0;width:70px;height:70px;margin-left:-35px;border-radius:50%;background:radial-gradient(circle,#FFF4C2,#FFC94D 60%);box-shadow:0 0 60px 20px rgba(255,200,80,.45)}
.u309-ly{position:absolute;left:-10%;width:120%;bottom:0;will-change:transform}
.u309-ly svg{display:block;width:100%;height:auto}
.u309-t{position:absolute;left:0;right:0;top:120px;text-align:center;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.25);will-change:transform}
.u309-t b{display:block;font-size:30px;font-weight:880;letter-spacing:-.04em}
.u309-t span{font-size:12.5px;font-weight:700;opacity:.9}
.u309-body{position:relative;margin-top:-90px;padding:0 14px 20px;display:grid;gap:12px}
.u309-c{padding:16px;border-radius:20px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 18px 30px -18px var(--ux-shadow-strong);color:var(--ux-ink)}
.u309-c b{font-size:15px;font-weight:850}
.u309-c p{margin:6px 0 0;font-size:13.5px;line-height:1.6;color:var(--ux-ink-2)}
</style>
<div class="ux u309">
  <div class="u309-sc" tabindex="0" aria-label="Travelogue, scroll to read">
    <div class="u309-scene" aria-hidden="true">
      <span class="u309-sun"></span>
      <div class="u309-t"><b>Three days up high</b><span>Seorak ridge walk · Autumn 2026</span></div>
      <div class="u309-ly" data-s="0.12"><svg viewBox="0 0 360 200"><path d="M0 120 L50 70 L95 110 L150 40 L210 100 L260 60 L320 105 L360 80 V200 H0z" fill="#9DB4D6"/></svg></div>
      <div class="u309-ly" data-s="0.28"><svg viewBox="0 0 360 200"><path d="M0 150 L60 95 L120 140 L175 80 L235 135 L290 100 L360 140 V200 H0z" fill="#6E86B5"/></svg></div>
      <div class="u309-ly" data-s="0.5"><svg viewBox="0 0 360 200"><path d="M0 170 L45 130 L90 160 L140 120 L200 165 L250 128 L310 160 L360 135 V200 H0z" fill="#3F5A8A"/></svg></div>
      <div class="u309-ly" data-s="0.8"><svg viewBox="0 0 360 120"><path d="M0 70 q10-30 20 0 q10-36 22 0 q10-28 20 0 q12-40 24 0 q10-30 20 0 q12-34 22 0 q10-30 20 0 q12-40 24 0 q10-30 20 0 q12-34 22 0 q10-30 20 0 q12-38 24 0 q10-30 20 0 q12-34 22 0 q10-30 20 0 q8-26 20 0 V120 H0z" fill="#1F3B37"/></svg></div>
    </div>
    <div class="u309-body">
      <div class="u309-c"><b>Day one</b><p>At 4 a.m. we climbed the first slope by headlamp alone. As the sun came up, the ridges revealed themselves one layer at a time.</p></div>
      <div class="u309-c"><b>Day two</b><p>We ate warm noodles at the shelter while clouds drifted beneath our feet. The wind was so strong I had to grab my hat twice.</p></div>
      <div class="u309-c"><b>Day three</b><p>The way down was longer than expected, but looking back, the ridges seemed much closer than at the start.</p></div>
    </div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u309-sc'), scene = root.querySelector('.u309-scene'), sun = root.querySelector('.u309-sun'), title = root.querySelector('.u309-t');
  var layers = Array.prototype.slice.call(root.querySelectorAll('.u309-ly'));
  var raf = 0;
  function mix(a, b, t) { return 'rgb(' + a.map(function (v, i) { return Math.round(v + (b[i] - v) * t); }).join(',') + ')'; }
  function draw() {
    raf = 0;
    var y = sc.scrollTop, p = Math.min(1, y / 420);
    layers.forEach(function (l) { l.style.transform = 'translateY(' + (y * (1 - +l.dataset.s) * -0.35 + p * 40 * (+l.dataset.s)).toFixed(1) + 'px)'; });
    sun.style.transform = 'translateY(' + (60 + p * 230).toFixed(1) + 'px) scale(' + (1 + p * 0.25).toFixed(2) + ')';
    title.style.transform = 'translateY(' + (p * 150).toFixed(1) + 'px)';
    title.style.opacity = (1 - p * 1.1).toFixed(2);
    scene.style.setProperty('--s1', mix([126, 196, 242], [70, 60, 130], p));
    scene.style.setProperty('--s2', mix([215, 238, 255], [255, 160, 110], p));
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  draw();
})();
</script>
--- Code end ---
