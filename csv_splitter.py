import pandas as pd
import time as timer
import os

'''
Created by Jan Kyle Lewis T. Nolasco
'''

def split_csv(csv_folder, split_length, output_folder):
    #create output folder
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for csv_file in os.listdir(csv_folder):
        print("Current: ", csv_file)
        csv_df=pd.read_csv(os.path.join(csv_folder, csv_file))
        csv_len=len(csv_df.index)
        csv_file_prefix=csv_file.split(".")[0]
        if csv_len>split_length:
            print("Greater than split length, splitting . . . ")
            print("Total Length: ", csv_len)
            start_index=0
            end_index=split_length-1
            for i in range(csv_len//split_length+1):
                print(f"Current Range: {start_index} to {end_index}" )
                curr_split_df=csv_df.loc[start_index:end_index]
                start_index=start_index+split_length
                end_index=end_index+split_length
                print(curr_split_df)

                #export
                if i+1<10:
                    curr_split_df_suffix=f"_P0{i+1}.csv"
                elif i+1>=10:
                    curr_split_df_suffix = f"_P{i+1}.csv"
                curr_split_df_file_name=csv_file_prefix+curr_split_df_suffix

                #only export if df is not empty
                if not curr_split_df.empty:
                    curr_split_df.to_csv(os.path.join(output_folder, curr_split_df_file_name),
                                         index_label="Source Index")

        else:
            print("Less than split length, directly exporting . . . ")
            print("Total Length: ", csv_len)
            curr_split_df_suffix=f"_P01.csv"
            curr_split_df_file_name = csv_file_prefix + curr_split_df_suffix
            csv_df.to_csv(os.path.join(output_folder, curr_split_df_file_name), index_label="Source Index")

def main():
    csv_folder = "csv_to_split"
    output_folder = "csv_splitter_output"
    split_length=10000
    split_csv(csv_folder, split_length, output_folder)

if __name__ == "__main__":
    start = timer.time()
    main()
    end = timer.time()
    total_time = (end - start) / 60
    print(f"Elapsed Time: {total_time} mins")