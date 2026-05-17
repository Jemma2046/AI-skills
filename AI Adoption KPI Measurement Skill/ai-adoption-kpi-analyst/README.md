# AI Adoption KPI Analyst & Adaptive Enablement Specialist

企业级 AI 采用率分析引擎 - 将统一培训升级为 AI 自适应学习

---

# English Version

## What

AI continuously analyzes KPI gaps for each employee: insufficient usage, low efficiency, lack of proficiency, etc. Automatically generates personalized learning paths, customized work manuals, dedicated prompts, and micro-tutorials. Dynamically adjusts content based on usage effectiveness until metrics reach targets. Transforms enablement from uniform training to AI-adaptive learning.

## Why

Enterprise AI Enablement is fundamentally not about "teaching people to use AI", but about ensuring AI investments generate real business value and do not waste budgets.

**1. Business Essence: ROI Verification**
Enterprises purchasing AI tools and investing in enablement need to prove value for money, requiring quantification of efficiency gains and cost savings.

**2. Organizational Essence: Determining True AI Adoption**
Not just going through the motions of training. Many enterprises find employees don't use AI after training. KPIs distinguish between formal learning vs. real daily usage.

**3. Management Essence: Identifying Bottlenecks & Iterating Programs**
Low usage, low confidence, and poor satisfaction indicate that prompts, use cases, and training don't align with business needs and require adjustment.

## How

**AI-Driven Passive Telemetry & Real-Time KPI Calculation (AI-Native)**

Deploy embedded agent logging within enterprise AI tools to automatically capture usage metrics, prompt quality, revision ratio, and task completion speed without manual tracking. AI backend aggregates WAU, productivity gain, confidence level, and satisfaction signals in real-time, then auto-generates adoption dashboards and bottleneck alerts.

## How It Works

### Core Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Enterprise AI Telemetry                       │
│         (Embedded Agent Logs: Usage, Prompt Quality, etc.)       │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 1: collect_telemetry.py                        │
│         Receive Logs → Data Cleaning → Basic Metrics            │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 2: calculate_kpi.py                            │
│      WAU Aggregation → Efficiency Gain → Confidence → 4D KPIs  │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 3: generate_recommendations.py                 │
│      Root Cause → Gap Classification → Learning Path/Prompts    │
└─────────────────────────────────────────────────────────────────┘
```

### 4 Core KPI Dimensions

| KPI | What It Measures | Max Score | Core Metrics |
|-----|-----------------|-----------|--------------|
| **Usage** | Usage frequency & activity | 25 | WAU/Total Users |
| **Productivity** | Efficiency gain & output quality | 25 | Efficiency %, Completion Rate, Revision Rate |
| **Confidence** | Self-service & complex task willingness | 25 | Self-Service Rate, Complex Task Rate |
| **Proficiency** | Prompt ability & compliance | 25 | Prompt Quality, Compliance Rate |

### Closed-Loop Feedback Mechanism

```
┌──────────┐    Diagnose Gaps    ┌──────────┐    Generate Plan    ┌──────────┐
│ KPI Monitoring │ ───────────▶ │ Root Cause │ ───────────▶ │ Content Generation │
└──────────┘                └──────────┘                  └──────────┘
     ▲                           │                          │
     │                           ▼                          │
     │                    ┌──────────┐                     │
     │                    │ Gap Classification │                     │
     │                    └──────────┘                     │
     │                                                  │
     └─────────────── Effect Tracking & Dynamic Adjustment ──────────────────┘
