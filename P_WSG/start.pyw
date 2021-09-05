import cocos
import threading
import time
from cocos.director import director
import lib.experimentalScene as experimentalScene

class timeThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        while director.window.has_exit != True:
            print(time.ctime(time.time()))
            time.sleep(1)


if __name__ == "__main__" :

    director.init(1280, 720, 'warShipGirl')
    timeThr = timeThread(1, "time", 0)
    timeThr.start()
    print(director.window.has_exit)
    director.run(experimentalScene.get_scene())
    print(director.window.has_exit)