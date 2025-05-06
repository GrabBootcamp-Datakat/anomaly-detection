<<<<<<< HEAD
import pandas as pd

# Load the original log CSV file
file_path = "result/merged_logs.log_structured.csv"  # Replace with the correct path if needed
df = pd.read_csv(file_path)

# Define labeling logic: "Abnormal" if any "Level" is "ERROR" for a given Container_ID
def label_container(group):
    return 'abnormal' if 'ERROR' in group['Level'].values else 'normal'

# Group by Container_ID and apply the label
summary_df = df.groupby('Container_ID').apply(label_container).reset_index()
summary_df.columns = ['Container_ID', 'Label']

# Save the output to a new CSV file
output_path = "result/merged_labled.csv"
summary_df.to_csv(output_path, index=False)

print("Summary file created:", output_path)
=======
import pandas as pd

# Load the original log CSV file
file_path = "result/merged_logs.log_structured.csv"  # Replace with the correct path if needed
df = pd.read_csv(file_path)

# Define labeling logic: "Abnormal" if any "Level" is "ERROR" for a given Container_ID
def label_container(group):
    return 'abnormal' if 'ERROR' in group['Level'].values else 'normal'

# Group by Container_ID and apply the label
summary_df = df.groupby('Container_ID').apply(label_container).reset_index()
summary_df.columns = ['Container_ID', 'Label']

# Save the output to a new CSV file
output_path = "result/merged_labled.csv"
summary_df.to_csv(output_path, index=False)

print("Summary file created:", output_path)
>>>>>>> 2ba4dafa332bd1f4d7b245a7011b588af28727e0
