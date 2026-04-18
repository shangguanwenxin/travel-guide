#!/usr/bin/env python3
"""武汉天气预报脚本 - 每天21:00播报未来两天天气"""

import urllib.request
import json

def get_weather():
    try:
        url = "http://wttr.in/Wuhan?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        # 获取今天和明天的数据
        weather_data = data['weather']
        
        results = []
        for i, day in enumerate(weather_data[:2]):
            date = day['date']
            max_temp = day['maxtempC']
            min_temp = day['mintempC']
            hourly = day['hourly']
            
            # 获取各时段天气
            morning = hourly[4] if len(hourly) > 4 else hourly[0]  # 9-10点
            noon = hourly[7] if len(hourly) > 7 else hourly[0]    # 12-13点
            evening = hourly[10] if len(hourly) > 10 else hourly[0] # 15-16点
            
            day_name = "明天" if i == 1 else "今天"
            
            msg = f"""
【{day_name}天气 · {date}】
☀️ 上午: {morning['weatherDesc'][0]['value']} {morning['tempC']}°C (体感{morning['FeelsLikeC']}°C)
🌤️ 中午: {noon['weatherDesc'][0]['value']} {noon['tempC']}°C (体感{noon['FeelsLikeC']}°C)
🌆 傍晚: {evening['weatherDesc'][0]['value']} {evening['tempC']}°C (体感{evening['FeelsLikeC']}°C)
🌡️ 气温: {min_temp}°C ~ {max_temp}°C
💨 风速: {evening['windspeedKmph']} km/h
"""
            results.append(msg.strip())
        
        return "\n\n".join(results)
        
    except Exception as e:
        return f"获取天气失败: {e}"

if __name__ == "__main__":
    print(get_weather())
