import cocos
from cocos.actions import *
from cocos.director import director
import pyglet
import lib.mainScene
import lib.strategyScene

class backGrundIMG(cocos.layer.Layer):
    is_event_handler = True
    bgw = 0
    bgh = 0
    def __init__(self):
        super().__init__()
        bg = cocos.sprite.Sprite("GFX/backGrund/illust_83257173_20200730_201353.png")
        self.bgw = bg.width
        self.bgh = bg.height
        bg.position = (self.bgw//2, self.bgh//2)
        self.add(bg)

class mainMenu(cocos.menu.Menu):
    def __init__(self, title):
        super().__init__(title=title)

        self.position = 400, 0
        #定义菜单列表
        items_x = 100
        items_y = 200
        items = []
        #加入选项
        items.append(cocos.menu.MenuItem("场景1", self.changeScene1))
        items[0].x = items_x
        items[0].y = items_y
        items.append(cocos.menu.MenuItem("场景2", self.changeScene2))
        items[1].x = items_x
        items[1].y = items_y


        self.font_title['color'] = (0,0,0,255)
        self.font_item['color'] = (0,0,0,255)
        self.font_item_selected['color'] = (0,0,0,255)
        self.font_item_selected['font_size'] = 32


        self.create_menu(items)

    def changeScene1(self):
        director.push(lib.mainScene.get_scene())

    def changeScene2(self):
        director.push(lib.strategyScene.get_scene())

def get_startScene():
    main_scene = cocos.scene.Scene()
    bg = backGrundIMG()
    menu1 = mainMenu("跳转接口")
    main_scene.add(menu1 , 10)
    main_scene.add(bg)
    return main_scene

if __name__ == "__main__" :
    
    director.init(1280, 720, "WarShipGirl")
    # timeThr = timeThread(1, "time")
    # timeThr.start()
    main_scene = get_startScene()
    director.run(main_scene)