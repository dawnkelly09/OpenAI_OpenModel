# Schema for Document Frontmatter

Each `.md` file in the corpus should begin with a YAML block matching this template.

```yaml
---
source_id: 0000 # ID for parent source from sources.csv
source_url: "https://..."   # Canonical URL for parent source
item_id: "INSERT_ITEM_ID"  # source_id-ISOdate-stable slug (i.e: "1020-2023-06-07-uniswap-v3-limit-orders") 
title: "INSERT_DOCUMENT_TITLE"  # Human-readable title
author_or_org: ["INSERT_AUTHOR_OR_ORG_NAME(S)"] # Who created this file?
item_source_url: "https://..."   # Canonical URL for this file
local_path: "data/rag/.../file.md"   # Path inside repo
type: "doc|standard|audit|report|paper|guide|checklist|taxonomy|code"
intended_use: "RAG|FT|both" # How this file is used
license: "INSERT_LICENSE"     # SPDX or short label
date_last_updated: "YYYY-MM-DD"  # ISO dates only
source_family: "trailofbits|owasp|openzeppelin|ethtrust|ethereum|cyfrin|immunefi"
tags: ["tag1","tag2"]       # 2–5 controlled tags
status: "active|legacy|draft"  # Only for standards/specs
language: "en"              # Language code

# Optional crosswalk mappings
x:
  crosswalk:
    ethtrust: []
    scwe: []
    swc: []
---
