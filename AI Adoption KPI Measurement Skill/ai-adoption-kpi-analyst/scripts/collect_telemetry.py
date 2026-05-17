#!/usr/bin/env python3
"""
AI Adoption Telemetry Collector
接收企业 AI 工具的嵌入式日志，进行数据清洗和基础指标计算
输入：遥测日志 JSONL 文件
输出：结构化的基础指标 JSON
"""

import json
import argparse
from datetime import datetime, timedelta
from collections import defaultdict
import sys


def parse_arguments():
    parser = argparse.ArgumentParser(description='收集并处理 AI 使用遥测数据')
    parser.add_argument('--input', '-i', required=True, help='遥测日志文件路径 (JSONL 格式)')
    parser.add_argument('--output', '-o', required=True, help='处理后的指标文件路径 (JSON 格式)')
    parser.add_argument('--period', '-p', default='7d', help='分析周期: 1d, 7d, 30d')
    return parser.parse_args()


def load_telemetry_data(input_path):
    """加载遥测日志数据"""
    events = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
                events.append(event)
            except json.JSONDecodeError as e:
                print(f"警告: 第 {line_num} 行 JSON 解析失败: {e}", file=sys.stderr)
                continue
    return events


def calculate_period_days(period_str):
    """解析周期字符串"""
    if period_str.endswith('d'):
        return int(period_str[:-1])
    elif period_str.endswith('w'):
        return int(period_str[:-1]) * 7
    elif period_str.endswith('m'):
        return int(period_str[:-1]) * 30
    return 7  # 默认 7 天


def calculate_basic_metrics(events, period_days):
    """计算基础指标"""
    now = datetime.now()
    start_date = now - timedelta(days=period_days)
    
    # 初始化指标
    metrics = {
        'period_days': period_days,
        'total_users': set(),
        'total_sessions': set(),
        'total_tasks': 0,
        'dau': set(),  # 日活跃用户
        'wau': set(),  # 周活跃用户
        'mau': set(),  # 月活跃用户（基于 period_days）
        
        # 提示词质量指标
        'prompt_quality_scores': [],
        'structured_prompt_count': 0,
        
        # 输出质量指标
        'revision_ratios': [],  # 修改率
        'avg_revision_ratio': 0,
        
        # 任务完成指标
        'task_completion_times': [],
        'completed_tasks': 0,
        'failed_tasks': 0,
        
        # 求助行为指标
        'help_requests': 0,
        'complex_tasks_attempted': 0,
        
        # 合规行为指标
        'compliant_tasks': 0,
        
        # 用户满意度（如果有）
        'satisfaction_scores': [],
        
        # 任务类型分布
        'task_types': defaultdict(int),
        
        # 角色分布
        'user_roles': defaultdict(int),
    }
    
    for event in events:
        # 过滤时间范围内的事件
        if 'timestamp' in event:
            try:
                event_time = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
                if event_time.replace(tzinfo=None) < start_date:
                    continue
            except (ValueError, AttributeError):
                pass
        
        # 提取用户 ID
        user_id = event.get('user_id') or event.get('userId') or event.get('id')
        if not user_id:
            continue
        
        metrics['total_users'].add(user_id)
        metrics['wau'].add(user_id)  # 假设所有数据都在周期内
        
        # 每日活跃用户
        if 'date' in event:
            metrics['dau'].add(f"{user_id}:{event['date']}")
        
        # 会话统计
        session_id = event.get('session_id') or event.get('conversation_id')
        if session_id:
            metrics['total_sessions'].add(session_id)
        
        # 任务统计
        if event.get('event_type') in ['task_submit', 'task_complete', 'task_start']:
            metrics['total_tasks'] += 1
            
            # 任务类型分布
            task_type = event.get('task_type', 'unknown')
            metrics['task_types'][task_type] += 1
            
            # 用户角色
            role = event.get('user_role') or event.get('role', 'general')
            metrics['user_roles'][role] += 1
        
        # 提示词质量评分
        if 'prompt_quality_score' in event:
            metrics['prompt_quality_scores'].append(event['prompt_quality_score'])
        elif 'is_structured' in event and event['is_structured']:
            metrics['structured_prompt_count'] += 1
        
        # 输出修改率
        if 'revision_ratio' in event:
            metrics['revision_ratios'].append(event['revision_ratio'])
        
        # 任务完成时间
        if 'completion_time_seconds' in event:
            metrics['task_completion_times'].append(event['completion_time_seconds'])
        
        # 任务完成状态
        if event.get('status') == 'completed':
            metrics['completed_tasks'] += 1
        elif event.get('status') == 'failed':
            metrics['failed_tasks'] += 1
        
        # 求助行为
        if event.get('help_requested') or event.get('event_type') == 'help_request':
            metrics['help_requests'] += 1
        
        # 复杂任务尝试
        if event.get('is_complex') or event.get('complexity') in ['high', 'medium']:
            metrics['complex_tasks_attempted'] += 1
        
        # 合规行为
        if event.get('compliant', True):
            metrics['compliant_tasks'] += 1
        
        # 满意度评分
        if 'satisfaction_score' in event:
            metrics['satisfaction_scores'].append(event['satisfaction_score'])
    
    return metrics


