# YOLOv7 Frame-by-Frame Video Analysis

This script performs frame-by-frame analysis on multiple video files using different YOLOv7 model variants (YOLOv7, YOLOv7-tiny, YOLOv7x). It loops over different image sizes, video files, and model weights to calculate and log the frames per second (FPS) and average FPS for each combination.

## Usage

### Requirements
- YOLOv7 model weights for each variant (YOLOv7, YOLOv7-tiny, YOLOv7x).
- One or more video files for analysis.
- The YOLOv7 repository cloned from GitHub.

### Instructions

1. **Set the File Paths:**
   - Replace `<YOUR_DEVICE_NAME>` with the name of the device you are using (e.g., "RTX 2080 Ti").
   - Replace `<YOUR_POWER_MODE>` with the current power mode of your device (used for metadata storage).
   - Replace `<PATH_TO_YOLOV7_DIRECTORY>` with the path to your cloned YOLOv7 GitHub repository.
   - Replace the paths in `yolo_variants` with the paths to your YOLOv7 weights files.
   - Replace the paths in `video_paths` with the paths to your video files.
   - Replace `<PATH_TO_RESULTS_DIRECTORY>` with the path where you want to save the results.

2. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python frame_by_frame_analysis.py
     ```

3. **Output:**
   - The script will save FPS results to the specified results directory, including the average FPS for each video, model variant, and image size.

### How the Script Works

- **Frame-by-Frame Analysis**: The script processes each video frame by frame, running inference with the YOLOv7 model variants.
- **Batch Processing**: The entire video is processed as one batch for each variant and image size, allowing the calculation of average FPS over the entire video length.
- **Multiple Configurations**: The script automatically loops over different image sizes, video files, and model weights, calculating FPS for each combination.

### Notes

- Ensure that the paths to the YOLOv7 weights, video files, YOLOv7 directory, and results directory are correctly specified to avoid errors.
- The script provides a detailed FPS analysis for different configurations, making it useful for benchmarking and performance evaluation.

