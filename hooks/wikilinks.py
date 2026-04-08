r"""
MkDocs hook: converts Obsidian-style [[wikilinks]] to standard markdown links.

Handles:
  [[path/to/file]]                 -> [File Title](../path/to/file.md)
  [[path/to/file|Display Text]]    -> [Display Text](../path/to/file.md)
  [[path/to/file\|Display Text]]   -> same (escaped pipe inside table cells)
  [[path/to/file#section]]         -> [File Title](../path/to/file.md#section)
  [[#section]]                     -> [Section](#section)  (same-page anchor)
  [[_index]] / [[_index#section]]  -> [Index](../index.md#section)
"""

import re
import os


def on_page_markdown(markdown, page, config, files):
    current_dir = os.path.dirname(page.file.src_path)  # e.g. "coins" or ""

    def replace_wikilink(match):
        inner = match.group(1).strip()

        # Normalise escaped pipes used in markdown table cells: \| → |
        inner = inner.replace("\\|", "|")

        # Split display text  [[path|Display Text]]
        if "|" in inner:
            path_part, display = inner.split("|", 1)
            path_part = path_part.strip()
            display = display.strip()
        else:
            path_part = inner
            display = None

        # Same-page anchor  [[#section]]
        if path_part.startswith("#"):
            anchor_str = "#" + re.sub(r"[^\w-]", "-", path_part[1:].lower()).strip("-")
            display = display or path_part[1:].replace("-", " ").title()
            return f"[{display}]({anchor_str})"

        # Split anchor  [[path#section]]
        anchor_str = ""
        if "#" in path_part:
            path_part, anchor = path_part.split("#", 1)
            path_part = path_part.strip()
            anchor_str = "#" + re.sub(r"[^\w-]", "-", anchor.lower()).strip("-")

        # _index → index.md
        if path_part in ("_index", ""):
            target = ("../" if current_dir else "") + "index.md"
            display = display or "Index"
            return f"[{display}]({target}{anchor_str})"

        # Build relative path from current file to target
        target_md = path_part + ".md"   # e.g. "concepts/zero-knowledge-proofs.md"

        if current_dir:
            rel = os.path.relpath(target_md, current_dir).replace("\\", "/")
        else:
            rel = target_md

        # Auto-generate display text from filename if not provided
        if display is None:
            basename = os.path.basename(path_part)
            display = basename.replace("-", " ").replace("_", " ").title()

        return f"[{display}]({rel}{anchor_str})"

    return re.sub(r"\[\[([^\]]+)\]\]", replace_wikilink, markdown)
