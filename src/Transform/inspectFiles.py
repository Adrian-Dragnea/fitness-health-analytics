import pandas as pd
from pathlib import Path

RAW_DIR = Path("/mnt/nas/Projects/fitness-health-analytics/data/raw") 

def inspect():
    files = list(RAW_DIR.glob("*.xlsx*"))

    print(f"Found {len(files)} raw files")

    for f in files:
        print("\nFile:", f.name)
        xlsx = pd.ExcelFile(f)
        print("Sheets:", xlsx.sheet_names)

        df = pd.read_excel(f, sheet_name=xlsx.sheet_names[0])
        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        print(df.head(3))

if __name__ == "__main__":
    inspect()
