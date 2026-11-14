---
source: "lucianlabs"
id: "057"
title: "Face-picker testimonial carousel"
category: "Cards & Content"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#057"
tags: ["carousel", "testimonial", "autoplay", "swipe", "avatars"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Face-picker testimonial carousel (057, Cards & Content)
[What it does] Reviews advance every few seconds; in the row of faces below, the current speaker grows and a ring around them fills with the time left. The quote fades in word by word, and you can drag sideways or press a face to jump.
[How to use it] Press a face below or drag the review sideways. Hovering pauses the auto-advance. With a keyboard, use the left and right arrow keys

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
<!-- Lucian UX/UI Prompt #057 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#057 -->
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
.u057{position:relative;width:350px;height:370px;display:flex;flex-direction:column;padding:26px 24px 22px;border-radius:30px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden;outline:none}
.u057:focus-visible{box-shadow:0 0 0 2px var(--ux-accent),0 30px 60px -36px var(--ux-shadow-strong)}
.u057-mark{position:absolute;right:20px;top:-6px;font-size:150px;line-height:1;font-weight:900;font-family:Georgia,serif;background:linear-gradient(160deg,var(--c1,#FFB547),var(--c2,#FF6B8B));-webkit-background-clip:text;background-clip:text;color:transparent;opacity:.22;transition:opacity .4s;pointer-events:none}
.u057-stars{display:flex;gap:3px;color:#FFB547}
.u057-stars svg{width:16px;height:16px;fill:currentColor}
.u057-view{position:relative;flex:1;margin-top:14px;touch-action:pan-y;cursor:grab}
.u057-view.drag{cursor:grabbing}
.u057-q{position:absolute;inset:0;margin:0;font-size:24px;line-height:1.42;font-weight:760;letter-spacing:-.045em;transition:transform .5s var(--ux-ease),opacity .3s}
.u057-q span{display:inline-block;opacity:0;transform:translateY(10px);filter:blur(4px);transition:opacity .45s var(--ux-ease),transform .6s var(--ux-spring),filter .45s;transition-delay:calc(var(--i) * 32ms)}
.u057-q.on span{opacity:1;transform:none;filter:none}
.u057-q.on mark{background:linear-gradient(transparent 62%,color-mix(in srgb,var(--c1,#FFB547) 40%,transparent) 62%);color:inherit}
.u057-q mark{background:none;color:inherit;transition:background .4s .5s}
.u057-who{display:flex;align-items:baseline;gap:8px;margin-bottom:14px;height:22px}
.u057-who b{font-size:15px;font-weight:800;letter-spacing:-.02em}
.u057-who small{font-size:12.5px;font-weight:600;color:var(--ux-ink-3)}
.u057-faces{display:flex;align-items:center;gap:10px}
.u057-f{position:relative;width:40px;height:40px;flex:none;border:0;padding:0;border-radius:50%;background:none;transition:width .5s var(--ux-spring),height .5s var(--ux-spring)}
.u057-f i{position:absolute;inset:4px;border-radius:50%;background:var(--g);filter:grayscale(.7);opacity:.6;transition:filter .4s,opacity .4s,inset .4s}
.u057-f:hover i{opacity:.9}
.u057-f[aria-current="true"]{width:54px;height:54px}
.u057-f[aria-current="true"] i{filter:none;opacity:1;inset:5px}
.u057-f svg{position:absolute;inset:0;width:100%;height:100%;transform:rotate(-90deg);opacity:0;transition:opacity .3s}
.u057-f[aria-current="true"] svg{opacity:1}
.u057-f circle{fill:none;stroke-width:2.5}
.u057-f .tr{stroke:var(--ux-line)}
.u057-f .pr{stroke:var(--ux-accent);stroke-linecap:round;stroke-dasharray:100;stroke-dashoffset:calc(100 - var(--p,0) * 100)}
.u057-f:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u057-n{margin-left:auto;font-size:12.5px;font-weight:700;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
</style>
<div class="ux u057" tabindex="0" role="region" aria-roledescription="carousel" aria-label="Customer reviews">
  <span class="u057-mark" aria-hidden="true">“</span>
  <div class="u057-stars" role="img" aria-label="Rated 5 out of 5"><svg viewBox="0 0 16 16"><path d="M8 1.5l2 4.2 4.5.6-3.3 3.1.8 4.5L8 11.7l-4 2.2.8-4.5L1.5 6.3l4.5-.6z"/></svg><svg viewBox="0 0 16 16"><path d="M8 1.5l2 4.2 4.5.6-3.3 3.1.8 4.5L8 11.7l-4 2.2.8-4.5L1.5 6.3l4.5-.6z"/></svg><svg viewBox="0 0 16 16"><path d="M8 1.5l2 4.2 4.5.6-3.3 3.1.8 4.5L8 11.7l-4 2.2.8-4.5L1.5 6.3l4.5-.6z"/></svg><svg viewBox="0 0 16 16"><path d="M8 1.5l2 4.2 4.5.6-3.3 3.1.8 4.5L8 11.7l-4 2.2.8-4.5L1.5 6.3l4.5-.6z"/></svg><svg viewBox="0 0 16 16"><path d="M8 1.5l2 4.2 4.5.6-3.3 3.1.8 4.5L8 11.7l-4 2.2.8-4.5L1.5 6.3l4.5-.6z"/></svg></div>
  <div class="u057-view" aria-live="polite"></div>
  <div class="u057-who"><b></b><small></small></div>
  <div class="u057-faces" role="group" aria-label="Choose a review"><span class="u057-n" aria-hidden="true"></span></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var view = root.querySelector('.u057-view'), who = root.querySelector('.u057-who'), faces = root.querySelector('.u057-faces'), num = root.querySelector('.u057-n');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var D = [
    ['The code matches our mockups, so build time was *cut in half.*', 'Doyun Park', 'Frontend lead', 'linear-gradient(140deg,#B7A4FF,#6A57F2)', '#B7A4FF', '#6A57F2'],
    ['The motion never overdoes it and fits our tone. *User response* clearly improved.', 'Harin Choi', 'Product designer', 'linear-gradient(140deg,#A5F2D3,#17A077)', '#A5F2D3', '#17A077'],
    ['I pasted the prompt and it slotted into our old button *seamlessly.*', 'Seojun Yoon', 'Startup founder', 'linear-gradient(140deg,#FFD08A,#D2702A)', '#FFD08A', '#FF6B8B'],
    ['Dark mode came out right too, so *QA time* just vanished.', 'Mina Jung', 'QA manager', 'linear-gradient(140deg,#7DB4FF,#3D5BFF)', '#7DB4FF', '#3D5BFF']
  ];
  var DUR = 5200, cur = -1, t0 = 0, paused = false, raf = 0, acc = 0;
  var btns = D.map(function (d, i) {
    var b = document.createElement('button');
    b.className = 'u057-f'; b.type = 'button';
    b.setAttribute('aria-label', 'Review ' + (i + 1) + ', ' + d[1]);
    b.style.setProperty('--g', d[3]);
    b.innerHTML = '<i></i><svg viewBox="0 0 40 40" aria-hidden="true"><circle class="tr" cx="20" cy="20" r="18.5"/><circle class="pr" cx="20" cy="20" r="18.5" pathLength="100"/></svg>';
    b.addEventListener('click', function () { show(i); });
    faces.insertBefore(b, num);
    return b;
  });
  function quote(d) {
    var p = document.createElement('p');
    p.className = 'u057-q';
    var k = 0;
    p.innerHTML = d[0].split(/(\*[^*]+\*)/).map(function (part) {
      var hi = part.charAt(0) === '*';
      var w = (hi ? part.slice(1, -1) : part).split(' ').filter(Boolean).map(function (x) { return '<span style="--i:' + (k++) + '">' + x + '</span>'; }).join(' ');
      return hi ? ' <mark>' + w + '</mark> ' : w;
    }).join('');
    return p;
  }
  function show(i, dir) {
    i = (i + D.length) % D.length;
    if (i === cur) return;
    dir = dir || (i > cur ? 1 : -1);
    var old = view.querySelector('.u057-q.on');
    cur = i;
    var d = D[i];
    root.style.setProperty('--c1', d[4]); root.style.setProperty('--c2', d[5]);
    var q = quote(d);
    view.appendChild(q);
    void q.offsetWidth;
    q.classList.add('on');
    if (old) {
      old.classList.remove('on');
      old.style.transform = 'translateX(' + (-dir * 30) + 'px)'; old.style.opacity = '0';
      setTimeout(function () { old.remove(); }, 500);
    }
    who.querySelector('b').textContent = d[1];
    who.querySelector('small').textContent = d[2];
    if (!rm && old) who.animate([{ opacity: 0, transform: 'translateY(6px)' }, { opacity: 1, transform: 'none' }], { duration: 450, easing: 'ease-out' });
    btns.forEach(function (b, k) { b.setAttribute('aria-current', String(k === i)); b.style.setProperty('--p', 0); });
    num.textContent = (i + 1) + ' / ' + D.length;
    acc = 0; t0 = performance.now();
  }
  function loop(now) {
    if (!root.isConnected) return;
    if (!paused && !rm) {
      var p = Math.min(1, (acc + now - t0) / DUR);
      btns[cur].style.setProperty('--p', p.toFixed(3));
      if (p >= 1) show(cur + 1, 1);
    }
    raf = requestAnimationFrame(loop);
  }
  function pause(v) {
    if (v === paused) return;
    if (v) acc += performance.now() - t0; else t0 = performance.now();
    paused = v;
  }
  root.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') pause(true); });
  root.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse' && !root.contains(document.activeElement)) pause(false); });
  root.addEventListener('focusin', function () { pause(true); });
  root.addEventListener('focusout', function (e) { if (!root.contains(e.relatedTarget)) pause(false); });
  root.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight') { e.preventDefault(); show(cur + 1, 1); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); show(cur - 1, -1); }
  });
  var sx = 0, dragging = false;
  view.addEventListener('pointerdown', function (e) { dragging = true; sx = e.clientX; view.setPointerCapture(e.pointerId); view.classList.add('drag'); });
  view.addEventListener('pointermove', function (e) {
    if (!dragging) return;
    var q = view.querySelector('.u057-q.on');
    if (q) { q.style.transition = 'none'; q.style.transform = 'translateX(' + (e.clientX - sx) * 0.6 + 'px)'; }
  });
  function end(e) {
    if (!dragging) return;
    dragging = false; view.classList.remove('drag');
    var dx = e.clientX - sx, q = view.querySelector('.u057-q.on');
    if (q) { q.style.transition = ''; q.style.transform = ''; }
    if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1), dx < 0 ? 1 : -1);
  }
  view.addEventListener('pointerup', end);
  view.addEventListener('pointercancel', end);
  show(0);
  raf = requestAnimationFrame(loop);
})();
</script>
--- Code end ---
