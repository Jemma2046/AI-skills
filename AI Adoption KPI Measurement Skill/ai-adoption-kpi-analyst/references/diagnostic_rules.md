# AI Adoption Diagnostic Rules

## 目录

1. [Overview](#overview)
2. [Gap Classification Matrix](#gap-classification-matrix)
3. [Root Cause Analysis Framework](#root-cause-analysis-framework)
4. [Output Templates](#output-templates)
5. [Decision Trees](#decision-trees)

---

## Overview

诊断规则定义了如何将 KPI 数据转化为可执行的改进建议，包括：
- 差距分类（Gap Classification）
- 根因分析（Root Cause Analysis）
- 改进优先级（Improvement Prioritization）

---

## Gap Classification Matrix

### 4 大差距类型

| Gap Type | 英文名 | 核心症状 | KPI 关联 |
|----------|--------|----------|----------|
| 使用不足 | Low Usage | 偶尔使用、无规律、场景局限 | Usage < 60% |
| 效率偏低 | Low Productivity | 修改率高、效率提升不明显 | Productivity < 15% |
| 信心不足 | Low Confidence | 频繁求助、回避复杂任务 | Confidence < 50% |
| 熟练度低 | Low Proficiency | 提示词简单、效果不稳定 | Proficiency < 60% |

### 差距严重程度

| Severity | 定义 | 响应时间 | 干预级别 |
|----------|------|----------|----------|
| Critical | 单 KPI < 阈值 40% | 24 小时内 | 紧急干预 |
| Warning | 单 KPI 40-60% | 1 周内 | 重点关注 |
| Good | 单 KPI 60-80% | 2 周内 | 持续优化 |
| Excellent | 单 KPI >= 80% | 1 个月内 | 保持领先 |

---

## Root Cause Analysis Framework

### 5-Why 根因分析法

对每个差距追问 5 层为什么，追溯到根本原因：

#### Low Usage 根因链

```
Q1: 为什么使用率低？
A: 不知道 AI 能做什么

Q2: 为什么会不知道？
A: 没有看到与自己工作相关的案例

Q3: 为什么没有案例？
A: 培训材料与业务场景脱节

Q4: 为什么培训材料脱节？
A: 没有针对不同角色的定制内容

Q5: 为什么不定制？
A: 采用统一培训策略，未分层分级

Root Cause: 缺乏角色定制化的培训策略
```

#### Low Productivity 根因链

```
Q1: 为什么效率提升不明显？
A: 输出需要大量修改

Q2: 为什么会大量修改？
A: 提示词不够清晰具体

Q3: 为什么提示词不够清晰？
A: 不了解结构化提示词方法

Q4: 为什么不学习提示词方法？
A: 缺乏简单易懂的教程

Q5: 为什么不提供教程？
A: 认为 AI 使用不需要培训

Root Cause: 缺乏系统性提示词培训
```

### 根因分类框架

每个差距的根因分为三类：

| 类别 | Low Usage | Low Productivity | Low Confidence | Low Proficiency |
|------|-----------|------------------|----------------|-----------------|
| **认知障碍** | 不知道能做什么 | 不了解优化方法 | 不知道边界 | 不懂结构化方法 |
| **环境障碍** | 访问不便 | 工作流未整合 | 失败压力大 | 缺乏练习机会 |
| **技能障碍** | 找不到场景 | 提示词设计差 | 不敢试复杂任务 | 术语使用不准 |

---

## Output Templates

### Section 1: KPI Summary Template

```markdown
AI Adoption KPI Summary
========================

Overall Score: {total_score}/100
├─ Usage Rate: {usage_score}/25
├─ Productivity: {productivity_score}/25
├─ Confidence: {confidence_score}/25
└─ Proficiency: {proficiency_score}/25

KPI Status:
[{usage_bar}] Usage: {usage_pct}% - {usage_status}
[{productivity_bar}] Productivity: {productivity_pct}% - {productivity_status}
[{confidence_bar}] Confidence: {confidence_pct}% - {confidence_status}
[{proficiency_bar}] Proficiency: {proficiency_pct}% - {proficiency_status}

Primary Gap: {primary_gap}
Secondary Gap: {secondary_gap}
```

### Section 2: Gap Diagnosis Template

```markdown
## Gap #{n}: {gap_name}

**Severity**: {severity}
**Current Status**: {current_value}%
**Target**: {target_value}%

### Symptoms (症状表现)
{foreach symptom in symptoms}
- {symptom}
{/foreach}

### Root Cause Analysis (根本原因)
**Root Cause**: {root_cause}
**Category**: {cause_category} (认知/环境/技能)
**Impact Assessment**: {impact_description}

### Why-Why Chain (5-Why 追问)
1. Why: {symptom}
   Answer: {reason_1}
2. Why: {reason_1}
   Answer: {reason_2}
3. Why: {reason_2}
   Answer: {reason_3}
4. Why: {reason_3}
   Answer: {reason_4}
5. Why: {reason_4}
   Answer: {root_cause}
```

### Section 3: Improvement Recommendations Template

```markdown
## Targeted Improvement Recommendations

### Gap: {gap_name}

| Priority | Improvement Method | Expected Effect | Difficulty | Timeline |
|----------|-------------------|-----------------|------------|----------|
| P0 | {p0_method} | {p0_effect} | Low | {p0_time} |
| P1 | {p1_method} | {p1_effect} | Medium | {p1_time} |
| P2 | {p2_method} | {p2_effect} | High | {p2_time} |

### Immediate Actions (1-2 天内)
1. {action_1}
2. {action_2}
3. {action_3}

### Short-term Plan (1-4 周)
- {plan_item_1}
- {plan_item_2}
```

### Section 4: Learning Path Template

```markdown
## Personalized Learning Path

**Duration**: {weeks} weeks
**Weekly Commitment**: {hours} hours
**Target**: {target_description}

{foreach week in weeks}
### Week {week_num}: {theme}
- **Goal**: {goal}
- **Daily Practice**:
  - Day 1-2: {day_1_2_task}
  - Day 3-4: {day_3_4_task}
  - Day 5-7: {day_5_7_task}
- **Micro-Tutorial**: {micro_tutorial}
- **Success Metric**: {success_metric}
{/foreach}
```

### Section 5: Prompt Templates Template

```markdown
## Role-Specific Ready-to-Use Prompts

### Prompt #{n}: {prompt_name}

**Scenario**: {applicable_scenario}
**Role**: {target_role}

```
{complete_prompt_template}
```

**Customization Notes**:
- {customization_note_1}
- {customization_note_2}

**Example Input**: {example_input}
**Expected Output**: {expected_output}
```

### Section 6: Reusable Templates Template

```markdown
## Reusable Prompt Templates

### Template #{n}: {template_name}

**Pattern**: {pattern_description}
**Original Usage**: {original_usage}
**Generalized Applications**: {generalized_applications}

**Template Code**:
```
{parameterized_template}
```

**Variations**:
- Variant 1: {variation_1}
- Variant 2: {variation_2}
- Variant 3: {variation_3}
```

---

## Decision Trees

### Gap Identification Decision Tree

```
Start: KPI Report
│
├─ Is Usage < 60%?
│   ├─ YES → Low Usage Gap
│   └─ NO
│
├─ Is Productivity < 15%?
│   ├─ YES → Low Productivity Gap
│   └─ NO
│
├─ Is Confidence < 50%?
│   ├─ YES → Low Confidence Gap
│   └─ NO
│
└─ Is Proficiency < 60%?
    ├─ YES → Low Proficiency Gap
    └─ NO → No Significant Gap
```

### Root Cause Decision Tree

```
Gap Type: Low Usage
│
├─ Can user describe AI capabilities?
│   ├─ NO → Awareness Root Cause
│   └─ YES
│
├─ Is AI easily accessible?
│   ├─ NO → Access Root Cause
│   └─ YES
│
├─ Is AI integrated into workflow?
│   ├─ NO → Workflow Root Cause
│   └─ YES
│
└─ Does user trust AI output?
    ├─ NO → Trust Root Cause
    └─ YES → Relevance Root Cause
```

### Improvement Priority Decision Tree

```
Gap: {identified_gap}
│
├─ Is gap Critical (immediate risk)?
│   ├─ YES → P0 Immediate Action Required
│   └─ NO
│
├─ Can fix be implemented in 1-2 days?
│   ├─ YES → P0 Quick Win
│   └─ NO
│
├─ Does fix require training?
│   ├─ YES → P1 Training Intervention
│   └─ NO
│
└─ Does fix require process change?
    ├─ YES → P2 Process Redesign
    └─ NO → P1 Tool/Template Adjustment
```

---

## Diagnostic Examples

### Example 1: Low Usage

**Situation**: Usage KPI = 35% (Critical)

**Diagnosis**:
1. Survey shows users don't know what AI can do
2. No role-specific use cases documented
3. AI access requires VPN (inconvenient)
4. No success stories shared

**Root Cause**: Awareness + Access barriers

**Recommendations**:
- P0: Share 5 quick wins per role (1 day)
- P0: Simplify AI access path (3 days)
- P1: Create role-specific use case library (1 week)
- P2: Embed AI in daily workflow tools (2 weeks)

### Example 2: Low Productivity

**Situation**: Productivity KPI = 12% (Warning)

**Diagnosis**:
1. Average revision ratio = 45%
2. Users report "AI output needs too much editing"
3. Most prompts are short, single sentences
4. No structured template usage

**Root Cause**: Prompt Design Skills Gap

**Recommendations**:
- P0: Distribute structured prompt templates (1 day)
- P0: Train on context provision (2 days)
- P1: Establish iteration workflow (1 week)
- P2: Advanced prompt engineering training (2 weeks)

### Example 3: Low Confidence

**Situation**: Confidence KPI = 42% (Warning)

**Diagnosis**:
1. Help request rate = 58%
2. Complex task rate = 12%
3. Exit interviews mention "afraid of making mistakes"
4. No safe environment for experimentation

**Root Cause**: Psychological Safety Gap

**Recommendations**:
- P0: Establish "safe to fail" policy (1 day)
- P0: Share success stories (2 days)
- P1: Progressive challenge ladder (1 week)
- P2: Mentorship pairing program (2 weeks)

### Example 4: Low Proficiency

**Situation**: Proficiency KPI = 38% (Critical)

**Diagnosis**:
1. Structured prompt usage = 15%
2. Compliance rate = 45%
3. No understanding of Role-Task-Context-Output framework
4. Terms like "context" and "constraints" not used

**Root Cause**: Knowledge Gap in Prompt Engineering

**Recommendations**:
- P0: Basic prompt structure workshop (2 hours)
- P0: Create prompt template library (3 days)
- P1: Hands-on practice exercises (1 week)
- P2: Advanced techniques training (2 weeks)
