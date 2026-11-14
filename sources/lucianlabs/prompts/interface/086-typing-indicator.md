---
source: "lucianlabs"
id: "086"
title: "Streaming AI answer"
category: "Loading & Progress"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#086"
tags: ["typing", "streaming", "ai", "cursor", "stop"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Streaming AI answer (086, Loading & Progress)
[What it does] Send a question and three dots bounce to show it’s thinking, then the answer flows out word by word, each one floating up slightly. A cursor blinks at the end, and the stop button turns into “Regenerate” once it finishes.
[How to use it] Tap a suggested question below. Cut the answer off with “Stop” while it streams, or press “Regenerate” after it ends

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
<!-- Lucian UX/UI Prompt #086 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#086 -->
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
.u086{position:relative;width:340px;height:440px;display:flex;flex-direction:column;border-radius:30px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u086-log{flex:1;display:flex;flex-direction:column;gap:12px;padding:18px 16px 8px;overflow:hidden}
.u086-q{align-self:flex-end;max-width:80%;padding:10px 14px;border-radius:18px 18px 6px 18px;background:var(--ux-surface-2);font-size:14px;font-weight:650;line-height:1.45;animation:u086-pop .45s var(--ux-spring)}
@keyframes u086-pop{from{opacity:0;transform:translateY(10px) scale(.95)}}
.u086-a{display:flex;gap:10px}
.u086-av{width:30px;height:30px;flex:none;border-radius:10px;background:var(--ux-grad);display:grid;place-items:center}
.u086-av::after{content:"";width:12px;height:12px;border-radius:3px;background:#fff;transform:rotate(45deg)}
.u086.is-gen .u086-av{animation:u086-glow 1.6s ease-in-out infinite}
@keyframes u086-glow{50%{box-shadow:0 0 0 5px var(--ux-accent-soft)}}
.u086-body{flex:1;min-width:0;font-size:14px;line-height:1.65;color:var(--ux-ink)}
.u086-body p{margin:0 0 8px}
.u086-body ol{margin:0 0 8px;padding-left:18px}
.u086-body b{font-weight:800}
.u086-w{animation:u086-w .45s var(--ux-ease) backwards}
@keyframes u086-w{from{opacity:0;filter:blur(3px)}}
.u086-caret{display:inline-block;width:8px;height:15px;margin-left:2px;border-radius:2px;vertical-align:-2px;background:var(--ux-accent);animation:u086-c 1s steps(1) infinite}
@keyframes u086-c{50%{opacity:0}}
.u086-dots{display:inline-flex;gap:4px;padding:10px 12px;border-radius:14px;background:var(--ux-surface-2)}
.u086-dots i{width:7px;height:7px;border-radius:50%;background:var(--ux-ink-3);animation:u086-b 1.1s ease-in-out infinite}
.u086-dots i:nth-child(2){animation-delay:.15s}.u086-dots i:nth-child(3){animation-delay:.3s}
@keyframes u086-b{0%,60%,100%{transform:none;opacity:.45}30%{transform:translateY(-5px);opacity:1}}
.u086-stop{display:block;margin-top:4px;font-size:12px;font-weight:700;color:var(--ux-ink-3)}
.u086-sug{display:flex;flex-wrap:wrap;gap:6px;padding:0 16px 10px}
.u086-sug button{height:34px;padding:0 12px;border:0;border-radius:999px;background:var(--ux-surface-2);font-size:12.5px;font-weight:700;color:var(--ux-ink-2);transition:background-color .2s,transform .3s var(--ux-spring)}
.u086-sug button:hover{background:var(--ux-surface-3);color:var(--ux-ink)}
.u086-sug button:active{transform:scale(.95)}
.u086-sug button:disabled{opacity:.4;cursor:default}
.u086-bar{display:flex;align-items:center;gap:8px;margin:0 12px 12px;padding:6px 6px 6px 16px;border-radius:22px;box-shadow:inset 0 0 0 1.5px var(--ux-line-2);font-size:13.5px;color:var(--ux-ink-3)}
.u086-bar span{flex:1}
.u086-ctl{height:36px;padding:0 14px;border:0;border-radius:18px;display:inline-flex;align-items:center;gap:6px;background:var(--ux-ink);color:var(--ux-page);font-size:13px;font-weight:750;transition:transform .3s var(--ux-spring),opacity .3s}
.u086-ctl:active{transform:scale(.94)}
.u086-ctl[aria-disabled="true"]{opacity:.35}
.u086-ctl i{width:10px;height:10px;border-radius:2px;background:currentColor}
.u086-ctl svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.u086-sug button:focus-visible,.u086-ctl:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
</style>
<div class="ux u086">
  <div class="u086-log" aria-live="polite"></div>
  <div class="u086-sug" role="group" aria-label="Suggested questions"><button type="button">Ideas to improve onboarding</button><button type="button">What’s a good button transition time?</button></div>
  <div class="u086-bar"><span>Ask anything</span><button class="u086-ctl" type="button" aria-disabled="true"><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M7 11.5V2.5M3 6.5l4-4 4 4"/></svg>Send</button></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var log = root.querySelector('.u086-log'), sugs = root.querySelectorAll('.u086-sug button'), ctl = root.querySelector('.u086-ctl');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var A = {
    'Ideas to improve onboarding': [['p', 'Three things are worth trying first.'], ['li', 'Let people <b>start on the first screen</b> and cut the explaining'], ['li', 'Show the <b>steps left</b> with a progress bar'], ['li', 'Keep the skip button <b>in the same place</b>'], ['p', 'The first one cuts drop-off the most.']],
    'What’s a good button transition time?': [['p', 'For most cases <b>150–250ms</b> is enough.'], ['li', 'Start press feedback <b>within 100ms</b>'], ['li', 'Large moving panels: <b>around 300ms</b>'], ['p', 'Shorter feels faster, but too short and the change disappears.']]
  };
  var ts = [], state = 'idle', last = null, stopFn = null;
  function clear() { ts.forEach(clearTimeout); ts = []; }
  function later(fn, ms) { ts.push(setTimeout(function () { if (root.isConnected) fn(); }, ms)); }
  function setCtl(s) {
    state = s;
    root.classList.toggle('is-gen', s === 'gen');
    if (s === 'gen') ctl.innerHTML = '<i aria-hidden="true"></i>Stop';
    else if (s === 'done') ctl.innerHTML = '<svg viewBox="0 0 14 14" aria-hidden="true"><path d="M11.5 7a4.5 4.5 0 1 1-1.3-3.2M11.5 2v2.5H9"/></svg>Regenerate';
    ctl.setAttribute('aria-disabled', String(s === 'idle'));
    sugs.forEach(function (b) { b.disabled = s === 'gen'; });
  }
  function ask(q) {
    clear(); last = q;
    log.innerHTML = "";
    var qe = document.createElement('div'); qe.className = 'u086-q'; qe.textContent = q; log.appendChild(qe);
    var a = document.createElement('div'); a.className = 'u086-a';
    a.innerHTML = '<span class="u086-av" aria-hidden="true"></span><div class="u086-body"><span class="u086-dots" aria-label="Thinking"><i></i><i></i><i></i></span></div>';
    log.appendChild(a);
    var body = a.querySelector('.u086-body');
    setCtl('gen');
    var tokens = [];
    A[q].forEach(function (blk) {
      tokens.push({ open: blk[0] });
      blk[1].split(/(<b>.*?<\/b>|\s+)/).filter(Boolean).forEach(function (t) { tokens.push({ t: t }); });
    });
    var i = 0, el = null, ol = null, caret = document.createElement('span');
    caret.className = 'u086-caret'; caret.setAttribute('aria-hidden', 'true');
    stopFn = function () { clear(); caret.remove(); var s = document.createElement('span'); s.className = 'u086-stop'; s.textContent = '— Stopped here'; body.appendChild(s); setCtl('done'); };
    later(function () {
      body.innerHTML = '';
      (function tick() {
        var n = rm ? tokens.length : 1 + Math.round(Math.random());
        while (n-- > 0 && i < tokens.length) {
          var tk = tokens[i++];
          if (tk.open === 'p') { el = document.createElement('p'); body.appendChild(el); ol = null; }
          else if (tk.open === 'li') { if (!ol) { ol = document.createElement('ol'); body.appendChild(ol); } el = document.createElement('li'); ol.appendChild(el); }
          else if (/^\s+$/.test(tk.t)) el.appendChild(document.createTextNode(' '));
          else { var w = document.createElement('span'); w.className = 'u086-w'; w.innerHTML = tk.t; el.appendChild(w); }
        }
        if (el) el.appendChild(caret);
        if (i < tokens.length) later(tick, 45 + Math.random() * 60);
        else later(function () { caret.remove(); setCtl('done'); }, 600);
      })();
    }, rm ? 200 : 1200);
  }
  sugs.forEach(function (b) { b.addEventListener('click', function () { if (state !== 'gen') ask(b.textContent); }); });
  ctl.addEventListener('click', function () {
    if (state === 'gen' && stopFn) stopFn();
    else if (state === 'done' && last) ask(last);
  });
  ask('Ideas to improve onboarding');
})();
</script>
--- Code end ---
