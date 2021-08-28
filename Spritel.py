"""
学习用文件
"""




import cocos
from cocos.director import director
import pyglet

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
        
        self.add(spr)   
        



class Spritel2(cocos.sprite.Sprite):
    def __init__(self):
        #sprite可以直接读取图像
        super().__init__("img/01.png")
        
        self.position = 600, 360



if __name__ == '__main__':

    director.init(1280,720,'new')

    spr1_layer = Spritel()
    spr2_layer = Spritel2()
    
    #创建新的scene
    test_scene = cocos.scene.Scene()
    #将layer加入scenne
    test_scene.add(spr1_layer, name="1")
    test_scene.add(spr2_layer, name="player")
    

    director.run(test_scene)