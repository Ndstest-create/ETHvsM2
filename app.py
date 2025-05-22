import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Global M2 vs ETH", layout="wide")
st.title("📈 เปรียบเทียบ Global M2 กับ Ethereum (ETH) รายเดือน (2020 - ปัจจุบัน)")

# จำลองข้อมูลรายเดือน
dates = pd.date_range(start="2020-01-01", end=datetime.today(), freq="M")
n = len(dates)

# Global M2 โตขึ้นทีละนิด
np.random.seed(42)
m2 = 80 + np.cumsum(np.random.normal(0.2, 0.1, size=n))

# จำลองราคา ETH รายเดือน (มีการสวิงขึ้นลง)
eth_base = [307.66, 2775, 1982, 1792, 3046, 2387]  # เฉลี่ยปี 2020–2025
eth_monthly = []
for i in range(len(dates)):
    year_idx = min((dates[i].year - 2020), 5)
    base_price = eth_base[year_idx]
    price = base_price + np.random.normal(0, base_price * 0.1)
    eth_monthly.append(max(price, 50))  # ไม่ให้ต่ำกว่า 50

# สร้าง DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Global_M2": m2,
    "ETH_Price": eth_monthly
})
df.set_index("Date", inplace=True)

# วาดกราฟ
st.subheader("📊 เส้นกราฟ Global M2 และราคา ETH รายเดือน")
fig, ax1 = plt.subplots(figsize=(12, 6))

color1 = 'tab:blue'
ax1.set_xlabel("เดือน")
ax1.set_ylabel("Global M2 (T$)", color=color1)
line1 = ax1.plot(df.index, df["Global_M2"], label="Global M2", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("ETH Price (USD)", color=color2)
line2 = ax2.plot(df.index, df["ETH_Price"], label="ETH Price", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

# รวม legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

fig.tight_layout()
st.pyplot(fig)

# ตารางข้อมูล
with st.expander("📋 ดูข้อมูล"):
    st.dataframe(df.tail(12).style.format({"Global_M2": "{:.2f}", "ETH_Price": "${:.2f}"}))
