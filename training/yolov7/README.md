# YOLOv7 Training for Oil Tank Detection

This README provides detailed instructions for training YOLOv7 models (YOLOv7-tiny, YOLOv7-standard, YOLOv7-x) for Oil Tank Detection.

## Prerequisites

Ensure you have the following dependencies installed:

- **Python 3.7+**
- **PyTorch**
- **TorchVision**

1. **Clone the YOLOv7 repository:**
   ```bash
   git clone https://github.com/WongKinYiu/yolov7.git
   cd yolov7
   ```
2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure you are using a version of PyTorch and TorchVision that is compatible with CUDA for GPU acceleration.** You can find compatible versions [here](https://pytorch.org/get-started/previous-versions/).

## Training Script
To begin training, ensure that you have the YOLOv7 repository cloned and the `train.py` script available. If you haven't already, download the repository using the commands provided above.

Below is the training script used for all YOLOv7 variants. This example is for the YOLOv7-standard variant:

```bash
python train.py --opt OT/OT_yolov7/opt.yaml
```

## How to Use

### Prepare the Dataset:
- Ensure the dataset paths are correctly set in the `OT_data.yaml` file.
- The `OT_data.yaml` file should be referenced in the `opt.yaml` file for training.

### Run the Training Script:
Navigate to the folder containing the YOLOv7 `train.py` script and run the command specific to your variant:

```bash
python train.py --opt OT/OT_yolov7/opt.yaml
```

## Configuration (opt.yaml)
Each YOLOv7 variant uses an `opt.yaml` file to configure training parameters. Below is an example configuration for YOLOv7-standard:

```yaml
weights: yolov7.pt
cfg: OT/OT_yolov7/OT_yolov7.yaml
data: OT/OT_yolov7/OT_data.yaml
hyp: data/hyp.scratch.p5.yaml
epochs: 300
batch_size: 8
img_size:
- 640
- 640
device: '0'
workers: 8
project: yolov7
name: OT_run
save_dir: yolov7/OT_run
...
```

## Hyperparameters (hyp.yaml)
The `hyp.yaml` file includes hyperparameters for training. Below is an example configuration:

```yaml
lr0: 0.01
lrf: 0.1
momentum: 0.937
weight_decay: 0.0005
warmup_epochs: 3.0
warmup_momentum: 0.8
warmup_bias_lr: 0.1
box: 0.05
cls: 0.3
obj: 0.7
iou_t: 0.2
hsv_h: 0.015
hsv_s: 0.7
hsv_v: 0.4
translate: 0.2
scale: 0.9
fliplr: 0.5
mosaic: 1.0
mixup: 0.15
...
```

## Data Augmentation
The `hyp.yaml` file includes parameters for data augmentation. These parameters control how images are augmented during training:

- `hsv_h`, `hsv_s`, `hsv_v`: Adjust hue, saturation, and value.
- `degrees`: Degree of rotation.
- `translate`: Translation as a fraction of image dimensions.
- `scale`: Scale factor.
- `fliplr`: Probability of horizontal flip.
- `mosaic`: Mosaic augmentation probability.
- `mixup`: Probability of applying mixup augmentation, where images are blended with other images.
- `shear`: Shear angle in degrees.
- `perspective`: Perspective distortion factor.

- `degrees`, `translate`, `scale`, `fliplr`, `mosaic`, `mixup`: Various augmentation techniques.

These augmentations are automatically applied during training when the script is executed.

## Output
The training logs and results, including model checkpoints, will be saved automatically in the `yolov7/OT_run` directory.
