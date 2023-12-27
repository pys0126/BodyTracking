# 基于YoloV8的人体追踪程序

## 安装环境

- 推荐`Python>=3.8`
- 推荐使用`python -m venv venv`创建虚拟环境
- 安装[CUDA11.7](https://developer.nvidia.com/cuda-toolkit-archive)
- 安装PyTorch（Linux略过此步）：`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117`
- 安装依赖`pip install -r requirements.txt`

## 运行

- 执行命令：`python main.py `

## 模型下载

- yolov8n-pose.pt（已在`models`目录中）
- [yolov8x-pose.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt)（下载后放入`models`目录中）