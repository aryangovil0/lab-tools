# lab-tools
for Blessing Lab, NYU Langone and NYU Grossman School of Medicine

### EDF Anonymization Script

This script anonymizes EDF (European Data Format) files by removing or replacing identifying metadata. It processes all EDF files in a specified folder, anonymizes them, and saves the anonymized files in a new subfolder within the input directory.

### Features
- Anonymizes subject information and metadata fields such as patient name, additional patient information, technician, equipment, and admin code.
- Processes all `.edf` files in a specified folder.
- Saves anonymized files in a subfolder named `anonymized_<original_folder_name>` within the input directory.
- Prints the total time taken to process all files in seconds.

### Prerequisites
- Python 3.6 or higher
- The following Python packages:
  - `mne` (for reading and exporting EDF files)
  - `os` (for file and directory operations)
  - `datetime` (for tracking and printing processing time)

You can install the required packages using pip:
```sh
pip install mne