#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
💎 小红书钻石科普文案生成器
每天自动生成撤柜钻石科普文案 + 配图建议
"""

import random
from datetime import datetime

# 钻石科普知识点库
KNOWLEDGE_BASE = {
    "4C标准": [
        "💎 钻石4C是什么？切工、颜色、净度、克拉！缺一不可～",
        "✨ 切工是钻石的灵魂！切工好=火彩好=闪瞎眼！",
        "🌈 颜色D-Z，D色最白最珍贵！H色性价比最高～",
        "🔍 净度VVS/VS/SI，肉眼无差就够用！别被忽悠多花钱～",
        "⚖️ 克拉不是越大越好！切工差的大钻不如切工好的小钻～"
    ],
    "选购技巧": [
        "🛒 买钻戒先看证书！GIA>IGI>国检，认准GIA！",
        "💡 预算有限？选H色+SI净度+3EX切工，完美平衡！",
        "🎯 异形钻更便宜！椭圆/梨形/心形，省钱又独特～",
        "⚠️ 荧光要慎选！强荧光影响火彩，无荧光最稳～",
        "💍 戒托很重要！六爪显大，四爪显钻，选对显大一倍！"
    ],
    "避坑指南": [
        "🚫 别买奶钻！看着雾蒙蒙，火彩全无～",
        "🚫 警惕咖钻！带褐色调，价值大打折扣～",
        "🚫 证书要对版！GIA证书号去官网查，别造假证骗你～",
        "🚫 柜台钻溢价高！品牌钻=同品质裸钻×2-3倍价格～",
        "🚫 别被「南非钻」忽悠！产地不影响品质，4C才是王道～"
    ],
    "撤柜优势": [
        "💰 撤柜钻=柜姐提成省掉=你省30-50%！",
        "🏷️ 同品质GIA钻，专柜5万，撤柜2.5万！",
        "✅ 撤柜也是GIA证书！品质一模一样，价格香爆～",
        "🤝 找靠谱渠道！看证书、看实物、支持复检～",
        "📈 钻石保值看4C！撤柜钻保值率和专柜一样～"
    ],
    "保养知识": [
        "🧼 钻石亲油！别摸钻石表面，会变暗～",
        "🚿 洗澡摘钻戒！沐浴露会让钻石失去光泽～",
        "📦 单独存放！钻石硬度最高，会划伤其他珠宝～",
        "🔬 定期清洗！温水+洗洁精+软毛刷，自己就能洗～",
        "✅ 每年检查爪！松了赶紧修，别把钻弄丢了～"
    ],
    "冷知识": [
        "🧊 钻石其实是碳！和铅笔芯同元素，结构不同而已～",
        "🔥 钻石能烧没！高温下会变成二氧化碳～",
        "🌍 钻石不稀有！只是戴比尔斯控制产量罢了～",
        "💍 婚戒戴左手无名指=古埃及相信这里有爱情静脉～",
        "⭐ 最大的钻石=非洲之星530克拉，在英王权杖上～"
    ]
}

# 配图建议
IMAGE_SUGGESTIONS = {
    "4C标准": [
        "📸 配图：4C标准示意图，四个维度一目了然",
        "📸 配图：不同切工对比图，火彩差异明显",
        "📸 配图：D-Z颜色渐变图，白到黄的变化"
    ],
    "选购技巧": [
        "📸 配图：GIA证书样本，教你看懂证书",
        "📸 配图：不同形状钻石对比，圆钻vs异形钻",
        "📸 配图：戒托款式对比，六爪vs四爪"
    ],
    "避坑指南": [
        "📸 配图：奶钻vs正常钻对比，雾蒙蒙很明显",
        "📸 配图：咖钻vs白钻对比，褐色调一眼看出",
        "📸 配图：真假证书对比，教你识别假证"
    ],
    "撤柜优势": [
        "📸 配图：专柜vs撤柜价格对比表，差价一目了然",
        "📸 配图：同品质钻石对比，专柜撤柜一模一样",
        "📸 配图：GIA证书+裸钻实拍，品质有保障"
    ],
    "保养知识": [
        "📸 配图：钻石清洗步骤图解，自己在家洗",
        "📸 配图：钻戒存放方式，单独包装很重要",
        "📸 配图：爪镶检查示意图，定期检查防脱落"
    ],
    "冷知识": [
        "📸 配图：钻石结构图，碳原子排列",
        "📸 配图：非洲之星图片，世界最大钻石",
        "📸 配图：婚戒佩戴位置图，左手无名指"
    ]
}

# 爆款标题模板
TITLE_TEMPLATES = [
    "姐妹们！{topic}一定要知道的事！",
    "后悔没早知道！{topic}避坑指南",
    "省钱攻略｜{topic}这样选立省几万！",
    "干货满满！{topic}小白必看！",
    "柜姐不会告诉你的{topic}真相！",
    "别被坑！{topic}避雷指南来了！",
    "撤柜钻真的香！{topic}省下一半钱！",
    "{topic}｜看完这篇就够了！"
]

# 话题标签
HASHTAGS = [
    "#钻石科普", "#钻戒选购", "#GIA钻石", "#撤柜钻",
    "#婚戒", "#求婚钻戒", "#钻石4C", "#避坑指南",
    "#省钱攻略", "#钻石保养", "#珠宝知识", "#钻石冷知识"
]


def generate_post():
    """生成一篇小红书文案"""
    # 随机选择主题
    topic = random.choice(list(KNOWLEDGE_BASE.keys()))
    content = random.choice(KNOWLEDGE_BASE[topic])
    image = random.choice(IMAGE_SUGGESTIONS[topic])
    
    # 生成标题
    title = random.choice(TITLE_TEMPLATES).format(topic=topic)
    
    # 随机选择话题标签
    tags = random.sample(HASHTAGS, 4)
    
    return {
        "title": title,
        "topic": topic,
        "content": content,
        "image": image,
        "tags": tags
    }


def format_post(post):
    """格式化输出文案"""
    output = f"""
{'='*50}
📱 小红书文案
{'='*50}

