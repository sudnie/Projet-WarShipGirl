from typing import ItemsView
import cocos
from cocos import menu
from cocos.director import director
import pyglet


class NewCamera(cocos.camera.Camera):
    def __init__(self):
        super().__init__()

        


#创建菜单图层
class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super().__init__('Game')

        img = pyglet.image.load("img/01.png")


        #定义菜单列表
        items = []
        #加入选项
        items.append(cocos.menu.MenuItem("Newgame", self.on_new_game))
        items.append(cocos.menu.MenuItem("Quit", self.on_quit))
        ##开关项
        items.append(cocos.menu.ToggleMenuItem("show FPS:", self.on_show_fps, director.show_FPS))

        items.append(cocos.menu.ImageMenuItem(img, self.on_img))
        self.create_menu(items)


    def on_new_game(self):
        print('start game')

    def on_quit(self):
        director.window.close()

    def on_show_fps(self, show_fps):
        print("Show FPS")
        director.show_FPS = show_fps

    def on_img(self):
        print('img')

if __name__ == "__main__":
    director.init(1280,720,'new')

    menu = MainMenu()

    test_scene = cocos.scene.Scene()
    test_scene.add(menu)

    director.run(test_scene)