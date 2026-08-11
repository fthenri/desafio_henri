import os
import csv
from datetime import datetime

CSV_DIR = 'lh_nautical_csv'
OUTPUT_FILE = 'schema.sql'

def infer_type(value):
    if not value or value.strip() == '':
        return None
    
    val_lower = value.lower()
    if val_lower in ('true', 'false'):
        return 'BOOLEAN'
    
    try:
        int(value)
        return 'INTEGER'
    except ValueError:
        pass
        
    try:
        float(value)
        return 'NUMERIC'
    except ValueError:
        pass
        
    try:
        if len(value) >= 10 and value[4] == '-' and value[7] == '-':
            datetime.strptime(value[:19], '%Y-%m-%d %H:%M:%S')
            return 'TIMESTAMP'
    except ValueError:
        try:
            datetime.strptime(value[:10], '%Y-%m-%d')
            return 'DATE'
        except ValueError:
            pass

    return 'VARCHAR'

def resolve_type(type1, type2):
    if type1 is None: return type2
    if type2 is None: return type1
    if type1 == type2: return type1
    
    if {type1, type2} == {'INTEGER', 'NUMERIC'}: 
        return 'NUMERIC'
    if {type1, type2} == {'DATE', 'TIMESTAMP'}: 
        return 'TIMESTAMP'
    
    return 'VARCHAR'

def generate_schema():
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as sql_file:
        for filename in os.listdir(CSV_DIR):
            if not filename.endswith('.csv'):
                continue
            
            filepath = os.path.join(CSV_DIR, filename)
            table_name = filename[:-4]
            
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                try:
                    headers = next(reader)
                except StopIteration:
                    continue
                
                column_types = {header: None for header in headers}
                
                for i, row in enumerate(reader):
                    if i >= 100: 
                        break
                    for header, value in zip(headers, row):
                        inferred = infer_type(value)
                        column_types[header] = resolve_type(column_types[header], inferred)
                
            sql_file.write(f"CREATE TABLE {table_name} (\n")
            col_defs = []
            for header in headers:
                ctype = column_types[header] if column_types[header] else 'VARCHAR'
                col_defs.append(f"    {header} {ctype}")
            sql_file.write(",\n".join(col_defs) + "\n);\n\n")

if __name__ == '__main__':
    generate_schema()