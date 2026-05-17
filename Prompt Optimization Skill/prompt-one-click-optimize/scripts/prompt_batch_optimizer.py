#!/usr/bin/env python3
"""
提示词批量优化工具
输入: JSON文件，每行一个提示词对象
输出: 优化后的提示词JSON
"""

import argparse
import json
import sys


def load_prompts(input_file):
    """加载提示词列表"""
    prompts = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                prompts.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"警告: 第{line_num}行JSON解析失败: {e}", file=sys.stderr)
                continue
    return prompts


def optimize_prompt(prompt_data):
    """
    优化单个提示词
    输入格式: {"id": "...", "prompt": "...", "description": "..."}
    输出格式: {"id": "...", "original": "...", "optimized": "...", "changes": [...]}
    """
    prompt_text = prompt_data.get('prompt', '')
    if not prompt_text:
        return {
            "id": prompt_data.get('id', 'unknown'),
            "original": "",
            "optimized": "",
            "changes": ["原始提示词为空"]
        }

    # 分析并生成优化版本
    optimized = generate_optimized_prompt(prompt_text)
    changes = analyze_changes(prompt_text, optimized)

    return {
        "id": prompt_data.get('id', 'unknown'),
        "original": prompt_text,
        "optimized": optimized,
        "changes": changes
    }


def generate_optimized_prompt(original):
    """
    根据最佳实践生成优化后的提示词
    策略: 角色定义 -> 任务描述 -> 约束条件 -> 输出格式
    """
    # 检查是否已有角色定义
    has_role = any(keyword in original.lower() for keyword in [
        '你是', '你是一个', '你是一个', '角色', 'assistant', 'you are', 'act as', 'as a'
    ])

    # 检查是否有输出格式定义
    has_output_format = any(keyword in original for keyword in [
        '输出', '返回', '格式', '请以', '用json', '用markdown'
    ])

    lines = original.strip().split('\n')
    optimized_parts = []

    # 如果缺少角色定义，在开头补充
    if not has_role and len(lines) > 0:
        # 尝试推断角色
        first_line = lines[0]
        if len(first_line) < 100:  # 可能是简短的指令
            optimized_parts.append("# 角色设定")
            optimized_parts.append("你是一个专业的AI助手，擅长理解和执行用户指令。")
            optimized_parts.append("")

    # 添加原始内容
    for line in lines:
        if line.strip():
            optimized_parts.append(line)

    # 如果缺少输出格式，添加通用输出提示
    if not has_output_format:
        optimized_parts.append("")
        optimized_parts.append("# 输出要求")
        optimized_parts.append("回答应简洁、准确，直接给出结果。")

    return '\n'.join(optimized_parts)


def analyze_changes(original, optimized):
    """分析优化做了哪些改动"""
    changes = []

    if len(optimized) > len(original) * 1.2:
        changes.append("新增了结构化要素(角色定义/输出格式)")

    if '\n' in optimized and optimized.count('\n') > original.count('\n'):
        changes.append("增强了内容组织结构")

    if not changes:
        changes.append("原始提示词结构已较完善，保持原样或微调")

    return changes


def main():
    parser = argparse.ArgumentParser(description='提示词批量优化工具')
    parser.add_argument('--input', '-i', required=True, help='输入JSON文件路径')
    parser.add_argument('--output', '-o', help='输出JSON文件路径(默认stdout)')
    parser.add_argument('--optimization-level', '-l', choices=['basic', 'standard', 'advanced'],
                        default='standard', help='优化级别')

    args = parser.parse_args()

    # 加载提示词
    prompts = load_prompts(args.input)
    if not prompts:
        print("错误: 未找到有效提示词", file=sys.stderr)
        sys.exit(1)

    # 优化每个提示词
    results = []
    for prompt_data in prompts:
        optimized = optimize_prompt(prompt_data)
        results.append(optimized)

    # 输出结果
    output_data = {
        "total": len(results),
        "optimized_prompts": results
    }

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        print(f"已优化 {len(results)} 个提示词，输出到: {args.output}")
    else:
        print(json.dumps(output_data, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
