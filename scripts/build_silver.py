import pandas as pd
import os

def clean_and_save_silver(bronze_dir, silver_dir):

    os.makedirs(silver_dir, exist_ok=True)
    
    for file in os.listdir(bronze_dir):
        if file.endswith('.csv'):
            file_path = os.path.join(bronze_dir, file)
            print(f"processando: {file}...")
            
            df = pd.read_csv(file_path, low_memory=False)
            
            # padronizacao
            df.columns = [col.lower().strip() for col in df.columns]
            
            # conversao de colunas de datas
            date_columns = [col for col in df.columns if col.endswith('_at') or col.endswith('_date')]
            for date_col in date_columns:
                df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
                
            # tratamento de ids nulos
            id_columns = [col for col in df.columns if col.endswith('_id')]
            for id_col in id_columns:
                df[id_col] = df[id_col].astype('Int64')
                
            # parquet
            table_name = file.replace('.csv', '.parquet')
            silver_path = os.path.join(silver_dir, table_name)
            
            df.to_parquet(silver_path, index=False)
            print(f"salvo com sucesso em: {silver_path}\n")

if __name__ == "__main__":
    BRONZE_PATH = "data/bronze/lh_nautical_csv"
    SILVER_PATH = "data/silver"
    
    print("iniciando processamento na camada silver...\n")
    clean_and_save_silver(BRONZE_PATH, SILVER_PATH)
    print("processamento concluido")