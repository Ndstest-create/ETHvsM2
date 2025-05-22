import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Global M2 vs ETH & BTC", layout="wide")
st.title("📈 เปรียบเทียบ Global M2 กับ Ethereum (ETH) และ Bitcoin (BTC) รายเดือน")

# เตรียมวันที่
dates = pd.date_range(start="2020-01-01", end=datetime.today(), freq="M")
n = len(dates)
np.random.seed(42)

# Global M2 (หน่วย ล้านล้าน USD)
m2 = 80 + np.cumsum(np.random.normal(0.2, 0.1, size=n))

# ราคาเฉลี่ยต่อปีของ ETH และ BTC
eth_avg = [307.66, 2775, 1982, 1792, 3046, 2387]
btc_avg = [9000, 47000, 28000, 25000, 43000, 39000]

# จำลองรายเดือน
eth_monthly, btc_monthly = [], []
for i in range(len(dates)):
    year_idx = min((dates[i].year - 2020), 5)
    eth_price = eth_avg[year_idx] + np.random.normal(0, eth_avg[year_idx] * 0.1)
    btc_price = btc_avg[year_idx] + np.random.normal(0, btc_avg[year_idx] * 0.15)
    eth_monthly.append(max(eth_price, 50))
    btc_monthly.append(max(btc_price, 1000))

# สร้าง DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Global_M2": m2,
    "ETH_Price": eth_monthly,
    "BTC_Price": btc_monthly
})
df.set_index("Date", inplace=True)

# วาดกราฟ
st.subheader("📊 กราฟ Global M2, ETH และ BTC")
fig, ax1 = plt.subplots(figsize=(13, 6))

# แกนซ้าย: M2
color1 = 'tab:blue'
ax1.set_xlabel("เดือน")
ax1.set_ylabel("Global M2 (T$)", color=color1)
line1 = ax1.plot(df.index, df["Global_M2"], label="Global M2", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

# แกนขวา: ETH และ BTC
ax2 = ax1.twinx()
line2 = ax2.plot(df.index, df["ETH_Price"], label="ETH Price", color='tab:orange')
line3 = ax2.plot(df.index, df["BTC_Price"], label="BTC Price", color='tab:green')
ax2.set_ylabel("ETH / BTC Price (USD)", color='gray')
ax2.tick_params(axis='y', labelcolor='gray')

# รวม legend
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

fig.tight_layout()
st.pyplot(fig)

# ตารางข้อมูลท้ายสุด
with st.expander("📋 ดูข้อมูลล่าสุด"):
    st.dataframe(df.tail(12).style.format({
        "Global_M2": "{:.2f}",
        "ETH_Price": "${:.2f}",
        "BTC_Price": "${:.2f}"
    }))
