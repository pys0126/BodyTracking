import cv2
import os
import time
import platform
from torch import Tensor
from typing import Optional
from cv2 import VideoCapture
from ultralytics import YOLO
from cv2.typing import MatLike
from ultralytics.engine.results import Results
from config import model_path, window_classname
from ultralytics.engine.results import Keypoints
from threading import Thread
from utils import tensor_to_list, get_window_info_by_linux, capture_screen, move_mouse_by_window, draw_box_by_window

# 加载Yolo模型
model: YOLO = YOLO(model_path)

for source in capture_screen():
    frame: MatLike = cv2.imread(source)

    result: Results = model.predict(source=frame)[0]
    keypoints: Optional[Keypoints] = result.keypoints  # 关键点数据
    if not keypoints:
        continue
    confidence_tensor: Tensor = keypoints.conf  # 关键点关联的置信度对象
    xy_tensor: Tensor = keypoints.xy  # 关键点对象
    if not all([xy_list := tensor_to_list(xy_tensor), confidence_list := tensor_to_list(confidence_tensor)]):
        continue
    # 将所有头部关键点以及置信度保存到head_data_list，格式为[(1, 1), 0.98983]
    head_data_list: list = []
    for xy, confidence in zip(xy_list, confidence_list):
        x: int = int(xy[0][0])
        y: int = int(xy[0][1])
        head_data_list.append([(x, y), confidence[0]])

    # 置信度最高的头部关键点以及置信度数据
    max_head_data: list = max(head_data_list, key=lambda args: args[1])

    # 如果置信度小于0.7则跳过
    if max_head_data[1] < 0.7:
        continue

    # 读取图片将鼠标移动到图片中头部关键点位置
    center: tuple = max_head_data[0]  # 点的中心坐标
    radius: int = 3  # 点的半径
    color: tuple = (0, 255, 0)  # 点的颜色，这里使用绿色
    thickness: int = 2  # 线条宽度
    # # 框出来
    # cv2.rectangle(frame, (center[0] - 50, center[1] - 50), (center[0] + 50, center[1] + 50), color, thickness)
    # # 显示图像
    # cv2.imshow("Yolov8", frame)
    # # 等待键盘事件
    # cv2.waitKey(0)

    # 判断平台为Windows还是Linux，执行对应的窗口坐标获取
    if "windows" in platform.system().lower():
        # Windows获取窗口坐标
        window_pos: Optional[tuple] = (0, 0)
    else:
        # Linux获取窗口坐标
        window_pos: Optional[tuple] = get_window_info_by_linux(window_classname=window_classname)[:2]
        if not window_pos:
            print("请启动该窗口程序！")
            break
    # 移动鼠标
    move_mouse_by_window(window_xy=(window_pos[0], window_pos[1]), xy=center)
    # 绘制框
    Thread(target=draw_box_by_window, args=(window_pos[0], window_pos[1], center[0], center[1])).start()

# 释放资源
cv2.destroyAllWindows()
