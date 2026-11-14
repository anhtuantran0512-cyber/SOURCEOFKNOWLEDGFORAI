---
source: "lucianlabs"
id: "216"
title: "Staggered hero entrance"
category: "Hero & Backgrounds"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#216"
tags: ["hero", "landing", "stagger", "entrance", "reveal"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Staggered hero entrance (216, Hero & Backgrounds)
[What it does] The moment a landing page's first screen appears, the top menu settles in, then the badge, headline words, description, two buttons and product screen rise from below one after another at short intervals. Each headline word slides up from beneath a hidden line, and the product screen arrives tilted back and blurred before straightening into focus. Use Replay in the top right to watch the entrance again.
[How to use it] Press Replay in the top right to watch the entrance order again

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
<!-- Lucian UX/UI Prompt #216 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#216 -->
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
.u216{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:radial-gradient(120% 70% at 50% 0%,var(--ux-accent-soft),transparent 60%),var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink);perspective:700px}
.u216-nav{position:absolute;left:16px;right:16px;top:14px;display:flex;align-items:center;gap:12px;font-size:10.5px;font-weight:700;color:var(--ux-ink-2)}
.u216-lg{display:flex;align-items:center;gap:6px;font-size:12.5px;font-weight:900;color:var(--ux-ink);margin-right:auto}
.u216-lg i{width:14px;height:14px;border-radius:5px;background:var(--ux-grad)}
.u216-nav b{padding:5px 10px;border-radius:999px;background:var(--ux-ink);color:var(--ux-surface);font-weight:800}
.u216-bd{position:absolute;left:0;right:0;top:56px;display:flex;justify-content:center}
.u216-bd span{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;background:var(--ux-surface);box-shadow:inset 0 0 0 1px var(--ux-line);font-size:10px;font-weight:800;color:var(--ux-ink-2)}
.u216-bd span i{width:6px;height:6px;border-radius:50%;background:var(--ux-mint)}
.u216-h{position:absolute;left:0;right:0;top:82px;margin:0;text-align:center;font-size:25px;line-height:1.18;font-weight:900;letter-spacing:-.04em}
.u216-ln{display:block}
.u216-w{display:inline-block;overflow:hidden;vertical-align:top;padding:0 .08em}
.u216-w>span{display:inline-block}
.u216-p{position:absolute;left:30px;right:30px;top:150px;margin:0;text-align:center;font-size:11.5px;line-height:1.5;font-weight:600;color:var(--ux-ink-2)}
.u216-ct{position:absolute;left:0;right:0;top:180px;display:flex;justify-content:center;gap:8px}
.u216-ct span{display:inline-flex;align-items:center;gap:5px;height:30px;padding:0 13px;border-radius:999px;font-size:11px;font-weight:800}
.u216-ct span:first-child{background:var(--ux-accent);color:#fff;box-shadow:0 8px 18px -8px var(--ux-accent)}
.u216-ct span:last-child{background:var(--ux-surface);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink)}
.u216-sc{position:absolute;left:28px;right:28px;top:228px;height:150px;border-radius:14px 14px 0 0;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 -10px 40px -18px var(--ux-shadow-strong);display:grid;grid-template-columns:62px 1fr;overflow:hidden;transform-origin:50% 100%}
.u216-sb{background:var(--ux-surface-2);padding:10px 8px;display:flex;flex-direction:column;gap:6px}
.u216-sb i{height:6px;border-radius:3px;background:var(--ux-line)}
.u216-sb i:first-child{width:60%;background:var(--ux-accent)}
.u216-mn{padding:10px 12px}
.u216-mn small{font-size:8.5px;font-weight:800;color:var(--ux-ink-3)}
.u216-bars{display:flex;align-items:flex-end;gap:5px;height:56px;margin-top:6px}
.u216-bars i{flex:1;border-radius:3px 3px 0 0;background:color-mix(in srgb,var(--ux-accent) 35%,transparent)}
.u216-bars i:nth-child(5){background:var(--ux-accent)}
.u216-re{position:absolute;right:12px;bottom:12px;z-index:3;display:inline-flex;align-items:center;gap:5px;height:26px;padding:0 10px;border:0;border-radius:999px;background:var(--ux-ink);color:var(--ux-surface);font:inherit;font-size:10.5px;font-weight:800;cursor:pointer;opacity:.92}
.u216-re svg{width:11px;height:11px}
.u216-re:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}

