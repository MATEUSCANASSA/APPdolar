# Projeto de Cotação de Dólar - API do Banco Central

Este é um projeto desenvolvido em Python para consultar a cotação do dólar usando a API do Banco Central do Brasil. Permite consultar tanto a cotação de compra quanto a de venda. 


## Requisitos

- **Versão do Python**: 3.11.0
- **Dependências**: Pacotes listados no arquivo `requirements.txt`.

### Para instalar as dependências, execute o seguinte comando:
    ```shell script
    $> (venv) python -m pip install -r requirements.txt
    ```
## API utilizada
 [`API's Banco Central`][api-olinda-bc]

[api-olinda-bc]: https://dadosabertos.bcb.gov.br/dataset/expectativas-mercado/resource/d420a704-75a7-4f45-8f4b-0fca813c70f0

## TODO:

- [x] Modificar o código para incluir a cotação de venda da nova API.
- [x] Ajustar o gráfico para exibir a cotação de compra e venda em eixos Y separados.
- [x] Atualizar o código para gerar duas colunas no arquivo Excel: uma para a cotação de compra e outra para a cotação de venda.
- [x] Testar a nova implementação com diferentes períodos de consulta.
