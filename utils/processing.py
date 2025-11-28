from pathlib import Path
from typing import List
import zipfile
import pandas as pd

def unzip_notice_zip(zip_path: Path, extract_to: Path) -> List[Path]:
    """Unzips the CSV archive and returns list of extracted file paths."""
    extract_to.mkdir(parents=True, exist_ok=True)
    extracted_files = []

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        extracted_files = [extract_to / member for member in zip_ref.namelist() if member.endswith('.csv')]

    return extracted_files


def csvs_to_xlsx(csv_folder: Path, xlsx_path: Path) -> None:
    """Reads all CSVs and writes them as separate sheets in one XLSX file."""
    from pandas import ExcelWriter

    with ExcelWriter(xlsx_path, engine='openpyxl') as writer:
        for csv_file in sorted(csv_folder.glob("*.csv")):
            sheet_name = csv_file.stem[:31]  # Excel max sheet name = 31 chars
            df = pd.read_csv(csv_file, low_memory=False)
            df.to_excel(writer, sheet_name=sheet_name, index=False)


def merge_csvs_on_notice_id(csv_folder: Path, xlsx_path: Path) -> None:
    """Reads all CSVs, merges them on 'noticeIdentifier', and writes to a new sheet in the XLSX."""
    print('merge_csvs_on_notice_id','TEST:::')
    dfs = []
    for csv_file in sorted(csv_folder.glob("*.csv")):
        try:
            df = pd.read_csv(csv_file, low_memory=False)
            if 'noticeIdentifier' in df.columns:
                df_reduced = df.set_index('noticeIdentifier')
                dfs.append(df_reduced)
        except Exception as e:
            print(f"⚠️ Could not read {csv_file.name}: {e}")

    if not dfs:
        print("No files with 'noticeIdentifier' found.")
        return

    merged_df = dfs[0]
    for df in dfs[1:]:
        merged_df = merged_df.join(df, how='outer', rsuffix='_dup')

    # Reset index to include noticeIdentifier as a column again
    merged_df.reset_index(inplace=True)

    # Append to existing XLSX
    with pd.ExcelWriter(xlsx_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        merged_df.to_excel(writer, sheet_name='merged_by_noticeIdentifier', index=False)
        
def delete_zip_file(zip_path: Path) -> None:
    """Deletes the ZIP file if it exists."""
    try:
        if zip_path.exists():
            zip_path.unlink()
            print(f"🗑️ Deleted ZIP file: {zip_path}")
        else:
            print(f"⚠️ ZIP file not found: {zip_path}")
    except Exception as e:
        print(f"❌ Could not delete ZIP file: {e}")