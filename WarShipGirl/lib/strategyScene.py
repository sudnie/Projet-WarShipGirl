"""
第二界面
"""
from cocos import text
from cocos.layer import scrolling
from cocos.text import Label
import lib.floatingWindow as floatingWindow
import cocos
from cocos.director import director
from cocos.actions.interval_actions import MoveTo 
from cocos.actions import *
from pyglet.window import key
from pyglet.window import mouse

class backGrundIMG(cocos.layer.Layer):
    
    bgw = 0
    bgh = 0
    def __init__(self):
        super().__init__()
        bg = cocos.layer.ColorLayer(100,100,100,255,width=10000,height=10000)
        self.bgw = bg.width
        self.bgh = bg.height
        bg.position = (self.bgw//2+500, self.bgh//2-400)
        self.add(bg)
    
    # def on_mouse_motion(self, x, y, dx, dy):
    #     """
    #     动态背景
    #     """
    #     #print(x,y)
    #     winW = director.window.width
    #     winH = director.window.height
    #     needX = (((x/winW)*100)-50)
    #     needY = (((y/winH)*100)-50)+100
    #     #print(needX, needY)
    #     self.do(MoveTo((needX, needY), 0.10))

    def on_mouse_press(self, x, y, button, modifiers):
        print(x,y)
        #必须的两行，负责更新场景图层的前后顺序
        main_scene = reset_scene_data()
        director.replace(main_scene)
        
class mainMenu(cocos.menu.Menu):
    def __init__(self, title):
        super().__init__(title=title)

        self.position = 400, 0
        #定义菜单列表
        items_x = 100
        items_y = 200
        items = []
        #加入选项
        items.append(cocos.menu.MenuItem("窗口1", self.A))
        items[0].x = items_x
        items[0].y = items_y
        items.append(cocos.menu.MenuItem("窗口2", self.B))
        items[1].x = items_x
        items[1].y = items_y
        items.append(cocos.menu.MenuItem("返回上级", self.changeScene))
        items[2].x = items_x
        items[2].y = items_y

        self.font_title['color'] = (0,0,0,255)
        self.font_item['color'] = (0,0,0,255)
        self.font_item_selected['color'] = (0,0,0,255)
        self.font_item_selected['font_size'] = 32


        self.create_menu(items)


    #这下面分别是不同窗口的开关控制函数
    def A(self):
        pass
    def B(self):
        pass

    def changeScene(self):
        director.pop()

class visualFocus(cocos.layer.ScrollableLayer):
    is_event_handler = True
    def __init__(self, parallax=1):
        super().__init__(parallax=parallax)

        focus = cocos.sprite.Sprite("GFX/ui/visualFocus.png")
        focus.position = (focus.width//2, focus.height//2)
        focus.velocity = (0,0)
        focus.do(VFMove())

        self.add(focus,name="vf")
        
    def on_key_press(self,key,modifiers):
        if key == 32:
            vfxy = self.get("vf").position
            print(vfxy)

            x = (vfxy[0]//32) * 32
            if vfxy[0]%32 <= 16:
                pass
            else:
                x = x + 32

            y = (vfxy[1]//32) * 32
            if vfxy[1]%32 <= 16:
                pass
            else:
                y = y + 32
            print(x,y)
            self.get("vf").position = (x,y)

class VFMove(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        vel_x = (keyboard[key.D] - keyboard[key.A]) * 500
        vel_y = (keyboard[key.W] - keyboard[key.S]) * 500
        if keyboard[65505] == True:
            vel_x, vel_y = vel_x * 2, vel_y * 2
        self.target.velocity = (vel_x, vel_y)
        #print(keyboard)
        #print(vel_x,vel_y)
        #print(self.target.position)
        #设置卷轴焦点
        scroller.set_focus(self.target.x, self.target.y)

class visualFocusText(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()
        self.VFText = cocos.text.Label(
            "",
            font_size = 32,
            anchor_x = "center",
            anchor_y = "center"
        )
        self.position = (1100, 50)
        self.add(self.VFText, name="text")
        self.do(Repeat(Delay(0.1)+CallFunc(self.updata)))
    def updata(self):
        xy = scroller.get("vfl").get("vf").position
        x = int(xy[0])
        y = int(xy[1])
        self.VFText.element.text = str(x)+"||"+str(y)


class report(cocos.actions.Action):
    def step(self, dt):
        super().step(dt)
        

class backgroundLayer():
    def __init__(self) -> None:
        bg = cocos.tiles.load("GFX/mapTiles/strategy/Smap.tmx")
        self.layer1 = bg["Y0"]
        self.layer2 = bg["Y1"]


def reset_scene_data():
    main_scene = cocos.scene.Scene()
    updataSceneList = [[scroller,-100],[vftext, 0],[Cmenu, 1]]
    for i in updataSceneList:
        main_scene.add(i[0],z = i[1])
        #print(i[1])
    return main_scene

def get_scene():
    """
    说明：
        这是用来获取场景的函数
        return: cocos.scene.Scene对象
            返回所属场景文件的场景对象
    """
    main_scene = cocos.scene.Scene()
    
    global updataSceneList, backGrund, timeUI, Cmenu, keyboard, scroller, vftext
    updataSceneList = []

    #设定键盘变量
    keyboard = key.KeyStateHandler()
    #读取键盘
    director.window.push_handlers(keyboard)

    bgLayer = backgroundLayer()
    VFlayer = visualFocus()

    scroller = cocos.layer.ScrollingManager()
    scroller.add(bgLayer.layer1)
    scroller.add(bgLayer.layer2)
    scroller.add(VFlayer, name="vfl")

    vftext = visualFocusText()

    # timeUI = timeLog()
    Cmenu = mainMenu("控制面板")
    main_scene = reset_scene_data()
    return main_scene


