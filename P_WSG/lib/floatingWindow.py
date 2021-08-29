import cocos
from cocos.actions.interval_actions import MoveTo
from cocos.director import director
from pyglet.window import mouse

#创建浮动窗口
class createFloatWindowLayer(cocos.layer.ColorLayer):
    is_event_handler = True
    dx = 0
    dy = 0
    #xy坐标，宽，高，名
    def __init__(self,x,y,size_width,size_height,name):
        #定义窗口
        super(createFloatWindowLayer,self).__init__(195,195,195,255,width=size_width,height=size_height)
        inWindow = cocos.layer.ColorLayer(100,100,100,255,width=size_width-10,height=size_height-50)
        inWindow.position = 5,0
        #定义窗口名
        txetLabel = cocos.text.Label(
            name,
            font_size = 20,
            anchor_x = "center",
            anchor_y = "center",
            color = (0, 0, 0, 255)
        )
        txetLabel.position = self.width//2 , self.height-25
        
        self.add(inWindow)
        self.add(txetLabel)
        self.position = x, y
        self.z = -1
        
    def mouse_on_layer(self,x,y):
        #判断鼠标是否点在了layer上
            if x < self.x + self.width and x > self.x and y < self.y + self.height and y > self.y:
                return True
            return False


    def on_mouse_press(self, x, y, button, modifiers):
        #鼠标是否点下
        if button & mouse.LEFT:
            if self.mouse_on_layer(x,y):
                self.z = 0
                print("updata z")
                print(self.z)
            else:
                self.z = self.z-1
    
    #窗口拖动相关
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            if self.mouse_on_layer(x,y) and self.z == 0:
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

    WindowLayer = createFloatWindowLayer(10,20,300,400,"实验性窗口")

    main_scene = cocos.scene.Scene()
    main_scene.add(WindowLayer)

    director.run(main_scene)

        