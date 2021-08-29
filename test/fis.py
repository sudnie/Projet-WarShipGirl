import cocos
from cocos import layer
from cocos.director import director

class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        label = cocos.text.Label(
            "HelloWorld",
            font_size = 32,
            anchor_x = "center",
            anchor_y = "center"
        )
        #获取窗口大小
        size = director.get_window_size()
        
        #设置label位置
        label.position = size[0]/2, size[1]/2
        
        #将label加入图层
        self.add(label)

if __name__ == '__main__':

    director.init(1280,720,'new')
    hello_layer = HelloWorld()
    test_scene = cocos.scene.Scene(hello_layer)

    director.run(test_scene)