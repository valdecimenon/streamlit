#============  SOFTGRAF Cursos Avançados ============#
#            por Valdeci Menon - maio/2024           #
#====================================================#

#Criando ambiente virtual: python -m venv venv
#Ativando o ambiente:      .\venv\Scripts\activate
#Executando app:           python -m streamlit run PrimeiroApp.py

# importações
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

 
# título da página
st.title('Meu primeiro app :sunglasses:')

st.image('https://www.softgraf.com/icones/logo_softgraf.png', width=200)

st.header('Este é um header com um divisor', divider='rainbow')

st.subheader('Este é um subheader: _Streamlit_ é :blue[legal]')

st.write('Este é um *Texto* comum')

"Texto Mágico!"
texto = "Texto na Variável"
texto

x = 10
'x', x 

st.markdown("Markdown: *Streamlit* é **realmente** ***legal***.")
st.markdown('''
    :red[Streamlit] :orange[pode] :green[escrever] :blue[texto] :violet[em]
    :gray[muitas] :rainbow[cores] e :blue-background[texto destacado].
''')

multi = '''Se terminar a linha com dois espacos,  
uma quebra de linha suave é usada para a próxima linha.

Dois ou mais ENTER resulta em apenas uma quebra de linha.
'''
st.markdown(multi)


#----------------------------------------------------------------
st.subheader('Abas', divider='red')
aba1, aba2, aba3 = st.tabs(['Tabelas', 'Gráficos', 'Histogramas'])

with aba1:
    st.write('Exibindo um DataFrame com Streamlit')
    df = pd.read_excel('produtos.xlsx')
    df

with aba2:
    st.write('Exibindo um gráfico de linhas')
    #cria um array de 20 linhas x 3 colunas, com valores randômicos (distribuição padrão)
    arr = np.random.randn(20, 3)
    tabela = pd.DataFrame(arr, columns=["a", "b", "c"])
    st.line_chart(tabela)

with aba3:
    st.write('Exibindo um histograma')
    #cria uma distribuição normal aleatória de tamanho 100 com média 1 e desvio padrão 1
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    fig

#-------------------------------------------
st.subheader('Input widgets', divider='red')

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Reset", type="primary")
    aceito = st.checkbox("Aceito os termos")
    if aceito:
        st.write("Aceitou!")

with col2:
    if st.button("Salvar"):
        st.write("Você clicou em Salvar")
    else:
        st.write("Reiniciou")

    on = st.toggle("Ligar recurso")
    if on:
        st.write("Recurso ativado!")

with col3:
    st.link_button("Ir para galeria", "https://streamlit.io/gallery")
    cor = st.color_picker("Escolha uma cor", "#00f900")
    st.write("A cor escolhida foi: ", cor)


texto = st.text_input(
                      label = "Digite um texto",
                      value = "Este é o texto padrão",
                      placeholder="isto é o placeholder",
                     )
st.write("Você digitou: ", texto)


area = st.text_area(
    "Área de texto",
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
    "when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    )

st.write(f"Você digitou {len(area)} caracteres.")


#observe que o chat estará fixo na parte inferior da tela
prompt = st.chat_input("Digite alguma coisa")
if prompt:
    st.write(':red[Usuário enviou o seguinte prompt:]', prompt)


numero = st.number_input("Digite um número")
st.write("Você digitou: ", numero)


d = st.date_input("Quando é seu aniversário?", dt.date(1996, 2, 16))
st.write("Seu aniversário é:", d)


idade = st.slider("Qual sua idade?", 0, 120, 25)
st.write("Eu tenho", idade, "anos")


opcoes = st.multiselect(
    "Selecione suas cores favoritas",
    ["Verde", "Amarelo", "Vermelho", "Azul"],
    ["Amarelo", "Vermelho"])

"Cores selecionadas:"
st.write(opcoes)


genero = st.radio(
    "Escolha seu gênero de filme favorito",
    [":rainbow[Comédia]", "***Drama***", "Documentário :movie_camera:"],
    index=None,
)

st.write("Você escolheu:", genero)


opcao = st.selectbox(
    "Como você gostaria de ser contactado?",
    ("Email", "Telefone", "Whatsapp"))

st.write("Você escolheu:", opcao)


cidades = ['Ponta Grossa', 'Curitiba', 'Castro', 'Carambeí', 'Piraí do Sul']
padroes = ['Curitiba', 'Castro', 'Carambeí']
with st.expander('Expander cidades'):
    escolhidas = st.multiselect('Selecione as cidades', cidades, padroes)

st.write("Cidades escolhidas:", escolhidas)

#barra lateral
with st.sidebar:
    mensagens = st.container(height=300)
    #novo 'operador morsa' :=  (a partir do python 3.8)
    if prompt := st.chat_input('Digite algo:'):
        mensagens.chat_message('usuario').write(prompt)
        mensagens.chat_message('assistente').write(f'Echo: {prompt}')


#-------------------------------------------
st.subheader('Páginas', divider='red')

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.page_link("PrimeiroApp.py", label="Home", icon="🏠")
 
with c2:
    st.page_link("pages/pag1.py", label="Página 1", icon="1️⃣")

with c3:
    st.page_link("pages/pag2.py", label="Página 2", icon="2️⃣", disabled=True)

with c4:    
    st.page_link("http://www.google.com", label="Google", icon="🌎")
