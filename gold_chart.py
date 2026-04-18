import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# 2026年3月黄金价格数据 (元/克)
dates = ['Mar 2', 'Mar 3', 'Mar 4', 'Mar 6', 'Mar 13', 'Mar 16', 'Mar 17', 'Mar 18']
prices = [1156.00, 1186.00, 1152.00, 1143.50, 1133.70, 1095.00, 1106.95, 1103.52]

plt.figure(figsize=(10, 6))
plt.plot(dates, prices, marker='o', linewidth=2.5, markersize=10, color='#FFD700', markerfacecolor='#FFA500')
plt.fill_between(dates, prices, alpha=0.3, color='#FFD700')
plt.title('Gold Price Trend - March 2026', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (CNY/g)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

# 添加数据标签
for i, price in enumerate(prices):
    plt.annotate(f'{price}', (dates[i], prices[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('/Users/shangguan/Desktop/gold_price_march_2026.png', dpi=150, facecolor='white')
print("Chart saved to Desktop")
