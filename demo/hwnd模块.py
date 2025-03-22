from typing import Tuple

import win32gui
import win32con
from win32con import SWP_NOMOVE,SWP_NOSIZE


def 根据标题枚举窗口句柄(目标窗口标题):
    hwnds,窗口句柄列表 = [],[]
    win32gui.EnumWindows(lambda 窗口句柄,参数:参数.append(窗口句柄),窗口句柄列表)
    for 窗口句柄 in 窗口句柄列表:
        标题 = win32gui.GetWindowText(窗口句柄)
        if 标题.find(目标窗口标题) >= 0:
            hwnds.append(窗口句柄)
    return hwnds
    
def 获取窗口句柄_标题(title):
    return win32gui.FindWindow(None, title)

def 设置窗口状态(hwnd,最大化=0,最小化=0,改变大小=0,大小=(1280,720),改变位置=0,位置=(346,186),全屏置顶=0,激活=0,位置大小=0,关闭窗口=0,置底=0):
    if hwnd:
        if 最大化:
            win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
        if 最小化:
            win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)
        if 改变大小:
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOP,0,0,大小[0],大小[1],win32con.SWP_NOMOVE)
        if 改变位置:
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOP,位置[0],位置[1],0,0,win32con.SWP_NOSIZE)
            print(f"窗口已移动到 ({位置[0]}, {位置[1]})")
        if 全屏置顶:
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOP,0,0,1920,1080,win32con.SWP_SHOWWINDOW)
            win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
        if 激活:
            win32gui.SetForegroundWindow(hwnd)
            win32gui.ShowWindow(hwnd,win32con.SW_SHOWNORMAL)
        if 位置大小:

            """
                血泪教学:
                win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)
                win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,346,186,1280,720,win32con.SWP_NOACTIVATE)
            
                win32con.HWND_TOPMOST：将窗口置于所有非顶级窗口之上（始终置顶）
                win32con.HWND_NOTOPMOST：将窗口置于非顶级窗口之下
                win32con.HWND_TOP：将窗口置于所有非顶级窗口之上，但不是始终置顶
                win32con.HWND_BOTTOM：将窗口置于所有非顶级窗口之下
                
                win32con.SWP_NOMOVE：不改变窗口的位置
                win32con.SWP_NOSIZE：不改变窗口的大小
                win32con.SWP_NOZORDER：不改变窗口的 Z 轴顺序
                win32con.SWP_NOACTIVATE：不激活窗口
                win32con.SWP_SHOWWINDOW：显示窗
                win32con.SWP_HIDEWINDOW：隐藏窗口
                win32con.SWP_FRAMECHANGED：强制窗口框架重新绘制
                win32con.SWP_NOREDRAW：不重绘窗口
                win32con.SWP_NOSENDCHANGING：不发送 WM_WINDOWPOSCHANGING 消息
                
            """
            win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOP,346,186,1280,720,win32con.SWP_NOACTIVATE)
            
            print(f"窗口已移动到 ({346}, {186})，大小为 {1280}x{720}。")
        if 置底:
            win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)
            win32gui.SetWindowPos(hwnd,win32con.HWND_BOTTOM,346,186,1280,720,win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)
        if 关闭窗口:
            win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
    else: print("句柄不存在!")

def 获取窗口xywh(hwnd)->tuple[int,int,int,int]:
    # 获取当前窗口的位置和大小
    左,上,右,下 = win32gui.GetWindowRect(hwnd)
    宽度,高度 = 右 - 左,下 - 上
    return 左,右,宽度,高度

def 获取窗口状态(hwnd,打印=1,obj=""):
    obj = win32gui.GetWindowPlacement(hwnd)
    if 打印:print(obj," ---函数名称:获取窗口状态()")
    if obj:return obj

if __name__ == '__main__':
    import time
    
    times = time.time()
    目标窗口标题 = r"大漠插件接口说明v7.2450"
    hwnd = 获取窗口句柄_标题(目标窗口标题)
    # hwnd = 根据标题枚举窗口句柄(目标窗口标题)[0]
    # time.sleep(1)
    # 设置窗口状态(hwnd,最大化=1)
    # time.sleep(1)
    # 设置窗口状态(hwnd,最小化=1)
    # time.sleep(1)
    # 设置窗口状态(hwnd,最大化=1)
    # time.sleep(1)
    # 设置窗口状态(hwnd,改变位置=1)
    # time.sleep(1)
    # 设置窗口状态(hwnd,改变大小=1,大小=(100,100))
    # time.sleep(1)
    # 设置窗口状态(hwnd,全屏置顶=1)
    
    设置窗口状态(hwnd,位置大小=1)
    
    