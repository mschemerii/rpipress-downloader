#!/Users/mschemer/my-repos/rpipress-downloader/.venv/bin/python

import os
import requests
from tqdm import tqdm
import time

# Folder to store PDF files
save_dir = "MagPi_Issues"
os.makedirs(save_dir, exist_ok=True)

# Start from issue 1
issue_number = 1
max_consecutive_failures = 2
failure_streak = 0

# Infinite loop until two consecutive failures
while True:
    url = f"https://magazine.raspberrypi.com/issues/{issue_number}/pdf/download"
    filename = os.path.join(save_dir, f"MagPi_Issue_{issue_number}.pdf")

    # Skip if already exists
    if os.path.exists(filename):
        tqdm.write(f"[Issue {issue_number}] Already exists. Skipping.")
        issue_number += 1
        failure_streak = 0
        continue

    # Try downloading with 3 retries
    success = False
    for attempt in range(3):
        try:
            response = requests.get(url, allow_redirects=True, timeout=10)
            response.raise_for_status()
            with open(filename, "wb") as f:
                f.write(response.content)
            tqdm.write(f"[Issue {issue_number}] Downloaded successfully.")
            success = True
            break
        except Exception as e:
            tqdm.write(f"[Issue {issue_number}] Attempt {attempt + 1}/3 failed: {e}")
            time.sleep(1)

    if success:
        failure_streak = 0
    else:
        tqdm.write(f"[Issue {issue_number}] ❌ Failed after 3 attempts.")
        failure_streak += 1
        if failure_streak >= max_consecutive_failures:
            tqdm.write(f"\n🛑 Stopping: {failure_streak} consecutive issues not found. Assuming end of list.")
            break

    issue_number += 1

