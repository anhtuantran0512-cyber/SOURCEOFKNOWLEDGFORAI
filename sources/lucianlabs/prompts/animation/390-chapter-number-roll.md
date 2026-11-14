---
source: "lucianlabs"
id: "390"
title: "Rolling chapter numbers"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#390"
tags: ["scroll", "chapter", "counter", "progress", "reading"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Rolling chapter numbers (390, Scroll Motion)
[What it does] Scroll the text and the big chapter number on the left rolls continuously like a strip of digits to point at the next chapter, while the ring gauge below fills with how much of the current chapter you have read. The chapter title beneath the number slides up as it changes.
[How to use it] Scroll the text on the right up and down

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
<!-- Lucian UX/UI Prompt #390 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#390 -->
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
.u390{position:relative;width:340px;height:330px;display:flex;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u390-side{flex:none;width:118px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;border-right:1px solid var(--ux-line);background:var(--ux-surface-2)}
.u390-lb{font:800 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.14em;color:var(--ux-ink-3)}
.u390-num{position:relative;width:96px;height:78px;overflow:hidden;-webkit-mask-image:linear-gradient(transparent,#000 22%,#000 78%,transparent);mask-image:linear-gradient(transparent,#000 22%,#000 78%,transparent)}
.u390-strip{position:absolute;left:0;right:0;top:0;will-change:transform}
.u390-strip span{display:block;height:78px;font:900 70px/78px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:-.06em;text-align:center;color:var(--ux-ink)}
.u390-g{width:40px;height:40px;margin-top:4px}
.u390-g circle{fill:none;stroke-width:4}
.u390-g .t{stroke:var(--ux-line-2)}
.u390-g .v{stroke:var(--ux-accent);stroke-linecap:round;transform:rotate(-90deg);transform-origin:20px 20px}
.u390-tt{position:relative;width:100%;height:20px;overflow:hidden;text-align:center}
.u390-tt span{position:absolute;left:0;right:0;font-size:13px;font-weight:800;transition:transform .45s var(--ux-spring),opacity .3s}
.u390-tt span.out{transform:translateY(-100%);opacity:0}
.u390-tt span.in{transform:translateY(100%);opacity:0}
.u390-sc{flex:1;overflow-y:auto;padding:16px 16px 140px;scrollbar-width:none;outline:none}
.u390-sc::-webkit-scrollbar{display:none}
.u390-sec{padding:6px 0 30px}
.u390-sec b{display:block;font-size:16px;font-weight:850}
.u390-sec p{margin:6px 0 0;font-size:13.5px;line-height:1.75;color:var(--ux-ink-2)}
.u390-sec i{display:block;height:70px;margin-top:10px;border-radius:12px;background:var(--ux-surface-2)}
</style>
<div class="ux u390">
  <div class="u390-side" aria-hidden="true">
    <span class="u390-lb">CH</span>
    <div class="u390-num"><div class="u390-strip"></div></div>
    <div class="u390-tt"></div>
    <svg class="u390-g" viewBox="0 0 40 40"><circle class="t" cx="20" cy="20" r="16"/><circle class="v" cx="20" cy="20" r="16"/></svg>
  </div>
  <div class="u390-sc" tabindex="0" aria-label="Text, scroll to read"></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u390-sc'), strip = root.querySelector('.u390-strip'), tt = root.querySelector('.u390-tt'), gv = root.querySelector('.u390-g .v');
  var CH = [['Seed', 'Every story began with a tiny question. Why is this button always so confusing?'], ['Watching', 'We spent a week watching how people really use the screen. Their hands paused in unexpected places.'], ['Trying', 'We built twenty different shapes and tested them one by one. Most failed, but two remained.'], ['Refining', 'We blended the two into one and kept trimming until it needed no explanation.']];
  var secs = CH.map(function (c, i) {
    var s = document.createElement('section');
    s.className = 'u390-sec';
    s.innerHTML = '<b></b><p></p><i aria-hidden="true"></i>';
    s.querySelector('b').textContent = String(i + 1).padStart(2, '0') + ' · ' + c[0];
    s.querySelector('p').textContent = c[1];
    sc.appendChild(s);
    var n = document.createElement('span'); n.textContent = String(i + 1).padStart(2, '0'); strip.appendChild(n);
    return s;
  });
  var C = 2 * Math.PI * 16, cur = -1, raf = 0;
  gv.style.strokeDasharray = C;
  function title(i) {
    var old = tt.querySelector('span:not(.out)'), n = document.createElement('span');
    n.textContent = CH[i][0]; n.className = 'in'; tt.appendChild(n);
    if (old) { old.className = 'out'; setTimeout(function () { old.remove(); }, 450); }
    requestAnimationFrame(function () { requestAnimationFrame(function () { n.className = ''; }); });
  }
  function draw() {
    raf = 0;
    var y = sc.scrollTop + 20, f = 0;
    secs.forEach(function (s, i) { if (y >= s.offsetTop) f = i + Math.min(1, (y - s.offsetTop) / s.offsetHeight); });
    var i = Math.min(CH.length - 1, Math.floor(f)), inCh = f - i;
    var roll = Math.max(0, Math.min(CH.length - 1, i + Math.max(0, inCh - 0.75) / 0.25));
    strip.style.transform = 'translateY(' + (-78 * roll).toFixed(1) + 'px)';
    gv.style.strokeDashoffset = (C * (1 - Math.min(1, inCh))).toFixed(1);
    if (i !== cur) { cur = i; title(i); }
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  draw();
})();
</script>
--- Code end ---
