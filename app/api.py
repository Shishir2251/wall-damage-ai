from fastapi import APIRouter, UploadFile, File,Form
from inference.detector import detect_damage
from cost_engine.cost_calculator import calculate_cost
from recommender.repair_advisor import recommend_repairs

router = APIRouter()

@router.post("/Analyze")
async def analyze_wall(image: UploadFile= File(...), country: str = Form(...)):
    detections = detect_damage(image)
    cost = calculate_cost(detections, country)
    advice = recommend_repairs (detections)

    return{
        "detections": detections,
        "estimated_cost": cost,
        "repair_advice" : advice
    }