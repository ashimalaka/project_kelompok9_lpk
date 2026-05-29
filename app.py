import streamlit as st

# Card dengan border
with st.container(border=True):
    st.subheader("Judul Section")
    st.write("Konten di sini")

# Layout kolom
col1, col2 = st.columns(2)
with col1:
    st.metric("Revenue", "$1.2M", "+12%", border=True)
with col2:
    st.metric("Users", "762k", "+5%", border=True)

# Sidebar untuk filter
with st.sidebar:
    pilihan = st.selectbox("Pilih kategori", ["A", "B", "C"])
