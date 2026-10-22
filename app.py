
import streamlit as st

st.set_page_config(
    page_title="Země zprávy",
    page_icon="📰",
    layout="wide",
)

st.title("📰 Země zprávy")
st.caption("České zpravodajství v kontextu.")

st.subheader("Přehled médií")

media = [
    "ČT24",
    "iROZHLAS",
    "Seznam Zprávy",
    "Deník N",
    "iDNES.cz",
]

for name in media:
    st.write(f"🗞️ {name}")

st.info("Zatím testovací verze — další krok bude načítání aktuálních zpráv.")
