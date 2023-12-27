from configparser import ConfigParser
import os

# 获取当前工作目录
app_dir: str = os.getcwd()

# 创建一个 ConfigParser 对象，读取配置
config: ConfigParser = ConfigParser()
config.read(os.path.join(app_dir, "config.ini"), encoding="u8")

# 配置项
mouse_speed: int = int(config.get("AppConfig", "mouse_speed"))  # 鼠标移动速度
x_offset: int = int(config.get("AppConfig", "x_offset"))  # x轴偏移值
y_offset: int = int(config.get("AppConfig", "y_offset"))  # y轴偏移值

# 模型配置
model_type: str = config.get("AppConfig", "model_type")  # 模型类型【n, x】，n识别速度快，精确度稍低；x识别速度稍慢，精确度高
model_path: str = os.path.join(app_dir, "models", f"yolov8{model_type}-pose.pt")

# 窗口配置
window_classname: str = config.get("AppConfig", "window_classname")  # 窗口类名