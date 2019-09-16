"""
Python3
用于判断日志中，出现次数大于特定量的IP
"""
import sys
import re
# import termcolor
from colorama import init, Fore


# 获取日志文件路径
file = sys.argv[1]
# file = "C:\\Users\\chengziyang\\Desktop\\access.log"
# autoreset参数为True时只对当前输出起作用，输出完成后颜色恢复默认设置
init(autoreset=True)
print(Fore.GREEN + ">>>>>>>>>>>>>>>>>>>>>开始分析<<<<<<<<<<<<<<<<<<<<<<", "\n")
# 读取日志
with open(file, "r") as lines:
    count = 1
    for line in lines:
        print((Fore.GREEN + ("第%d行:" % count)), line)
        # print(re.split)
        count = count + 1
print(Fore.GREEN + str(count))
