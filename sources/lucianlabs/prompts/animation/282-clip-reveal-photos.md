---
source: "lucianlabs"
id: "282"
title: "Widening photo reveal"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#282"
tags: ["scroll", "reveal", "clip-path", "gallery", "photo"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Widening photo reveal (282, Scroll Motion)
[What it does] As a photo scrolls into view, a narrow slit in the middle widens to both sides to reveal it, while the image inside scales down slightly so it seems to approach. The caption rises from below just as the slit finishes opening, and scrolling back up closes it again.
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
<!-- Lucian UX/UI Prompt #282 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#282 -->
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
.u282{position:relative;width:300px;height:500px;border-radius:30px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u282-sc{position:absolute;inset:0;overflow-y:auto;padding:22px 16px 80px;scrollbar-width:none;outline:none}
.u282-sc::-webkit-scrollbar{display:none}
.u282-k{margin:0;font-size:24px;font-weight:880;letter-spacing:-.04em}
.u282-s{margin:2px 0 220px;font-size:12.5px;font-weight:700;color:var(--ux-ink-3)}
.u282-ph{margin:0 0 44px}
.u282-fr{position:relative;height:300px;border-radius:20px;overflow:hidden;clip-path:inset(0 calc(var(--c,1) * 46%) 0 calc(var(--c,1) * 46%) round 20px)}
.u282-img{position:absolute;inset:-6%;transform:scale(calc(1 + var(--c,1) * .3))}
.u282-cap{margin-top:10px;opacity:calc(1 - var(--c,1) * 3);transform:translateY(calc(var(--c,1) * 30px))}
.u282-cap b{display:block;font-size:16px;font-weight:850}
.u282-cap span{font-size:12px;font-weight:700;color:var(--ux-ink-3)}
</style>
<div class="ux u282">
  <div class="u282-sc" tabindex="0" aria-label="Photo set, scroll to view">
    <p class="u282-k">A year of scenes</p><p class="u282-s">Four photos</p>
    <div class="u282-list"></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u282-sc'), list = root.querySelector('.u282-list');
  var PH = [['Dawn sea', 'Gangneung · 5:40 AM'], ['Misty forest', 'Odaesan · 7:10 AM'], ['Sunset bridge', 'Seoul · 6:25 PM'], ['Field of falling stars', 'Pyeongchang · 11:50 PM']];
  var ART = [
    'linear-gradient(#FFD8A8 0,#FFC078 30%,#74C0FC 55%,#1C7ED6 100%)',
    'radial-gradient(60% 40% at 50% 30%,rgba(255,255,255,.8),transparent 70%),linear-gradient(#C3D0C8,#5C7F6B 70%,#2B4B3A)',
    'radial-gradient(30% 20% at 70% 45%,#FFE066,transparent 70%),linear-gradient(#5F3DC4,#E8590C 55%,#343A40 56%,#212529)',
    'radial-gradient(1.5px 1.5px at 20% 20%,#fff,transparent),radial-gradient(1.5px 1.5px at 60% 30%,#fff,transparent),radial-gradient(1px 1px at 80% 15%,#fff,transparent),radial-gradient(1px 1px at 40% 40%,#fff,transparent),linear-gradient(#0B1340,#3B2C7A 60%,#1B4332 61%,#081C15)'
  ];
  var items = PH.map(function (p, i) {
    var el = document.createElement('figure');
    el.className = 'u282-ph';
    el.innerHTML = '<div class="u282-fr" role="img"><div class="u282-img"></div></div><figcaption class="u282-cap"><b></b><span></span></figcaption>';
    el.querySelector('.u282-img').style.background = ART[i];
    el.querySelector('.u282-fr').setAttribute('aria-label', p[0]);
    el.querySelector('b').textContent = p[0];
    el.querySelector('span').textContent = p[1];
    list.appendChild(el);
    return el;
  });
  var raf = 0;
  function draw() {
    raf = 0;
    var vh = sc.clientHeight, top = sc.scrollTop;
    items.forEach(function (el) {
      var y = el.offsetTop - top, c = Math.max(0, Math.min(1, (y - vh * 0.42) / (vh * 0.48)));
      el.style.setProperty('--c', c.toFixed(3));
    });
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  draw();
})();
</script>
--- Code end ---
