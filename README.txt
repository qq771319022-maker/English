DC Engineer English PWA V1.59

V1.59 is based directly on V1.55.

1. Added a structured “关联记忆组” learning model: one core word + prefix/suffix changes + meaning relationships.
2. Added only high-value gaps found by scanning the existing vocabulary, avoiding inflection-only padding.
3. Strong groups include connect, charge, load, power, operate, approve, test, configure, respond, depend, prepare, safe, effect, active, direct, possible, necessary, and regular.
4. Added high-value new headwords such as reconnect, connectivity, overcharge, reload, unload, powered, powerful, powerless, operational, approval, disapprove, testing, tester, configure, configuration, reconfigure, responsive, dependent, independent, dependence, independence, preparation, unprepared, unsafe, safely, ineffective, effectively, inactive, deactivate, indirect, impossible, possibility, unnecessary, irregular, regularly.
5. Existing strong family members were assigned consistent family metadata so the UI can recognize them as one association group.
6. Today learning still keeps Daily and Professional pools independent, while related words inside each pool are kept adjacent.
7. No audio files are included.


V1.59 association enhancement: existing vocabulary is organized into three association layers — word families, prefix/contrast relationships, and practical data-center/electrical engineering scenarios. No bulk vocabulary expansion was performed.


V1.59 UI optimization:
- Follow the device/system light/dark mode automatically.
- Light mode keeps the existing blue-white UI unchanged.
- Dark mode uses a unified neutral dark palette inspired by WeChat-style black/white contrast.
- Header, content cards, detail sheets, controls, and bottom navigation switch as one consistent theme.
- No vocabulary, learning logic, review logic, or association logic changes.
- No audio files added.


V1.65: Removed the in-page startup cover and opacity gate that could appear during refresh. Restored normal immediate page painting and changed navigation caching to cache-first with background update for a no-visible-intermediate refresh experience. All vocabulary and learning logic unchanged.


V1.65: removed all visible static HTML app content from initial document; app shell is created only after vocab is available, then rendered once. Vocab cache query removed for immediate SW cache hit. No vocabulary or learning logic changes.


V1.65 quality pass: repaired 55 structurally shifted legacy records; repaired 177 generic/mismatched Chinese examples; polished selected technical/email entries; normalized high-confidence family metadata and association links; corrected daily-plan cache key so the updated vocabulary can generate a fresh plan. No audio files.


V1.65: Fixed white-screen regression from V1.63/V1.64. The existing app shell is inserted before the main JS binds DOM events; the previous null-element error no longer stops initialization. No vocabulary, theme, learning-plan, or review logic changes.

V1.68: Continued vocabulary quality audit based on V1.67. Refined 80+ technical/daily example sentences for natural usage, clearer engineering context, and better headword coverage; removed remaining avoidable duplicate/family examples. Updated vocabulary metadata and service-worker cache version. No app feature or learning-logic changes.

V1.69: Deep vocabulary QA pass based on V1.68. Removed the 17 personal words from the formal vocab dataset and kept them local-only with first-run localStorage seeding; repaired remaining template-style Chinese translations, 80+ technical example sentences, malformed collocations, and several semantic mismatches. Revalidated JSON, JavaScript, service-worker cache version, and ZIP integrity. No learning/review logic changes.


V1.70: Deep second-stage vocabulary QA based on V1.69. Reworked the remaining template-heavy daily, travel, medical, and technical examples; corrected the legacy Chinese template cluster; fixed semantic mismatches between headwords and examples; normalized I/O notation; refined selected collocations; and revalidated the formal/local word separation. Formal vocab remains 2,533 entries, with 17 personal words seeded locally on first run. No learning/review logic changes.


V1.71: Third deep vocabulary QA pass based on V1.70. Reworked the remaining repetitive inspection examples into task-specific engineering sentences; repaired an incorrect Chinese meaning/example for “fitting”; polished selected everyday/workplace phrases; revalidated word-example coverage, duplicate examples, JSON, JavaScript syntax, cache version, and formal/local vocabulary separation. No learning/review logic changes.


V1.72: Deep contextual QA and naturalness pass based on V1.71. Corrected high-confidence English/Chinese mismatches, removed generated filler collocations from generator/switchgear and daily-life vocabulary blocks, repaired travel examples that incorrectly used “booking” as a generic object, improved transformer/test-report examples, clarified REF/dB terminology, normalized “no-load test” and “function/functional test”, and synchronized connected-speech hints. No learning/review logic changes.


V1.73: Fourth deep vocabulary QA pass based on V1.72. Normalized high-confidence part-of-speech labels that did not match standard usage, repaired several English/Chinese mismatches, refined generic or awkward engineering examples, improved technical collocations such as root cause and three-phase supply, normalized SLD capitalization, and synchronized connected-speech hints for revised examples. Updated the visible app version and service-worker cache. No learning/review logic changes.


V1.73 QA follow-up: Removed 44 redundant hyphen/space duplicate headwords where they represented the same lexical item, while preserving genuine grammatical contrasts such as check-in/check in. Corrected several headword/POS mismatches in everyday vocabulary and technical examples, fixed the incorrect “simulate-trip” item by replacing it with “trip simulation”, and refined additional travel and engineering sentences for natural usage.