```

### Root Cause Diagnosis Process

1. **Collect Data**: Passive telemetry, no manual input required
2. **Calculate KPIs**: Real-time scoring with threshold alerts
3. **Identify Gaps**: Low Usage / Low Productivity / Low Confidence / Low Proficiency
4. **Root Cause Analysis**: 5-Why inquiry, distinguish cognitive/environmental/skill barriers
5. **Generate Plan**: Personalized learning path, prompt templates, micro-tutorials
6. **Closed-Loop Feedback**: Track effects, dynamically adjust until targets are met

## Advantages

| Dimension | Traditional Approach | This Skill |
|-----------|---------------------|------------|
| **Data Collection** | Manual surveys/interviews, time-consuming and inaccurate | AI-Driven passive telemetry, automatic collection, real-time accuracy |
| **Analysis** | Manual data analysis, long cycles, lag | Real-time KPI calculation, dynamic monitoring, timely detection |
| **Plan Generation** | Uniform training materials, one-size-fits-all | Personalized learning paths, AI-generated |
| **Adjustment Mechanism** | Quarterly reviews, long feedback cycles | Real-time closed-loop, effect-driven, rapid iteration |
| **ROI Verification** | Vague estimates, difficult to quantify | Quantified efficiency gains, visible cost savings |
| **Scalability** | Labor-intensive, hard to cover everyone | Automated, scalable to entire organization |

## Quick Start

### 1. Collect Telemetry Data

```bash
python scripts/collect_telemetry.py --input ./telemetry.jsonl --output ./metrics.json
```

### 2. Calculate KPIs

```bash
python scripts/calculate_kpi.py --input ./metrics.json --output ./kpi_report.json
```

### 3. Generate Diagnostic Report

```bash
python scripts/generate_recommendations.py --input ./kpi_report.json --output ./full_report.json
```

## Telemetry Log Format

```jsonl
{"event_id":"e1","timestamp":"2024-01-15T09:00:00Z","user_id":"u001","user_role":"analyst","session_id":"s1","event_type":"task_complete","task_type":"data_analysis","prompt_quality_score":70,"is_structured":true,"completion_time_seconds":90,"status":"completed","help_requested":false,"compliant":true}
```

**Required Fields**: event_id, timestamp, user_id, event_type, status

**Optional Fields**: prompt_quality_score, revision_ratio, completion_time_seconds, help_requested, is_complex, satisfaction_score

## Output Example

### KPI Summary

```
Overall Score: 68/100 (Proficient)

4 Core KPI Scores:
  Usage        [████████████░░░░░░░░░] 74% - Good
  Productivity [██████░░░░░░░░░░░░░] 21% - Warning  
  Confidence   [████████████████░░░░] 76% - Excellent
  Proficiency  [██████████░░░░░░░░░░] 61% - Good
```

### Diagnostic Report

- **Primary Gap**: Productivity - efficiency gains not obvious (root cause: unclear prompt design)
- **Improvement Suggestions**: P0 prompt optimization training, P1 iteration workflow promotion
- **Learning Path**: 4-week personalized path with weekly themes + daily tasks + micro-tutorials
- **Prompt Templates**: 5 role-customized templates ready to use
- **Reusable Patterns**: Identify high-frequency prompts, convert to parameterized templates

## File Structure

```
ai-adoption-kpi-analyst/
├── SKILL.md                              # Skill entry and usage guide
├── scripts/
│   ├── collect_telemetry.py              # Passive telemetry collection
│   ├── calculate_kpi.py                  # 4D KPI real-time calculation
│   └── generate_recommendations.py       # Diagnostic analysis & content generation
├── references/
│   ├── kpi_metrics.md                   # KPI definitions, formulas, thresholds
│   ├── diagnostic_rules.md              # Diagnostic rules, decision trees
│   └── learning_content_templates.md     # Template library, learning paths
└── README.md                            # This file
```

---

---

# 中文版本

## What - 核心功能

AI 持续分析每位员工的 KPI 短板：使用率不足、效率偏低、使用不熟练等。自动生成专属学习路线、定制化工作手册、专属提示词、微型教程，并根据使用效果实时动态调整内容，直到指标达标。赋能由统一培训转为 AI 自适应学习。

## Why - 为什么需要

企业做 AI Enablement，本质不是「教大家用 AI」，而是确保 AI 投入产生真实业务价值、不浪费预算。

**1. 商业本质：验证投资回报 ROI**
企业采购 AI 工具、投入人力做赋能，需要证明钱花得值，必须量化效率提升、成本节约。

**2. 组织本质：判断 AI 有没有真正落地**
不是停留在培训走过场。很多企业培训完员工不用，KPI 就是用来区分形式化学习 vs 真实日常使用。

**3. 管理本质：识别卡点、迭代赋能方案**
使用率低、信心不足、满意度差，说明提示词、用例、培训不贴合业务，需要调整。

## How - 如何实现

**AI-Driven Passive Telemetry & Real-Time KPI Calculation（AI-Native）**

在企业 AI 工具中部署嵌入式 Agent 日志，自动捕获使用频率、提示词质量、修改率、任务完成速度，无需手动追踪。AI 后端实时聚合 WAU、生产力提升、信心指数和满意度信号，自动生成采用率仪表盘和瓶颈告警。

## Skill 原理

### 核心架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Enterprise AI Telemetry                       │
│        嵌入式 Agent 日志: 使用频率、提示词质量、修改率、完成速度) │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 1: collect_telemetry.py                        │
│         接收日志 → 数据清洗 → 基础指标计算 → 结构化数据          │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 2: calculate_kpi.py                            │
│      聚合 WAU → 计算效率提升 → 信心指数 → 满意度 → 4维KPI评分    │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 3: generate_recommendations.py                 │
│      根因诊断 → 差距分类 → 生成学习路线/提示词/微教程            │
└─────────────────────────────────────────────────────────────────┘
```

