---
source: "lucianlabs"
id: "338"
title: "Rolling word cube"
category: "Text Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#338"
tags: ["text", "3d", "cube", "rotate", "hero"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Rolling word cube (338, Text Motion)
[What it does] The key word sits on one face of a 3D box, and each change rolls the box downward to show the next face. As it rolls, the top face darkens and the front brightens, and the caption below turns over too. A progress bar fills while it advances on its own, and hovering pauses it.
[How to use it] Roll it up or down with the arrows, or press a dot below to jump to that word

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
<!-- Lucian UX/UI Prompt #338 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#338 -->
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
.u338{position:relative;width:340px;height:282px;display:flex;flex-direction:column;padding:22px 20px 18px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u338-k{margin:0;font-size:12px;font-weight:750;color:var(--ux-ink-3)}
.u338-main{display:flex;align-items:center;gap:12px;margin-top:22px}
.u338-sc{flex:1;height:72px;perspective:520px}
.u338-cube{position:relative;width:100%;height:72px;transform-style:preserve-3d;transform:translateZ(-36px) rotateX(var(--r,0deg));transition:transform .9s cubic-bezier(.5,-.25,.3,1.3)}
.u338-f{position:absolute;inset:0;display:flex;align-items:center;padding:0 18px;border-radius:16px;background:var(--ux-ink);color:var(--ux-page);font-size:42px;font-weight:880;letter-spacing:-.05em;backface-visibility:hidden;transition:filter .9s}
.u338-f:nth-child(1){transform:rotateX(0deg) translateZ(36px)}
.u338-f:nth-child(2){transform:rotateX(-90deg) translateZ(36px);background:var(--ux-accent);color:var(--ux-accent-ink)}
.u338-f:nth-child(3){transform:rotateX(-180deg) translateZ(36px)}
.u338-f:nth-child(4){transform:rotateX(-270deg) translateZ(36px);background:var(--ux-accent);color:var(--ux-accent-ink)}
.u338-f:not(.on){filter:brightness(.55)}
.u338-ar{display:flex;flex-direction:column;gap:6px}
.u338-up,.u338-dn{width:36px;height:33px;border:0;border-radius:11px;display:grid;place-items:center;background:var(--ux-surface-2);color:var(--ux-ink);transition:transform .35s var(--ux-spring)}
.u338-up:active,.u338-dn:active{transform:scale(.9)}
.u338-ar svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.u338-d{position:relative;height:48px;margin:18px 0 0;overflow:hidden;font-size:16px;line-height:1.5;font-weight:650;color:var(--ux-ink-2)}
.u338-d span{position:absolute;left:0;right:0;top:0;transition:transform .7s var(--ux-spring),opacity .4s}
.u338-d span.out{transform:translateY(-100%);opacity:0}
.u338-d span.in{transform:translateY(100%);opacity:0}
.u338-ft{margin-top:auto;display:flex;align-items:center;gap:10px}
.u338-dots{display:flex;gap:6px}
.u338-dot{width:26px;height:26px;border:0;border-radius:50%;background:transparent;display:grid;place-items:center}
.u338-dot::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--ux-line-2);transition:background-color .3s,transform .4s var(--ux-spring)}
.u338-dot[aria-pressed="true"]::before{background:var(--ux-ink);transform:scale(1.3)}
.u338-bar{flex:1;height:3px;border-radius:3px;background:var(--ux-line);overflow:hidden}
.u338-bar i{display:block;height:100%;width:100%;background:var(--ux-accent);transform-origin:0 50%;transform:scaleX(0)}
</style>
<div class="ux u338">
  <p class="u338-k">What we do</p>
  <div class="u338-main">
    <div class="u338-sc"><div class="u338-cube" aria-live="polite"></div></div>
    <div class="u338-ar">
      <button class="u338-up" type="button" aria-label="Previous word"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 15l6-6 6 6"/></svg></button>
      <button class="u338-dn" type="button" aria-label="Next word"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
    </div>
  </div>
  <p class="u338-d"></p>
  <div class="u338-ft"><div class="u338-dots" role="group" aria-label="Pick a word"></div><div class="u338-bar" aria-hidden="true"><i></i></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var cube = root.querySelector('.u338-cube'), desc = root.querySelector('.u338-d'), dotsEl = root.querySelector('.u338-dots'), bar = root.querySelector('.u338-bar i');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var WORDS = ['Plan', 'Design', 'Build', 'Run'];
  var DESC = ['We break the problem down and set the order', 'We draw screens you want to touch', 'We build it fast and solid', 'We stay with you after launch'];
  var faces = WORDS.map(function (w) { var f = document.createElement('span'); f.className = 'u338-f'; f.textContent = w; cube.appendChild(f); return f; });
  var dots = WORDS.map(function (w, i) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'u338-dot'; b.setAttribute('aria-label', w); b.setAttribute('aria-pressed', 'false');
    b.addEventListener('click', function () { go(i - idx); });
    dotsEl.appendChild(b);
    return b;
  });
  var idx = 0, turns = 0, hold = false, timer = 0, anim = null;
  function go(step) {
    if (!step) return;
    idx = (idx + step + 4 * 10) % 4;
    turns += step;
    cube.style.setProperty('--r', (turns * 90) + 'deg');
    faces.forEach(function (f, k) { f.classList.toggle('on', k === idx); f.setAttribute('aria-hidden', String(k !== idx)); });
    dots.forEach(function (d, k) { d.setAttribute('aria-pressed', String(k === idx)); });
    var old = desc.querySelector('span:not(.out)'), n = document.createElement('span');
    n.textContent = DESC[idx]; n.className = 'in';
    desc.appendChild(n);
    if (old) { old.className = 'out'; setTimeout(function () { old.remove(); }, 700); }
    requestAnimationFrame(function () { requestAnimationFrame(function () { n.className = ''; }); });
    restart();
  }
  function restart() {
    clearTimeout(timer);
    if (anim) anim.cancel();
    if (rm || !bar.animate) return;
    anim = bar.animate([{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }], { duration: 2600, easing: 'linear', fill: 'forwards' });
    if (hold) anim.pause();
    timer = setTimeout(function tick() { if (!root.isConnected) return; if (hold) { timer = setTimeout(tick, 300); return; } go(1); }, 2600);
  }
  root.querySelector('.u338-up').addEventListener('click', function () { go(-1); });
  root.querySelector('.u338-dn').addEventListener('click', function () { go(1); });
  cube.addEventListener('pointerenter', function () { hold = true; if (anim) anim.pause(); });
  cube.addEventListener('pointerleave', function () { hold = false; if (anim) anim.play(); });
  faces[0].classList.add('on');
  dots[0].setAttribute('aria-pressed', 'true');
  var first = document.createElement('span'); first.textContent = DESC[0]; desc.appendChild(first);
  faces.forEach(function (f, k) { if (k) f.setAttribute('aria-hidden', 'true'); });
  restart();
})();
</script>
--- Code end ---
