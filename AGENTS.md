# 给 agent 的说明

本仓库是一个 skill：**小说创作辅助工作流（灵感→分场细纲）**。

- 用户想把一个灵感、点子、画面或人物发展成小说故事，想写大纲、细纲、分场表或情节骨架时：先完整阅读 `SKILL.md`，严格按其中的全程规则和流程执行。
- 你的工具和 Claude 应用不同时（没有弹窗提问、没有可评论的文档），按 `SKILL.md` 的“工具适配”一节换成等价做法。
- 进入第2步前读 `references/story-framework.md`；给知识点时照 `references/knowledge.md` 原文，一个字不改。
- 建档用 `assets/templates/work-file-template.md`；拿不准颗粒度、表格格式或候选写法时，看 `examples/xiao-laohu/`。
- 本 skill 做到第3步分场就停。用户要写正文时，改用姊妹 skill outline-to-prose（https://github.com/1d-a/outline-to-prose），把编剧档案交给它。
- 不要改动本仓库里的参考原文和模板；每部作品的档案放在作品自己的位置。
