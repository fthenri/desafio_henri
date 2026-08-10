# Desafio Indicium - LH Nautical

Este repositório contém a solução estruturada para o pipeline de dados e IA da LH Nautical, utilizando a Arquitetura Medalhão.

## Estrutura de Diretórios

*   **`data/bronze/`**: Dados brutos originais recebidos (`lh_nautical_csv`). Nenhuma alteração é feita aqui.
*   **`data/silver/`**: Dados limpos, com tipos padronizados e tratamento de valores nulos.
*   **`data/gold/`**: Tabelas modeladas (Fatos e Dimensões), agregadas e prontas para consumo de BI (Dashboards) e Machine Learning.
*   **`scripts/`**: Scripts Python para ingestão, transformação (ETL) e análise.
*   **`docs/`**: Documentação complementar, metadados gerados (ex: `metadata_summary.json`) e dicionário de dados.