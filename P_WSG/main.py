import lib.floatingWindow
from cocos.director import director
import cocos








if __name__ == '__main__':

    director.init(1280, 720, 'warShipGirl')

    new_window = lib.floatingWindow.createWindowLayer(100, 200, "newwindow")
    main_scene = cocos.scene.Scene()
    main_scene.add(new_window)

    director.run(main_scene)
