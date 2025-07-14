# 🛰️ Geo Processor API (FastAPI)

This project was deployed on Render.com and is available at: [Geo Processor Backend](https://geo-processor-backend.onrender.com)

This is a lightweight **Python microservice** built with **FastAPI** that receives a list of coordinate points, validates them, and returns:

- 📦 A **bounding box** (`north`, `south`, `east`, `west`)
- 🎯 The **geographic centroid** of the input points

Used in combination with a frontend and middleware to power geographic data visualization.

---

## 🧱 Project Structure
TechnicalTest/
- ├── dependencies/                  # Dependency injection and validation logic
- │   └── validate_coordinates.py
- ├── routers/                       # Route definitions
- │   └── geo_processor.py          # POST endpoint logic
- ├── schemas/                       # Pydantic models
- │   └── coordinates.py
- ├── utils/                         # Business logic
- │   └── analyze_coordinates.py    # Bounding box and centroid functions
- ├── main.py                        # App entrypoint
- ├── requirements.txt               # Python dependencies
- └── README.md                      # You’re here!

---

## ⚙️ How It Works

1. The user sends a POST request to `/geo/process/` with a JSON body:
```json
{
  "points": [
    { "lat": 40.7128, "lng": -74.006 },
    { "lat": 34.0522, "lng": -118.2437 }
  ]
}
```

The api returns it
```json
{
  "centroid": { "lat": 37.3825, "lng": -96.1249 },
  "bounds": {
    "north": 40.7128,
    "south": 34.0522,
    "east": -74.006,
    "west": -118.2437
  }
}
```

## 🚀️ Clone and run locally

1. Clone the repository
```bash
git clone https://github.com/your-username/geo-processor-api.git
cd geo-processor-api
```

2.	Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
```

3.	Install dependencies
```bash
pip install -r requirements.txt
```

4.	Run the server
```baah
uvicorn main:app --reload
```

5.	Visit Swagger docs:
http://localhost:8000/docs
