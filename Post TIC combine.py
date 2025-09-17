import pandas as pd
import os

def load_csv(file_path):
    return pd.read_csv(file_path, header=0, names=['Mass', 'Relative_Intensity']).set_index('Mass')

def merge_csvs(file_paths):
    combined_df = load_csv(file_paths[0])
    combined_df.columns = ['CSV1']
    
    for i, file_path in enumerate(file_paths[1:], start=2):
        next_df = load_csv(file_path)
        next_df.columns = [f'CSV{i}']
        combined_df = combined_df.merge(next_df, how='outer', left_index=True, right_index=True)
    
    combined_df.fillna(0, inplace=True)
    
    return combined_df

csv_files = [
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G5-1B Intensities.csv',  #Ctl
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G6-1B Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G7-1B Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G2-8B R1 Intensities.csv',   #SP3
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G2-8B R2 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G2-8B R3 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G3-10B R1 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G3-10B R2 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G3-10B R3 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-4B R1 Intensities.csv', 
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-4B R2 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-4B R3 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-10B R1 Intensities.csv',   #LP3
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-10B R2 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-10B R3 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G2-8B R1 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G2-8B R2 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G2-8B R3 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G3-8B R1 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G3-8B R2 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G3-8B R3 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-7B R1 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-7B R2 Intensities.csv',
    r'E:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SC3 SN3\\Intensities\\G4-7B R3 Intensities.csv'
]
merged_df = merge_csvs(csv_files)

output_csv_path = r'e:\\University\\SIMS Data\\Surface effect\\Ctl SP3 SN3 combined.csv'

merged_df.to_csv(output_csv_path)

print(f"CSV files merged successfully into {output_csv_path}")
