import React, { lazy, Suspense, useState } from "react";
import {
  ArrowUpRight,
  Bookmark,
  Boxes,
  Braces,
  ExternalLink,
  Layers3,
  Search,
} from "lucide-react";
import { categories, resources, templates } from "./data.js";
import { Composer, Empty, PageTitle } from "./ui.jsx";
const Chips = lazy(() => import("./pinui/Chips.tsx"));
const Task = lazy(() => import("./pinui/TaskCard.tsx"));
export default function Explore({
  savedOnly,
  saved,
  toggleSave,
  theme,
  add,
  notify,
}) {
  const param = new URLSearchParams(location.search).get("template");
  const [mode, setMode] = useState(param ? "Kho template" : "Tài nguyên"),
    [category, setCategory] = useState("Tất cả"),
    [filter, setFilter] = useState(""),
    [search, setSearch] = useState(""),
    [sort, setSort] = useState("Nguồn tuyển chọn"),
    [selected, setSelected] = useState(
      templates.find((t) => t.id === param) || templates[0],
    ),
    [draft, setDraft] = useState("");
  const allTags = [...new Set(resources.flatMap((r) => r.tags))].sort();
  const matching = (x) =>
    !search ||
    [x.title, x.desc, x.category, x.source, ...(x.tags || [])]
      .join(" ")
      .toLowerCase()
      .includes(search.toLowerCase());
  const rows = resources.filter(
    (r) =>
      (category === "Tất cả" || r.category === category) &&
      (!filter || r.tags.includes(filter)) &&
      matching(r) &&
      (!savedOnly || saved.includes(r.id)),
  );
  const collection = templates
    .filter(
      (t) =>
        (!filter || t.style === filter) &&
        matching(t) &&
        (!savedOnly || saved.includes(t.id)),
    )
    .sort((a, b) => (sort === "Tên A–Z" ? a.title.localeCompare(b.title) : 0));
  const item = collection.find((x) => x.id === selected?.id) || collection[0];
  const save = (id) => {
    toggleSave(id);
    notify(saved.includes(id) ? "Đã bỏ lưu." : "Đã lưu trên thiết bị.");
  };
  const use = (x) =>
    add(
      "",
      `${x.title} — ${x.desc}\nNguồn: ${x.url}\nQuyền sử dụng: ${x.license}`,
    );
  return (
    <div className="container page explore">
      <PageTitle
        n="02"
        label="EXPLORE"
        title={savedOnly ? "Đã lưu" : "Tìm đúng thứ để bắt đầu."}
      >
        {savedOnly
          ? "Tài nguyên và mẫu bạn đã lưu trên thiết bị này."
          : "Giữ nguồn, giấy phép và mẫu xem thử cạnh nhau để dễ chọn."}
      </PageTitle>
      <div className="explore-dock">
        <div className="dock-top">
          <div className="segmented">
            {["Tài nguyên", "Kho template"].map((m) => (
              <button
                className={mode === m ? "active" : ""}
                key={m}
                onClick={() => {
                  setMode(m);
                  setFilter("");
                }}
              >
                {m === "Tài nguyên" ? (
                  <Boxes size={16} />
                ) : (
                  <Layers3 size={16} />
                )}{" "}
                {m}
              </button>
            ))}
          </div>
          <label className="search-box">
            <Search size={16} />
            <input
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Tìm theo tên hoặc tag"
              aria-label="Tìm tài nguyên"
            />
          </label>
          <select
            aria-label="Bộ lọc tag"
            value={filter}
            onChange={(e) => setFilter(e.target.value)}
          >
            <option value="">
              {mode === "Tài nguyên" ? "Tất cả tag" : "Mọi phong cách"}
            </option>
            {(mode === "Tài nguyên"
              ? allTags
              : [...new Set(templates.map((t) => t.style))]
            ).map((t) => (
              <option key={t}>{t}</option>
            ))}
          </select>
        </div>
        {mode === "Tài nguyên" && (
          <div className="category-row">
            {["Tất cả", ...categories].map((c) => (
              <button
                key={c}
                className={category === c ? "active" : ""}
                onClick={() => setCategory(c)}
              >
                {c}
              </button>
            ))}
          </div>
        )}
      </div>
      {mode === "Tài nguyên" ? (
        <div className="resource-list">
          <div className="results-note eyebrow">{rows.length} TÀI NGUYÊN</div>
          {rows.map((r, i) => (
            <article className="resource-row" key={r.id}>
              <span className="eyebrow">{String(i + 1).padStart(2, "0")}</span>
              <div>
                <span className="eyebrow">{r.category}</span>
                <h2>{r.title}</h2>
                <p>{r.desc}</p>
                <div className="tag-list">
                  {r.tags.map((t) => (
                    <span key={t}>{t}</span>
                  ))}
                </div>
                <small>
                  {r.license} · Đối chiếu thông tin trong kho {r.reviewed}; chưa
                  chạy thử.
                </small>
              </div>
              <div className="resource-actions">
                <a
                  className="btn"
                  href={r.url}
                  target="_blank"
                  rel="noreferrer"
                >
                  Nguồn <ExternalLink size={14} />
                </a>
                <button
                  className="icon-button"
                  aria-pressed={saved.includes(r.id)}
                  onClick={() => save(r.id)}
                  aria-label={`Lưu ${r.title}`}
                >
                  <Bookmark
                    size={17}
                    fill={saved.includes(r.id) ? "currentColor" : "none"}
                  />
                </button>
                <button className="btn" onClick={() => use(r)}>
                  Dùng trong dự án <ArrowUpRight size={14} />
                </button>
              </div>
            </article>
          ))}
          {!rows.length && (
            <Empty icon={Search} title="Không có tài nguyên phù hợp">
              Thử bỏ bộ lọc hoặc dùng từ khóa khác.
            </Empty>
          )}
        </div>
      ) : (
        <>
          <div className="results-note template-note">
            <span className="eyebrow">{collection.length} MẪU</span>
            <select
              aria-label="Sắp xếp mẫu"
              value={sort}
              onChange={(e) => setSort(e.target.value)}
            >
              <option>Nguồn tuyển chọn</option>
              <option>Tên A–Z</option>
            </select>
          </div>
          {!item ? (
            <Empty title="Không có template phù hợp" />
          ) : (
            <div className="browse-stage">
              <div className="cascade">
                {collection.map((t, i) => (
                  <button
                    key={t.id}
                    aria-pressed={t.id === item.id}
                    className={"template-tile " + t.tone}
                    onClick={() => {
                      setSelected(t);
                      setDraft("");
                    }}
                  >
                    <div
                      className={
                        t.height === "tall"
                          ? "template-art tall"
                          : "template-art"
                      }
                    >
                      {t.image ? (
                        <img src={t.image} alt="" loading="lazy" />
                      ) : (
                        <Braces size={t.height === "tall" ? 44 : 29} />
                      )}
                    </div>
                    <div className="template-label">
                      <span>
                        <b>{t.title}</b>
                        <small>
                          {t.source} · {t.style}
                        </small>
                      </span>
                      <ArrowUpRight size={17} />
                    </div>
                  </button>
                ))}
              </div>
              <aside className="sticky-stage">
                <div className="stage-head">
                  <span className="eyebrow">
                    <span className="route-led" />{" "}
                    {item.kind === "reference" ? "THAM CHIẾU" : "XEM MẪU"}
                  </span>
                  <button
                    className="icon-button"
                    aria-label={`Lưu ${item.title}`}
                    aria-pressed={saved.includes(item.id)}
                    onClick={() => save(item.id)}
                  >
                    <Bookmark
                      size={17}
                      fill={saved.includes(item.id) ? "currentColor" : "none"}
                    />
                  </button>
                </div>
                <div className="template-preview" key={item.id}>
                  <Suspense fallback={<p>Đang tải mẫu…</p>}>
                    {item.kind === "prompt" ? (
                      <Composer
                        value={draft}
                        onChange={setDraft}
                        onSubmit={() => add(draft, item.url)}
                        placeholder="Thử nhập một ý tưởng…"
                      />
                    ) : item.kind === "html" ? (
                      <iframe
                        src={item.file}
                        title={item.title}
                        sandbox="allow-scripts"
                        loading="lazy"
                      />
                    ) : item.kind === "chips" ? (
                      <Chips theme={theme} />
                    ) : item.kind === "task" ? (
                      <Task theme={theme} />
                    ) : item.image ? (
                      <img src={item.image} alt={item.title} />
                    ) : (
                      <Empty icon={Braces} title="Chỉ có thông tin tham khảo">
                        Mã nguồn không được cung cấp trong kho.
                      </Empty>
                    )}
                  </Suspense>
                </div>
                <div className="stage-description">
                  <h2>{item.title}</h2>
                  <p>{item.desc}</p>
                  <small>
                    {item.source} · {item.license}
                  </small>
                  <div>
                    <a
                      className="btn"
                      href={item.url}
                      target="_blank"
                      rel="noreferrer"
                    >
                      Nguồn <ExternalLink size={14} />
                    </a>
                    <button className="btn primary" onClick={() => use(item)}>
                      Mở trong Work space <ArrowUpRight size={15} />
                    </button>
                  </div>
                </div>
              </aside>
            </div>
          )}
        </>
      )}
    </div>
  );
}
