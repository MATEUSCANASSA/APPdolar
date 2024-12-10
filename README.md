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
- [ ] Implementar feedback para o usuário de possíveis erros relacionados a API ou ao APP. 
- [ ] Adicionar input no estilo "date picker" ao invés de digitar a data apenas.
- [ ] Otimizar o uso de funções e variáveis.
- [ ] Verificar e se possível otimizar imports realizados.
