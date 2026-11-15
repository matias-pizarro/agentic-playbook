"""MkDocs hook: links in imported src pages to files the playbook lacks.

The infra pages imported from src (PP-Q7) link to src files the playbook does
not import: tickets, perimeters, scripts. On imported pages only, such a link
becomes plain text naming the file in src at the imported commit (PP-Q19), so
the strict build still fails on a broken link in the playbook's own pages.
"""

import posixpath
import re

PREFIX = "imported/"
# [text](target) or [text](target "title"); images ![..](..) are left alone.
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)(\s+\"[^\"]*\")?\)")


def on_page_markdown(markdown, page, config, files):
    src_uri = page.file.src_uri
    if not src_uri.startswith(PREFIX):
        return markdown
    commit = config["extra"]["src_commit"][:7]
    here = posixpath.dirname(src_uri)

    def replace(match):
        text, target = match.group(1), match.group(2)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith(("#", "/")):
            return match.group(0)
        path = posixpath.normpath(posixpath.join(here, target.split("#")[0]))
        if files.get_file_from_path(path) is not None:
            return match.group(0)
        return f"{text} (`{path[len(PREFIX):]}` in src at `{commit}`)"

    return LINK.sub(replace, markdown)
