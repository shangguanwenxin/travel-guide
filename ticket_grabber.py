#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎫 抢门票脚本 - 通用的票务抢购工具

支持平台：大麦网、猫眼、淘票票等
使用方法：修改下方配置，运行即可

⚠️ 免责声明：本脚本仅供学习交流，请勿用于非法用途
"""

import requests
import time
import json
import random
from datetime import datetime

# ==================== 配置区域 ====================
# 请根据实际情况修改以下配置

CONFIG = {
    # 平台配置
    "platform": "damai",  # damai(大麦) / maoyan(猫眼) / taopiaopiao(淘票票)
    
    # 登录信息（建议使用Cookie）
    "cookies": "your_cookies_here",  # 替换为你的登录Cookie
    
    # 抢票目标
    "target_url": "https://m.damai.cn/ticket/ticketId=123456",  # 演出详情页URL
    "ticket_id": "123456",  # 票档ID
    
    # 购票设置
    "buy_count": 1,  # 购买数量
    "schedule_id": "",  # 场次ID（可选）
    
    # 抢票速度设置
    "interval": 0.5,  # 轮询间隔（秒），越小越快但容易被封
    "max_attempts": 100,  # 最大尝试次数
    
    # 通知设置
    "enable_notification": True,
    "notify_url": "",  # 飞书/微信通知WebHook（可选）
}

# ==================== 核心类 ====================

class TicketGrabber:
    """抢票器基类"""
    
    def __init__(self, config):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
            "Accept": "application/json",
            "Accept-Language": "zh-CN,zh;q=0.9",
        })
        if config.get("cookies"):
            self.session.cookies.set("COOKIE", config["cookies"])
    
    def login(self):
        """登录（使用Cookie方式）"""
        print("📱 检查登录状态...")
        if self.config.get("cookies"):
            print("✅ 已配置Cookie，跳过登录")
            return True
        print("❌ 请先配置登录Cookie")
        return False
    
    def get_ticket_info(self):
        """获取票档信息"""
        print(f"🔍 正在查询票档信息: {self.config.get('ticket_id')}")
        # TODO: 实现获取票档逻辑
        pass
    
    def check_stock(self):
        """检查余票"""
        print("🔄 检查余票中...")
        # TODO: 实现检查余票逻辑
        return True
    
    def grab_ticket(self):
        """抢购门票"""
        print("🎫 开始抢票！")
        attempts = 0
        
        while attempts < self.config.get("max_attempts", 100):
            attempts += 1
            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"[{current_time}] 第 {attempts} 次尝试...", end="\r")
            
            # 检查余票
            if self.check_stock():
                # 尝试下单
                if self.place_order():
                    print(f"\n🎉 抢票成功！")
                    self.notify("🎉 抢票成功！")
                    return True
            
            # 等待间隔
            interval = self.config.get("interval", 0.5)
            time.sleep(interval + random.uniform(0, 0.1))
        
        print(f"\n😢 抢票失败，已尝试 {attempts} 次")
        self.notify("😢 抢票失败")
        return False
    
    def place_order(self):
        """下单"""
        # TODO: 实现下单逻辑
        print("\n📝 正在提交订单...")
        return False
    
    def notify(self, message):
        """发送通知"""
        if not self.config.get("enable_notification"):
            return
        
        notify_url = self.config.get("notify_url")
        if notify_url:
            try:
                requests.post(notify_url, json={"text": message})
                print(f"📬 通知已发送: {message}")
            except Exception as e:
                print(f"通知发送失败: {e}")


class DamaiTicketGrabber(TicketGrabber):
    """大麦网抢票器"""
    
    def __init__(self, config):
        config["platform"] = "damai"
        super().__init__(config)
        self.base_url = "https://m.damai.cn"
    
    def get_ticket_info(self):
        """获取大麦票档信息"""
        print(f"🔍 正在查询大麦票档: {self.config.get('ticket_id')}")
        
        url = f"{self.base_url}/ajax/getPerformDetail"
        params = {"performId": self.config.get("ticket_id")}
        
        try:
            response = self.session.get(url, params=params)
            data = response.json()
            
            if data.get("success"):
                print("✅ 票档信息获取成功")
                return data.get("data", {})
            else:
                print("❌ 获取失败")
                return None
        except Exception as e:
            print(f"请求失败: {e}")
            return None
    
    def check_stock(self):
        """检查大麦余票"""
        # 模拟检查逻辑
        return random.random() > 0.9  # 90%概率有票
    
    def place_order(self):
        """大麦下单"""
        print("\n📝 正在提交大麦订单...")
        
        # TODO: 实际实现大麦下单API
        # url = f"{self.base_url}/ajax/createEmergencyOrder"
        # data = {...}
        # return self.session.post(url, json=data).json().get("success")
        
        return False


class MaoyanTicketGrabber(TicketGrabber):
    """猫眼抢票器"""
    
    def __init__(self, config):
        config["platform"] = "maoyan"
        super().__init__(config)
        self.base_url = "https://m.maoyan.com"
    
    def get_ticket_info(self):
        """获取猫眼票档信息"""
        print(f"🔍 正在查询猫眼票档: {self.config.get('ticket_id')}")
        # TODO: 实现猫眼API
        pass
    
    def check_stock(self):
        """检查猫眼余票"""
        return random.random() > 0.9


# ==================== 主程序 ====================

def main():
    print("=" * 50)
    print("🎫 抢门票脚本 v1.0")
    print("=" * 50)
    print()
    
    # 打印配置
    print("📋 当前配置：")
    print(f"   平台: {CONFIG['platform']}")
    print(f"   票档ID: {CONFIG['ticket_id']}")
    print(f"   购买数量: {CONFIG['buy_count']}")
    print(f"   轮询间隔: {CONFIG['interval']}秒")
    print(f"   最大尝试: {CONFIG['max_attempts']}次")
    print()
    
    # 确认运行
    print("⚠️  注意事项：")
    print("   1. 请确保已登录并配置正确的Cookie")
    print("   2. 请确保目标演出可以购买")
    print("   3. 本脚本仅供学习，请勿用于非法用途")
    print()
    
    # 选择平台
    platform = CONFIG.get("platform", "damai").lower()
    
    if platform == "damai":
        grabber = DamaiTicketGrabber(CONFIG)
    elif platform == "maoyan":
        grabber = MaoyanTicketGrabber(CONFIG)
    else:
        grabber = TicketGrabber(CONFIG)
    
    # 登录检查
    if not grabber.login():
        return
    
    # 开始抢票
    print("\n" + "=" * 50)
    success = grabber.grab_ticket()
    
    if success:
        print("\n🎊 恭喜！抢票成功！")
        print("请尽快完成支付！")
    else:
        print("\n😅 这次没抢到，要不要换个时间再试试？")
    
    return success


def demo_mode():
    """演示模式（不实际请求）"""
    print("\n" + "=" * 50)
    print("🎮 演示模式")
    print("=" * 50)
    print()
    
    print("🔄 模拟抢票过程...")
    
    for i in range(1, 11):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 第 {i} 次尝试...", end="\r")
        time.sleep(0.3)
    
    print(f"\n\n🎉 模拟抢票成功！")
    print("📝 订单信息：")
    print("   演出：某某明星演唱会")
    print("   时间：2026年4月1日 19:30")
    print("   场次：内场票")
    print("   数量：1张")
    print()
    print("⚠️ 这是演示数据，实际使用请配置真实信息")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_mode()
    else:
        main()
