from flask import Flask ,render_template
import pandas as pd
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

app=Flask(__name__)
@app.route("/")
def home():
    data_folder = DATA_DIR
    jobs=[]
    for file in os.listdir(data_folder):
        if file.startswith("filtered_") and file.endswith(".csv"):
            df=pd.read_csv(os.path.join(data_folder,file))
            source=file.replace("filtered_","").replace(".csv","").capitalize()
            for _, row in df.iterrows():
                jobs.append({
                    "title":row.get("Job Title","N/A"),
                    "desc":row.get("Job Description","N/A"),
                    "link":row.get("link","#"),
                    "price":row.get("price","N/A"),
                    "source":source
                })
    return render_template("index.html",jobs=jobs)

if __name__ == "__main__":
    print("🚀 Flask app is running...")
    app.run(debug=True)
