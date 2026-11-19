import sanitizeHtml from "sanitize-html";
import postcss from "postcss";
export const MAX_HTML = 48000;
import { looksSensitive } from "../src/sensitive.js";
export { looksSensitive };
export function cleanPage(input) {
  if (
    typeof input !== "string" ||
    input.length > MAX_HTML ||
    looksSensitive(input)
  )
    throw Error("Không thể nhận mã nguồn này.");
  const title = sanitizeHtml(
    input.match(/<title[^>]*>([^<]*)<\/title>/i)?.[1] || "Dự án F‑FORUM",
    { allowedTags: [], allowedAttributes: {} },
  ).slice(0, 100);
  const cssInput = [...input.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)]
    .map((m) => m[1])
    .join("\n");
  let css = "";
  try {
    const tree = postcss.parse(cssInput);
    tree.walkAtRules((rule) => {
      if (
        !["media", "supports", "keyframes"].includes(rule.name.toLowerCase()) ||
        /[<\\]/.test(rule.params)
      )
        rule.remove();
    });
    tree.walkDecls((d) => {
      if (
        /[<\\]|url\s*\(|image-set\s*\(|expression\s*\(|@import/i.test(
          d.value,
        ) ||
        /[<\\]/.test(d.prop)
      )
        d.remove();
    });
    tree.walkRules((r) => {
      if (/[<\\]/.test(r.selector)) r.remove();
    });
    tree.walkComments((c) => c.remove());
    css = tree.toString();
    if (/[<\\]|url\s*\(|image-set\s*\(/i.test(css)) css = "";
  } catch {
    /* Invalid styles are not executable. */
  }
  const body = sanitizeHtml(
    input.replace(/<head\b[^>]*>[\s\S]*?<\/head>/gi, ""),
    {
      allowedTags: [
        "main",
        "article",
        "section",
        "header",
        "footer",
        "nav",
        "aside",
        "h1",
        "h2",
        "h3",
        "h4",
        "p",
        "div",
        "span",
        "ul",
        "ol",
        "li",
        "strong",
        "em",
        "small",
        "figure",
        "figcaption",
        "blockquote",
        "details",
        "summary",
        "table",
        "thead",
        "tbody",
        "tr",
        "th",
        "td",
        "br",
        "hr",
        "code",
        "pre",
        "a",
        "button",
        "label",
        "time",
      ],
      allowedAttributes: {
        "*": ["class", "id", "title", "aria-label", "role", "lang", "dir"],
        a: ["href"],
        button: ["type"],
        details: ["open"],
      },
      transformTags: {
        a: (t, a) => ({
          tagName: t,
          attribs: {
            ...a,
            href: /^#[a-z\w-]+$/i.test(a.href || "") ? a.href : "",
          },
        }),
        button: (t, a) => ({ tagName: t, attribs: { ...a, type: "button" } }),
      },
      nonTextTags: [
        "script",
        "style",
        "textarea",
        "object",
        "iframe",
        "noscript",
        "template",
      ],
    },
  );
  if (!body.trim()) throw Error("Mã nguồn chưa có nội dung để xem.");
  return `<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">\n<title>${title}</title>\n<style>\n${css}\n</style>\n</head>\n<body>\n${body}\n</body>\n</html>`;
}
