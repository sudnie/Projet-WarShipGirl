"""
文件名：浮动窗口创建(floatingWindow.py)\n
介绍：
本文件用于创建基础浮动窗口对象。 \n
使用方法：
    createFloatWindowLayer()来创建对象即可。\n
    例：
        new_window = floatingWindow.createFloatWindowLayer(30, 103, 150, 200, "浮动窗口")
"""
import cocos
from cocos.actions.interval_actions import MoveTo
from cocos.director import director
from pyglet.window import mouse

#创建浮动窗口
class createFloatWindowLayer(cocos.layer.ColorLayer):
    """
    这是用于创建基础浮动窗口的对象
    """
    is_event_handler = True
    dx = 0
    dy = 0
    #xy坐标，宽，高，名
    def __init__(self,x,y,size_width,size_height,name):
        """
        说明：
            这是用于创建基础浮动窗口的方法
            x: int
                为窗口基础x轴位置
            y: int
                为窗口基础y轴位置
            size_width: int
                窗口的宽度(像素)
            size_height: int
                窗口的高度(像素)
            name: str
                窗口名称
        """


        self.show = True
        #定义窗口
        super(createFloatWindowLayer,self).__init__(242,255,245,170,width=size_width,height=size_height)
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
        
        closeWindowButton = cocos.layer.ColorLayer(214, 0, 10, 255, width = 25, height=25)
        closeWindowButton.position = self.width - 25, 0
    


        self.add(inWindow)
        self.add(txetLabel)
        self.add(closeWindowButton)
        self.position = x, y
        self.z = -1
        
    def mouse_on_layer(self,x,y):
        #判断鼠标是否点在了layer上
            if x < self.x + self.width and x > self.x and y < self.y + self.height and y > self.y:
                return True
            else:
                return False

    def mouse_on_closeButton(self,mouse_x,mouse_y):
        #判断xy位置是否在关闭按键上
        #print(mouse_x >= self.x + self.width - 25, mouse_x <= self.x + self.width, mouse_y >= self.y, mouse_y <= self.y + 25)
        if (mouse_x >= self.x + (self.width - 25) and mouse_x <= self.x + self.width) and (mouse_y >= self.y and mouse_y <= self.y + 25):
            return True
        else:
            return False

    def mouse_on_windowtitel(self,mouse_x,mouse_y):
        #鼠标是否在窗口标题
        if (mouse_x >= self.x and mouse_x <= self.x + self.width) and (mouse_y >= self.y + self.height - 50 and mouse_y <= self.y + self.height):
            return True
        else:
            return False

    def on_mouse_press(self, x, y, button, modifiers):
        #鼠标是否点下
        if button & mouse.LEFT:
            if self.mouse_on_layer(x,y):
                self.z = 0
                print("updata z")
                print(self.z)
                if self.mouse_on_closeButton(x,y):
                    self.closeWindow()
            else:
                self.z = self.z-1
    
    #窗口拖动相关
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            #print(self.mouse_on_windowtitel(x,y))
            if self.visible == True:
                if self.mouse_on_windowtitel(x,y) and self.z == 0:
                    if self.x+self.width < director.window.width and self.y+self.height < director.window.height and self.x > 0 and self.y > 0:
                        dx = dx * 1.05
                        dy = dy * 1.05
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

    def closeWindow(self):
        self.visible = False

    def showWindow(self):
        self.visible = True

        
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

        