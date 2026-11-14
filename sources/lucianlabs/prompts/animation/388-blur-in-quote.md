---
source: "lucianlabs"
id: "388"
title: "Word-by-word focus quote"
category: "Text Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#388"
tags: ["text", "quote", "blur", "testimonial", "stagger"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Word-by-word focus quote (388, Text Motion)
[What it does] The words of a quote float out of focus, then come into focus one after another as they settle into place. Move on and the current words blur away as if scattering, while the speaker’s name slides up from below. A bar at the bottom shows when it will move on by itself.
[How to use it] Use the arrows or dots to change quotes. Hovering pauses the rotation

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
<!-- Lucian UX/UI Prompt #388 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#388 -->
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
.u388{position:relative;width:340px;height:330px;display:flex;flex-direction:column;padding:22px 22px 16px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u388-qm{position:absolute;right:16px;top:-6px;font:900 120px/1 Georgia,serif;color:var(--ux-accent-soft);pointer-events:none}
.u388-st{position:relative;flex:1}
.u388-q{position:absolute;left:0;right:0;top:4px;margin:0;font-size:22px;line-height:1.42;font-weight:780;letter-spacing:-.035em;color:var(--ux-ink)}
.u388-w{display:inline-block;filter:blur(10px);opacity:0;transform:translateY(-10px) scale(1.12);transition:filter .7s var(--ux-ease),opacity .6s var(--ux-ease),transform .9s var(--ux-spring);transition-delay:calc(var(--i) * 55ms)}
.u388-q.in .u388-w{filter:none;opacity:1;transform:none}
.u388-q.out .u388-w{filter:blur(8px);opacity:0;transform:translate(var(--dx),8px) scale(.92);transition-duration:.45s;transition-delay:calc(var(--r) * 1ms)}
.u388-by{position:absolute;left:0;bottom:0;display:flex;align-items:center;gap:10px;overflow:hidden;height:44px}
.u388-by>div{transition:transform .6s var(--ux-spring),opacity .4s}
.u388-by.swap>div{transform:translateY(100%);opacity:0;transition:none}
.u388-av{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--a1),var(--a2))}
.u388-by b{display:block;font-size:14px;font-weight:800}
.u388-role{font-size:12px;font-weight:650;color:var(--ux-ink-3)}
.u388-ft{display:flex;align-items:center;gap:8px;margin-top:14px}
.u388-dots{display:flex;gap:2px;flex:1}
.u388-dot{position:relative;flex:1;height:22px;border:0;background:none;padding:0}
.u388-dot::before{content:"";position:absolute;left:0;right:0;top:9px;height:4px;border-radius:4px;background:var(--ux-line-2)}
.u388-dot i{position:absolute;left:0;top:9px;height:4px;width:100%;border-radius:4px;background:var(--ux-ink);transform-origin:0 50%;transform:scaleX(0)}
.u388-dot.past i{transform:scaleX(1)}
.u388-pv,.u388-nx{width:36px;height:36px;border:0;border-radius:50%;display:grid;place-items:center;background:var(--ux-surface-2);color:var(--ux-ink);transition:transform .35s var(--ux-spring)}
.u388-pv:active,.u388-nx:active{transform:scale(.9)}
.u388-ft svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
</style>
<div class="ux u388">
  <span class="u388-qm" aria-hidden="true">&ldquo;</span>
  <div class="u388-st"><blockquote class="u388-q in" aria-live="polite"></blockquote><div class="u388-by"></div></div>
  <div class="u388-ft">
    <div class="u388-dots" role="group" aria-label="Pick a quote"></div>
    <button class="u388-pv" type="button" aria-label="Previous quote"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg></button>
    <button class="u388-nx" type="button" aria-label="Next quote"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></button>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var st = root.querySelector('.u388-st'), by = root.querySelector('.u388-by'), dotsEl = root.querySelector('.u388-dots');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var Q = [['Simplicity is not taking things away but keeping only what matters.', 'Harin Kim', 'Product designer'], ['The time a user waits is part of the design too.', 'Doyun Park', 'Interaction designer'], ['Good motion goes unnoticed and helps you understand.', 'Seojun Lee', 'Motion designer']];
  var AV = [['#FF8A5B', '#B49CFF'], ['#38D9A9', '#3D8BFF'], ['#FFD166', '#FF6B9D']];
  var cur = -1, timer = 0, anim = null, hold = false, DUR = 5200;
  var dots = Q.map(function (q, i) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'u388-dot'; b.setAttribute('aria-label', (i + 1) + ' of 3');
    b.innerHTML = '<i></i>';
    b.addEventListener('click', function () { show(i); });
    dotsEl.appendChild(b);
    return b;
  });
  function build(i) {
    var q = document.createElement('blockquote');
    q.className = 'u388-q';
    q.setAttribute('aria-live', 'polite');
    Q[i][0].split(' ').forEach(function (w, k) {
      if (k) q.appendChild(document.createTextNode(' '));
      var s = document.createElement('span');
      s.className = 'u388-w'; s.textContent = w;
      s.style.setProperty('--i', k);
      s.style.setProperty('--r', Math.round(Math.random() * 160));
      s.style.setProperty('--dx', ((Math.random() - 0.5) * 16).toFixed(1) + 'px');
      q.appendChild(s);
    });
    return q;
  }
  function show(i) {
    if (i === cur) return;
    var old = st.querySelector('.u388-q:not(.out)');
    if (old) { old.classList.remove('in'); old.classList.add('out'); old.removeAttribute('aria-live'); setTimeout(function () { old.remove(); }, 700); }
    cur = i;
    var q = build(i);
    st.insertBefore(q, by);
    setTimeout(function () { if (root.isConnected) q.classList.add('in'); }, old && !rm ? 260 : 20);
    by.classList.add('swap');
    by.innerHTML = '<div><i class="u388-av" style="--a1:' + AV[i][0] + ';--a2:' + AV[i][1] + ';display:block"></i></div><div><b class="u388-nm"></b><span class="u388-role"></span></div>';
    by.querySelector('.u388-nm').textContent = Q[i][1];
    by.querySelector('.u388-role').textContent = Q[i][2];
    void by.offsetWidth;
    setTimeout(function () { by.classList.remove('swap'); }, 360);
    dots.forEach(function (d, k) { d.classList.toggle('past', k < i); d.setAttribute('aria-current', String(k === i)); });
    run();
  }
  function run() {
    clearTimeout(timer);
    if (anim) anim.cancel();
    var bar = dots[cur].querySelector('i');
    if (rm || !bar.animate) return;
    anim = bar.animate([{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }], { duration: DUR, fill: 'forwards' });
    if (hold) anim.pause();
    anim.onfinish = function () { if (root.isConnected) show((cur + 1) % Q.length); };
  }
  root.querySelector('.u388-nx').addEventListener('click', function () { show((cur + 1) % Q.length); });
  root.querySelector('.u388-pv').addEventListener('click', function () { show((cur + Q.length - 1) % Q.length); });
  st.addEventListener('pointerenter', function () { hold = true; if (anim) anim.pause(); });
  st.addEventListener('pointerleave', function () { hold = false; if (anim) anim.play(); });
  st.querySelector('.u388-q').remove();
  show(0);
})();
</script>
--- Code end ---
