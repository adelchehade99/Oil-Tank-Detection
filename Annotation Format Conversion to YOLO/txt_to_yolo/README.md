# TXT to YOLO Annotation Conversion

This script is used to convert annotations from a custom TXT format to the YOLO format. It was specifically applied to the dataset described in "J. Rabbi, S. Chowdhury, and D. Chao. Oil and gas tank dataset, 2020," accessed on March 1, 2024. The dataset includes annotations in both TXT and XML formats, though only one format is necessary for use.

## Usage

### Requirements
- Python 3.x
- glob

### Instructions

1. **Set the File Paths:**
   - Update the following variables in the script to point to the correct locations on your system:
     - `txt_dir = '<PATH_TO_YOUR_TXT_FILES>'`: Path to the directory containing the original TXT annotation files.
     - `output_dir = '<PATH_TO_YOUR_YOLO_OUTPUT_FOLDER>'`: Directory where YOLO format annotations will be saved.

2. **Adjust Image Dimensions (if needed):**
   - The script assumes that all images are 512x512 pixels. If your images have different dimensions, modify the `img_width` and `img_height` variables accordingly.

3. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python txt_to_yolo.py
     ```

4. **Output:**
   - The script will generate `.txt` files in YOLO format, saved in the specified output directory. Each image will have a corresponding `.txt` file with the same name.

## Notes

- The script assumes a custom TXT format with the following fields: `class, xmin, ymin, xmax, ymax`.
- This dataset also includes annotations in XML format, which have been converted separately.
 
