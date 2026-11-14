---
source: "lucianlabs"
id: "343"
title: "Rocket back-to-top button"
category: "Navigation"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#343"
tags: ["scroll", "back-to-top", "progress", "button", "rocket"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Rocket back-to-top button (343, Navigation)
[What it does] Scroll far enough down and a round button floats up at the bottom right, its ring filling with how much you have read. Press it and the arrow inside becomes a rocket that blasts off with a flame, while the article glides smoothly back to the top.
[How to use it] Scroll the article down, then press the button at the bottom right

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
<!-- Lucian UX/UI Prompt #343 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#343 -->
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
.u343{position:relative;width:340px;height:340px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u343-sc{position:absolute;inset:0;overflow-y:auto;padding:22px 22px 60px;scrollbar-width:none;outline:none}
.u343-sc::-webkit-scrollbar{display:none}
.u343-sc h3{margin:0;font-size:22px;font-weight:880;letter-spacing:-.04em}
.u343-sc small{display:block;margin:4px 0 14px;font-size:12px;font-weight:700;color:var(--ux-ink-3)}
.u343-sc p{margin:0 0 14px;font-size:14.5px;line-height:1.75;color:var(--ux-ink-2)}
.u343-sc i{display:block;height:110px;margin:0 0 14px;border-radius:16px;background:linear-gradient(135deg,#FFE3E3,#E5DBFF)}
.u343-up{position:absolute;right:16px;bottom:16px;width:52px;height:52px;border:0;padding:0;border-radius:50%;background:var(--ux-ink);color:var(--ux-page);box-shadow:0 12px 24px -10px var(--ux-shadow-strong);opacity:0;transform:translateY(20px) scale(.6);pointer-events:none;transition:opacity .3s,transform .5s var(--ux-spring)}
.u343.show .u343-up{opacity:1;transform:none;pointer-events:auto}
.u343-up svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.u343-ring{fill:none;stroke:var(--ux-accent);stroke-width:3;stroke-linecap:round;transform:rotate(-90deg);transform-origin:26px 26px}
.u343-ar{fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;transition:opacity .2s}
.u343-rk{opacity:0}
.u343-rk .b{fill:currentColor}
.u343-rk .w{fill:var(--ux-accent)}
.u343-rk .f{fill:#FF922B;transform-box:fill-box;transform-origin:50% 0}
.u343.fly .u343-ar{opacity:0}
.u343.fly .u343-rk{opacity:1}
.u343.fly .u343-rk .f{animation:u343-fl .12s linear infinite alternate}
@keyframes u343-fl{to{transform:scaleY(1.6)}}
</style>
<div class="ux u343">
  <article class="u343-sc" tabindex="0" aria-label="Article, scroll to read"><h3>How small habits add up</h3><small>4 min read</small></article>
  <button class="u343-up" type="button" aria-label="Back to top">
    <svg viewBox="0 0 52 52" aria-hidden="true"><circle class="u343-ring" cx="26" cy="26" r="24"/><path class="u343-ar" d="M26 34V18M19 25l7-7 7 7"/><g class="u343-rk"><path class="f" d="M23 33h6l-3 7z"/><path class="b" d="M26 13c4 3 5 9 4 16h-8c-1-7 0-13 4-16z"/><circle class="w" cx="26" cy="22" r="2.2"/><path class="b" d="M22 26l-3 6h4zM30 26l3 6h-4z"/></g></svg>
  </button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u343-sc'), up = root.querySelector('.u343-up'), ring = root.querySelector('.u343-ring'), rk = root.querySelector('.u343-rk');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var P = ['Pick one tiny thing to do at the same time every day. A glass of water, one page of a book, a single stretch is enough.', 'For the first week, focus only on not skipping it rather than on results. Once you keep a log, you will hate leaving a gap.', 'In the second week, grow it just a little. One page becomes two, one glass becomes two.', 'After a month, your body remembers the habit before your willpower does. That is the time to add one more.', 'What matters is not starting big. Start small and it lasts.'];
  P.forEach(function (t, i) { var p = document.createElement('p'); p.textContent = t; sc.appendChild(p); if (i === 1) { var im = document.createElement('i'); im.setAttribute('aria-hidden', 'true'); sc.appendChild(im); } });
  var C = 2 * Math.PI * 24, raf = 0, flying = false;
  ring.style.strokeDasharray = C;
  function draw() {
    raf = 0;
    var max = sc.scrollHeight - sc.clientHeight, p = max ? sc.scrollTop / max : 0;
    ring.style.strokeDashoffset = (C * (1 - p)).toFixed(1);
    if (!flying) root.classList.toggle('show', sc.scrollTop > 120);
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  up.addEventListener('click', function () {
    if (flying) return;
    flying = true;
    root.classList.add('fly');
    var from = sc.scrollTop, t0 = performance.now(), D = rm ? 1 : 900;
    if (!rm && rk.animate) rk.animate([{ transform: 'none' }, { transform: 'translateY(4px)', offset: 0.15 }, { transform: 'translateY(-260px)' }], { duration: 900, easing: 'cubic-bezier(.6,0,.8,.4)' });
    (function f(now) {
      if (!root.isConnected) return;
      var k = Math.min(1, Math.max(0, (now - t0) / D)), e = k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
      sc.scrollTop = from * (1 - e);
      if (k < 1) { requestAnimationFrame(f); return; }
      setTimeout(function () { flying = false; root.classList.remove('fly'); draw(); }, 200);
    })(t0);
  });
  draw();
})();
</script>
--- Code end ---
