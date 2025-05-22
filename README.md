
# BTC & ETH Forecast App (Streamlit)

📈 เว็บแอป Streamlit สำหรับ:
- แสดงราคาย้อนหลังของ Bitcoin (BTC) และ Ethereum (ETH) ตั้งแต่ปี 2021 - ปัจจุบัน
- เปรียบเทียบกราฟราคา
- พยากรณ์ราคาวันถัดไปด้วย Linear Regression

## 🔧 วิธีติดตั้งและใช้งาน

### 1. ติดตั้งไลบรารีที่จำเป็น:
```bash
pip install streamlit yfinance pandas matplotlib scikit-learn
```

### 2. รันแอป:
```bash
streamlit run btc_eth_forecast_app.py
```

## 📂 ไฟล์ในโปรเจกต์
- `btc_eth_forecast_app.py` - ตัวหลักของ Streamlit App
- `README.md` - คู่มือการใช้งาน

## ⚠️ หมายเหตุ
- โมเดล Linear Regression ใช้เพื่อการสาธิต ไม่เหมาะสำหรับการลงทุนจริง
- หากต้องการพยากรณ์ที่แม่นยำขึ้น แนะนำลองใช้ LSTM, Prophet หรือ ARIMA

---

พัฒนาเพื่อแสดงแนวทางการใช้ Streamlit กับข้อมูลคริปโต 💡
