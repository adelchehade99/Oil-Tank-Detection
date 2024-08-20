# YOLOv8 Image Inference with Multiple Variants

This script allows you to perform inference on a batch of images using multiple YOLOv8 model variants (Nano, Small, Medium, Large, Extra Large). The results, including annotated images, will be saved to a specified output directory.

## Usage

### Requirements
- YOLOv8 model weights for each variant (Nano, Small, Medium, Large, Extra Large).
- A directory containing the images you want to run inference on.

### Instructions

1. **Set the File Paths:**
   - Replace `<PATH_TO_YOLOV8_NANO_WEIGHTS>`, `<PATH_TO_YOLOV8_SMALL_WEIGHTS>`, etc., in the script with the paths to your YOLOv8 weights files.
   - Replace `<PATH_TO_YOUR_TEST_IMAGES_DIRECTORY>` in the script with the path to the directory containing your test images.
   - Replace `<PATH_TO_OUTPUT_DIRECTORY>` with the path where you want to save the annotated images.

2. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python image_inference.py
     ```

3. **Output:**
   - The script will save the annotated images in the specified output directory, with each image annotated by different YOLOv8 variants.

### Script Overview

- **Variants Dictionary**: The script loops through the specified YOLOv8 variants (Nano, Small, Medium, Large, Extra Large).
- **model = YOLO(weight_path)**: Loads the YOLOv8 model with the specified weights.
- **results = model.predict(...)**: Runs inference on the images in the specified directory, saving the annotated results.

### Notes

- Ensure that the correct paths to the YOLOv8 weights and directories are specified to avoid errors.
- The annotated images will be saved in the output directory, with filenames indicating the model variant used.
 
