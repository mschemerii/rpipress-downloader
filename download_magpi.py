#!/Users/mschemer/my-repos/rpipress-downloader/.venv/bin/python

import os
import requests
from tqdm import tqdm
import time

# Folder to store PDF files
save_dir = "MagPi_Issues"
os.makedirs(save_dir, exist_ok=True)

# Total number of issues to download
total_issues = 153

# Start download loop
for issue_number in tqdm(range(1, total_issues + 1), desc="Downloading MagPi PDFs"):
    url = f"https://magazine.raspberrypi.com/issues/{issue_number}/pdf/download"
    filename = os.path.join(save_dir, f"MagPi_Issue_{issue_number}.pdf")

    # Skip if file already exists
    if os.path.exists(filename):
        tqdm.write(f"[Issue {issue_number}] Already exists. Skipping.")
        continue

    # Retry logic
    for attempt in range(3):
        try:
            response = requests.get(url, allow_redirects=True, timeout=10)
            response.raise_for_status()
            with open(filename, "wb") as f:
                f.write(response.content)
            tqdm.write(f"[Issue {issue_number}] Downloaded successfully.")
            break  # Exit retry loop on success
        except requests.HTTPError as http_err:
            tqdm.write(f"[Issue {issue_number}] HTTP error: {http_err}")
        except Exception as e:
            tqdm.write(f"[Issue {issue_number}] Attempt {attempt + 1}/3 failed: {e}")
        time.sleep(1)  # Brief delay before retry
    else:
        tqdm.write(f"[Issue {issue_number}] ❌ Failed after 3 attempts.")