📌 标题：{post['title']}

📝 正文：

{post['content']}

姐妹们记住了吗？点赞收藏不迷路～ 💕

{' '.join(post['tags'])}

{'='*50}
{post['image']}
{'='*50}
"""
    return output


def generate_daily_posts(count=3):
    """生成每日多篇文案"""
    print(f"\n💎 小红书钻石科普文案 - {datetime.now().strftime('%Y-%m-%d')}\n")
    print("="*50)
    
    posts = []
    used_topics = set()
    
    for i in range(count):
        post = generate_post()
        # 尽量避免重复主题
        attempts = 0
        while post['topic'] in used_topics and attempts < 10:
            post = generate_post()
            attempts += 1
        used_topics.add(post['topic'])
        posts.append(post)
        
        print(f"\n【第 {i+1} 篇】")
        print(format_post(post))
    
    return posts


def save_posts(posts):
    """保存文案到文件"""
    filename = f"/Users/shangguan/.qclaw/workspace/diamond_posts_{datetime.now().strftime('%Y%m%d')}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# 小红书钻石科普文案 - {datetime.now().strftime('%Y-%m-%d')}\n\n")
        
        for i, post in enumerate(posts, 1):
            f.write(f"## 第 {i} 篇\n\n")
            f.write(f"**标题**：{post['title']}\n\n")
            f.write(f"**正文**：\n\n{post['content']}\n\n")
            f.write(f"姐妹们记住了吗？点赞收藏不迷路～ 💕\n\n")
            f.write(f"{' '.join(post['tags'])}\n\n")
            f.write(f"**配图建议**：{post['image']}\n\n")
            f.write("---\n\n")
    
    print(f"✅ 文案已保存到：{filename}")
    return filename


if __name__ == "__main__":
    import sys
    
    count = 3
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except:
            pass
    
    posts = generate_daily_posts(count)
    save_posts(posts)