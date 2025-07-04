**Freelance Job Aggregator Bot**

A complete, modular Python-based system to scrape, filter, and notify freelance job listings from multiple platforms via WhatsApp.

---

## 🌟 Features

* **Multi-Platform Scraping**: Automates job data extraction from PeoplePerHour, Guru.com, and RemoteOK using Selenium & BeautifulSoup.
* **Modular Architecture**: Clean separation of scrapers, utilities, and main controller for easy maintenance and scalability.
* **Robust Data Saving**: Saves raw and filtered job listings as structured CSV files.
* **Keyword Filtering**: Leverages Pandas to filter jobs by customizable keyword list.
* **WhatsApp Notifications**: Sends real-time job alerts via Twilio WhatsApp Sandbox.
* **Environment Security**: Credentials managed securely via `.env` file.

---

## 🛠️ Tech Stack

* **Python 3.8+**
* **Selenium** for browser automation
* **BeautifulSoup** for HTML parsing
* **Pandas** for data manipulation
* **Twilio** for WhatsApp notifications
* **python-dotenv** for environment variable management

---

## 🚀 Prerequisites

* Python 3.8 or higher
* [Chromedriver](https://chromedriver.chromium.org/) (compatible with your Chrome version)
* Twilio account with WhatsApp Sandbox enabled

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/freelance_job_aggregator.git
   cd freelance_job_aggregator
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\\Scripts\\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔒 Configuration

1. **Create a `.env` file** in project root:

   ```env
   ACCOUNT_SID=your_twilio_account_sid
   AUTH_TOKEN=your_twilio_auth_token
   FROM_WHATSAPP=whatsapp:+14155238886    # Twilio sandbox number
   TO_WHATSAPP=whatsapp:+92XXXXXXXXXX    # Your WhatsApp number
   ```

2. **Ensure `.env` is listed in `.gitignore`** to keep credentials secure.

---

## 📂 Folder Structure

```
freelance_job_aggregator/
├── scrapers/                  # Platform-specific scraper modules
│   ├── pph_scraper.py
│   ├── guru_scraper.py
│   └── remoteok_scraper.py
│
├── utils/                     # Utility modules
│   ├── helpers.py             # CSV saving helper
│   └── keyword_filter.py      # Pandas-based filtering
│
├── data/                      # Raw and filtered CSV outputs
│   ├── pph_jobs.csv
│   ├── guru_jobs.csv
│   ├── remoteok_jobs.csv
│   ├── filtered_pph_jobs.csv
│   ├── filtered_guru_jobs.csv
│   └── filtered_remoteok_jobs.csv
│
├── config/                    # Configuration files (keywords, settings)
│   └── keywords.txt
│
├── main.py                    # Master controller: scrape, filter, notify
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and documentation
```

---

## 🎯 Usage

1. **Run scrapers and filter**

   ```bash
   python main.py
   ```

   * Executes all scrapers
   * Filters jobs based on keywords
   * Saves data in `data/` directory

2. **WhatsApp Notifications**

   * Messages sent automatically for each filtered job.

3. **Customize keywords**

   * Edit `config/keywords.txt` or update `utils/keyword_filter.py` load function.

---

## 🤝 Contributing

1. Fork this repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add YourFeature"`).
4. Push to branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure all new code includes comments and follows PEP8 guidelines.

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
