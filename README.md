# Projeto de aplicativo de cotação de dolar escrito em pyhton consultando a API do banco central

# Quando fiz esse projeto, a API do BC disponibilizava apenas uma cotação a de compra, porém, hoje existe uma API mais abrangente, que tras as cotações de compra e de venda.

# Estou tentando mudar meu código para que ele traga as duas cotações, tanto no GRÁFICO quanto no EXCEL. 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='09-01-2024'&@dataFinalCotacao='09-30-2024'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao'

# Se possivel,me ajude a ajustar o código inserindo a nova API para trazer as cotações de compra e venda e a visualização do gráfico precisa demonstrar duas linhas em eixos diferentes e a planilha em excel deve gerar duas colunas, uma com o dolar compra e outra com o dolar venda.
