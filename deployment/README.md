# Deployment Scripts for Oil Tank Detection

This directory contains deployment scripts for oil tank detection using YOLOv7 and YOLOv8 models. The scripts are designed for testing on images, videos, and performance analysis in terms of frames per second (FPS). The deployment process is consistent across high-end GPUs and edge devices, with the primary difference being the installation method for PyTorch and TorchVision on edge devices like Nvidia Jetson.

## Directory Structure

- `yolov7/`: Contains scripts and requirements for deploying YOLOv7 models.
- `yolov8/`: Contains scripts and requirements for deploying YOLOv8 models.

## Requirements

### YOLOv7
- **Python version**: Python 3.x
- **Environment**: Anaconda is recommended.
- **Dependencies**:
  1. Clone the YOLOv7 repository from GitHub:
     ```bash
     git clone https://github.com/WongKinYiu/yolov7
     cd yolov7
     pip install -r requirements.txt
     ```
  2. For high-end GPUs, install PyTorch and TorchVision compatible with CUDA and cuDNN:
     ```bash
     pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
     ```
     - [Link for compatible PyTorch versions with CUDA for high-end GPUs](https://pytorch.org/get-started/previous-versions/)
  3. For edge devices like Nvidia Jetson, install PyTorch and TorchVision using pre-built pip wheels:
     - **Install PyTorch** (example for JetPack 5.0.2):
       ```bash
       sudo apt-get install -y libopenblas-base libopenmpi-dev
       wget https://developer.download.nvidia.com/compute/redist/jp/v50/pytorch/torch-1.12.0a0+2c916ef.nv22.3-cp38-cp38-linux_aarch64.whl -O torch-1.12.0a0+2c916ef.nv22.3-cp38-cp38-linux_aarch64.whl
       pip3 install torch-1.12.0a0+2c916ef.nv22.3-cp38-cp38-linux_aarch64.whl
       ```
     - **Install TorchVision** (compatible with PyTorch v1.12.0):
       ```bash
       sudo apt install -y libjpeg-dev zlib1g-dev
       git clone --branch v0.13.0 https://github.com/pytorch/vision torchvision
       cd torchvision
       python3 setup.py install --user
       ```
     - [Link for PyTorch compatibility with Jetson platforms](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)

### YOLOv8
- **Python version**: Python 3.8+
- **Environment**: Can be used with Anaconda or PyCharm.
- **Dependencies**:
  1. Clone the YOLOv8 repository from Ultralytics:
     ```bash
     git clone https://github.com/ultralytics/ultralytics.git
     cd ultralytics
     pip install -r requirements.txt
     ```
  2. For high-end GPUs, install PyTorch and TorchVision compatible with CUDA and cuDNN:
     ```bash
     pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
     ```
     - [Link for compatible PyTorch versions with CUDA for high-end GPUs](https://pytorch.org/get-started/previous-versions/)
  3. For edge devices like Nvidia Jetson, install PyTorch and TorchVision using pre-built pip wheels (as described in the YOLOv7 section above).

## Notes

- The deployment scripts work similarly across high-end GPUs and edge devices. The key difference lies in how PyTorch and TorchVision are installed to optimize performance on the respective hardware.
- Ensure that you have the appropriate NVIDIA drivers installed on your system to leverage GPU acceleration.
- The provided installation commands for edge devices are examples. Adjust them based on your specific JetPack version and PyTorch/TorchVision requirements.

 
