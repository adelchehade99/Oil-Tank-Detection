# XML to YOLO Annotation Conversion

This script is used to convert annotations from the XML format (commonly used with Pascal VOC) to the YOLO format. It was specifically applied to the dataset described in "J. Rabbi, S. Chowdhury, and D. Chao. Oil and gas tank dataset, 2020," accessed on March 1, 2024. The dataset includes annotations in both TXT and XML formats, though only one format is necessary for use.

## Usage

### Requirements
- Python 3.x
- xml.etree.ElementTree

### Instructions

1. **Set the File Paths:**
   - Update the following variables in the script to point to the correct locations on your system:
     - `xml_dir = '<PATH_TO_YOUR_XML_ANNOTATIONS>'`: Path to the directory containing the original XML annotation files.
     - `output_dir = '<PATH_TO_YOUR_YOLO_ANNOTATIONS_FOLDER>'`: Directory where YOLO format annotations will be saved.

2. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python xml_to_yolo.py
     ```

3. **Output:**
   - The script will generate `.txt` files in YOLO format, saved in the specified output directory. Each image will have a corresponding `.txt` file with the same name.

## Notes

- The script assumes that all objects are labeled as 'tank' and are mapped to class 0. If your dataset includes multiple classes, you will need to modify the `label_dict` variable in the script accordingly.
- This dataset also includes annotations in TXT format, which have been converted separately.
 
