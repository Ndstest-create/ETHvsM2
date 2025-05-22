import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Global M2 vs ETH", layout="wide")
st.title("📈 เปรียบเทียบ Global M2 กับ Ethereum (ETH)")

# ข้อมูลราคา ETH และ Global M2
data = {
    "Year": [2020, 2021, 2022, 2023, 2024, 2025],
    "ETH_Price": [307.66, 2775, 1982, 1792, 3046, 2387],
    "Global_M2": [80, 84, 88, 90, 91, 92]
}
df = pd.DataFrame(data)
df.set_index("Year", inplace=True)

# วาดกราฟ
st.subheader("📊 กราฟเปรียบเทียบ Global M2 และราคา ETH")
fig, ax1 = plt.subplots(figsize=(12, 6))

color1 = 'tab:blue'
ax1.set_xlabel("ปี")
ax1.set_ylabel("Global M2 (ล้านล้าน USD)", color=color1)
line1 = ax1.plot(df.index, df["Global_M2"], label="Global M2", color=color1, marker='o')
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("ราคา ETH (USD)", color=color2)
line2 = ax2.plot(df.index, df["ETH_Price"], label="ETH Price", color=color2, marker='o')
ax2.tick_params(axis='y', labelcolor=color2)

# รวม legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

fig.tight_layout()
st.pyplot(fig)

# แสดงตารางข้อมูล
with st.expander("📋 ดูข้อมูลตาราง"):
    st.dataframe(df.style.format({"ETH_Price": "${:.2f}", "Global_M2": "{:.2f}"}))
