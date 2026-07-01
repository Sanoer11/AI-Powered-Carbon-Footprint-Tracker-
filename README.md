# AI-Powered Carbon Footprint Analytics

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

EcoTrack is a full-stack Green Tech web application designed to digitize and analyze personal environmental impact. By logging daily activities across commute, energy consumption, and dietary habits, the platform leverages Machine Learning to forecast future emission trends and provide actionable, data-driven insights.

Developed to align with modern corporate sustainability goals and fast-growing Green Tech verticals.

---

## 🚀 Key Features

* **Predictive Machine Learning Engine:** Utilizes a Scikit-Learn Linear Regression model trained on rolling historical data to forecast a 30-day continuous emission trendline.
* **Automated Feature Importance (AI Insights):** Dynamically analyzes the user's most recent data block to identify and flag the specific lifestyle category (e.g., Electricity vs. Food) driving upward emission trends.
* **Interactive Data Visualization:** A responsive React UI leveraging Recharts to translate complex environmental data and predictive ML arrays into intuitive, user-friendly graphs and KPI summary cards.
* **Robust API & QA Validation:** A high-performance Python/FastAPI backend employing Pydantic models for strict data validation (QA), ensuring absolute data integrity before it reaches the SQLAlchemy ORM layer.

---

## 🏗️ System Architecture

The application follows a decoupled, modern full-stack architecture:

1. **Client Layer (React):** Manages user state, form ingestion, and renders interactive analytic charts.
2. **API Layer (FastAPI):** Handles CORS, data routing, validation, and mathematical conversions using standardized environmental emission factors.
3. **Data & Persistence Layer (SQLite & SQLAlchemy):** Securely logs time-series data for user activities.
4. **Data Science Engine (Pandas & Scikit-learn):** Ingests SQLite data into DataFrames, cleans date formats, calculates aggregates, and outputs trained predictive models back to the API.

---

## 💻 Tech Stack

**Frontend (UI/UX & Web Technologies)**
* React.js
* Tailwind CSS (Styling)
* Recharts (Data Visualization)
* Lucide React (Dynamic Iconography)

**Backend (Full Stack & DevOps)**
* Python 3
* FastAPI (REST API Framework)
* Uvicorn (ASGI Server)
* SQLite & SQLAlchemy (Relational Database & ORM)

**Data Science & Machine Learning**
* Pandas & NumPy (Data manipulation & cleaning)
* Scikit-Learn (Linear Regression modeling)

---

## 📡 API Reference

The backend exposes fully documented REST endpoints (Swagger UI accessible at `/docs`).

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/config` | Retrieves the static JSON dictionary of environmental emission factors. |
| `POST` | `/log-activity` | Ingests user activity, validates schema, calculates CO2e, and commits to SQLite. |
| `GET` | `/predictive-trends` | Triggers the ML pipeline: fetches historical data, trains the model, predicts the next 30 days, and returns a JSON payload with actionable warnings. |

---

## ⚙️ Local Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://[github.com/YOUR_USERNAME/ecotrack-ai-carbon-tracker](https://github.com/Sanoer11/AI-Powered-Carbon-Footprint-Tracker).git](https://github.com/YOUR_USERNAME/ecotrack-ai-carbon-tracker.git)
cd ecotrack-ai-carbon-tracker
