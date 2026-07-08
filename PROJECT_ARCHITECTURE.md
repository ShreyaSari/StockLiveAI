                Multiple Data Sources
                         │
                         ▼
                Data Validation Layer
                         │
                         ▼
                Data Preprocessing
                         │
                         ▼
               Feature Engineering
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
     XGBoost       Transformer     Baseline Model
        └────────────────┬────────────────┘
                         ▼
             Dynamic Ensemble Engine
                         ▼
          Buy / Hold / Sell + Confidence
                         ▼
         Reinforcement Learning Agent
                         ▼
      Backtesting & Portfolio Simulator
                         ▼
             Streamlit Dashboard

             NEW

                              Data Pipeline
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
  XGBoost       Transformer      Baseline
        │              │              │
        └──────────────┼──────────────┘
                       ▼
             Dynamic Ensemble Engine
                       ▼
              Confidence Calibration
                       ▼
              Buy / Hold / Sell
                       ▼
                Risk Management





Every folder has one job.

Folder	Responsibility
config	All configurable settings
data	Working datasets
datasets	Dataset import definitions/adapters
database	PostgreSQL integration
preprocessing	Cleaning and validation
feature_engineering	Technical indicators
models	All ML models
trainers	Training logic
predictors	Live inference
evaluators	Metrics and validation
backtesting	Historical simulations
dashboard	Streamlit UI
monitoring	Continuous prediction service
alerts	Notifications (desktop/email/Telegram later)
outputs	Generated predictions and reports
checkpoints	Saved model versions
utils	Shared helper functions
tests	Unit/integration tests