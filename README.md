# Maki's Wiki

Source for https://a2zchocolate.github.io — a personal wiki built with GitHub Pages (Jekyll, no plugins).

**Add an article:** create `wiki/<name>.md` with this at the top, then write in Markdown:

```
---
title: Article title
category: Projects
summary: One line shown on the All articles page.
infobox:            # optional
  - [Label, Value]
---
```

Sections (`## Heading`) build the Contents box automatically once there are three or more.
`python3 preview.py` builds a rough local preview in `_preview/` (needs `pip install python-liquid markdown pyyaml`).
