"""
第二界面
"""
from cocos import menu
from cocos.actions.base_actions import Repeat
import lib.floatingWindow as floatingWindow
import cocos
from cocos.director import director
from pyglet.window import mouse
from cocos.actions.interval_actions import MoveTo
import time 
from cocos.actions import *
import lib.mainScene as mainScene
atime = 0 
class backGrundIMG(cocos.layer.Layer):
    is_event_handler = True
    bgw = 0
    bgh = 0
    def __init__(self):
        super().__init__()
        bg = cocos.sprite.Sprite("GFX/backGrund/New_bg.jpg")
        self.bgw = bg.width
        self.bgh = bg.height
        bg.position = (self.bgw//2+500, self.bgh//2-400)
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
        
class mainMenu(cocos.menu.Menu):
    def __init__(self, title):
        super().__init__(title=title)

        self.position = 400, 0
        #定义菜单列表
        items_x = 100
        items_y = 200
        items = []
        #加入选项
        items.append(cocos.menu.MenuItem("窗口1", self.A))
        items[0].x = items_x
        items[0].y = items_y
        items.append(cocos.menu.MenuItem("窗口2", self.B))
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
    def A(self):
        pass
    def B(self):
        pass

    def changeScene(self):
        director.pop()

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


def updataTime():
    global atime
    atime = time.strftime("%H:%M:%S", time.localtime())
    return atime

def reset_scene_data():
    global updataSceneList, timeUI
    main_scene = cocos.scene.Scene()
    updataSceneList = [[backGrund,-100],[Cmenu, 1]]
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
    
    global updataSceneList, backGrund, timeUI, Cmenu

    updataSceneList = []
    backGrund = backGrundIMG()
    # timeUI = timeLog()
    Cmenu = mainMenu("控制面板")
    main_scene = reset_scene_data()
    return main_scene


