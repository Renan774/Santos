import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios de adoções passadas
adocoes_passadas = [
    {"animal": "Rex", "adotante": "Alice", "data": "2023-01-15"},
    {"animal": "Miau", "adotante": "Bob", "data": "2023-02-20"},
    {"animal": "Tweety", "adotante": "Carla", "data": "2023-03-10"}
]
df_adocoes_passadas = pd.DataFrame(adocoes_passadas)

# Função para plotar gráfico de adoções
def plotar_grafico(df):
    df['data'] = pd.to_datetime(df['data'])
    df['mes'] = df['data'].dt.to_period('M')
    adocoes_por_mes = df.groupby('mes').size()

    fig, ax = plt.subplots()
    adocoes_por_mes.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Adoções por Mês')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Número de Adoções')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

# Página inicial
st.title("Sistema de Adoção de Animais")

# Formulário de Adoção
st.header("Formulário de Adoção")
with st.form(key='adoption_form'):
    nome_adotante = st.text_input("Nome do Adotante")
    endereco = st.text_input("Endereço")
    telefone = st.text_input("Telefone")
    nome_animal = st.text_input("Nome do Animal")
    raca = st.text_input("Raça")
    cor = st.text_input("Cor")
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
    castrado = st.selectbox("Castrado?", ["Sim", "Não"])
    vacinado = st.selectbox("Vacinado?", ["Sim", "Não"])
    data_adocao = st.date_input("Data de Adoção")
    submit_button = st.form_submit_button(label='Enviar Solicitação')

    if submit_button:
        novo_dado = {
            "nome_adotante": nome_adotante,
            "endereco": endereco,
            "telefone": telefone,
            "nome_animal": nome_animal,
            "raca": raca,
            "cor": cor,
            "sexo": sexo,
            "castrado": castrado,
            "vacinado": vacinado,
            "data_adocao": data_adocao,
        }

        df_novo_dado = pd.DataFrame([novo_dado])
        df_novo_dado.to_csv('dados_adocao.csv', mode='a', header=False, index=False)
        st.success(f"Sua solicitação para adotar o {nome_animal} foi enviada com sucesso!")

# Gráfico de adoções passadas
plotar_grafico(df_adocoes_passadas)
