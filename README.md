# Wall Damage AI API

AI system for detecting wall damages from images and estimating repair cost.

## Features
- Crack, hole, damp, mold detection
- Area estimation
- Country-based repair cost
- Repair recommendations

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
