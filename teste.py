import streamlit as st
import pandas as pd

def style():
    st.markdown("""
        ... seu CSS aqui ...
    """, unsafe_allow_html=True)

style()

st.title("Agendar de Pregação")

data = st.date_input("Data da Pregação", format="DD/MM/YYYY")
hora = st.time_input("Horário da Pregação")
local = st.text_input("Local da Pregação")
pregador = st.text_input("Nome do Pregador")

# Tente carregar os agendamentos existentes antes do botão ser pressionado
try:
    agendamentos = pd.read_excel("agendamentos.xlsx")
except FileNotFoundError:
    agendamentos = pd.DataFrame(columns=["Data", "Horário", "Local", "Pregador"])

# Mostra os agendamentos existentes
st.header("Agendamentos")
if not agendamentos.empty:
    st.table(agendamentos)
else:
    st.warning("Nenhum agendamento encontrado.")

if st.button("Agendar Pregação"):
    novo_agendamento = pd.DataFrame({
        "Data": [data],
        "Horário": [hora],
        "Local": [local],
        "Pregador": [pregador]
    })

    agendamentos = pd.concat([agendamentos, novo_agendamento], ignore_index=True)
    
    agendamentos.to_excel("agendamentos.xlsx", index=False)

    st.success("Pregação agendada com sucesso!")
    st.balloons()  # Mostra animação de balões como feedback visual

    # Atualiza a visualização dos agendamentos com o novo dado adicionado
    st.table(agendamentos)