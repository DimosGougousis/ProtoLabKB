---
type: command
name: pl-refresh-kb
description: Refresh cached knowledge base articles from ProtoLabs website
usage: /pl-refresh-kb [folder]
---

# /pl-refresh-kb

Refresh cached knowledge base articles by re-fetching content from ProtoLabs website URLs.

## Usage

```
/pl-refresh-kb              # Refresh all knowledge base articles
/pl-refresh-kb cnc-machining # Refresh only CNC machining articles
/pl-refresh-kb injection-molding  # Refresh only injection molding articles
/pl-refresh-kb 3d-printing   # Refresh only 3D printing articles
/pl-refresh-kb materials     # Refresh only materials articles
/pl-refresh-kb verticals      # Refresh only verticals articles
/pl-refresh-kb trends         # Refresh only trends articles
/pl-refresh-kb sheet-metal    # Refresh only sheet metal articles
```

## Procedure

1. **Parse Argument**
   - If no argument: target all knowledge folders
   - If folder specified: target only that folder

2. **Validate Folder**
   - Check if folder exists in `knowledge/`
   - Check if `_index.md` exists in folder
   - If invalid, report error

3. **Read Index**
   - Parse `_index.md` to get list of articles and URLs
   - Extract source_url for each article

4. **Fetch Each Article**
   - For each article in the index:
     - Fetch content from source_url using WebFetch
     - Update `fetched_at` timestamp
     - Update `summary` if content changed significantly
     - Write updated content to article file

5. **Report Results**
   - List successfully refreshed articles
   - List any failed fetches with error reasons
   - Show summary count (refreshed/total)

## Output Format

```
# Knowledge Base Refresh Report

## Summary
- Folder: [folder name or "all"]
- Articles processed: [count]
- Successfully refreshed: [count]
- Failed: [count]
- Timestamp: [ISO 8601]

## Refreshed Articles
| Article | Status | Previous Fetch | New Fetch |
|---------|--------|----------------|-----------|
| [name] | ✅ Success | [old date] | [new date] |
| [name] | ❌ Failed | [old date] | [error] |

## Failed Fetches
| Article | Error | Action Required |
|---------|-------|-----------------|
| [name] | [error] | [suggestion] |
```

## Error Handling

- **404 Not Found**: URL may have changed; check ProtoLabs website for new location
- **Network Error**: Retry once; if persists, skip and report
- **Parse Error**: Content may have changed format; manual review needed
- **Permission Error**: Check URL accessibility; may require different approach

## Notes

- The `_index.md` file in each folder serves as the source of truth for URLs
- Articles are fetched individually to avoid overwhelming the server
- Timestamps are updated only on successful fetch
- Failed fetches preserve the existing cached content
- Some URLs may return 404 if ProtoLabs has restructured their content
