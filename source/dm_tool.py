# -*- coding: utf-8 -*-

# @PyCharm：2024.2.1
# @Python：3.11
# @项目：dm插件模板

# @文件：dm_tool.py
# @时间：2025/3/20 19:11
# @作者：LexiSiy
# @邮箱：2172500693@163.com

import time
from source import DMClient

dm = DMClient.dm_client("127.0.0.1", "9000", 0)
def 左键点击(x=0,y=0,延迟=200):
    dm.Delay(延迟)
    if x != 0 and y != 0:
        dm.MoveTo(x,y)
    dm.LeftClick()
    
def 提取颜色和坐标(str):
    # 分割输入字符串,提取坐标和颜色
    parts = str.split()
    坐标 = parts[0].split(',')
    x,y = int(坐标[0]),int(坐标[1])
    
    # 调整顺序为 RGB
    color = parts[1]
    color = color[4:6] + color[2:4] + color[0:2]
    return {
        "x":x,
        "y":y,
        "color":color
    }


def 提取颜色和坐标_aa(str):
    # 分割输入字符串,提取坐标和颜色
    parts = str.split()
    坐标 = parts[0].split(',')
    x,y = int(坐标[0]),int(坐标[1])
    
    # 调整顺序为 RGB
    color = parts[1]
    color = color[4:6] + color[2:4] + color[0:2]
    return x,y

def 单点找色_前台(arr: dict,相似度=0.9,备注="",是否打印=1):
    result = dm.CmpColor(arr["x"],arr["y"],arr["color"],相似度)
    if result['value']:
        if 是否打印:print("未找到:",备注)
        return False
    else:
        print("找到!",备注,end="")
        return True

def 找色循环(text,回调函数=None,是否移动鼠标=False,单次找色=False,点击并移动=False,查找时长=10,备注=""):
    arr = 提取颜色和坐标(text)
    
    if 点击并移动:
        是否移动鼠标,回调函数 = True,lambda:左键点击(arr['x'],arr['y'],200)
    if 是否移动鼠标:dm.MoveTo(arr["x"],arr["y"])
    if 单次找色:return 单点找色_前台(arr,备注=备注)
    
    time_找色时长 = time.time()
    time_打印频率 = time.time()
    
    while True:
        time_new = time.time()
        if time_new - time_找色时长 > 查找时长:return
        if time_new - time_打印频率 >= 1:
            if 单点找色_前台(arr,备注=备注,是否打印=True):break
            time_打印频率 = time.time()
        else:
            if 单点找色_前台(arr,备注=备注,是否打印=False):break
    
    if 回调函数 == 1:左键点击(arr['x'],arr['y'],200)
    elif 回调函数:回调函数()
    


def 查找窗口标题(title=r"C:\Users\ADMINI~1\Desktop\python\DM-server\.venv\Scripts\python.exe")->list[int]:
    #匹配出的窗口按照窗口打开顺序依次排列
    keep = dm.EnumWindow(0,title,"",1 + 32)
    hwld_LIST: list = keep['value'].split(",")
    return [int(k) for k in hwld_LIST if k != ""]

def 组合按键(a="win",b="d"):
    dm.KeyDownChar(a)
    dm.KeyPressChar(b)
    dm.KeyUpChar(a)

def 等待程序打开并激活窗口(title="ToDesk云电脑",窗口状态=1)->int:
    while True:
        hwld_todesk = 查找窗口标题(title)
        if hwld_todesk:
            dm.SetWindowState(hwld_todesk[-1],窗口状态)
            return hwld_todesk[-1]

def 找色循环_多次点击(text,点击次数=5):
    arr = 提取颜色和坐标坐标(text)
    for k in range(点击次数):
        if 单点找色_前台(arr):return
        else:左键点击(arr['x'],arr['y'],200)

def 最大化窗口(hwld):
    dm.SetWindowState(hwld,1)
    dm.SetWindowState(hwld,4)

def 窗口绑定dm对象(dms, hwnd, display="dx2", mouse="dx.mouse.raw.input|dx.mouse.position.lock.message", keypad="windows", public="dx.public.graphic.protect", mode=0):
    """
    绑定指定窗口到大漠对象。

    :param dm: 大漠对象实例
    :param hwnd: 窗口句柄列表，第一个元素为需要绑定的窗口句柄
    :param display: 屏幕颜色获取方式，默认值为 "normal"
    :param mouse: 鼠标仿真模式，默认值为 "windows3" #TODO dx.mouse.raw.input
    :param keypad: 键盘仿真模式，默认值为 "windows"
    :param public: 公共属性，默认值为 "dx.public.graphic.protect"
    :param mode: 绑定模式，默认值为 0
    :return: None
    """
    # print(dms.BindWindowEx(hwnd, display, "dx.mouse.raw.input|dx.mouse.position.lock.message", keypad, public, mode),窗口绑定dm对象.__name__)
    print(dms.BindWindowEx(hwnd,display, "dx.mouse.position.lock.api|dx.mouse.position.lock.message|dx.mouse.state.message", keypad,public, 0),窗口绑定dm对象.__name__)
    
