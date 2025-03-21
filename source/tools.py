import os
import PIL
import time
import subprocess
import win32gui
import base64
import requests
import json
from pynput.mouse import Controller
import win32con
def 截图(path,是否截取全屏=1,x=0,y=0,w=1280,h=720):
    """
    :param path:填写需要保存图片的路径
    :return 依赖模块from PIL import ImageGrab
    """
    if 是否截取全屏:
        screenshot = PIL.ImageGrab.grab()
        screenshot.save(path)
        return
    else:
        bbox = (x,y,w,h)  # (左上角x, 左上角y, 右下角x, 右下角y)
        region_screenshot = PIL.ImageGrab.grab(bbox=bbox)
        region_screenshot.save(path)

def 打开软件并将窗口置于前台(path=0,windos_text=0,是否最大化=0):
    """
        使用范例:打开软件并将窗口置于前台(r"D:\App\ToDesk_Daas\ToDesk_Daas.exe","ToDesk云电脑")
        函数原理:os模块打开软件后循环查找标题为指定文本的窗口,然后抓取句柄,觉得是否最大化,会阻塞进程
        依赖模块:import os,win32gui,time
    """
    os.system(path)
    while True:
        hwnd = win32gui.FindWindow(None,windos_text)
        if hwnd: print("软件成功运行,句柄&标题:",hwnd,"&",windos_text);win32gui.BringWindowToTop(hwnd);break
        else: print("未找到指定标题的窗口")
        time.sleep(0.5)
    if 是否最大化:
        win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
    else:
        win32gui.ShowWindow

def 打开网页(url):
    os.system(r"C:\Users\Administrator\Desktop\360浏览器X.lnk " + url)






























"""----------分割线----------"""
import subprocess


def 执行终端命令(command,是否打印=0):
    result = subprocess.run(["powershell","-Command",command],shell=True,capture_output=True,text=True,encoding="gbk",errors="replace")
    # 检查命令是否成功执行
    if result.returncode == 0:
        print("命令执行成功，输出如下：")
        if 是否打印: print(result.stdout)  # 打印标准输出
        return result.stdout
    else:
        print("命令执行失败，错误信息如下：")
        print(result.stderr)  # 打印标准错误
        return False
def 识别滑动验证码(path):
    """path:图片路径"""
    token = "hqQEOIM1_HUKLas-IM3GC7qVF8-lAXhUFULONsx8Dsg"  # 用户中心Token
    
    """读取图片并转换为 Base64 字符串"""
    with open(path,"rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    
    """发送 POST 请求到接口"""
    headers = {
        "Content-Type":"application/json"
    }
    data = {
        "image":image_base64,
        "token":token,
        "type":"22222",
        "extra":False
    }
    response = requests.post("http://api.jfbym.com/api/YmServer/customApi",headers=headers,data=json.dumps(data))
    
    if response.json()["msg"] == "识别成功":
        return response.json()["data"]["data"]
    else:
        return False

    # x = 识别滑动验证码(r"360截图184307011079995.png")
    # if x: print("识别成功,返回相距像素大小:",x)
    # else: print("识别失败")


def 鼠标滚轮(x=0,y=0):
    mouse = Controller()
    mouse.scroll(x,y)


def 确认DM插件后台服务端运行(cmd窗口是否显示=0):
    窗口标题 = r"C:\Users\ADMINI~1\Desktop\DM-server\PY32\python.exe"
    服务端运行脚本路径 = r"C:\Users\Administrator\Desktop\DM-server\start.bat"
    hwnd = win32gui.FindWindow(None,窗口标题)
    if hwnd:
        print("DM插件后台服务端正在运行,句柄:",hwnd)
        print()
        if not cmd窗口是否显示:win32gui.ShowWindow(hwnd,win32con.SW_HIDE)#隐藏窗口
        else:win32gui.ShowWindow(hwnd,win32con.SW_SHOW)#显示窗口
        return
    else:
        print("DM插件后台服务端未运行")
        subprocess.Popen(服务端运行脚本路径)
    print("服务端启动中...",end="")
    while True:
        hwnd = win32gui.FindWindow(None,窗口标题)
        if hwnd:
            print("服务端成功运行,句柄:",hwnd);time.sleep(0.5)
            if not cmd窗口是否显示: win32gui.ShowWindow(hwnd,win32con.SW_HIDE)  #隐藏窗口
            else: win32gui.ShowWindow(hwnd,win32con.SW_SHOW)  #显示窗口
            break
        else: pass

    

def 识别图片验证码(path):
    """path:图片路径"""
    token = "hqQEOIM1_HUKLas-IM3GC7qVF8-lAXhUFULONsx8Dsg"  # 用户中心Token
    url = "http://api.jfbym.com/api/YmServer/customApi"  # 请求地址

    """读取图片并转换为 Base64 字符串"""
    with open(path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    """发送 POST 请求到接口"""
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "image": image_base64,
        "token": token,
        "type": "30009"  # 根据文档，type 应为 "30009"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    """解析返回结果"""
    response_data = response.json()
    if response_data["code"] == 10000:  # 识别成功
        return response_data["data"]["data"]
    else:
        print(f"识别失败，错误信息：{response_data['msg']}")
        return False













































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
