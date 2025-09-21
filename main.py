from src.video_splitter import split_video
from src.frame_extractor import extract_frames
from src.detector import run_detection
from src.report_generator import generate_report

RAW_VIDEO = "data/raw/train.mp4"
TRAIN_NUMBER = "12309"

def main():
    print("🚆 Splitting video...")
    coach_videos = split_video(RAW_VIDEO, TRAIN_NUMBER)

    print("🖼 Extracting frames...")
    coach_frames = extract_frames(coach_videos, TRAIN_NUMBER)

    print("🔎 Running detection...")
    run_detection(coach_frames, TRAIN_NUMBER)

    print("📑 Generating report...")
    generate_report(TRAIN_NUMBER)

    print("✅ Project Completed. Check 'output/' folder.")

if __name__ == "__main__":
    main()
