#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐷 小猪的本地大脑
使用 DeepSeek R1 14B 进行本地思考
"""

import requests
import json
import time

# Ollama API 配置
OLLAMA_API = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:14b"

def think(prompt, verbose=False):
    """
    小猪用本地大模型思考
    
    Args:
        prompt: 思考的问题
        verbose: 是否显示详细过程
    
    Returns:
        str: 思考结果
    """
    print(f"\n🧠 小猪在思考: {prompt}")
    print("⏳ 请稍候...\n")
    
    try:
        response = requests.post(
            OLLAMA_API,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "temperature": 0.7,
            },
            timeout=300
        )
        
        if response.status_code == 200:
            data = response.json()
            result = data.get('response', '')
            
            if verbose:
                print(f"⏱️  耗时: {data.get('total_duration', 0) / 1e9:.2f}秒")
                print(f"📊 Token数: {data.get('eval_count', 0)}")
            
            return result
        else:
            return f"❌ 错误: {response.status_code}"
    
    except requests.exceptions.ConnectionError:
        return "❌ 无法连接到 Ollama，请确保已启动"
    except Exception as e:
        return f"❌ 错误: {str(e)}"


def analyze_code(code):
    """分析代码"""
    prompt = f"""请分析以下 Python 代码，说明它的功能和改进建议：

```python
{code}
```

请用中文回答。"""
    return think(prompt)


def generate_idea(topic):
    """生成创意"""
    prompt = f"""请为以下主题生成 3 个创意想法：

主题: {topic}

请用中文回答，每个想法用数字编号。"""
    return think(prompt)


def optimize_text(text):
    """优化文本"""
    prompt = f"""请优化以下文本，使其更吸引人、更专业：

原文本:
{text}

请用中文回答，直接给出优化后的版本。"""
    return think(prompt)


def main():
    """主程序"""
    print("\n" + "🐷"*20)
    print("欢迎使用小猪的本地大脑！")
    print("🐷"*20)
    
    print("\n📚 功能菜单:")
    print("1. 自由思考")
    print("2. 分析代码")
    print("3. 生成创意")
    print("4. 优化文本")
    print("5. 退出")
    
    while True:
        choice = input("\n请选择 (1-5): ").strip()
        
        if choice == "1":
            question = input("请输入你的问题: ")
            result = think(question, verbose=True)
            print(f"\n💭 小猪的思考结果:\n{result}")
        
        elif choice == "2":
            print("请输入 Python 代码 (输入 END 结束):")
            lines = []
            while True:
                line = input()
                if line == "END":
                    break
                lines.append(line)
            code = "\n".join(lines)
            result = analyze_code(code)
            print(f"\n📝 代码分析:\n{result}")
        
        elif choice == "3":
            topic = input("请输入主题: ")
            result = generate_idea(topic)
            print(f"\n💡 创意想法:\n{result}")
        
        elif choice == "4":
            text = input("请输入要优化的文本: ")
            result = optimize_text(text)
            print(f"\n✨ 优化后的文本:\n{result}")
        
        elif choice == "5":
            print("\n👋 再见！哼唧哼唧～ 🐷")
            break
        
        else:
            print("❌ 请输入 1-5")


if __name__ == "__main__":
    main()
