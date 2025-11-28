import requests
from pathlib import Path


def vergabe_basic_scraper(params=None):
    print('params',params['pubDay'])
    if params is None:
        raise ValueError("params must be provided")
    url = "https://oeffentlichevergabe.de/api/notice-exports"
    headers = {
        "Accept": "application/vnd.bekanntmachungsservice.csv.zip+zip",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    print("Requested URL:", response.url)
    print("Status code:", response.status_code)
    response.raise_for_status()
    Path("data").mkdir(parents=True, exist_ok=True)

    with open("data/notices_"+str(params['pubDay'])+"_csv.zip", "wb") as f:
        f.write(response.content)

    print("✅ ZIP file downloaded successfully.")