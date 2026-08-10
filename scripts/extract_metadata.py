import pandas as pd
import os
import json
import numpy as np

def default_converter(o):
    if isinstance(o, np.integer): return int(o)
    if isinstance(o, np.floating): return float(o)
    if isinstance(o, np.ndarray): return o.tolist()
    return str(o)

def extract_metadata(bronze_path, output_path):
    metadata = {}
    
    for file in os.listdir(bronze_path):
        if file.endswith('.csv'):
            file_path = os.path.join(bronze_path, file)
            df = pd.read_csv(file_path, low_memory=False)
            
            metadata[file] = {
                "shape": df.shape,
                "columns": list(df.columns),
                "dtypes": df.dtypes.astype(str).to_dict(),
                "missing_values": df.isnull().sum().to_dict(),
                "sample": df.head(2).to_dict(orient='records')
            }
            
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, default=default_converter, indent=4)

if __name__ == "__main__":
    extract_metadata("data/bronze/lh_nautical_csv", "docs/metadata_summary.json")