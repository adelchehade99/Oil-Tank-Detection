# YOLOv8 Video Prediction with Recording

This script performs object detection on each frame of a video using the YOLOv8 model and saves the annotated video to a specified output file.

## Usage

### Requirements
- YOLOv8 model weights file.
- A video file that you want to process.

### Instructions

1. **Set the File Paths:**
   - Replace `<PATH_TO_YOUR_YOLOV8_WEIGHTS_FILE>` in the script with the path to your YOLOv8 weights file.
   - Replace `<PATH_TO_YOUR_VIDEO_FILE>` in the script with the path to your input video file.
   - Replace `<PATH_TO_YOUR_OUTPUT_VIDEO_FILE>` with the path where you want to save the annotated video.

2. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python video_prediction_with_recording.py
     ```

3. **Output:**
   - The script will save the annotated video to the specified output path, with each frame of the video annotated by the YOLOv8 model.

### Script Overview

- **model = YOLO('<PATH_TO_YOUR_YOLOV8_WEIGHTS_FILE>')**: Loads the YOLOv8 model with the specified weights.
- **cap = cv2.VideoCapture(video_path)**: Opens the video file for frame-by-frame processing.
- **video_writer = cv2.VideoWriter(output_path, ...)**: Initializes a VideoWriter object to save the annotated video.
- **while cap.isOpened():**: Loops through each frame of the video, performs object detection, and saves the annotated frames.

### Notes

- Ensure that the paths to the YOLOv8 weights, input video, and output video are correctly specified to avoid errors.
- The annotated video will be saved in the specified output directory.
- You can exit the video preview by pressing the 'q' key.
 
