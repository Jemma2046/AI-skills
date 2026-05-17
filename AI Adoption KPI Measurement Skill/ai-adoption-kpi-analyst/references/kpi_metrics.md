# AI Adoption KPI Metrics Definition

## 目录

1. [Overview](#overview)
2. [4 Core KPIs](#4-core-kpis)
3. [Metric Calculation Formulas](#metric-calculation-formulas)
4. [Threshold Standards](#threshold-standards)
5. [Data Collection Requirements](#data-collection-requirements)

---

## Overview

AI Adoption KPI 系统基于企业 AI 工具的被动遥测数据，实时计算 4 大核心维度：

| KPI | 衡量内容 | 满分 |
|-----|----------|------|
| Usage | 使用频率与活跃度 | 25 |
| Productivity | 效率提升与产出质量 | 25 |
| Confidence | 自主使用与复杂任务挑战 | 25 |
| Proficiency | 提示词能力与最佳实践 | 25 |

**总分**: 100 分 (4 KPI 各 25 分)

---

## 4 Core KPIs

### 1. Usage（使用率）

**定义**: 衡量员工实际使用 AI 工具的频率和覆盖度

**核心指标**:
- DAU (Daily Active Users): 日活跃用户数
- WAU (Weekly Active Users): 周活跃用户数
- MAU (Monthly Active Users): 月活跃用户数
- Active User Rate: 活跃用户占比

**计算公式**:
```
Usage Score = (WAU / Total Users) × 25
```

**数据来源**:
- 遥测日志中的 `user_id`、`timestamp`、`event_type`

---

### 2. Productivity（生产力）

**定义**: 衡量 AI 使用带来的效率提升和工作产出质量

**核心指标**:
- Time Efficiency Gain: 时间效率提升
- Task Completion Rate: 任务完成率
- Revision Ratio: 输出修改率（越低越好）
- Quality Output Rate: 高质量输出比例

**计算公式**:
```
# 效率提升
Time Efficiency = (Baseline Time - Actual Time) / Baseline Time × 100%

# 生产力得分
Productivity Score = (Time Efficiency × 0.7 + Completion Rate × 0.5 - Revision Penalty × 0.3) / 100 × 25
```

**数据来源**:
- 遥测日志中的 `completion_time_seconds`、`status`、`revision_ratio`

---

### 3. Confidence（信心度）

**定义**: 衡量员工自主使用 AI 的意愿和面对复杂任务的信心

**核心指标**:
- Self-Service Rate: 自助服务率（不求助比例）
- Complex Task Rate: 复杂任务尝试率
- Escalation Rate: 升级求助率（越低越好）
- Independent Success Rate: 独立成功率

**计算公式**:
```
Confidence Score = (Self-Service Rate × 0.7 + Complex Task Rate × 0.3) / 100 × 25
```

**数据来源**:
- 遥测日志中的 `help_requested`、`is_complex`、`event_type`

---

### 4. Proficiency（熟练度）

**定义**: 衡量员工使用 AI 的技能水平，包括提示词质量和合规性

**核心指标**:
- Prompt Quality Score: 提示词质量评分
- Structured Prompt Rate: 结构化提示词使用率
- Compliance Rate: 合规使用率
- Output Stability: 输出稳定性

**计算公式**:
```
Proficiency Score = (Prompt Quality × 0.7 + Compliance Rate × 0.3) / 100 × 25
```

**数据来源**:
- 遥测日志中的 `prompt_quality_score`、`is_structured`、`compliant`

---

## Metric Calculation Formulas

### 提示词质量评分算法

```python
def calculate_prompt_quality_score(prompt_features):
    """
    prompt_features: {
        'has_role': bool,
        'has_task': bool,
        'has_context': bool,
        'has_constraints': bool,
        'has_output_format': bool,
        'length': int,
        'has_examples': bool,
    }
    """
    weights = {
        'has_role': 15,
        'has_task': 25,
        'has_context': 20,
        'has_constraints': 15,
        'has_output_format': 15,
        'has_examples': 10,
    }
    
    base_score = sum(score for feature, score in weights.items() if prompt_features.get(feature))
    
    # 长度调整（过长或过短都扣分）
    optimal_length = (50, 500)  # 字符数范围
    if prompt_features['length'] < optimal_length[0]:
        base_score *= 0.9
    elif prompt_features['length'] > optimal_length[1]:
        base_score *= 0.95
    
    return min(100, base_score)
```

### 输出修改率计算

```python
def calculate_revision_ratio(initial_output, final_output):
    """
    计算修改率 = 修改字符数 / 总字符数
    """
    if not initial_output or not final_output:
        return 0
    
    initial_len = len(initial_output)
    final_len = len(final_output)
    
    # 简单比较：字符差异比例
    diff_ratio = abs(final_len - initial_len) / max(initial_len, final_len)
    
    return min(100, diff_ratio * 100)
```

### 效率提升计算

```python
def calculate_efficiency_gain(baseline_time, actual_time, baseline_output_quality, actual_output_quality):
    """
    综合效率提升计算
    """
    if baseline_time <= 0:
        return 0
    
    time_gain = (baseline_time - actual_time) / baseline_time
    
    # 质量调整因子
    quality_factor = actual_output_quality / baseline_output_quality if baseline_output_quality > 0 else 1
    
    efficiency_gain = (time_gain * 0.7 + (quality_factor - 1) * 0.3) * 100
    
    return max(0, efficiency_gain)
```

---

## Threshold Standards

### 阈值定义表

| KPI | 指标 | Excellent (绿) | Good (黄) | Warning (橙) | Critical (红) |
|-----|------|----------------|-----------|--------------|---------------|
| Usage | Active User Rate | >= 80% | >= 60% | >= 40% | < 40% |
| Productivity | Efficiency Gain | >= 30% | >= 15% | >= 5% | < 5% |
| Confidence | Self-Service Rate | >= 75% | >= 50% | >= 25% | < 25% |
| Proficiency | Prompt Quality | >= 80 | >= 60 | >= 40 | < 40 |

### 阈值配置 (JSON 格式)

```json
{
  "usage": {
    "excellent": 80,
    "good": 60,
    "warning": 40,
    "critical": 0
  },
  "productivity": {
    "excellent": 30,
    "good": 15,
    "warning": 5,
    "critical": 0
  },
  "confidence": {
    "excellent": 75,
    "good": 50,
    "warning": 25,
    "critical": 0
  },
  "proficiency": {
    "excellent": 80,
    "good": 60,
    "warning": 40,
    "critical": 0
  }
}
```

### 调整阈值建议

**场景 1: 早期采用阶段**
- 目标：验证工具可用性
- 建议：降低 Excellent 阈值至 60%，鼓励早期用户

**场景 2: 大规模推广阶段**
- 目标：快速提升覆盖率
- 建议：强调 Usage KPI，权重提升至 30%

**场景 3: 深度应用阶段**
- 目标：提升使用质量和效率
- 建议：强调 Proficiency 和 Productivity，权重各提升

---

## Data Collection Requirements

### 遥测日志格式 (JSONL)

每行一条遥测事件记录：

```json
{
  "event_id": "evt_20240115_001",
  "timestamp": "2024-01-15T10:30:00Z",
  "user_id": "user_12345",
  "user_role": "engineer",
  "session_id": "sess_abc123",
  "event_type": "task_complete",
  "task_type": "code_generation",
  "is_complex": false,
  "prompt_quality_score": 75,
  "is_structured": true,
  "revision_ratio": 15.5,
  "completion_time_seconds": 45,
  "status": "completed",
  "help_requested": false,
  "compliant": true,
  "satisfaction_score": 4.5
}
```

### 必需字段

| 字段 | 类型 | 描述 | 用途 |
|------|------|------|------|
| event_id | string | 事件唯一标识 | 追踪 |
| timestamp | string | ISO 8601 时间戳 | 时间分析 |
| user_id | string | 用户唯一标识 | 用户统计 |
| event_type | string | 事件类型 | 行为分析 |
| status | string | 任务状态 | 质量分析 |

### 可选字段

| 字段 | 类型 | 描述 | 用途 |
|------|------|------|------|
| prompt_quality_score | number | 提示词质量评分 | Proficiency 计算 |
| revision_ratio | number | 输出修改率 | Productivity 计算 |
| completion_time_seconds | number | 完成时间 | Productivity 计算 |
| help_requested | boolean | 是否求助 | Confidence 计算 |
| is_complex | boolean | 是否复杂任务 | Confidence 计算 |
| satisfaction_score | number | 满意度评分 | 综合分析 |

### 数据采集最佳实践

1. **匿名化处理**: user_id 应为脱敏后的唯一标识，不包含个人信息
2. **频率控制**: 采集频率建议 1 次/会话，避免过度采集
3. **延迟批量**: 可批量发送遥测数据，减少网络开销
4. **敏感过滤**: 不采集具体任务内容，仅采集行为指标

---

## 示例数据

### 遥测日志示例

```jsonl
{"event_id":"e1","timestamp":"2024-01-15T09:00:00Z","user_id":"u001","user_role":"analyst","session_id":"s1","event_type":"task_start","task_type":"data_analysis"}
{"event_id":"e2","timestamp":"2024-01-15T09:00:30Z","user_id":"u001","user_role":"analyst","session_id":"s1","event_type":"task_submit","task_type":"data_analysis","prompt_quality_score":70,"is_structured":true}
{"event_id":"e3","timestamp":"2024-01-15T09:02:00Z","user_id":"u001","user_role":"analyst","session_id":"s1","event_type":"task_complete","task_type":"data_analysis","completion_time_seconds":90,"status":"completed","help_requested":false,"compliant":true}
{"event_id":"e4","timestamp":"2024-01-15T10:00:00Z","user_id":"u002","user_role":"developer","session_id":"s2","event_type":"task_start","task_type":"code_generation","is_complex":true}
{"event_id":"e5","timestamp":"2024-01-15T10:05:00Z","user_id":"u002","user_role":"developer","session_id":"s2","event_type":"help_request","task_type":"code_generation"}
```

### KPI 报告示例

```json
{
  "overall": {
    "total_score": 68,
    "max_score": 100,
    "percentage": 68,
    "status": "Proficient"
  },
  "kpis": {
    "usage": {"score": 18.5, "max_score": 25, "percentage": 74, "status": "Good"},
    "productivity": {"score": 15.2, "max_score": 25, "percentage": 20.5, "status": "Warning"},
    "confidence": {"score": 19.0, "max_score": 25, "percentage": 76, "status": "Excellent"},
    "proficiency": {"score": 15.3, "max_score": 25, "percentage": 61, "status": "Good"}
  }
}
```
