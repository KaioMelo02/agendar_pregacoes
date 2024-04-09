import streamlit as st
import pandas as pd

# Define o estilo da página
def style():
    st.markdown("""
        <style>
            .reportview-container {
                background: #f7f7f7;
            }
            .sidebar .sidebar-content {
                background: #37474f;
                color: #ffffff;
            }
            .Widget>label {
                color: #ffffff;
            }
            .stButton>button {
                color: #ffffff;
                background-color: #1976d2;
            }
            .stTextInput>div>div>input {
                background-color: #455a64;
                color: #ffffff;
            }
            .stTable>div>div>div>div>div>table {
                color: #ffffff;
            }
            /* Estilo personalizado para o seletor de data */
            .stDateInput>div {
                background-color: #455a64 !important;
                border-radius: 10px !important;
            }
            .stDateInput>div>div>input {
                color: #ffffff !important;
            }
            .stDateInput>div>div>div>div>div>div>div {
                background-color: #1976d2 !important;
                border-radius: 5px !important;
            }
        </style>
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