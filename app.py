
import streamlit as st

# 🔐 Sistema de Senha Simples
senha_correta = "TESTE789"
senha = st.sidebar.text_input("🔑 Digite a senha para acessar:", type="password")

if senha != senha_correta:
    st.error("🚫 Acesso negado. Senha incorreta.")
    st.stop()

# 🚀 Dashboard liberado após senha correta
st.set_page_config(page_title="m00 Dashboard", page_icon="🧠")
st.title("🧠 m00 Dashboard")

st.markdown("""
## 🔗 Menu lateral
→ Acesse as páginas no menu à esquerda  
→ Status da API, Logs, Banco e mais  

---
Powered by Streamlit 🔥
""")
