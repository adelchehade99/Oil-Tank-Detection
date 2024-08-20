# Import necessary libraries
import cv2
import time
from ultralytics import YOLO

# Image size for YOLO inference (You can change it)
image_size = 640
# Power mode comment (used for data storage and you can change it depending to the power mode choosed)
power_mode = "Max Performance"

# Paths to the videos to be processed
# NOTE: Replace the paths below with the appropriate paths on your system
video_paths = [
    '<PATH_TO_VIDEO_1>',
    '<PATH_TO_VIDEO_2>',
    '<PATH_TO_VIDEO_3>',
]

# YOLOv8 variants and their respective weight paths
# NOTE: Replace the paths below with the paths to your YOLOv8 weights files
yolo_variants = {
    'Nano': '<PATH_TO_NANO_WEIGHTS>',
    'Small': '<PATH_TO_SMALL_WEIGHTS>',
    'Medium': '<PATH_TO_MEDIUM_WEIGHTS>',
    'Large': '<PATH_TO_LARGE_WEIGHTS>',
    'Extra Large': '<PATH_TO_EXTRA_LARGE_WEIGHTS>',
}

# Initialize lists for FPS data storage
jetson_model = "Jetson Nano" #you can change this depending to the harware you work on it, it is just metadata
all_results = [f"Jetson Model: {jetson_model}\n"]
all_summary_results = [f"Jetson Model: {jetson_model}\n"]

# Loop over each video for processing
for video_path in video_paths:
    cap = cv2.VideoCapture(video_path)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    video_results = [
        f"\n=== Video: {video_path} ===\nLength: {video_length} frames\nImage Size: {image_size}\nPower Mode: {power_mode}\n"]
    video_summary_results = video_results.copy()

    # Loop over YOLO variants for inference
    for variant, weight_path in yolo_variants.items():
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset video to the first frame
        model = YOLO(weight_path)
        frame_count = 0
        inference_count = 0
        fps_list = []
        inference_results = [f"\n----- {variant} -----\n"]

        # Loop through each frame of the video for inference
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1
            start_time = time.time()
            results = model(frame, imgsz=image_size)
            elapsed_time = time.time() - start_time
            fps = 1.0 / elapsed_time
            fps_list.append(fps)
            inference_count += 1
            print(f"{variant} - Current FPS at video frame {frame_count}, inference {inference_count}: {fps}")
            inference_results.append(f"Current FPS at video frame {frame_count}, inference {inference_count}: {fps}\n")

        if fps_list:
            avg_fps = sum(fps_list) / len(fps_list)
            print(f"{variant} - Average FPS: {avg_fps}")
            inference_results.append(f"Average FPS: {avg_fps}\n")
            video_summary_results.append(f"\n----- {variant} -----\nAverage FPS: {avg_fps}\n")

        video_results.extend(inference_results)

        print(f"Waiting 20 seconds before starting the next YOLOv8 variant...")
        time.sleep(20)

    all_results.extend(video_results)
    all_summary_results.extend(video_summary_results)

# Save FPS data to a file
# NOTE: Replace the path below with the path to your results storage directory
with open('<PATH_TO_YOUR_RESULTS_DIRECTORY>.txt', 'w') as f:
    f.writelines(all_results)

# Save summary FPS data to a file
# NOTE: Replace the path below with the path to your results storage directory
with open('<PATH_TO_YOUR_RESULTS_DIRECTORY>.txt', 'w') as f:
    f.writelines(all_summary_results)
