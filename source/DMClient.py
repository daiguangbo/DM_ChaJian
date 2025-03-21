# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/7 0:26
@Auth ： 大雄
@File ：client.py
@IDE ：PyCharm
@Email:3475228828@qq.com
@func:功能
"""

import json
import sys
import requests
import os
import json

class dm_client:
    实例字典 = {}

    def __init__(self, ip, prot, index=0):
        self.ip = ip
        self.prot = prot
        self.index = index

    def __new__(cls, ip, prot, index=0):
        key = (ip, prot, index)
        if key not in cls.实例字典:
            实例 = super(dm_client, cls).__new__(cls)
            # print(f'大漠对象{index}创建成功!!!')
            cls.实例字典[key] = 实例
        else:
            pass
            # print(f'大漠对象{index}返回成功')
        return cls.实例字典[key]
        
    def __getattribute__(self,item):
        ret = super().__getattribute__(item)
        if str(type(ret))=="<class 'function'>" or str(type(ret))=="<class 'method'>":
            global  temp
            temp = ret
            def res(*args):
                data = {
                    "dm_num":self.index,# 如果不写默认使用序号0
                    "func":str(temp.__name__),
                    "args":args,
                }
                return requests.post(f'http://{self.ip}:{self.prot}/login', json=data).json()
            return res
        else:
            return ret
    @staticmethod
    def GetDmCount():
        pass

    @staticmethod
    def FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        """在指定区域内查找图片"""
        pass

    @staticmethod
    def Capture(x1, y1, x2, y2, file):
        """捕获屏幕上的指定区域并保存为图片文件"""
        pass

    @staticmethod
    def Ver():
        """获取版本信息。"""
        pass

    @staticmethod
    def LeftClick():
        """模拟鼠标左键点击"""
        pass

    @staticmethod
    def Delay(num):
        """延时一定时间"""
        pass

    @staticmethod
    def MoveTo(x: int, y: int):
        """模拟鼠标移动到指定位置"""
        pass
    
    @staticmethod
    def RightClick():
        """模拟鼠标右键点击"""
        pass
    
    @staticmethod
    def FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, dir):
        """根据指定的多点查找颜色坐标"""
        pass

    @staticmethod
    def CaptureGif(x1, y1, x2, y2, file, delay, time):
        """捕获屏幕上的指定区域并保存为GIF动画文件"""
        pass
    
    @staticmethod
    def CmpColor(x, y, color, sim):
        """比较指定坐标的颜色与给定颜色的相似度"""
        pass
    
    @staticmethod
    def FindStr(x1, y1, x2, y2, string, color_format, sim):
        """在指定区域内查找指定颜色格式的字符串"""
        pass

    @staticmethod
    def Ocr(x1, y1, x2, y2, color_format, sim):
        """使用OCR技术识别指定区域内的文本"""
        pass
    
    @staticmethod
    def RunApp(app_path, mode):
        """运行指定的应用程序"""
        pass
    
    @staticmethod
    def GetID():
        pass
    
    @staticmethod
    def LeftDown():
        """模拟按住左键点击"""
        pass
    
    @staticmethod
    def LeftUp():
        """模拟按住左键点击"""
        pass
    
    @staticmethod
    def MoveR(rx,ry):
        """
        移动鼠标
        参数定义:
        rx: 鼠标移动的x轴偏移量
        ry: 鼠标移动的y轴偏移量
        """
    @staticmethod
    def EnableMouseAccuracy(enable):
        """鼠标精准度开关"""
    
    @staticmethod
    def WheelUp():
        """模拟鼠标滚轮向上"""
    
    @staticmethod
    def WheelDown():
        """模拟鼠标滚轮向下"""
        
        
        
        
    """按键操作合集: back-退格 space-空格 cap-大写  ctrl alt shift win tab esc enter up down leftright------------------------------------- """
    @staticmethod
    def KeyDownChar(key_str):
        """模拟键盘按住"""
        pass
    @staticmethod
    def KeyPressChar(key_str):
        """模拟键盘按下"""
        pass
    @staticmethod
    def KeyPressStr(key_str,delay):
        """模拟键盘输入字符串"""
        pass
    @staticmethod
    def KeyUpChar(key_str):
        """模拟键盘松开"""
        pass
    @staticmethod
    def GetCursorPos():
        """获取当前鼠标的位置"""
        pass
    
    
    """窗口操作"""
    @staticmethod # 枚举进程,按打开先后排序
    def EnumProcess(name):
        
        pass
    
    @staticmethod # 枚举系统中符合条件的窗口
    def EnumWindow(parent,title,class_name,filter):
        pass
        """函数简介:
                根据指定条件,枚举系统中符合条件的窗口,可以枚举到按键自带的无法枚举到的窗口
                函数原型:
                string EnumWindow(parent,title,class_name,filter)
                
                参数定义:
                parent 整形数: 获得的窗口句柄是该窗口的子窗口的窗口句柄,取0时为获得桌面句柄
                title 字符串: 窗口标题. 此参数是模糊匹配.
                class_name 字符串: 窗口类名. 此参数是模糊匹配.
                
                filter整形数: 取值定义如下
                1 : 匹配窗口标题,参数title有效
                2 : 匹配窗口类名,参数class_name有效.
                4 : 只匹配指定父窗口的第一层孩子窗口
                8 : 匹配父窗口为0的窗口,即顶级窗口
                16 : 匹配可见的窗口
                32 : 匹配出的窗口按照窗口打开顺序依次排列
                这些值可以相加,比如4+8+16就是类似于任务管理器中的窗口列表
                
                返回值:
                字符串 :返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"
                
                示例:
                hwnds = dm.EnumWindow(0,"QQ三国","",1+4+8+16)
                这句是获取到所有标题栏中有QQ三国这个字符串的窗口句柄集合
                hwnds = split(hwnds,",")
                转换为数组后,就可以处理了
                这里注意,hwnds数组里的是字符串,要用于使用,比如BindWindow时,还得强制类型转换,比如int(hwnds(0))
                """
                
    @staticmethod # 枚举指定进程下的窗口
    def EnumWindowByProcess(process_name,title,class_name,filter):
        pass

    @staticmethod # 移动窗口
    def MoveWindow(hwnd,x,y):
        pass
    
    @staticmethod #设置窗口的状态
    def SetWindowState(hwnd, flag):
        pass
        """
            hwnd (int): 指定的窗口句柄。
            flag (int): 窗口状态标志，取值定义如下：
                0: 关闭指定窗口
                1: 激活指定窗口
                2: 最小化指定窗口，但不激活
                3: 最小化指定窗口，并释放内存，但同时也会激活窗口
                4: 最大化指定窗口，同时激活窗口
                5: 恢复指定窗口，但不激活
                6: 隐藏指定窗口
                7: 显示指定窗口
                8: 置顶指定窗口
                9: 取消置顶指定窗口
                10: 禁止指定窗口
                11: 取消禁止指定窗口
                12: 恢复并激活指定窗口
                13: 强制结束窗口所在进程
                14: 闪烁指定的窗口
                15: 使指定的窗口获取输入焦点
        返回值:
            int: 操作结果，0 表示失败，1 表示成功。
        """
    @staticmethod
    def GetWindowState(hwnd,flag):#检测窗口属性
        pass
    
    
    
    """其他函数"""
    @staticmethod #蜂鸣器-频率&时长
    def Beep(f=2500,duration=1000):
        pass
    
    @staticmethod #获取剪贴板内容
    def GetClipboard():
        pass
    
    @staticmethod #获取显卡信息
    def GetDisplayInfo():
        pass
    
    @staticmethod #设置剪贴板内容
    def SetClipboard(value):
        pass
    
    @staticmethod #显示任务栏图标
    def ShowTaskBarIcon(hwnd,is_show):
        """is_show 整形数: 0为隐藏,1为显示"""
        pass
        
    @staticmethod # 获取注册在系统中的dm.dll的路径.
    def GetBasePath():
        pass
    
    """文件操作---------------------------------------------------------------------------------------------------------------------------"""
    @staticmethod # 下载文件
    def DownloadFile(url,save_file,timeout):
        pass
        """
            url 字符串: 下载的url地址.
            save_file 字符串: 要保存的文件名.
            timeout整形数: 连接超时时间，单位是毫秒.
        """
    
    
    """后台设置---------------------------------------------------------------------------------------------------------------------------"""
    @staticmethod
    def BindWindow(hwnd, display, mouse, keypad, mode): pass
    
    @staticmethod
    def BindWindowEx(hwnd, display, mouse, keypad, public, mode): pass
    
    @staticmethod
    def DownCpu(type, rate): pass
    
    @staticmethod
    def EnableBind(enable): pass
    
    @staticmethod
    def EnableFakeActive(enable): pass
    
    @staticmethod
    def EnableIme(enable): pass
    
    @staticmethod
    def EnableKeypadMsg(enable): pass
    
    @staticmethod
    def EnableKeypadPatch(enable): pass
    
    @staticmethod
    def EnableKeypadSync(enable, time_out): pass
    
    @staticmethod
    def EnableMouseMsg(enable): pass
    
    @staticmethod
    def EnableMouseSync(enable, time_out): pass
    
    @staticmethod
    def EnableRealKeypad(enable): pass
    
    @staticmethod
    def EnableRealMouse(enable, mousedelay, mousestep): pass
    
    @staticmethod
    def EnableSpeedDx(enable): pass
    
    @staticmethod
    def ForceUnBindWindow(hwnd): pass
    
    @staticmethod
    def GetBindWindow(): pass
    
    @staticmethod
    def GetFps(): pass
    
    @staticmethod
    def HackSpeed(rate): pass
    
    @staticmethod
    def IsBind(hwnd): pass
    
    @staticmethod
    def LockDisplay(lock): pass
    
    @staticmethod
    def LockInput(lock): pass
    
    @staticmethod
    def LockMouseRect(x1, y1, x2, y2): pass
    
    @staticmethod
    def SetAero(enable): pass
    
    @staticmethod
    def SetDisplayDelay(time): pass
    
    @staticmethod
    def SetDisplayRefreshDelay(time): pass
    
    @staticmethod
    def SetInputDm(dm_id, rx, ry): pass
    
    @staticmethod
    def SwitchBindWindow(hwnd): pass
    
    @staticmethod
    def UnBindWindow(): pass
    
    
    
    
    
    
    @staticmethod
    def ClientToScreen(hwnd,x,y):pass
    
    @staticmethod
    def GetLastError():pass
    
    @staticmethod
    def EnumWindowSuper(spec1,flag1,type1,spec2,flag2,type2,sort):pass

    
    
    
    

