# Prompt One-Click Optimize — User Guide

---

## 1. Skill Positioning

**prompt-one-click-optimize** is an intelligent prompt optimization skill. Its core mission: **perform structured rewriting and expression upgrades on your original prompt, producing a clearer, sharper, and more executable optimized version.**

It does not replace your intent — it reinforces it. You say what you want; it helps you say it better.

<img width="1239" height="354" alt="image" src="https://github.com/user-attachments/assets/1ce47f5a-5bd4-4736-bf50-723de8fbac6f" />

---

## 2. Core Capabilities

| Capability Dimension | What It Does | What Problem It Solves |
|----------------------|-------------|------------------------|
| Structural Optimization | Role definition, task decomposition, output format specification | Prompt "says something but not clearly" — model understanding drifts |
| Expression Optimization | Remove ambiguity, clarify boundaries, add constraints | Prompt "says something but is interpreted differently" — outputs are uncontrolled |
| Effect Enhancement | Example injection, layered instructions, error handling guidance | Prompt "is clear but poorly executed" — results are low quality |

---

## 3. Trigger Methods

Simply express **the intent to optimize a prompt** in conversation — no manual loading required. Typical trigger phrases:

- "Help me optimize this prompt"
- "One-click optimize this prompt"
- "Improve this prompt, make it more concise"
- "This prompt isn't working well, help me rewrite it"
- "Optimize this for Claude specifically"

**Key signal words**: `optimize`, `one-click optimize`, `improve`, `rewrite` + `prompt`

---

## 4. Optimization Workflow

Upon receiving an optimization request, the skill executes the following five steps:

```
Receive Original Prompt → Analyze Current Structure → Fill In Missing Elements → Output Optimized Version → Briefly Explain Changes
```

**Step 1: Receive Original Prompt**
The raw text provided by the user — it may be a paragraph, a structured instruction, or even a vague one-liner.

**Step 2: Analyze Current Structure**
Cross-reference against the "Structure Checklist" (see Section 5) to identify missing or weak elements in the original prompt.

**Step 3: Fill In Missing Elements**
Address each gap in priority order, ensuring every layer is properly covered.

**Step 4: Output Optimized Version**
Produce a complete, ready-to-use optimized prompt that preserves the original intent without deviation.

**Step 5: Briefly Explain Changes**
List what was added and what was improved, so the user understands not just the result but the reasoning.

---

## 5. Structure Checklist (Core Framework)

During optimization, check each layer below item by item — fill in whatever is missing:

| Layer | Element | Optimization Focus | Common Pitfall |
|-------|---------|--------------------|----------------|
| **Role Definition** | Identity / Capability | Specify the role the AI plays, including domain background and capability boundaries | "You are an assistant" — too vague, no professional anchor |
| **Task Description** | Input / Output | Clearly define input format and expected output format | Only says "help me write" — no mention of audience, length, or style |
| **Constraints** | Prohibitions / Limits | Explicitly state what not to do and where boundaries lie | No constraints — the model goes off the rails |
| **Example Injection** | Few-shot | Provide 2-3 typical input-output examples | Instructions only, no examples — the model guesses the output format |
| **Error Handling** | Edge Cases | Define how to handle problems or ambiguous inputs | On vague input, the model fabricates rather than asking for clarification |

---

## 6. Output Format Specification

After each optimization, output in the following standardized format:

```markdown
## Original Prompt
[The user's original text]

## Optimized Prompt
[The complete optimized prompt]

## Optimization Notes
- Added: [What was specifically added]
- Improved: [What was specifically changed]
```

---

## 7. Use Cases & Examples

### Case 1: Direct Optimization

> **User**: Help me optimize — "Write an article about AI"

**Optimization Focus**: Missing role definition, vague task description, no constraints, no examples, no error handling → all five layers need to be filled in

---

### Case 2: Goal-Oriented Optimization

> **User**: Optimize this prompt, make it more concise

**Optimization Focus**: Compress redundant expressions while preserving completeness — remove unnecessary qualifiers, merge instructions at the same level

---

### Case 3: Model-Specific Optimization

> **User**: Optimize this for Claude specifically

**Optimization Focus**: Adjust instruction style for the target model's characteristics (e.g., Claude prefers XML tag structures, is more responsive to "do not" instructions, etc.)

---

### Case 4: Batch Optimization

> **User**: Optimize all 5 of these prompts for me

**Optimization Focus**: Optimize each individually, maintain stylistic consistency, prioritize efficiency, use a uniform output format

---

## 8. Optimization Principles

1. **Do not alter core intent** — Optimization is reinforcement, not replacement. What the user wants to say must be expressed more precisely, not swapped for something else.
2. **Ready to use** — The optimized prompt should be usable as-is, requiring no secondary processing.
3. **General-first** — If no model is specified, optimize using universal best practices; if a model is specified, adapt accordingly.
4. **Avoid over-engineering** — Longer is not better. Redundant structure dilutes core instructions. Every sentence must earn its place.

---

## 9. Quick Self-Check: Does Your Prompt Need Optimization?

If your prompt shows any of the following signals, it's time to trigger optimization:

- [ ] AI output frequently deviates from your expectations
- [ ] No role definition in the prompt
- [ ] Expected output format is not specified
- [ ] No constraints or boundaries are set
- [ ] No examples are provided
- [ ] Running the same prompt at different times produces very different results
- [ ] The prompt exceeds 500 words but the core instruction is only one sentence

---

*A prompt is a contract between you and AI. Writing it well is not about pleasing the model — it's about precisely conveying your intent.*


