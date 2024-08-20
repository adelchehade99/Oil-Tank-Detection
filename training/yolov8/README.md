# YOLOv8 Training for Oil Tank Detection

This README provides detailed instructions for training YOLOv8 models (YOLOv8n, YOLOv8s, YOLOv8m, YOLOv8l, YOLOv8xl) for Oil Tank Detection.

## Prerequisites

Ensure you have the following dependencies installed:

- Python 3.8+
- PyTorch
- Ultralytics YOLOv8 package

1. **Clone the YOLOv8 repository:**
   ```bash
   git clone https://github.com/ultralytics/ultralytics.git
   cd ultralytics
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure you are using a version of PyTorch and TorchVision that is compatible with CUDA for GPU acceleration.** You can find compatible versions [here](https://pytorch.org/get-started/previous-versions/).

4. **Install the Ultralytics YOLOv8 package:**

   ```bash
   pip install ultralytics 
   ```

## Training Script
Below is the training script used for all YOLOv8 variants. This example is for the YOLOv8n variant:

```python
from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
model.train(data='OT_data.yaml', epochs=300, imgsz=640)
```

## How to Use

### Prepare the Dataset:
- Ensure the dataset paths are correctly set in the `OT_data.yaml` file.
- The `OT_data.yaml` file should be in the same directory as your training script.

### Run the Training Script:
Navigate to the folder containing the `train.py` script and run:

```bash
python train.py
```

## Configuration (OT_data.yaml)
The `OT_data.yaml` file specifies the paths to your training and validation datasets, the number of classes, and the class names. Below is an example configuration:

```yaml
# OT dataset

# train and val data as 1) directory: path/images/, 2) file: path/images.txt, or 3) list: [path1/images/, path2/images/]
train: /path/to/train/images.txt
val: /path/to/val/images.txt

# Number of classes
nc: 1

# Class names
names: ['OT']
```
- `train`: Path to the text file listing all the training images.
- `val`: Path to the text file listing all the validation images.
- `nc`: Number of classes in your dataset. For oil tank detection, this is set to 1.
- `names`: List of class names. Here, it's set to ['OT'] for oil tanks.

## Configuration (args.yaml)
Each YOLOv8 variant uses an `args.yaml` file to configure training parameters. Below is an example configuration:

```yaml
task: detect
mode: train
model: yolov8n.yaml
data: OT_data.yaml
epochs: 300
batch: 16
imgsz: 640
save: true
optimizer: auto
...

# Data Augmentation
hsv_h: 0.015
hsv_s: 0.7
hsv_v: 0.4
degrees: 0.0
translate: 0.1
scale: 0.5
fliplr: 0.5
mosaic: 1.0
```
## Data Augmentation
The `args.yaml` file includes parameters for data augmentation. These parameters control how images are augmented during training:

- `hsv_h`, `hsv_s`, `hsv_v`: Adjust hue, saturation, and value.
- `degrees`: Degree of rotation.
- `translate`: Translation as a fraction of image dimensions.
- `scale`: Scale factor.
- `fliplr`: Probability of horizontal flip.
- `mosaic`: Mosaic augmentation probability.

These augmentations are automatically applied during training when the script is executed.

## Output
The training logs and results, including model checkpoints, will be saved automatically in the `runs/detect/trainX` directory.
