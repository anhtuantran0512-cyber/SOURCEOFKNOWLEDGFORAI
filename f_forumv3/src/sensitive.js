const secretPattern =
  /-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----|\b(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,})\b/;
export function looksSensitive(text) {
  return (
    secretPattern.test(text) ||
    /\b(?:api[_-]?key|password|client[_-]?secret|access[_-]?token)\s*[:=]\s*['"]?[^\s'"<>]{12,}/i.test(
      text,
    )
  );
}
