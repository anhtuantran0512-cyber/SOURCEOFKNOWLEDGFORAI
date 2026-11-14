---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/tag-input/"
title: "Tag Input"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Type a tag and press Enter or comma to commit it as a chip."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tag Input
Source: https://codefronts.com/components/css-input-fields/tag-input/

Type a tag and press Enter or comma to commit it as a chip. Backspace on an empty input removes the last chip — a polished pattern for filters and email recipients.
## HTML
```html
<label class="if-12">
  <span class="if-12-label">Tags</span>
  <span class="if-12-wrap" data-if-tags>
    <span class="if-12-list"></span>
    <input type="text" placeholder="Add a tag…" aria-label="Tags" />
  </span>
  <span class="if-12-help">Press <kbd>Enter</kbd> or <kbd>,</kbd> to add</span>
</label>
```
## CSS
```css
.if-12 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
  font-size: 11px;
  color: #b8b6d4;
}

.if-12-label {
  font-weight: 600;
}

.if-12-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 8px 10px;
  align-items: center;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.if-12-wrap:focus-within {
  border-color: #fb923c;
  box-shadow: 0 0 0 3px rgba(251, 146, 60, 0.15);
}

.if-12-list {
  display: contents;
}

.if-12-chip {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(251, 146, 60, 0.12);
  border: 1px solid rgba(251, 146, 60, 0.35);
  color: #fdba74;
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 99px;
  font-weight: 500;
}

.if-12-chip button {
  background: transparent;
  border: 0;
  padding: 0;
  color: inherit;
  cursor: pointer;
  font-size: 12px;
  line-height: 1;
  opacity: 0.7;
}

.if-12-chip button:hover {
  opacity: 1;
}

.if-12 input {
  flex: 1;
  min-width: 80px;
  background: transparent;
  border: 0;
  outline: none;
  color: #f0eeff;
  font-size: 14px;
  padding: 2px 0;
}

.if-12 input::placeholder {
  color: #b8b6d4;
}

.if-12-help {
  font-size: 10.5px;
  color: #b8b6d4;
}

.if-12-help kbd {
  display: inline-block;
  background: #2a2a36;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 4px;
  padding: 0 4px;
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
}
```

## JavaScript
```js
// Tag input — Enter/comma commits a chip, Backspace removes the last
document.querySelectorAll("[data-if-tags]").forEach(function (wrap) {
  var input = wrap.querySelector("input");
  var list = wrap.querySelector(".if-12-list");
  if (!input || !list) return;

  function addChip(value) {
    value = (value || "").trim();
    if (!value) return;
    var chip = document.createElement("span");
    chip.className = "if-12-chip";
    chip.textContent = value + " ";
    var x = document.createElement("button");
    x.type = "button";
    x.setAttribute("aria-label", "Remove tag " + value);
    x.textContent = "×";
    x.addEventListener("click", function () {
      chip.remove();
    });
    chip.appendChild(x);
    list.appendChild(chip);
  }

  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === ",") {
      e.preventDefault();
      addChip(input.value);
      input.value = "";
    } else if (e.key === "Backspace" && !input.value) {
      var last = list.querySelector(".if-12-chip:last-child");
      if (last) last.remove();
    }
  });
});
```
