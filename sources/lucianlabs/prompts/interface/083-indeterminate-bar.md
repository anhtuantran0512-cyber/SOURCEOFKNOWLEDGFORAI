---
source: "lucianlabs"
id: "083"
title: "Queue bar turning into progress"
category: "Loading & Progress"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#083"
tags: ["indeterminate", "progress", "deploy", "log", "morph"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Queue bar turning into progress (083, Loading & Progress)
[What it does] While queued with no known end, two bar segments stretch and slide; once the build starts, the same bar smoothly turns into a progress bar that fills. Log lines rise one by one as spinners turn into checks, and the status pill changes its color and text along with it.
[How to use it] Watch the deploy move from the queue to building to done. “Redeploy” plays it again from the start

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
<!-- Lucian UX/UI Prompt #083 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#083 -->
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
.u083{position:relative;width:350px;height:400px;display:flex;flex-direction:column;padding:20px 20px 18px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u083-h{display:flex;align-items:center;gap:10px}
.u083-h i{width:36px;height:36px;border-radius:11px;background:var(--ux-ink);position:relative}
.u083-h i::after{content:"";position:absolute;left:10px;top:11px;border-left:8px solid transparent;border-right:8px solid transparent;border-bottom:14px solid var(--ux-page)}
.u083-h b{display:block;font-size:15.5px;font-weight:850;letter-spacing:-.03em}
.u083-h small{display:block;font-size:12px;font-weight:650;color:var(--ux-ink-3)}
.u083-pill{margin-left:auto;height:26px;padding:0 10px;border-radius:999px;display:inline-flex;align-items:center;gap:6px;background:color-mix(in srgb,var(--c) 14%,transparent);color:var(--c);font-size:12px;font-weight:800;transition:background-color .4s,color .4s}
.u083-pill::before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor;animation:u083-blink 1.2s ease-in-out infinite}
.u083.is-done .u083-pill::before{animation:none}
@keyframes u083-blink{50%{opacity:.3}}
.u083-trk{position:relative;height:6px;margin:18px 0 6px;border-radius:3px;background:var(--ux-surface-3);overflow:hidden}
.u083-seg{position:absolute;top:0;bottom:0;border-radius:inherit;background:var(--ux-accent);transition:opacity .4s}
.u083-seg.a{animation:u083-a 1.6s cubic-bezier(.65,.05,.35,1) infinite}
.u083-seg.b{animation:u083-b 1.6s cubic-bezier(.25,.6,.4,1) .55s infinite}
@keyframes u083-a{0%{left:-35%;right:100%}60%{left:100%;right:-90%}100%{left:100%;right:-90%}}
@keyframes u083-b{0%{left:-200%;right:100%}60%{left:107%;right:-8%}100%{left:107%;right:-8%}}
.u083-fill{position:absolute;left:0;top:0;bottom:0;width:100%;border-radius:inherit;background:var(--ux-accent);transform-origin:0 50%;transform:scaleX(var(--p,0));opacity:0;transition:transform .5s var(--ux-ease),opacity .3s,background-color .4s}
.u083.is-det .u083-seg{opacity:0}
.u083.is-det .u083-fill{opacity:1}
.u083.is-done .u083-fill{background:var(--ux-mint)}
.u083-meta{display:flex;justify-content:space-between;font-size:12px;font-weight:700;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u083-log{flex:1;margin:12px 0 0;padding:12px;border-radius:16px;background:var(--ux-surface-2);list-style:none;overflow:hidden;display:flex;flex-direction:column;gap:7px;font-size:12.5px;font-weight:600;line-height:1.4}
.u083-log li{display:flex;align-items:center;gap:8px;color:var(--ux-ink-2);animation:u083-in .4s var(--ux-ease)}
@keyframes u083-in{from{opacity:0;transform:translateY(8px)}}
.u083-log time{color:var(--ux-ink-3);font:600 11.5px ui-monospace,SFMono-Regular,Menlo,monospace}
.u083-st{width:14px;height:14px;flex:none;position:relative}
.u083-st::before{content:"";position:absolute;inset:0;border-radius:50%;border:2px solid var(--ux-accent);border-right-color:transparent;animation:u083-spin .7s linear infinite}
.u083-log li.ok .u083-st::before{border:0;animation:none;background:var(--ux-mint);-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 14'%3E%3Cpath d='M3 7.4l2.6 2.6L11 4.6' fill='none' stroke='%23000' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/100% no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 14'%3E%3Cpath d='M3 7.4l2.6 2.6L11 4.6' fill='none' stroke='%23000' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/100% no-repeat}
.u083-log li.ok{color:var(--ux-ink-3)}
@keyframes u083-spin{to{transform:rotate(360deg)}}
.u083-re{margin-top:12px;height:44px;border:0;border-radius:14px;background:var(--ux-ink);color:var(--ux-page);font-size:14px;font-weight:750;transition:opacity .3s,transform .3s var(--ux-spring)}
.u083-re:active{transform:scale(.97)}
.u083-re[aria-disabled="true"]{opacity:.35}
.u083-re:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
</style>
<div class="ux u083">
  <div class="u083-h"><i aria-hidden="true"></i><span><b>Deploy #128</b><small>main · a3f9c21</small></span><span class="u083-pill" role="status" aria-live="polite" style="--c:var(--ux-warn)">Queued</span></div>
  <div class="u083-trk" role="progressbar" aria-label="Deploy progress" aria-valuemin="0" aria-valuemax="100"><span class="u083-seg a" aria-hidden="true"></span><span class="u083-seg b" aria-hidden="true"></span><span class="u083-fill" aria-hidden="true"></span></div>
  <div class="u083-meta"><span class="u083-l">Waiting for a spot in the queue</span><span class="u083-r"></span></div>
  <ol class="u083-log" aria-label="Deploy log"></ol>
  <button class="u083-re" type="button" aria-disabled="true">Redeploy</button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var pill = root.querySelector('.u083-pill'), trk = root.querySelector('.u083-trk'), fill = root.querySelector('.u083-fill');
  var ml = root.querySelector('.u083-l'), mr = root.querySelector('.u083-r'), log = root.querySelector('.u083-log'), re = root.querySelector('.u083-re');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var STEPS = [['Install dependencies', 0.22], ['Type check', 0.38], ['Build bundle', 0.7], ['Optimize images', 0.85], ['Deploy to edge', 1]];
  var ts = [], raf = 0, sec = 0;
  function later(fn, ms) { ts.push(setTimeout(function () { if (root.isConnected) fn(); }, rm ? Math.min(ms, 200) : ms)); }
  function line(txt) {
    var li = document.createElement('li');
    sec += 1 + Math.round(Math.random() * 3);
    li.innerHTML = '<span class="u083-st" aria-hidden="true"></span><time>00:' + ('0' + sec).slice(-2) + '</time><span></span>';
    li.lastChild.textContent = txt;
    log.appendChild(li);
    while (log.children.length > 6) log.firstChild.remove();
    return li;
  }
  function setPill(t, c) { pill.textContent = t; pill.style.setProperty('--c', c); }
  function run() {
    ts.forEach(clearTimeout); ts = []; cancelAnimationFrame(raf);
    root.classList.remove('is-det', 'is-done'); log.innerHTML = ''; sec = 0;
    fill.style.setProperty('--p', 0); trk.removeAttribute('aria-valuenow');
    setPill('Queued', 'var(--ux-warn)'); ml.textContent = 'Waiting for a spot in the queue'; mr.textContent = '';
    re.setAttribute('aria-disabled', 'true');
    var q = line('Queued · 2 ahead');
    later(function () {
      q.classList.add('ok');
      root.classList.add('is-det');
      setPill('Building', 'var(--ux-accent)');
      var i = 0;
      (function next() {
        var st = STEPS[i], li = line(st[0] + '…');
        ml.textContent = st[0];
        fill.style.setProperty('--p', st[1]);
        trk.setAttribute('aria-valuenow', Math.round(st[1] * 100));
        mr.textContent = Math.round(st[1] * 100) + '%';
        later(function () {
          li.classList.add('ok'); li.lastChild.textContent = st[0] + ' done';
          i++;
          if (i < STEPS.length) next();
          else {
            root.classList.add('is-done');
            setPill('Ready', 'var(--ux-mint)'); ml.textContent = 'Deployed to lumen.app'; mr.textContent = '38s';
            re.setAttribute('aria-disabled', 'false');
          }
        }, 650 + i * 120);
      })();
    }, 2300);
  }
  re.addEventListener('click', function () { if (re.getAttribute('aria-disabled') !== 'true') run(); });
  run();
})();
</script>
--- Code end ---
