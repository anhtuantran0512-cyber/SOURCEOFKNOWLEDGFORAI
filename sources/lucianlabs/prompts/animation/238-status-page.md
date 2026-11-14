---
source: "lucianlabs"
id: "238"
title: "Status page with uptime bars"
category: "App Screens"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#238"
tags: ["status-page", "uptime", "incidents", "monitoring", "saas"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Status page with uptime bars (238, App Screens)
[What it does] At the top of a service status page, “All systems operational” sits beside a green pulse, and below it API, Dashboard, Payments and Webhooks each show the last 30 days as a row of 30 small bars. The bars grow in from the left as the page opens, and resting the pointer on one shows that day's uptime and any incident in a bubble. Press a component to unfold its past incidents below.
[How to use it] Rest the pointer on the bars, then press a component name to open its history

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
<!-- Lucian UX/UI Prompt #238 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#238 -->
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
.u238{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u238-hd{position:absolute;left:14px;right:14px;top:14px;display:flex;align-items:center;gap:10px;padding:11px 12px;border-radius:15px;background:color-mix(in srgb,#10B981 12%,transparent)}
.u238-pu{position:relative;flex:none;width:12px;height:12px;border-radius:50%;background:#10B981}
.u238-pu::after{content:"";position:absolute;inset:-5px;border-radius:50%;border:2px solid #10B981;animation:u238-p 1.8s ease-out infinite}
@keyframes u238-p{from{transform:scale(.5);opacity:1}to{transform:scale(1.5);opacity:0}}
.u238-hd div{flex:1}
.u238-hd b{display:block;font-size:13px;font-weight:900;color:#047857}
.u238-hd small{display:block;font-size:9.5px;font-weight:700;color:var(--ux-ink-3)}
.u238-hd>span:last-child{height:26px;padding:0 10px;border-radius:999px;background:var(--ux-surface);box-shadow:inset 0 0 0 1px var(--ux-line);font-size:10.5px;font-weight:850;line-height:26px}
.u238-ls{position:absolute;left:14px;right:14px;top:76px;bottom:8px;overflow-y:auto;scrollbar-width:none}
.u238-ls::-webkit-scrollbar{display:none}
.u238-it{padding:9px 2px 8px;border-bottom:1px solid var(--ux-line)}
.u238-tp{display:flex;align-items:center;gap:6px}
.u238-nm{display:flex;align-items:center;gap:5px;padding:0;border:0;background:none;color:var(--ux-ink);font:inherit;font-size:11.5px;font-weight:850;cursor:pointer}
.u238-nm svg{width:9px;height:9px;color:var(--ux-ink-3);transition:transform .25s}
.u238-it.is-open .u238-nm svg{transform:rotate(90deg)}
.u238-tp em{margin-left:auto;font-style:normal;font-size:10px;font-weight:800;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u238-bar{position:relative;display:flex;gap:2px;height:24px;margin-top:6px;align-items:flex-end}
.u238-bar i{flex:1;height:100%;border-radius:2px;background:#10B981;transform:scaleY(0);transform-origin:50% 100%;transition:transform .45s cubic-bezier(.3,1.4,.5,1),opacity .15s}
.u238.is-in .u238-bar i{transform:none}
.u238-bar i.w{background:#F59E0B}
.u238-bar i.e{background:#E11D48}
.u238-bar i.is-hl{opacity:.6}
.u238-ax{display:flex;justify-content:space-between;margin-top:3px;font-size:8.5px;font-weight:700;color:var(--ux-ink-3)}
.u238-tt{position:absolute;bottom:30px;z-index:3;width:max-content;max-width:180px;padding:6px 9px;border-radius:9px;background:var(--ux-ink);color:var(--ux-surface);font-size:9.5px;line-height:1.4;font-weight:700;transform:translateX(-50%);opacity:0;pointer-events:none;transition:opacity .12s}
.u238-tt.is-on{opacity:1}
.u238-tt b{display:block;font-size:10px;font-weight:850}
.u238-hx{display:grid;grid-template-rows:0fr;transition:grid-template-rows .35s cubic-bezier(.3,1,.4,1)}
.u238-hx>div{min-height:0;overflow:hidden}
.u238-it.is-open .u238-hx{grid-template-rows:1fr}
.u238-hx p{display:flex;align-items:center;gap:7px;margin:7px 0 0;padding:7px 9px;border-radius:9px;background:var(--ux-surface-2);font-size:10px;font-weight:700;color:var(--ux-ink-2)}
.u238-hx p i{flex:none;width:7px;height:7px;border-radius:50%}
.u238-hx p span{flex:1}
.u238-hx p small{font-size:9px;font-weight:800;color:#059669}
.u238 button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u238-pu::after{animation:none}.u238-bar i,.u238-hx{transition:none}}
</style>
<div class="ux u238">
  <div class="u238-hd"><span class="u238-pu" aria-hidden="true"></span><div><b>All systems operational</b><small>Checked 1 min ago</small></div><span>Subscribe</span></div>
  <div class="u238-ls"></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ls = root.querySelector('.u238-ls');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var S = [['API', 99.98], ['Dashboard', 100], ['Payments', 99.71], ['Webhooks', 99.95]];
  var INC = {0: [[11, 'Slow responses', '12 min']], 2: [[18, 'Some card payments failed', '41 min'], [26, 'Payment confirmation delayed', '9 min']], 3: [[22, 'Retry delays', '15 min']]};
  var tt = document.createElement('div'); tt.className = 'u238-tt'; tt.setAttribute('role', 'tooltip'); root.appendChild(tt);
  S.forEach(function (s, si) {
    var it = document.createElement('div'); it.className = 'u238-it';
    it.innerHTML = '<div class="u238-tp"><button type="button" class="u238-nm" aria-expanded="false"><svg viewBox="0 0 9 9" aria-hidden="true"><path d="M3 1.5l3 3-3 3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span></span></button><em></em></div><div class="u238-bar"></div><div class="u238-ax"><span></span><span></span></div><div class="u238-hx"><div></div></div>';
    it.querySelector('.u238-nm span').textContent = s[0]; it.querySelector('em').textContent = s[1] + '%';
    var ax = it.querySelectorAll('.u238-ax span'); ax[0].textContent = '30 days ago'; ax[1].textContent = 'Today';
    var bar = it.querySelector('.u238-bar'), inc = INC[si] || [], B = [];
    for (var d = 0; d < 30; d++) {
      var hit = inc.filter(function (x) { return x[0] === d; })[0], b = document.createElement('i');
      if (hit) b.className = parseInt(hit[2], 10) > 30 ? 'e' : 'w';
      b.style.transitionDelay = (d * 0.018 + si * 0.06) + 's'; b._hit = hit; b._d = d;
      bar.appendChild(b); B.push(b);
    }
    function show(x) {
      var r = bar.getBoundingClientRect(), d = Math.max(0, Math.min(29, Math.floor((x - r.left) / r.width * 30))), b = B[d];
      B.forEach(function (o) { o.classList.toggle('is-hl', o !== b); });
      var ago = 29 - d, up = b._hit ? (100 - parseInt(b._hit[2], 10) / 14.4).toFixed(2) : '100.00';
      tt.innerHTML = '<b></b><span></span>'; tt.firstChild.textContent = ago ? ago + ' days ago' : 'Today';
      tt.lastChild.textContent = b._hit ? b._hit[1] + ' · ' + b._hit[2] : 'Uptime ' + up + '%' + ' · No incidents';
      var rr = root.getBoundingClientRect(), k = 340 / (rr.width || 340), br = b.getBoundingClientRect();
      tt.style.left = Math.max(70, Math.min(270, (br.left + br.width / 2 - rr.left) * k)) + 'px'; tt.style.top = ((br.top - rr.top) * k - 8) + 'px'; tt.style.bottom = 'auto'; tt.style.transform = 'translate(-50%,-100%)';
      tt.classList.add('is-on');
    }
    bar.addEventListener('pointermove', function (e) { show(e.clientX); });
    bar.addEventListener('pointerover', function (e) { show(e.clientX); });
    bar.addEventListener('pointerleave', function () { tt.classList.remove('is-on'); B.forEach(function (o) { o.classList.remove('is-hl'); }); });
    var hx = it.querySelector('.u238-hx>div');
    if (!inc.length) { var p0 = document.createElement('p'); p0.innerHTML = '<i style="background:#10B981"></i><span></span>'; p0.lastChild.textContent = 'No incidents in the last 30 days'; hx.appendChild(p0); }
    inc.slice().reverse().forEach(function (x) { var p = document.createElement('p'); p.innerHTML = '<i style="background:' + (parseInt(x[2], 10) > 30 ? '#E11D48' : '#F59E0B') + '"></i><span></span><small></small>'; p.querySelector('span').textContent = (29 - x[0]) + ' days ago · ' + x[1] + ' (' + x[2] + ')'; p.querySelector('small').textContent = 'Resolved'; hx.appendChild(p); });
    var nm = it.querySelector('.u238-nm');
    nm.addEventListener('click', function () { var o = !it.classList.contains('is-open'); it.classList.toggle('is-open', o); nm.setAttribute('aria-expanded', o); });
    ls.appendChild(it);
  });
  if (rm || !('IntersectionObserver' in window)) root.classList.add('is-in');
  else { var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); requestAnimationFrame(function () { root.classList.add('is-in'); }); } }); io.observe(root); }
})();
</script>
--- Code end ---
