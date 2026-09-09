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


V1.61: Removed the in-page startup cover and opacity gate that could appear during refresh. Restored normal immediate page painting and changed navigation caching to cache-first with background update for a no-visible-intermediate refresh experience. All vocabulary and learning logic unchanged.
