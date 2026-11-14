---
source: "lucianlabs"
id: "265"
title: "Delivery promise with order cutoff"
category: "Commerce & Pricing"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#265"
tags: ["delivery", "countdown", "shipping", "eta", "ecommerce"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Delivery promise with order cutoff (265, Commerce & Pricing)
[What it does] A product page's delivery note counts down “Order within 1 h 23 min for delivery tomorrow” by the second, while the bar below shrinks with the time left before today's dispatch cutoff. Change the address to Jeju and the headline flips to the day after tomorrow, a note replaces the countdown, and a ferry step slides into the delivery steps below so the truck goes that much farther.
[How to use it] Press the address button and switch regions

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
<!-- Lucian UX/UI Prompt #265 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#265 -->
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
.u265{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u265-cd{position:absolute;left:18px;right:18px;top:20px;padding:16px;border-radius:20px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line)}
.u265-rw{display:flex;align-items:center;gap:7px;font-size:11px;font-weight:750;color:var(--ux-ink-3)}
.u265-rg{display:inline-flex;align-items:center;gap:4px;height:26px;padding:0 8px 0 10px;border:0;border-radius:8px;background:var(--ux-surface);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink);font:inherit;font-size:11px;font-weight:850;cursor:pointer}
.u265-rg svg{width:10px;height:10px;transition:transform .25s}
.u265.is-open .u265-rg svg{transform:rotate(180deg)}
.u265-dd{position:absolute;left:62px;top:66px;z-index:3;width:170px;padding:5px;border-radius:13px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 16px 30px -14px var(--ux-shadow-strong);transform-origin:20% 0;transform:scale(.92) translateY(-4px);opacity:0;pointer-events:none;transition:transform .22s cubic-bezier(.3,1.5,.5,1),opacity .15s}
.u265.is-open .u265-dd{transform:none;opacity:1;pointer-events:auto}
.u265-op{display:flex;align-items:center;justify-content:space-between;width:100%;height:32px;padding:0 9px;border:0;border-radius:8px;background:none;color:var(--ux-ink);font:inherit;font-size:11.5px;font-weight:750;cursor:pointer}
.u265-op:hover,.u265-op.g-hov{background:var(--ux-surface-2)}
.u265-op small{font-size:9.5px;font-weight:800;color:#059669}
.u265-op small.l{color:#D97706}
.u265-hd{position:relative;height:30px;margin-top:12px;overflow:hidden}
.u265-hd b{position:absolute;left:0;top:0;display:flex;align-items:center;gap:8px;height:30px;font-size:19px;font-weight:900;letter-spacing:-.03em;transition:transform .45s cubic-bezier(.3,1.3,.5,1),opacity .3s}
.u265-hd b i{width:22px;height:22px;border-radius:7px;display:grid;place-items:center;background:#10B981;color:#fff}
.u265-hd b i svg{width:13px;height:13px}
.u265-hd b.is-l i{background:#F59E0B}
.u265-hd b.is-in{transform:translateY(100%);opacity:0;transition:none}
.u265-hd b.is-out{transform:translateY(-100%);opacity:0}
.u265-sb{position:relative;height:18px;margin-top:6px;font-size:11.5px;font-weight:700;color:var(--ux-ink-2)}
.u265-sb>span{position:absolute;left:0;top:0;transition:opacity .3s,transform .3s}
.u265-sb>span.is-off{opacity:0;transform:translateY(5px)}
.u265-sb b{font-weight:900;color:#E11D48;font-variant-numeric:tabular-nums}
.u265-bar{height:6px;margin-top:10px;border-radius:3px;background:var(--ux-surface-3);overflow:hidden}
.u265-bar i{display:block;height:100%;border-radius:3px;background:linear-gradient(90deg,#F43F5E,#FB923C);transform-origin:0 50%;transition:transform 1s linear,background .3s,opacity .3s}
.u265.is-late .u265-bar i{opacity:.25}
.u265-tl{position:absolute;left:30px;right:30px;bottom:44px;height:60px}
.u265-ln{position:absolute;left:0;right:0;top:22px;height:3px;border-radius:2px;background:var(--ux-surface-3)}
.u265-ln i{display:block;height:100%;border-radius:2px;background:var(--ux-ink);transition:width .7s cubic-bezier(.3,1,.4,1)}
.u265-nd{position:absolute;top:16px;width:15px;height:15px;margin-left:-7.5px;border-radius:50%;background:var(--ux-surface);box-shadow:inset 0 0 0 2.5px var(--ux-surface-3);transition:left .6s cubic-bezier(.3,1.2,.5,1),opacity .35s,transform .35s cubic-bezier(.3,1.6,.5,1)}
.u265-nd.is-done{box-shadow:inset 0 0 0 5px var(--ux-ink)}
.u265-nd.is-off{opacity:0;transform:scale(.3)}
.u265-nd span{position:absolute;left:50%;top:22px;transform:translateX(-50%);white-space:nowrap;font-size:10px;font-weight:800;color:var(--ux-ink-3)}
.u265-nd.is-x{box-shadow:inset 0 0 0 2.5px #F59E0B}
.u265-nd.is-x span{color:#D97706}
.u265-tr{position:absolute;top:-6px;width:26px;height:20px;margin-left:-13px;color:var(--ux-ink);transition:left .7s cubic-bezier(.3,1,.4,1);animation:u265-bob .6s ease-in-out infinite alternate}
@keyframes u265-bob{to{transform:translateY(-2px)}}
.u265 button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:1px}
@media (prefers-reduced-motion: reduce){.u265-hd b,.u265-nd,.u265-tr,.u265-ln i,.u265-bar i,.u265-dd{transition:none}.u265-tr{animation:none}}
</style>
<div class="ux u265">
  <div class="u265-cd">
    <div class="u265-rw">Ship to<button type="button" class="u265-rg" aria-haspopup="listbox" aria-expanded="false" aria-label="Change address"><span></span><svg viewBox="0 0 10 10" aria-hidden="true"><path d="M2 3.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>
    <div class="u265-hd" aria-live="polite"></div>
    <div class="u265-sb"><span class="u265-cn"></span><span class="u265-nt is-off"></span></div>
    <div class="u265-bar" aria-hidden="true"><i></i></div>
  </div>
  <div class="u265-dd" role="listbox"></div>
  <div class="u265-tl" aria-hidden="true"><div class="u265-ln"><i></i></div><svg class="u265-tr" viewBox="0 0 26 20"><path d="M2 4h13v10H2zM15 7h5l4 4v3h-9z" fill="currentColor"/><circle cx="7" cy="15.5" r="2.6" fill="var(--ux-surface)" stroke="currentColor" stroke-width="1.8"/><circle cx="19" cy="15.5" r="2.6" fill="var(--ux-surface)" stroke="currentColor" stroke-width="1.8"/></svg></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var rg = root.querySelector('.u265-rg'), rgl = rg.querySelector('span'), dd = root.querySelector('.u265-dd'), hd = root.querySelector('.u265-hd'), cn = root.querySelector('.u265-cn'), nt = root.querySelector('.u265-nt'), bar = root.querySelector('.u265-bar i'), tl = root.querySelector('.u265-tl'), ln = root.querySelector('.u265-ln i'), tr = root.querySelector('.u265-tr');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var RG = [['Seoul, Gangnam', 1], ['Busan, Haeundae', 1], ['Jeju City', 2]];
  var DAY = ['', 'Arrives tomorrow (Thu)', 'Arrives Fri (in 2 days)'], SHORT = ['', 'Tomorrow', 'In 2 days'];
  var ST = [['Order', 0], ['Ships today', 0], ['Ferry', 2], ['Delivered', 0]];
  var WIN = 6 * 3600, left = 1 * 3600 + 23 * 60 + 45, cur = -1;
  nt.textContent = 'Island addresses take one more day by ferry';
  var O = RG.map(function (r, i) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u265-op'; b.setAttribute('role', 'option');
    b.innerHTML = '<span></span><small' + (r[1] > 1 ? ' class="l"' : '') + '></small>'; b.firstChild.textContent = r[0]; b.lastChild.textContent = SHORT[r[1]];
    b.addEventListener('click', function () { pick(i); setOpen(false); rg.focus({ preventScroll: true }); });
    dd.appendChild(b); return b;
  });
  var N = ST.map(function (s) { var d = document.createElement('div'); d.className = 'u265-nd'; d.innerHTML = '<span></span>'; d.firstChild.textContent = s[0]; tl.appendChild(d); return d; });
  var TRUCK = '<svg viewBox="0 0 14 14" aria-hidden="true"><path d="M1.5 3.5h7v6h-7zM8.5 5.5h2.6l1.9 2v2h-4.5z" fill="currentColor"/></svg>';
  function head(k) {
    var old = hd.firstChild, b = document.createElement('b'); b.innerHTML = '<i>' + TRUCK + '</i><span></span>'; b.lastChild.textContent = DAY[k]; if (k > 1) b.classList.add('is-l');
    if (!old || rm) { hd.innerHTML = ''; hd.appendChild(b); return; }
    b.classList.add('is-in'); hd.appendChild(b); void b.offsetWidth; b.classList.remove('is-in'); old.classList.add('is-out'); setTimeout(function () { old.remove(); }, 460);
  }
  function steps(k) {
    var vis = ST.filter(function (s) { return !s[1] || k > 1; }), n = vis.length;
    ST.forEach(function (s, i) {
      var d = N[i], j = vis.indexOf(s);
      d.classList.toggle('is-off', j < 0); d.classList.toggle('is-x', !!s[1]);
      if (j >= 0) d.style.left = (j / (n - 1) * 100) + '%';
      d.classList.toggle('is-done', j >= 0 && j <= 1);
    });
    var at = (1.5 / (n - 1)) * 100; ln.style.width = at + '%'; tr.style.left = at + '%';
  }
  function pick(i) {
    if (i === cur) return;
    var k = RG[i][1], was = cur < 0 ? -1 : RG[cur][1]; cur = i;
    rgl.textContent = RG[i][0]; O.forEach(function (o, j) { o.setAttribute('aria-selected', j === i); });
    root.classList.toggle('is-late', k > 1);
    cn.classList.toggle('is-off', k > 1); nt.classList.toggle('is-off', k <= 1);
    if (k !== was) { head(k); steps(k); }
  }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function draw() {
    var h = Math.floor(left / 3600), m = Math.floor(left % 3600 / 60), s = left % 60;
    cn.innerHTML = '<b></b> '; cn.firstChild.textContent = h + ' h ' + pad(m) + ' min ' + pad(s); cn.appendChild(document.createTextNode(' s left to order'));
    bar.style.transform = 'scaleX(' + (left / WIN).toFixed(4) + ')';
  }
  (function tick() { if (!root.isConnected) return; draw(); left = Math.max(0, left - 1); setTimeout(tick, 1000); })();
  function setOpen(v) { root.classList.toggle('is-open', v); rg.setAttribute('aria-expanded', v); }
  rg.addEventListener('click', function () { setOpen(!root.classList.contains('is-open')); });
  root.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  pick(0);
})();
</script>
--- Code end ---
