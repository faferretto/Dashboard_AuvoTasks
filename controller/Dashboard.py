import streamlit as st
import time

class Dashboard:

    def __init__(self, data_loader, update_interval):
        self.data_loader = data_loader
        self.update_interval = update_interval

    def show_dashboard(self):
        st.title("Dashboard em Tempo Real com Dados do CSV")

        while True:
            df = self.data_loader.load_data()
            st.write(df)  # Exibe os dados do CSV

            st.write("Atualizando em tempo real...")
            time.sleep(self.update_interval)  # Aguarda o intervalo para a próxima atualização


