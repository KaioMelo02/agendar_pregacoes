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

# Título do aplicativo
st.title("Agendar de Pregação")

# Criando campos para entrada de dados
data = st.date_input("Data da Pregação", format="DD/MM/YYYY")
hora = st.time_input("Horário da Pregação")
local = st.text_input("Local da Pregação")
pregador = st.text_input("Nome do Pregador")

# Botão para adicionar a pregação ao agendamento
if st.button("Agendar Pregação"):
    # Salvar os dados em um dataframe ou em um arquivo
    novo_agendamento = pd.DataFrame({
        "Data": [data],
        "Horário": [hora],
        "Local": [local],
        "Pregador": [pregador]
    })

    # Anexar ao dataframe existente ou salvar em um arquivo Excel
    try:
        agendamentos = pd.read_excel("agendamentos.xlsx")
        agendamentos = pd.concat([agendamentos, novo_agendamento], ignore_index=True)
    except FileNotFoundError:
        agendamentos = novo_agendamento

    agendamentos.to_excel("agendamentos.xlsx", index=False)

    # Feedback para o usuário
    st.success("Pregação agendada com sucesso!")

# Mostrar agendamentos existentes
st.header("Agendamentos")
try:
    agendamentos = pd.read_excel("agendamentos.xlsx")
    st.table(agendamentos)
except FileNotFoundError:
    st.warning("Nenhum agendamento encontrado.")