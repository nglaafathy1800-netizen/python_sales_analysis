import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# إنشاء بيانات مبيعات وهمية
np.random.seed(0)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': np.random.randint(5000, 15000, 6),
    'Profit': np.random.randint(1000, 5000, 6)
}
df = pd.DataFrame(data)

print("--- Sales Report ---")
print(df)
print(f"\nTotal Sales: {df['Sales'].sum()}")
print(f"Average Profit: {df['Profit'].mean():.2f}")

# رسم بياني
plt.figure(figsize=(8, 5))
plt.plot(df['Month'], df['Sales'], marker='o', label='Sales')
plt.plot(df['Month'], df['Profit'], marker='s', label='Profit')
plt.title('Sales Analysis - First Half 2026')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.savefig('sales_chart.png')
print("\nChart saved as sales_chart.png")
