from ctypes import create_string_buffer
import cocos
from cocos.actions.interval_actions import MoveBy, MoveTo
from cocos.director import director
from pyglet.window import mouse


class createWindowLayer(cocos.layer.ColorLayer):
    is_event_handler = True
    dx = 0
    dy = 0
    def __init__(self,size_x,size_y,name):
        super(createWindowLayer,self).__init__(195,195,195,255,width=size_x,height=size_y)

        inWindow = cocos.layer.ColorLayer(100,100,100,255,width=size_x-10,height=size_y-50)
        inWindow.position = 5,0
        
        txetLabel = cocos.text.Label(
            name,
            font_size = 30,
            anchor_x = "center",
            anchor_y = "center"
        )
        txetLabel.position = self.width//2 , self.height-25
        
        self.add(inWindow)
        self.add(txetLabel)
        self.position = 500, 200
        
    def mouse_on_layer(self,x,y):
        #判断鼠标是否点在了layer上
            if x < self.x + self.width and x > self.x and y < self.y + self.height and y > self.y:
                return True
            return False

#    def on_mouse_press(self, x, y, button, modifiers):
#        #鼠标是否点下
#        if button & mouse.LEFT:
#            if self.mouse_on_layer(x,y):
#                print('鼠标在上面')

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            if self.mouse_on_layer(x,y):
                dx = dx * 2
                dy = dy * 2
                if self.x+self.width < director.window.width and self.y+self.height < director.window.height and self.x > 0 and self.y > 0:
                    self.do(MoveTo((self.x+dx, self.y+dy),0))
                else:
                    if self.x+self.width >= director.window.width:
                        self.do(MoveTo((self.x-4, self.y+dy),0))
                    elif self.y+self.height >= director.window.height:
                        self.do(MoveTo((self.x+dx, self.y-4),0))
                    elif self.x <= 0:
                        self.do(MoveTo((self.x+4, self.y+dy),0))
                    elif self.y <= 0:
                        self.do(MoveTo((self.x+dx, self.y+4),0))

        
class windowMover(cocos.actions.Move):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def step(self, dt):
        super().step(dt)

        

if __name__ == "__main__":
    director.init(1280, 720, 'warShipGirl')

    WindowLayer = createWindowLayer(300,400,"实验性窗口")

    main_scene = cocos.scene.Scene()
    main_scene.add(WindowLayer)

    director.run(main_scene)

        