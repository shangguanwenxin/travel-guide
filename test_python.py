# ========== 1. Hello World ==========
print("Hello, World! 🐷")
print("欢迎来到 Python 世界！")


# ========== 2. 变量和数据类型 ==========
name = "上官"          # 字符串
age = 18               # 整数
price = 999.9          # 浮点数
is_cute = True         # 布尔值

print(f"名字: {name}, 年龄: {age}")
print(f"价格: {price} 元")


# ========== 3. 列表操作 ==========
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")       # 添加
fruits.remove("香蕉")       # 删除
print(f"水果列表: {fruits}")
print(f"第1个水果: {fruits[0]}")


# ========== 4. 字典 ==========
person = {
    "name": "上官",
    "hobby": "看抖音",
    "gold_price_lover": True
}
print(f"个人信息: {person}")
print(f"爱好: {person['hobby']}")


# ========== 5. 条件判断 ==========
gold_price = 980

if gold_price > 1000:
    print("金价好贵啊！😢")
elif gold_price > 900:
    print("金价还行，可以考虑～ 👍")
else:
    print("金价便宜，买它！💰")


# ========== 6. 循环 ==========
# for 循环
for i in range(5):
    print(f"计数: {i}")

# while 循环
count = 0
while count < 3:
    print(f"循环次数: {count}")
    count += 1


# ========== 7. 函数 ==========
def greet(username):
    """打招呼函数"""
    return f"你好呀，{username}！🐷"

def calculate_sum(a, b):
    """求和函数"""
    return a + b

print(greet("上官"))
print(f"1 + 2 = {calculate_sum(1, 2)}")


# ========== 8. 类（面向对象）==========
class Dog:
    """狗狗类"""
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        return f"{self.name} 叫: 汪汪汪！🐶"
    
    def info(self):
        return f"狗狗 {self.name}，颜色 {self.color}"

# 创建对象
my_dog = Dog("旺财", "金色")
print(my_dog.info())
print(my_dog.bark())


# ========== 9. 文件读取/写入 ==========
# 写入文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("这是小猪写的第一行代码！🐷\n")
    f.write("第二行～\n")

# 读取文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容:")
    print(content)


# ========== 10. 异常处理 ==========
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零哦！⚠️")
finally:
    print("程序结束～")


# ========== 11. 常用库示例 ==========
# math 数学库
import math
print(f"PI 向上取整: {math.ceil(math.pi)}")
print(f"PI 向下取整: {math.floor(math.pi)}")

# random 随机库
import random
print(f"随机数: {random.randint(1, 10)}")
print(f"随机选一个: {random.choice(['苹果', '香蕉', '橙子'])}")

# datetime 时间库
import datetime
now = datetime.datetime.now()
print(f"现在时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

print("\n" + "="*30)
print("以上就是 Python 基础代码啦～")
print("有问题随时问小猪！🐷")
