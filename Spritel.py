"""
学习用文件
2021/8/29
"""


import cocos
from cocos.director import director
import pyglet
from pyglet.window import key


#移动class
class Mover(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        print(keyboard)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)
        



class Spritel(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        #pyglet读取图片
        img = pyglet.image.load("img\Eship.png")
        #pyglet图片网格化
        img_grid = pyglet.image.ImageGrid(img, 1, 5, item_width=100, item_height=100)

        #print(img_grid[0:])

        #将网格图片变成gif动图
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)
        
        #将动图加入图层（laeyr）
        spr = cocos.sprite.Sprite(anim)
        spr.position = 400, 360

        #设定图层速度
        spr.velocity = (0,0)
        #执行移动
        spr.do(Mover())

        self.add(spr)   
        

class Spritel2(cocos.sprite.Sprite):
    def __init__(self):
        #sprite可以直接读取图像
        super().__init__("img/01.png")
        
        self.position = 600, 360

class BackgroundLayer(cocos.layer.ScrollableLayer):
    def __init__(self, parallax):
        super().__init__(parallax=parallax)



if __name__ == '__main__':

    director.init(1280,720,'new')
    
    #设定键盘变量
    keyboard = key.KeyStateHandler()
    #读取键盘
    director.window.push_handlers(keyboard)
    

    
    spr1_layer = Spritel()
    spr2_layer = Spritel2()
    
    #创建新的scene
    test_scene = cocos.scene.Scene()
    #将layer加入scenne
    test_scene.add(spr1_layer, name="1")
    #test_scene.add(spr2_layer, name="player")
    

    director.run(test_scene)