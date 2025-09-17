import pandas as pd

def ppm_difference(mz1, mz2):
    return abs((mz1 - mz2) / mz1) * 1e6

def merge_mz_values(df, ppm_threshold=50):
    merged_data = []
    current_group = [df.iloc[0].tolist()]

    for i in range(1, len(df)):
        current_mz = df.loc[i, 'm/z']
        prev_mz = df.loc[i-1, 'm/z']

        if ppm_difference(current_mz, prev_mz) <= ppm_threshold:
            current_group.append(df.iloc[i].tolist())
        else:
            merged_data.append(merge_group(current_group))
            current_group = [df.iloc[i].tolist()]

    if current_group:
        merged_data.append(merge_group(current_group))
    
    return pd.DataFrame(merged_data, columns=df.columns)

def merge_group(group):
    mz_values = [row[0] for row in group]
    avg_mz = sum(mz_values) / len(mz_values)
    
    summed_intensities = [sum(row[i] for row in group) for i in range(1, len(group[0]))]
    
    return [avg_mz] + summed_intensities

def process_csv(input_file, output_file, ppm_threshold=50):
    try:
        df = pd.read_csv(input_file)
        print(f"Successfully read the file: {input_file}")
        print(df.head())

    except FileNotFoundError:
        print(f"Error: File {input_file} not found. Please check the path.")
        return

    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file: {e}")
        return

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    if 'm/z' not in df.columns:
        print("Error: 'm/z' column not found in the CSV file.")
        return

    df = df.sort_values(by='m/z').reset_index(drop=True)

    merged_df = merge_mz_values(df, ppm_threshold)

    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV saved to {output_file}")

input_csv = r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3.csv'
output_csv = r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3 Aligned.csv'
process_csv(input_csv, output_csv)
