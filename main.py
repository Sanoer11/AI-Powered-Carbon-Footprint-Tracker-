import json
import datetime
from pathlib import Path
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Import database configuration
from database import init_db, SessionLocal, ActivityLogModel

app = FastAPI(title="Green Tech Footprint API")

# Add CORS middleware to allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "emission_factors.json"
EMISSION_FACTORS = {}

# Dependency to safely handle database session lifecycle per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    # 1. Initialize relational database tables
    init_db()
    
    # 2. Load emission parameters into system memory
    global EMISSION_FACTORS
    try:
        with open(DATA_FILE, "r") as file:
            EMISSION_FACTORS = json.load(file)
        print("✅ System initialized: SQLite tables created and emission factors cached.")
    except FileNotFoundError:
        print("❌ System initialization failed: emission_factors.json missing.")

class ActivityLog(BaseModel):
    category: str
    subcategory: str
    value: float

@app.post("/log-activity")
async def log_activity(activity: ActivityLog, db: Session = Depends(get_db)):
    # Validate category and subcategory against configuration cache
    if activity.category not in EMISSION_FACTORS:
        raise HTTPException(status_code=400, detail=f"Invalid category: {activity.category}")
    
    category_data = EMISSION_FACTORS[activity.category]
    if activity.subcategory not in category_data:
        raise HTTPException(status_code=400, detail=f"Invalid subcategory: {activity.subcategory}")

    # Compute carbon factor logic
    factor = category_data[activity.subcategory]["factor"]
    total_co2e = round(activity.value * factor, 2)

    # 3. Create database record instance
    new_log = ActivityLogModel(
        category=activity.category,
        subcategory=activity.subcategory,
        value=activity.value,
        calculated_co2e=total_co2e
    )
    
    # 4. Save to SQLite database
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return {
        "status": "success",
        "record_id": new_log.id,
        "timestamp": new_log.timestamp,
        "calculated_co2e": new_log.calculated_co2e
    }

@app.get("/config")
async def get_config():
    return EMISSION_FACTORS

@app.get("/predictive-trends")
async def get_predictive_trends(db: Session = Depends(get_db)):
    """
    Fetches historical data, trains a Linear Regression model, 
    predicts the next 30 days, and flags the worst habit.
    """
    # 1. Fetch all data from the database
    logs = db.query(ActivityLogModel).all()
    if not logs:
        raise HTTPException(status_code=400, detail="Not enough data to run ML model.")

    # 2. Convert to Pandas DataFrame for easy manipulation
    df = pd.DataFrame([{
        "date": log.timestamp.date(),
        "category": log.category,
        "co2e": log.calculated_co2e
    } for log in logs])

    # Convert the date column to actual pandas datetime objects to prevent the .dt crash
    df['date'] = pd.to_datetime(df['date'])

    # 3. Group by date to get Total Daily Emissions
    daily_totals = df.groupby('date')['co2e'].sum().reset_index()
    daily_totals['days_since_start'] = (daily_totals['date'] - daily_totals['date'].min()).dt.days

    # 4. Train the Linear Regression Model
    X = daily_totals[['days_since_start']].values
    y = daily_totals['co2e'].values
    
    model = LinearRegression()
    model.fit(X, y)

    # 5. Predict the next 30 days
    last_day = daily_totals['days_since_start'].max()
    future_X = np.array([[last_day + i] for i in range(1, 31)])
    predictions = model.predict(future_X)
    
    # Format predictions for the frontend chart (converting pandas timestamps back to JSON-friendly strings)
    future_dates = [daily_totals['date'].max() + datetime.timedelta(days=i) for i in range(1, 31)]
    forecast = [{"date": date.strftime('%Y-%m-%d'), "predicted_co2e": round(float(pred), 2)} for date, pred in zip(future_dates, predictions)]

    # 6. Feature Importance: Find the category driving the highest emissions recently
    last_7_days = df[df['date'] >= (df['date'].max() - datetime.timedelta(days=7))]
    if last_7_days.empty:
         worst_category = df.groupby('category')['co2e'].sum().idxmax()
    else:
         worst_category = last_7_days.groupby('category')['co2e'].sum().idxmax()
         
    percentage_increase = round((predictions[-1] - y[-1]) / y[-1] * 100, 1)

    return {
        "status": "success",
        "historical_data_points": len(daily_totals),
        "insight_alert": f"Warning: Your emissions are projected to change by {percentage_increase}% next month. Your '{worst_category}' habits are the primary driver.",
        "forecast": forecast
    }