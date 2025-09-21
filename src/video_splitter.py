import cv2, os

def split_video(video_path, train_number):
    os.makedirs("output/processed_videos", exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = length / fps

    print(f"Video length: {duration:.2f}s, FPS: {fps}")

    # 🚨 For now: split every 10 seconds = 1 coach (you can improve this with ML detection)
    coach_videos = []
    segment = 10
    idx = 1
    start = 0

    while start < duration:
        end = min(start + segment, duration)
        output_file = f"output/processed_videos/{train_number}_{idx}.mp4"

        # FFmpeg-style cut using OpenCV (simplified)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_file, fourcc, fps,
                              (int(cap.get(3)), int(cap.get(4))))

        cap.set(cv2.CAP_PROP_POS_MSEC, start*1000)
        while cap.get(cv2.CAP_PROP_POS_MSEC) < end*1000:
            ret, frame = cap.read()
            if not ret: break
            out.write(frame)
        out.release()

        coach_videos.append(output_file)
        print(f"Created {output_file}")
        idx += 1
        start += segment

    cap.release()
    return coach_videos
