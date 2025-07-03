import pandas as pd
import os
def load_keywords():
    return["web scraping", "selenium", "python", "automation", "api integration",
        "telegram bot", "email automation", "freelancing bot", "job scraper", "chrome extension"]
def filter_jobs(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return
    df=pd.read_csv(input_path)
    if df.empty:
        print(f"⚠️ No jobs found in: {input_path}")
        return
    df['combined']=df["Job Title"].fillna('')+" "+df["link"].fillna('')
    keywords=load_keywords()
    filtered_df=df[df['combined'].str.lower().apply(
        lambda x: any(keyword in x for keyword in keywords)
    )]
    filtered_df=filtered_df.drop(columns=['combined'])
    if filtered_df.empty:
        print(f"⚠️ No matching jobs found in {input_path}")
    else:
        os.makedirs(os.path.dirname(output_path),exist_ok=True)
        filtered_df.to_csv(output_path,index=False)
        print(f"✅ {len(filtered_df)} relevant jobs saved to {output_path}")