def 获取函数名称(func):
    return " ---函数名称:" + func.__name__ + "()"

def 判断窗口是否后台绑定(hwnd):
    re = dm.IsBind(hwnd)
    if re['value'] == 0:
        print("窗口未绑定")
        return False
    else:
        print("窗口后台已被绑定")
        return True

def 枚举窗口_程序标题_子类名(标题,类名)->list:
    hwnds = dm.EnumWindowSuper(标题,8,1,类名,2,1,0)
    if hwnds['value']:
        print("找到句柄:",hwnds['value'],获取函数名称(枚举窗口_程序标题_子类名))
        return hwnds['value'].split(',')
    else:
        print("未找到句柄: ",获取函数名称(枚举窗口_程序标题_子类名))
        return []
def 枚举窗口_父句柄_子类名(句柄,类名)->list:
    hwnds = dm.EnumWindowSuper(句柄,4,1,类名,2,1,0)
    if hwnds['value']:
        print("找到句柄:",hwnds['value'],获取函数名称(枚举窗口_父句柄_子类名))
        return hwnds['value'].split(',')
    else:
        print("未找到句柄: ",获取函数名称(枚举窗口_父句柄_子类名))
        return []









"""封装函数部分----------------------------------------------------------------------------------------------------------------------------"""


import ctypes
import os

from win32com.client import Dispatch

# =============================
对象 = None


# 免注册调用大漠方法2
def 注册大漠_简(注册码='', 附加码=''):
    print('正在初始化')
    #  通过调用DmReg.dll注册大漠 这样不会把dm.dll写到系统中，从而实现免注册
    patch = ctypes.windll.LoadLibrary(os.path.dirname(__file__) + './DmReg.dll')
    patch.SetDllPathW(os.path.dirname(__file__) + './dm.dll', 0)
    dm_主对象 = Dispatch('dm.dmsoft')  # 创建对象
    ver = dm_主对象.ver()
    print('免注册调用初始化成功 版本号为:', ver)
    # 注册大漠VIP
    if ver != '':
        reg = dm_主对象.reg(注册码, 附加码)
        if reg == 1:
            print("大漠vip注册成功")
            return dm_主对象
        else:
            print(f"大漠注册失败,错误代码: {reg}")

# =================================
def 创建大漠对象(要创建的个数):
    '''
	这里是应对多线程 创建多个对象.返回的是列表类型
	如:
	dll = dm.注册大漠_简('注册码','附加码')
objects = dm.创建大漠对象(3) #创建三个对象
for i in objects:
	id = dm.取大漠对象ID(i)
	print(i,id)
	:param 要创建的个数:
	:return: 返回对象列表
	'''
    dms = []
    a = 0
    for i in range(要创建的个数):
        dms.append(Dispatch('dm.dmsoft'))  # 创建对象)
        a += 1
    return dms

def 取创建的大漠对象总数():
    '''
	:param 对象:
	:return: 返回所有的大漠对象个数
	'''
    return 对象.GetDmCount()
def 窗口_查找(类名='', 标题=''):
    return 对象.FindWindow(类名, 标题)
def 窗口_枚举(parent, title, class_name, filter):
    return 对象.EnumWindow(parent, title, class_name, filter)
def 窗口_绑定Ex(hwnd, display, mouse, keypad, public, mode=int):
    return 对象.BindWindowEx(hwnd, display, mouse, keypad, public, mode)
def 窗口_绑定(hwnd, display, mouse, keypad, mode=int):
    return 对象.BindWindow(hwnd, display, mouse, keypad, mode)
def 窗口_绑定判断(hwnd):
    return 对象.IsBind(hwnd)
def 窗口_解绑(对象):
    return 对象.UnBindWindow()
def 窗口_取鼠标所在窗口句柄():
    return 对象.GetMousePointWindow()
def 鼠标_模拟鼠标真实移动开关(开关, 间隔, 距离):
    return 对象.EnableRealMouse(开关, 间隔, 距离)
def 鼠标_鼠标移动(x, y):
    return 对象.MoveTo(x, y)
def 鼠标_鼠标右键单击():
    return 对象.RightClick()
