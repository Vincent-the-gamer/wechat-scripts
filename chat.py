import time
from core import WeChat

wx = WeChat()

def chat(who: str):
    wx.GetSessionList()  # 获取会话列表
    wx.ChatWith(who)  # 打开`who`聊天窗口
    temp_msg = ''
    while True:
        try:
            friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
            if receive_msg != temp_msg and receive_msg.startswith("/ai"):
                """
                条件：
                朋友名字正确:(friend_name == who)
                不是上次的对话:(receive_msg != temp_msg)
                """
                temp_msg = receive_msg

                wx.SendMsg("as")  # 向`who`发送消息
        except:

            wx.SendMsg("出错啦！")  # 向`who`发送消息


chat("")
