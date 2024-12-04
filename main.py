import os.path
import tkinter.font
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import sys
import requests

# Define root
root = Tk()

# Geometric properties
# root.geometry('400x360')  # Tamanho da tela
root.resizable(width=False, height=False)  # Bloquea redimensionamento

# Name properties
root.title('Consulta Dolar')


def obter_cotacoes(data_inicial, data_final):
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%27{data_inicial}%27&@dataFinalCotacao=%27{data_final}%27&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"

    response = requests.get(url)  # Fazendo a requisição GET para a API
    if response.status_code == 200:  # Verificando se a requisição foi bem-sucedida
        return response.json()  # Retorna os dados em formato JSON
    else:
        print("Erro ao fazer a requisição:", response.status_code)
        return None


def transformar_em_dataframe(dados_json):
    # A chave 'value' contém a lista com os dados da cotação
    dados = dados_json.get("value", [])

    # Criando o DataFrame com as colunas 'cotacaoCompra', 'cotacaoVenda', e 'dataHoraCotacao'
    df = pd.DataFrame(dados)

    # Convertendo a coluna 'dataHoraCotacao' para o formato de data e hora
    df['dataHoraCotacao'] = pd.to_datetime(df['dataHoraCotacao'])

    return df


def gerar_grafico(df, data_inicial, data_final):
    data_inicial_graph = data_inicial.strftime('%d/%m/%Y')
    data_final_graph = data_final.strftime('%d/%m/%Y')

    # Plotando a cotação de compra
    plt.figure(figsize=(10, 6))  # Ajustando o tamanho da figura para melhor visualização
    plt.plot(df['dataHoraCotacao'], df['cotacaoCompra'], marker='o', color='b', label='Cotação de Compra')

    # Plotando a cotação de venda
    plt.plot(df['dataHoraCotacao'], df['cotacaoVenda'], marker='o', color='r', label='Cotação de Venda')

    # Adicionando os valores das cotações de compra e venda no gráfico
    for x, y in zip(df['dataHoraCotacao'], df['cotacaoCompra']):
        plt.text(x, y, f'{y:.4f}', fontsize=9, ha='center', va='bottom')

    for x, y in zip(df['dataHoraCotacao'], df['cotacaoVenda']):
        plt.text(x, y, f'{y:.4f}', fontsize=9, ha='center', va='top')

    # Configurando o título e os rótulos
    plt.title(f'Histórico de cotações do dólar de {data_inicial_graph} a {data_final_graph}')
    plt.xlabel('Data')
    plt.ylabel('Cotação')

    # Melhorando a visualização das datas no eixo X
    plt.xticks(rotation=45)  # Rotacionando as datas para melhor legibilidade
    plt.tight_layout()  # Ajustando para que o gráfico não sobreponha os rótulos

    # Exibindo a legenda
    plt.legend()

    # Exibindo o gráfico
    plt.show()


def gerar_excel(df):
    df.to_excel('Dolar.xlsx', index=False)
    tkinter.messagebox.showinfo(title="AVISO", message="Arquivo gerado com sucesso!!")


def on_gerar_click(data_inicial_entry, data_final_entry, tipo=0):
    data_inicial = data_inicial_entry.get()
    data_final = data_final_entry.get()

    try:
        data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
        data_final = datetime.strptime(data_final, '%d/%m/%Y')
    except ValueError:
        print('Data inválida. Por favor, digite a data no formato dd/mm/aaaa.')
        return

    # Converte para o formato da API atualizada
    data_inicial_api = data_inicial.strftime('%m-%d-%Y')
    data_final_api = data_final.strftime('%m-%d-%Y')
    json = obter_cotacoes(data_inicial_api, data_final_api)

    if json is None:
        return

    df = transformar_em_dataframe(json)

    if tipo == 0:
        gerar_grafico(df, data_inicial, data_final)
    else:
        gerar_excel(df)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def informacoes():
    top = Toplevel(root)
    top.geometry("300x200")
    top.title("Sobre")
    Label(top, text="Engenharia e Design: Mateus Canassa").pack()
    Label(top, text="Consultoria Tecnica: João G. Ribeiro").pack()
    Label(top, text="").pack()
    Label(top, text="").pack()
    Label(top, text="© Copyright: Todos os direitos reservados MSC & JGR").pack()


class Application:
    def __init__(self, master=None):
        self.Manager = None

        self.cont_principal = ttk.Frame(master)
        self.cont_principal.pack(fill=BOTH, expand=True)

        self.cont_title = ttk.Frame(self.cont_principal)
        self.cont_title.pack(ipady=15, fill=BOTH, expand=True)

        self.cont_input = ttk.Frame(self.cont_principal)
        self.cont_input.pack(ipady=10, fill=BOTH, expand=True)

        self.cont_btn = ttk.Frame(self.cont_principal)
        self.cont_btn.pack(fill=BOTH, expand=True)

        self.cont_copy = ttk.Frame(self.cont_principal)
        self.cont_copy.pack()

        # Placeholder
        # ttk.Label(self.cont_title, text="<imagem aqui>").grid()

        # Abre a imagem e redimensiona
        base_image = Image.open(resource_path("dolar.jpg")).resize((150, 80))
        logo_dol = ImageTk.PhotoImage(base_image)
        self.imagem = Label(self.cont_title, image=logo_dol, cursor="cross")
        self.imagem.image = logo_dol
        self.imagem.pack(anchor=CENTER, expand=True)
        self.imagem.bind("<Button-1>", lambda e: informacoes())

        # Input sub frames
        self.sub_cont_input_left = ttk.Frame(self.cont_input)
        self.sub_cont_input_left.grid(row=0, column=0, sticky=NSEW)

        self.sub_cont_input_right = ttk.Frame(self.cont_input)
        self.sub_cont_input_right.grid(row=0, column=1, sticky=NSEW)

        custom_font = tkinter.font.Font(family='Arial', size=12)

        # Labels dos inputs
        ttk.Label(self.sub_cont_input_left, text="Data inicial:", font=custom_font).pack(
            side="top", fill="x", anchor=CENTER, padx=(10, 0), pady=(0, 10)
        )
        ttk.Label(self.sub_cont_input_left, text="Data final:", font=custom_font).pack(
            side="top", fill="x", anchor=CENTER, padx=(10, 0)
        )

        # Inputs
        self.input_user = ttk.Entry(self.sub_cont_input_right, width=30)
        self.input_user.pack(padx=(15, 0), pady=(0, 10))

        self.input_pass = ttk.Entry(self.sub_cont_input_right, width=30)
        self.input_pass.pack(padx=(15, 0))

        # Definição dos botões
        self.bnt_grafico = ttk.Button(
            self.cont_btn, text="Grafico",
            command=lambda inp1=self.input_user, inp2=self.input_pass: on_gerar_click(inp1, inp2)
        )
        self.bnt_grafico.pack(side=LEFT, expand=True)

        self.bnt_excel = ttk.Button(
            self.cont_btn, text="Excel",
            command=lambda inp1=self.input_user, inp2=self.input_pass: on_gerar_click(inp1, inp2, tipo=1)
        )
        self.bnt_excel.pack(side=LEFT, expand=True)

        self.bnt_cancel = ttk.Button(
            self.cont_btn, text="Cancelar", command=root.destroy
        )
        self.bnt_cancel.pack(side=LEFT, expand=True)

        # Label do copyright
        self.label_copy = ttk.Label(self.cont_copy, text="© MSC & JGR")
        self.label_copy.pack(pady=5)


if __name__ == '__main__':
    Application(root)
    root.mainloop()
