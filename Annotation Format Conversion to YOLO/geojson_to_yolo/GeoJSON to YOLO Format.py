# Import necessary libraries
import pandas as pd
import os
import ast

# Define the dimensions of the images
width, height = 2560, 2560

# Read the CSV file that contains the annotations
# NOTE: Replace the path below with the path to your annotations.csv file
data = pd.read_csv("<PATH_TO_YOUR_ANNOTATIONS_FILE>")

# Loop over each annotation in the CSV file
for index, row in data.iterrows():

    # Get the coordinates of the bounding box from the 'bounds' column
    bounds = ast.literal_eval(row["bounds"])
    xmin, ymin, xmax, ymax = bounds

    # Convert the bounding box coordinates to the YOLO format
    x_center = (xmin + xmax) / 2 / width
    y_center = (ymin + ymax) / 2 / height
    w = (xmax - xmin) / width
    h = (ymax - ymin) / height

    # Write the converted coordinates to a new text file
    # NOTE: Replace the path below with the path to your desired directory
    with open(os.path.join("<PATH_TO_YOUR_YOLO_DIRECTORY>", row["image_id"] + ".txt"), "a") as f:
        f.write(f"0 {x_center} {y_center} {w} {h}\n")
