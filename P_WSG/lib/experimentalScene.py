"""
文件名：实验性菜单与浮动窗口场景(experimentalScene.py)\n
介绍：
本文件为实验性的场景创建文件。\n
包含：
    一个菜单（menu）对象\n
    三个浮动窗口与其控制菜单选项
"""

from cocos import menu
import lib.floatingWindow as floatingWindow
from cocos.director import director
import cocos
from pyglet.window import mouse

class backGrundImg(cocos.layer.Layer):
    #创建背景图层对象
    is_event_handler = True
    def __init__(self):
        super().__init__()
        bg = cocos.sprite.Sprite("GFX/bg.png")

        bg.position =(bg.width//2, bg.height//2)

        self.add(bg)

    def updata_scene(self):
        #更新屏幕场景
        main_scene = reset_scene_data()
        director.replace(main_scene)
    
    def on_mouse_press(self, x, y, button, modifiers):
        #当背景被点击即开始更新
        self.updata_scene()
        print("up")
        
class mainManu(cocos.menu.Menu):
    #开关浮动窗口
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
        items.append(cocos.menu.MenuItem("窗口3", self.window_3))
        items[2].x = items_x
        items[2].y = items_y
        items.append(cocos.menu.MenuItem("退出", self.exit))
        items[3].x = items_x
        items[3].y = items_y

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

    def window_3(self):
        if new_window3.visible == True:
            new_window3.closeWindow()
        else:
            new_window3.showWindow()

    def exit(self):
        director.window.close()
def reset_scene_data():
    global updataSceneList
    main_scene = cocos.scene.Scene()
    updataSceneList = [[backGrund, -100],[new_window, new_window.z],[new_window2, new_window2.z],[new_window3, new_window3.z], [mainMenu, 0]]
    for i in updataSceneList:
        main_scene.add(i[0],z = i[1])
        print(i[1])
    return main_scene


def get_scene():
    """
    说明：
        这是用来获取场景的函数
        return: cocos.scene.Scene对象
            返回所属场景文件的场景对象
    """
    main_scene = cocos.scene.Scene()
    
    global updataSceneList, backGrund, new_window, new_window2, new_window3, mainMenu

    updataSceneList = []
    new_window = floatingWindow.createFloatWindowLayer(30, 103, 150, 200, "浮动窗口")
    new_window2 = floatingWindow.createFloatWindowLayer(10, 40, 300, 200, "浮动窗口2")
    new_window3 = floatingWindow.createFloatWindowLayer(13, 30, 100, 400, "浮动窗口3")
    backGrund = backGrundImg()

    mainMenu = mainManu("主面板")

    main_scene = reset_scene_data()
    return main_scene