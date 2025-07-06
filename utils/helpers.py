# utils/helpers.py
import csv
import os
# utils/helpers.py ya main.py ke andar
def load_keywords(file_path='config/keywords.txt'):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

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
