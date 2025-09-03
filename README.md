# **Silhouette Tracker: Real-Time Human Pose Estimation via YOLOv8 with CUDA Acceleration**

A real-time human pose estimation system using **YOLOv8** with **NVIDIA CUDA** hardware acceleration. The project is implemented in an isolated **Conda** environment for reproducibility and portability.

> **Note**:  
This is an educational project focused on demonstrating modern computer vision workflows and CUDA acceleration rather than providing a production tracking system.

## **Available Documentation / Доступная документация**

- [English Documentation](README.md) (current document / текущий документ)
- [Документация на русском языке](README_RU.md)

## **Prerequisites**

1. **OS:** Linux x86_64.
2. **Python Package Manager:** Conda (Anaconda, Miniconda, Mamba, or Micromamba).
3. **NVIDIA CUDA:** CUDA version 12.6.3 or higher with corresponding NVIDIA drivers installed.

## **Project Structure**

```bash
.
├── .env.example    # Configuration template
├── SBOMs/          # Dependency metadata
├── app/            # Application source code
├── models/         # YOLOv8 models
└── videos/         # Input video files
```

## **Quick Start**

### **I. Clone the Repository**

```bash
git clone https://github.com/Sierra-Arn/silhouette-tracker-python.git  
cd silhouette-tracker-python
```

### **II. Create and Activate Virtual Environment**

```bash
conda env create -p ./.venv -f SBOMs/conda-linux-64-lock.yml
conda activate ./.venv
```

### **III. Prepare Data**

Models and videos are not included in the repository due to size limitations. To download the models, run:

```bash
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n-pose.pt   && \
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s-pose.pt   && \
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8m-pose.pt   && \
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8l-pose.pt   && \
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8x-pose.pt  
```

Add any video to the `videos/` directory. For demonstration, you can download videos from [Pexels Free Stock Videos](https://www.pexels.com/videos/).  
For example: [Mother and daughter with face masks at the park by Gustavo Fring from Pexels](https://www.pexels.com/video/mother-and-daughter-with-face-masks-at-the-park-4265036/).

### **IV. Configure via `.env`**

1. Create `.env` file from template:
```bash
cp .env.example .env
```

2. Edit `.env` in any text editor (e.g., `nano`, `VSCode`):
```bash
nano .env
```

3. Configure parameters: the file is divided into sections — modify values according to your needs. For example:

```bash
# === MODEL CONFIGURATION ===
MODEL_NAME=yolov8m-pose.pt
CONFIDENCE=0.8

# === VIDEO CONFIGURATION ===
VIDEO_NAME=example-pexels.mp4

# === DISPLAY SETTINGS ===
DISPLAY_WIDTH=1020
DISPLAY_HEIGHT=720

# === PATH CONFIGURATION ===
MODELS_DIR=models
VIDEOS_DIR=videos
```

### **V. Run the Application**

```bash
python -m app.main
```

## **License**

This project is licensed under the [BSD-3-Clause License](LICENSE).

> **Warning**  
> The project includes third-party components with separate licenses that may differ from BSD-3-Clause.  
> A complete list of dependency licenses is available in [THIRD_PARTY_LICENSES.md](SBOMs/THIRD_PARTY_LICENSES.md).

## **Development Tools**

The project uses the following tools for reproducibility and dependency management:

- [Micromamba](https://github.com/mamba-org/mamba), an ultra-fast implementation of [Conda](https://github.com/conda/conda) for creating isolated environments.
- [conda-lock](https://github.com/conda/conda-lock), a utility for generating [exact lock files](SBOMs/conda-linux-64-lock.yml) to guarantee identical environment recreation across systems.
- [pip-licenses](https://github.com/raimon49/pip-licenses), a utility for generating [THIRD_PARTY_LICENSES.md](SBOMs/THIRD_PARTY_LICENSES.md) with licenses of all conda dependencies.