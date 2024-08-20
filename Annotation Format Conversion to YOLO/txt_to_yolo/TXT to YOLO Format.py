# Import necessary libraries
import os
import glob

# Path to the directory containing .txt files
# NOTE: Replace the path below with the appropriate path on your system
txt_dir = '<PATH_TO_YOUR_TXT_FILES>'

# Path to the output directory for YOLO formatted annotations
# NOTE: Replace the path below with the appropriate path on your system
output_dir = '<PATH_TO_YOUR_YOLO_OUTPUT_FOLDER>'

# Dimensions of the image (you should know the dimensions of your images)
img_width = 512
img_height = 512

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Find all .txt files in the specified directory
txt_files = glob.glob(os.path.join(txt_dir, "*.txt"))

# Loop over each .txt file
for txt_file in txt_files:
    with open(txt_file, "r") as f_in:
        # Determine the name for the output file
        base_name = os.path.basename(txt_file)
        output_file = os.path.join(output_dir, base_name)

        with open(output_file, "w") as f_out:
            for line in f_in:
                # Read values from the txt file
                # Note: assuming your txt file format is:
                # class, xmin, ymin, xmax, ymax
                elements = line.strip().split()

                # Calculate the center, width, and height of the bounding box
                class_id = int(elements[0]) - 1  # Subtract 1 from class_id for zero-indexing
                xmin = float(elements[1])
                ymin = float(elements[2])
                xmax = float(elements[3])
                ymax = float(elements[4])

                # Convert to YOLO format (center x, center y, width, height) normalized to image size
                x_center = (xmin + xmax) / 2.0 / img_width
                y_center = (ymin + ymax) / 2.0 / img_height
                bb_width = (xmax - xmin) / img_width
                bb_height = (ymax - ymin) / img_height

                # Write the YOLO format annotation to the output file
                f_out.write(f"{class_id} {x_center} {y_center} {bb_width} {bb_height}\n")

