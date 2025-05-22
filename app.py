
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Global M2 vs ETH", layout="wide")
st.title("📈 เปรียบเทียบ Global M2 กับ Ethereum (ETH)")

# ตัวอย่างข้อมูลจำลอง (เปลี่ยนเป็นของจริงได้ภายหลัง)
df = pd.DataFrame({
    "Date": pd.date_range(start="2022-01-01", periods=24, freq="M"),
    "Global_M2": [100 + i * 1.5 for i in range(24)],
    "ETH_Price": [2000 + i * 80 for i in range(24)]
})

# ตั้งค่า index
df.set_index("Date", inplace=True)

# วาดกราฟ
st.subheader("📊 เส้นกราฟ Global M2 และราคา ETH")
fig, ax1 = plt.subplots(figsize=(10, 5))

color1 = 'tab:blue'
color2 = 'tab:orange'

ax1.set_xlabel("Date")
ax1.set_ylabel("Global M2 (in T$)", color=color1)
ax1.plot(df.index, df["Global_M2"], label="Global M2", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
ax2.set_ylabel("ETH Price (USD)", color=color2)
ax2.plot(df.index, df["ETH_Price"], label="ETH Price", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

fig.tight_layout()
st.pyplot(fig)

# แสดงตาราง
with st.expander("📋 ดูข้อมูลตาราง"):
    st.dataframe(df)
