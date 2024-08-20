# YOLOv7 Image Inference

This script performs inference on a batch of images using different YOLOv7 model variants (YOLOv7, YOLOv7-tiny, YOLOv7x). The results are saved in a specified output directory, with subdirectories for each model variant.

## Usage

### Requirements
- YOLOv7 model weights for each variant (YOLOv7, YOLOv7-tiny, YOLOv7x).
- A directory containing the images you want to run inference on.
- The YOLOv7 repository cloned from GitHub.

### Instructions

1. **Set the File Paths:**
   - Replace `<PATH_TO_YOLOV7_WEIGHTS>`, `<PATH_TO_YOLOV7_TINY_WEIGHTS>`, `<PATH_TO_YOLOV7X_WEIGHTS>` with the paths to your YOLOv7 weights files.
   - Replace `<PATH_TO_SOURCE_IMAGE_DIRECTORY>` with the path to the directory containing your test images.
   - Replace `<PATH_TO_YOLOV7_DIRECTORY>` with the path to your cloned YOLOv7 GitHub repository.
   - Replace `<PATH_TO_OUTPUT_DIRECTORY>` with the path where you want to save the results.

2. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python test_images_inference.py
     ```

3. **Output:**
   - The script will save the annotated images to the specified output directory, with each variant's results saved in a separate subdirectory.

### Script Overview

- **weights_paths**: Dictionary mapping YOLOv7 variants to their respective weights files.
- **source_image**: Path to the directory containing the images to be processed.
- **output_directory**: Directory where the results will be saved. Subdirectories are created for each YOLOv7 variant.

### Notes

- Ensure that the paths to the YOLOv7 weights, source images, YOLOv7 directory, and output directory are correctly specified to avoid errors.
- The script allows you to easily compare the performance of different YOLOv7 model variants by running inference on the same set of images.
 
