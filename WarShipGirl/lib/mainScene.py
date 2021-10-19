"""
初始界面
"""
from cocos.actions.base_actions import Repeat
import pyglet
import lib.floatingWindow as floatingWindow
import cocos
from cocos.director import director
from pyglet.window import mouse
from cocos.actions.interval_actions import MoveTo
import time 
from cocos.actions import *

class backGrundIMG(cocos.layer.Layer):
    is_event_handler = True
    bgw = 0
    bgh = 0
    def __init__(self):
        super().__init__()
        bg = cocos.sprite.Sprite("GFX/backGrund/Main_light_bg_spring.png")
        self.bgw = bg.width
        self.bgh = bg.height
        bg.position = (self.bgw//2-200, self.bgh//2-200)
        self.add(bg)
        
    def on_mouse_motion(self, x, y, dx, dy):
        """
        动态背景
        """
        #print(x,y)
        winW = director.window.width
        winH = director.window.height
        needX = (((x/winW)*100)-50)
        needY = (((y/winH)*100)-50)+100
        #print(needX, needY)
        self.do(MoveTo((needX, needY), 0.10))

    def on_mouse_press(self, x, y, button, modifiers):
        print(x,y)
        #必须的两行，负责更新场景图层的前后顺序
        main_scene = reset_scene_data()
        director.replace(main_scene)
        
# class timeLog(cocos.layer.Layer):
#     def __init__(self):
#         super().__init__()
#         timeUi = cocos.sprite.Sprite("GFX/ui/timeUi.png")
#         timeUi.position = (1110, 685)
        

#         self.label = cocos.text.Label(
#             '',
#             font_size = 32,
#             anchor_x = "center",
#             anchor_y = "center",
#             color = (0,0,0,255)

#         )
#         self.label.position = (1110, 685)
#         self.add(timeUi)
#         self.add(self.label)
#         self.do(Repeat(Delay(0.1)+CallFunc(self.relrodTime)))
    
#     def relrodTime(self):
#         global atime
#         self.label.element.text = atime



#    def relrodTime(self):
 #       self.label.kwargs['text'] = "aa"
  #      print(self.label.kwargs['text'],'AAA')
   #     main_scene = reset_scene_data()
    #    print(main_scene)
     #   director.replace(main_scene)

class mainMenu(cocos.menu.Menu):
    def __init__(self, title):
        super().__init__(title=title)

        self.position = 400, 0
        #定义菜单列表
        items_x = 100
        items_y = 200
        items = []
        #加入选项
        items.append(cocos.menu.MenuItem("窗口1", self.window_1))
        items[0].x = items_x
        items[0].y = items_y
        items.append(cocos.menu.MenuItem("窗口2", self.window_2))
        items[1].x = items_x
        items[1].y = items_y
        items.append(cocos.menu.MenuItem("返回上级", self.changeScene))
        items[2].x = items_x
        items[2].y = items_y

        self.font_title['color'] = (0,0,0,255)
        self.font_item['color'] = (0,0,0,255)
        self.font_item_selected['color'] = (0,0,0,255)
        self.font_item_selected['font_size'] = 32


        self.create_menu(items)


    #这下面分别是不同窗口的开关控制函数
    def window_1(self):
        if new_window.visible == True:
            new_window.closeWindow()
        else:
            new_window.showWindow()

    def window_2(self):
        if new_window2.visible == True:
            new_window2.closeWindow()
        else:
            new_window2.showWindow()

    def changeScene(self):
        director.pop()


def updataTime():
    global atime
    atime = time.strftime("%H:%M:%S", time.localtime())
    return atime

def reset_scene_data():
    global updataSceneList, timeUI
    main_scene = cocos.scene.Scene()
    updataSceneList = [[backGrund,-100],[new_window, new_window.z],[new_window2, new_window2.z], [Menu, 1]]
    for i in updataSceneList:
        main_scene.add(i[0],z = i[1])
        #print(i[1])
    return main_scene

def get_scene():
    """
    说明：
        这是用来获取场景的函数
        return: cocos.scene.Scene对象
            返回所属场景文件的场景对象
    """
    main_scene = cocos.scene.Scene()
    
    global updataSceneList, backGrund, timeUI, new_window, new_window2, Menu

    updataSceneList = []
    backGrund = backGrundIMG()
    # timeUI = timeLog()
    Menu = mainMenu("控制面板")
    new_window = floatingWindow.createFloatWindowLayer(30, 103, 150, 200, "浮动窗口")
    new_window2 = floatingWindow.createFloatWindowLayer(30, 140, 150, 200, "浮动窗口")
    main_scene = reset_scene_data()
    return main_scene


