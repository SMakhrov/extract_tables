# Table Extraction Script

## Overview
This script extracts tables from **PDF** and **HTML** files. It processes all supported files located in the `input_files` directory and saves the extracted tables as CSV files in the `extracted_tables` directory.

The script supports:
- Extracting tables from **PDF** files using `pdfplumber`.
- Extracting tables from **HTML** files using `BeautifulSoup` and `pandas`.
- Automatically ignores unsupported files (e.g., `git.keep`, `.txt`, etc.).

---

## Prerequisites
Ensure you have the following installed:
1. **Python 3.8 or higher**
2. Install the required Python libraries using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   
## Folder Structure
The script expects the following folder structure:
```
project/
├── extract.py          # The main script
├── requirements.txt    # Dependencies file
├── input_files/        # Directory for input files
│   ├── file1.pdf
│   ├── file2.html
│   └── git.keep
├── extracted_tables/   # Directory for output CSV files (created automatically)
```

## How to Use

1. **Place Input Files**:
   - Add all your **PDF** and **HTML** files to the `input_files` directory.

2. **Install Dependencies**:
   - Ensure all required dependencies are installed:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Script**:
   - Execute the script from the command line:
     ```bash
     python extract.py
     ```

4. **Check the Results**:
   - Extracted tables will be saved as CSV files in the `extracted_tables` directory. Each file will have a name format:
     ```
     {input_file_name}_table_{table_number}_{file_type}_id_{identifier}.csv
     ```

---

## Supported File Types
- **PDF**: Extracts tables from all pages in the file.
- **HTML**: Extracts tables from all `<table>` tags in the file.

---

## Output
- The extracted tables are saved as CSV files.
  - Example output file names:stalled:
    - with_table_inside_table_1_pdf_id_7.csv 
    - example_table_1_html_id_1.csv