---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/glossary-word-card/"
title: "Glossary Word Card"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "Dotted-underlined words in a paragraph that pop out a rich dictionary card on hover — part-of-speech tag, headword, IPA pronunciation, etymology, italic…"
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glossary Word Card
Source: https://codefronts.com/snippets/css-tooltips/glossary-word-card/

Dotted-underlined words in a paragraph that pop out a rich dictionary card on hover — part-of-speech tag, headword, IPA pronunciation, etymology, italic definition, usage quotation, and a row of synonym pills. Built for longform articles, language-learning sites, encyclopedias.
## HTML
```html
<div class="tp-07">
  <div class="tp-07__inner">
    <p class="tp-07__text">
      There is a word for the smell of rain on dry earth —
      <span class="tp-07__t">
        <span class="tp-07__word">petrichor</span>
        <span class="tp-07__tip">
          <span class="tp-07__top">
            <span class="tp-07__pos">noun · meteorology</span>
            <span class="tp-07__head">petrichor</span>
            <span class="tp-07__ipa">/ˈpɛtrɪkɔːr/</span>
          </span>
          <span class="tp-07__origin"><strong>Origin:</strong> Greek <em>petra</em> (stone) + <em>ichor</em> (the ethereal fluid said to flow through the veins of gods). Coined 1964 by Bear &amp; Thomas.</span>
          <span class="tp-07__def">The pleasant, earthy scent that arises when rain falls on dry soil, produced by geosmin released from actinobacteria.</span>
          <span class="tp-07__ex">
            <span class="tp-07__ex-label">In use</span>
            <span class="tp-07__ex-quote">"The petrichor that rose from the cracked earth was the first sign that the long drought had broken."</span>
          </span>
          <span class="tp-07__syn">
            <span class="tp-07__syn-pill">geosmin</span>
            <span class="tp-07__syn-pill">earthy scent</span>
            <span class="tp-07__syn-pill">rain smell</span>
          </span>
        </span>
      </span>
      — a sensation so specific it once had no name. Equally unnamed was
      <span class="tp-07__t">
        <span class="tp-07__word">sonder</span>
        <span class="tp-07__tip">
          <span class="tp-07__top">
            <span class="tp-07__pos">noun · neologism</span>
            <span class="tp-07__head">sonder</span>
            <span class="tp-07__ipa">/ˈsɒndər/</span>
          </span>
          <span class="tp-07__origin"><strong>Origin:</strong> Coined by John Koenig in <em>The Dictionary of Obscure Sorrows</em> (2012). Likely influenced by French <em>sonder</em> (to probe, to fathom).</span>
          <span class="tp-07__def">The sudden realization that every passerby is living a life as vivid and complex as one's own — filled with ambitions, fears, and an intricate private world.</span>
          <span class="tp-07__ex">
            <span class="tp-07__ex-label">In use</span>
            <span class="tp-07__ex-quote">"Staring out the train window, she was struck by sonder — each lit window a whole life she'd never know."</span>
          </span>
          <span class="tp-07__syn">
            <span class="tp-07__syn-pill">empathy</span>
            <span class="tp-07__syn-pill">weltanschauung</span>
          </span>
        </span>
      </span>,
      the act of registering that strangers have entire interior worlds. We live in
      <span class="tp-07__t">
        <span class="tp-07__word">liminal</span>
        <span class="tp-07__tip">
          <span class="tp-07__top">
            <span class="tp-07__pos">adjective · anthropology</span>
            <span class="tp-07__head">liminal</span>
            <span class="tp-07__ipa">/ˈlɪmɪnəl/</span>
          </span>
          <span class="tp-07__origin"><strong>Origin:</strong> Latin <em>limen</em> (threshold). Popularised by anthropologist Arnold van Gennep (1909) to describe transitional ritual phases.</span>
          <span class="tp-07__def">Occupying a position at, or on both sides of, a threshold or boundary; relating to a transitional or initial stage of a process.</span>
          <span class="tp-07__ex">
            <span class="tp-07__ex-label">In use</span>
            <span class="tp-07__ex-quote">"The airport is the most liminal of spaces — everyone passing through on the way to somewhere else."</span>
          </span>
          <span class="tp-07__syn">
            <span class="tp-07__syn-pill">transitional</span>
            <span class="tp-07__syn-pill">threshold</span>
            <span class="tp-07__syn-pill">interstitial</span>
          </span>
        </span>
      </span>
      spaces more than we realise.
    </p>
  </div>
</div>
```
## CSS
```css
.tp-07 {
  width: 100%;
  min-height: 100vh;
  background: #fdf9f3;
  /* Top room for the dictionary card (~280px tall) popping up from
       dotted-underlined words. Glossary words can be anywhere on the
       line, so generous top is the safest choice. */
  padding: 300px 28px 40px;
  font-family: Georgia, serif;
}

.tp-07__inner {
  max-width: 560px;
  margin: 0 auto;
}

.tp-07__text {
  font-size: 18px;
  line-height: 1.85;
  color: #2c2416;
  margin: 0;
}

.tp-07__t {
  position: relative;
  display: inline-block;
}

.tp-07__word {
  cursor: help;
  border-bottom: 1.5px dotted #a08050;
  color: #6a4820;
  transition: color .15s, border-color .15s;
}

.tp-07__t:hover .tp-07__word {
  color: #3a2010;
  border-bottom-color: #3a2010;
}

.tp-07__tip {
  position: absolute;
  bottom: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  width: 320px;
  background: #fff;
  border-radius: 10px;
  border: 1px solid rgba(160, 128, 80, 0.2);
  box-shadow: 0 8px 36px rgba(60, 40, 10, 0.13), 0 2px 8px rgba(60, 40, 10, 0.06);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  z-index: 30;
  overflow: hidden;
  font-family: Georgia, serif;
  text-align: left;
  display: block;
  white-space: normal;
}

.tp-07__t:hover .tp-07__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-07__top {
  display: block;
  padding: 16px 18px 12px;
  background: #faf6ef;
  border-bottom: 1px solid rgba(160, 128, 80, 0.12);
}

.tp-07__pos {
  display: block;
  font-size: 10px;
  font-family: 'Inter', system-ui, sans-serif;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #b09060;
  margin-bottom: 5px;
}

.tp-07__head {
  display: block;
  font-size: 24px;
  font-weight: 500;
  color: #1a1008;
  line-height: 1;
  margin-bottom: 4px;
}

.tp-07__ipa {
  display: block;
  font-size: 12px;
  color: #a09070;
  font-style: italic;
}

.tp-07__origin {
  display: block;
  padding: 11px 18px;
  border-bottom: 1px solid rgba(160, 128, 80, 0.1);
  font-size: 11px;
  font-family: 'Inter', system-ui, sans-serif;
  color: #9a8060;
  line-height: 1.5;
}

.tp-07__origin strong {
  color: #6a5030;
  font-weight: 500;
}

.tp-07__def {
  display: block;
  padding: 13px 18px;
  font-size: 13px;
  color: #3c2c14;
  line-height: 1.65;
  border-bottom: 1px solid rgba(160, 128, 80, 0.1);
  font-style: italic;
}

.tp-07__ex {
  display: block;
  padding: 11px 18px 13px;
  font-size: 12px;
  font-family: 'Inter', system-ui, sans-serif;
  color: #8a7050;
}

.tp-07__ex-label {
  display: block;
  font-size: 9px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #c0a878;
  margin-bottom: 5px;
}

.tp-07__ex-quote {
  display: block;
  color: #5a4020;
  line-height: 1.5;
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 13px;
}

.tp-07__syn {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  padding: 9px 18px 13px;
  border-top: 1px solid rgba(160, 128, 80, 0.1);
}

.tp-07__syn-pill {
  font-size: 10px;
  font-family: 'Inter', system-ui, sans-serif;
  padding: 3px 8px;
  border-radius: 20px;
  background: rgba(160, 128, 80, 0.08);
  color: #8a6840;
  border: 1px solid rgba(160, 128, 80, 0.18);
}
```
