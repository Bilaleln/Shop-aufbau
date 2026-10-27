# FALUNARA Singing Ad – Production Status

## Completed
- [x] Winning Copy (English, ~350 words, ~3 min target)
- [x] Songtext with structure tags (100 lines, Verse/Build/Chorus/Bridge/Outro)
- [x] Character Bible (Claire, Lily, packaging, locations)
- [x] Scene Plan (56 scenes, all with descriptions)
- [x] Cost Estimate (~5,900 credits / ~$30)
- [x] Packaging reference image (falunara-packaging.webp)
- [x] Singing-Ad Skill installed (.claude/skills/singing-ad/SKILL.md)
- [x] Automation scripts (kie_api.py, subtitle_renderer.py, clip_inspector.py)
- [x] KIE AI API connection verified

## Next Steps (awaiting approval)
- [ ] **Song generation** – Suno V4.5, 2 variants (12 credits)
- [ ] Song selection + trimming
- [ ] STT transcription + line timing
- [ ] Character reference images (Claire, Lily) – 2 × 18 credits
- [ ] Character approval
- [ ] 1 test scene (image + clip) – ~88 credits
- [ ] Full image generation (56 scenes)
- [ ] Full clip generation (56 clips)
- [ ] Assembly + subtitles
- [ ] Final quality check

## API Endpoints (verified 2026-10-27)
| Endpoint | Status |
|---|---|
| `POST /api/v1/generate` (Suno) | Ready |
| `GET /api/v1/generate/record-info` (Suno status) | Verified |
| `POST /api/v1/jobs/createTask` (Images/Video) | Ready |
| `GET /api/v1/jobs/recordInfo` (Job status) | Verified |

## File Structure
```
singing-ad/
├── winning-copy.md          # Source copy
├── songtext.txt             # Lyrics with tags
├── figuren-bibel.md         # Character bible
├── szenenplan.md            # 56-scene plan
├── kostenschaetzung.md      # Cost estimate
├── falunara-packaging.webp  # Product reference image
├── STATUS.md                # This file
├── scripts/
│   ├── kie_api.py           # KIE AI API client
│   ├── subtitle_renderer.py # PNG subtitle renderer
│   └── clip_inspector.py    # Video QA tool
├── figuren/                 # Character reference images
├── startbilder/             # Generated scene images
├── clips/                   # Generated video clips
├── output/                  # Final assembled video
└── verworfen/               # Rejected generations
```
