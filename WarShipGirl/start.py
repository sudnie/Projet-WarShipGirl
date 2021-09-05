import cocos
from cocos.director import director
from pyglet import event
import lib.mainScene
import threading
import time

class timeThread(threading.Thread):
    def __init__(self, threadID, name,):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        global gameTime
        while director.window.has_exit != True:
            gameTime = lib.mainScene.updataTime()
            time.sleep(1)

if __name__ == "__main__" :
    
    director.init(1280, 720, "WarShipGirl")
    mainScene = lib.mainScene.get_scene()
    timeThr = timeThread(1, "time")
    timeThr.start()
    director.run(mainScene)