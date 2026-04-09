# Data_Engineering_project

🛒 BigMart Sales Forecasting Pipeline
This project showcases a complete Data Engineering + Machine Learning pipeline using BigMart retail sales data. It includes automated data ingestion, MySQL database setup, model training, and deployment via a Streamlit app.


                ┌──────────────────────────┐
                │     BigMart Dataset      │
                │  (CSV / Database Source) │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │   Data Preprocessing     │
                │--------------------------│
                │ • Missing Value Handling │
                │ • Feature Engineering    │
                │ • Encoding (OneHot)      │
                │ • Scaling (if applied)   │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │   Train/Test Split       │
                └────────────┬─────────────┘
                             │
                             ▼
    ┌───────────────────────────────────────────────┐
    │           Model Training Layer                │
    │-----------------------------------------------│
    │ • Linear Regression                           │
    │ • Random Forest Regressor                     │
    │ • Gradient Boosting Regressor (Selected)      │
    └────────────┬──────────────────────────────────┘
                 │
                 ▼
    ┌───────────────────────────────────────────────┐
    │         Model Evaluation Layer                │
    │-----------------------------------------------│
    │ • R² Score                                   │
    │ • RMSE                                       │
    │ • Model Selection                            │
    └────────────┬──────────────────────────────────┘
                 │
                 ▼
    ┌───────────────────────────────────────────────┐
    │        Model Serialization                    │
    │-----------------------------------------------│
    │  bigmart_best_model.pkl                       │
    └────────────┬──────────────────────────────────┘
                 │
                 ▼
    ┌───────────────────────────────────────────────┐
    │          Streamlit Application                │
    │-----------------------------------------------│
    │ • User Input Form                             │
    │ • DataFrame Conversion                        │
    │ • Model Prediction                            │
    │ • Result Display                              │
    └────────────┬──────────────────────────────────┘
                 │
                 ▼
    ┌───────────────────────────────────────────────┐
    │            End User (Browser)                 │
    │-----------------------------------------------│
    │  Input Data → Get Sales Prediction            │
    └───────────────────────────────────────────────┘
