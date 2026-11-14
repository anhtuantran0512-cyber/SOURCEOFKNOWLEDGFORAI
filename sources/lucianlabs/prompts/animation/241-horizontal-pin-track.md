---
source: "lucianlabs"
id: "241"
title: "Vertical scroll, horizontal track"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#241"
tags: ["scroll", "horizontal", "pin", "sticky", "story"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Vertical scroll, horizontal track (241, Scroll Motion)
[What it does] While you scroll vertically, the view stays pinned and the strip of panels inside flows sideways. The big numbers and shapes in each panel trail slightly behind the strip for a layered feel, and the progress bar and step dots below move along.
[How to use it] Scroll down inside the card. After the last panel it flows vertically again

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
<!-- Lucian UX/UI Prompt #241 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#241 -->
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
.u241{position:relative;width:340px;height:330px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u241-sc{position:absolute;inset:0;overflow-y:auto;scrollbar-width:none;outline:none}
.u241-sc::-webkit-scrollbar{display:none}
.u241-pin{position:sticky;top:0;height:330px;overflow:hidden;display:flex;flex-direction:column;padding:22px 0 20px;box-sizing:border-box}
.u241-k{margin:0 22px;font-size:14px;font-weight:850;letter-spacing:-.02em;color:var(--ux-ink)}

.u241-vp{margin:14px 16px 0;border-radius:22px;overflow:hidden}
.u241-tr{display:flex;gap:10px;will-change:transform}
.u241-p{position:relative;flex:none;width:252px;height:206px;padding:20px;border-radius:22px;overflow:hidden;color:#fff;box-sizing:border-box}
.u241-n{position:absolute;right:10px;bottom:-26px;font-size:150px;line-height:1;font-weight:900;letter-spacing:-.06em;opacity:.25;will-change:transform}
.u241-sh{position:absolute;left:20px;bottom:20px;width:64px;height:64px;will-change:transform}
.u241-p b{display:block;font-size:26px;font-weight:880;letter-spacing:-.04em}
.u241-p span{display:block;margin-top:4px;font-size:13.5px;font-weight:650;opacity:.88}
.u241-ft{display:flex;align-items:center;gap:10px;margin:auto 22px 0}
.u241-bar{flex:1;height:4px;border-radius:4px;background:var(--ux-line-2);overflow:hidden}
.u241-bar i{display:block;height:100%;background:var(--ux-ink);transform-origin:0 50%;transform:scaleX(0)}
.u241-dots{display:flex;gap:5px}
.u241-dots i{width:7px;height:7px;border-radius:50%;background:var(--ux-line-2);transition:background-color .3s,transform .4s var(--ux-spring)}
.u241-dots i.on{background:var(--ux-ink);transform:scale(1.3)}
.u241-after{height:120px;display:flex;align-items:center;justify-content:center;gap:8px;font-size:14px;font-weight:800;color:var(--ux-ink-3)}
.u241-after::before{content:"";width:18px;height:18px;border-radius:50%;background:var(--ux-surface-2) url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 18 18%27%3E%3Cpath d=%27M5 9.3l2.6 2.6L13 6.6%27 fill=%27none%27 stroke=%27%2310B981%27 stroke-width=%272%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27/%3E%3C/svg%3E") center/100% no-repeat;box-shadow:inset 0 0 0 1px var(--ux-line)}
</style>
<div class="ux u241">
  <div class="u241-sc" tabindex="0" aria-label="Stages, scroll to move along">
    <div class="u241-run">
      <div class="u241-pin">
        <p class="u241-k">Four stages of an idea</p>
        <div class="u241-vp"><div class="u241-tr"></div></div>
        <div class="u241-ft"><div class="u241-bar" aria-hidden="true"><i></i></div><div class="u241-dots" aria-hidden="true"></div></div>
      </div>
    </div>
    <div class="u241-after">That’s all four</div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u241-sc'), run = root.querySelector('.u241-run'), vp = root.querySelector('.u241-vp'), tr = root.querySelector('.u241-tr'), bar = root.querySelector('.u241-bar i'), dots = root.querySelector('.u241-dots');
  var PANELS = [['Seed', 'Write down a small idea'], ['Sprout', 'Shape it so others can see'], ['Stem', 'Build it piece by piece'], ['Fruit', 'Put it in people’s hands']];
  var BG = ['#845EF7', '#20C997', '#FF922B', '#F03E3E'];
  var SH = ['<circle cx="32" cy="32" r="14" fill="#fff"/>', '<path d="M32 56V30M32 34c-10 0-16-8-16-16 10 0 16 6 16 16zM32 30c8 0 14-6 14-14-8 0-14 6-14 14z" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>', '<path d="M32 60V8M32 26l-14-10M32 40l14-12" stroke="#fff" stroke-width="5" stroke-linecap="round" fill="none"/>', '<circle cx="24" cy="38" r="14" fill="#fff"/><circle cx="42" cy="28" r="11" fill="#fff" opacity=".7"/>'];
  var panels = PANELS.map(function (p, i) {
    var el = document.createElement('section');
    el.className = 'u241-p'; el.style.background = BG[i];
    el.innerHTML = '<span class="u241-n" aria-hidden="true">0' + (i + 1) + '</span><b></b><span></span><svg class="u241-sh" viewBox="0 0 64 64" aria-hidden="true">' + SH[i] + '</svg>';
    el.querySelector('b').textContent = p[0];
    el.querySelector('span:not(.u241-n)').textContent = p[1];
    tr.appendChild(el);
    dots.appendChild(document.createElement('i'));
    return el;
  });
  var dist = 0, raf = 0;
  function measure() {
    dist = Math.max(0, tr.scrollWidth - vp.clientWidth);
    run.style.height = (330 + dist) + 'px';
  }
  function draw() {
    raf = 0;
    var y = Math.min(dist, sc.scrollTop), p = dist ? y / dist : 0;
    tr.style.transform = 'translateX(' + (-y).toFixed(1) + 'px)';
    panels.forEach(function (el, i) {
      var c = el.offsetLeft - y, f = c / 262;
      el.querySelector('.u241-n').style.transform = 'translateX(' + (f * 26).toFixed(1) + 'px)';
      el.querySelector('.u241-sh').style.transform = 'translateX(' + (f * -18).toFixed(1) + 'px) rotate(' + (f * -14).toFixed(1) + 'deg)';
    });
    bar.style.transform = 'scaleX(' + p.toFixed(3) + ')';
    var cur = Math.round(p * (panels.length - 1));
    Array.prototype.forEach.call(dots.children, function (d, i) { d.classList.toggle('on', i === cur); });
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  measure(); draw();
})();
</script>
--- Code end ---
