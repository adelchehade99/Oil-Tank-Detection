from ultralytics import YOLO
import os

# Define the variants of YOLOv8 you want to use
variants = {
    'Nano': '<PATH_TO_YOLOV8_NANO_WEIGHTS>',
    'Small': '<PATH_TO_YOLOV8_SMALL_WEIGHTS>',
    'Medium': '<PATH_TO_YOLOV8_MEDIUM_WEIGHTS>',
    'Large': '<PATH_TO_YOLOV8_LARGE_WEIGHTS>',
    'Extra Large': '<PATH_TO_YOLOV8_EXTRA_LARGE_WEIGHTS>',
}

# Define path to the directory containing images
source_directory = '<PATH_TO_YOUR_TEST_IMAGES_DIRECTORY>'

# Output directory for the results
output_dir = '<PATH_TO_OUTPUT_DIRECTORY>'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Loop through each YOLOv8 variant
for name, weight_path in variants.items():
    print(f"Processing with {name} model...")

    # Load the model
    model = YOLO(weight_path)

    # Run inference on the source directory
    results = model.predict(source=source_directory, show_labels=False, show_conf=False, save=True)

    # Process each result in results
    for i, result in enumerate(results):
        # The save method automatically saves the visualized result to the disk
        # Construct the result filename for clarity
        original_filename = os.path.splitext(os.path.basename(result.path))[0]
        result_filename = f"{original_filename}_{name}.jpg"
        result_path = os.path.join(output_dir, result_filename)
        result.save(filename=result_path)  # Save visualized result

        print(f"Results saved for {name} - Image {i+1} to {result_path}")

print("Inference completed for all variants.")

