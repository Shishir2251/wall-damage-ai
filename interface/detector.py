from ultralytics import YOLO
from PIL import Image
import io

model= YOLO("yolov8n.pt")

DAMAGE_MAP={
    "crack": ["crack", "fracture", "break"],
    "hole":  ["hole"],
    "damp":  ["stain","wet"],
    "mold":  ["mold", "fungus"],
    "peeling": ["peel"],
}

def detect_damage(image_file):
    Image = Image.open(io.BytesIO(image_file.file.read()))
    results = model(Image)

    damages = []
    for box in results[0].boxes:
        cls = int(box.cls)
        label = model.names[cls].lower()
        area= float(box.xywh[0][2]*box.xywh[0][3])

        damage_type = "unknown"
        for k, v in DAMAGE_MAP.items():
            if any(word in label for word in v):
                damage_type = k
        damages.append({
            "type": damage_type,
            "raw_labels": label,
            "area": round(area,2)
        })
    return damages
