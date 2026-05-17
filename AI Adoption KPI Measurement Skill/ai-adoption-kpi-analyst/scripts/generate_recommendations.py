#!/usr/bin/env python3
"""
AI Adoption Recommendations Generator
基于 KPI 报告进行根因诊断，生成个性化改进建议、学习路径和提示词模板
输入：KPI 报告 JSON 文件
输出：完整诊断报告 JSON 文件
"""

import json
import argparse
import sys
from datetime import datetime
from typing import Dict, List, Any


def parse_arguments():
    parser = argparse.ArgumentParser(description='生成 AI 采用改进建议')
    parser.add_argument('--input', '-i', required=True, help='KPI 报告文件路径 (JSON 格式)')
    parser.add_argument('--output', '-o', required=True, help='建议报告文件路径 (JSON 格式)')
    return parser.parse_args()


# 根因诊断规则
ROOT_CAUSE_RULES = {
    'usage': {
        'symptoms': ['使用率低', '活跃度不稳定', '场景局限'],
        'root_causes': {
            'awareness': '不知道 AI 能解决什么问题',
            'access': '访问路径不便捷或权限限制',
            'workflow': '未将 AI 融入现有工作流程',
            'trust': '对 AI 输出质量不信任',
            'relevance': 'AI 能力与业务需求不匹配',
        }
    },
    'productivity': {
        'symptoms': ['修改率高', '效率提升不明显', '产出不达标'],
        'root_causes': {
            'prompt_design': '提示词设计不够清晰具体',
            'context': '缺乏必要的上下文信息',
            'iteration': '缺乏迭代优化意识',
            'verification': '缺乏输出验证标准',
            'integration': '未充分利用 AI 特性',
        }
    },
    'confidence': {
        'symptoms': ['频繁求助', '不敢尝试复杂任务', '过度依赖'],
        'root_causes': {
            'failure_trail': '失败经历导致心理阴影',
            'model_gap': '缺乏 Mental Model，不知道 AI 边界',
            'example_lack': '缺乏成功案例参考',
            'responsibility': '担心出错承担责任',
            'complexity': '任务难度超出当前能力',
        }
    },
    'proficiency': {
        'symptoms': ['提示词简单', '效果不稳定', '缺乏结构'],
        'root_causes': {
            'structure': '不了解结构化提示词方法',
            'vocabulary': '术语使用不准确',
            'context_building': '不会构建上下文',
            'output_control': '不会控制输出格式',
            'testing': '缺乏测试迭代能力',
        }
    },
}


