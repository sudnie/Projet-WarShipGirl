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
        main_scene = cocos.scene.Scene()
        updataSceneList = [[backGrund, -100],[new_window, new_window.z],[new_window2, new_window2.z],[new_window3, new_window3.z]]
        for i in updataSceneList:
            main_scene.add(i[0],z = i[1])
            print(i[1])
        director.replace(main_scene)
    
    def on_mouse_press(self, x, y, button, modifiers):
        global updataSceneList
        self.updata_scene(updataSceneList)
        print("up")
    


if __name__ == '__main__':

    director.init(1280, 720, 'warShipGirl')
    main_scene = cocos.scene.Scene()
    updataSceneList = []
    new_window = lib.floatingWindow.createFloatWindowLayer(30, 103, 150, 200, "浮动窗口")
    new_window2 = lib.floatingWindow.createFloatWindowLayer(10, 40, 150, 200, "浮动窗口2")
    new_window3 = lib.floatingWindow.createFloatWindowLayer(13, 30, 150, 200, "浮动窗口3")
    backGrund = backGrundImg()
    updataSceneList = [[backGrund, -100],[new_window, new_window.z],[new_window2, new_window2.z],[new_window3, new_window3.z]]
    for i in updataSceneList:
            main_scene.add(i[0],z = i[1])
            print(i[1])
            print('1ad')
    director.run(main_scene)