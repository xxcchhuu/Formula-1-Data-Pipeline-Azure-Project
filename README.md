# 🏎️ Formula 1 Data Pipeline using Microsoft Azure

An end-to-end Data Engineering project that extracts Formula 1 race data from the Jolpica (Ergast) API, stores it in Azure Data Lake Storage Gen2, transforms it using Python, and visualizes insights with Power BI.

---

## 📌 Project Overview

This project demonstrates a modern cloud-based ETL pipeline using Microsoft Azure services.

The pipeline performs the following:

- Extract Formula 1 2023 race results from the Jolpica API
- Store raw JSON data in Azure Data Lake Storage Gen2
- Transform JSON into a structured CSV using Python
- Organize data into Raw, Ingested, and Presentation layers
- Build an interactive Power BI dashboard

---

## 🏗️ Architecture
## Architecture


![Pipeline Architecture](assets/F1%20azure.png)

---

```
             Jolpica Formula 1 API
                     │
                     ▼
          Azure Data Factory (ADF)
                     │
                     ▼
      Azure Data Lake Storage Gen2
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Raw       Ingested     Presentation
                     │
                     ▼
          Python Data Transformation
                     │
                     ▼
               Power BI Dashboard
```

---

## 🛠️ Tech Stack

- Microsoft Azure
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Python
- Pandas
- Requests
- Power BI
- Git
- GitHub

---

## 📂 Project Structure

```
formula1-data-pipeline/
│
├── data/
│   ├── raw/
│   │   └── f1_results.json
│   ├── ingested/
│   │   └── race_results.csv
│   └── presentation/
│
├── src/
│   ├── extract.py
│   └── transform.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dashboard Features

The Power BI dashboard includes:

- Season Overview
- Total Races
- Total Drivers
- Total Constructors
- Top Driver
- Top Team
- Driver Standings
- Constructor Standings
- Race Winners
- Average Points per Driver
- Interactive Filters

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Formula-1-Data-Pipeline-Azure-Project.git
```

Move into the project

```bash
cd Formula-1-Data-Pipeline-Azure-Project
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Extract Formula 1 data

```bash
python src/extract.py
```

Transform the data

```bash
python src/transform.py
```

---

## 📈 Sample Output

```
Race                  Driver             Constructor      Position  Points
Bahrain Grand Prix    Max Verstappen     Red Bull         1         25
Bahrain Grand Prix    Sergio Pérez       Red Bull         2         18
Bahrain Grand Prix    Fernando Alonso    Aston Martin     3         15
```

- 22 races
- 440 race records
- 20 drivers
- 10 constructors

---

## 📷 Dashboard Preview

> Add screenshots of your Power BI dashboard here.

Example:

```
images/dashboard.png
```

---

## 🔮 Future Improvements

- Azure Databricks integration
- Delta Lake implementation
- Incremental data loading
- Azure Synapse Analytics
- Azure Key Vault
- CI/CD with GitHub Actions

---

## 📚 Data Source

Jolpica Formula 1 API

https://api.jolpi.ca/ergast/f1/2023/results.json

---

## 👨‍💻 Author

**Ashwin CV**

- GitHub: https://github.com/xxcchhuu
- LinkedIn: https://www.linkedin.com/in/ashwin-cv-b305883b1/

---

## ⭐ If you found this project useful, consider giving it a star.