### 4 大 KPI 维度

| KPI | 衡量内容 | 满分 | 核心指标 |
|-----|----------|------|----------|
| **Usage** | 使用频率与活跃度 | 25 | WAU/总用户数 |
| **Productivity** | 效率提升与产出质量 | 25 | 效率增益、完成率、修改率 |
| **Confidence** | 自主使用与复杂任务挑战 | 25 | 自助率、复杂任务尝试率 |
| **Proficiency** | 提示词能力与合规性 | 25 | 提示词质量、合规率 |

### 闭环反馈机制

```
┌──────────┐    诊断差距    ┌──────────┐    生成方案    ┌──────────┐
│  KPI监控  │ ───────────▶ │  根因分析  │ ───────────▶ │  内容生成 │
└──────────┘              └──────────┘               └──────────┘
     ▲                         │                          │
     │                         ▼                          │
     │                   ┌──────────┐                     │
     │                   │  差距分类 │                     │
     │                   └──────────┘                     │
     │                                                  │
     └─────────────── 效果跟踪与动态调整 ──────────────────┘
```

### 根因诊断流程

1. **收集数据**：被动遥测，无需手动输入
2. **计算 KPI**：实时评分，阈值告警
3. **识别差距**：Low Usage / Low Productivity / Low Confidence / Low Proficiency
4. **根因分析**：5-Why 追问，区分认知/环境/技能障碍
5. **生成方案**：个性化学习路径、提示词模板、微教程
6. **闭环反馈**：跟踪效果，动态调整，直到达标

## 优势对比

| 维度 | 传统方式 | 本 Skill |
|------|----------|----------|
| **数据收集** | 手动问卷/访谈，耗时且不准确 | AI-Driven 被动遥测，自动采集，实时准确 |
| **分析方式** | 人工分析数据，周期长、滞后 | 实时 KPI 计算，动态监控，及时发现 |
| **方案生成** | 统一培训材料，一刀切 | 个性化学习路径，AI 自动生成 |
| **调整机制** | 季度复盘，反馈周期长 | 实时闭环，效果驱动，快速迭代 |
| **ROI 验证** | 模糊估算，难以量化 | 量化效率提升，成本节约可视化 |
| **规模化** | 人力密集，难以覆盖全员 | 自动化的，可扩展至全组织 |

## 快速开始

### 1. 收集遥测数据

```bash
python scripts/collect_telemetry.py --input ./telemetry.jsonl --output ./metrics.json
```

### 2. 计算 KPI

```bash
python scripts/calculate_kpi.py --input ./metrics.json --output ./kpi_report.json
```

### 3. 生成诊断报告

```bash
python scripts/generate_recommendations.py --input ./kpi_report.json --output ./full_report.json
```

## 遥测日志格式

```jsonl
{"event_id":"e1","timestamp":"2024-01-15T09:00:00Z","user_id":"u001","user_role":"analyst","session_id":"s1","event_type":"task_complete","task_type":"data_analysis","prompt_quality_score":70,"is_structured":true,"completion_time_seconds":90,"status":"completed","help_requested":false,"compliant":true}
```

**必需字段**：event_id, timestamp, user_id, event_type, status

**可选字段**：prompt_quality_score, revision_ratio, completion_time_seconds, help_requested, is_complex, satisfaction_score

## 输出示例

### KPI Summary

```
Overall Score: 68/100 (Proficient)

4 大 KPI 评分:
  Usage        [████████████░░░░░░░░░] 74% - Good
  Productivity [██████░░░░░░░░░░░░░] 21% - Warning  
  Confidence   [████████████████░░░░] 76% - Excellent
  Proficiency  [██████████░░░░░░░░░░] 61% - Good
```

### 诊断报告

- **主要差距**：Productivity 效率提升不明显（根因：提示词设计不够清晰）
- **改进建议**：P0 提示词优化培训、P1 迭代工作流推广
- **学习路径**：4 周个性化路径，周主题 + 每日任务 + 微教程
- **提示词模板**：5 个可直接使用的角色定制模板
- **可复用模式**：识别高频提示词，转化为参数化模板

## 文件结构

```
ai-adoption-kpi-analyst/
├── SKILL.md                              # 技能入口与使用指南
├── scripts/
│   ├── collect_telemetry.py              # 被动遥测数据收集
│   ├── calculate_kpi.py                  # 4大KPI实时计算
│   └── generate_recommendations.py       # 诊断分析与内容生成
├── references/
│   ├── kpi_metrics.md                   # KPI定义、公式、阈值
│   ├── diagnostic_rules.md               # 诊断规则、决策树
│   └── learning_content_templates.md     # 模板库、学习路径
└── README.md                            # 本文档
```
