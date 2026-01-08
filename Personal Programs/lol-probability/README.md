# League of Legends Match Win Porobability

    Program designed use machine learning to predict future LOL matches.

## Phase 1: Define the Scope

    Match Winner: The simplest starting point.
    First Blood: A more volatile event.
    Game Duration: A regression problem.

## Phase 2: Acquire and Prepare Data

    Use Python libraries: requests to fetch data from APIs, and pandas for data manipulation.
    Key Data Points (Features): Gather these stats for both teams involved in a match:
    Overall Win Rate (across the season)
    Win rate on the current patch
    Average Gold Difference at 15 minutes (GD@15)
    First Tower/Dragon/Baron control rate
    Champion win rates of the selected champions in the draft

## Phase 3: Build the Predictive Model

    This is where the machine learning comes in. The go-to tool is the scikit-learn library.
    Recommended Algorithm: Logistic Regression or XGBoost. XGBoost often performs better with this type of structured, tabular data.

## File Structure

    lol-win-predictor/
    │
    ├── data/
    │   ├── raw/
    │   └── processed/
    │
    ├── src/
    │   ├── config.py
    │   ├── main.py
    │
    │   ├── data_collection/
    │   │   ├── fetch_matches.py
    │   │   └── fetch_stats.py
    │
    │   ├── data_processing/
    │   │   ├── clean_data.py
    │   │   └── feature_engineering.py
    │
    │   ├── models/
    │   ├───└── xgboost_model.py
    │
    │   └── utils/
    │       ├── api_helpers.py
    │       └── logger.py
    │
    ├── notebooks/
    │   └── eda.ipynb
    │
    ├── requirements.txt
    └── README.md
