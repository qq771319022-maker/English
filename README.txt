V1.66（基于 V1.65 重做）

新增：在“我的”页面增加“单词检索”功能：
1. 同时检索日常英语 + 专业工程英语本地词库；
2. 词库已有单词可直接加入复习计划，沿用原有复习箱/到期机制；
3. 词库没有的单词可手动填写英文和中文释义，并选择日常/专业；
4. 新增单词保存到浏览器本地，不修改 vocab.json；
5. 新增/已有单词均可使用浏览器系统 SpeechSynthesis 发音；
6. 手动新增单词保存后立即进入“复习”页面的到期队列。

保留 V1.65 原有学习进度、收藏、每日计划和发音设置。

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
