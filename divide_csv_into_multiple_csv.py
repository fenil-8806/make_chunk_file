import pandas as pd
import os

def divide_csv(input_file, num_files):
    # Create a directory to store the divided CSV files
    output_dir = 'non_matched_output_5_8'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read CSV file
    if str(input_file).endswith('.xlsx'):
        df = pd.read_excel(input_file,sheet_name="Sheet1")
    else:
        df = pd.read_csv(input_file)
    
    # Calculate number of rows per file
    total_rows = len(df)
    rows_per_file = total_rows // num_files
    remainder = total_rows % num_files
    
    # Split DataFrame into multiple DataFrames
    split_dfs = []
    start_index = 0
    for i in range(num_files):
        extra_row = 1 if i < remainder else 0
        end_index = start_index + rows_per_file + extra_row
        split_dfs.append(df.iloc[start_index:end_index])
        print(start_index,"---->",end_index)
        start_index = end_index
    
    # Write each DataFrame to a CSV file
    for i, split_df in enumerate(split_dfs, start=1):
        file_name = f"{output_dir}/chunk_{i}.csv"
        # split_df.to_csv(file_name, index=False)
        split_df.to_csv(file_name, index=False)

if __name__ == "__main__":
    input_file = 'non_matched_output_5_8.csv'
    divide_csv(input_file, 5)
    print("CSV file has been divided into multiple files successfully.")
