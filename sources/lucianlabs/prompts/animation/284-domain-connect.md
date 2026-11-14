---
source: "lucianlabs"
id: "284"
title: "Step-by-step domain connection"
category: "Site Builder Tools"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#284"
tags: ["domain", "dns", "ssl", "verification", "hosting"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Step-by-step domain connection (284, Site Builder Tools)
[What it does] A connect-your-domain screen lists the DNS records you need to add, each value with a copy button that turns into a check when pressed. Press Verify and DNS lookup, global propagation and certificate issuance each spin in turn before turning into checks, with the region dots on a small map lighting up green one by one during propagation. When everything is done, a lock and https appear in the address and the domain is connected.
[How to use it] Press a value's copy button, then press Verify

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
<!-- Lucian UX/UI Prompt #284 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#284 -->
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
.u284{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u284-hd{position:absolute;left:18px;right:18px;top:18px}
.u284-hd b{font-size:15px;font-weight:900}
.u284-ad{display:flex;align-items:center;gap:5px;margin-top:8px;height:32px;padding:0 10px;border-radius:10px;background:var(--ux-surface-2);font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;font-weight:700}
.u284-ad .s{display:inline-block;overflow:hidden;max-width:0;color:#059669;transition:max-width .5s cubic-bezier(.3,1,.4,1)}
.u284.is-done .u284-ad .s{max-width:70px}
.u284-ad svg{width:13px;height:13px;color:var(--ux-ink-3);transition:color .3s}
.u284.is-done .u284-ad svg{color:#059669}
.u284-ad em{margin-left:auto;font-style:normal;font-family:inherit;font-size:9.5px;font-weight:850;padding:2px 7px;border-radius:999px;background:color-mix(in srgb,#F59E0B 16%,transparent);color:#B45309;transition:background .3s,color .3s}
.u284.is-done .u284-ad em{background:color-mix(in srgb,#10B981 16%,transparent);color:#047857}
.u284-tb{position:absolute;left:18px;right:18px;top:88px;font-size:10px}
.u284-r{display:grid;grid-template-columns:44px 30px 1fr 28px;align-items:center;gap:6px;height:30px;border-bottom:1px solid var(--ux-line)}
.u284-r.h{height:22px;font-weight:850;color:var(--ux-ink-3)}
.u284-r b{font-weight:850}
.u284-r code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:10px;color:var(--ux-ink-2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.u284-cp{width:26px;height:24px;border:0;border-radius:7px;background:var(--ux-surface-2);color:var(--ux-ink-2);display:grid;place-items:center;cursor:pointer}
.u284-cp svg{width:12px;height:12px}
.u284-cp.is-ok{background:color-mix(in srgb,#10B981 16%,transparent);color:#059669}
.u284-ck{position:absolute;left:18px;right:18px;top:182px}
.u284-st{display:flex;align-items:center;gap:8px;height:24px;font-size:11px;font-weight:750;color:var(--ux-ink-3);transition:color .25s}
.u284-st i{position:relative;flex:none;width:16px;height:16px;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--ux-line)}
.u284-st.is-run{color:var(--ux-ink)}
.u284-st.is-run i{box-shadow:none;border:2px solid color-mix(in srgb,var(--ux-accent) 25%,transparent);border-top-color:var(--ux-accent);box-sizing:border-box;animation:u284-sp .7s linear infinite}
@keyframes u284-sp{to{transform:rotate(360deg)}}
.u284-st.is-ok{color:var(--ux-ink)}
.u284-st.is-ok i{background:#10B981;box-shadow:none;animation:u284-pop .35s cubic-bezier(.3,1.7,.5,1)}
@keyframes u284-pop{from{transform:scale(.4)}}
.u284-st.is-ok i::after{content:"";position:absolute;left:5.5px;top:3px;width:3.5px;height:7px;border:solid #fff;border-width:0 1.6px 1.6px 0;transform:rotate(45deg)}
.u284-mp{position:relative;width:96px;height:30px;margin-left:auto}
.u284-mp span{position:absolute;width:6px;height:6px;border-radius:50%;background:var(--ux-surface-3);transition:background .3s,box-shadow .3s}
.u284-mp span.is-on{background:#10B981;box-shadow:0 0 0 3px color-mix(in srgb,#10B981 25%,transparent)}
.u284-mp svg{position:absolute;inset:0;width:96px;height:30px;color:var(--ux-surface-3)}
.u284-go{position:absolute;left:18px;right:18px;bottom:18px;height:44px;border:0;border-radius:13px;background:var(--ux-ink);color:var(--ux-surface);font:inherit;font-size:12.5px;font-weight:850;cursor:pointer;transition:background .3s,opacity .2s}
.u284-go:disabled{opacity:.6;cursor:default}
.u284.is-done .u284-go{background:#059669;opacity:1}
.u284 button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u284-st.is-run i,.u284-st.is-ok i{animation:none}.u284-ad .s{transition:none}}
</style>
<div class="ux u284">
  <div class="u284-hd"><b>Connect domain</b><div class="u284-ad"><svg viewBox="0 0 13 13" aria-hidden="true"><rect x="2.5" y="6" width="8" height="5.5" rx="1.4" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M4.3 6V4.4a2.2 2.2 0 0 1 4.4 0V6" fill="none" stroke="currentColor" stroke-width="1.4"/></svg><span class="s">https://</span>mybrand.com<em class="u284-bd"></em></div></div>
  <div class="u284-tb"><div class="u284-r h"><span>Type</span><span>Name</span><span>Value</span><span></span></div></div>
  <div class="u284-ck" aria-live="polite"></div>
  <button type="button" class="u284-go">Verify</button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var tb = root.querySelector('.u284-tb'), ck = root.querySelector('.u284-ck'), go = root.querySelector('.u284-go'), bd = root.querySelector('.u284-bd');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var REC = [['A', '@', '76.76.21.21'], ['CNAME', 'www', 'cname.hostly.app']];
  var CK = ['Finding DNS records', 'Propagating worldwide', 'Issuing SSL certificate'];
  var COPY = '<svg viewBox="0 0 12 12" aria-hidden="true"><rect x="3.5" y="3.5" width="6.5" height="6.5" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M2 8V2.8C2 2.4 2.4 2 2.8 2H8" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>', OK = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 6.3l2.3 2.3L9.5 3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  REC.forEach(function (r) {
    var d = document.createElement('div'); d.className = 'u284-r'; d.innerHTML = '<b></b><span></span><code></code><button type="button" class="u284-cp"></button>';
    d.querySelector('b').textContent = r[0]; d.querySelector('span').textContent = r[1]; d.querySelector('code').textContent = r[2];
    var b = d.querySelector('button'); b.innerHTML = COPY; b.setAttribute('aria-label', r[2] + ' copy');
    b.addEventListener('click', function () { try { navigator.clipboard && navigator.clipboard.writeText(r[2]).catch(function () {}); } catch (e) {} b.innerHTML = OK; b.classList.add('is-ok'); setTimeout(function () { b.innerHTML = COPY; b.classList.remove('is-ok'); }, 1600); });
    tb.appendChild(d);
  });
  var DOTS = [[14, 10], [22, 18], [44, 8], [50, 16], [70, 12], [80, 20], [88, 9]];
  var S = CK.map(function (c, i) {
    var d = document.createElement('div'); d.className = 'u284-st'; d.innerHTML = '<i aria-hidden="true"></i><span></span>'; d.querySelector('span').textContent = c;
    if (i === 1) { var m = document.createElement('div'); m.className = 'u284-mp'; m.setAttribute('aria-hidden', 'true'); DOTS.forEach(function (p) { var s = document.createElement('span'); s.style.left = p[0] + 'px'; s.style.top = p[1] + 'px'; m.appendChild(s); }); d.appendChild(m); }
    ck.appendChild(d); return d;
  });
  var M = ck.querySelectorAll('.u284-mp span'), gen = 0;
  bd.textContent = 'Pending';
  function later(g, ms, fn) { setTimeout(function () { if (g === gen && root.isConnected) fn(); }, rm ? 0 : ms); }
  go.addEventListener('click', function () {
    if (root.classList.contains('is-done')) return;
    var g = ++gen, t = 0; go.disabled = true; go.textContent = 'Checking…';
    S.forEach(function (s, i) {
      var dur = i === 1 ? 1900 : 1000;
      later(g, t, function () { s.classList.add('is-run'); });
      if (i === 1) Array.prototype.forEach.call(M, function (m, k) { later(g, t + 200 + k * 240, function () { m.classList.add('is-on'); }); });
      t += dur;
      later(g, t, function () { s.classList.remove('is-run'); s.classList.add('is-ok'); });
    });
    later(g, t + 250, function () { root.classList.add('is-done'); go.disabled = false; go.textContent = 'Connected'; bd.textContent = 'SSL'; });
  });
})();
</script>
--- Code end ---
