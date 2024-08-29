# import pandas as pd
# import os
# for i in range(1,30):
#     path="E:/PMAIP/xzt/data_AI/slice_+{i}+.csv"
#     df=pd.read_csv(path)
#     # Split the content column into individual rows
#     split_content = df['内容'].str.split(r'\n').tolist()

#     # Flatten the list of lists to get all individual rows
#     all_rows = [item for sublist in split_content for item in sublist]

#     # Combine all rows into a single string with periods as separators
#     combined_content = '。'.join(all_rows)

#     # Write the combined content to a TXT file
#     txt_file_path = 'E:/PMAIP/xzt/data_AI/slice+{i}.txt'
#     with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
#         txt_file.write(combined_content)

import pandas as pd
import os

for i in range(1, 30):
    # Correct the file path using f-string for formatting
    csv_file_path = f"E:/PMAIP/xzt/data_AI/slice_{i}.csv"
    txt_file_path = f"E:/PMAIP/xzt/data_AI/txt/slice_{i}.txt"
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Check if '内容' column exists in the DataFrame
    if '内容' in df.columns:
        # Split the '内容' column into individual rows
        split_content = df['内容'].str.split(r'\n').tolist()

        # Flatten the list of lists to get all individual rows
        all_rows = [item for sublist in split_content for item in sublist if item]  # Added a check to avoid empty strings

        # Combine all rows into a single string with periods as separators
        combined_content = '。'.join(all_rows)

        # Write the combined content to a TXT file
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(combined_content)
    else:
        print(f"Column '内容' not found in {csv_file_path}")
