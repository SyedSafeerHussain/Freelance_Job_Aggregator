import pandas as pd
import os
import json

PROCESSED_LINKS_FILE = "processed_links.json"

def load_keywords():
    return [
        "web scraping", "selenium", "python", "automation", "api integration",
        "telegram bot", "email automation", "freelancing bot", "job scraper", "chrome extension"
    ]

def load_seen_links():
    if not os.path.exists(PROCESSED_LINKS_FILE):
        return set()
    with open(PROCESSED_LINKS_FILE, "r") as file:
        return set(json.load(file))

def save_seen_links(seen_links):
    with open(PROCESSED_LINKS_FILE, "w") as file:
        json.dump(list(seen_links), file)

def filter_jobs(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    df = pd.read_csv(input_path)
    if df.empty:
        print(f"⚠️ No jobs found in: {input_path}")
        return

    df['combined'] = df["Job Title"].fillna('') + " " + df["link"].fillna('')
    keywords = load_keywords()
    filtered_df = df[df['combined'].str.lower().apply(
        lambda x: any(keyword in x for keyword in keywords)
    )]
    filtered_df = filtered_df.drop(columns=['combined'])

    # ✅ Remove duplicates based on previously seen job links
    seen_links = load_seen_links()
    new_jobs = filtered_df[~filtered_df["link"].isin(seen_links)]

    if new_jobs.empty:
        print(f"⚠️ No NEW matching jobs found in {input_path}")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    new_jobs.to_csv(output_path, index=False)
    print(f"✅ {len(new_jobs)} relevant NEW jobs saved to {output_path}")

    # ✅ Update seen links
    updated_links = seen_links.union(set(new_jobs["link"]))
    save_seen_links(updated_links)
