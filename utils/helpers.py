# utils/helpers.py
import csv
import os

def save_to_csv(data, filename):
    folder = "data"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)

    if not data:
        print(f"[INFO] No data to save in {filename}")
        return

    keys = data[0].keys()
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"[✓] Saved {len(data)} records to {filepath}")
