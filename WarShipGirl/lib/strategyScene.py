"""
第二界面
"""
from typing import Type
from cocos import text
from cocos.layer import scrolling
from cocos.text import Label
from pyglet.graphics import NullGroup
import lib.floatingWindow as floatingWindow
import cocos
from cocos.director import director
from cocos.actions.interval_actions import MoveTo 
from cocos.actions import *
from pyglet.window import key
from pyglet.window import mouse
import lib.Objects as obj


class backGrundIMG(cocos.layer.Layer):
    is_event_handler = True
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

class replaceScene(cocos.layer.Layer):
    """
    说明：
        用来负责更新窗口的前后顺序。
    """
    is_event_handler = True
    def __init__(self):
        super().__init__()
        i = cocos.layer.ColorLayer(100,100,100,255,width=1280,height=720)
        i.position = (0,0)
        self.add(i)

    def on_mouse_press(self, x, y, button, modifiers):
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
        items.append(cocos.menu.MenuItem("移动", self.C))
        items[3].x = items_x
        items[3].y = items_y
        items.append(cocos.menu.MenuItem("移动2", self.D))
        items[4].x = items_x
        items[4].y = items_y

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
    def C(self):
        a.moveTo(1,1,1)
        print(a.xy[0])
    def D(self):
        a.moveTo(3,1,1)
        print(a.xy[0])

    def changeScene(self):
        director.pop()

class visualFocus(cocos.layer.ScrollableLayer):
    """
    焦点
    """
    xy = [0,0]
    is_event_handler = True
    def __init__(self, parallax=1):
        super().__init__(parallax=parallax)

        focus = cocos.sprite.Sprite("GFX/ui/visualFocus.png")
        focus.position = (0, 0)
        focus.velocity = (0,0)
        focus.do(VFMove())

        self.add(focus,name="vf")
        
    def on_key_press(self,key,modifiers):
        vfxy = self.get("vf").position
        #print(vfxy)
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

        self.setselfxy(x//32,y//32)
        #print(x,y)
        if key == 32:
            self.get("vf").position = (self.xy[0]*32,self.xy[1]*32)
            print(self.checkObj(self.xy[0],self.xy[1]))

    def checkObj(self,x,y):
        checkedlist = []
        print(self.xy)
        for i in range(len(objList)):
            objxy = objList[i].nowXY()
            print(objxy[0] == int(x),objxy[1] == int(y),"\n", a.name)
            if objxy[0] == int(x) and objxy[1] == int(y):
                vftext.check(objList[i])
                checkedlist.append(objList[i].name)
            else:
                vftext.check("reset")
        return "check:"+str(x)+"||"+str(y)+"\n"+str(checkedlist)+'in here'

    def setselfxy(self,x,y):
        self.xy = [x,y]
        return self.xy

class VFMove(cocos.actions.Move):
    """
    焦点移动控制
    """
    def step(self, dt):
        super().step(dt)
        vel_x = (keyboard[key.D] - keyboard[key.A]) * 100
        vel_y = (keyboard[key.W] - keyboard[key.S]) * 100
        if keyboard[65505] == True:
            vel_x, vel_y = vel_x * 10, vel_y * 10
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
        self.VFText2 = cocos.text.Label(
            "",
            font_size = 32,
            anchor_x = "center",
            anchor_y = "center"
        )
        self.VFText.position = (1100, 50)
        self.VFText2.position = (1100, 85)
        self.add(self.VFText, name="text")
        self.add(self.VFText2, name="text2")
        self.do(Repeat(Delay(0.1)+CallFunc(self.updata)))
    def updata(self):
        xy = scroller.get("vfl").get("vf").position
        x = int(xy[0])/32
        y = int(xy[1])/32
        self.VFText.element.text = str(x)+"||"+str(y)
    def check(self,obj):
        print(obj)
        if obj == "reset":
            self.VFText2.element.text = "not a Object"
        else:
            self.VFText2.element.text = "Object:%s"%obj.name

class backgroundLayer():
    def __init__(self) -> None:
        bg = cocos.tiles.load("GFX/mapTiles/strategy/Smap.tmx")
        self.layer1 = bg["Y0"]
        self.layer2 = bg["Y1"]


def reset_scene_data():
    """
    说明：
        这个函数的用途是将图层按顺序进行渲染并回传Scene
    """
    main_scene = cocos.scene.Scene()
    updataSceneList = [[rpS,-101], [scroller,-100],[vftext, 0] ,[Cmenu, 1], [new_window, new_window.z], [new_window2, new_window2.z], [a, 10]]
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
    
    global rpS, updataSceneList, backGrund, Cmenu, keyboard, scroller, vftext, objList, new_window, new_window2, a
    updataSceneList = []

    #设定键盘变量
    keyboard = key.KeyStateHandler()
    #读取键盘
    director.window.push_handlers(keyboard)

    a = obj.Objects("T1","GFX/mapTiles/Objects/Temporaryidentification.png" , xy=[2,0])

    bgLayer = backgroundLayer()
    VFlayer = visualFocus()

    scroller = cocos.layer.ScrollingManager()
    scroller.add(bgLayer.layer1)
    scroller.add(bgLayer.layer2)
    #scroller.add(a)
    scroller.add(VFlayer, name="vfl")
   

    vftext = visualFocusText()

    new_window = floatingWindow.createFloatWindowLayer(30, 103, 150, 200, "浮动窗口1")
    new_window2 = floatingWindow.createFloatWindowLayer(30, 140, 150, 200, "浮动窗口2")

    rpS = replaceScene()

    # timeUI = timeLog()
    Cmenu = mainMenu("控制面板")

    objList = []
    objList.append(a)
    main_scene = reset_scene_data()
    return main_scene


