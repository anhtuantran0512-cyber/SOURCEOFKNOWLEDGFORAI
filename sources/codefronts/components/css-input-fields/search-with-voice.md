---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/search-with-voice/"
title: "Search with Voice"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Search field with a microphone trigger that toggles a recording state — pulses a halo while \"listening\"."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Search with Voice
Source: https://codefronts.com/components/css-input-fields/search-with-voice/

Search field with a microphone trigger that toggles a recording state — pulses a halo while "listening". Real <input type="search"> so AT announces it as a search field.
## HTML
```html
<form class="if-20" role="search" autocomplete="off">
  <label class="if-20-label" for="if-20-input">Voice search</label>
  <span class="if-20-wrap">
    <svg viewBox="0 0 24 24" aria-hidden="true" class="if-20-glass">
      <circle cx="11" cy="11" r="7" />
      <path d="m20 20-3.5-3.5" />
    </svg>
    <input
      id="if-20-input"
      type="search"
      name="q"
      inputmode="search"
      placeholder="Speak or type to search..."
    />
    <button
      type="button"
      class="if-20-mic"
      aria-label="Start voice input"
      aria-pressed="false"
      data-if-20
    >
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <rect x="9" y="3" width="6" height="11" rx="3" />
        <path d="M5 11a7 7 0 0 0 14 0M12 18v3" />
      </svg>
    </button>
  </span>
</form>
```
## CSS
```css
.if-20 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 320px;
}

.if-20-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-20-wrap {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 4px 4px 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  transition: border-color 0.2s;
}

.if-20-wrap:focus-within {
  border-color: #ff6c8a;
}

.if-20-glass {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
  fill: none;
  stroke: #6b6987;
  stroke-width: 2;
  stroke-linecap: round;
}

.if-20 input {
  flex: 1;
  min-width: 0;
  padding: 8px 0;
  border: 0;
  outline: none;
  background: transparent;
  color: #f0eeff;
  font: 500 14px/1 system-ui, sans-serif;
}

.if-20 input::placeholder {
  color: #b8b6d4;
}

.if-20-mic {
  width: 36px;
  height: 36px;
  flex-shrink: 0;
  border: 0;
  cursor: pointer;
  background: transparent;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: background 0.2s;
}

.if-20-mic:hover {
  background: rgba(255, 108, 138, 0.1);
}

.if-20-mic svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: #a78bfa;
  stroke-width: 2;
  stroke-linecap: round;
}

.if-20-mic[aria-pressed="true"] svg {
  stroke: #ff6c8a;
}

.if-20-mic[aria-pressed="true"]::after {
  content: "";
  position: absolute;
  inset: 4px;
  border-radius: 6px;
  border: 1.5px solid #ff6c8a;
  animation: if-20-pulse 1.2s ease-out infinite;
}

@keyframes if-20-pulse {
  0% {
    transform: scale(0.8);
    opacity: 1;
  }

  100% {
    transform: scale(1.4);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .if-20-mic[aria-pressed="true"]::after {
    animation: none !important;
  }
}
```

## JavaScript
```js
// Voice button — toggle aria-pressed (mock recording state for the demo)
document.querySelectorAll("[data-if-20]").forEach(function (btn) {
  btn.addEventListener("click", function () {
    var on = btn.getAttribute("aria-pressed") === "true";
    btn.setAttribute("aria-pressed", on ? "false" : "true");
    btn.setAttribute("aria-label", on ? "Start voice input" : "Stop voice input");
    // Hook real Web Speech API here if you want actual voice input:
    // const rec = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  });
});
```
