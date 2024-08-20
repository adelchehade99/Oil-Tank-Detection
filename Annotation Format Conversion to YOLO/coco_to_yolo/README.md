# COCO to YOLO Annotation Conversion

This script is used to convert annotations from the COCO format to the YOLO format. It was specifically applied to the dataset described in "K Heyer. Oil storage tanks, 2019," accessed on March 1, 2024. After conversion, further annotations and refinements were performed.

## Usage

### Requirements
- Python 3.x
- JSON files in COCO format

### Instructions

1. **Set the File Paths:**
   - Update the following variables in the script to point to the correct locations on your system:
     - `coco_annotation_file_path`: Path to the COCO annotation file.
     - `yolo_annotation_folder_path`: Directory where YOLO format annotations will be saved.

2. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python coco_to_yolo.py
     ```

3. **Output:**
   - The script will generate `.txt` files in the YOLO format, saved in the specified output directory. Each image will have a corresponding `.txt` file with the same name.

4. **Statistics:**
   - The script will print the total number of annotated images after conversion.

### Notes

- The script assumes all images are of size 512x512. If your images have different dimensions, modify the `image_id_to_size` dictionary accordingly.
- The script assumes a single class for all objects. If you have multiple classes, you will need to adjust the `class_id` variable within the loop. 
