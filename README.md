# Wall Damage AI (No Training Version)

This system uses pretrained computer vision models.
No dataset, no training, no GPU required.

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload

## Endpoint
POST /analyze
Form-data:
- image
- country
