from twilio.rest import Client
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # 👈 Load from .env

# Twilio credentials
accound_sid=os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client=Client(accound_sid,auth_token)

# Load filtered jobs
df=pd.read_csv('data/filtered_guru_jobs.csv')
# Loop through each job
for index,row in df.iterrows():
    title=row['Job Title']
    desc=row['Job Description']
    price=row['price']
    link=row['link']
    msg = f"📢 New Job Alert!\n\n🔹 *{title}*\n💰 {price}\n🔗 {link}\n📝 {desc[:150]}..."

    message=client.messages.create(
        
        from_number = os.getenv("FROM_WHATSAPP"),
        to=os.getenv("TO_WHATSAPP"),
        body=msg
)

# Send WhatsApp message


print(f"✅ Sent: {title}")
