import os
from ultralytics import YOLO

def run_detection(frame_paths, train_number):
    os.makedirs("output/detections", exist_ok=True)
    model = YOLO("yolov8n.pt")  # Pretrained small model

    for frame in frame_paths:
        results = model.predict(frame, save=True, project="output/detections", name="")
        print(f"Detection done: {frame}")
