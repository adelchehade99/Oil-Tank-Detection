# GeoJSON to YOLO Annotation Conversion

This script is used to convert annotations from a CSV file (with GeoJSON format bounding boxes) to YOLO format. It was specifically applied to the dataset described in "AirbusGeo. Airbus oil storage detection, 2021," accessed on March 1, 2024. After conversion, further annotations and refinements were performed using CVAT.

## Usage

### Requirements
- Python 3.x
- pandas

### Instructions

1. **Set the File Paths:**
   - Update the following variables in the script to point to the correct locations on your system:
     - `data = pd.read_csv("<PATH_TO_YOUR_ANNOTATIONS_FILE>")`: Path to the CSV file containing the annotations.
     - `with open(os.path.join("<PATH_TO_YOUR_YOLO_DIRECTORY>", row["image_id"] + ".txt"), "a")`: Directory where YOLO format annotations will be saved.

2. **Adjust Image Dimensions (if needed):**
   - The script assumes that all images are 2560x2560 pixels. If your images have different dimensions, modify the `width` and `height` variables accordingly.

3. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python geojson_to_yolo.py
     ```

4. **Output:**
   - The script will generate `.txt` files in YOLO format, saved in the specified output directory. Each image will have a corresponding `.txt` file with the same name.

## Notes

- The script assumes a single class for all objects. If your dataset includes multiple classes, you will need to modify the script accordingly.
- After conversion, annotations were refined using CVAT for enhanced accuracy.

 