# 改进建议模板
IMPROVEMENT_TEMPLATES = {
    'usage': {
        'awareness': {
            'priority': 'P0',
            'method': '场景化培训：展示 AI 在用户具体工作场景中的成功案例',
            'expected_effect': '使用率提升 20-30%',
            'difficulty': '低',
        },
        'access': {
            'priority': 'P0',
            'method': '简化访问路径：在常用工具中嵌入 AI 入口',
            'expected_effect': '使用率提升 15-25%',
            'difficulty': '中',
        },
        'workflow': {
            'priority': 'P1',
            'method': '工作流整合：识别高频任务，将 AI 嵌入流程节点',
            'expected_effect': '使用率提升 25-40%',
            'difficulty': '中',
        },
        'trust': {
            'priority': 'P1',
            'method': '透明度提升：展示 AI 决策逻辑和置信度',
            'expected_effect': '使用率提升 10-20%',
            'difficulty': '低',
        },
        'relevance': {
            'priority': 'P2',
            'method': '需求调研：收集实际业务需求，针对性训练',
            'expected_effect': '使用率提升 30-50%',
            'difficulty': '高',
        },
    },
    'productivity': {
        'prompt_design': {
            'priority': 'P0',
            'method': '提示词优化培训：结构化、具体化、角色化',
            'expected_effect': '修改率降低 30-50%',
            'difficulty': '低',
        },
        'context': {
            'priority': 'P0',
            'method': '上下文构建指南：提供背景信息的最佳实践',
            'expected_effect': '修改率降低 20-40%',
            'difficulty': '低',
        },
        'iteration': {
            'priority': 'P1',
            'method': '迭代工作流推广：初稿 -> 反馈 -> 优化的循环',
            'expected_effect': '效率提升 15-25%',
            'difficulty': '中',
        },
        'verification': {
            'priority': 'P1',
            'method': '验收标准清单：明确的输出质量标准',
            'expected_effect': '修改率降低 20-30%',
            'difficulty': '低',
        },
        'integration': {
            'priority': 'P2',
            'method': '高级功能培训：充分利用 AI 特性（多轮对话、文件处理等）',
            'expected_effect': '效率提升 20-35%',
            'difficulty': '高',
        },
    },
    'confidence': {
        'failure_trail': {
            'priority': 'P0',
            'method': '安全失败环境：允许试错，分析失败但不惩罚',
            'expected_effect': '信心指数提升 15-25%',
            'difficulty': '低',
        },
        'model_gap': {
            'priority': 'P0',
            'method': 'Mental Model 构建：明确 AI 能力边界和最佳用例',
            'expected_effect': '信心指数提升 20-30%',
            'difficulty': '中',
        },
        'example_lack': {
            'priority': 'P1',
            'method': '成功案例库：分享最佳实践和成功故事',
            'expected_effect': '信心指数提升 10-20%',
            'difficulty': '低',
        },
        'responsibility': {
            'priority': 'P1',
            'method': '责任明确：AI 作为辅助工具，人工保持最终决策权',
            'expected_effect': '信心指数提升 15-25%',
            'difficulty': '低',
        },
        'complexity': {
            'priority': 'P2',
            'method': '渐进式挑战：从简单任务开始，逐步增加复杂度',
            'expected_effect': '信心指数提升 25-40%',
            'difficulty': '中',
        },
    },
    'proficiency': {
        'structure': {
            'priority': 'P0',
            'method': '结构化提示词培训：Role-Task-Context-Output 框架',
            'expected_effect': '提示词质量提升 30-50%',
            'difficulty': '低',
        },
        'vocabulary': {
            'priority': 'P1',
            'method': '术语指南：AI 友好的专业术语和表达方式',
            'expected_effect': '提示词质量提升 15-25%',
            'difficulty': '低',
        },
        'context_building': {
            'priority': 'P1',
            'method': '上下文构建技巧：背景、约束、示例的提供方法',
            'expected_effect': '提示词质量提升 20-35%',
            'difficulty': '中',
        },
        'output_control': {
            'priority': 'P1',
            'method': '输出格式控制：JSON、Markdown、表格等格式指定',
            'expected_effect': '提示词质量提升 15-25%',
            'difficulty': '低',
        },
        'testing': {
            'priority': 'P2',
            'method': 'A/B 测试方法：提示词版本对比与优化',
            'expected_effect': '提示词质量提升 30-45%',
            'difficulty': '高',
        },
    },
}


