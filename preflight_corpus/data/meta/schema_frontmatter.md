# Schema for Document Frontmatter

Each `.md` file in the corpus should begin with a YAML block matching this template.

```yaml
---
doc_id: 0000                # Unique numeric/string ID
title: "TITLE GOES HERE"    # Human-readable title
source_url: "https://..."   # Canonical source
local_path: "data/rag/.../file.md"   # Path inside repo
type: "doc|standard|audit|report|paper|guide|checklist|taxonomy|code"
intended_use: "RAG|FT|both" # How this file is used
license: "LICENSE HERE"     # SPDX or short label
version_or_date: "YYYY-MM-DD or vX.Y"  # ISO preferred
tags: ["tag1","tag2"]       # 2–5 controlled tags
status: "active|legacy|draft"  # Only for standards/specs
language: "en"              # Language code

# Optional crosswalk mappings
x:
  crosswalk:
    ethtrust: ["L1-Validation"]
    scwe: ["SCWE-1.1"]
    swc: ["SWC-107"]
---
