import pandas as pd

# Load the Excel file
file_path = "E:/PMAIP/xzt/data_AI/贵阳恒大群聊-新.xlsx"
df = pd.read_excel(file_path)

# Get the number of slices needed
num_slices = len(df) // 10 + (1 if len(df) % 10 != 0 else 0)

# Function to save each slice as a CSV file
def save_slices_to_csv(df, num_slices):
    for i in range(num_slices):
        # Calculate the start and end index for the slice
        start_index = i * 10
        end_index = (i + 1) * 10 if (i + 1) * 10 < len(df) else len(df)
        # Create the slice
        df_slice = df.iloc[start_index:end_index]
        # Define the CSV file name
        csv_file_name = f'slice_{i+1}.csv'
        # Save the slice to a CSV file
        df_slice.to_csv(csv_file_name, index=False)
    return num_slices

# Save the slices to CSV files and get the number of created files
num_csv_files_created = save_slices_to_csv(df, num_slices)
print(num_csv_files_created)
 
 
 