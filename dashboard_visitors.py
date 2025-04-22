
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data (simulate reading from Excel)
df_age = pd.read_excel("Dashboard ผู้เยี่ยมชมศึกษาดูงาน.xlsx", sheet_name="TAge")
df_response = pd.read_excel("Dashboard ผู้เยี่ยมชมศึกษาดูงาน.xlsx", sheet_name="TResponse")
df_education = pd.read_excel("Dashboard ผู้เยี่ยมชมศึกษาดูงาน.xlsx", sheet_name="TEducation")
df_satisfaction = pd.read_excel("Dashboard ผู้เยี่ยมชมศึกษาดูงาน.xlsx", sheet_name="TSatisfaction")

st.title("📊 Dashboard ผู้เยี่ยมชมศึกษาดูงาน สำนักงานเลขาธิการวุฒิสภา")

# รวมยอดผู้เยี่ยมชมรายเดือน
st.header("ยอดผู้เยี่ยมชมแยกตามเดือน")
monthly_total = df_age.iloc[:, 1:].sum().reset_index()
monthly_total.columns = ["เดือน", "จำนวน"]
fig1 = px.bar(monthly_total, x="เดือน", y="จำนวน", color="เดือน", text="จำนวน")
st.plotly_chart(fig1)

# แยกตามช่วงอายุ
st.header("ผู้เยี่ยมชมแยกตามช่วงอายุ")
age_melted = df_age.melt(id_vars="อายุ", var_name="เดือน", value_name="จำนวน")
age_selected_month = st.selectbox("เลือกเดือน", df_age.columns[1:])
fig2 = px.bar(df_age, x="อายุ", y=age_selected_month, color="อายุ", text=age_selected_month)
st.plotly_chart(fig2)

# แยกตามระดับการศึกษา
st.header("ผู้เยี่ยมชมแยกตามระดับการศึกษา")
edu_selected_month = st.selectbox("เลือกเดือน (การศึกษา)", df_education.columns[1:])
fig3 = px.pie(df_education, names="ระดับการศึกษา", values=edu_selected_month, hole=0.4)
st.plotly_chart(fig3)

# แยกตามประเภทผู้เยี่ยมชม
st.header("ผู้เยี่ยมชมแยกตามประเภท")
resp_selected_month = st.selectbox("เลือกเดือน (ประเภท)", df_response.columns[1:])
fig4 = px.bar(df_response, x="ประเภทผู้ตอบแบบประเมิน", y=resp_selected_month,
              color="ประเภทผู้ตอบแบบประเมิน", text=resp_selected_month)
st.plotly_chart(fig4)

# ความพึงพอใจ
st.header("ความพึงพอใจต่อการศึกษาดูงาน")
sat_selected_month = st.selectbox("เลือกเดือน (ความพึงพอใจ)", df_satisfaction.columns[1:])
sat_total = df_satisfaction[sat_selected_month].sum()
df_satisfaction["ร้อยละ"] = (df_satisfaction[sat_selected_month] / sat_total) * 100
fig5 = px.bar(df_satisfaction, x="ความพึงพอใจ (ระดับมากที่สุด)", y="ร้อยละ", text="ร้อยละ")
st.plotly_chart(fig5)

st.markdown("---")
st.caption("ข้อมูลโดย สำนักงานเลขาธิการวุฒิสภา")
