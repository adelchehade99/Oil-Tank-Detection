# Import necessary libraries
import json
import os

# Define paths for input COCO annotation file and output YOLO format annotations folder
# NOTE: Replace the paths below with the appropriate paths on your system
coco_annotation_file_path = "<PATH_TO_YOUR_COCO_ANNOTATIONS_FILE>"
yolo_annotation_folder_path = "<PATH_TO_YOUR_YOLO_ANNOTATIONS_FOLDER>"

# Ensure the output directory exists
os.makedirs(yolo_annotation_folder_path, exist_ok=True)

# Load the COCO annotation file
with open(coco_annotation_file_path) as f:
    data = json.load(f)

# Create mappings from image ID to filename and image ID to size
image_id_to_filename = {image["id"]: image["file_name"] for image in data["images"]}
image_id_to_size = {image["id"]: (512, 512) for image in data["images"]}  # Assuming all images are of size 512x512

# Initialize the set for storing annotated images
annotated_images = set()

# Iterate over each annotation in the COCO data
for annotation in data["annotations"]:
    # Check if this image ID exists in the image_id_to_filename mapping
    if annotation["image_id"] in image_id_to_filename:
        bbox = annotation["bbox"]
        image_width, image_height = image_id_to_size[annotation["image_id"]]

        # Convert COCO bounding box format [x, y, width, height]
        # to YOLO format [x_center, y_center, width, height] relative to image size
        x_center = (bbox[0] + bbox[2] / 2) / image_width
        y_center = (bbox[1] + bbox[3] / 2) / image_height
        w = bbox[2] / image_width
        h = bbox[3] / image_height

        # Assuming the dataset only has one class
        class_id = 0

        # Determine the path for the YOLO annotation file
        yolo_annotation_file_path = os.path.join(yolo_annotation_folder_path,
                                                 image_id_to_filename[annotation["image_id"]].replace('.jpg', '.txt'))

        # If this is the first bounding box for this image, add the file path to the set of annotated images
        if yolo_annotation_file_path not in annotated_images:
            annotated_images.add(yolo_annotation_file_path)

        # Append the YOLO format bounding box to the annotation file
        with open(yolo_annotation_file_path, 'a') as file:
            file.write(f"{class_id} {x_center} {y_center} {w} {h}\n")

# Print out statistics about the annotations
print(f"Total number of annotated images: {len(annotated_images)}")
