import pdfplumber
import pandas as pd
import os
from bs4 import BeautifulSoup
import io


def extract_tables_with_pdfplumber(file_path):
    """
    Extract tables from a PDF using pdfplumber.
    """
    tables = []
    try:
        print(f"Extracting tables from {file_path} using pdfplumber...")
        with pdfplumber.open(file_path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                extracted_tables = page.extract_tables()
                for table in extracted_tables:
                    if table:
                        cleaned_table = [[cell if cell else "" for cell in row] for row in table]
                        tables.append((page_number, cleaned_table))
        return tables
    except Exception as e:
        print(f"Error extracting tables with pdfplumber: {e}")
        return []


def extract_tables_from_html(file_path):
    """
    Extract tables from an HTML file.
    """
    tables = []
    try:
        print(f"Extracting tables from {file_path} using BeautifulSoup...")
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            all_tables = soup.find_all("table")

            for idx, table in enumerate(all_tables, start=1):
                table_html = io.StringIO(str(table))
                df = pd.read_html(table_html)[0]
                tables.append((idx, df.values.tolist()))  # Добавляем номер таблицы и данные
        return tables
    except Exception as e:
        print(f"Error extracting tables from HTML: {e}")
        return []


def save_tables(tables, output_dir, file_name, file_type):
    """
    Save extracted tables to CSV files.
    """
    os.makedirs(output_dir, exist_ok=True)
    saved_files = []
    for idx, (identifier, table) in enumerate(tables):
        output_file = os.path.join(output_dir, f"{file_name}_table_{idx + 1}_{file_type}_id_{identifier}.csv")
        try:
            df = pd.DataFrame(table)
            df.to_csv(output_file, index=False, header=False)
            saved_files.append(output_file)
        except Exception as e:
            print(f"Error saving table {idx + 1}: {e}")
    return saved_files


def process_file(file_path, output_dir):
    """
    Process a file to extract tables based on its type (PDF or HTML).
    """
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    if file_path.endswith(".pdf"):
        print(f"Processing PDF file: {file_path}")
        tables = extract_tables_with_pdfplumber(file_path)
        file_type = "pdf"
    elif file_path.endswith(".html"):
        print(f"Processing HTML file: {file_path}")
        tables = extract_tables_from_html(file_path)
        file_type = "html"
    else:
        print(f"Unsupported file format: {file_path}")
        return

    if tables:
        print(f"Found {len(tables)} table(s) in {file_path}")
        saved_files = save_tables(tables, output_dir, file_name, file_type)
        print(f"Tables saved to: {saved_files}")
    else:
        print(f"No tables found in {file_path}")


def main():
    """
    Main function to process all files in the input_files directory.
    """
    input_dir = "input_files"
    output_dir = "extracted_tables"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Supported file extensions
    supported_extensions = {".pdf", ".html"}

    # Iterate over all files in the input directory
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        file_extension = os.path.splitext(file_name)[1].lower()
        if os.path.isfile(file_path) and file_extension in supported_extensions:
            try:
                process_file(file_path, output_dir)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    main()