# 提示词一键优化 — 操作指南

---

## 一、技能定位

**prompt-one-click-optimize** 是一项智能提示词优化技能，核心使命是：**对你提供的原始提示词进行结构化重写与表达升级，生成更清晰、更精准、更易执行的优化版本。**

它不做意图替换，只做意图强化。你想要什么，它帮你表达得更到位。

<img width="1239" height="354" alt="image" src="https://github.com/user-attachments/assets/812398ab-e386-4f3f-a32f-db5d67f43757" />

---

## 二、核心能力

| 能力维度 | 做什么 | 解决什么问题 |
|----------|--------|-------------|
| 结构优化 | 角色定义、任务拆解、输出格式规范 | 提示词"说了但没说清"，模型理解漂移 |
| 表达优化 | 去除歧义、明确边界、增加约束 | 提示词"说了但理解不一"，输出不可控 |
| 效果增强 | 示例注入、分层指令、错误处理指导 | 提示词"说清了但执行不好"，结果质量低 |

---

## 三、触发方式

只需在对话中表达**优化提示词的意图**即可，无需手动加载。典型触发语：

- "帮我优化一下这段提示词"
- "一键优化这个 prompt"
- "改进这段提示词，让它更简洁"
- "这个提示词效果不好，帮我重写"
- "帮我优化，要更适合 Claude 模型"

**关键信号词**：`优化`、`一键优化`、`改进`、`重写` + `提示词/prompt`

---

## 四、优化操作流程

技能接收到优化请求后，按以下五步执行：

```
接收原始提示词 → 分析当前结构 → 逐项补充完善 → 输出优化版本 → 简要说明改动
```

**第1步：接收原始提示词**
用户提供的原始文本，可能是一段话、一段结构化指令，甚至只是一句模糊描述。

**第2步：分析当前结构**
对照"结构检查清单"（见第五节），识别原始提示词中缺少或薄弱的要素。

**第3步：逐项补充完善**
针对缺失项，按优先级依次补充，确保每一层都到位。

**第4步：输出优化版本**
输出可直接使用的完整优化提示词，保持原意不偏移。

**第5步：简要说明改动**
列出做了哪些新增与改进，让用户知其然更知其所以然。

---

## 五、结构检查清单（核心框架）

优化时按以下层级逐项检查，缺什么补什么：
<img width="1604" height="421" alt="image" src="https://github.com/user-attachments/assets/a59da264-a27d-4ac2-bfff-923308126d39" />


| 层级 | 要素 | 优化要点 | 常见问题 |
|------|------|----------|----------|
| **角色定义** | 身份 / 能力 | 明确 AI 扮演的角色，包含领域背景和能力边界 | "你是一个助手"——太泛，没有专业锚点 |
| **任务描述** | 输入 / 输出 | 清晰定义输入格式、期望输出格式 | 只说"帮我写"，没说写给谁、写多长、什么风格 |
| **约束条件** | 禁止 / 限制 | 明确不做什么、边界在哪里 | 没有约束，模型自由发挥导致失控 |
| **示例注入** | Few-shot | 提供 2-3 个典型输入输出示例 | 纯指令无示例，模型靠猜输出格式 |
| **错误处理** | 异常情况 | 定义遇到问题时的处理方式 | 遇到模糊输入时，模型自行编造而非追问 |

---

## 六、输出格式规范

每次优化后，按以下统一格式输出：

```markdown
## 原始提示词
[用户提供的原文]

## 优化后提示词
[优化后的完整提示词]

## 优化说明
- 新增：[具体新增了什么]
- 改进：[具体改动了什么]
```

---

## 七、使用场景与示例

### 场景1：直接优化

> **用户**：帮我优化一下 — "写一篇关于AI的文章"

**优化方向**：角色定义缺失、任务描述模糊、无约束、无示例、无错误处理 → 五项全补

---

### 场景2：带目标的优化

> **用户**：帮我优化这段提示词，要更简洁

**优化方向**：在保证完整性的前提下压缩冗余表达，去除不必要的修饰语，合并同层级指令

---

### 场景3：指定模型的优化

> **用户**：帮我优化，要更适合 Claude 模型

**优化方向**：针对目标模型的特性调整指令风格（如 Claude 偏好 XML 标签结构、对"不要做什么"更敏感等）

---

### 场景4：批量优化

> **用户**：帮我把这 5 个提示词都优化一下

**优化方向**：逐个优化，保持风格一致性，效率优先，输出格式统一

---

## 八、优化原则

1. **不改变核心意图** — 优化是强化，不是替换。用户想说什么，必须说得更到位，而不是换成另一件事。
2. **可直接使用** — 优化后的提示词拿来就能用，不需要二次加工。
3. **通用优先** — 如用户未指定模型，按通用最佳实践优化；指定了模型，则针对性适配。
4. **避免过度工程化** — 提示词不是越长越好，冗余的结构反而稀释核心指令。每一句话都要有存在的理由。

---

## 九、快速自查：你的提示词需要优化吗？

如果你的提示词存在以下任一信号，就该触发优化了：

- [ ] AI 的输出经常偏离你的预期
- [ ] 提示词中没有任何角色定义
- [ ] 没有说明期望的输出格式
- [ ] 没有设定任何约束或边界
- [ ] 没有提供任何示例
- [ ] 不同时候执行同一提示词，结果差异很大
- [ ] 提示词超过 500 字但核心指令只有一句话

---

*提示词是人与 AI 之间的契约。写好它，不是为了讨好模型，而是为了精准传递你的意图。*
