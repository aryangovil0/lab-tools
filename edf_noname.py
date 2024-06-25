import mne
from mne.io import read_raw_edf
import os

def anonymize_edf(input_file):
    # Load the .EDF file
    raw = read_raw_edf(input_file, preload=True)
    
    # Anonymize the data
    raw.info['subject_info'] = None  # Remove subject info
    
    raw._raw_extras[0]['subject_info'] = None
    raw._raw_extras[0]['recording_id'] = None
    raw._raw_extras[0]['patientname'] = "anonymized"
    raw._raw_extras[0]['patient_additional'] = "anonymized"
    raw._raw_extras[0]['technician'] = "anonymized"
    raw._raw_extras[0]['equipment'] = "anonymized"
    raw._raw_extras[0]['admincode'] = "anonymized"

    print("Subject information anonymized")
    
    base_name = os.path.basename(input_file)
    dir_name = os.path.dirname(input_file)
    name, ext = os.path.splitext(base_name)
    new_name = f"{name}_anonymized{ext}"
    output_file = os.path.join(dir_name, new_name)
    
    # Save the anonymized .EDF
    raw.export(output_file, fmt='edf', overwrite=True)
    
    print(f"Anonymized file saved as: {output_file}")

# function
file_path = input("Enter the path to the EDF file: ")
anonymize_edf(file_path)