from pathlib import Path
p=Path('/mnt/data/v156work/index.html')
s=p.read_text(encoding='utf-8')
# Add CSS before </style>
css='''\n.captureHint{font-size:12px;color:#71859b;line-height:1.55;margin-top:7px}.captureInput{width:100%;padding:13px 14px;border:1px solid #dce8f5;border-radius:14px;font-size:16px;background:#fbfdff;outline:none}.captureInput:focus{border-color:#8dbef5;box-shadow:0 0 0 4px rgba(64,145,235,.1)}.captureResult{margin-top:12px;background:#f7fbff;border:1px solid #dceaf7;border-radius:16px;padding:14px}.captureResult h3{margin:0 0 6px;font-size:20px}.captureGrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:10px}.captureChip{background:#fff;border:1px solid #e2ebf4;border-radius:12px;padding:9px;font-size:12px}.captureChip b{display:block;color:#516a84;font-size:10px;margin-bottom:3px}.captureAssoc{display:flex;gap:7px;flex-wrap:wrap;margin-top:8px}.captureAssoc span{padding:5px 9px;background:#edf6ff;color:#286fd9;border-radius:999px;font-size:12px}.captureList{max-height:230px;overflow:auto;margin-top:10px}.captureWord{display:flex;justify-content:space-between;gap:8px;align-items:center;padding:9px 0;border-bottom:1px solid #edf2f7}.captureWord:last-child{border-bottom:0}.captureWord b{font-size:15px}.captureWord small{display:block;color:#71859b;margin-top:2px}.apiBox{background:#f7fafc;border:1px dashed #d6e2ed;border-radius:14px;padding:12px;margin-top:10px}.apiBox label{display:block;font-size:11px;color:#657b91;margin:8px 0 4px}.apiBox input{width:100%;padding:10px 11px;border:1px solid #d8e4ef;border-radius:10px;background:#fff}.dangerNote{font-size:11px;color:#9a5b2b;line-height:1.45;margin-top:8px}\n'''
s=s.replace('</style>',css+'</style>',1)
# Add capture modal
old='<div id="modal" class="modal"><div class="sheet"><button class="close" id="closeBtn">关闭</button><div id="detail"></div></div></div>'
new=old+'\n<div id="captureModal" class="modal"><div class="sheet"><button class="close" id="captureClose">关闭</button><div id="captureBody"></div></div></div>'
s=s.replace(old,new,1)
# Add personal vocab vars after favs
needle="const favs=new Set(JSON.parse(localStorage.getItem('favs')||'[]'));"
insert=needle+"\nlet personalVocab=JSON.parse(localStorage.getItem('dceng_personal_vocab')||'[]');\n"
s=s.replace(needle,insert,1)
# Add functions before familyKey
needle='function familyKey(x){'
func=r'''function savePersonalVocab(){localStorage.setItem('dceng_personal_vocab',JSON.stringify(personalVocab));}
function mergePersonalVocab(){
  const base=new Set(items.map(x=>String(x.word||'').trim().toLowerCase()));
  personalVocab.filter(x=>x&&x.word&& !base.has(String(x.word).trim().toLowerCase())).forEach(x=>items.push(x));
}
function findLocalWord(word){const k=String(word||'').trim().toLowerCase();return uniqueByWord(items).find(x=>String(x.word||'').trim().toLowerCase()===k)||null;}
function localAssociation(word){
  const x=findLocalWord(word); if(x){
    const k=familyKey(x); if(k.startsWith('single:')) return [];
    return uniqueByWord(items.filter(y=>familyKey(y)===k)).slice(0,12);
  }
  const w=String(word||'').trim().toLowerCase();
  const probes=[w.replace(/^re/,'').replace(/^un/,'').replace(/^dis/,'').replace(/^in/,'').replace(/^im/,'').replace(/^ir/,'').replace(/^de/,'').replace(/^over/,'').replace(/^under/,'').replace(/(tion|sion|ment|ness|ity|er|or|ly|able|ive)$/,''),w.replace(/(tion|sion|ment|ness|ity|er|or|ly|able|ive)$/,'')].filter(Boolean);
  for(const q of probes){const cand=uniqueByWord(items.filter(y=>{const yw=String(y.word||'').toLowerCase();return yw===q || String(y.root||'').toLowerCase()===q || String(y.family||'').toLowerCase()===q}));if(cand.length)return cand.slice(0,12)}
  return [];
}
function aiConfig(){return {endpoint:localStorage.getItem('dceng_ai_endpoint')||'',key:localStorage.getItem('dceng_ai_key')||'',model:localStorage.getItem('dceng_ai_model')||'gpt-5-mini'}}
function saveAiConfig(){localStorage.setItem('dceng_ai_endpoint',$id('aiEndpoint')?.value.trim()||'');localStorage.setItem('dceng_ai_key',$id('aiKey')?.value.trim()||'');localStorage.setItem('dceng_ai_model',$id('aiModel')?.value.trim()||'gpt-5-mini');}
function extractAIText(data){
  const c=data?.choices?.[0]?.message?.content;
  if(typeof c==='string')return c;
  if(Array.isArray(c))return c.map(x=>typeof x==='string'?x:(x?.text||'')).join('');
  if(typeof data?.output_text==='string')return data.output_text;
  return '';
}
function parseAIJSON(text){
  let t=String(text||'').trim().replace(/^```(?:json)?/i,'').replace(/```$/,'').trim();
  try{return JSON.parse(t)}catch(e){}
  const a=t.indexOf('{'),b=t.lastIndexOf('}'); if(a>=0&&b>a){try{return JSON.parse(t.slice(a,b+1))}catch(e){}}
  return null;
}
function compactCandidates(arr){return arr.slice(0,12).map(x=>({word:x.word,meaning_zh:x.meaning_zh,pos:x.pos,root:x.root,family:x.family,category:x.category}));}
function buildAIRequest(word,context){
  const assoc=localAssociation(word), candidates=compactCandidates(assoc);
  return {model:aiConfig().model,messages:[
    {role:'system',content:'你是一个严谨的英语学习内容编辑，服务对象是数据中心/电气工程师。必须真实、常用、自然，禁止为了凑关联组而虚构词源或生硬搭配。只返回一个合法JSON对象，不要Markdown。'},
    {role:'user',content:`分析用户刚遇到的英文词：${word}\n用户可选上下文：${context||'未提供'}\n现有本地词库中可能相关的词：${JSON.stringify(candidates)}\n\n请返回JSON：{word,meaning_zh,pos,phonetic,root,family,association_type,related_words,collocations,daily_scene,engineering_scene,example_en,example_zh,confusable_words,category}\n规则：meaning_zh给最常用中文义；related_words只填高置信度真实关联词；family用核心词；association_type说明如“前缀变化/后缀派生/同源词/无可靠关联”；category只能是“Daily & Work English”或“Data Center & Electrical Engineering”；如果没有可靠关联，related_words=[]，family=''。`}
  ]};
}
async function analyzeWithAI(word,context){
  const cfg=aiConfig(); if(!cfg.endpoint)throw new Error('请先配置 AI 接口');
  const payload=buildAIRequest(word,context);
  const headers={'Content-Type':'application/json'}; if(cfg.key)headers.Authorization='Bearer '+cfg.key;
  const r=await fetch(cfg.endpoint,{method:'POST',headers,body:JSON.stringify(payload)});
  if(!r.ok)throw new Error('AI接口返回 HTTP '+r.status);
  const data=await r.json(),txt=extractAIText(data),obj=parseAIJSON(txt); if(!obj)throw new Error('AI 返回内容不是有效 JSON');
  return obj;
}
function renderCapture(){
  const cfg=aiConfig(), mine=personalVocab.slice().reverse();
  $id('captureBody').innerHTML=`<h2 style="margin:0 0 5px">遇到新词</h2><p class="small">把你在工作、邮件、报告、现场或日常英语中遇到的词直接放进来。先查本地词库，再由 AI 完善学习内容。</p>
    <input id="captureWord" class="captureInput" placeholder="例如：remediation / reconfigure" autocomplete="off">
    <input id="captureContext" class="captureInput" style="margin-top:8px" placeholder="可选：在哪里看到的？例如：设备整改报告">
    <button id="analyzeWord" class="cta blue">✨ 智能分析并生成学习卡</button>
    <div id="captureResult"></div>
    <div class="apiBox"><b>AI 接口设置</b><div class="captureHint">完整智能功能需要一个兼容 Chat Completions 格式的 AI 接口。接口地址和 Key 只保存在本机浏览器。</div>
      <label>Endpoint</label><input id="aiEndpoint" value="${esc(cfg.endpoint)}" placeholder="https://your-api.example/v1/chat/completions">
      <label>API Key（可留空，适用于你的代理服务）</label><input id="aiKey" type="password" value="${esc(cfg.key)}" placeholder="sk-...">
      <label>Model</label><input id="aiModel" value="${esc(cfg.model)}" placeholder="gpt-5-mini">
      <button id="saveAI" class="cta secondary">保存接口设置</button>
      <div class="dangerNote">提示：直接在浏览器保存第三方 API Key 存在泄露风险；更安全的方式是填写你自己的后端代理 Endpoint。</div>
    </div>
    <div class="panel" style="margin-top:12px"><b>我的生词 ${mine.length}</b><div class="captureList">${mine.length?mine.map(x=>`<div class="captureWord"><div><b>${esc(x.word)}</b><small>${esc(x.meaning_zh||'待完善')} · ${esc(x.family||'')}</small></div><button class="tabsBtn" data-personal-detail="${esc(x.word)}">查看</button></div>`).join(''):'<div class="small" style="padding:8px 0">还没有个人生词。</div>'}</div></div>`;
  $id('saveAI').onclick=()=>{saveAiConfig();$id('captureResult').innerHTML='<div class="status">✓ AI 接口设置已保存。</div>'};
  $id('analyzeWord').onclick=async()=>{
    const w=$id('captureWord').value.trim().toLowerCase(),ctx=$id('captureContext').value.trim(),out=$id('captureResult');
    if(!/^[a-z][a-z' -]{1,80}$/i.test(w)){out.innerHTML='<div class="status">请输入一个英文单词或短语。</div>';return}
    const existing=findLocalWord(w),assoc=localAssociation(w);
    out.innerHTML=`<div class="captureResult"><h3>${esc(w)}</h3><div class="small">${existing?'✓ 已在本地词库中找到':'未在现有词库中找到'}${assoc.length?` · 发现关联组：${esc(assoc[0].family||assoc[0].root||familyKey(assoc[0]))}`:''}</div>${assoc.length?`<div class="captureAssoc">${assoc.map(x=>`<span>${esc(x.word)}</span>`).join('')}</div>`:''}<div class="status">正在准备 AI 智能分析…</div></div>`;
    try{
      const obj=existing?await analyzeWithAI(w,ctx):await analyzeWithAI(w,ctx);
      const related=Array.isArray(obj.related_words)?obj.related_words.filter(Boolean).slice(0,10):[];
      const family=String(obj.family||'').trim();
      const entry={id:'p_'+Date.now()+'_'+Math.random().toString(36).slice(2,7),word:String(obj.word||w).trim(),meaning_zh:String(obj.meaning_zh||'').trim(),pos:String(obj.pos||'').trim(),phonetic:String(obj.phonetic||'').trim(),root:String(obj.root||family).trim(),family,association_type:String(obj.association_type||'').trim(),collocations:Array.isArray(obj.collocations)?obj.collocations.filter(Boolean).slice(0,8):[],daily_scene:String(obj.daily_scene||'').trim(),engineering_scene:String(obj.engineering_scene||'').trim(),example_en:String(obj.example_en||'').trim(),example_zh:String(obj.example_zh||'').trim(),confusable_words:Array.isArray(obj.confusable_words)?obj.confusable_words.filter(Boolean).slice(0,8):[],category:obj.category==='Data Center & Electrical Engineering'?'Data Center & Electrical Engineering':'Daily & Work English',quality:'ai-generated',source:'我的生词'};
      const same=findLocalWord(entry.word);
      if(!same){personalVocab.push(entry);savePersonalVocab();items.push(entry)}
      const finalAssoc=localAssociation(entry.word);
      out.innerHTML=`<div class="captureResult"><h3>${esc(entry.word)}</h3><div class="cn">${esc(entry.meaning_zh||'—')}</div><div class="captureGrid"><div class="captureChip"><b>词性 / 音标</b>${esc(entry.pos||'—')} · ${esc(entry.phonetic||'—')}</div><div class="captureChip"><b>关联方式</b>${esc(entry.association_type||'—')}</div><div class="captureChip"><b>日常场景</b>${esc(entry.daily_scene||'—')}</div><div class="captureChip"><b>工程场景</b>${esc(entry.engineering_scene||'—')}</div></div><div style="margin-top:10px"><b>关联记忆组</b><div class="captureAssoc">${finalAssoc.length?finalAssoc.map(x=>`<span>${esc(x.word)}</span>`).join(''):related.map(x=>`<span>${esc(x)}</span>`).join('')||'<span>暂无可靠关联</span>'}</div></div><p><b>搭配：</b>${esc(entry.collocations.join(', ')||'—')}</p><p><b>例句：</b>${esc(entry.example_en||'—')}<br><span class="tr">${esc(entry.example_zh||'')}</span></p><p class="small">${same?'这个词已存在于现有词库，本次分析不会重复添加。':'✓ 已加入“我的生词”，并可进入现有学习/复习体系。'}</p><button class="cta blue" id="openGenerated">打开完整词卡</button></div>`;
      $id('openGenerated').onclick=()=>{ $id('captureModal').classList.remove('show'); detailByWord(entry.word); };
      bindCapturePersonal();
    }catch(e){out.innerHTML=`<div class="captureResult"><b>智能分析未完成</b><div class="status">${esc(e.message||'接口调用失败')}。你可以检查 Endpoint、Key、Model 以及网络/CORS 设置。</div><div class="captureHint">本地词库检查和关联识别仍然有效；没有成功的 AI 结果不会写入个人词库。</div></div>`}
  };
  bindCapturePersonal();
}
function bindCapturePersonal(){document.querySelectorAll('[data-personal-detail]').forEach(b=>b.onclick=()=>{const w=b.dataset.personalDetail;$id('captureModal').classList.remove('show');detailByWord(w)})}
function openCapture(){renderCapture();$id('captureModal').classList.add('show');setTimeout(()=>$id('captureWord')?.focus(),60)}

'''
s=s.replace(needle,func+needle,1)
# Change cache version condition 156 to 157, fetch vocab v=157, cache cleanup string
s=s.replace("!==\'156\'","!==\'157\'",1)
s=s.replace("localStorage.setItem('dceng_dict_cache_version','156')","localStorage.setItem('dceng_dict_cache_version','157')")
s=s.replace("fetch('./vocab.json?v=154')","fetch('./vocab.json?v=157')")
# Add capture button and personal count to Mine, without changing other settings
needle='<div class="panel"><b>当前学习统计</b>'
add='<div class="panel"><b>遇到新词</b><p class="small">真实工作中遇到的词，可以直接交给 AI 完善：释义、关联记忆组、搭配、日常/工程场景和例句。</p><button type="button" class="cta blue" onclick="openCapture()">✨ 智能收词</button><p class="small" style="margin-bottom:0">我的生词：<b>'+"${personalVocab.length}"+'</b> 个</p></div>'
s=s.replace(needle,add+needle,1)
# Add capture close handlers near closeBtn
needle="$id('closeBtn').onclick=()=>{$id('modal').classList.remove('show')};"
add=needle+"\n$id('captureClose').onclick=()=>{$id('captureModal').classList.remove('show')};\n$id('captureModal').onclick=e=>{if(e.target.id==='captureModal')$id('captureModal').classList.remove('show')};"
s=s.replace(needle,add,1)
# Merge personal vocab after fetch loaded
old="then(d=>{items=d.entries||[];lastDateKey=today();render();scheduleMidnightRefresh();scheduleGreetingRefresh()})"
new="then(d=>{items=d.entries||[];mergePersonalVocab();lastDateKey=today();render();scheduleMidnightRefresh();scheduleGreetingRefresh()})"
s=s.replace(old,new,1)
# Update initial version label and README separately later
s=s.replace('V1.56：基于 V1.54 优化词源分组学习计划，并加入 pose 词源家族；无内置音频。','V1.57：基于 V1.56 增加 AI 智能收词、自动查词库、关联记忆组与场景生成；无内置音频。')
p.write_text(s,encoding='utf-8')