# 提示词模板库
PROMPT_TEMPLATES = {
    'writing': {
        'name': '专业写作助手',
        'template': '''你是[角色]，负责[任务类型]撰写。

## 任务
[具体写作任务描述]

## 背景信息
[相关背景、目标受众、用途]

## 要求
1. [格式要求]
2. [风格要求]
3. [字数要求]

## 输出格式
[期望的输出结构]

请生成[具体内容]，确保符合以上要求。''',
        'applicable_scenarios': ['邮件撰写', '报告生成', '文案创作', '文档起草'],
    },
    'analysis': {
        'name': '数据分析解读',
        'template': '''你是数据分析专家，负责解读[数据类型]。

## 数据背景
[数据来源、时间范围、基本情况]

## 分析目标
[需要回答的问题或达成的目标]

## 约束条件
- [分析深度]
- [时间范围]
- [资源限制]

## 输出要求
1. 关键发现（3-5点）
2. 数据支撑
3. 建议行动

请基于提供的数据进行分析。''',
        'applicable_scenarios': ['数据报告解读', '趋势分析', '对比分析', '异常检测'],
    },
    'review': {
        'name': '审查与优化',
        'template': '''你是[领域]专家，负责审查以下内容：

## 待审查内容
[需要审查的文本/代码/文档]

## 审查标准
1. [准确性]
2. [完整性]
3. [规范性]
4. [可执行性]

## 输出格式
- 问题列表（编号）
- 优先级（高/中/低）
- 修改建议

请进行详细审查并提供改进建议。''',
        'applicable_scenarios': ['代码审查', '文档审核', '方案评审', '质量检查'],
    },
    'summarization': {
        'name': '信息摘要提取',
        'template': '''你是信息整理专家，负责提取关键信息。

## 源文档
[需要总结的文档内容]

## 摘要类型
[简要摘要/详细摘要/要点列表]

## 重点关注
- [需要特别关注的内容]
- [需要忽略的内容]

## 输出格式
- 标题
- 核心要点（3-5条）
- 关键细节（如需要）

请生成结构化摘要。''',
        'applicable_scenarios': ['会议纪要', '长文档总结', '新闻摘要', '报告概览'],
    },
    'coding': {
        'name': '代码开发助手',
        'template': '''你是[编程语言]开发专家。

## 任务目标
[需要实现的 功能/特性]

## 技术栈
- 语言：[编程语言]
- 框架：[相关框架]
- 环境：[运行环境]

## 代码要求
1. [性能要求]
2. [安全要求]
3. [可维护性要求]

## 输入输出示例
输入：[示例输入]
输出：[期望输出]

请生成完整的、可直接使用的代码。''',
        'applicable_scenarios': ['代码编写', '代码修复', '代码优化', '技术方案设计'],
    },
}


# 学习路径模板
LEARNING_PATH_TEMPLATE = {
    'week_1': {
        'theme': '基础认知与快速上手',
        'goal': '建立正确的 AI 使用心智模型',
        'daily_practice': {
            'day_1_2': '了解 AI 能力边界：通过 5 个不同类型任务测试 AI 能力',
            'day_3_4': '基础提示词练习：使用结构化模板完成 3 个日常任务',
            'day_5_7': '实践应用：将 AI 应用于1个真实工作场景',
        },
        'micro_tutorial': '结构化提示词 = 角色(Role) + 任务(Task) + 上下文(Context) + 输出格式(Output)',
        'success_metric': '能独立使用结构化提示词完成简单任务',
    },
    'week_2': {
        'theme': '效率提升与质量优化',
        'goal': '掌握提示词优化技巧，提升输出质量',
        'daily_practice': {
            'day_1_2': '上下文构建：学会提供充分的背景信息',
            'day_3_4': '迭代优化：初稿-反馈-优化的工作流',
            'day_5_7': '质量对比：记录优化前后效果差异',
        },
        'micro_tutorial': '好提示词 = 具体描述 + 约束条件 + 示例参考 + 格式指定',
        'success_metric': '输出修改率降低 30% 以上',
    },
    'week_3': {
        'theme': '信心建立与复杂任务',
        'goal': '挑战复杂任务，建立使用信心',
        'daily_practice': {
            'day_1_2': '复杂任务拆解：将大任务分解为可管理的子任务',
            'day_3_4': '多轮对话练习：学会通过追问深化结果',
            'day_5_7': '独立完成1个复杂任务全流程',
        },
        'micro_tutorial': '复杂任务处理：拆解 -> 分步 -> 整合 -> 验证',
        'success_metric': '能独立完成中等复杂度任务',
    },
    'week_4': {
        'theme': '习惯养成与最佳实践',
        'goal': '将 AI 融入日常工作习惯',
        'daily_practice': {
            'day_1_2': '工作流整合：识别可嵌入 AI 的工作节点',
            'day_3_4': '模板积累：建立个人常用提示词模板库',
            'day_5_7': '分享经验：总结 1-2 个成功案例',
        },
        'micro_tutorial': '习惯养成 = 触发场景 + 固定流程 + 效果记录 + 持续优化',
        'success_metric': 'AI 使用频率达到日常工作的 20% 以上',
    },
}


