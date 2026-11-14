---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/email-with-suggestions/"
title: "Email with Suggestions"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "When the user types `@`, common email domains are suggested in a keyboard-navigable dropdown."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Email with Suggestions
Source: https://codefronts.com/components/css-input-fields/email-with-suggestions/

When the user types `@`, common email domains are suggested in a keyboard-navigable dropdown. `aria-controls` + `aria-expanded` + `role="listbox"` make it a proper combobox.
## HTML
```html
<label class="if-21">
  <span class="if-21-label">Work email</span>
  <span class="if-21-wrap">
    <input
      id="if-21-input"
      type="email"
      name="email"
      autocomplete="email"
      placeholder="[email protected]"
      aria-controls="if-21-list"
      aria-expanded="false"
      aria-autocomplete="list"
    />
    <ul id="if-21-list" class="if-21-list" role="listbox" hidden></ul>
  </span>
</label>
```
## CSS
```css
.if-21 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-21-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-21-wrap {
  position: relative;
  display: block;
}

.if-21 input {
  width: 100%;
  box-sizing: border-box;
  padding: 12px 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  color: #f0eeff;
  font: 500 14px/1 system-ui, sans-serif;
  outline: none;
  transition: border-color 0.2s, border-radius 0.15s;
}

.if-21 input:focus {
  border-color: #2eb88a;
}

.if-21 input[aria-expanded="true"] {
  border-radius: 10px 10px 0 0;
  border-bottom-color: transparent;
}

.if-21-list {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin: 0;
  padding: 4px;
  list-style: none;
  background: #1a1a22;
  border: 1px solid #2eb88a;
  border-top: 0;
  border-radius: 0 0 10px 10px;
  z-index: 10;
  max-height: 180px;
  overflow-y: auto;
}

.if-21-list li {
  padding: 7px 10px;
  font: 500 13px/1.2 system-ui, sans-serif;
  color: #cbd5e1;
  cursor: pointer;
  border-radius: 6px;
}

.if-21-list li[aria-selected="true"],
.if-21-list li:hover {
  background: rgba(46, 184, 138, 0.15);
  color: #fff;
}

.if-21-list li b {
  color: #2eb88a;
  font-weight: 600;
}
```

## JavaScript
```js
// Email Suggestions — show common domains after the user types '@'
(function () {
  var input = document.getElementById("if-21-input");
  var list = document.getElementById("if-21-list");
  if (!input || !list) return;
  var DOMAINS = ["gmail.com", "outlook.com", "icloud.com", "protonmail.com", "fastmail.com"];
  var idx = -1;

  function close() {
    list.hidden = true;
    input.setAttribute("aria-expanded", "false");
    idx = -1;
  }
  function render(local) {
    list.innerHTML = "";
    DOMAINS.forEach(function (d) {
      var li = document.createElement("li");
      li.setAttribute("role", "option");
      li.innerHTML = (local || "") + "<b>@" + d + "</b>";
      list.appendChild(li);
    });
  }
  function open(local) {
    render(local);
    list.hidden = false;
    input.setAttribute("aria-expanded", "true");
  }
  function select(n) {
    var items = list.querySelectorAll("li");
    items.forEach(function (li) {
      li.removeAttribute("aria-selected");
    });
    idx = (n + items.length) % items.length;
    items[idx].setAttribute("aria-selected", "true");
  }

  input.addEventListener("input", function () {
    var v = input.value,
      at = v.indexOf("@");
    if (at >= 0) open(v.substring(0, at + 1));
    else close();
  });
  input.addEventListener("blur", function () {
    setTimeout(close, 150);
  });
  input.addEventListener("keydown", function (e) {
    if (list.hidden) return;
    var items = list.querySelectorAll("li");
    if (e.key === "ArrowDown") {
      e.preventDefault();
      select(idx + 1);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      select(idx - 1);
    } else if (e.key === "Escape") {
      close();
    } else if (e.key === "Enter" && idx >= 0) {
      e.preventDefault();
      input.value = items[idx].textContent;
      close();
    }
  });
  list.addEventListener("mousedown", function (e) {
    var li = e.target.closest('li[role="option"]');
    if (li) {
      input.value = li.textContent;
      close();
    }
  });
})();
```
