# Import necessary libraries
import os
import xml.etree.ElementTree as ET

# Define the directory where the XML annotation files are stored and the output directory for YOLO format annotations
# NOTE: Replace the paths below with the appropriate paths on your system
xml_dir = '<PATH_TO_YOUR_XML_ANNOTATIONS>'
output_dir = '<PATH_TO_YOUR_YOLO_ANNOTATIONS_FOLDER>'

# Define a dictionary to map object names to their respective labels.
# In this case, all objects are 'tank', so they are mapped to label 0.
label_dict = {'tank': 0}

# Loop over each file in the XML directory
for xml_file in os.listdir(xml_dir):
    # Only process files that end with '.xml' (XML files)
    if not xml_file.endswith('.xml'):
        continue

    # Parse the XML file
    tree = ET.parse(os.path.join(xml_dir, xml_file))
    root = tree.getroot()

    # Extract the size of the image from the XML
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    # List to store YOLO format annotations for each object in the image
    yolo_annots = []

    # Iterate over each object in the XML file
    for obj in root.iter('object'):
        # Get the label of the object using the label_dict
        label = label_dict[obj.find('name').text]

        # Extract the bounding box coordinates of the object
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        # Convert the bounding box coordinates to YOLO format
        # (center x, center y, width, height) and normalize them
        x_center = (xmin + xmax) / (2 * width)
        y_center = (ymin + ymax) / (2 * height)
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        # Append the YOLO format annotation to the list
        yolo_annots.append(f'{label} {x_center} {y_center} {bbox_width} {bbox_height}')

    # Write the YOLO format annotations to a text file
    with open(os.path.join(output_dir, xml_file.replace('.xml', '.txt')), 'w') as f:
        f.write('\n'.join(yolo_annots))