def diagnose_gaps(kpi_report: Dict) -> List[Dict]:
    """诊断差距并分析根因"""
    gaps = []
    
    for gap_info in kpi_report.get('gaps', {}).get('all_gaps', []):
        kpi = gap_info['kpi']
        status = gap_info['status']
        percentage = gap_info['percentage']
        
        # 确定根因
        if kpi == 'usage':
            if percentage < 40:
                root_cause = 'awareness'
            else:
                root_cause = 'workflow'
        elif kpi == 'productivity':
            if percentage < 15:
                root_cause = 'prompt_design'
            else:
                root_cause = 'verification'
        elif kpi == 'confidence':
            if percentage < 50:
                root_cause = 'failure_trail'
            else:
                root_cause = 'complexity'
        else:  # proficiency
            if percentage < 60:
                root_cause = 'structure'
            else:
                root_cause = 'testing'
        
        gaps.append({
            'gap_name': kpi,
            'status': status,
            'current_value': percentage,
            'root_cause': root_cause,
            'root_cause_description': ROOT_CAUSE_RULES[kpi]['root_causes'][root_cause],
            'symptoms': ROOT_CAUSE_RULES[kpi]['symptoms'],
        })
    
    return gaps


def generate_improvements(gaps: List[Dict]) -> List[Dict]:
    """生成改进建议"""
    improvements = []
    
    for gap in gaps:
        kpi = gap['gap_name']
        root_cause = gap['root_cause']
        
        # 获取对应改进模板
        template = IMPROVEMENT_TEMPLATES.get(kpi, {}).get(root_cause, {
            'priority': 'P2',
            'method': '综合培训',
            'expected_effect': '提升 15-20%',
            'difficulty': '中',
        })
        
        improvements.append({
            'kpi': kpi,
            'root_cause': root_cause,
            'priority': template['priority'],
            'method': template['method'],
            'expected_effect': template['expected_effect'],
            'difficulty': template['difficulty'],
        })
    
    # 按优先级排序
    priority_order = {'P0': 0, 'P1': 1, 'P2': 2}
    improvements.sort(key=lambda x: priority_order.get(x['priority'], 3))
    
    return improvements


def generate_learning_path(primary_gap: str) -> Dict:
    """生成个性化学习路径"""
    # 根据主要差距调整学习路径重点
    path = LEARNING_PATH_TEMPLATE.copy()
    
    if primary_gap == 'usage':
        path['week_1']['theme'] = '发现 AI 价值'
        path['week_1']['goal'] = '找到 AI 与自身工作的结合点'
    elif primary_gap == 'productivity':
        path['week_1']['theme'] = '效率工具认知'
        path['week_1']['goal'] = '掌握快速提效的提示词技巧'
    elif primary_gap == 'confidence':
        path['week_1']['theme'] = '安全探索'
        path['week_1']['goal'] = '在低风险环境中建立信心'
    
    return path


def select_prompt_templates(applicable_scenarios: List[str] = None) -> List[Dict]:
    """选择适用的提示词模板"""
    if not applicable_scenarios:
        # 返回所有模板
        return [
            {**template, 'id': template_id}
            for template_id, template in PROMPT_TEMPLATES.items()
        ]
    
    # 根据场景过滤
    selected = []
    for template_id, template in PROMPT_TEMPLATES.items():
        if any(scenario in template['applicable_scenarios'] for scenario in applicable_scenarios):
            selected.append({**template, 'id': template_id})
    
    return selected if selected else list(PROMPT_TEMPLATES.values())[:3]


