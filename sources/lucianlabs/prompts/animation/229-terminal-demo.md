---
source: "lucianlabs"
id: "229"
title: "Self-typing terminal demo"
category: "Site Builder Tools"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#229"
tags: ["terminal", "cli", "typing", "onboarding", "landing"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Self-typing terminal demo (229, Site Builder Tools)
[What it does] In a landing page's terminal window, an install command types itself out one character at a time as if by hand; at Enter, download and setup lines spin in turn before turning into checks while a progress bar fills. Next a run command types in, the server starts and a local address lights up, and clicking that address pops a small browser preview out beside it. Replay starts it over.
[How to use it] Watch to the end, then click the address on the last line

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
<!-- Lucian UX/UI Prompt #229 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#229 -->
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
.u229{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:radial-gradient(90% 70% at 50% 0%,color-mix(in srgb,#22C55E 10%,transparent),transparent 70%),var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u229-tm{position:absolute;left:14px;right:14px;top:16px;bottom:62px;border-radius:16px;background:#0B0D12;box-shadow:0 0 0 1px #232733,0 20px 40px -20px rgba(0,0,0,.6);overflow:hidden;color:#D1D5DB;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:10.5px;line-height:1.75}
.u229-bar{display:flex;align-items:center;gap:6px;height:28px;padding:0 12px;border-bottom:1px solid #1E222C}
.u229-bar i{width:9px;height:9px;border-radius:50%;background:#2E3340}
.u229-bar i:nth-child(1){background:#F87171}.u229-bar i:nth-child(2){background:#FBBF24}.u229-bar i:nth-child(3){background:#34D399}
.u229-bar span{margin-left:auto;color:#6B7280;font-size:9.5px}
.u229-bd{padding:8px 12px}
.u229-l{white-space:pre;overflow:hidden}
.u229-l .p{color:#34D399}
.u229-l .d{color:#6B7280}
.u229-l .ok{color:#34D399}
.u229-l .sp{display:inline-block;width:1ch;color:#A78BFA}
.u229-cu{display:inline-block;width:6px;height:12px;margin-left:1px;vertical-align:-2px;background:#E5E7EB;animation:u229-bl 1s steps(1) infinite}
@keyframes u229-bl{50%{opacity:0}}
.u229-pb{display:inline-block;width:110px;height:6px;margin:0 6px;border-radius:3px;background:#1F2430;vertical-align:1px;overflow:hidden}
.u229-pb i{display:block;height:100%;width:0;background:linear-gradient(90deg,#34D399,#A78BFA);transition:width .25s}
.u229-lk{padding:0;border:0;background:none;color:#60A5FA;font:inherit;text-decoration:underline;text-underline-offset:2px;cursor:pointer;animation:u229-gw 1.4s ease}
@keyframes u229-gw{0%{text-shadow:0 0 0 transparent}30%{text-shadow:0 0 10px #60A5FA}100%{text-shadow:0 0 0 transparent}}
.u229-lk:focus-visible{outline:2px solid #60A5FA;outline-offset:2px}
.u229-bw{position:absolute;right:20px;bottom:74px;width:150px;border-radius:12px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 20px 40px -14px rgba(0,0,0,.5);overflow:hidden;transform-origin:20% 100%;transform:scale(.4) translateY(30px);opacity:0;pointer-events:none;transition:transform .45s cubic-bezier(.3,1.5,.5,1),opacity .25s}
.u229.is-bw .u229-bw{transform:none;opacity:1}
.u229-bw header{display:flex;gap:4px;padding:6px 8px;background:var(--ux-surface-2)}
.u229-bw header i{width:6px;height:6px;border-radius:50%;background:var(--ux-surface-3)}
.u229-bw div{padding:10px}
.u229-bw b{display:block;font-size:12px;font-weight:900}
.u229-bw div i{display:block;height:5px;margin-top:6px;border-radius:3px;background:var(--ux-surface-3)}
.u229-bw div em{display:inline-block;margin-top:8px;padding:4px 8px;border-radius:999px;background:var(--ux-ink);color:var(--ux-surface);font-style:normal;font-size:8.5px;font-weight:850}
.u229-re{position:absolute;left:14px;bottom:16px;display:inline-flex;align-items:center;gap:6px;height:34px;padding:0 13px;border:0;border-radius:11px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink-2);font:inherit;font-size:11.5px;font-weight:850;cursor:pointer}
.u229-re svg{width:12px;height:12px}
.u229-re:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u229-cu,.u229-lk{animation:none}.u229-bw,.u229-pb i{transition:none}}
</style>
<div class="ux u229">
  <div class="u229-tm" role="log" aria-label="Terminal demo"><div class="u229-bar" aria-hidden="true"><i></i><i></i><i></i><span>~/projects</span></div><div class="u229-bd"></div></div>
  <div class="u229-bw" aria-hidden="true"><header><i></i><i></i><i></i></header><div><b>My first page</b><i style="width:90%"></i><i style="width:70%"></i><em>Get started</em></div></div>
  <button type="button" class="u229-re"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M10 4.6A4.2 4.2 0 1 0 10.4 7.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M10.5 1.8v3H7.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Replay</button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var bd = root.querySelector('.u229-bd'), re = root.querySelector('.u229-re'), bw = root.querySelector('.u229-bw');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var STEP = ['Downloading template', 'Installing packages', 'Writing config'];
  var SPIN = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏', gen = 0, started = false;
  function line(html) { var d = document.createElement('div'); d.className = 'u229-l'; d.innerHTML = html || ''; bd.appendChild(d); return d; }
  function wait(g, ms) { return new Promise(function (res, rej) { setTimeout(function () { if (g === gen && root.isConnected) res(); else rej(); }, rm ? 0 : ms); }); }
  function type(g, el, text) {
    return new Promise(function (res, rej) {
      var cu = document.createElement('span'); cu.className = 'u229-cu'; el.appendChild(cu); var i = 0;
      (function step() { if (g !== gen) { rej(); return; } if (i >= text.length || rm) { if (rm) cu.insertAdjacentText('beforebegin', text); cu.remove(); res(); return; } cu.insertAdjacentText('beforebegin', text[i++]); setTimeout(step, 28 + Math.random() * 50); })();
    });
  }
  function spin(g, el, label, ms) {
    return new Promise(function (res, rej) {
      el.innerHTML = '<span class="sp"></span> '; el.appendChild(document.createTextNode(label)); var sp = el.firstChild, k = 0, t0 = performance.now();
      (function f() { if (g !== gen) { rej(); return; } sp.textContent = SPIN[k++ % SPIN.length]; if (rm || performance.now() - t0 > ms) { el.innerHTML = '<span class="ok">✔</span> '; el.appendChild(document.createTextNode(label)); res(); return; } setTimeout(f, 80); })();
    });
  }
  function run() {
    var g = ++gen; bd.innerHTML = ''; root.classList.remove('is-bw'); started = true;
    var l1 = line('<span class="p">❯</span> ');
    wait(g, 300).then(function () { return type(g, l1, 'npx create-lucian@latest my-app'); })
      .then(function () { return wait(g, 250); })
      .then(function () {
        var pl = line('<span class="d">  </span><span class="u229-pb"><i></i></span><span class="d">0%</span>'), pi = pl.querySelector('i'), pt = pl.querySelectorAll('.d')[1];
        var chain = Promise.resolve();
        STEP.forEach(function (s, i) { chain = chain.then(function () { var l = line(); bd.insertBefore(l, pl); return spin(g, l, s, 520 + i * 160); }).then(function () { var p = Math.round((i + 1) / STEP.length * 100); pi.style.width = p + '%'; pt.textContent = p + '%'; }); });
        return chain.then(function () { pl.remove(); var d = line('<span class="d"></span>'); d.firstChild.textContent = '  Done · 4.2s'; });
      })
      .then(function () { return wait(g, 350); })
      .then(function () { var l = line('<span class="p">❯</span> '); return type(g, l, 'cd my-app && npm run dev'); })
      .then(function () { return wait(g, 450); })
      .then(function () { var l = line('<span class="ok">▲</span> '); l.appendChild(document.createTextNode('Ready on ')); var a = document.createElement('button'); a.type = 'button'; a.className = 'u229-lk'; a.textContent = 'http://localhost:3000'; a.addEventListener('click', function () { root.classList.toggle('is-bw'); }); l.appendChild(a); })
      .catch(function () {});
  }
  re.addEventListener('click', run);
  if ('IntersectionObserver' in window) { var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting && !started) { io.disconnect(); run(); } }); io.observe(root); } else run();
})();
</script>
--- Code end ---
