#!/usr/bin/env python3
"""
AI Adoption KPI Calculator
基于处理后的指标数据，计算 4 大 KPI：Usage、Productivity、Confidence、Proficiency
输入：基础指标 JSON 文件
输出：KPI 评分报告 JSON 文件
"""

import json
import argparse
import sys
from datetime import datetime


def parse_arguments():
    parser = argparse.ArgumentParser(description='计算 AI 采用 4 大 KPI')
    parser.add_argument('--input', '-i', required=True, help='基础指标文件路径 (JSON 格式)')
    parser.add_argument('--output', '-o', required=True, help='KPI 报告文件路径 (JSON 格式)')
    parser.add_argument('--baseline-efficiency', '-e', type=float, default=1.0, 
                        help='基线效率值 (不使用 AI 的效率，默认为 1.0)')
    return parser.parse_args()


# KPI 阈值配置
KPI_THRESHOLDS = {
    'usage': {
        'excellent': 80,   # >= 80%
        'good': 60,        # >= 60%
        'warning': 40,     # >= 40%
        'critical': 0,
    },
    'productivity': {
        'excellent': 30,   # 效率提升 >= 30%
        'good': 15,        # >= 15%
        'warning': 5,      # >= 5%
        'critical': 0,
    },
    'confidence': {
        'excellent': 75,   # 自助率 >= 75%
        'good': 50,        # >= 50%
        'warning': 25,     # >= 25%
        'critical': 0,
    },
    'proficiency': {
        'excellent': 80,   # 提示词质量 >= 80
        'good': 60,        # >= 60
        'warning': 40,     # >= 40
        'critical': 0,
    },
}


def get_status_label(value, thresholds, reverse=False):
    """根据阈值获取状态标签"""
    if reverse:
        # 反向指标（如修改率越低越好）
        if value <= thresholds['critical']:
            return 'Excellent'
        elif value <= thresholds['warning']:
            return 'Good'
        elif value <= thresholds['good']:
            return 'Warning'
        else:
            return 'Critical'
    else:
        if value >= thresholds['excellent']:
            return 'Excellent'
        elif value >= thresholds['good']:
            return 'Good'
        elif value >= thresholds['warning']:
            return 'Warning'
        else:
            return 'Critical'


def calculate_usage_kpi(metrics):
    """计算 Usage KPI"""
    usage_rate = metrics.get('user_metrics', {}).get('usage_rate', 0)
    
    # Usage 权重分布
    wau = metrics.get('user_metrics', {}).get('wau', 0)
    total_users = metrics.get('user_metrics', {}).get('total_users', 0)
    
    # 实际得分 (满分 25)
    score = min(25, (usage_rate / 100) * 25)
    percentage = usage_rate
    
    return {
        'score': round(score, 2),
        'max_score': 25,
        'percentage': percentage,
        'status': get_status_label(percentage, KPI_THRESHOLDS['usage']),
        'details': {
            'wau': wau,
            'total_users': total_users,
        }
    }


def calculate_productivity_kpi(metrics, baseline_efficiency=1.0):
    """计算 Productivity KPI"""
    # 效率提升计算
    avg_completion_time = metrics.get('time_metrics', {}).get('avg_completion_time_seconds', 0)
    completion_rate = metrics.get('task_metrics', {}).get('completion_rate', 0)
    revision_ratio = metrics.get('prompt_metrics', {}).get('avg_revision_ratio', 0)
    
    # 估算效率提升（假设基线时间为 300 秒）
    baseline_time = 300
    if avg_completion_time > 0:
        time_efficiency = (baseline_time - avg_completion_time) / baseline_time * 100
    else:
        time_efficiency = 0
    
    # 完成率贡献
    completion_score = completion_rate * 0.5  # 权重 50%
    
    # 修改率贡献（越低越好）
    revision_penalty = revision_ratio * 0.3  # 权重 30%
    
    # 综合效率提升
    efficiency_gain = time_efficiency * 0.7 + completion_score - revision_penalty
    
    # 得分 (满分 25)
    score = min(25, max(0, efficiency_gain / 100 * 25))
    percentage = max(0, efficiency_gain)
    
    return {
        'score': round(score, 2),
        'max_score': 25,
        'percentage': round(percentage, 2),
        'status': get_status_label(percentage, KPI_THRESHOLDS['productivity']),
        'details': {
            'avg_completion_time_seconds': avg_completion_time,
            'completion_rate': completion_rate,
            'revision_ratio': revision_ratio,
            'time_efficiency_gain': round(time_efficiency, 2),
        }
    }


def calculate_confidence_kpi(metrics):
    """计算 Confidence KPI"""
    self_service_rate = metrics.get('confidence_metrics', {}).get('self_service_rate', 0)
    complex_task_rate = metrics.get('confidence_metrics', {}).get('complex_task_rate', 0)
    
    # 自助服务率贡献 (70%)
    self_service_score = self_service_rate * 0.7
    
    # 复杂任务尝试率贡献 (30%，越愿意尝试说明信心越足)
    complex_score = min(30, complex_task_rate * 0.5)
    
    # 综合得分
    combined_score = self_service_score + complex_score
    
    # 得分 (满分 25)
    score = min(25, combined_score)
    percentage = combined_score
    
    return {
        'score': round(score, 2),
        'max_score': 25,
        'percentage': round(percentage, 2),
        'status': get_status_label(percentage, KPI_THRESHOLDS['confidence']),
        'details': {
            'self_service_rate': self_service_rate,
            'complex_task_rate': complex_task_rate,
        }
    }