def 鼠标_鼠标左键单击():
    return 对象.LeftClick()
def 鼠标_鼠标移动点击(x, y):
    鼠标_鼠标移动(x, y)
    随机延时(10, 100)
    鼠标_鼠标左键单击()
def 键盘_按键(键码):
    return 对象.KeyPress(键码)
def 键盘_输入文本(字符串):
    return 对象.KeyPressStr(字符串)
def 键盘_文本输入(字符串):
    return 对象.KeyPressChar(字符串)
def 键盘_按住_字符(键码):
    return 对象.KeyDownChar(键码)
def 键盘_弹起_字符(键码):
    return 对象.KeyUpChar(键码)

def 鼠标_置前台鼠标模拟方式(模式):
    '''除了模式3,其他模式同时支持32位系统和64位系统.模式: 0
    正常模式(默认模式) 1 硬件模拟 2 硬件模拟2(ps2) 3 硬件模拟3'''
    return 对象.SetSimMode(模式)
def 随机延时(最小, 最大):
    return 对象.Delays(最小, 最大)
def 图色_找图(x1, y1, x2, y2, pic_name, delta_color, sim, dir):
    return 对象.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, '', '')
def 图色_多点找色(x1, y1, x2, y2, first_color, offset_color, sim, dir):
    return 对象.FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, dir, '', '')
def 图色_取色_RGB(x, y):
    '''获取(x,y)的颜色,颜色返回格式"RRGGBB"'''
    return 对象.GetColor(x, y)
def 图色_取区域里指定颜色(x1, y1, x2, y2, color, sim, dir):
    return 对象.FindColorEx(x1, y1, x2, y2, color, sim, dir)
def 图色_取区域里的指定颜色返回序号_取颜色坐标(colors, colors_序号):
    return 对象.GetResultPos(colors, colors_序号)
def 截图(x1, y1, x2, y2, file):
    return 对象.Capture(x1, y1, x2, y2, file)
def 识字(x1, y1, x2, y2, color_format, sim):
    '''识别屏幕范围(x1,y1,x2,y2)内符合color_format的字符串,并且相似度为sim 取值0.1-1'''
    return 对象.Ocr(x1, y1, x2, y2, color_format, sim)
def 找字_fastExS(x1, y1, x2, y2, string, color_format, sim):
    '''返回多个字符串的坐标
	此函数比FindStrExS要快很多，尤其是在字库很大时，或者模糊识别时，效果非常明显。
    推荐使用此函数。
    
    另外由于此函数是只识别待查找的字符，所以可能会有如下情况出现问题。
    
    比如 字库中有"张和三" 一共3个字符数据，然后待识别区域里是"张和三",如果用FindStrExS查找
    "张三"肯定是找不到的，但是用FindStrFastExS却可以找到，因为"和"这个字符没有列入查找计划中
    所以，在使用此函数时，也要特别注意这一点。'''
    return 对象.FindStrFastExS(x1, y1, x2, y2, string, color_format, sim)
def 找字_fastS(x1, y1, x2, y2, string, color_format, sim, intX, intY):
    '''返回找到的字符串. 没找到的话返回长度为0的字符串'''
    return 对象.FindStrFastS(x1, y1, x2, y2, string, color_format, sim, intX, intY)
def 置全局路径(路径):
    return 对象.SetPath(路径)
def 置字库路径(序号, 文件名):
    return 对象.SetDict(序号, 文件名)
def a星_取指定坐标最近坐标(all_pos, type, 指定x, 指定y):
    '''
	:param 指定y:
	:param 指定x:
	:param all_pos:
	:param ints:取值为0或者1 如果all_pos的内容是由FindPicEx,FindStrEx,FindStrFastEx,FindStrWithFontEx返回，那么取值为0
	如果all_pos的内容是由FindColorEx, FindMultiColorEx,FindColorBlockEx返回，那么取值为1
	:param x:
	:param y:
	:return:
	'''
    return 对象.FindNearestPos(all_pos, type, 指定x, 指定y)
def a星坐标排序(all_pos, type, x, y):
    '''
	根据部分Ex接口的返回值，然后对所有坐标根据对指定坐标的距离(或者指定X或者Y)进行从小到大的排序.
	注意:如果x为65535并且y为0时，那么排序的结果是仅仅对x坐标进行排序,如果y为65535并且x为0时，那么排序的结果是仅仅对y坐标进行排序.
	:param all_pos:
	:param type:
	:param x: 为0 则以y坐标排序
	:param y:为0 则以x坐标排序
	:return:
	'''
    return 对象.SortPosDistance(all_pos, type, x, y)











