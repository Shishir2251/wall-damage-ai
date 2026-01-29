from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="wall.yaml",
    epochs=50,
    imasz=640,
    batch=8,
    device="cpu"

)
