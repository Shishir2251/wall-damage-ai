from ultralytics import YOLO
from PIL import Image
import io

model= YOLO("yolov8n.pt")

"""DAMAGE_MAP={
    "crack": ["crack", "fracture", "break"],
    "hole":  ["hole"],
    "damp":  ["stain","wet"],
    "mold":  ["mold", "fungus"],
    "peeling": ["peel"],
}"""

def detect_damage(image_file):
    Image = Image.open(io.BytesIO(image_file.file.read())).convert("RGB")
    results = model(Image)

    detections = []
    for r in results:
        for box in r.boxes:
            cls_id= int(box.cls[0])
            label = model.names[cls_id]
            area= float((box.xywh[0][2] - box.xyxy[0][0])*
                        box.xywh[0][3] - box.xyxy[0][0])

            detections.append({
                "type": label,
                "raw_label": label,
                "area": area
            })
    return detections
