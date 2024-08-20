from ultralytics import YOLO

# Load a model
model = YOLO('yolov8l.yaml')  # build a new model from YAML
model = YOLO('yolov8l.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8l.yaml').load('yolov8l.pt')  # build from YAML and transfer weights

# Train the model
model.train(data='OT_data.yaml', batch =8, epochs=300, imgsz=640)

