from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data=r"C:\Users\Shishir\Projects\wall-damage-ai\training\wall.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    device="cpu",
    workers=2,
    project="runs",
    name="wall_damage"
)

print("Training finished.")
print("Model saved at: runs/detect/wall_damage/weights/best.pt")
