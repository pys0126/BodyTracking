from pyMeow import *

# while True:
#     pyMeow.begin_drawing()
#     pyMeow.draw_fps(10, 10)
#     print(pyMeow.draw_rectangle(100, 100, 100, 100, pyMeow.get_color("orange")))

# 列出所有活动进程
# for process in enum_processes():
#     print(process)

# 根据进程名称获取进程ID
process_id: str = get_process_id("QQ.exe")

process = open_process(process=process_id, debug=False)
for module in enum_modules(process):
    print(module)
