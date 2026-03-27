# 📊 Codveda Internship — Basic Level Project  
### 🚀 End-to-End Data Pipeline (Web Scraping → Data Engineering → Dashboard)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-red)

---

## 📌 Overview  

This project is part of my **Data Science Internship at Codveda Technology**, focused on building a **complete data pipeline** from raw web data to actionable insights.

The dataset was scraped from <b>Books to Scrape</b>, a structured e-commerce website commonly used for practicing real-world data extraction.

---

## 🔄 Project Workflow  

```
Web Scraping → Raw Dataset → Data Cleaning → Feature Engineering → Dashboard Visualization
```

---

## 🎯 Objectives  

- Extract structured data from a live website  
- Clean and preprocess raw data  
- Engineer meaningful features for analysis  
- Build a dashboard for insight communication  

---

## 📂 Project Structure  

```
Codveda_Tech_Basic_Lev_Project/
│
├── scrapper.py                    # Web scraping script
├── Data_Processing_clean.ipynb    # Data cleaning & feature engineering
├── raw_dataset.csv                # Original scraped data
├── cleaned_dataset.csv            # Final processed dataset
│
└── README.md                      # Documentation
```

---

## 🛠️ Tech Stack  

### 📊 Data Processing  
- Python (Pandas, NumPy)  

### 🌐 Data Collection  
- Web Scraping (Requests, BeautifulSoup)  

### 📈 Visualization  
- Streamlit  
- Plotly  

### 💻 Tools  
- Jupyter Notebook  
- VS Code  
- Git & GitHub  

---

## 🔍 Key Components  

### 1️⃣ Web Scraping (`scrapper.py`)  
- Extracted book data including:
  - Title  
  - Price  
  - Rating  
  - Availability  
- Generated a structured raw dataset for analysis  

---

### 2️⃣ Data Cleaning & Feature Engineering  
(`Data_Processing_clean.ipynb`)  

This stage focused on transforming raw data into **analysis-ready and insight-driven features**:

#### ✅ Data Cleaning  
- Handled missing values  
- Removed inconsistencies  
- Standardized formats  

#### 🔄 Feature Engineering  

- **Rating Conversion**  
  - Converted textual ratings (`One`, `Two`, ..., `Five`) → numeric scale (1–5)  

- **Rating Grouping**  
  - Created `rating_group` column:
    - `Low`  
    - `Medium`  
    - `High`  

- **Price Categorization**  
  - Created `price_category`:
    - `Very Low`  
    - `Low`  
    - `Medium`  

- **Currency Localization (₦ Naira Conversion)**  
  - Added new column converting prices to **Nigerian Naira (₦)**  
  - Enables **localized analysis and better storytelling for Nigerian stakeholders**  

---

### 3️⃣ Datasets  

| Dataset | Description |
|--------|------------|
| `raw_dataset.csv` | Original scraped dataset |
| `cleaned_dataset.csv` | Processed dataset with engineered features |

---

## 📊 Interactive Dashboard  

The cleaned dataset was used to build a fully interactive dashboard for insights exploration.

### 🌐 Live App  
👉 https://appapplicationdashboard-yocyhlm8tvawis4f3rton4.streamlit.app/

### 💻 Dashboard Repository  
👉 https://github.com/HamzyinTech/Streamlit_Application_Dashboard  

---

## 📈 Dashboard Features  

- Dynamic filtering by price and rating  
- Visual breakdown of book distribution  
- Insightful charts for decision-making  
- Clean and user-friendly UI  

---

## 📊 Key Insights  

- Higher-rated books tend to cluster within specific price ranges  
- Categorization improved interpretability of pricing patterns  
- Currency conversion enhanced **local business relevance**  
- Feature engineering significantly improved analytical clarity  

---

## 📈 Results  

| Stage              | Outcome |
|-------------------|--------|
| Data Collection   | Automated via scraping |
| Data Quality      | Cleaned and structured |
| Feature Engineering | Enhanced for analysis |
| Visualization     | Interactive dashboard deployed |
| Accessibility     | Publicly available |

---

## 💡 Business Value  

- Bridges gap between raw data and decision-making  
- Enables localized insights using ₦ currency  
- Demonstrates ability to design **real-world data workflows**  

---

## 🧩 Challenges & Solutions  

| Challenge | Solution |
|----------|---------|
| Text-based ratings | Converted to numeric scale |
| Unstructured pricing | Categorized into meaningful groups |
| Foreign currency | Converted to ₦ for local relevance |
| Raw data noise | Cleaned and standardized dataset |

---

## 🚀 How to Run  

```bash
# Clone repository
git clone https://github.com/HamzyinTech/Codvede_Technology_Intern_Project.git

# Navigate to project folder
cd Codvede_Technology_Intern_Project/Codveda_Tech_Basic_Lev_Project

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook

# Run scraper
python scrapper.py
```

---

## 🏆 Key Takeaways  

✔ Built a complete end-to-end data pipeline  
✔ Applied real-world feature engineering techniques  
✔ Improved storytelling using localized currency  
✔ Delivered insights via an interactive dashboard  

---

## 🔗 Related Projects  

- 📊 Streamlit Dashboard:  
  https://github.com/HamzyinTech/Streamlit_Application_Dashboard  

---

## 👨‍💻 Author  

**Oyegoke Hamad**  
- Data Analyst | Data Scientist  
- Passionate about transforming data into actionable insights  

---

## ⭐ Support  

If you found this project useful:

- ⭐ Star the repository  
- 🍴 Fork it  
- 📢 Share with others  

---