def aggregate_metrics(metrics):
    """聚合指标，计算最终数值"""
    
    total_users = len(metrics['total_users'])
    total_sessions = len(metrics['total_sessions'])
    total_tasks = metrics['total_tasks']
    
    # 活跃用户数（周活跃）
    wau = len(metrics['wau'])
    
    # 使用率
    usage_rate = (wau / total_users * 100) if total_users > 0 else 0
    
    # 平均提示词质量
    avg_prompt_quality = 0
    if metrics['prompt_quality_scores']:
        avg_prompt_quality = sum(metrics['prompt_quality_scores']) / len(metrics['prompt_quality_scores'])
    elif total_tasks > 0:
        # 基于结构化比例估算
        avg_prompt_quality = (metrics['structured_prompt_count'] / total_tasks) * 100
    
    # 平均修改率（越低越好）
    avg_revision_ratio = 0
    if metrics['revision_ratios']:
        avg_revision_ratio = sum(metrics['revision_ratios']) / len(metrics['revision_ratios'])
    
    # 平均完成时间
    avg_completion_time = 0
    if metrics['task_completion_times']:
        avg_completion_time = sum(metrics['task_completion_times']) / len(metrics['task_completion_times'])
    
    # 任务完成率
    task_completion_rate = 0
    if total_tasks > 0:
        task_completion_rate = (metrics['completed_tasks'] / total_tasks) * 100
    
    # 求助率（越低信心度越高）
    help_request_rate = 0
    if total_tasks > 0:
        help_request_rate = (metrics['help_requests'] / total_tasks) * 100
    
    # 复杂任务尝试率
    complex_task_rate = 0
    if total_tasks > 0:
        complex_task_rate = (metrics['complex_tasks_attempted'] / total_tasks) * 100
    
    # 合规率
    compliance_rate = 0
    if total_tasks > 0:
        compliance_rate = (metrics['compliant_tasks'] / total_tasks) * 100
    
    # 平均满意度
    avg_satisfaction = 0
    if metrics['satisfaction_scores']:
        avg_satisfaction = sum(metrics['satisfaction_scores']) / len(metrics['satisfaction_scores'])
    
    return {
        'period_days': metrics['period_days'],
        'user_metrics': {
            'total_users': total_users,
            'wau': wau,
            'usage_rate': round(usage_rate, 2),
        },
        'session_metrics': {
            'total_sessions': total_sessions,
            'avg_tasks_per_session': round(total_tasks / total_sessions, 2) if total_sessions > 0 else 0,
        },
        'task_metrics': {
            'total_tasks': total_tasks,
            'completed_tasks': metrics['completed_tasks'],
            'failed_tasks': metrics['failed_tasks'],
            'completion_rate': round(task_completion_rate, 2),
        },
        'prompt_metrics': {
            'avg_quality_score': round(avg_prompt_quality, 2),
            'structured_count': metrics['structured_prompt_count'],
            'avg_revision_ratio': round(avg_revision_ratio, 2),
        },
        'time_metrics': {
            'avg_completion_time_seconds': round(avg_completion_time, 2),
        },
        'confidence_metrics': {
            'help_request_rate': round(help_request_rate, 2),
            'complex_task_rate': round(complex_task_rate, 2),
            'self_service_rate': round(100 - help_request_rate, 2),
        },
        'compliance_metrics': {
            'compliance_rate': round(compliance_rate, 2),
        },
        'satisfaction_metrics': {
            'avg_satisfaction_score': round(avg_satisfaction, 2) if avg_satisfaction > 0 else None,
        },
        'distribution': {
            'task_types': dict(metrics['task_types']),
            'user_roles': dict(metrics['user_roles']),
        },
        'collected_at': datetime.now().isoformat(),
    }


def main():
    args = parse_arguments()
    
    # 解析周期
    period_days = calculate_period_days(args.period)
    
    # 加载数据
    print(f"正在加载遥测数据: {args.input}")
    events = load_telemetry_data(args.input)
    print(f"成功加载 {len(events)} 条事件记录")
    
    if not events:
        print("警告: 没有有效的事件数据", file=sys.stderr)
        # 输出空报告
        result = {
            'period_days': period_days,
            'error': 'No valid events found',
            'collected_at': datetime.now().isoformat(),
        }
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return
    
    # 计算基础指标
    print("正在计算基础指标...")
    basic_metrics = calculate_basic_metrics(events, period_days)
    
    # 聚合指标
    result = aggregate_metrics(basic_metrics)
    
    # 输出结果
    print(f"正在保存结果: {args.output}")
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    # 打印摘要
    print("\n=== 遥测数据摘要 ===")
    print(f"分析周期: {period_days} 天")
    print(f"总用户数: {result['user_metrics']['total_users']}")
    print(f"周活跃用户: {result['user_metrics']['wau']}")
    print(f"使用率: {result['user_metrics']['usage_rate']}%")
    print(f"总任务数: {result['task_metrics']['total_tasks']}")
    print(f"任务完成率: {result['task_metrics']['completion_rate']}%")
    print(f"平均提示词质量: {result['prompt_metrics']['avg_quality_score']}")
    print(f"平均修改率: {result['prompt_metrics']['avg_revision_ratio']}%")
    print(f"自助服务率: {result['confidence_metrics']['self_service_rate']}%")
    
    print("\n遥测数据收集完成!")


if __name__ == "__main__":
    main()
