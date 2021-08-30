from cocos import menu
import lib.floatingWindow
from cocos.director import director
import cocos
from pyglet.window import mouse

class backGrundImg(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()
        bg = cocos.sprite.Sprite("GFX/bg.png")

        bg.position =(bg.width//2, bg.height//2)

        self.add(bg)

    def updata_scene(self, updataSceneList):
        #更新屏幕场景
        main_scene = cocos.scene.Scene()
        updataSceneList = [[backGrund, -100],[new_window, new_window.z],[new_window2, new_window2.z],[new_window3, new_window3.z], [menu, 0]]
        for i in updataSceneList:
            main_scene.add(i[0],z = i[1])
            print(i[1])
        director.replace(main_scene)
    
    def on_mouse_press(self, x, y, button, modifiers):
        #当背景被点击即开始更新
        global updataSceneList
        self.updata_scene(updataSceneList)
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

if __name__ == '__main__':

    director.init(1280, 720, 'warShipGirl')
    main_scene = cocos.scene.Scene()

    updataSceneList = []
    new_window = lib.floatingWindow.createFloatWindowLayer(30, 103, 150, 200, "浮动窗口")
    new_window2 = lib.floatingWindow.createFloatWindowLayer(10, 40, 150, 200, "浮动窗口2")
    new_window3 = lib.floatingWindow.createFloatWindowLayer(13, 30, 150, 200, "浮动窗口3")
    backGrund = backGrundImg()

    menu = mainManu("窗口控制")

    updataSceneList = [[backGrund, -100],[new_window, new_window.z],[new_window2, new_window2.z],[new_window3, new_window3.z], [menu, 0]]


    for i in updataSceneList:
            main_scene.add(i[0],z = i[1])
            print(i[1])
            print('1ad')
    director.run(main_scene)