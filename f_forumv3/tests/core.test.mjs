import { test } from "node:test";
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { buildStarter, makeProject } from "../src/project.js";
import { cleanPage, looksSensitive } from "../server/output.js";
import { categories, resources, templates } from "../src/data.js";
import handler from "../api/studio.js";
test("guest starter escapes prompt, uses no active scripts, and refuses apparent secrets", () => {
  const html = buildStarter("<script>alert(1)</script>");
  assert.match(html, /&lt;script&gt;/);
  assert.doesNotMatch(html, /<script>/);
  assert.throws(() => buildStarter(`token: sk-${"example".repeat(4)}`));
  assert.notEqual(makeProject().id, makeProject().id);
});
test("provider output strips scripts, events, remote media and non-fragment links", () => {
  const html = cleanPage(
    '<html><head><title>Test</title><style>@import "https://example.test/style"; p{color:#333;background:url(https://example.test/x)}</style></head><body><main onload="alert(1)"><h1 id="a">Hello</h1><script>alert(2)</script><img src="https://example.test/a"><a href="https://example.test">External</a><a href="#a">Jump</a><form action="https://example.test"><input name="secr"></form></main></body></html>',
  );
  assert.match(html, /href="#a"/);
  assert.match(html, /color:#333/);
  assert.doesNotMatch(html, /example\.test|<script|onload=|<form|<img/);
  assert.match(html, /default-src 'none'/);
});
test("blocks unsafe CSS and likely credential patterns", () => {
  const html = cleanPage(
    '<html><style>@font-face{src:U\\52L(https://example.test/data)}.thing{background:from-image(image-set(https://example.test/x));color:red}</style><main class="thing">test</main></html>',
  );
  assert.match(html, /color:red/);
  assert.doesNotMatch(html, /https:/);
  assert.ok(looksSensitive("password = longExample123456"));
});
test("catalog covers all eight categories and labels references distinctly", () => {
  assert.equal(categories.length, 8);
  assert.deepEqual(
    new Set(resources.map((x) => x.category)),
    new Set(categories),
  );
  assert.ok(
    templates.some((t) => t.kind === "reference" && t.source === "ThreeUI"),
  );
});
test("without credentials public config exposes no secrets and admin fails closed", async () => {
  const keys = [
    "SUPABASE_URL",
    "SUPABASE_ANON_KEY",
    "SUPABASE_SERVICE_ROLE_KEY",
    "AI_API_KEY",
  ];
  const prev = Object.fromEntries(keys.map((k) => [k, process.env[k]]));
  for (const k of keys) delete process.env[k];
  process.env.AI_API_KEY = "never-return-this";
  const server = createServer(handler);
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  try {
    const url = `http://127.0.0.1:${server.address().port}/api/studio`;
    const res = await fetch(url + "?action=config");
    assert.deepEqual(await res.json(), {
      url: null,
      anon: null,
      ai: false,
      limit: 15,
    });
    assert.equal((await fetch(url + "?action=admin")).status, 503);
  } finally {
    await new Promise((r) => server.close(r));
    for (const k of keys) {
      if (prev[k] === undefined) delete process.env[k];
      else process.env[k] = prev[k];
    }
  }
});
