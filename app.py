import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Global M2 vs ETH", layout="wide")
st.title("📈 เปรียบเทียบ Global M2 กับ Ethereum (ETH)")

# ตัวอย่างข้อมูลจำลองแบบสมจริง (2020-2025)
np.random.seed(42)
dates = pd.date_range(start="2020-01-01", periods=60, freq="M")

# จำลอง Global M2 เติบโตเรื่อยๆ
global_m2 = 90 + np.cumsum(np.random.normal(0.8, 0.3, size=60))  # เริ่มที่ 90 ล้านล้าน USD

# จำลองราคา ETH มีความผันผวน
eth_price = 200 + np.cumsum(np.random.normal(10, 100, size=60))  # มีการสวิงขึ้น-ลง

df = pd.DataFrame({
    "Date": dates,
    "Global_M2 (T$)": global_m2,
    "ETH_Price (USD)": eth_price
})
df.set_index("Date", inplace=True)

# วาดกราฟ
st.subheader("📊 เส้นกราฟ Global M2 กับราคา Ethereum (ETH)")
fig, ax1 = plt.subplots(figsize=(12, 6))

# แกนซ้าย: Global M2
color1 = 'tab:blue'
ax1.set_xlabel("Date")
ax1.set_ylabel("Global M2 (Trillion USD)", color=color1)
line1 = ax1.plot(df.index, df["Global_M2 (T$)"], label="Global M2", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

# แกนขวา: ETH
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("ETH Price (USD)", color=color2)
line2 = ax2.plot(df.index, df["ETH_Price (USD)"], label="ETH Price", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

# รวม legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

fig.tight_layout()
st.pyplot(fig)

# ตารางข้อมูล
with st.expander("📋 ดูข้อมูล"):
    st.dataframe(df.style.format({"Global_M2 (T$)": "{:.2f}", "ETH_Price (USD)": "${:.2f}"}))
