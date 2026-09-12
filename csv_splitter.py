"""
Splits a CSV file into multiple output files, one per unique 'alias' value.

How it works:
1. Read the input file.
2. Group all rows by the 'alias' column.
3. Write each group to its own CSV file.
"""

import pandas as pd
import os

INPUT_FILE = r"Input_path/file.csv"
SEPERATOR = ","     # column separator in the input file
OUTPUT_FOLDER = r"Output_path"

def main(input_file):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    df = pd.read_csv(input_file, delimiter=SEPERATOR, dtype=str)
    df = df.dropna(how="all")       #removes empty rows

    for alias, group in df.groupby("alias"):
        output_path = os.path.join(OUTPUT_FOLDER, f"{alias}.csv")
        group.to_csv(output_path, sep=SEPERATOR, index=False)
        print(f"Created {output_path} ({len(group)} rows)")

if __name__ == "__main__":
    main(INPUT_FILE)