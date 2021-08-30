import cocos
import pyglet
from pyglet.window import mouse
from cocos.director import director

class backGrund(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()

        bg = cocos.sprite.Sprite("img/BG.png")

        bg.position =(bg.width//2, bg.height//2)

        self.add(bg)

    def on_mouse_press(self, x, y, button, modifiers):
        #鼠标是否点下
        if button & mouse.LEFT:
            print(x,y)



if __name__ == "__main__":
    director.init(1280,720,'new')

    backGrundIMG = backGrund()
    
    #创建新的scene
    test_scene = cocos.scene.Scene()
    #将layer加入scenne
    test_scene.add(backGrundIMG)
    #test_scene.add(spr2_layer, name="player")
    

    director.run(test_scene)