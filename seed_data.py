import datetime
import random
from database import SessionLocal, init_db, ActivityLogModel

def seed_historical_data():
    init_db()
    db = SessionLocal()
    
    # Clear existing data so we don't duplicate
    db.query(ActivityLogModel).delete()
    
    today = datetime.datetime.utcnow()
    
    categories = [
        {"cat": "commute", "sub": "petrol_car", "factor": 0.192, "base_val": 15},
        {"cat": "electricity", "sub": "grid_default", "factor": 0.710, "base_val": 10},
        {"cat": "food", "sub": "heavy_meat", "factor": 3.30, "base_val": 2}
    ]

    print("🌱 Seeding 60 days of historical data...")
    
    for day in range(60, 0, -1):
        log_date = today - datetime.timedelta(days=day)
        
        # Simulate a slight upward trend over time (e.g., user gets careless)
        trend_multiplier = 1.0 + ((60 - day) * 0.005) 
        
        for item in categories:
            # Add some daily randomness
            daily_val = item["base_val"] * trend_multiplier * random.uniform(0.8, 1.2)
            co2e = round(daily_val * item["factor"], 2)
            
            log = ActivityLogModel(
                timestamp=log_date,
                category=item["cat"],
                subcategory=item["sub"],
                value=round(daily_val, 2),
                calculated_co2e=co2e
            )
            db.add(log)
            
    db.commit()
    db.close()
    print("✅ Database successfully seeded with 60 days of data!")

if __name__ == "__main__":
    seed_historical_data()