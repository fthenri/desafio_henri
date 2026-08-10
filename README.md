# Desafio Indicium - LH Nautical

Este repositório contém a solução estruturada para o pipeline de dados e IA da LH Nautical, focado em escalabilidade, reprodutibilidade e geração de valor de negócio.

## Arquitetura e Decisões de Projeto

Para garantir organização e performance, o projeto foi estruturado com base nas seguintes premissas:

*   **Data Profiling Automatizado:** Em vez de explorações manuais, implementamos um extrator de metadados (`extract_metadata.py`) na origem. Isso mapeia esquemas, tipos, volumetria e valores nulos de forma automatizada, garantindo previsibilidade para a engenharia de dados.
*   **Arquitetura Medalhão:** Separação lógica em três camadas (Bronze, Silver e Gold) para assegurar a rastreabilidade do dado, desde sua ingestão bruta até o consumo final por ferramentas de BI e modelos de Machine Learning.
*   **Adoção do Formato Parquet:** Na transição da camada Bronze para a Silver, os arquivos CSV são convertidos para `.parquet`. Isso garante compressão otimizada, leitura mais rápida e a preservação estrita dos tipos de dados (especialmente datas e IDs), evitando reprocessamento em etapas futuras.

## Estrutura de Diretórios

*   **`data/bronze/`**: Dados brutos originais recebidos (`lh_nautical_csv`). Nenhuma alteração é feita aqui.
*   **`data/silver/`**: Dados limpos e convertidos para `.parquet`, com padronização de nomenclatura de colunas e tipagem correta.
*   **`data/gold/`**: Tabelas modeladas (Fatos e Dimensões), tratadas e prontas para análise de vendas, clientes, previsão de demanda e recomendação.
*   **`scripts/`**: Scripts modulares em Python para extração de metadados, pipelines ETL e modelagem.
*   **`docs/`**: Documentação de apoio, como o mapeamento estrutural (`metadata_summary.json`) e dicionários de dados.