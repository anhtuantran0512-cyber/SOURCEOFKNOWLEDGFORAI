---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-ai-model-selector-button-group-with-provider-badges-llm-model-picker/"
title: "CSS AI Model Selector Button Group with Provider Badges (LLM Model Picker)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "The model picker every AI product now ships: a selectable list of LLMs — each row a button with a provider badge, model name, capability tags and a…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS AI Model Selector Button Group with Provider Badges (LLM Model Picker)
Source: https://codefronts.com/components/css-button-groups/css-ai-model-selector-button-group-with-provider-badges-llm-model-picker/

The model picker every AI product now ships: a selectable list of LLMs — each row a button with a provider badge, model name, capability tags and a context-window hint, one row selected with a check. The definitive 'CSS AI model selector button group with provider badges' for chat apps and AI dashboards — radio-driven, keyboard-friendly and dark-mode ready.
## HTML
```html
<section class="btn-11" aria-label="AI model selector demo">
  <div class="btn-11__panel">
    <p class="btn-11__eyebrow">Model</p>
    <h3 class="btn-11__title">Select a model</h3>
    <div class="btn-11__list" role="radiogroup" aria-label="AI model">
      <input type="radio" name="btn-11" id="btn-11-1" class="btn-11__in" checked>
      <label for="btn-11-1" class="btn-11__row" style="--brand:#10a37f">
        <span class="btn-11__badge">AI</span>
        <span class="btn-11__meta"><span class="btn-11__name">GPT-class Turbo</span><span class="btn-11__chips"><i>Vision</i><i>Tools</i></span></span>
        <span class="btn-11__ctx">128K ctx</span>
        <span class="btn-11__check" aria-hidden="true"></span>
      </label>
      <input type="radio" name="btn-11" id="btn-11-2" class="btn-11__in">
      <label for="btn-11-2" class="btn-11__row" style="--brand:#d97757">
        <span class="btn-11__badge">CL</span>
        <span class="btn-11__meta"><span class="btn-11__name">Claude-class Opus</span><span class="btn-11__chips"><i>Vision</i><i>200K</i></span></span>
        <span class="btn-11__ctx">200K ctx</span>
        <span class="btn-11__check" aria-hidden="true"></span>
      </label>
      <input type="radio" name="btn-11" id="btn-11-3" class="btn-11__in">
      <label for="btn-11-3" class="btn-11__row" style="--brand:#4285f4">
        <span class="btn-11__badge">GM</span>
        <span class="btn-11__meta"><span class="btn-11__name">Gemini-class Pro</span><span class="btn-11__chips"><i>Multimodal</i><i>1M</i></span></span>
        <span class="btn-11__ctx">1M ctx</span>
        <span class="btn-11__check" aria-hidden="true"></span>
      </label>
      <input type="radio" name="btn-11" id="btn-11-4" class="btn-11__in">
      <label for="btn-11-4" class="btn-11__row" style="--brand:#8e6fe6">
        <span class="btn-11__badge">LL</span>
        <span class="btn-11__meta"><span class="btn-11__name">Llama-class 70B</span><span class="btn-11__chips"><i>Open</i><i>Fast</i></span></span>
        <span class="btn-11__ctx">64K ctx</span>
        <span class="btn-11__check" aria-hidden="true"></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-11,
.btn-11 *,
.btn-11 *::before,
.btn-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-11 {
  --accent: oklch(0.7 0.15 230);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(165deg,#0c1220,#0a0f1a);
  padding: 44px 20px;
}

.btn-11__panel {
  width: min(520px,100%);
  background: #111827;
  border: 1px solid #1f2b40;
  border-radius: 20px;
  padding: 26px 24px 28px;
  box-shadow: 0 34px 80px -40px rgba(0,0,0,.9);
}

.btn-11__eyebrow {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.btn-11__title {
  font-size: 23px;
  font-weight: 800;
  color: #eef3fb;
  letter-spacing: -.02em;
  margin: 5px 0 18px;
}

.btn-11__list {
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.btn-11__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-11__row {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 13px 15px;
  background: #0e1524;
  border: 1.5px solid #1e2a3f;
  border-radius: 14px;
  cursor: pointer;
  transition: border-color .18s,background .18s;
}

.btn-11__row:hover {
  border-color: #334563;
}

.btn-11__badge {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 800;
  color: #fff;
  background: var(--brand);
  box-shadow: 0 4px 14px -4px var(--brand);
}

.btn-11__meta {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.btn-11__name {
  font-size: 15px;
  font-weight: 700;
  color: #e8eefa;
}

.btn-11__chips {
  display: flex;
  gap: 6px;
}

.btn-11__chips i {
  font-style: normal;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .02em;
  color: #9fb2cf;
  background: #1a2438;
  padding: 3px 7px;
  border-radius: 6px;
}

.btn-11__ctx {
  margin-left: auto;
  font-size: 12.5px;
  font-weight: 650;
  color: #7d90ad;
  white-space: nowrap;
}

.btn-11__check {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid #33455f;
  flex: none;
  position: relative;
  transition: border-color .18s,background .18s;
  scale: .8;
  opacity: .5;
}

.btn-11__check::after {
  content: "";
  position: absolute;
  left: 6px;
  top: 2.5px;
  width: 6px;
  height: 11px;
  border-right: 2.5px solid #fff;
  border-bottom: 2.5px solid #fff;
  rotate: 45deg;
  opacity: 0;
  transition: opacity .18s;
}

.btn-11__in:checked + .btn-11__row {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 12%,#0e1524);
}

.btn-11__in:checked + .btn-11__row .btn-11__check {
  border-color: var(--accent);
  background: var(--accent);
  scale: 1;
  opacity: 1;
}

.btn-11__in:checked + .btn-11__row .btn-11__check::after {
  opacity: 1;
}

.btn-11__in:focus-visible + .btn-11__row {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-11__row,
    .btn-11__check,
    .btn-11__check::after {
    transition: none;
  }
}
```