.u216 [data-s]{opacity:0;transform:translateY(14px);transition:opacity .55s var(--ux-ease),transform .7s cubic-bezier(.2,.8,.2,1);transition-delay:calc(var(--d) * 1ms)}
.u216 .u216-nav[data-s]{transform:translateY(-12px)}
.u216 .u216-w>span{transform:translateY(105%);transition:transform .75s cubic-bezier(.2,.8,.2,1);transition-delay:calc(var(--d) * 1ms)}
.u216 .u216-sc[data-s]{transform:translateY(46px) rotateX(24deg) scale(.94);filter:blur(6px);transition:opacity .6s,transform 1.1s cubic-bezier(.2,.8,.2,1),filter .9s;transition-delay:calc(var(--d) * 1ms)}
.u216.is-in [data-s]{opacity:1;transform:none;filter:none}
.u216.is-in .u216-w>span{transform:none}
.u216.is-snap [data-s],.u216.is-snap .u216-w>span{transition:none}
@media (prefers-reduced-motion: reduce){.u216 [data-s],.u216 .u216-w>span{transition:none}}
</style>
<div class="ux u216">
  <div class="u216-nav" data-s style="--d:0"><span class="u216-lg"><i aria-hidden="true"></i>Lumen</span><span>Product</span><span>Pricing</span><span>Blog</span><b>Get started</b></div>
  <div class="u216-bd" data-s style="--d:180"><span><i aria-hidden="true"></i>Version 2.0 is out</span></div>
  <h3 class="u216-h"></h3>
  <p class="u216-p" data-s style="--d:620">From planning to launch, every scattered tool in one place.</p>
  <div class="u216-ct" data-s style="--d:760"><span>Start free</span><span>Watch demo</span></div>
  <div class="u216-sc" data-s style="--d:900" aria-hidden="true"><div class="u216-sb"><i></i><i></i><i></i><i></i><i></i></div><div class="u216-mn"><small>This week</small><div class="u216-bars"><i style="height:40%"></i><i style="height:62%"></i><i style="height:48%"></i><i style="height:74%"></i><i style="height:92%"></i><i style="height:58%"></i></div></div></div>
  <button type="button" class="u216-re"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.2 6a3.8 3.8 0 1 0 1.1-2.7M2 1.6v2.2h2.2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Replay</button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var h = root.querySelector('.u216-h'), re = root.querySelector('.u216-re');
  var WORDS = [['Finish', 'your', 'team’s'], ['work', 'in', 'one', 'place']];
  var d = 300;
  WORDS.forEach(function (line) {
    var ln = document.createElement('span'); ln.className = 'u216-ln';
    line.forEach(function (w, i) {
      var box = document.createElement('span'), inner = document.createElement('span');
      box.className = 'u216-w'; inner.textContent = w; inner.style.setProperty('--d', d); d += 70;
      box.appendChild(inner); ln.appendChild(box); if (i < line.length - 1) ln.appendChild(document.createTextNode(' '));
    });
    h.appendChild(ln);
  });
  h.setAttribute('aria-label', WORDS.map(function (l) { return l.join(' '); }).join(' '));
  function play() {
    root.classList.add('is-snap'); root.classList.remove('is-in'); void root.offsetWidth;
    root.classList.remove('is-snap'); requestAnimationFrame(function () { root.classList.add('is-in'); });
  }
  re.addEventListener('click', play);
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); play(); } }, { threshold: 0.35 });
    io.observe(root);
  } else root.classList.add('is-in');
})();
</script>
--- Code end ---
