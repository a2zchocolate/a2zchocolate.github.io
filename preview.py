"""Local preview of the Jekyll site (GitHub Pages builds the real one). Output: _preview/"""
import re, os, json, pathlib, yaml, markdown, liquid
root = pathlib.Path(__file__).parent
cfg = yaml.safe_load((root/"_config.yml").read_text())
def fm(path):
    t = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", t, re.S)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else (None, t)
pages = []
for p in sorted(list(root.glob("*.md")) + list(root.glob("wiki/*.md"))):
    meta, body = fm(p)
    if meta is None: continue
    rel = str(p.relative_to(root))
    url = meta.get("permalink") or ("/" if rel == "index.md" else "/" + rel[:-3] + "/")
    pages.append({**meta, "url": url, "path": rel, "_body": body})
env = liquid.Environment()
md = lambda s: markdown.markdown(s, extensions=["tables", "md_in_html", "attr_list", "def_list"])
env.filters["relative_url"] = lambda c, v: v
env.filters["markdownify"] = lambda c, v: md(str(v))
env.filters["slugify"] = lambda c, v: re.sub(r"[^a-z0-9]+", "-", str(v).lower()).strip("-")
def where_exp(c, seq, var, expr):
    field = expr.split(".", 1)[1]
    return [x for x in seq if x.get(field)]
env.filters["where_exp"] = where_exp
layout = env.parse((root/"_layouts/wiki.html").read_text())
out = root/"_preview"; out.mkdir(exist_ok=True)
site = {**cfg, "pages": pages}
for pg in pages:
    ctx = {"site": site, "page": pg}
    body = env.parse(pg["_body"]).render(ctx)
    html = layout.render({**ctx, "content": md(body)})
    # make links relative so the preview works anywhere
    depth = len([x for x in pg["url"].split("/") if x and not x.endswith(".html")])
    up = "../" * depth or "./"
    def fix(m):
        u = m.group(2)
        if u.startswith("//"): return m.group(0)
        path, _, frag = u[1:].partition("#")
        if path and not path.endswith((".css", ".html")): path = path.rstrip("/") + "/index.html"
        if not path: path = "index.html"
        return m.group(1) + up + path + ("#" + frag if frag else "")
    html = re.sub(r'((?:href|src)=")(/[^"]*)', fix, html)
    html = re.sub(r'"(/[a-z0-9/-]*/)"', lambda m: '"' + up + m.group(1).strip("/") + '/index.html"', html)
    dest = out / (pg["url"].strip("/") or "") / "index.html" if not pg["url"].endswith(".html") else out / pg["url"].lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(html, encoding="utf-8")
(out/"assets").mkdir(exist_ok=True); (out/"assets/wiki.css").write_text((root/"assets/wiki.css").read_text())
print("built", [p["url"] for p in pages])
