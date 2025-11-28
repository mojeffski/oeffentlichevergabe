from datetime import date, timedelta
from pathlib import Path
from utils.scraper import vergabe_basic_scraper
from utils.processing import unzip_notice_zip, csvs_to_xlsx, merge_csvs_on_notice_id, delete_zip_file

# Get yesterday’s date
yesterday = date.today() - timedelta(days=1)
print(f"Running for: {yesterday}")

# Run scraper to download ZIP
vergabe_basic_scraper({"pubDay": yesterday})



# Paths
zip_filename = f"notices_{yesterday.strftime('%Y-%m-%d')}_csv.zip"
zip_path = Path("data") / zip_filename
extract_to = Path("data/unzipped") / f"notices_{yesterday.isoformat()}"
xlsx_path = Path("data") / f"notices_{yesterday.isoformat()}.xlsx"

# Unzip
extracted_files = unzip_notice_zip(zip_path, extract_to)

# Convert to XLSX
csvs_to_xlsx(extract_to, xlsx_path)

# Merge by the id variable noticeIdentifier (not yet working)
#merge_csvs_on_notice_id(extract_to, xlsx_path)

delete_zip_file(zip_path)

print("🎉 All steps completed.")