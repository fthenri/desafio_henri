import os
import psycopg2

CSV_DIR = 'lh_nautical_csv'

def load_data():
    conn = psycopg2.connect(
        dbname="lh_nautical",
        user="postgres", # mude o user caso necessario
        password="senha", # mude a senha aqui
        host="localhost",
        port="5433" # mude para a porta do postgresql que voce esteja usando (no meu caso é 5433)
    )
    cur = conn.cursor()

    for filename in os.listdir(CSV_DIR):
        if filename.endswith('.csv'):
            table_name = filename[:-4]
            filepath = os.path.join(CSV_DIR, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)
            
            conn.commit()

    cur.close()
    conn.close()

if __name__ == '__main__':
    load_data()