def extract_reusable_templates(kpi_report: Dict) -> List[Dict]:
    """提取可复用模板模式"""
    # 基于 KPI 分析，推荐适合的模板
    kpis = kpi_report.get('kpis', {})
    
    templates = []
    
    # 根据 proficiency 水平推荐
    prof_score = kpis.get('proficiency', {}).get('score', 0)
    if prof_score < 15:
        # 初学者：推荐结构简单的模板
        templates.append({
            'name': '基础任务执行',
            'pattern': '角色 + 任务 + 期望结果',
            'example': '我是产品经理，请帮我写一份产品需求文档，包含：功能描述、用户故事、验收标准',
            'usage': '适合快速执行明确任务',
        })
    
    # 根据 productivity 推荐
    prod_score = kpis.get('productivity', {}).get('score', 0)
    if prod_score < 15:
        templates.append({
            'name': '迭代优化模板',
            'pattern': '初稿请求 + 反馈要点 + 优化方向',
            'example': '请帮我起草一份市场分析报告初稿，重点关注竞品对比，我会告诉你需要调整的方向',
            'usage': '适合需要多轮优化的复杂任务',
        })
    
    # 根据 confidence 推荐
    conf_score = kpis.get('confidence', {}).get('score', 0)
    if conf_score < 15:
        templates.append({
            'name': '安全探索模板',
            'pattern': '任务 + 容错空间 + 确认机制',
            'example': '帮我分析这份数据报告初稿，如有不确定的地方请标注，我会进一步说明',
            'usage': '适合需要逐步确认的谨慎场景',
        })
    
    return templates


def generate_full_report(kpi_report: Dict) -> Dict:
    """生成完整诊断报告"""
    
    # 1. KPI 摘要
    summary = {
        'overall_score': kpi_report['overall']['total_score'],
        'overall_status': kpi_report['overall']['status'],
        'kpis': kpi_report['kpis'],
    }
    
    # 2. 差距诊断
    gaps = diagnose_gaps(kpi_report)
    
    # 3. 改进建议
    improvements = generate_improvements(gaps)
    
    # 4. 学习路径
    primary_gap = kpi_report['gaps'].get('primary', 'productivity')
    learning_path = generate_learning_path(primary_gap)
    
    # 5. 提示词模板
    prompt_templates = select_prompt_templates()
    
    # 6. 可复用模式
    reusable_templates = extract_reusable_templates(kpi_report)
    
    return {
        'section_1_kpi_summary': summary,
        'section_2_gaps_diagnosis': gaps,
        'section_3_improvements': improvements,
        'section_4_learning_path': learning_path,
        'section_5_prompt_templates': prompt_templates,
        'section_6_reusable_templates': reusable_templates,
        'generated_at': datetime.now().isoformat(),
    }


def main():
    args = parse_arguments()
    
    # 加载 KPI 报告
    print(f"正在加载 KPI 报告: {args.input}")
    with open(args.input, 'r', encoding='utf-8') as f:
        kpi_report = json.load(f)
    
    if 'error' in kpi_report:
        print(f"警告: {kpi_report['error']}", file=sys.stderr)
        result = {'error': kpi_report['error']}
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return
    
    # 生成报告
    print("正在生成诊断报告...")
    report = generate_full_report(kpi_report)
    
    # 输出结果
    print(f"正在保存报告: {args.output}")
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    # 打印摘要
    print("\n" + "=" * 60)
    print("         AI Adoption Full Diagnostic Report")
    print("=" * 60)
    print(f"\n总体评分: {report['section_1_kpi_summary']['overall_score']}/100")
    print(f"状态: {report['section_1_kpi_summary']['overall_status']}")
    
    print(f"\n主要差距 ({len(report['section_2_gaps_diagnosis'])} 个):")
    for gap in report['section_2_gaps_diagnosis']:
        print(f"  - {gap['gap_name']}: {gap['root_cause_description']}")
    
    print(f"\n优先级改进方案:")
    for imp in report['section_3_improvements'][:3]:
        print(f"  [{imp['priority']}] {imp['method']}")
    
    print(f"\n生成提示词模板: {len(report['section_5_prompt_templates'])} 个")
    print(f"可复用模式: {len(report['section_6_reusable_templates'])} 个")
    
    print("\n报告生成完成!")


if __name__ == "__main__":
    main()
