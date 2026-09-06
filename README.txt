DC Engineer English PWA V4

本版本修复：
1. 手机单词/例句播放采用全局 Audio 对象，避免列表按钮播放后立即失效。
2. 列表和详情页改为事件监听，不再使用容易被引号内容破坏的 inline onclick。
3. 保留 StreamElements 在线语音，在线失败自动回退系统语音。
4. 增加 Service Worker 注册。
5. 增加标准 192x192 / 512x512 PNG 图标和完整 Manifest。
6. 增加 Android Chrome 的“安装到手机桌面”提示按钮。
7. 保留原 3538 条词库。

GitHub Pages 根目录需要放：
index.html
manifest.webmanifest
sw.js
vocab.json
icon-192.png
icon-512.png

更新后建议：
- 等 GitHub Pages 部署完成
- Android Chrome 打开网页
- Ctrl+F5 不适用于手机，可在 Chrome 设置中清除该站点缓存，或等待 Service Worker 更新
- 如果页面出现“📲 安装到手机桌面”，直接点击即可
