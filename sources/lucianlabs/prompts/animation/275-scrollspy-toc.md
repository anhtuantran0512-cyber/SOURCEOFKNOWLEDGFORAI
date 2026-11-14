---
source: "lucianlabs"
id: "275"
title: "Scroll-following table of contents"
category: "Navigation"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#275"
tags: ["scroll", "toc", "scrollspy", "navigation", "docs"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Scroll-following table of contents (275, Navigation)
[What it does] Scroll the body and the chapter you are reading darkens in the table of contents on the right, while a vertical marker grows and shrinks to cover however much of that chapter is on screen. When two chapters are visible the marker spans both, and pressing an entry scrolls smoothly to that chapter.
[How to use it] Scroll the body on the left, or press an entry in the contents on the right

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
<!-- Lucian UX/UI Prompt #275 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#275 -->
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
.u275{position:relative;width:340px;height:330px;display:flex;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u275-sc{position:relative;flex:1;overflow-y:auto;padding:14px 12px 120px 18px;scrollbar-width:none;outline:none}
.u275-sc::-webkit-scrollbar{display:none}
.u275-sec{padding:8px 0 14px}
.u275-sec h4{margin:0;font-size:16px;font-weight:850;letter-spacing:-.02em}
.u275-sec p{margin:6px 0 0;font-size:13px;line-height:1.65;color:var(--ux-ink-2)}
.u275-sec i{display:block;height:60px;margin-top:8px;border-radius:10px;background:repeating-linear-gradient(90deg,var(--ux-surface-2) 0 46%,transparent 46% 50%)}
.u275-toc{position:relative;flex:none;width:118px;padding:16px 12px 16px 16px;border-left:1px solid var(--ux-line)}
.u275-toc p{margin:0 0 8px;font-size:11px;font-weight:750;color:var(--ux-ink-3)}
.u275-ul{position:relative;margin:0;padding:0 0 0 10px;list-style:none}
.u275-ul::before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;border-radius:2px;background:var(--ux-line)}
.u275-ti{display:block;width:100%;padding:6px 0;border:0;background:none;text-align:left;font-size:12.5px;font-weight:650;color:var(--ux-ink-3);transition:color .25s}
.u275-ti.on{color:var(--ux-ink);font-weight:800}
.u275-mk{position:absolute;left:0;top:0;width:2px;border-radius:2px;background:var(--ux-accent);transition:transform .35s var(--ux-spring),height .35s var(--ux-spring)}
</style>
<div class="ux u275">
  <div class="u275-sc" tabindex="0" aria-label="Document body"></div>
  <nav class="u275-toc" aria-label="Contents"><p>On this page</p><ul class="u275-ul"><span class="u275-mk" aria-hidden="true"></span></ul></nav>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u275-sc'), ul = root.querySelector('.u275-ul'), mk = root.querySelector('.u275-mk');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SEC = [['Getting started', 'Installing takes a single line. Run the command and the files you need are added to your project along with a default config.'], ['Theming', 'It uses two sets of color tokens, light and dark. Map them to your project’s variables and they follow along.'], ['Components', 'Common pieces like buttons, inputs and menus are collected here. Take only the ones you need.'], ['Accessibility', 'Every element works with the keyboard and carries names for screen readers.'], ['Deploying', 'The build output is static files. Upload them to any host as they are.']];
  var secs = [], items = [];
  SEC.forEach(function (s, i) {
    var el = document.createElement('section');
    el.className = 'u275-sec';
    el.innerHTML = '<h4></h4><p></p>' + (i % 2 ? '' : '<i aria-hidden="true"></i>');
    el.querySelector('h4').textContent = s[0];
    el.querySelector('p').textContent = s[1];
    sc.appendChild(el); secs.push(el);
    var li = document.createElement('li'), b = document.createElement('button');
    b.type = 'button'; b.className = 'u275-ti'; b.textContent = s[0];
    b.addEventListener('click', function () { sc.scrollTo({ top: el.offsetTop - 6, behavior: rm ? 'auto' : 'smooth' }); });
    li.appendChild(b); ul.appendChild(li); items.push(b);
  });
  var raf = 0;
  function draw() {
    raf = 0;
    var top = sc.scrollTop, bot = top + sc.clientHeight, first = -1, last = -1, best = -1, bestV = 0;
    secs.forEach(function (s, i) {
      var a = s.offsetTop, b = a + s.offsetHeight, vis = Math.max(0, Math.min(b, bot) - Math.max(a, top)) / s.offsetHeight;
      if (vis > 0.12) { if (first < 0) first = i; last = i; }
      if (vis > bestV) { bestV = vis; best = i; }
    });
    if (first < 0) first = last = Math.max(0, best);
    items.forEach(function (b, i) { b.classList.toggle('on', i === best); if (i === best) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current'); });
    var y0 = items[first].parentNode.offsetTop, y1 = items[last].parentNode.offsetTop + items[last].parentNode.offsetHeight;
    mk.style.transform = 'translateY(' + y0 + 'px)';
    mk.style.height = (y1 - y0) + 'px';
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  requestAnimationFrame(draw);
})();
</script>
--- Code end ---
