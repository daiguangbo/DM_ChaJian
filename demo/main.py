import win32gui
import win32con
from win32con import SWP_NOSIZE


def 根据标题枚举窗口句柄(目标窗口标题):
    hwnds,窗口句柄列表 = [],[]
    win32gui.EnumWindows(lambda 窗口句柄,参数:参数.append(窗口句柄),窗口句柄列表)
    for 窗口句柄 in 窗口句柄列表:
        标题 = win32gui.GetWindowText(窗口句柄)
        if 标题.find(目标窗口标题) >= 0:
            hwnds.append(窗口句柄)
    return hwnds


def 设置窗口状态(hwnd,最大化=0,最小化=0,改变大小=0,大小=(1280,720),改变位置=0,位置=(346,186),全屏置顶=0,激活=0,位置大小=0,关闭窗口=0):
    # if 最大化:
    # win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)
    if hwnd:
        if 最大化:
            win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
        if 最小化:
            win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)
        if 改变大小:
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOP,0,0,大小[0],大小[1],win32con.SWP_NOMOVE)
        if 改变位置:
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOP,位置[0],位置[1],0,0,win32con.SWP_NOSIZE)
        if 全屏置顶:
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOP,0,0,1920,1080,win32con.SWP_SHOWWINDOW)
            win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
        if 激活:
            win32gui.SetForegroundWindow(hwnd)
            win32gui.ShowWindow(hwnd,win32con.SW_SHOWNORMAL)
        if 位置大小:
            win32gui.SetForegroundWindow(hwnd)
            win32gui.ShowWindow(hwnd,win32con.SW_SHOWNORMAL)
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,346,186,1280,720,win32con.SWP_NOACTIVATE)
            win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)
        if 关闭窗口:
            win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
    else: print("句柄不存在!")

def 获取窗口状态(hwnd):
    return win32gui.GetWindowPlacement(hwnd)




if __name__ == '__main__':
    import time
    
    times = time.time()
    目标窗口标题 = r"大漠插件接口说明v7.2450"
    hwnd = 根据标题枚举窗口句柄(目标窗口标题)[0]
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
