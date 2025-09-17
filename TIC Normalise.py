import pandas as pd
import os

def tic_normalize(input_csv, specified_masses, instrument_resolution_ppm=50):
    """
    TIC-normalize mass spectrometry data and calculate relative intensities for specified peaks
    based on instrument resolution (in ppm).

    :param input_csv: Path to the input CSV file.
    :param specified_masses: List of mass values to calculate relative intensity for.
    :param instrument_resolution_ppm: Resolution of the instrument in parts per million (ppm).
    :return: A DataFrame with normalized data and relative intensities of specified peaks.
    """
    # Load the data
    data = pd.read_csv(input_csv)
    
    # Ensure columns exist
    if not all(col in data.columns for col in ['Mass', 'Intensity']):
        raise ValueError("Input CSV must contain 'Mass' and 'Intensity' columns.")
    
    # TIC normalization
    total_intensity = data['Intensity'].sum()
    data['Normalized_Intensity'] = data['Intensity'] / total_intensity

    # Calculate relative intensities for specified peaks
    relative_intensities = []
    for mass in specified_masses:
        # Calculate the resolution window for the instrument at the given mass
        tolerance = mass * instrument_resolution_ppm / 1_000_000
        
        # Find rows within the mass resolution window
        matched_peaks = data[(data['Mass'] >= mass - tolerance) & 
                             (data['Mass'] <= mass + tolerance)]
        # Sum normalized intensities of matched peaks
        relative_intensity = matched_peaks['Normalized_Intensity'].sum()
        relative_intensities.append({
            'Mass': mass,
            'Relative_Intensity': relative_intensity
        })

    # Convert results to a DataFrame
    result_df = pd.DataFrame(relative_intensities)
    
    return data, result_df


# Example usage:
if __name__ == "__main__":
    # Input file and specified masses
    input_file = 'C:\Elkan File Transfer\TIC Normalise test files\G3-8 Brain.csv'  # Replace with your CSV file path
    masses_to_check = [369.35, 770.51, 739.46, 844.50]  # Replace with your desired mass list

    # Perform normalization and calculate relative intensities
    normalized_data, peak_intensities = tic_normalize(input_file, masses_to_check)

    # Save results to CSVs
    normalized_data.to_csv('C:\Elkan File Transfer\TIC Normalise test files\G3-8 Brain_normalised.csv', index=False)
    peak_intensities.to_csv('C:\Elkan File Transfer\TIC Normalise test files\G3-8 Brain_normalised_intensities.csv', index=False)

    # Print results
    print("Normalized Data:")
    print(normalized_data.head())
    print("\nPeak Intensities:")
    print(peak_intensities)
