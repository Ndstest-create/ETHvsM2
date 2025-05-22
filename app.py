import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Global M2 vs ETH", layout="wide")
st.title("📈 เปรียบเทียบ Global M2 กับ Ethereum (ETH)")

# ข้อมูล 60 เดือน (2020 - 2025)
df = pd.DataFrame({
    "Date": pd.date_range(start="2020-01-01", periods=60, freq="M"),
    "Global_M2": [90 + i * 1.8 for i in range(60)],
    "ETH_Price": [140 + (i**1.3) * 5 for i in range(60)]
})
df.set_index("Date", inplace=True)

st.subheader("📊 เส้นกราฟ Global M2 และราคา ETH")
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.set_xlabel("Date")
ax1.set_ylabel("Global M2 (T$)", color='tab:blue')
ax1.plot(df.index, df["Global_M2"], color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel("ETH Price (USD)", color='tab:orange')
ax2.plot(df.index, df["ETH_Price"], color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

fig.tight_layout()
st.pyplot(fig)

with st.expander("📋 ดูข้อมูล"):
    st.dataframe(df)
