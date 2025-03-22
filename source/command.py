# -*- coding: utf-8 -*-

# @PyCharm：2024.2.1
# @Python：3.11
# @项目：DM后台

# @文件：command.py
# @时间：2025/3/22 20:59
# @作者：LexiSiy
# @邮箱：2172500693@163.com
from source import DMClient
from demo import hwnd模块

def 获取函数名称(func):
    return " ---函数名称:" + func.__name__ + "()"
def 判断窗口是否后台绑定(dm,hwnd):
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
def 后台绑定窗口模式组合(dm,组合索引=0,打印=1):
    if 组合索引==0:
        obj = dm.BindWindowEx(hwnd,"dx2","windows3","dx.keypad.input.lock.api|dx.keypad.state.api|dx.keypad.api","dx.public.graphic.protect",0)
        if 打印: print(obj,获取函数名称(后台绑定窗口模式组合))
    if 组合索引==1:pass
    
"""封装DM函数-----------------------------------------------------------------------------------------------------------------------------"""
def 后台_设置截图等待时长(dm,tiem=2000,打印=1):
    obj = dm.SetDisplayDelay(tiem)
    if 打印:print(obj,获取函数名称(后台_设置截图等待时长))
    
def 后台_解除窗口绑定(dm,打印=1):
    obj = dm.UnBindWindow()
    if 打印:print(obj,获取函数名称(后台_解除窗口绑定))
    
def 后台_禁止外部输入(dm,参数,打印=1):
    "0关闭 1开启 2键盘 3鼠标 4and5"
    obj = dm.LockInput(参数)
    if 打印:print(obj,获取函数名称(后台_禁止外部输入))
    if 参数 != 0 :print("注意您开启了后台_禁止外部输入,记得操作完恢复外部输入!")
    
def 后台_返回dm对象绑定的窗口句柄(dm,打印=1):
    obj = dm.GetBindWindow()
    if 打印:print(obj,获取函数名称(后台_返回dm对象绑定的窗口句柄))
    
def 后台_强制解绑窗口(dm,hwnd,打印=1):
    obj = dm.ForceUnBindWindow(hwnd)
    if 打印:print(obj,获取函数名称(后台_强制解绑窗口))

def 后台_鼠标真实模拟(dm,模式,移动时间,移动速度,打印=1):
    """dm.EnableRealMouse 1,20,30 ;0关闭 1开启直线 2随机曲线 3小弧曲线 4大弧曲线"""
    obj = dm.EnableRealMouse(模式,移动时间,移动速度)
    if 打印:print(obj,获取函数名称(后台_鼠标真实模拟))

def 后台_按键真实模拟(dm,参数,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableRealKeypad(参数)
    if 打印:print(obj,获取函数名称(后台_按键真实模拟))
    
def 后台_设置是否鼠标同步点击(dm,参数,等待超时,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableMouseSync(参数,等待超时)
    if 打印:print(obj,获取函数名称(后台_设置是否鼠标同步点击))
    
def 后台_设置是否键盘同步点击(dm,参数,等待超时,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableKeypadSync(参数,等待超时,打印=1)
    if 打印:print(obj,获取函数名称(后台_设置是否键盘同步点击))

def 后台_DX模式鼠标关闭Windows消息(dm,参数,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableMouseMsg(参数)
    if 打印:print(obj,获取函数名称(后台_DX模式鼠标关闭Windows消息))
    
def 后台_DX模式键盘关闭Windows消息(dm,参数,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableKeypadMsg(参数)
    if 打印:print(obj,获取函数名称(后台_DX模式键盘关闭Windows消息))

def 后台_窗口假激活(dm,参数,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableFakeActive(参数)
    if 打印:print(obj,获取函数名称(后台_窗口假激活))

def 后台_临时关闭后台模式(dm,参数,打印=1):
    """参数:0全关 1恢复"""
    obj = dm.EnableBind(enable)
    if 打印: print(obj,获取函数名称(后台_临时关闭后台模式))


    

if __name__ == '__main__':
    dm = DMClient.dm_client("127.0.0.1", "9000", 0)
    dm1 = DMClient.dm_client("127.0.0.1", "9000", 1)
    hwnd = hwnd模块.获取窗口句柄_标题("大漠插件接口说明v7.2416")
    EnableRealMouse(enable,mousedelay,mousestep)
    
    后台_解除窗口绑定(dm)
    后台_设置截图等待时长(dm)
    后台_禁止外部输入(dm,1)
    后台_禁止外部输入(dm,0)
    判断窗口是否后台绑定(dm,hwnd=hwnd)
    
    
