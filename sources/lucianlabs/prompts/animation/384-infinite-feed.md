---
source: "lucianlabs"
id: "384"
title: "Endlessly appending feed"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#384"
tags: ["scroll", "infinite", "feed", "loader", "pagination"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Endlessly appending feed (384, Scroll Motion)
[What it does] Reach the end of the list and a bouncing three-dot loader appears before new cards float up from below one at a time and join the list. Meanwhile, when new posts pile up above, a ‘3 new posts’ pill slides down; tap it to glide to the top where the new posts shimmer.
[How to use it] Scroll to the bottom of the list, and tap the pill when it drops in

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
<!-- Lucian UX/UI Prompt #384 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#384 -->
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
.u384{position:relative;width:340px;height:350px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u384-hd{position:absolute;left:0;right:0;top:0;z-index:2;height:50px;display:flex;align-items:center;padding:0 18px;background:color-mix(in srgb,var(--ux-surface) 85%,transparent);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);box-shadow:0 1px 0 var(--ux-line);font-size:17px;font-weight:850}
.u384-sc{position:absolute;inset:0;overflow-y:auto;padding:58px 14px 14px;scrollbar-width:none;outline:none}
.u384-sc::-webkit-scrollbar{display:none}
.u384-ls{display:grid;gap:10px}
.u384-c{display:flex;align-items:center;gap:12px;padding:12px;border-radius:16px;background:var(--ux-surface-2)}
.u384-c.in{animation:u384-in .55s var(--ux-spring) both;animation-delay:var(--d)}
@keyframes u384-in{from{opacity:0;transform:translateY(24px) scale(.96)}}
.u384-c.fresh{animation:u384-in .55s var(--ux-spring) both,u384-glow 1.6s ease .3s}
@keyframes u384-glow{0%,100%{box-shadow:none}30%{box-shadow:0 0 0 2px var(--ux-accent),0 0 20px color-mix(in srgb,var(--ux-accent) 35%,transparent)}}
.u384-c i{flex:none;width:52px;height:52px;border-radius:12px;background:linear-gradient(135deg,var(--a),var(--b))}
.u384-c b{display:block;font-size:14px;font-weight:780}
.u384-c span{font-size:12px;font-weight:650;color:var(--ux-ink-3)}
.u384-ld{display:flex;justify-content:center;gap:6px;height:0;overflow:hidden;transition:height .3s}
.u384.is-load .u384-ld{height:44px;padding-top:16px}
.u384-ld i{width:9px;height:9px;border-radius:50%;background:var(--ux-ink-3);animation:u384-b .6s ease-in-out infinite alternate}
.u384-ld i:nth-child(2){animation-delay:.15s}
.u384-ld i:nth-child(3){animation-delay:.3s}
@keyframes u384-b{to{transform:translateY(-8px);background:var(--ux-accent)}}
.u384-new{position:absolute;left:50%;top:58px;z-index:3;height:34px;padding:0 14px 0 10px;border:0;border-radius:999px;display:flex;align-items:center;gap:6px;background:var(--ux-accent);color:var(--ux-accent-ink);font-size:12.5px;font-weight:800;box-shadow:0 10px 20px -8px var(--ux-shadow-strong);transform:translate(-50%,-120px);transition:transform .55s var(--ux-spring)}
.u384.has-new .u384-new{transform:translate(-50%,0)}
.u384-new svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
</style>
<div class="ux u384">
  <div class="u384-hd">Feed</div>
  <div class="u384-sc" tabindex="0" aria-label="Feed" aria-busy="false"><div class="u384-ls"></div><div class="u384-ld" aria-hidden="true"><i></i><i></i><i></i></div></div>
  <button class="u384-new" type="button" tabindex="-1"><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M7 12V2M3 6l4-4 4 4"/></svg><span></span></button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u384-sc'), ls = root.querySelector('.u384-ls'), nb = root.querySelector('.u384-new');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var WORDS = ['Today’s sunset', 'A new bakery', 'Weekend hiking route', 'Cat update', 'What I’m reading', 'Rainy streets', 'First film photo', 'Homemade pasta', 'Han River bike ride', 'Tidying the studio', 'New sneakers', 'Morning walk'];
  var C = [['#FFC9C9', '#FFA8A8'], ['#D0EBFF', '#A5D8FF'], ['#D3F9D8', '#8CE99A'], ['#FFF3BF', '#FFD43B'], ['#E5DBFF', '#B197FC']];
  var n = 0, loading = false, pending = 0, loads = 0;
  function card(fresh, delay) {
    var i = n++, el = document.createElement('div');
    el.className = 'u384-c ' + (fresh ? 'fresh' : 'in');
    el.style.setProperty('--d', (delay || 0) + 'ms');
    var c = C[i % C.length];
    el.innerHTML = '<i style="--a:' + c[0] + ';--b:' + c[1] + '"></i><div><b></b><span></span></div>';
    el.querySelector('b').textContent = WORDS[i % WORDS.length];
    el.querySelector('span').textContent = (fresh ? 1 : 5 + i * 7) + ' min ago';
    return el;
  }
  function more() {
    if (loading) return;
    loading = true;
    root.classList.add('is-load'); sc.setAttribute('aria-busy', 'true');
    setTimeout(function () {
      if (!root.isConnected) return;
      for (var k = 0; k < 3; k++) ls.appendChild(card(false, rm ? 0 : k * 110));
      loading = false; loads += 1;
      root.classList.remove('is-load'); sc.setAttribute('aria-busy', 'false');
      if (loads === 2) setTimeout(function () { pending = 3; nb.querySelector('span').textContent = pending + ' new posts'; nb.tabIndex = 0; root.classList.add('has-new'); }, 600);
    }, rm ? 200 : 1000);
  }
  sc.addEventListener('scroll', function () { if (sc.scrollTop + sc.clientHeight > sc.scrollHeight - 30) more(); }, { passive: true });
  nb.addEventListener('click', function () {
    root.classList.remove('has-new'); nb.tabIndex = -1;
    sc.scrollTo({ top: 0, behavior: rm ? 'auto' : 'smooth' });
    setTimeout(function () {
      for (var k = 0; k < pending; k++) { var el = card(true); el.style.setProperty('--d', (k * 90) + 'ms'); ls.insertBefore(el, ls.children[k]); }
      pending = 0;
    }, rm ? 0 : 450);
  });
  for (var k = 0; k < 4; k++) ls.appendChild(card(false, k * 60));
})();
</script>
--- Code end ---
