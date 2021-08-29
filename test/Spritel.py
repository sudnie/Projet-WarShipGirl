"""
学习用文件
2021/8/29
"""
import cocos
from cocos.director import director
import pyglet
from pyglet.window import key


#移动动作class
class Mover(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        print(keyboard)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)

        #设置卷轴焦点
        scorller.set_focus(self.target.x, self.target.y)
        


#创建一个卷轴图层（精灵）
class player(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()

        #pyglet读取图片
        img = pyglet.image.load("img\Eship.png")
        #pyglet图片网格化
        img_grid = pyglet.image.ImageGrid(img, 1, 5, item_width=100, item_height=100)

        #print(img_grid[0:])

        #将网格图片变成gif动图
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.05, loop=True)
        
        #将动图加入图层（laeyr）
        spr = cocos.sprite.Sprite(anim)
        #spr.position = 400, 360

        #设定图层速度
        spr.velocity = (0,0)
        #执行移动
        spr.do(Mover())

        self.add(spr)   

#创建卷轴图片背景
class BackgroundLayerIMG(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()

        bg = cocos.sprite.Sprite("img/BG.png")
        #设定背景锚点
        #bg.position = (1500, 600)
        bg.position =(bg.width//2, bg.height//2)

        #设定背景卷轴大小
        #self.px_width = 3000
        #self.px_height = 1200
        self.px_width, self.px_height = bg.width, bg.height

        
        self.add(bg)

class Spritel2(cocos.sprite.Sprite):
    def __init__(self):
        #sprite可以直接读取图像
        super().__init__("img/01.png")
        
        self.position = 600, 360

#创建卷轴tiles图层（背景）
class BackgroundLayer():
    def __init__(self):
        #读取tiled文件
        bg = cocos.tiles.load("map/map.tmx")
        #读取并定义tiles图层
        self.layer1 = bg['layer1']

if __name__ == '__main__':

    director.init(1280,720,'new')
    
    #设定键盘变量
    keyboard = key.KeyStateHandler()
    #读取键盘
    director.window.push_handlers(keyboard)
    
    player_layer = player()
    spr2_layer = Spritel2()
    bg_layer = BackgroundLayer()

    #定义卷轴，并将两个卷轴图层加入卷轴
    scorller = cocos.layer.ScrollingManager()
    scorller.add(bg_layer.layer1)
    scorller.add(player_layer)
    
    #创建新的scene
    test_scene = cocos.scene.Scene()
    #将layer加入scenne
    test_scene.add(scorller)
    #test_scene.add(spr2_layer, name="player")
    

    director.run(test_scene)