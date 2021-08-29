import lib.floatingWindow
from cocos.director import director
import cocos

class backGrundImg(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        bg = cocos.sprite.Sprite("GFX/bg.png")

        bg.position =(bg.width//2, bg.height//2)

        self.add(bg)






if __name__ == '__main__':

    director.init(1280, 720, 'warShipGirl')
    main_scene = cocos.scene.Scene()
    updataSceneList = []
    new_window = lib.floatingWindow.createFloatWindowLayer(30, 103, 150, 200, "浮动窗口")
    new_window2 = lib.floatingWindow.createFloatWindowLayer(10, 40, 150, 200, "浮动窗口2")
    new_window3 = lib.floatingWindow.createFloatWindowLayer(13, 30, 150, 200, "浮动窗口3")
    backGrund = backGrundImg()
    updataSceneList=(backGrund,new_window,new_window2,new_window3)
    for i in updataSceneList:
        main_scene.add(i)

    director.run(main_scene)
