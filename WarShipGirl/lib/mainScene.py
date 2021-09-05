"""
初始界面
"""
from cocos.actions.base_actions import Repeat
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
        
class timeLog(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        timeUi = cocos.sprite.Sprite("GFX/ui/timeUi.png")
        timeUi.position = (1110, 685)
        

        self.label = cocos.text.Label(
            '',
            font_size = 32,
            anchor_x = "center",
            anchor_y = "center",
            color = (0,0,0,255)

        )
        self.label.position = (1110, 685)
        self.add(timeUi)
        self.add(self.label)
        self.do(Repeat(Delay(0.1)+CallFunc(self.relrodTime)))
    
    def relrodTime(self):
        global atime
        self.label.element.text = atime



#    def relrodTime(self):
 #       self.label.kwargs['text'] = "aa"
  #      print(self.label.kwargs['text'],'AAA')
   #     main_scene = reset_scene_data()
    #    print(main_scene)
     #   director.replace(main_scene)

class mainMenu(cocos.menu.Menu):
    pass


def updataTime():
    global atime
    atime = time.strftime("%H:%M:%S", time.localtime())
    return atime

def reset_scene_data():
    global updataSceneList, timeUI
    main_scene = cocos.scene.Scene()
    updataSceneList = [[backGrund,-100],[timeUI,1]]
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
    
    global updataSceneList, backGrund, timeUI, new_window2, new_window3, mainMenu

    updataSceneList = []
    backGrund = backGrundIMG()
    timeUI = timeLog()
    #mainMenu = mainManu("主面板")

    main_scene = reset_scene_data()
    return main_scene


