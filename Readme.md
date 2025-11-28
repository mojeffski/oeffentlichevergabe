# Öffentliche Vergabe Scraper

This project downloads and processes daily procurement notice exports from [öffentlichevergabe.de](https://oeffentlichevergabe.de).

It performs the following steps:
1. 🗂️ Downloads a ZIP file containing multiple CSV files for a given `pubDay`.
2. 📂 Unzips the archive and extracts the CSVs.
3. 📊 Converts each CSV into a separate Excel sheet.
4. 🔗 Merges all CSVs on the `noticeIdentifier` column into a combined sheet.

---

## 📁 Project Structure
```
├── main.py                  # Main runner script
├── utils/
│   ├── scraper.py           # Handles data download from API
│   ├── processing.py        # Handles unzip, Excel conversion, and merging
│   └── init.py
├── data/                    # Stores ZIPs, extracted CSVs, and XLSX output
├── .gitignore
├── requirements.txt
└── venv/                    # Virtual environment (excluded from git)
```

---

## 🚀 How to Run

1. **Set up virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run script:**
```bash
    python3 -m main
```
 
## Info;
By default, the script runs for **yesterday’s date**.  
The output ZIP, extracted CSVs, and final Excel file will be saved in the `data/` directory.

---

## 🧾 Output

- `data/notices_YYYY-MM-DD_csv.zip`
- `data/unzipped/notices_YYYY-MM-DD/*.csv`
- `data/notices_YYYY-MM-DD.xlsx` (with merged and individual sheets)

---

## 🛠️ Dependencies

- `requests`
- `pandas`
- `openpyxl`
- `python-dateutil` *(optional if used)*

See `requirements.txt` for full details.

---

## 📄 License

MIT License — feel free to adapt or reuse.