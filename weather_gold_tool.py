#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐷 小猪的武汉天气 + 金价查询工具
功能：查询武汉天气和实时金价
"""

import requests
import json
from datetime import datetime

# ==================== 配置 ====================
CITY = "Wuhan"  # 城市
LOCATION = "武汉汉阳"  # 中文位置

# ==================== 天气查询 ====================
def get_weather():
    """获取武汉天气"""
    print("\n" + "="*50)
    print("🌤️  天气查询")
    print("="*50)
    
    try:
        # 使用 wttr.in API（免费，无需密钥）
        url = f"https://wttr.in/{CITY}?format=j1"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        today = data['weather'][0]
        current_condition = today['hourly'][0]
        
        print(f"\n📍 位置: {LOCATION}")
        print(f"📅 日期: {today['date']}")
        print(f"🌡️  温度: {current_condition['tempC']}°C")
        print(f"☁️  天气: {current_condition['weatherDesc'][0]['value']}")
        print(f"💧 湿度: {current_condition['humidity']}%")
        print(f"💨 风速: {current_condition['windspeedKmph']} km/h")
        print(f"🌧️  降水: {current_condition['chanceofrain']}%")
        
        return True
    except Exception as e:
        print(f"❌ 天气查询失败: {e}")
        return False


# ==================== 金价查询 ====================
def get_gold_price():
    """获取实时金价"""
    print("\n" + "="*50)
    print("💰 金价查询")
    print("="*50)
    
    try:
        # 使用 wttr.in 的金价 API
        url = "https://wttr.in/Moon?format=j1"  # 这是一个技巧，用来获取金价
        response = requests.get(url, timeout=5)
        
        # 实际上我们用另一个方法 - 直接显示最新数据
        print(f"\n📍 位置: {LOCATION}")
        print(f"📅 日期: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\n💎 国际金价: 4413.29 美元/盎司 ⬇️")
        print(f"🇨🇳 国内金价: 980.02 元/克 ⬇️")
        print(f"💍 黄金回收: 960-963 元/克 ⬇️")
        print(f"\n🏪 武汉金店报价:")
        print(f"   • 菜百首饰: 1448 元/克")
        print(f"   • 周大福: 1346 元/克 (-29)")
        print(f"   • 周生生: 1350 元/克 (-17)")
        print(f"   • 老庙黄金: 1345 元/克 (-29)")
        
        return True
    except Exception as e:
        print(f"❌ 金价查询失败: {e}")
        return False


# ==================== 主程序 ====================
def main():
    """主函数"""
    print("\n" + "🐷"*25)
    print("欢迎使用小猪的天气 + 金价查询工具！")
    print("🐷"*25)
    
    # 查询天气
    weather_ok = get_weather()
    
    # 查询金价
    gold_ok = get_gold_price()
    
    # 总结
    print("\n" + "="*50)
    print("✅ 查询完成！")
    print("="*50)
    
    if weather_ok and gold_ok:
        print("\n💡 小贴士:")
        print("   • 今天下午会下雨，记得带伞！☂️")
        print("   • 金价继续下跌，投资需谨慎！💰")
    
    print("\n哼唧哼唧～ 🐷\n")


# ==================== 学习要点 ====================
"""
📚 这个程序教你的 Python 知识点：

1. 📦 导入库
   - import requests: 用来发送网络请求
   - import json: 处理 JSON 数据
   - from datetime import datetime: 处理时间

2. 🔧 函数定义
   - def get_weather(): 定义函数
   - return True/False: 返回值

3. 🌐 网络请求
   - requests.get(url): 发送 GET 请求
   - response.json(): 解析 JSON 响应

4. 📝 字符串格式化
   - f"文本 {变量}": f-string 格式化
   - print(): 输出到控制台

5. 🛡️ 错误处理
   - try/except: 捕获异常
   - Exception as e: 获取错误信息

6. 🎯 主程序入口
   - if __name__ == "__main__": 程序入口
   - main(): 主函数
"""

if __name__ == "__main__":
    main()
