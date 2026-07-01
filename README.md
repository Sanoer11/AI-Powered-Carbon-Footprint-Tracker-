# AI-Powered Carbon Footprint Analytics

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## 📌 Overview

** A full-stack AI-powered Carbon Footprint Analytics platform that helps users monitor, analyze, and predict their environmental impact. The application records daily activities including transportation, electricity usage, and dietary habits, converts them into CO₂ emissions, and uses Machine Learning to forecast future emission trends while providing intelligent sustainability insights.

The project combines **React**, **FastAPI**, **SQLite**, and **Scikit-Learn** to build a modern data-driven GreenTech application.

---

# 🚀 Features

### 🌍 Carbon Footprint Tracking
- Log transportation, electricity consumption, and food habits.
- Automatically converts activities into CO₂ equivalent (CO₂e).
- Stores historical environmental data in SQLite.

### 🤖 Machine Learning Prediction
- Uses **Scikit-Learn Linear Regression** to forecast the next **30 days** of carbon emissions.
- Generates trendlines from historical activity data.
- Continuously retrains on updated user data.

### 💡 AI Sustainability Insights
- Identifies which lifestyle category contributes most to increasing emissions.
- Generates actionable recommendations for reducing carbon footprint.
- Performs automated feature importance analysis.

### 📊 Interactive Dashboard
- Responsive React dashboard.
- Dynamic KPI cards.
- Interactive emission trend charts using Recharts.
- Real-time visualization of historical and predicted emissions.

### ⚡ FastAPI Backend
- RESTful API architecture.
- Input validation using Pydantic.
- High-performance asynchronous API endpoints.
- Automatic Swagger API documentation.

### 🗄 Database Layer
- SQLite database with SQLAlchemy ORM.
- Secure CRUD operations.
- Historical time-series storage for ML training.

---

# 🏗 System Architecture

```
                    React Frontend
                          │
                          │ REST API
                          ▼
                 FastAPI Backend Server
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
 SQLite Database                    ML Prediction Engine
(SQLAlchemy ORM)             (Pandas + Scikit-Learn)
        │                                   │
        └──────────────► Insights ◄─────────┘
                          │
                          ▼
                Interactive Dashboard
```

---

# 💻 Tech Stack

## Frontend

- React.js
- Tailwind CSS
- Recharts
- Lucide React

## Backend

- Python 3
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic

## Machine Learning

- Pandas
- NumPy
- Scikit-Learn (Linear Regression)

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|----------|-------------------------|--------------------------------------------|
| GET | `/config` | Returns environmental emission factors |
| POST | `/log-activity` | Logs user activity and calculates CO₂ emissions |
| GET | `/predictive-trends` | Predicts future emissions using ML |

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📂 Project Structure

```
CARBON TRACKER/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── data/
│
├── main.py
├── database.py
├── seed_data.py
├── carbon_tracker.db
├── README.md
└── requirements.txt
```

---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Sanoer11/AI-Powered-Carbon-Footprint-Tracker.git

cd AI-Powered-Carbon-Footprint-Tracker
```

---

## 2️⃣ Install Backend Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pandas
pip install numpy
pip install scikit-learn
pip install pydantic
```

Or

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Seed Database

```bash
python seed_data.py
```

This generates sample historical emission data for model training.

---

## 4️⃣ Start Backend Server

```bash
uvicorn main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 5️⃣ Run Frontend

```bash
cd frontend

npm install

npm start
```

React App:

```
http://localhost:3000
```

---

# 📈 Machine Learning Workflow

```
Historical Activity Data
            │
            ▼
 Data Cleaning (Pandas)
            │
            ▼
 Feature Engineering
            │
            ▼
 Linear Regression Model
            │
            ▼
30-Day CO₂ Prediction
            │
            ▼
 AI Insights Generation
            │
            ▼
 React Dashboard
```

---

# 📊 Sample Workflow

1. User logs daily activities.
2. FastAPI validates incoming data.
3. CO₂ emissions are calculated.
4. Data is stored in SQLite.
5. Historical records are processed using Pandas.
6. Linear Regression predicts future emissions.
7. AI identifies the highest contributing emission category.
8. Dashboard displays predictions and recommendations.

---

# 🎯 Future Improvements

- Docker Containerization
- AWS Cloud Deployment
- JWT Authentication
- Multi-user Support
- User Login & Registration
- Carbon Offset Recommendation System
- Deep Learning-based Emission Forecasting
- Real-time Weather & Energy API Integration
- CSV/PDF Report Export
- Personalized Sustainability Goals

---

# 🛠 Skills Demonstrated

- Full Stack Development
- Machine Learning
- REST API Development
- Database Design
- Data Analytics
- Green Technology
- Predictive Analytics
- Data Visualization
- Software Architecture
- SQLAlchemy ORM
- FastAPI
- React.js
- Python
- SQLite
- Scikit-Learn

---

# 📸 Application Highlights

- 📈 Predictive Carbon Emission Forecasting
- 🌍 Sustainable Lifestyle Analytics
- 📊 Interactive Dashboard
- 🤖 AI-generated Environmental Insights
- ⚡ FastAPI REST APIs
- 🗄 SQL Database Integration
- 📉 Trend Analysis using Machine Learning

---

# 👨‍💻 Author

**Sanoer Soni**

B.Tech Electronics & Computer Engineering (AI & ML)

MIT World Peace University

GitHub: https://github.com/Sanoer11
