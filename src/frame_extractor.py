import cv2, os

def extract_frames(coach_videos, train_number, step=30):
    os.makedirs("output/frames", exist_ok=True)
    frame_paths = []

    for idx, video in enumerate(coach_videos, start=1):
        folder = f"output/frames/{train_number}_{idx}"
        os.makedirs(folder, exist_ok=True)

        cap = cv2.VideoCapture(video)
        count = 0
        while True:
            ret, frame = cap.read()
            if not ret: break
            if count % step == 0:
                filename = f"{folder}/{train_number}_{idx}_{count}.jpg"
                cv2.imwrite(filename, frame)
                frame_paths.append(filename)
            count += 1
        cap.release()
        print(f"Extracted frames for coach {idx}")
    return frame_paths
