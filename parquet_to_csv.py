import pandas as pd
import time as timer

'''
Created by Jan Kyle Lewis T. Nolasco
'''

def convert_to_csv(parquet_file_path, rename_cols):
    parquet_df = pd.read_parquet(parquet_file_path)

    #rename cols
    parquet_df.rename(columns=rename_cols, inplace=True)

    print(len(parquet_df.index))
    parquet_df.to_csv('coverted_parquet.csv', index=False)

def main():
    parquet_file_path=""
    rename_cols={

    }
    convert_to_csv(parquet_file_path, rename_cols)

if __name__ == "__main__":
    start = timer.time()
    main()
    end = timer.time()
    total_time = (end - start) / 60
    print(f"Elapsed Time: {total_time} mins")