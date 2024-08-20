# YOLOv8 Frame-by-Frame Video Analysis

This script performs frame-by-frame analysis on multiple video files using different YOLOv8 model variants (Nano, Small, Medium, Large, Extra Large). It calculates and logs the frames per second (FPS) for each variant, providing detailed and summary results.

## Usage

### Requirements
- YOLOv8 model weights for each variant (Nano, Small, Medium, Large, Extra Large).
- One or more video files for analysis.
- The script is optimized for use on hardware like the Jetson Nano but can be adapted for other platforms.

### Instructions

1. **Set the File Paths:**
   - Replace `<PATH_TO_VIDEO_1>`, `<PATH_TO_VIDEO_2>`, etc., with the paths to your video files.
   - Replace `<PATH_TO_NANO_WEIGHTS>`, `<PATH_TO_SMALL_WEIGHTS>`, etc., with the paths to your YOLOv8 weights files.
   - Replace `<PATH_TO_YOUR_RESULTS_DIRECTORY>` with the path where you want to save the results.

2. **Adjust Metadata and Parameters (if needed):**
   - **jetson_model**: Modify this to reflect the hardware you are using, e.g., "Jetson Nano," "Jetson Xavier," etc.
   - **image_size**: Set the desired image size for inference (default is 640).
   - **power_mode**: Set this to match your device's power mode (used for metadata storage).

3. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python frame_by_frame_analysis.py
     ```

4. **Output:**
   - The script will save detailed and summary FPS results to the specified results directory.
   - Detailed results include frame-by-frame FPS for each video and model variant.
   - Summary results include average FPS for each video and model variant.

### Script Overview

- **video_paths**: List of video files to be processed.
- **yolo_variants**: Dictionary mapping YOLOv8 variants to their respective weights files.
- **frame-by-frame analysis**: The script processes each video frame individually, calculates FPS, and logs the results.

### Notes

- Ensure that the paths to the YOLOv8 weights, video files, and results directory are correctly specified to avoid errors.
- The script includes a 20-second delay between processing each YOLOv8 variant to prevent overheating or resource exhaustion on edge devices.
- The metadata fields `jetson_model` and `power_mode` are for informational purposes and can be customized as needed.
 
