# **Silhouette Tracker: Real-Time Human Pose Estimation via YOLOv8 with CUDA Acceleration**

Система отслеживания человеческих поз в реальном времени с использованием **YOLOv8** и аппаратного ускорения **NVIDIA CUDA**. Проект реализован в изолированном окружении на базе **Conda** для обеспечения воспроизводимости и переносимости.

> **Примечание**:  
Это учебный проект, направленный на демонстрацию современных рабочих процессов компьютерного зрения и ускорения CUDA, а не на создание производственной системы отслеживания.

## **Предварительные требования**

1. **ОС:** Linux x86_64.
2. **Менеджер пакетов python:** Conda (Anaconda, Miniconda, Mamba или Micromamba).
3. **NVIDIA CUDA:** версия CUDA должна быть 12.6.3 или выше, а также должны быть установлены соответствующие драйверы NVIDIA.

## **Структура проекта**

```bash
.
├──.env.example # Шаблон конфигурации
├── SBOMs/      # Метаданные зависимостей
├── app/        # Исходный код приложения
├── models/     # Модели YOLOv8 для работы
└── videos/     # Видео для работы
```

## **Инструкция по установке и запуску**

### **I. Клонирование репозитория**

```bash
git clone https://github.com/Sierra-Arn/silhouette-tracker-python.git
cd silhouette-tracker-python
```

### **II. Создание и активация виртуальной среды**

```bash
conda env create -p ./.venv -f SBOMs/conda-linux-64-lock.yml
conda activate ./.venv
```

### **III. Подготовка данных**

Модели и видео не включены в репозиторий из-за ограничений размера. Чтобы скачать модели выполните следующие команды:

```bash
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n-pose.pt && \
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s-pose.pt && \
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8m-pose.pt && \
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8l-pose.pt && \
wget -P models/ https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8x-pose.pt
```

В директорию `videos` Вы можете добавить любое видео. В качестве демонстрации, Вы можете скачать видео с сайта [Pexels Free Stock Videos](https://www.pexels.com/videos/).  
Например, [Mother and daughter with face masks at the park by Gustavo Fring from Pexels](https://www.pexels.com/video/mother-and-daughter-with-face-masks-at-the-park-4265036/).

### **IV. Настройка конфигурации через `.env`**

1. Создайте файл `.env` из шаблона:
```bash
cp .env.example .env
```

2. Отредактируйте `.env` в любом текстовом редакторе (например, `nano`, `VSCode`):
```bash
nano .env
```

3. Настройте параметры: файл разделен на секции — измените значения в соответствии с Вашими задачами. Например:

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

### **V. Запуск приложения**

```bash
python -m app.main
```

## **Лицензия**

Проект распространяется под лицензией [BSD-3-Clause](LICENSE). 

> **Внимание**  
> Проект включает сторонние компоненты с отдельными лицензиями, которые могут отличаться от BSD-3-Clause.  
> Полный список лицензий зависимостей доступен в файле [THIRD_PARTY_LICENSES.md](SBOMs/THIRD_PARTY_LICENSES.md).

## **Инструменты разработки**
Проект использует следующие инструменты для обеспечения воспроизводимости и управления зависимостями:

- [Micromamba](https://github.com/mamba-org/mamba), ультрабыстрая реализация [Conda](https://github.com/conda/conda) для создания изолированных окружений.
- [conda-lock](https://github.com/conda/conda-lock), утилита для генерации [точного lock-файла](SBOMs/conda-linux-64-lock.yml) для гарантии идентичного воссоздания окружения на любых системах.
- [pip-licenses](https://github.com/raimon49/pip-licenses), утилита для генерации файла [THIRD_PARTY_LICENSES.md](SBOMs/THIRD_PARTY_LICENSES.md) с лицензиями всех conda-зависимостей.
