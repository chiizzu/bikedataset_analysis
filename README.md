# Bike Dataset Analysis 🚲📊

A hands‑on data–analysis project built for a Dicoding **Data Analytics** submission.  
It explores the classical **[Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset)**, walks through a full EDA pipeline in a Jupyter Notebook, and ships an interactive Streamlit dashboard for quick insights.

---

## Project Goals
1. Perform end‑to‑end exploratory data analysis (EDA) on daily bike‑share ridership.
2. Uncover seasonality, weather impact, and trend patterns.
3. Build an interactive dashboard so stakeholders can slice metrics without touching code.

---

## Quick Start

bash
# 1 . Clone the repo
git clone https://github.com/chiizzu/bikedataset_analysis.git
cd bikedataset_analysis

# 2 . Create & activate a virtual env (pipenv, conda, or venv — your call)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3 . Install requirements
pip install -r requirement.txt      # typo in file‑name preserved from repo 🙂

# 4 . Fire up the notebook (optional)
jupyter notebook Proyek_Analisis_Data.ipynb

# 5 . Launch the Streamlit app
streamlit run bike_stream.py

# Repository Structure
```
├── data/                     # Raw dataset (day.csv, hour.csv)
├── dashboard/
│   └── bike_stream.py        # Streamlit dashboard source
├── Proyek_Analisis_Data.ipynb# Full EDA notebook
├── requirement.txt           # Python dependencies
└── README.md                 # You are here :)
```
# Key Insight
| Theme                  | Highlight                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------- |
| Seasonality            | Ridership peaks in late summer; sharp dips in winter.                                 |
| Weather impact         | Rain and high humidity correlate with \~30 % lower rentals.                           |
| Working‑day effect     | Weekdays show bimodal rush‑hour spikes; weekends trend smoother across the afternoon. |
| Temperature versus use | Optimal rental occurs around 25 °C; extreme cold/heat suppress demand.                |

# Tech Stack
| Layer       | Tools & Libraries                          |
| ----------- | ------------------------------------------ |
| Core Python | `pandas`, `numpy`, `matplotlib`, `seaborn` |
| Dashboard   | `streamlit`, `plotly`                      |
| Environment | Tested on Python 3.11 (should work ≥3.8)   |

