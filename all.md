---
title: All articles
permalink: /all/
---
Every article on this wiki, grouped by category.

{% assign arts = site.pages | where_exp: "p", "p.category" | sort: "title" %}
{% assign cats = arts | map: "category" | uniq | sort %}
{% for c in cats %}
<h2 id="{{ c | slugify }}">{{ c }}</h2>
<ul>
{% for p in arts %}{% if p.category == c %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>{% if p.summary %} – {{ p.summary }}{% endif %}</li>
{% endif %}{% endfor %}
</ul>
{% endfor %}
