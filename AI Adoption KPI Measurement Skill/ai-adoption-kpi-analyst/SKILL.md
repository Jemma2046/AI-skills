---
name: ai-adoption-kpi-analyst
description: 企业级AI采用率分析引擎；被动收集使用数据、实时计算4大KPI、诊断能力差距、自动生成个性化学习路径与提示词；赋能AI落地验证ROI
---

# AI Adoption KPI Analyst & Adaptive Enablement Specialist

## 任务目标

本 Skill 用于：为企业 AI Enablement 项目提供实时 KPI 分析与自适应学习赋能。

核心能力：
- AI-Driven Passive Telemetry：自动接收遥测数据，无需手动输入
- 实时 KPI 计算：Usage、Productivity、Confidence、Proficiency 四维评估
- 闭环诊断与建议：识别根因、生成定制化方案、动态调整内容
- ROI 验证：量化效率提升与成本节约

触发场景：分析员工 AI 使用数据、诊断组织 AI 落地卡点、生成个性化赋能方案、验证 AI 投入回报

## 系统架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Enterprise AI Telemetry                       │
│  (嵌入式 Agent 日志: 使用频率、提示词质量、修改率、完成速度)      │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              collect_telemetry.py                                │
│  接收日志 → 数据清洗 → 基础指标计算 → 输出结构化数据              │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              calculate_kpi.py                                    │
│  聚合 WAU/MAU → 计算效率提升 → 信心指数 → 满意度 → 4维KPI评分    │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              generate_recommendations.py                        │
│  根因诊断 → 差距分类 → 生成学习路线/提示词/微教程 → 闭环反馈     │
└─────────────────────────────────────────────────────────────────┘
```

## 核心流程

### 1. 被动遥测数据收集

调用脚本接收遥测数据：

```bash
python scripts/collect_telemetry.py --input ./telemetry_logs.jsonl --output ./processed_metrics.json
```

数据来源（企业 AI 工具嵌入式日志）：
- 使用频率：每日/周活跃用户 (DAU/WAU/MAU)
- 提示词质量：结构化程度、上下文丰富度、术语准确性
- 输出修改率：初稿与终稿差异度
- 任务完成速度：从提交到满意输出的时间
- 合规行为：遵循最佳实践的程度

### 2. KPI 实时计算

```bash
python scripts/calculate_kpi.py --input ./processed_metrics.json --output ./kpi_report.json
```

4 大 KPI 维度（详见 [references/kpi_metrics.md](references/kpi_metrics.md)）：
- **Usage（使用率）**：DAU/WAU/MAU 活跃度
- **Productivity（生产力）**：效率提升比例、任务完成率
- **Confidence（信心度）**：求助率、自主完成任务率、复杂任务尝试率
- **Proficiency（熟练度）**：提示词质量评分、输出稳定性、场景覆盖度

### 3. 诊断与建议生成

```bash
python scripts/generate_recommendations.py --input ./kpi_report.json --output ./recommendations.json
```

完整诊断流程：
1. 识别差距类型（Low Usage / Low Productivity / Low Confidence / Low Proficiency）
2. 根因深度分析（5-Why 追问，区分个人/环境/工具障碍）
3. 生成定制化方案（学习路径、提示词模板、微教程）
4. 闭环反馈（跟踪效果，动态调整内容）

## 闭环机制

```
┌──────────┐    诊断差距    ┌──────────┐    生成方案    ┌──────────┐
│  KPI监控  │ ──────────▶ │  根因分析  │ ───────────▶ │  内容生成 │
└──────────┘              └──────────┘               └──────────┘
     ▲                         │                          │
     │                         ▼                          │
     │                   ┌──────────┐                     │
     │                   │  差距分类 │                     │
     │                   └──────────┘                     │
     │                                                  │
     └─────────────── 效果跟踪与动态调整 ──────────────────┘
```

## 输出格式（固定结构）

详见 [references/diagnostic_rules.md](references/diagnostic_rules.md)：

1. **AI Adoption KPI Summary**：4 维评分雷达图 + 状态标签
2. **Key Gaps & Root-Cause Diagnosis**：每个差距的根因链分析
3. **Targeted Improvement Recommendations**：优先级排序的改进方案
4. **Personalized Learning Path**：周计划 + 微教程
5. **Role-Specific Ready-to-Use Prompts**：3-5 个可直接使用的模板
6. **Reusable Prompt Templates**：高频模式泛化模板

## KPI 阈值标准

| KPI | 健康阈值 | 预警阈值 | 告警阈值 |
|-----|----------|----------|----------|
| Usage (WAU%) | >= 80% | 60-79% | < 60% |
| Productivity (效率提升) | >= 30% | 15-29% | < 15% |
| Confidence (自助率) | >= 75% | 50-74% | < 50% |
| Proficiency (提示词质量) | >= 80 分 | 60-79 分 | < 60 分 |

详见 [references/kpi_metrics.md](references/kpi_metrics.md)

## 资源索引

- 脚本：见 [scripts/collect_telemetry.py](scripts/collect_telemetry.py)（用途：被动遥测数据收集与清洗）
- 脚本：见 [scripts/calculate_kpi.py](scripts/calculate_kpi.py)（用途：4 大 KPI 实时计算）
- 脚本：见 [scripts/generate_recommendations.py](scripts/generate_recommendations.py)（用途：诊断分析与内容生成）
- 参考：见 [references/kpi_metrics.md](references/kpi_metrics.md)（何时读取：需要详细 KPI 定义或调整阈值）
- 参考：见 [references/diagnostic_rules.md](references/diagnostic_rules.md)（何时读取：需要诊断规则或输出模板）
- 参考：见 [references/learning_content_templates.md](references/learning_content_templates.md)（何时读取：生成学习路径或提示词模板）

## 与传统 Enablemnt 的区别

| 维度 | 传统方式 | 本 Skill |
|------|----------|----------|
| 数据收集 | 手动问卷/访谈 | AI-Driven 被动遥测，自动采集 |
| 分析方式 | 人工分析数据 | 实时 KPI 计算，动态监控 |
| 方案生成 | 统一培训材料 | 个性化学习路径，AI 生成 |
| 调整机制 | 季度复盘 | 实时闭环，效果驱动迭代 |
| ROI 验证 | 模糊估算 | 量化效率提升，成本节约计算 |

## 注意事项

- 脚本接收 JSONL 格式遥测日志，输出结构化 JSON 报告
- 所有路径引用相对于 Skill 目录（使用绝对路径或相对路径）
- KPI 阈值可根据企业实际情况在 references/kpi_metrics.md 中调整
- 生成的提示词模板可直接嵌入企业 AI 工具使用
