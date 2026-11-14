---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/inline-edit/"
title: "Inline Edit"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Click-to-edit text that swaps between a static value and an editable input."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Edit
Source: https://codefronts.com/components/css-input-fields/inline-edit/

Click-to-edit text that swaps between a static value and an editable input. Saves on Enter, cancels on Escape, blurs to commit — the canonical pattern from Notion and Linear.
## HTML
```html
<label class="if-23">
  <span class="if-23-label">Project name</span>
  <span class="if-23-wrap" data-if-23 data-value="Aurora Dashboard">
    <span class="if-23-display" tabindex="0" role="button" aria-label="Edit project name"
      >Aurora Dashboard</span
    >
    <input class="if-23-input" type="text" value="Aurora Dashboard" hidden />
    <span class="if-23-pencil" aria-hidden="true">✎</span>
  </span>
</label>
```
## CSS
```css
.if-23 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-23-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-23-wrap {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: transparent;
  border: 1px dashed transparent;
  border-radius: 8px;
  cursor: text;
  transition: background 0.15s, border-color 0.15s;
}

.if-23-wrap:hover {
  background: rgba(124, 108, 255, 0.06);
  border-color: rgba(124, 108, 255, 0.2);
}

.if-23-display,
.if-23-input {
  font: 600 14px/1.3 system-ui, sans-serif;
  color: #f0eeff;
  flex: 1;
  min-width: 0;
}

.if-23-display {
  outline: none;
}

.if-23-input {
  border: 0;
  outline: none;
  background: transparent;
  padding: 0;
}

.if-23-pencil {
  font-size: 12px;
  color: #7a7899;
  opacity: 0;
  transition: opacity 0.15s;
}

.if-23-wrap:hover .if-23-pencil {
  opacity: 1;
}

.if-23-wrap.is-editing {
  background: #1a1a22;
  border-color: #7c6cff;
  border-style: solid;
}

.if-23-wrap.is-editing .if-23-pencil {
  display: none;
}
```

## JavaScript
```js
// Inline Edit — click to edit, Enter saves, Escape cancels, blur commits
document.querySelectorAll("[data-if-23]").forEach(function (wrap) {
  var display = wrap.querySelector(".if-23-display");
  var input = wrap.querySelector(".if-23-input");

  function enter() {
    wrap.classList.add("is-editing");
    display.hidden = true;
    input.hidden = false;
    input.value = display.textContent;
    input.focus();
    input.select();
  }
  function commit() {
    var v = input.value.trim();
    if (v) {
      display.textContent = v;
      wrap.dataset.value = v;
    } else {
      input.value = display.textContent;
    }
    exit();
  }
  function cancel() {
    input.value = display.textContent;
    exit();
  }
  function exit() {
    wrap.classList.remove("is-editing");
    input.hidden = true;
    display.hidden = false;
  }

  display.addEventListener("click", enter);
  display.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      enter();
    }
  });
  input.addEventListener("blur", commit);
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      commit();
    }
    if (e.key === "Escape") {
      e.preventDefault();
      cancel();
    }
  });
});
```
