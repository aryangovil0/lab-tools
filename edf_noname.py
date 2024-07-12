import mne
from mne.io import read_raw_edf
import os
from datetime import datetime

def anonymize_edf(input_file, output_dir):
    # Load the .EDF file
    raw = read_raw_edf(input_file, preload=True)
    
    # Anonymize the metadata
    raw.info['subject_info'] = None
    
    for key in ['subject_info', 'patientname', 'patient_additional', 'technician', 'equipment', 'admincode']:
        if key in raw._raw_extras[0]:
            raw._raw_extras[0][key] = "anonymized"

    print(f"Subject information anonymized for file: {input_file}")
    
    base_name = os.path.basename(input_file)
    name, ext = os.path.splitext(base_name)
    new_name = f"{name}_anonymized{ext}"
    output_file = os.path.join(output_dir, new_name)
    
    # Export the anonymized .EDF
    raw.export(output_file, fmt='EDF', overwrite=True)
    
    print(f"Anonymized file saved as: {output_file}")

def anonymize_folder(folder_path):
    start_time = datetime.now()
    print(f"Start time: {start_time}")
    
    # Create output directory
    folder_name = os.path.basename(folder_path.rstrip('/'))
    output_dir = os.path.join(folder_path, f"anonymized_{folder_name}")
    os.makedirs(output_dir, exist_ok=True)
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.edf'):
            input_file = os.path.join(folder_path, file_name)
            anonymize_edf(input_file, output_dir)
    
    end_time = datetime.now()
    print(f"End time: {end_time}")
    
    total_time_seconds = (end_time - start_time).total_seconds()
    print(f"Total time taken: {total_time_seconds} seconds")

# Main script
folder_path = input("Enter the path to the folder containing EDF files: ")
anonymize_folder(folder_path)