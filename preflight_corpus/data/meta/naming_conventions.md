# Naming Conventions

This project uses consistent, predictable naming to make it easier to reference and maintain metadata.

## Item IDs

Each catalog entry must have a stable `item_id`. The format is:

`sourceid-YYYY-MM-DD-slug`

- `sourceid`: The parent source identifier from `sources.csv`
- `YYYY-MM-DD`: Date of publication or last update (ISO 8601 format)
- `slug`: A short, hyphenated string based on the document title

**Examples**
- `1014-2025-08-15-opensearch-benchmarking`
- `1020-2023-06-07-uniswap-v3-limit-orders`

## Zero-padding rule

- Always zero-pad month and day values:  
  ✅ `2025-08-05`  
  ❌ `2025-8-5`

## Slug rules

- Lowercase only
- Hyphens for separators (`-`)
- Alphanumeric characters only (`a–z`, `0–9`), plus hyphen  
- No underscores, spaces, punctuation, or special characters

**Examples**
- Title: *“OpenSearch Benchmarking”* → Slug: `opensearch-benchmarking`
- Title: *“Uniswap V3 Limit Orders”* → Slug: `uniswap-v3-limit-orders`


