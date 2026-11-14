---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/e-e-a-t-scorecard/"
title: "E-E-A-T Scorecard"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Google's quality evaluator framework — Experience, Expertise, Authoritativeness, Trustworthiness."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-E-A-T Scorecard
Source: https://codefronts.com/snippets/css-badges/e-e-a-t-scorecard/

Google's quality evaluator framework — Experience, Expertise, Authoritativeness, Trustworthiness. Composite score and a grade, with four animated bars showing per-dimension strength.
## HTML
```html
<div class="bdg-08-stage">
  <div class="bdg-08-card">
    <div class="bdg-08-top">
      <div class="bdg-08-composite">
        <div class="bdg-08-big-score">85</div>
        <div class="bdg-08-score-label">Composite · /100</div>
      </div>
      <div class="bdg-08-grade-block">
        <div class="bdg-08-grade">A</div>
        <div class="bdg-08-grade-label">Strong signal</div>
      </div>
    </div>
    <div class="bdg-08-bars">
      <div class="bdg-08-row">
        <div class="bdg-08-abbr" style="color:#3d7ebf">E</div>
        <div class="bdg-08-name">Experience</div>
        <div class="bdg-08-track"><div class="bdg-08-fill" style="background:#3d7ebf; --bdg-08-w: 82%"></div></div>
        <div class="bdg-08-val">82</div>
      </div>
      <div class="bdg-08-row">
        <div class="bdg-08-abbr" style="color:#1d8f4a">E</div>
        <div class="bdg-08-name">Expertise</div>
        <div class="bdg-08-track"><div class="bdg-08-fill" style="background:#1d8f4a; --bdg-08-w: 91%"></div></div>
        <div class="bdg-08-val">91</div>
      </div>
      <div class="bdg-08-row">
        <div class="bdg-08-abbr" style="color:#b8762d">A</div>
        <div class="bdg-08-name">Authoritativeness</div>
        <div class="bdg-08-track"><div class="bdg-08-fill" style="background:#b8762d; --bdg-08-w: 79%"></div></div>
        <div class="bdg-08-val">79</div>
      </div>
      <div class="bdg-08-row">
        <div class="bdg-08-abbr" style="color:#5b3aa0">T</div>
        <div class="bdg-08-name">Trustworthiness</div>
        <div class="bdg-08-track"><div class="bdg-08-fill" style="background:#5b3aa0; --bdg-08-w: 88%"></div></div>
        <div class="bdg-08-val">88</div>
      </div>
    </div>
    <div class="bdg-08-footer">
      <span>Evaluated May 2026</span>
      <span>Google Quality Rater Guidelines</span>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-08-stage {
  background: #fff;
  padding: 50px 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-08-card {
  background: #fff;
  border: 1.5px solid #e8e4da;
  border-radius: 6px;
  padding: 28px 28px 22px;
  width: 100%;
  max-width: 480px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
}

.bdg-08-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid #f0ece0;
}

.bdg-08-composite {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.bdg-08-big-score {
  font-family: Georgia, "Fraunces", serif;
  font-size: 72px;
  line-height: 0.85;
  font-weight: 300;
  font-style: italic;
  color: #1a1612;
  letter-spacing: -0.04em;
}

.bdg-08-score-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #aaa;
}

.bdg-08-grade-block {
  text-align: right;
}

.bdg-08-grade {
  font-family: Georgia, "Fraunces", serif;
  font-size: 48px;
  font-weight: 700;
  color: #1d8f4a;
  line-height: 1;
}

.bdg-08-grade-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #888;
  margin-top: 2px;
}

.bdg-08-bars {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.bdg-08-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.bdg-08-abbr {
  width: 12px;
  font-family: Georgia, "Fraunces", serif;
  font-weight: 700;
  font-size: 15px;
  flex-shrink: 0;
}

.bdg-08-name {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #4a4239;
  width: 120px;
  flex-shrink: 0;
}

.bdg-08-track {
  flex: 1;
  height: 6px;
  background: #f0ece0;
  border-radius: 3px;
  overflow: hidden;
}

.bdg-08-fill {
  height: 100%;
  border-radius: 3px;
  width: 0;
  animation: bdg-08-grow 1s cubic-bezier(0.4, 0, 0.2, 1) 0.4s forwards;
}

@keyframes bdg-08-grow {
  to {
    width: var(--bdg-08-w, 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-08-fill {
    animation: none;
    width: var(--bdg-08-w, 0);
  }
}

.bdg-08-val {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  color: #1a1612;
  width: 28px;
  text-align: right;
  flex-shrink: 0;
}

.bdg-08-footer {
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid #f0ece0;
  display: flex;
  justify-content: space-between;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
}
```
