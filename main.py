import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dasboard Auvo", page_icon=":bar_chart:",layout="wide")
st.title(" :bar_chart: Dasboard Auvo")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    df = pd.read_csv(r"data\Tasks.csv", sep=",", decimal=".")

col1, col2 = st.columns((2))
df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

# Getting the min and max date
startDate = pd.to_datetime(df["Data"]).min()
endDate = pd.to_datetime(df["Data"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

st.sidebar.header("Filtros:")

customer = st.sidebar.multiselect("Cliente:", df["Cliente"].unique())
if not customer:
    df2 = df.copy()
else:
    df2 = df[df["Cliente"].isin(customer)]

keyword = st.sidebar.multiselect("Palavra Chave:", df2["Projeto/Contrato"].unique())
if not keyword:
    df3 = df2.copy()
else:
    df3 = df2[df2["Projeto/Contrato"].isin(keyword)]

responsible = st.sidebar.multiselect("Responsável:", df3["Responsavel"].unique())
if not responsible:
    df4 = df3.copy()
else:
    df4 = df3[df3["Responsavel"].isin(responsible)]

tasktype = st.sidebar.multiselect("Tipo de tarefa:", df4["Tipo de tarefa"].unique())
if not tasktype:
    df5 = df4.copy()
else:
    df5 = df4[df4["Responsavel"].isin(responsible)]

role = st.sidebar.multiselect("Cargo:", df5["Cargo"].unique())
if not role:
    df6 = df5.copy()
else:
    df6 = df5[df5["Cargo"].isin(role)]

df = df6

tarefa_df = df.groupby(by = ["Responsavel"], as_index = False)["Tarefa"].count()

with col1:
    if not responsible or len(responsible) > 1:
        st.subheader("Tarefa x Responsavel")
        fig = px.bar(tarefa_df, x = "Tarefa", y = "Responsavel",
                     template = "seaborn", orientation = "h")
        st.plotly_chart(fig,use_container_width=True, height = 200)
    else:
        st.subheader("Total de Tarefas:")
        st.write(df["Tarefa"].count())