def calculate_proficiency_kpi(metrics):
    """计算 Proficiency KPI"""
    prompt_quality = metrics.get('prompt_metrics', {}).get('avg_quality_score', 0)
    compliance_rate = metrics.get('compliance_metrics', {}).get('compliance_rate', 0)
    
    # 提示词质量贡献 (70%)
    quality_score = prompt_quality * 0.7
    
    # 合规率贡献 (30%)
    compliance_score = compliance_rate * 0.3
    
    # 综合得分
    combined_score = quality_score + compliance_score
    
    # 得分 (满分 25)
    score = min(25, combined_score)
    percentage = combined_score
    
    return {
        'score': round(score, 2),
        'max_score': 25,
        'percentage': round(percentage, 2),
        'status': get_status_label(percentage, KPI_THRESHOLDS['proficiency']),
        'details': {
            'prompt_quality_score': prompt_quality,
            'compliance_rate': compliance_rate,
        }
    }


def calculate_overall_score(kpis):
    """计算总体得分"""
    total = sum([
        kpis['usage']['score'],
        kpis['productivity']['score'],
        kpis['confidence']['score'],
        kpis['proficiency']['score'],
    ])
    percentage = (total / 100) * 100
    return round(total, 2), percentage


def get_overall_status(total_score):
    """获取总体状态"""
    if total_score >= 80:
        return 'Advanced'
    elif total_score >= 60:
        return 'Proficient'
    elif total_score >= 40:
        return 'Developing'
    elif total_score >= 20:
        return 'Novice'
    else:
        return 'At Risk'


def identify_gaps(kpis):
    """识别主要差距"""
    gaps = []
    
    for name, kpi in kpis.items():
        if kpi['status'] in ['Warning', 'Critical']:
            gaps.append({
                'kpi': name,
                'status': kpi['status'],
                'percentage': kpi['percentage'],
                'gap_to_excellent': round(KPI_THRESHOLDS[name]['excellent'] - kpi['percentage'], 2) 
                                   if KPI_THRESHOLDS[name]['excellent'] > kpi['percentage'] else 0,
            })
    
    # 按严重程度排序
    gaps.sort(key=lambda x: (x['status'] == 'Critical', -x['percentage']))
    
    return gaps


def main():
    args = parse_arguments()
    
    # 加载基础指标
    print(f"正在加载指标数据: {args.input}")
    with open(args.input, 'r', encoding='utf-8') as f:
        metrics = json.load(f)
    
    if 'error' in metrics:
        print(f"警告: {metrics['error']}", file=sys.stderr)
        # 输出空报告
        result = {
            'error': metrics['error'],
            'collected_at': metrics.get('collected_at', datetime.now().isoformat()),
        }
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return
    
    # 计算各 KPI
    print("正在计算 4 大 KPI...")
    
    kpis = {
        'usage': calculate_usage_kpi(metrics),
        'productivity': calculate_productivity_kpi(metrics, args.baseline_efficiency),
        'confidence': calculate_confidence_kpi(metrics),
        'proficiency': calculate_proficiency_kpi(metrics),
    }
    
    # 计算总分
    total_score, total_percentage = calculate_overall_score(kpis)
    overall_status = get_overall_status(total_score)
    
    # 识别主要差距
    gaps = identify_gaps(kpis)
    primary_gap = gaps[0]['kpi'] if gaps else None
    secondary_gap = gaps[1]['kpi'] if len(gaps) > 1 else None
    
    # 构建报告
    result = {
        'overall': {
            'total_score': total_score,
            'max_score': 100,
            'percentage': round(total_percentage, 2),
            'status': overall_status,
        },
        'kpis': kpis,
        'gaps': {
            'primary': primary_gap,
            'secondary': secondary_gap,
            'all_gaps': gaps,
        },
        'summary': {
            'period_days': metrics.get('period_days', 0),
            'total_users': metrics.get('user_metrics', {}).get('total_users', 0),
            'wau': metrics.get('user_metrics', {}).get('wau', 0),
            'total_tasks': metrics.get('task_metrics', {}).get('total_tasks', 0),
        },
        'thresholds': KPI_THRESHOLDS,
        'generated_at': datetime.now().isoformat(),
    }
    
    # 输出结果
    print(f"正在保存 KPI 报告: {args.output}")
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    # 打印摘要
    print("\n" + "=" * 50)
    print("           AI Adoption KPI Report")
    print("=" * 50)
    print(f"\n总体评分: {total_score}/100 ({overall_status})")
    print(f"\n4 大 KPI 评分:")
    print("-" * 40)
    for name, kpi in kpis.items():
        bar = "█" * int(kpi['percentage'] / 5) + "░" * (20 - int(kpi['percentage'] / 5))
        print(f"  {name.capitalize():15} [{bar}] {kpi['score']:5.1f}/25 ({kpi['status']})")
    print("-" * 40)
    
    if gaps:
        print(f"\n主要差距:")
        for gap in gaps:
            print(f"  - {gap['kpi'].capitalize()}: {gap['status']} ({gap['percentage']}%)")
    
    print("\nKPI 计算完成!")


if __name__ == "__main__":
    main()
