# Student Career Planning Skill

`delivering-student-career-plans` 是一个面向 Codex 的学生职业规划交付 Skill。它用于把学生简历、问卷、截图和目标方向整理成可执行的职业规划，包含岗位梯度、公司池、薪资参考、项目补强、简历分版、投递节奏与飞书交付验收。

## 安装

克隆仓库：

```bash
git clone https://github.com/Amentman/delivering-student-career-plans.git
```

将整个仓库目录复制或软链接到 Codex Skill 目录：

```bash
ln -s "$(pwd)/delivering-student-career-plans" ~/.codex/skills/delivering-student-career-plans
```

安装后新开一个 Codex 会话，可以使用 `$delivering-student-career-plans` 显式调用，也可让 Codex 根据职业规划请求自动选择。

## 包含内容

- `SKILL.md`：主工作流和事实边界。
- `references/`：输入证据、岗位与项目规划、学生外部版标准、行业研究、飞书交付和 manifest 合同。
- `scripts/validate_delivery.py`：对交付 manifest、飞书读回、正文深度、附件、视觉与父子关系进行验证。
- `scripts/vendor/validate_visual_manifest.py`：为独立仓库打包的视觉 manifest 校验依赖；如已安装完整 `visual-document-delivery` Skill，会优先使用其同级校验器。
- `tests/`：校验器的正向与反向回归测试。

## 验证

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
uv run --with pyyaml python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## 安全边界

- 仓库不包含学生真实材料、生产凭据、私有飞书节点或个人绝对路径。
- 飞书空间、父节点、本地知识库与权限由每个使用者在运行时自行配置。
- 生成完整图文职业规划时仍需安装 `visual-document-delivery`；本仓库随包的只是确保交付校验器可独立运行的最小视觉校验依赖。
- 只有经确认的学生事实才能写成本人经历；推断、行业知识与待确认项必须分开。
